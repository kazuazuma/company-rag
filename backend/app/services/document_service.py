from sqlalchemy.orm import Session

from app.repositories.document_repository import save_document
from app.services.embedding_service import embed_text
from app.repositories.document_repository import (search_similar_documents,)

def search_documents(
    db: Session,
    question: str,
    top_k : int = 3,
):
    query_vector = embed_text(question)
    
    rows = search_similar_documents(
        db=db,
        query_vector=query_vector,
        top_k=top_k,
    )
    
    results = []
    
    for document, distance in rows:
        results.append({
            "id": document.id,
            "title": document.title,
            "content": document.content,
            "score": 1.0 - float(distance),
        })
    return results

def create_document(
    db: Session,
    title: str,
    content: str,
):
    
    embedding = embed_text(content)
    
    return save_document(
        db=db,
        title=title,
        content=content,
        embedding=embedding,
    )