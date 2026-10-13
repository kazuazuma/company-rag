from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.services.document_service import search_documents
from app.services.llm_service import generate_with_langchain

class RAGState(TypedDict):
    question: str
    documents : list[dict]
    answer: str

def retrieve_node(state: RAGState) -> dict:
    
    with SessionLocal() as db:
        
        documents = search_documents(
            db=db,
            question=state['question'],
            top_k=3,
        )
    return{
        "documents" : documents
    }

def generate_node(state: RAGState) -> dict:
    
    documents = state['documents']
    
    if not documents:
        return{
            "answer": "関連する資料が見つかりません。"
        }
        
    context = "\n\n".join(
        f"[資料ID: {doc['id']}]\n"
        f"タイトル: {doc['title']}\n"
        f"本文: {doc['content']}\n"
        for doc in documents
    )
    
    answer = generate_with_langchain(
        question=state['question'],
        context=context,
    )
    
    return {
        "answer": answer
    }
    
builder = StateGraph(RAGState)

builder.add_node("retriever", retrieve_node)
builder.add_node("generate", generate_node)

builder.add_edge(START, "retriever")
builder.add_edge("retriever", "generate")
builder.add_edge("generate", END)

rag_graph = builder.compile()

def ask_rag(question: str) -> dict:
    
    result = rag_graph.invoke(
        {
            "question": question,
            "documents": [],
            "answer": "",
        }
    )
    
    return {
        "answer": result["answer"],
        "sources": result["documents"],
    }