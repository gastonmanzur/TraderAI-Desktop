# ADR-001 Versiones tecnológicas

Accepted.

- Node 24 LTS, pnpm 11.x.
- Python 3.13.14.
- Rust 1.97 stable.
- Tauri requested: 2.11.5. Verification note: npm registry metadata checked on 2026-07-14 showed `@tauri-apps/api@2.11.5` unresolved and latest `@tauri-apps/api` as 2.11.1, so the scaffold pins JS Tauri packages to 2.11.1 while Rust crate metadata remains prepared for Tauri 2.
- FastAPI 0.139.0, Pydantic 2.13.4, SQLAlchemy 2.0.51, Celery 5.6.3.
- PostgreSQL 18.4, Redis 8.6.x.
