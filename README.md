# TraderAI Desktop

Scaffold reproducible for TraderAI Desktop (Etapa 1 / E1-P01). This repository currently contains only local infrastructure, health checks, contracts, and a Tauri/React desktop shell. It does **not** implement authentication, real market connectivity, risk engines, AI decisions, or real trading.

## Toolchains

- Node `24` (see `.node-version`) with pnpm `11.0.0`.
- Python `3.13.14` (see `.python-version`) with uv.
- Rust stable `1.97.0` (see `rust-toolchain.toml`).
- Docker/Compose for PostgreSQL and Redis.

The verification environment used for this scaffold had Node 20.20.2, Python 3.12.13, Rust 1.89.0, and no Docker, so frozen installs/builds requiring the pinned toolchains or Docker are documented as blocked locally.

## Setup

```bash
corepack enable
pnpm install --frozen-lockfile
uv sync --frozen --all-packages
docker compose config
docker compose up -d --build
```

## Common checks

```bash
pnpm contracts:generate
pnpm contracts:check
pnpm lint
pnpm typecheck
pnpm test
pnpm build
uv run ruff format --check .
uv run ruff check .
uv run mypy apps packages/python
uv run pytest
cargo fmt --all --check
cargo clippy --workspace --all-targets -- -D warnings
cargo test --workspace
curl --fail http://localhost:8000/api/v1/health
curl --fail http://localhost:8000/api/v1/ready
docker compose down
```

## Troubleshooting

- If `pnpm install --frozen-lockfile` fails, confirm Node 24 and pnpm 11 are active.
- If `uv sync --frozen --all-packages` fails, confirm Python 3.13.14 is installed and selected by uv.
- If Compose fails, confirm Docker is installed and the host ports in `.env.example` are free.
- `/api/v1/ready` intentionally returns `503` when PostgreSQL or Redis are unavailable.
