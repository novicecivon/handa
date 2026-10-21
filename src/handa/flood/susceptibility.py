"""Flood-susceptibility model (Module 1).

Plan:
- Features per grid cell: elevation, slope, distance to river, land cover,
  built-up share, drainage density.
- Target: official flood hazard class.
- Model: LightGBM, evaluated with spatial cross-validation (blocked folds),
  never a random split, so nearby cells do not leak between train and test.
- Track every run in MLflow.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class FoldResult:
    fold: int
    roc_auc: float
    pr_auc: float


def make_spatial_folds(n_folds: int) -> None:
    raise NotImplementedError


def train(n_folds: int = 5) -> list[FoldResult]:
    raise NotImplementedError
