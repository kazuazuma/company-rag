from app.services.rag_graph import ask_rag
from tests.evaluation_cases import evaluation_cases

def evaluate_generation():
    
    passed = 0
    
    for case in evaluation_cases:
        
        result = ask_rag(
            case["question"]
        )
        
        answer = result["answer"]
        
        is_correct = all(
            keyword in answer
            for keyword in case["expected_keywords"]
        )
        
        if is_correct:
            passed += 1
            
        print({
            "question": case["question"],
            "answer": answer,
            "passed": is_correct,
        })
        
    accuracy = passed / len(evaluation_cases)
    
    print(f"Keyword Pass Rate: {accuracy: .2%}")
    
if __name__ == "__main__":
    evaluate_generation()