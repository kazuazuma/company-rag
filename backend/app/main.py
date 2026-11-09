from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine
from app.models.product import Product
from app.routers.products import router as products_router
from app.routers import products, rag, documents

app = FastAPI(
    title="Company RAG API"
)

app.include_router(products_router)
app.include_router(rag.router)
app.include_router(documents.router)

@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }

app.add_middleware(
    CORSMiddleware,
    
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    
    allow_credentials=False,
    
    allow_methods=["GET", "POST"],
    
    allow_headers=["Content-Type"],
)