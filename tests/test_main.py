import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

VALID_PAYLOAD = {
    "concept": "Vector Database",
    "audience": "Marketing Manager"
}

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert all(key in response.json() for key in ["status", "timestamp", "system"])

def test_valid_explanation_request():
    response = client.post("/explain", json=VALID_PAYLOAD)
    assert response.status_code == 200
    data = response.json()
    assert data["concept"] == VALID_PAYLOAD["concept"]
    assert "simulated explanation" in data["explanation"]

def test_invalid_empty_concept():
    response = client.post("/explain", json={"concept": "   ", "audience": "Developer"})
    assert response.status_code == 422
    assert "Field cannot be empty" in response.text

def test_max_length_validation():
    payload = {
        "concept": "A" * 101,
        "audience": "B" * 51
    }
    response = client.post("/explain", json=payload)
    assert response.status_code == 422
    errors = response.json()["detail"]
    assert any("101 characters" in err["msg"] for err in errors)