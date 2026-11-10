import pytest

from app.services.question_service import normalize_question

def test_normalize_question():
    result = normalize_question("有給休暇について")
    
    assert result == "有給休暇について"
    
def test_empty_question():
    with pytest.raises(ValueError):
        normalize_question("   ")