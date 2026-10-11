from functools import lru_cache
from sentence_transformers import SentenceTransformer

@lru_cache(maxsize=1)
def get_embedding_model():
    return SentenceTransformer(
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

def embed_text(text: str) -> list[float]:
    
    model = get_embedding_model()
    
    vector = model.encode(
        text,
        normalize_embeddings=True,
    )
    
    return vector.tolist()