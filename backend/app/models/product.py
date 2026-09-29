from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base

class Product(Base):
    
    __tablename__ = "products"
    
    id: Mapped[int] = mapped_column(
        primary_key=True
    )
    
    name: Mapped[str] = mapped_column(
        String(100)
    )
    
    price: Mapped[int] = mapped_column()
    
    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )