"""Future incompatibility of the scalar activation-area quotient.

Equal current Ferrers activation areas can evolve to different future areas
under the same threshold insertion.  Therefore the scalar area is not a Markov
or composition-safe state for threshold-extension dynamics.

For one declared threshold insertion T on a fixed horizon h, the exact repair
is the new threshold crossing depth j_T (equivalently its active-span delta):

    A_next = A + (h+1-j_T)    if j_T is finite,
             A               otherwise.

Thus (A,j_T) is a sufficient one-step natural state, equivalent at fixed h to
(A,Delta_T A), and to the P023-style one-step repair (A,A_next).
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_dyadic_activation_potential import biaxial_activation_potential
from .abc_dyadic_ferrers_boundary import ferrers_boundary_from_staircase
from .abc_dyadic_threshold_staircase import DyadicThresholdStaircase


@dataclass(frozen=True)
class ThresholdAreaFutureState:
    current_area: int
    new_threshold: Fraction
    crossing_depth: int | None
    active_span: int
    future_area: int
    repaired_state: tuple[int, int | None]
    future_reconstructed: bool


@dataclass(frozen=True)
class ActivationAreaFutureCollision:
    common_current_area: int
    new_threshold: Fraction
    left_crossing_depth: int | None
    right_crossing_depth: int | None
    left_future_area: int
    right_future_area: int
    future_area_equal: bool
    area_quotient_future_safe: bool
    collision_verified: bool


def threshold_area_future_state(
    staircase: DyadicThresholdStaircase,
    new_threshold: Fraction,
) -> ThresholdAreaFutureState:
    """Return exact one-step area evolution under one new threshold insertion."""
    potential = biaxial_activation_potential(staircase, new_threshold)
    current = potential.old_area
    crossing = potential.new_threshold_crossing_depth
    span = potential.new_threshold_old_active_span
    future = potential.threshold_extended_area
    if future != current + span:
        raise AssertionError("threshold future area lost crossing-span reconstruction")
    return ThresholdAreaFutureState(
        current_area=current,
        new_threshold=new_threshold,
        crossing_depth=crossing,
        active_span=span,
        future_area=future,
        repaired_state=(current, crossing),
        future_reconstructed=True,
    )


def activation_area_future_collision(
    left: DyadicThresholdStaircase,
    right: DyadicThresholdStaircase,
    new_threshold: Fraction,
) -> ActivationAreaFutureCollision:
    """Certify equal current area but unequal future area under the same extension."""
    if left.thresholds != right.thresholds:
        raise ValueError("future collision requires the same current threshold grid")
    if left.horizon_steps != right.horizon_steps:
        raise ValueError("future collision requires the same current orbit horizon")
    left_area = ferrers_boundary_from_staircase(left).activation_area
    right_area = ferrers_boundary_from_staircase(right).activation_area
    if left_area != right_area:
        raise ValueError("future collision requires an equal current-area fiber")

    left_future = threshold_area_future_state(left, new_threshold)
    right_future = threshold_area_future_state(right, new_threshold)
    equal = left_future.future_area == right_future.future_area
    collision = not equal
    return ActivationAreaFutureCollision(
        common_current_area=left_area,
        new_threshold=new_threshold,
        left_crossing_depth=left_future.crossing_depth,
        right_crossing_depth=right_future.crossing_depth,
        left_future_area=left_future.future_area,
        right_future_area=right_future.future_area,
        future_area_equal=equal,
        area_quotient_future_safe=equal,
        collision_verified=collision,
    )
