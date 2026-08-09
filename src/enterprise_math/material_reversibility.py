"""One-step reversibility of the projected Pythagorean material oscillator.

The fixed-resolution projected value alone is many-to-one.  If the bounded
projection details are retained, however, the exact lifted coordinates can be
reconstructed and the previous integer state is recovered using

    M^T M = c^2 I,

for ``M=[[a,-b],[b,a]]``.

Thus projection-induced material extinction/history merging occurs only after an
explicit decision to discard detail.  This is an E001 application of the wider
history/future-sufficiency distinction, not a claim that physical dissipation is
merely information deletion.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_oscillator import (
    TOWARD_ZERO,
    PythagoreanRotation,
    projected_rotation_step,
)


@dataclass(frozen=True, order=True)
class ExtendedProjectedRotationState:
    """Projected value plus the bounded details needed for exact one-step recovery."""

    after: tuple[int, int]
    details: tuple[int, int]


def extended_projected_rotation_state(
    previous: tuple[int, int],
    rotation: PythagoreanRotation,
) -> ExtendedProjectedRotationState:
    """Encode one previous state as projected value plus explicit details."""
    report = projected_rotation_step(
        previous[0], previous[1], rotation, TOWARD_ZERO
    )
    return ExtendedProjectedRotationState(
        after=report.after,
        details=report.details,
    )


def reconstruct_previous_rotation_state(
    extended: ExtendedProjectedRotationState,
    rotation: PythagoreanRotation,
) -> tuple[int, int]:
    """Exactly invert one projected step when its details are retained."""
    qx, qy = extended.after
    dx, dy = extended.details
    for name, value in (("qx", qx), ("qy", qy), ("dx", dx), ("dy", dy)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    if abs(dx) >= rotation.c or abs(dy) >= rotation.c:
        raise ValueError("projection detail escaped its bounded fiber")

    raw_x = rotation.c * qx + dx
    raw_y = rotation.c * qy + dy
    denominator = rotation.c * rotation.c
    x_numerator = rotation.a * raw_x + rotation.b * raw_y
    y_numerator = -rotation.b * raw_x + rotation.a * raw_y
    if x_numerator % denominator != 0 or y_numerator % denominator != 0:
        raise ValueError("extended state is not in the image of this integer rotation step")
    previous = (
        x_numerator // denominator,
        y_numerator // denominator,
    )
    if extended_projected_rotation_state(previous, rotation) != extended:
        raise ValueError("extended state failed round-trip validation")
    return previous


def after_only_collision(
    left_previous: tuple[int, int],
    right_previous: tuple[int, int],
    rotation: PythagoreanRotation,
) -> bool:
    """Whether two distinct histories merge after discarding projection details."""
    if left_previous == right_previous:
        return False
    left = extended_projected_rotation_state(left_previous, rotation)
    right = extended_projected_rotation_state(right_previous, rotation)
    return left.after == right.after
