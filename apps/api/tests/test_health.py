from app.main import create_app
from fastapi.testclient import TestClient


def test_health_and_correlation() -> None:
    client = TestClient(create_app())
    response = client.get("/api/v1/health", headers={"X-Correlation-ID": "test-1"})
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "service": "api"}
    assert response.headers["X-Correlation-ID"] == "test-1"


def test_invalid_correlation_is_replaced() -> None:
    client = TestClient(create_app())
    response = client.get("/api/v1/health", headers={"X-Correlation-ID": "bad value"})
    assert response.status_code == 200
    assert response.headers["X-Correlation-ID"] != "bad value"
