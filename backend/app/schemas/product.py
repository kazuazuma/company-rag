from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: int
    description: str | None = None
    
class ProductUpdate(BaseModel):
    name: str | None = None
    price: int | None = None
    description: str | None = None