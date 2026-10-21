"""Flood-protection gap analysis (Module 1).

A gap is a high-susceptibility area with no flood-control project within a
set distance. Results describe what the data shows; they do not judge any
project, contractor or official.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class GapArea:
    barangay: str
    susceptibility: float
    nearest_project_m: float | None
    population: int | None


def find_gaps(min_susceptibility: float, max_distance_m: float) -> list[GapArea]:
    raise NotImplementedError
