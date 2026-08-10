"""Action-relative dual repairs for the scalar Ferrers activation area.

The scalar area quotient is unsafe under both primitive Stage-94 extensions.
For a declared threshold insertion, the one-step repair is the new threshold
crossing depth j_T (equivalently Delta_T A).  For a declared orbit-node append,
the dual repair is the new node rank r_new (equivalently Delta_J A).

This module records the orbit-side future collision and a small action compiler
that selects the directional response coordinate required by the declared
one-step action.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .abc_activation_area_future import threshold_area_future_state
from .abc_dyadic_ferrers_boundary import ferrers_boundary_from_staircase
from .abc_dyadic_threshold_staircase import (
    DyadicThresholdStaircase,
    dyadic_threshold_staircase,
)


@dataclass(frozen=True)
class OrbitAreaFutureState:
    current_area: int
    new_node_rank: int
    future_area: int
    repaired_state: tuple[int, int]
    future_reconstructed: bool


@dataclass(frozen=True)
class OrbitAreaFutureCollision:
    common_current_area: int
    left_new_node_rank: int
    right_new_node_rank: int
    left_future_area: int
    right_future_area: int
    future_area_equal: bool
    area_quotient_future_safe: bool
    collision_verified: bool


@dataclass(frozen=True)
class ActionRelativeAreaRepair:
    action: str
    current_area: int
    response_coordinate_name: str
    response_coordinate_value: int | None
    directional_area_increment: int
    future_area: int
    future_reconstructed: bool


def orbit_area_future_state(
    staircase: DyadicThresholdStaircase,
) -> OrbitAreaFutureState:
    """Return exact one-step area evolution under one appended dyadic node."""
    old_boundary = ferrers_boundary_from_staircase(staircase)
    updated = dyadic_threshold_staircase(
        staircase.q,
        staircase.p,
        staircase.base_exponent,
        staircase.horizon_steps + 1,
        staircase.thresholds,
    )
    new_boundary = ferrers_boundary_from_staircase(updated)
    current = old_boundary.activation_area
    new_rank = new_boundary.node_ranks[-1]
    future = new_boundary.activation_area
    if future != current + new_rank:
        raise AssertionError("orbit future area lost node-rank reconstruction")
    return OrbitAreaFutureState(
        current_area=current,
        new_node_rank=new_rank,
        future_area=future,
        repaired_state=(current, new_rank),
        future_reconstructed=True,
    )


def activation_area_orbit_future_collision(
    left: DyadicThresholdStaircase,
    right: DyadicThresholdStaircase,
) -> OrbitAreaFutureCollision:
    """Certify equal current area but unequal future area under one node append."""
    if left.thresholds != right.thresholds:
        raise ValueError("orbit future collision requires the same threshold grid")
    if left.horizon_steps != right.horizon_steps:
        raise ValueError("orbit future collision requires the same current horizon")
    left_area = ferrers_boundary_from_staircase(left).activation_area
    right_area = ferrers_boundary_from_staircase(right).activation_area
    if left_area != right_area:
        raise ValueError("orbit future collision requires an equal current-area fiber")

    left_future = orbit_area_future_state(left)
    right_future = orbit_area_future_state(right)
    equal = left_future.future_area == right_future.future_area
    return OrbitAreaFutureCollision(
        common_current_area=left_area,
        left_new_node_rank=left_future.new_node_rank,
        right_new_node_rank=right_future.new_node_rank,
        left_future_area=left_future.future_area,
        right_future_area=right_future.future_area,
        future_area_equal=equal,
        area_quotient_future_safe=equal,
        collision_verified=not equal,
    )


def action_relative_area_repair(
    staircase: DyadicThresholdStaircase,
    action: str,
    new_threshold: Fraction | None = None,
) -> ActionRelativeAreaRepair:
    """Choose the exact directional repair coordinate for one declared action."""
    if action == "threshold":
        if new_threshold is None:
            raise ValueError("threshold action requires new_threshold")
        state = threshold_area_future_state(staircase, new_threshold)
        return ActionRelativeAreaRepair(
            action=action,
            current_area=state.current_area,
            response_coordinate_name="crossing_depth",
            response_coordinate_value=state.crossing_depth,
            directional_area_increment=state.active_span,
            future_area=state.future_area,
            future_reconstructed=True,
        )
    if action == "orbit":
        if new_threshold is not None:
            raise ValueError("orbit action does not accept new_threshold")
        state = orbit_area_future_state(staircase)
        return ActionRelativeAreaRepair(
            action=action,
            current_area=state.current_area,
            response_coordinate_name="new_node_rank",
            response_coordinate_value=state.new_node_rank,
            directional_area_increment=state.new_node_rank,
            future_area=state.future_area,
            future_reconstructed=True,
        )
    raise ValueError("action must be 'threshold' or 'orbit'")
