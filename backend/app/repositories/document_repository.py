from sqlalchemy.orm import Session
from app.models.document import Document
from sqlalchemy import select

def search_similar_documents(
    db: Session,
    query_vector: list[float],
    top_k: int = 3,
):
    distance = Document.embedding.cosine_distance(
        query_vector
    )
    
    statement = (
        select(
            Document,
            distance.label("distance"),
        )
        .order_by(distance)
        .limit(top_k)
    )
    
    return db.execute(statement).all()

def save_document(
    db: Session,
    title: str,
    content: str,
    embedding: list[float],
) -> Document:
    
    document = Document(
        title=title,
        content=content,
        embedding= embedding,
    )
    
    try:
        db.add(document)
        
        db.commit()
        
        db.refresh(document)
        
        return document
    
    except Exception:
        db.rollback()
        raise