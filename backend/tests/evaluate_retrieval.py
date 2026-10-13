from app.database import SessionLocal
from app.services.document_service import search_documents

from tests.evaluation_cases import evaluation_cases

def evaluate_retrieval():
    
    hits = 0
    
    with SessionLocal() as db:
        
        for case in evaluation_cases:
            
            results = search_documents(
                db=db,
                question=case["question"],
                top_k=3,
            )
            
            retrieved_ids = [
                doc["id"]
                for doc in results
            ]
            
            if case["expected_document_id"] in retrieved_ids:
                hits += 1
    
    hit_rate = hits / len(evaluation_cases)
    
    print(f"hit rate@3: {hit_rate: .2%}")
    
if __name__ == "__main__":
    evaluate_retrieval()