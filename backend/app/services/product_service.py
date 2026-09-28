from fastapi import HTTPException

from app.repositories.product_repository import(
    find_all,
    save,
    count,
    find_by_id,
    update,
    delete,
)

def get_product(product_id: int):
    product = find_by_id(product_id)
    
    if product is None:
        raise HTTPException(
            status_code=404,
            detail="product not found",
        )
        
    return product

def create_product(name: str, price: int):
    new_id = count() + 1
    
    new_product = {
        "id": new_id,
        "name": name,
        "price": price,
    }
    
    return save(new_product)

def get_products():
    return find_all()

def update_product(
    product_id: int,
    name: str,
    price: int,
):
    product = find_by_id(product_id)
    
    if product is None:
        raise HTTPException(
            status_code=404,
            detail="product not found",
        )
    
    update_product = {
        "id" : product_id,
        "name": name,
        "price": price,
    }
    
    return update(
        product_id,
        update_product,
    )
    
def delete_product(product_id: int):

    product = find_by_id(product_id)

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found",
        )

    return delete(product_id)