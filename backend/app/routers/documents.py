from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.document import DocumentCreate, DocumentSearch
from app.services.document_service import (
    create_document,
    search_documents,
)

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)

@router.post("", status_code=201)
def add_document(
    request: DocumentCreate,
    db: Session = Depends(get_db),
):
    document = create_document(
        db=db,
        title=request.title,
        content=request.content,
    )
    
    return {
        "id": document.id,
        "title": document.title,
        "content": document.content,
    }
    
@router.post("/search")
def search(
    request: DocumentSearch,
    db: Session = Depends(get_db),
):
    return search_documents(
        db=db,
        question=request.question,
        top_k=request.top_k,
    )
    
    