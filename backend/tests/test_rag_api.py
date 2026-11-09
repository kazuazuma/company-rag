from fastapi.testclient import TestClient

from app.main import app
from app.routers import rag

def fake_ask_rag(question: str):
    return{
        "answer": "有給休暇は３営業日前までです。",
        "sources": [],
    }
    
def test_rag_api(monkeypatch):
    monkeypatch.setattr(
        rag,
        "ask_rag",
        fake_ask_rag,
    )
    
    client = TestClient(app)
    
    response = client.post(
        "/rag/ask",
        json={
            "question": "有給休暇は何日前？"
        },
    )
    
    assert response.status_code == 200
    
    data = response.json()
    
    assert data["answer"] == "有給休暇は３営業日前までです。"
    assert data["sources"] == []
    
def test_empty_question(monkeypatch):
    
    monkeypatch.setattr(
        rag,
        "ask_rag",
        fake_ask_rag,
    )
    
    client = TestClient(app)
    
    response = client.post(
        "/rag/ask",
        json={
            "question": ""
        },
    )
    
    assert response.status_code == 422
    
    