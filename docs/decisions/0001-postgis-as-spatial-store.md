# 0001: PostGIS as the spatial store

**Status:** accepted

**Context.** Handa joins hazard polygons, elevation, boundaries, roads and point reports, and serves map queries by area.

**Options.** PostGIS; files (GeoPackage or GeoParquet) queried with GeoPandas or DuckDB.

**Decision.** PostGIS for anything the API serves. Files stay acceptable for one-off analysis.

**Why.** Spatial indexes, SQL joins across layers, and one source of truth for the API and the models.
