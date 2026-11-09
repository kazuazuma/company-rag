from fastapi import APIRouter, HTTPException

from app.schemas.rag import RAGRequest
from app.services.rag_graph import ask_rag

router = APIRouter(
    prefix="/rag",
    tags=["RAG"],
)

@router.post("/ask")
def ask_question(
    request: RAGRequest,
):
    
    try:
        return ask_rag(
            question=request.question,
        )
    
    except ValueError as e:
        raise HTTPException(
            status_code=503,
            detail=str(e),
        )