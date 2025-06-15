import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_valid_cardiac_input():
    response = client.post(
        "/query",
        json={"user_input": "The patient is experiencing chest pain radiating to the left arm, shortness of breath, sweating, and dizziness."}
    )
    assert response.status_code == 200
    data = response.json()
    assert "Cardiac" in data["condition"]
    assert "First Aid" in data["answer"] or "first aid" in data["answer"].lower()

def test_empty_input():
    response = client.post("/query", json={"user_input": ""})
    assert response.status_code == 200
    data = response.json()
    assert "need more detailed information" in data["condition"] or "provide specific symptoms" in data["condition"]

def test_unknown_symptom_input():
    response = client.post(
        "/query",
        json={"user_input": "The patient reports yellow spots on the tongue and itchy ears."}
    )
    assert response.status_code == 200
    data = response.json()
    assert "Condition" in data["answer"] or len(data["answer"]) > 10  # Ensuring answer is generated
