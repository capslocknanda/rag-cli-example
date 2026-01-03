import json
import time
from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from typing import TypedDict, List, Annotated
import operator
from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import InMemorySaver

from src.llm_handler import load_lm, InputGuardrail, VSRagSignature
from src.db_handler import QdrantRetriever
from src.log_setup import log
import dspy


class GraphState(TypedDict):
    query: str
    is_continue: bool
    is_safe: bool
    context: str
    history: Annotated[List[dict], operator.add]
    answer: str


def guardrail_node(state: GraphState):
    log.info("Node: Guardrail - Checking query safety")
    checker = dspy.Predict(InputGuardrail)
    res = checker(query=state["query"])
    return {"is_safe": res.is_safe, "answer": res.reason if not res.is_safe else ""}

def retriever_node(state: GraphState):
    query = state["query"]
    log.info(f"Node: Retriever - Fetching context from Qdrant for query: '{query}'")
    start_time = time.perf_counter()
    retriever = QdrantRetriever()
    context = retriever.get_context(query)
    duration = time.perf_counter() - start_time
    log.debug(f"Retriever raw context output for query '{query}':\n---\n{context}\n---")
    log.info(f"Node: Retriever - Retrieved in {duration:.4f}s | Query: '{query}' | Context length: {len(context)}")
    return {"context": context}

def generator_node(state: GraphState):
    log.info("Node: Generator - Synthesizing response")
    start_time = time.perf_counter()
    prog = dspy.ChainOfThought(VSRagSignature)
    
    log.debug(f"Generator inputs:\n- Query: {state['query']}\n- History: {state['history']}\n- Context:\n---\n{state['context']}\n---")
    
    with dspy.context(config=dict(temperature=0.7, max_tokens=2048)):
        res = prog(
            context=state["context"], 
            question=state["query"], 
            history=state["history"]
        )

    duration = time.perf_counter() - start_time
    log.debug(f"Generator raw output:\n---\n{res}\n---")
    log.info(f"Node: Generator - Response generated in {duration:.4f}s | Answer: {res.answer}")
    
    new_history = [{"user": state["query"], "assistant": res.answer}]
    return {"answer": res.answer, "history": new_history}

workflow = StateGraph(GraphState)
workflow.add_node("guardrail", guardrail_node)
workflow.add_node("retriever", retriever_node)
workflow.add_node("generator", generator_node)

workflow.set_entry_point("guardrail")

workflow.add_conditional_edges(
    "guardrail", 
    lambda x: "retriever" if x["is_safe"] else END
)
workflow.add_edge("retriever", "generator")
workflow.add_edge("generator", END)

memory = InMemorySaver()
graph = workflow.compile(checkpointer=memory)

app = FastAPI()
load_lm()

@app.post("/stream")
async def stream_endpoint(request: Request):
    body = await request.json()
    config = {"configurable": {"thread_id": body.get("thread_id", "default")}}
    
    # Reset history if is_continue is False
    if not body.get("is_continue"):
        memory.storage.pop(config["configurable"]["thread_id"], None)

    async def event_generator():
        async for event in graph.astream(
            {"query": body["query"], "is_continue": body.get("is_continue")},
            config=config,
            stream_mode="updates"
        ):
            node_name = list(event.keys())[0]
            data = event[node_name]
            
            if node_name == "generator":
                yield f"data: {json.dumps({'text': data['answer']})}\n\n"
            else:
                log.debug(f"Status update from {node_name}: {data}")

    return StreamingResponse(event_generator(), media_type="text/event-stream")


if __name__ == "__main__":
    import uvicorn
    from src.log_setup import log

    log.info("Starting ViewSonic Software RAG Server...")
    
    uvicorn.run(app, host="0.0.0.0", port=8000)