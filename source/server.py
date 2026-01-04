import json
import asyncio
from typing import TypedDict, List, Annotated
import operator
from contextlib import asynccontextmanager
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from pydantic import BaseModel, Field
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import InMemorySaver
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
from langchain_core.runnables import RunnableConfig

from src.llm_handler import build_llm_provider, BaseLLMProvider
from src.db_handler import QdrantRetriever
from src.prompts import query_analyzer_prompt, question_generator_prompt
from src.log_setup import log

class SubQueries(BaseModel):
    queries: List[str] = Field(description="List of simple queries derived from the user query.")

# --- Graph State Definition ---
class GraphState(TypedDict):
    query: str
    queries: List[str]
    context: str
    history: Annotated[List[BaseMessage], operator.add]
    past_queries: Annotated[List[str], operator.add]
    answer: str


async def analyzer_node(state: GraphState, config: RunnableConfig):
    """Stage 1: Decompose query into sub-questions for better retrieval"""
    log.info("Node: Analyzer - Decomposing user query")

    llm: BaseLLMProvider = config["configurable"]["llm_provider"]

    # Format the past queries as a simple bullet list string
    past_queries_str = "\n".join([f"- {q}" for q in state.get("past_queries", [])]) if state.get("past_queries") else "None"
    
    # Generate sub-queries using structured output
    res = await llm.structured(
        prompt=query_analyzer_prompt.format(
            user_query=state["query"],
            past_queries=past_queries_str,
            given_schema=json.dumps(SubQueries.model_json_schema())
        ),
        extract_schema=SubQueries,
        temperature=0.0
    )
    
    sub_queries = res.queries if hasattr(res, 'queries') else [state["query"]]
    log.info(f"Sub-queries generated: {sub_queries}")
    return {"queries": sub_queries, "past_queries": [state["query"]]}

async def retriever_node(state: GraphState):
    """Stage 2: Fetch context for all sub-queries from Qdrant"""
    queries = state.get("queries", [state["query"]])
    retriever = QdrantRetriever()
    
    # Run retrieval for all queries in parallel
    tasks = [asyncio.to_thread(retriever.get_context, q) for q in queries]
    contexts = await asyncio.gather(*tasks)
    
    combined_context = "\n\n---\n\n".join(list(set(contexts)))
    return {"context": combined_context}

async def answer_node(state: GraphState, config: RunnableConfig):
    """Stage 3: Generate final answer and update history"""
    log.info("Node: Answer - Generating response")
    llm: BaseLLMProvider = config["configurable"]["llm_provider"]
    
    # Format the Prompt
    prompt_value = question_generator_prompt.format(
        context=state["context"],
        chat_history=state.get("history", []),
        user_query=state["query"]
    )
    
    # Generate full response (buffered)
    response = await llm.generate(prompt=prompt_value, temperature=0.3)
    
    # Create message objects to save to history
    new_history = [
        HumanMessage(content=state["query"]),
        AIMessage(content=response)
    ]
    
    # Return answer AND update history in one go
    return {"answer": response, "history": new_history}

# Graph Setup

workflow = StateGraph(GraphState)
workflow.add_node("analyzer", analyzer_node)
workflow.add_node("retriever", retriever_node)
workflow.add_node("answer", answer_node)

workflow.set_entry_point("analyzer")
workflow.add_edge("analyzer", "retriever")
workflow.add_edge("retriever", "answer")
workflow.add_edge("answer", END)

# Persistence layer
memory = InMemorySaver()
graph = workflow.compile(checkpointer=memory)


@asynccontextmanager
async def lifespan(app: FastAPI):

    log.info("Lifespan: Initializing LLM Provider...")
    app.state.llm = build_llm_provider()
    yield

    log.info("Lifespan: Shutting down...")

app = FastAPI(lifespan=lifespan)


@app.post("/stream")
async def stream_endpoint(request: Request):
    body = await request.json()
    thread_id = body.get("thread_id", "default")
    is_continue = body.get("is_continue", True)
    
    # 1. Prepare Config
    config = {
        "configurable": {
            "thread_id": thread_id,
            "llm_provider": request.app.state.llm
        }
    }

    # 2. Handle History Flush if new session
    if not is_continue:
        log.info(f"Resetting history for thread {thread_id}")
        await graph.aupdate_state(config, {"history": [], "past_queries": []})

    # 3. Stream Graph Updates
    async def event_generator():
        async for event in graph.astream(
            {"query": body["query"]},
            config=config,
            stream_mode="updates" 
        ):
            node_name = list(event.keys())[0]
            data = event[node_name]
            
            if node_name == "answer":
                # Send the final answer text
                yield f"data: {json.dumps({'text': data['answer']})}\n\n"
            elif node_name == "analyzer":
                log.debug(f"Analyzer finished: {data['queries']}")
            elif node_name == "retriever":
                log.debug(f"Retriever finished with context length: {len(data['context'])}")

    return StreamingResponse(event_generator(), media_type="text/event-stream")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)