from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from app.database import get_db
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

@router.get("")
def read_products(
    db:Session = Depends(get_db),
):
    return get_products(db)

@router.get("/{product_id}")
def read_product(
    product_id: int,
    db: Session = Depends(get_db),
):
    return get_product(
        db,
        product_id,
    )

@router.post("", status_code=201)
def add_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
):
    return create_product(
        db = db,
        name= product.name,
        price= product.price,
        description=product.description,
    )

@router.patch("/{product_id}")
def patch_product(
    product_id: int,
    product: ProductUpdate,
    db: Session = Depends(get_db),
):
    return update_product(
        db = db,
        product_id=product_id,
        name=product.name,
        price=product.price,
        description=product.description,
    )

@router.delete("/{product_id}")
def remove_product(
    product_id: int,
    db: Session = Depends(get_db),
):

    return delete_product(
        db,
        product_id
    )