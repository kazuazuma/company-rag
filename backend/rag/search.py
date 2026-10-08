import numpy as np
from sentence_transformers import SentenceTransformer

model = SentenceTransformer(
    "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
)

documents = [
    "有給休暇は原則3営業日前までに申請してください。",
    "交通費は毎月末日までに経費精算してください。",
    "リモートワークは週3日まで認められています。",
    "会社支給のパソコンには必ず画面ロックを設定してください。",
]

document_vectors = model.encode(
    documents,
    normalize_embeddings=True,
)

def search_documents(query: str, top_k: int = 2):
    
    query_vector = model.encode(
        query,
        normalize_embeddings=True,
    )
    
    scores = np.dot(
        document_vectors,
        query_vector,
    )
    
    top_indices = np.argsort(scores)[::-1][:top_k]
    
    results = []
    
    for index in top_indices:
        results.append({
            "document": documents[index],
            "score": float(scores[index]),
        })
        
    return results

if __name__ == "__main__":
    
    query = "有給休暇はいつまでに申請すればいい？"
    
    results = search_documents(query)
    
    for result in results:
        print(result)