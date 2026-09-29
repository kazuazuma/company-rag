from fastapi import FastAPI

from app.database import Base, engine
from app.models.product import Product
from app.routers.products import router as products_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(products_router)

@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }