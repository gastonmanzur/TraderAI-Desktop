FROM python:3.13-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir uv && uv sync --frozen --package traderai-market-data
CMD ["uv", "run", "python", "apps/market-data/market_data/main.py"]
