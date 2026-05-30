from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_root_response_body():
    response = client.get("/")
    assert response.json() == {"message": "FastAPI DevOps Project"}


def test_root_content_type():
    response = client.get("/")
    assert "application/json" in response.headers["content-type"]


def test_healthz():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_readyz():
    response = client.get("/readyz")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}

