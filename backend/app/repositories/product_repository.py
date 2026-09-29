from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.product import Product

def find_all(db: Session):
    
    statement = select(Product)
    
    return db.scalars(statement).all()
    
def find_by_id(
    db: Session,
    product_id: int,
):
    return db.get(Product, product_id)
    
def save(
    db: Session,
    product: Product,
):
    try:
        db.add(product)
        
        db.commit()
        
        db.refresh(product)
    
        return product
    
    except Exception:
        
        db.rollback()
        
        raise
    
def update(
    db: Session,
    product: Product,
):
    db.commit()
    db.refresh(product)
    
    return product
    
def delete(
    db: Session,
    product: Product,
):

    db.delete(product)
    db.commit()

