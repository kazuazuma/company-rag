from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column
from pgvector.sqlalchemy import Vector

from app.database import Base

class Document(Base):
    __tablename__ = "documents"
    
    id: Mapped[int] = mapped_column(
        primary_key=True
    )
    
    title: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )
    
    content: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )
    
    embedding: Mapped[list[float]] = mapped_column(
        Vector(384),
        nullable=False,
    )