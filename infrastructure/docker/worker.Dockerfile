FROM python:3.13-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir uv && uv sync --frozen --package traderai-worker
CMD ["uv", "run", "celery", "-A", "worker.celery_app.celery_app", "worker", "--workdir", "apps/worker", "--loglevel", "INFO"]
