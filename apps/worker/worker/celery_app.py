import os

from celery import Celery


def create_celery_app() -> Celery:
    broker_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    app = Celery("traderai_worker", broker=broker_url)
    app.conf.task_always_eager = os.getenv("CELERY_TASK_ALWAYS_EAGER", "false").lower() == "true"
    app.autodiscover_tasks(["worker.tasks"])
    return app


celery_app = create_celery_app()
