# Architecture

## Module map

| Path | Responsibility |
|---|---|
| `src/handa/api` | FastAPI app and routes |
| `src/handa/config.py` | Settings from environment variables |
| `src/handa/db` | Database engine and sessions (PostGIS) |
| `src/handa/ingest` | Data source registry and loaders for public layers |
| `src/handa/flood` | Susceptibility model and gap analysis (Module 1) |
| `src/handa/reports` | Resident flood reports and depth estimation (Module 1b) |
| `db/init` | SQL run once when the database is first created |
| `tests` | Unit and API tests |

## Database schemas

- `raw`: data as loaded from each source, unchanged
- `core`: cleaned, joined tables used by the models and the API

## Decisions

Record significant decisions in `docs/decisions/` as short notes: the context, the options considered, the choice and why.
