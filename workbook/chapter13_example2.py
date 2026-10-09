import pytest

@pytest.fixture
def record():
    return {"title": "Python Basics", "duration": 60, "level": "beginner"}

def test_record_title(record):
    assert record["title"] == "Python Basics"
    