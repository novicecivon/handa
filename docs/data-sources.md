# Data sources

Handa uses public data only. Raw files are never committed; loaders download them into `data/raw/`.

| Source | Publisher | Licence | Used for |
|---|---|---|---|
| OpenStreetMap | OpenStreetMap contributors | ODbL 1.0 (attribution required) | Roads, buildings, open spaces |
| Sentinel-2 L2A | ESA / Copernicus | Copernicus open licence | Land-cover segmentation |
| Flood-control project list | Philippine government | To confirm | Gap analysis |
| Flood hazard maps | To confirm | To confirm | Model target, comparison layer |
| Elevation model | To confirm | To confirm | Terrain features |
| Barangay boundaries and population | To confirm | To confirm | Aggregation, exposure |

Official hazard platforms are used only through published downloads or an agreed API. They are never scraped.
