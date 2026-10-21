"""Registry of public data sources.

Every dataset Handa loads is declared here with its licence, so the README,
the ingestion code and the map attribution all read from one place.
"""

from dataclasses import dataclass
from enum import StrEnum


class Licence(StrEnum):
    ODBL = "ODbL-1.0"
    CC_BY = "CC-BY-4.0"
    COPERNICUS = "Copernicus open licence"
    GOV_PUBLIC = "Philippine government public data"
    NON_COMMERCIAL = "Non-commercial use only"
    TO_CONFIRM = "Licence to confirm"


@dataclass(frozen=True)
class DataSource:
    key: str
    name: str
    publisher: str
    licence: Licence
    url: str
    notes: str = ""


SOURCES: tuple[DataSource, ...] = (
    DataSource(
        key="osm",
        name="OpenStreetMap roads, buildings and amenities",
        publisher="OpenStreetMap contributors",
        licence=Licence.ODBL,
        url="https://www.openstreetmap.org",
        notes="Attribution required on every map view.",
    ),
    DataSource(
        key="sentinel2",
        name="Sentinel-2 Level-2A imagery",
        publisher="European Space Agency / Copernicus",
        licence=Licence.COPERNICUS,
        url="https://dataspace.copernicus.eu",
    ),
    DataSource(
        key="flood_control_projects",
        name="Published flood-control project list",
        publisher="Philippine government",
        licence=Licence.TO_CONFIRM,
        url="",
        notes="Confirm the official source and licence before loading.",
    ),
)


def get_source(key: str) -> DataSource:
    for source in SOURCES:
        if source.key == key:
            return source
    raise KeyError(f"Unknown data source: {key}")
