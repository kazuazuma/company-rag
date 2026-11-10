def normalize_question(question: str) -> str:
    cleaned = question.strip()
    
    if not cleaned:
        raise ValueError("質問を入力して下さい。")
    
    return cleaned