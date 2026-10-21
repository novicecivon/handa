# Handa

**Interactive flood and earthquake readiness for Philippine communities.**

*Handa* is Filipino for "ready" or "prepared."

The Philippines already has good hazard maps. They tell you a place is at risk. Handa goes one step further and asks practical questions on top of that public data:

- Where is flood protection **missing** in high-risk areas?
- What did residents **actually see** during a flood, and how does it compare with the official hazard level?
- If a large earthquake hits, what is likely to break, which routes stay open, and where should responders be staged?

> **Disclaimer.** Handa is an independent research and visualization tool. It is not an official warning system. PHIVOLCS, PAGASA and your local government unit (LGU) are the authorities for hazard information and emergency instructions.

---

## Status

Early development. The pilot covers **one city** first; other areas follow only after the first one works end to end.

| Module | What it does | Status |
|---|---|---|
| 1 · Flood gaps | Public hazard, elevation, boundary and flood-control layers in PostGIS; land-cover segmentation on Sentinel-2; a flood-susceptibility model; a gap map of high-risk areas with no nearby flood-control project | In progress |
| 1b · Resident flood reports | Residents submit a photo or short video plus a short form; water depth is estimated from reference objects and compared with the official hazard level | Planned |
| 2 · Earthquake scenario | A West Valley Fault scenario: expected shaking, liquefaction zones, likely damage to roads and bridges, evacuation spaces and responder staging | Planned |
| Field kit | Offline, CPU-only versions of the models for use when power and signal are down | Planned |

## Architecture

```
public data sources ──► ingest ──► PostGIS ──► models (susceptibility, segmentation, depth)
                                       │                         │
                                       └──────► FastAPI ◄────────┘
                                                   │
                                              map dashboard
```

- **API:** FastAPI (`src/handa/api`)
- **Database:** PostgreSQL + PostGIS
- **ML:** LightGBM for susceptibility, a segmentation model for land cover, an image model for flood depth; tracked with MLflow
- **Pipelines:** scheduled ingestion and transformation (Airflow + dbt, planned)
- **Quality:** pytest, Ruff, mypy and GitHub Actions on every push

See [`docs/architecture.md`](docs/architecture.md) for the module map.

## Getting started

Requirements: Python 3.12, [uv](https://docs.astral.sh/uv/), Docker.

```bash
cp .env.example .env
make db-up        # start PostGIS
make install      # install dependencies
make test         # run the test suite
make run          # start the API at http://localhost:8000
```

Check it is alive: `curl http://localhost:8000/health`

## Data and licences

Handa uses public data only. Each source and its licence is listed in [`docs/data-sources.md`](docs/data-sources.md). Raw data is never committed to this repository.

- OpenStreetMap data © OpenStreetMap contributors, available under the [ODbL](https://www.openstreetmap.org/copyright).
- Some datasets allow non-commercial use only; this is noted per source.
- Official hazard data is used as published and is never overwritten. Where resident reports disagree with it, the mismatch is shown side by side.

## Privacy and safety

- Uploaded photos and videos have faces and licence plates blurred and location metadata stripped before anything is shown.
- New uploads are held for review before they appear on the map.
- Infrastructure checks report observations such as "no visible change, needs on-site check." Handa does not accuse or name contractors or officials.

## Contributing

Issues and suggestions are welcome. Please open an issue before starting larger changes.

## License

Code is released under the [MIT License](LICENSE). Data keeps the licence of its original source.
