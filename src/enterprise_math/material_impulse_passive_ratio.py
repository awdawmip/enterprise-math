"""Finite passive impulse-ratio calibration for a stationary 1D wall.

A fixed material impulse count is a useful general comparator but does not
uniformly preserve passivity across arbitrary incident momenta unless its domain
is restricted.  This module instead calibrates one finite *impulse ratio* sample
``j`` on an independent amplitude ``A_J`` with

    0 <= j <= 2 A_J.

For incoming oriented momentum ``P>0`` the applied impulse is

    J = floor(P*j/A_J),

with exact remainder retained.  The ratio bound guarantees ``J<=2P`` and hence
non-amplifying squared momentum under the minimal stationary-wall passivity
criterion.

The material lookup remains sparse and history-aware:

    (layer_depth, branch, material_response_sample) -> impulse_ratio_sample.

Missing keys are explicit ``PASSIVE_RATIO_UNDERRESOLVED`` states; no interpolation
is performed.  The ratio scale is independent from the material response scale.

Finite quantization creates an exact rebound threshold.  If ``j>A_J`` then
``floor(P*j/A_J)>P`` exactly when

    P*(j-A_J) >= A_J,

so the minimum positive momentum that resolves a rebound is

    ceil(A_J/(j-A_J)).

Thus a material ratio above the nominal stall value can still produce a stall at
small integer momentum until sufficient momentum precision is available.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_impulse_calibration import MaterialImpulseKey
from .material_impulse_passivity import ImpulsePassivityReport, impulse_passivity_report

PASSIVE_RATIO_CALIBRATED = "PASSIVE_RATIO_CALIBRATED"
PASSIVE_RATIO_UNDERRESOLVED = "PASSIVE_RATIO_UNDERRESOLVED"


@dataclass(frozen=True)
class FinitePassiveImpulseRatioCalibration:
    material_amplitude: int
    ratio_amplitude: int
    ratio_entries: tuple[tuple[MaterialImpulseKey, int], ...]


def explicit_passive_impulse_ratio_calibration(
    material_amplitude: int,
    ratio_amplitude: int,
    ratio_entries: dict[MaterialImpulseKey, int]
    | tuple[tuple[MaterialImpulseKey, int], ...]
    | list[tuple[MaterialImpulseKey, int]],
) -> FinitePassiveImpulseRatioCalibration:
    """Validate a sparse material-state -> passive impulse-ratio table."""
    for name, value in (
        ("material_amplitude", material_amplitude),
        ("ratio_amplitude", ratio_amplitude),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")
    raw = tuple(ratio_entries.items()) if isinstance(ratio_entries, dict) else tuple(ratio_entries)
    if not raw:
        raise ValueError("at least one passive impulse-ratio entry is required")
    keys = tuple(key for key, _ratio in raw)
    if len(keys) != len(set(keys)):
        raise ValueError("passive impulse-ratio keys must be unique")

    frozen: list[tuple[MaterialImpulseKey, int]] = []
    for key, ratio in raw:
        if not isinstance(key, MaterialImpulseKey):
            raise ValueError("ratio calibration keys must be MaterialImpulseKey values")
        if key.material_response_sample > material_amplitude:
            raise ValueError("material response sample exceeds material amplitude")
        if (
            isinstance(ratio, bool)
            or not isinstance(ratio, int)
            or not 0 <= ratio <= 2 * ratio_amplitude
        ):
            raise ValueError("impulse ratio sample must lie in 0..2*ratio_amplitude")
        if key.material_response_sample == 0 and ratio != 0:
            raise ValueError("zero material response must map to zero impulse ratio")
        frozen.append((key, ratio))
    frozen.sort(key=lambda item: item[0])
    return FinitePassiveImpulseRatioCalibration(
        material_amplitude=material_amplitude,
        ratio_amplitude=ratio_amplitude,
        ratio_entries=tuple(frozen),
    )


@dataclass(frozen=True)
class PassiveImpulseRatioOutcome:
    status: str
    key: MaterialImpulseKey
    incoming_oriented_momentum: int
    ratio_sample: int | None
    ratio_amplitude: int
    impulse: int | None
    ratio_remainder: int | None
    passivity: ImpulsePassivityReport | None

    @property
    def momentum_reversed(self) -> bool:
        return self.passivity is not None and self.passivity.outgoing_oriented_momentum < 0


def passive_impulse_from_material_state(
    calibration: FinitePassiveImpulseRatioCalibration,
    layer_depth: int,
    branch: str,
    material_response_sample: int,
    incoming_oriented_momentum: int,
) -> PassiveImpulseRatioOutcome:
    """Resolve one passive material impulse from current positive oriented momentum."""
    if (
        isinstance(incoming_oriented_momentum, bool)
        or not isinstance(incoming_oriented_momentum, int)
        or incoming_oriented_momentum <= 0
    ):
        raise ValueError("incoming_oriented_momentum must be a positive integer")
    key = MaterialImpulseKey(layer_depth, branch, material_response_sample)
    if material_response_sample > calibration.material_amplitude:
        raise ValueError("material response sample exceeds calibration material amplitude")
    ratio: int | None = None
    for candidate, value in calibration.ratio_entries:
        if candidate == key:
            ratio = value
            break
    if ratio is None:
        return PassiveImpulseRatioOutcome(
            status=PASSIVE_RATIO_UNDERRESOLVED,
            key=key,
            incoming_oriented_momentum=incoming_oriented_momentum,
            ratio_sample=None,
            ratio_amplitude=calibration.ratio_amplitude,
            impulse=None,
            ratio_remainder=None,
            passivity=None,
        )

    impulse, remainder = divmod(
        incoming_oriented_momentum * ratio,
        calibration.ratio_amplitude,
    )
    report = impulse_passivity_report(incoming_oriented_momentum, impulse)
    if not report.passive_nonamplifying:
        raise AssertionError("passive ratio calibration generated active amplification")
    return PassiveImpulseRatioOutcome(
        status=PASSIVE_RATIO_CALIBRATED,
        key=key,
        incoming_oriented_momentum=incoming_oriented_momentum,
        ratio_sample=ratio,
        ratio_amplitude=calibration.ratio_amplitude,
        impulse=impulse,
        ratio_remainder=remainder,
        passivity=report,
    )


def minimum_momentum_for_ratio_rebound(
    ratio_sample: int,
    ratio_amplitude: int,
) -> int | None:
    """Exact minimum P with floor(P*j/A)>P; None when j<=A."""
    if (
        isinstance(ratio_amplitude, bool)
        or not isinstance(ratio_amplitude, int)
        or ratio_amplitude <= 0
    ):
        raise ValueError("ratio_amplitude must be a positive integer")
    if (
        isinstance(ratio_sample, bool)
        or not isinstance(ratio_sample, int)
        or not 0 <= ratio_sample <= 2 * ratio_amplitude
    ):
        raise ValueError("ratio_sample must lie in 0..2*ratio_amplitude")
    if ratio_sample <= ratio_amplitude:
        return None
    excess = ratio_sample - ratio_amplitude
    return (ratio_amplitude + excess - 1) // excess
