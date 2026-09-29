from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.product import Product
from app.repositories.product_repository import(
    find_all,
    find_by_id,
    update,
    delete,
    save,
)

def get_products(db: Session,):
    return find_all(db)

def get_product(
    db: Session,
    product_id: int,
):
    product = find_by_id(
        db,
        product_id,
    )
    
    if product is None:
        raise HTTPException(
            status_code=404,
            detail="product not found",
        )
        
    return product

def create_product(
    db: Session,
    name: str,
    price: int,
    description: str | None,
):
    
    product = Product(
        name=name,
        price=price,
        description = description,
    )
    
    return save(
        db,
        product,
    )
    
def update_product(
    db: Session,
    product_id: int,
    name: str | None,
    price: int | None,
    description: str | None,
):
    product = find_by_id(
        db,
        product_id,
    )
    
    if product is None:
        raise HTTPException(
            status_code=404,
            detail="product not found",
        )
    
    if name is not None:
        product.name = name
        
    if price is not None:
        product.price = price
        
    if description is not None:
        product.description = description
    
    return update(
        db,
        product,
    )
    
def delete_product(
    db: Session,
    product_id: int
):

    product = find_by_id(
        db,
        product_id
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )
    
    delete(
        db,
        product,
    )

    return {
        "message": "product deleted"
    }