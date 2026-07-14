from typing import Any

import redis
from app.core.config import get_settings
from app.db.session import check_database
from fastapi import APIRouter, Response, status

router = APIRouter(tags=["system"])


@router.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "api"}


@router.get("/ready")
def ready(response: Response) -> dict[str, Any]:
    settings = get_settings()
    checks: dict[str, str] = {}
    healthy = True
    try:
        check_database(settings.database_url)
        checks["database"] = "ok"
    except Exception:
        checks["database"] = "unavailable"
        healthy = False
    try:
        client = redis.Redis.from_url(
            settings.redis_url, socket_connect_timeout=1, socket_timeout=1
        )
        client.ping()
        checks["redis"] = "ok"
    except Exception:
        checks["redis"] = "unavailable"
        healthy = False
    if not healthy:
        response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    return {"status": "ready" if healthy else "not_ready", "checks": checks}
