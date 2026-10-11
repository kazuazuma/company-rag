from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.rag import RAGRequest
from rag.rag_service import generate_answer

router = APIRouter(
    prefix="/rag",
    tags=["RAG"],
)

@router.post("/ask")
def ask_question(
    request: RAGRequest,
    db: Session = Depends(get_db),
):
    
    try:
        return generate_answer(
            db=db,
            question=request.question,
        )
    
    except ValueError as e:
        raise HTTPException(
            status_code=503,
            detail=str(e),
        )