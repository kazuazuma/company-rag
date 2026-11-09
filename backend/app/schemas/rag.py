from pydantic import BaseModel, Field

class RAGRequest(BaseModel):
    
    question: str = Field(
        min_length=1,
        description="質問文",
    )