# TraderAI Desktop

Plataforma de escritorio para Windows que recibe señales de TradingView, las evalúa con reglas cuantitativas y límites de riesgo, ejecuta paper trading en un backend permanente y presenta resultados auditables.

> **MODO PAPER TRADING**  
> No se ejecutan operaciones con dinero real.

## Estado

El proyecto está en **Etapa 0 — Descubrimiento y especificación**. En este punto existen documentos de producto e ingeniería; todavía no hay código productivo ni infraestructura desplegada. Consultar [STATUS.md](STATUS.md) y [docs/CODEX_IMPLEMENTATION_PLAN.md](docs/CODEX_IMPLEMENTATION_PLAN.md).

## Decisión de producto

El primer lanzamiento será una herramienta privada de validación, no un producto comercial ni una promesa de rentabilidad. El objetivo es demostrar que el pipeline de datos y paper trading es íntegro, reproducible y operable con la PC apagada. La IA queda bloqueada hasta disponer de un mínimo de 500 operaciones cerradas y controles de calidad aprobados.

## Arquitectura objetivo

- Desktop: Tauri 2 + React + TypeScript.
- API: FastAPI + Pydantic + SQLAlchemy.
- Persistencia: PostgreSQL como única fuente de verdad.
- Cola y coordinación: Celery + Redis, con patrón outbox en PostgreSQL.
- Mercado: adaptador Binance USD-M Futures para datos públicos.
- Tiempo real: WebSocket; recuperación por cursor desde eventos durables.
- Infraestructura: Docker Compose en desarrollo; VPS Ubuntu + Nginx + HTTPS en producción futura.

La arquitectura completa está en [docs/architecture/SYSTEM_ARCHITECTURE.md](docs/architecture/SYSTEM_ARCHITECTURE.md).

## Límites no negociables

- No conectar brokers ni exchanges para operar.
- No almacenar claves privadas de trading.
- No enviar órdenes reales.
- No introducir IA operativa durante el MVP.
- No representar resultados simulados como beneficios reales.
- No desplegar, comprar servicios ni publicar releases sin aprobación de Gastón.

## Documentación

El índice navegable está en [docs/README.md](docs/README.md). Las decisiones vinculantes están en [DECISIONS.md](DECISIONS.md) y los ADR en [docs/adr](docs/adr).

## Próximo paso

Ejecutar únicamente el paquete **E1-P01 — Scaffolding e infraestructura local**, definido en [docs/CODEX_IMPLEMENTATION_PLAN.md](docs/CODEX_IMPLEMENTATION_PLAN.md). No avanzar a autenticación hasta revisar el diff, ejecutar las verificaciones y actualizar el estado.

