"""Exact one-step history fibers of the E001 projected Pythagorean oscillator.

For a fixed projected coordinate q under signed toward-zero division by c, the
possible discarded details are finite:

* q>0:  delta in {0,...,c-1};
* q<0:  delta in {-(c-1),...,0};
* q=0:  delta in {-(c-1),...,c-1}.

Enumerating the two detail coordinates and applying the exact Pythagorean matrix
inverse therefore recovers the complete global one-step preimage fiber in Z^2.

The module keeps two observables separate:

* projection squared-radius loss of one history;
* fiber multiplicity of the projected value.

Neither determines the other in general.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_oscillator import PythagoreanRotation, projected_rotation_step
from .material_reversibility import (
    ExtendedProjectedRotationState,
    reconstruct_previous_rotation_state,
)


@dataclass(frozen=True, order=True)
class ProjectedRotationHistory:
    """One previous state inside a projected-value fiber."""

    previous: tuple[int, int]
    details: tuple[int, int]
    norm_sq_loss: int


@dataclass(frozen=True)
class ProjectedRotationFiber:
    """Complete global one-step preimage fiber of one projected value."""

    after: tuple[int, int]
    histories: tuple[ProjectedRotationHistory, ...]
    multiplicity: int
    distinct_loss_values: tuple[int, ...]


def _detail_values(projected_coordinate: int, c: int) -> range:
    if projected_coordinate > 0:
        return range(0, c)
    if projected_coordinate < 0:
        return range(-(c - 1), 1)
    return range(-(c - 1), c)


def projected_rotation_fiber(
    after: tuple[int, int],
    rotation: PythagoreanRotation,
) -> ProjectedRotationFiber:
    """Enumerate the complete finite previous-state fiber of ``after``."""
    qx, qy = after
    for name, value in (("qx", qx), ("qy", qy)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")

    histories: list[ProjectedRotationHistory] = []
    for dx in _detail_values(qx, rotation.c):
        for dy in _detail_values(qy, rotation.c):
            extended = ExtendedProjectedRotationState(
                after=after,
                details=(dx, dy),
            )
            try:
                previous = reconstruct_previous_rotation_state(extended, rotation)
            except ValueError:
                continue
            report = projected_rotation_step(*previous, rotation)
            if report.after != after or report.details != (dx, dy):
                raise AssertionError("reconstructed projected history failed validation")
            histories.append(
                ProjectedRotationHistory(
                    previous=previous,
                    details=(dx, dy),
                    norm_sq_loss=report.norm_sq_loss,
                )
            )

    histories_tuple = tuple(sorted(histories))
    if len({history.previous for history in histories_tuple}) != len(histories_tuple):
        raise AssertionError("projected fiber duplicated a previous state")
    return ProjectedRotationFiber(
        after=after,
        histories=histories_tuple,
        multiplicity=len(histories_tuple),
        distinct_loss_values=tuple(
            sorted({history.norm_sq_loss for history in histories_tuple})
        ),
    )
