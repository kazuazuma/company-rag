from fastapi import APIRouter

from app.schemas.product import ProductCreate,ProductUpdate
from app.services.product_service import(
    get_product,
    create_product,
    get_products,
    update_product,
    delete_product,
)

router = APIRouter(
    prefix="/products",
    tags=["products"],
)

@router.get("/{product_id}")
def read_product(product_id: int):
    return get_product(product_id)

@router.post("", status_code=201)
def add_product(product: ProductCreate):
    return create_product(
        name= product.name,
        price= product.price,
    )

@router.get("")
def read_products():
    return get_products()

@router.patch("/{product_id}")
def patch_product(
    product_id: int,
    product: ProductUpdate,
):
    return update_product(
        product_id=product_id,
        name=product.name,
        price=product.price,
    )

@router.delete("/{product_id}")
def delete_product_route(product_id: int):

    return delete_product(product_id)