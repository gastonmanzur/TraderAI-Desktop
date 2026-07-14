from fastapi import FastAPI

from app.api.v1.router import router
from app.core.correlation import correlation_middleware
from app.core.logging import configure_logging


def create_app() -> FastAPI:
    configure_logging()
    app = FastAPI(title="TraderAI API", version="0.1.0")
    app.middleware("http")(correlation_middleware)
    app.include_router(router)
    return app


app = create_app()
