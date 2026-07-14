FROM python:3.13-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir uv && uv sync --frozen --package traderai-api
EXPOSE 8000
CMD ["uv", "run", "uvicorn", "app.main:app", "--app-dir", "apps/api", "--host", "0.0.0.0", "--port", "8000"]
