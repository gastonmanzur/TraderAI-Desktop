from app.main import create_app
from fastapi.testclient import TestClient
from pytest import MonkeyPatch


def test_ready_unavailable_is_sanitized(monkeypatch: MonkeyPatch) -> None:
    def boom(_: str) -> None:
        raise RuntimeError("postgresql://secret")

    monkeypatch.setattr("app.api.v1.system.check_database", boom)

    class RedisBad:
        def ping(self) -> None:
            raise RuntimeError("redis secret")

    monkeypatch.setattr("app.api.v1.system.redis.Redis.from_url", lambda *a, **k: RedisBad())
    response = TestClient(create_app()).get("/api/v1/ready")
    assert response.status_code == 503
    assert "secret" not in response.text
    assert response.json()["status"] == "not_ready"
