from fastapi.testclient import TestClient
from backend.main import app

client = TestClient(app)


def test_health_status():
    response = client.get("/health")
    assert response.status_code == 200


def test_health_response():
    response = client.get("/health")
    assert response.json() == {"status": "ok"}


def test_unknown_endpoint():
    response = client.get("/unknown")
    assert response.status_code == 404
