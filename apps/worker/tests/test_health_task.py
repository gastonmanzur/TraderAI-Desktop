from worker.tasks.health import ping


def test_health_ping_is_idempotent() -> None:
    assert ping() == ping() == {"status": "ok", "service": "worker"}
