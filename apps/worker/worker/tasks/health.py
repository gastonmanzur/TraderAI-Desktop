from typing import Any, cast

from worker.celery_app import celery_app

_task = cast(Any, celery_app.task(name="health.ping"))


@_task
def ping() -> dict[str, str]:
    return {"status": "ok", "service": "worker"}
