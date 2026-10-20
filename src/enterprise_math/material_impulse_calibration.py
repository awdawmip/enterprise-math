"""Explicit finite calibration from material state to integer impulse magnitude.

The old E001 comparator maps a material response ratio directly to a returned
motion budget.  The impulse-world direction removes that shortcut.  A material
state first maps to a non-negative integer impulse count ``J`` in the same
abstract momentum-count unit used by the world state; momentum is then updated
by addition/subtraction and rebound is inferred only from the resulting sign.

Calibration keys retain the material coordinates that can be future-relevant:

    (layer_depth, branch, material_response_sample) -> impulse_count.

This deliberately avoids assuming that equal response samples at different
depths/branches must produce equal impulses.  The table is sparse and performs no
interpolation.  Missing keys are explicit IMPULSE_UNDERRESOLVED states.

This is an engineering calibration interface, not a physical force/impulse law.
Real calibration would additionally need a declared time/contact protocol and
consistent physical units.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_hysteresis import LOADING, RETURNING

IMPULSE_CALIBRATED = "IMPULSE_CALIBRATED"
IMPULSE_UNDERRESOLVED = "IMPULSE_UNDERRESOLVED"


@dataclass(frozen=True, order=True)
class MaterialImpulseKey:
    layer_depth: int
    branch: str
    material_response_sample: int

    def __post_init__(self) -> None:
        if (
            isinstance(self.layer_depth, bool)
            or not isinstance(self.layer_depth, int)
            or self.layer_depth <= 0
        ):
            raise ValueError("layer_depth must be a positive integer")
        if self.branch not in (LOADING, RETURNING):
            raise ValueError("branch must be LOADING or RETURNING")
        if (
            isinstance(self.material_response_sample, bool)
            or not isinstance(self.material_response_sample, int)
            or self.material_response_sample < 0
        ):
            raise ValueError("material_response_sample must be non-negative")


@dataclass(frozen=True)
class FiniteImpulseCalibration:
    material_amplitude: int
    impulse_entries: tuple[tuple[MaterialImpulseKey, int], ...]


def explicit_impulse_calibration(
    material_amplitude: int,
    impulse_entries: dict[MaterialImpulseKey, int]
    | tuple[tuple[MaterialImpulseKey, int], ...]
    | list[tuple[MaterialImpulseKey, int]],
) -> FiniteImpulseCalibration:
    """Validate and freeze one sparse finite material-state -> impulse table."""
    if (
        isinstance(material_amplitude, bool)
        or not isinstance(material_amplitude, int)
        or material_amplitude <= 0
    ):
        raise ValueError("material_amplitude must be a positive integer")
    raw = tuple(impulse_entries.items()) if isinstance(impulse_entries, dict) else tuple(impulse_entries)
    if not raw:
        raise ValueError("at least one impulse calibration entry is required")
    keys = tuple(key for key, _impulse in raw)
    if len(keys) != len(set(keys)):
        raise ValueError("impulse calibration keys must be unique")

    frozen: list[tuple[MaterialImpulseKey, int]] = []
    for key, impulse in raw:
        if not isinstance(key, MaterialImpulseKey):
            raise ValueError("impulse calibration keys must be MaterialImpulseKey values")
        if key.material_response_sample > material_amplitude:
            raise ValueError("material response sample exceeds material amplitude")
        if isinstance(impulse, bool) or not isinstance(impulse, int) or impulse < 0:
            raise ValueError("impulse_count must be a non-negative integer")
        if key.material_response_sample == 0 and impulse != 0:
            raise ValueError("zero material response must calibrate to zero impulse")
        frozen.append((key, impulse))
    frozen.sort(key=lambda item: item[0])
    return FiniteImpulseCalibration(
        material_amplitude=material_amplitude,
        impulse_entries=tuple(frozen),
    )


@dataclass(frozen=True)
class CalibratedImpulse:
    status: str
    key: MaterialImpulseKey
    impulse_count: int | None


def calibrated_material_impulse(
    calibration: FiniteImpulseCalibration,
    layer_depth: int,
    branch: str,
    material_response_sample: int,
) -> CalibratedImpulse:
    """Look up one exact material-state impulse without interpolation."""
    key = MaterialImpulseKey(layer_depth, branch, material_response_sample)
    if material_response_sample > calibration.material_amplitude:
        raise ValueError("material response sample exceeds calibration material amplitude")
    for candidate, impulse in calibration.impulse_entries:
        if candidate == key:
            return CalibratedImpulse(IMPULSE_CALIBRATED, key, impulse)
    return CalibratedImpulse(IMPULSE_UNDERRESOLVED, key, None)
