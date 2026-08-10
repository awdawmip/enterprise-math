"""Two-step history closure tests for P025 finite threshold precision.

The mathematical core is independent of ABC: a finite nondecreasing scalar orbit
is observed through ordered threshold rows. Primitive actions either insert a new
threshold row (+T) or append a new monotone orbit node (+J).

Stage 100 gives a one-step response signature. This module shows exactly where
that signature fails for two-step histories and identifies the missing mixed
corner bit / second future-node rank.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable, Sequence

from .abc_signed_exponent_transport import dyadic_difference_pressure_tower


@dataclass(frozen=True)
class OneStepAreaSignature:
    area: int
    candidate_first_depth: int | None
    next_node_rank: int


@dataclass(frozen=True)
class MixedTwoStepResponse:
    area: int
    threshold_span: int
    next_node_rank: int
    corner_bit: int
    final_area: int


@dataclass(frozen=True)
class TwoNodeResponse:
    area: int
    first_node_rank: int
    second_node_rank: int
    final_area: int


def _require_nondecreasing(values: Sequence[Fraction]) -> None:
    if not values:
        raise ValueError("values must be non-empty")
    if any(not isinstance(value, Fraction) for value in values):
        raise ValueError("values must be Fractions")
    if any(values[i] > values[i + 1] for i in range(len(values) - 1)):
        raise ValueError("values must be nondecreasing")


def _require_thresholds(thresholds: Sequence[Fraction]) -> None:
    if any(not isinstance(value, Fraction) or value <= 0 for value in thresholds):
        raise ValueError("thresholds must be positive Fractions")
    if any(thresholds[i] >= thresholds[i + 1] for i in range(len(thresholds) - 1)):
        raise ValueError("thresholds must be strictly increasing")


def activation_area(thresholds: Sequence[Fraction], values: Sequence[Fraction]) -> int:
    """Number of active cells B_{k,j}=1[values[j]>=thresholds[k]]."""
    _require_nondecreasing(values)
    _require_thresholds(thresholds)
    return sum(value >= threshold for threshold in thresholds for value in values)


def first_crossing_depth(values: Sequence[Fraction], threshold: Fraction) -> int | None:
    _require_nondecreasing(values)
    if not isinstance(threshold, Fraction) or threshold <= 0:
        raise ValueError("threshold must be a positive Fraction")
    return next((index for index, value in enumerate(values) if value >= threshold), None)


def threshold_span(values: Sequence[Fraction], threshold: Fraction) -> int:
    """Number of existing nodes activated by a newly inserted threshold."""
    depth = first_crossing_depth(values, threshold)
    return 0 if depth is None else len(values) - depth


def node_rank(thresholds: Sequence[Fraction], value: Fraction) -> int:
    """Number of existing thresholds activated by a newly appended node."""
    _require_thresholds(thresholds)
    if not isinstance(value, Fraction):
        raise ValueError("value must be a Fraction")
    return sum(value >= threshold for threshold in thresholds)


def corner_bit(candidate_threshold: Fraction, next_value: Fraction) -> int:
    if not isinstance(candidate_threshold, Fraction) or candidate_threshold <= 0:
        raise ValueError("candidate_threshold must be a positive Fraction")
    if not isinstance(next_value, Fraction):
        raise ValueError("next_value must be a Fraction")
    return int(next_value >= candidate_threshold)


def one_step_area_signature(
    thresholds: Sequence[Fraction],
    values: Sequence[Fraction],
    candidate_threshold: Fraction,
    next_value: Fraction,
) -> OneStepAreaSignature:
    """Stage-100-style one-step data for the primitive family {+T,+J}."""
    _require_nondecreasing(values)
    if next_value < values[-1]:
        raise ValueError("next_value must extend the monotone orbit")
    return OneStepAreaSignature(
        area=activation_area(thresholds, values),
        candidate_first_depth=first_crossing_depth(values, candidate_threshold),
        next_node_rank=node_rank(thresholds, next_value),
    )


def mixed_two_step_response(
    thresholds: Sequence[Fraction],
    values: Sequence[Fraction],
    candidate_threshold: Fraction,
    next_value: Fraction,
) -> MixedTwoStepResponse:
    """Exact final area after inserting +T and appending +J in either order.

    A'' = A + L_T + R_J + C_{T,J},
    where C_{T,J}=1[next_value>=candidate_threshold].
    """
    signature = one_step_area_signature(
        thresholds, values, candidate_threshold, next_value
    )
    span = threshold_span(values, candidate_threshold)
    corner = corner_bit(candidate_threshold, next_value)
    final_area = signature.area + span + signature.next_node_rank + corner

    thresholds_after = tuple(sorted((*thresholds, candidate_threshold)))
    values_after = (*values, next_value)
    exact = activation_area(thresholds_after, values_after)
    if final_area != exact:
        raise AssertionError("mixed two-step area formula failed")

    return MixedTwoStepResponse(
        area=signature.area,
        threshold_span=span,
        next_node_rank=signature.next_node_rank,
        corner_bit=corner,
        final_area=final_area,
    )


def two_threshold_final_area(
    thresholds: Sequence[Fraction],
    values: Sequence[Fraction],
    first_threshold: Fraction,
    second_threshold: Fraction,
) -> int:
    """Two threshold insertions have no pairwise area interaction."""
    if first_threshold == second_threshold:
        raise ValueError("inserted thresholds must be distinct")
    base = activation_area(thresholds, values)
    predicted = (
        base
        + threshold_span(values, first_threshold)
        + threshold_span(values, second_threshold)
    )
    exact_thresholds = tuple(sorted((*thresholds, first_threshold, second_threshold)))
    exact = activation_area(exact_thresholds, values)
    if predicted != exact:
        raise AssertionError("threshold-threshold additivity failed")
    return predicted


def two_node_response(
    thresholds: Sequence[Fraction],
    values: Sequence[Fraction],
    first_value: Fraction,
    second_value: Fraction,
) -> TwoNodeResponse:
    """Exact final area after two monotone node appends."""
    _require_nondecreasing(values)
    if first_value < values[-1] or second_value < first_value:
        raise ValueError("future nodes must extend the monotone orbit")
    base = activation_area(thresholds, values)
    rank1 = node_rank(thresholds, first_value)
    rank2 = node_rank(thresholds, second_value)
    predicted = base + rank1 + rank2
    exact = activation_area(thresholds, (*values, first_value, second_value))
    if predicted != exact:
        raise AssertionError("two-node area formula failed")
    return TwoNodeResponse(base, rank1, rank2, predicted)


def dyadic_pressures(q: int, p: int, base_exponent: int, horizon_steps: int) -> tuple[Fraction, ...]:
    """Arithmetic realization used by the Stage101 counterexamples."""
    return dyadic_difference_pressure_tower(
        q, p, base_exponent, horizon_steps
    ).pressures


def stage101_mixed_collision() -> dict[str, object]:
    """Two exact P025 orbits with the same one-step {+T,+J} signature.

    Current horizon has one node (depth 0).  Both states have
      A=1, j_T=None, r_new=1,
    but the mixed corner bit differs, so the two-step final areas are 2 and 3.
    """
    thresholds = (Fraction(1, 25),)
    candidate = Fraction(11, 20)
    flat = dyadic_pressures(3, 5, 2, 1)
    jump = dyadic_pressures(3, 41, 2, 1)

    flat_sig = one_step_area_signature(thresholds, flat[:1], candidate, flat[1])
    jump_sig = one_step_area_signature(thresholds, jump[:1], candidate, jump[1])
    if flat_sig != jump_sig:
        raise AssertionError("fixtures do not share the intended one-step signature")

    flat_response = mixed_two_step_response(thresholds, flat[:1], candidate, flat[1])
    jump_response = mixed_two_step_response(thresholds, jump[:1], candidate, jump[1])
    if flat_response.corner_bit == jump_response.corner_bit:
        raise AssertionError("fixtures do not separate the mixed corner bit")
    if flat_response.final_area == jump_response.final_area:
        raise AssertionError("fixtures do not separate two-step future area")

    return {
        "thresholds": thresholds,
        "candidate_threshold": candidate,
        "flat_pressures": flat,
        "jump_pressures": jump,
        "shared_one_step_signature": flat_sig,
        "flat_response": flat_response,
        "jump_response": jump_response,
    }


def stage101_two_node_collision() -> dict[str, object]:
    """Two exact P025 orbits with the same one-step +J signature but different +J;+J future."""
    thresholds = (Fraction(1, 1),)
    flat = dyadic_pressures(3, 5, 2, 2)
    jump = dyadic_pressures(3, 41, 2, 2)

    flat_base = activation_area(thresholds, flat[:1])
    jump_base = activation_area(thresholds, jump[:1])
    flat_rank1 = node_rank(thresholds, flat[1])
    jump_rank1 = node_rank(thresholds, jump[1])
    if (flat_base, flat_rank1) != (jump_base, jump_rank1):
        raise AssertionError("fixtures do not share the intended one-step +J signature")

    flat_response = two_node_response(thresholds, flat[:1], flat[1], flat[2])
    jump_response = two_node_response(thresholds, jump[:1], jump[1], jump[2])
    if flat_response.second_node_rank == jump_response.second_node_rank:
        raise AssertionError("fixtures do not separate second-node rank")
    if flat_response.final_area == jump_response.final_area:
        raise AssertionError("fixtures do not separate two-node future area")

    return {
        "thresholds": thresholds,
        "flat_pressures": flat,
        "jump_pressures": jump,
        "shared_one_step_signature": (flat_base, flat_rank1),
        "flat_response": flat_response,
        "jump_response": jump_response,
    }
