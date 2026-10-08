from fastapi import APIRouter, HTTPException
from app.schemas.rag import RAGRequest
from rag.rag_service import generate_answer

router = APIRouter(
    prefix="/rag",
    tags=["RAG"],
)

@router.post("/ask")
def ask_question(request: RAGRequest):
    
    try:
        return generate_answer(
            request.question
        )
    
    except ValueError as e:
        raise HTTPException(
            status_code=503,
            detail=str(e),
        )