"""Flood depth from resident reports (Module 1b).

Residents choose a reference level on the form. The image model refines it
using objects of known height in the photo (people, cars, doors).
"""

from enum import StrEnum


class ReferenceLevel(StrEnum):
    ANKLE = "ankle"
    KNEE = "knee"
    WAIST = "waist"
    CHEST = "chest"
    CAR_TIRE = "car_tire"


# Approximate heights in centimetres, used as priors for the image estimate.
REFERENCE_HEIGHT_CM: dict[ReferenceLevel, int] = {
    ReferenceLevel.ANKLE: 10,
    ReferenceLevel.KNEE: 50,
    ReferenceLevel.WAIST: 100,
    ReferenceLevel.CHEST: 130,
    ReferenceLevel.CAR_TIRE: 65,
}


def estimate_depth_cm(reference: ReferenceLevel) -> float:
    raise NotImplementedError
