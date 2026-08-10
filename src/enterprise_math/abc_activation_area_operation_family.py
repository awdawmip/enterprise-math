"""Finite operation-family response signature for the Ferrers activation area.

For a current staircase, declare a finite family consisting of ordered candidate
threshold insertions T_1<...<T_a and one orbit-node append.  The exact natural
one-step response signature is

    (A; j_{T_1},...,j_{T_a}; r_new),

where the candidate-threshold crossing depths form a weakly increasing
staircase.  Each threshold future area is reconstructed from its crossing span,
and the orbit future area from the new node rank.

The threshold response family therefore has only C(h+a+1,a) monotone crossing
states rather than (h+2)^a arbitrary response tuples before any arithmetic
restrictions are imposed.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb

from .abc_activation_area_action_repair import orbit_area_future_state
from .abc_activation_area_future import threshold_area_future_state
from .abc_dyadic_ferrers_boundary import ferrers_boundary_from_staircase
from .abc_dyadic_threshold_staircase import DyadicThresholdStaircase


@dataclass(frozen=True)
class OperationFamilyAreaSignature:
    current_area: int
    candidate_thresholds: tuple[Fraction, ...]
    threshold_crossing_depths: tuple[int | None, ...]
    threshold_area_increments: tuple[int, ...]
    threshold_future_areas: tuple[int, ...]
    orbit_new_rank: int
    orbit_future_area: int
    response_signature: tuple[object, ...]
    monotone_threshold_response_state_count: int
    unconstrained_threshold_response_tuple_count: int
    crossing_staircase_verified: bool
    future_reconstruction_verified: bool


def _require_candidate_thresholds(
    staircase: DyadicThresholdStaircase,
    candidate_thresholds: tuple[Fraction, ...],
) -> None:
    if not candidate_thresholds:
        raise ValueError("candidate_thresholds must be nonempty")
    if any(
        not isinstance(value, Fraction) or value <= 0
        for value in candidate_thresholds
    ):
        raise ValueError("candidate thresholds must be positive Fractions")
    if any(
        right <= left
        for left, right in zip(candidate_thresholds, candidate_thresholds[1:])
    ):
        raise ValueError("candidate thresholds must be strictly increasing")
    if any(value in staircase.thresholds for value in candidate_thresholds):
        raise ValueError("candidate thresholds must be genuine insertions")


def operation_family_area_signature(
    staircase: DyadicThresholdStaircase,
    candidate_thresholds: tuple[Fraction, ...],
) -> OperationFamilyAreaSignature:
    """Compile all one-step area futures in a finite threshold+orbit action family."""
    _require_candidate_thresholds(staircase, candidate_thresholds)
    current_area = ferrers_boundary_from_staircase(staircase).activation_area
    threshold_states = tuple(
        threshold_area_future_state(staircase, threshold)
        for threshold in candidate_thresholds
    )
    crossings = tuple(state.crossing_depth for state in threshold_states)
    keys = tuple(
        staircase.horizon_steps + 1 if depth is None else depth
        for depth in crossings
    )
    if any(right < left for left, right in zip(keys, keys[1:])):
        raise AssertionError("ordered candidate thresholds lost crossing staircase")
    increments = tuple(state.active_span for state in threshold_states)
    if any(right > left for left, right in zip(increments, increments[1:])):
        raise AssertionError("higher candidate threshold gained a larger active span")
    threshold_futures = tuple(state.future_area for state in threshold_states)
    if any(
        future != current_area + increment
        for future, increment in zip(threshold_futures, increments)
    ):
        raise AssertionError("threshold family future reconstruction failed")

    orbit_state = orbit_area_future_state(staircase)
    if orbit_state.future_area != current_area + orbit_state.new_node_rank:
        raise AssertionError("orbit family future reconstruction failed")

    a = len(candidate_thresholds)
    h = staircase.horizon_steps
    monotone_count = comb(h + a + 1, a)
    unconstrained_count = (h + 2) ** a
    signature: tuple[object, ...] = (
        current_area,
        crossings,
        orbit_state.new_node_rank,
    )
    return OperationFamilyAreaSignature(
        current_area=current_area,
        candidate_thresholds=candidate_thresholds,
        threshold_crossing_depths=crossings,
        threshold_area_increments=increments,
        threshold_future_areas=threshold_futures,
        orbit_new_rank=orbit_state.new_node_rank,
        orbit_future_area=orbit_state.future_area,
        response_signature=signature,
        monotone_threshold_response_state_count=monotone_count,
        unconstrained_threshold_response_tuple_count=unconstrained_count,
        crossing_staircase_verified=True,
        future_reconstruction_verified=True,
    )


def future_area_for_family_action(
    signature: OperationFamilyAreaSignature,
    action: str,
    threshold_index: int | None = None,
) -> int:
    """Read one declared action's next area from the compiled family signature."""
    if action == "orbit":
        if threshold_index is not None:
            raise ValueError("orbit action does not use threshold_index")
        return signature.orbit_future_area
    if action == "threshold":
        if isinstance(threshold_index, bool) or not isinstance(threshold_index, int):
            raise ValueError("threshold action requires an integer threshold_index")
        if not 0 <= threshold_index < len(signature.candidate_thresholds):
            raise ValueError("threshold_index out of range")
        return signature.threshold_future_areas[threshold_index]
    raise ValueError("action must be 'threshold' or 'orbit'")
