import json
import asyncio
from typing import TypedDict, List, Annotated
import operator

from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage

# Import your custom handlers from the files you provided
from src.llm_handler import build_llm_provider
from src.db_handler import QdrantRetriever
from src.prompts import query_analyzer_prompt, question_generator_prompt
from src.log_setup import log

# --- Schema for Stage 1 (Structured Output) ---
class SubQueries(BaseModel):
    queries: List[str] = Field(description="List of search queries for the vector database")

# --- Graph State Definition ---
class GraphState(TypedDict):
    query: str
    queries: List[str]
    context: str
    # 'operator.add' allows history to persist and append across turns
    history: Annotated[List[BaseMessage], operator.add]

# --- Node Functions ---

async def analyzer_node(state: GraphState):
    """Stage 1: Decompose query into sub-questions for better retrieval"""
    log.info("Node: Analyzer - Decomposing user query")
    llm = build_llm_provider()
    
    # Generate sub-queries using structured output
    res = await llm.structured(
        prompt=query_analyzer_prompt.format(
            user_query=state["query"],
            given_schema=json.dumps(SubQueries.model_json_schema())
        ),
        extract_schema=SubQueries,
        temperature=0.0
    )
    
    sub_queries = res.queries if hasattr(res, 'queries') else [state["query"]]
    log.info(f"Sub-queries generated: {sub_queries}")
    return {"queries": sub_queries}

async def retriever_node(state: GraphState):
    """Stage 2: Fetch context for all sub-queries from Qdrant"""
    queries = state.get("queries", [state["query"]])
    retriever = QdrantRetriever()
    
    # Run retrieval for all queries in parallel
    tasks = [asyncio.to_thread(retriever.get_context, q) for q in queries]
    contexts = await asyncio.gather(*tasks)
    
    # Join unique context chunks
    combined_context = "\n\n---\n\n".join(list(set(contexts)))
    return {"context": combined_context}

# --- Graph Construction ---
workflow = StateGraph(GraphState)
workflow.add_node("analyzer", analyzer_node)
workflow.add_node("retriever", retriever_node)

workflow.set_entry_point("analyzer")
workflow.add_edge("analyzer", "retriever")
workflow.add_edge("retriever", END)

# Persistence layer
memory = InMemorySaver()
graph = workflow.compile(checkpointer=memory)

app = FastAPI()

@app.post("/stream")
async def stream_endpoint(request: Request):
    body = await request.json()
    thread_id = body.get("thread_id", "default")
    user_query = body["query"]
    is_continue = body.get("is_continue", True)
    
    config = {"configurable": {"thread_id": thread_id}}
    llm = build_llm_provider()

    # --- Handle is_continue logic ---
    if not is_continue:
        log.info(f"Flushing chat history for thread: {thread_id}")
        # We update the state to have an empty list for history
        # This effectively "resets" the memory for this thread
        await graph.aupdate_state(config, {"history": []})

    # 1. Run the Graph (Stage 1 & 2) to prepare context
    # Note: We pass an empty dict for history here because the checkpointer 
    # will automatically load the existing history for this thread_id.
    final_state = await graph.ainvoke({"query": user_query}, config=config)
    
    # 2. Extract current history for the prompt
    current_history = final_state.get("history", [])

    # 3. Format the Generator Prompt
    prompt_value = question_generator_prompt.format(
        context=final_state["context"],
        chat_history=current_history,
        user_query=user_query
    )

    async def event_generator():
        full_response = ""
        # 4. Stream output using the custom stream_generate method
        async for chunk in llm.stream_generate(prompt=prompt_value, temperature=0.3):
            full_response += chunk
            yield f"data: {json.dumps({'text': chunk})}\n\n"
        
        # 5. Save the turn back to the graph's history
        new_messages = [
            HumanMessage(content=user_query),
            AIMessage(content=full_response)
        ]
        await graph.aupdate_state(config, {"history": new_messages})

    return StreamingResponse(event_generator(), media_type="text/event-stream")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)