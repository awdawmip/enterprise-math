"""Rectangular vector precision and integer translation actions for E002.

The scalar E002 horizon formula ``c_h = |S_h|`` is one-dimensional.  For a
rectangular vector quotient, future output exposes each coordinate quotient
separately.  A reachable residue vector can therefore contribute one threshold
on every coordinate at once, and correlations between action coordinates do
not in general reduce the amount of physical phase needed by the full vector
observable.

This module derives the exact replacement: if ``S_h`` is the finite set of
reachable residue vectors, the future-safe within-cell partition has cardinality
``prod_i |proj_i S_h|``.  At arbitrary horizon the coordinate projections are
cyclic subgroups selected by coordinate-wise gcds.  The gap between the full
action subgroup and the product of its coordinate projections is an integer
correlation-expansion factor; it is a negative boundary against naively using
only subgroup cardinality or a scalar gcd in multiple dimensions.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import reduce
from math import gcd, lcm
from operator import mul
from typing import Iterable, Sequence


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _normalize_widths(widths: Sequence[int]) -> tuple[int, ...]:
    values = tuple(widths)
    if not values:
        raise ValueError("at least one coordinate width is required")
    for width in values:
        _require_int("cell width", width)
        if width <= 0 or width % 2 == 0:
            raise ValueError("every centered cell width must be a positive odd integer")
    return values


def _normalize_vector(
    vector: Sequence[int],
    dimension: int,
    name: str,
) -> tuple[int, ...]:
    values = tuple(vector)
    if len(values) != dimension:
        raise ValueError(f"{name} must have dimension {dimension}")
    for value in values:
        _require_int(name, value)
    return values


def _normalize_actions(
    actions: Iterable[Sequence[int]],
    dimension: int,
) -> tuple[tuple[int, ...], ...]:
    values = tuple(_normalize_vector(action, dimension, "action coordinate") for action in actions)
    if not values:
        raise ValueError("at least one vector action is required")
    return values


def _product(values: Iterable[int]) -> int:
    return reduce(mul, values, 1)


@dataclass(frozen=True)
class CenteredVectorState:
    """Exact rectangular centered quotient/detail chart."""

    quotient: tuple[int, ...]
    detail: tuple[int, ...]
    widths: tuple[int, ...]

    def reconstruct(self) -> tuple[int, ...]:
        return tuple(
            width * quotient + detail - (width - 1) // 2
            for quotient, detail, width in zip(self.quotient, self.detail, self.widths)
        )


def centered_vector_state(
    point: Sequence[int],
    widths: Sequence[int],
) -> CenteredVectorState:
    """Apply the exact centered Euclidean chart independently on each axis."""
    normalized_widths = _normalize_widths(widths)
    normalized_point = _normalize_vector(point, len(normalized_widths), "point coordinate")
    quotient: list[int] = []
    detail: list[int] = []
    for coordinate, width in zip(normalized_point, normalized_widths):
        center = (width - 1) // 2
        q, r = divmod(coordinate + center, width)
        quotient.append(q)
        detail.append(r)
    return CenteredVectorState(tuple(quotient), tuple(detail), normalized_widths)


def vector_translation_descends(
    widths: Sequence[int],
    increment: Sequence[int],
) -> bool:
    """Whether one vector translation is exact on the rectangular quotient."""
    normalized_widths = _normalize_widths(widths)
    action = _normalize_vector(increment, len(normalized_widths), "increment coordinate")
    return all(value % width == 0 for value, width in zip(action, normalized_widths))


def vector_translation_certificate(
    point: Sequence[int],
    widths: Sequence[int],
    increment: Sequence[int],
) -> dict[str, tuple[int, ...]]:
    """Exact coordinate-wise bulk/detail/carry transport for one vector action."""
    state = centered_vector_state(point, widths)
    action = _normalize_vector(increment, len(state.widths), "increment coordinate")
    bulk: list[int] = []
    action_detail: list[int] = []
    carry: list[int] = []
    next_q: list[int] = []
    next_r: list[int] = []
    for q, r, width, value in zip(state.quotient, state.detail, state.widths, action):
        k, s = divmod(value, width)
        gamma = int(r + s >= width)
        bulk.append(k)
        action_detail.append(s)
        carry.append(gamma)
        next_q.append(q + k + gamma)
        next_r.append((r + s) % width)
    direct_point = tuple(coordinate + value for coordinate, value in zip(point, action))
    direct = centered_vector_state(direct_point, state.widths)
    if tuple(next_q) != direct.quotient or tuple(next_r) != direct.detail:
        raise AssertionError("vector translation certificate failed exact reconstruction")
    return {
        "quotient_before": state.quotient,
        "detail_before": state.detail,
        "bulk": tuple(bulk),
        "action_detail": tuple(action_detail),
        "carry": tuple(carry),
        "quotient_after": tuple(next_q),
        "detail_after": tuple(next_r),
    }


def reachable_vector_residues(
    widths: Sequence[int],
    actions: Iterable[Sequence[int]],
    horizon: int,
) -> tuple[tuple[int, ...], ...]:
    """Residue vectors reachable by action words of length at most ``horizon``."""
    normalized_widths = _normalize_widths(widths)
    _require_int("horizon", horizon)
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    normalized_actions = _normalize_actions(actions, len(normalized_widths))
    zero = tuple(0 for _ in normalized_widths)
    reachable = {zero}
    exact_length = {zero}
    for _ in range(horizon):
        exact_length = {
            tuple(
                (residue[index] + action[index]) % normalized_widths[index]
                for index in range(len(normalized_widths))
            )
            for residue in exact_length
            for action in normalized_actions
        }
        reachable.update(exact_length)
    return tuple(sorted(reachable))


def projected_residue_sets(
    widths: Sequence[int],
    residues: Iterable[Sequence[int]],
) -> tuple[tuple[int, ...], ...]:
    """Coordinate projections of a finite residue-vector set."""
    normalized_widths = _normalize_widths(widths)
    normalized_residues = tuple(
        _normalize_vector(residue, len(normalized_widths), "residue coordinate")
        for residue in residues
    )
    if not normalized_residues:
        raise ValueError("residue set must be nonempty")
    return tuple(
        tuple(sorted({residue[index] % normalized_widths[index] for residue in normalized_residues}))
        for index in range(len(normalized_widths))
    )


def vector_horizon_class_count(
    widths: Sequence[int],
    actions: Iterable[Sequence[int]],
    horizon: int,
) -> int:
    """Exact within-cell class count for full vector quotient output up to one horizon."""
    residues = reachable_vector_residues(widths, actions, horizon)
    projections = projected_residue_sets(widths, residues)
    return _product(len(projection) for projection in projections)


def vector_horizon_repair_rank(
    point: Sequence[int],
    widths: Sequence[int],
    actions: Iterable[Sequence[int]],
    horizon: int,
) -> tuple[int, ...]:
    """Coordinate-wise scalar ranks for the exact finite-horizon repair."""
    state = centered_vector_state(point, widths)
    residues = reachable_vector_residues(state.widths, actions, horizon)
    projections = projected_residue_sets(state.widths, residues)
    ranks: list[int] = []
    for detail, width, projection in zip(state.detail, state.widths, projections):
        ranks.append(
            sum(
                1
                for residue in projection
                if residue != 0 and detail + residue >= width
            )
        )
    return tuple(ranks)


def vector_horizon_repaired_key(
    point: Sequence[int],
    widths: Sequence[int],
    actions: Iterable[Sequence[int]],
    horizon: int,
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Full vector quotient plus coordinate repair ranks."""
    state = centered_vector_state(point, widths)
    return (
        state.quotient,
        vector_horizon_repair_rank(point, state.widths, actions, horizon),
    )


def vector_stable_widths(
    widths: Sequence[int],
    actions: Iterable[Sequence[int]],
) -> tuple[int, ...]:
    """Coarsest axis-aligned arbitrary-horizon refinement for a vector action family."""
    normalized_widths = _normalize_widths(widths)
    normalized_actions = _normalize_actions(actions, len(normalized_widths))
    result: list[int] = []
    for index, width in enumerate(normalized_widths):
        common = width
        for action in normalized_actions:
            common = gcd(common, abs(action[index]))
        result.append(common)
    return tuple(result)


def vector_stable_class_count(
    widths: Sequence[int],
    actions: Iterable[Sequence[int]],
) -> int:
    """Arbitrary-horizon future class count for the full rectangular quotient."""
    normalized_widths = _normalize_widths(widths)
    stable = vector_stable_widths(normalized_widths, actions)
    return _product(width // divisor for width, divisor in zip(normalized_widths, stable))


def reachable_vector_subgroup(
    widths: Sequence[int],
    actions: Iterable[Sequence[int]],
) -> tuple[tuple[int, ...], ...]:
    """Full finite subgroup of residue vectors generated by the actions."""
    normalized_widths = _normalize_widths(widths)
    normalized_actions = _normalize_actions(actions, len(normalized_widths))
    zero = tuple(0 for _ in normalized_widths)
    reachable = {zero}
    frontier = {zero}
    while frontier:
        next_frontier = {
            tuple(
                (residue[index] + action[index]) % normalized_widths[index]
                for index in range(len(normalized_widths))
            )
            for residue in frontier
            for action in normalized_actions
        } - reachable
        reachable.update(next_frontier)
        frontier = next_frontier
    return tuple(sorted(reachable))


def vector_correlation_expansion_factor(
    widths: Sequence[int],
    actions: Iterable[Sequence[int]],
) -> int:
    """Index of the action subgroup in the product of its coordinate projections.

    A value greater than one means subgroup cardinality undercounts the detail
    classes required when the full vector quotient is observed coordinate-wise.
    """
    normalized_widths = _normalize_widths(widths)
    subgroup = reachable_vector_subgroup(normalized_widths, actions)
    projections = projected_residue_sets(normalized_widths, subgroup)
    rectangular_count = _product(len(projection) for projection in projections)
    if rectangular_count % len(subgroup) != 0:
        raise AssertionError("action subgroup must embed in product of coordinate projections")
    return rectangular_count // len(subgroup)


def single_vector_action_horizon_class_count(
    widths: Sequence[int],
    action: Sequence[int],
    horizon: int,
) -> int:
    """Closed form ``prod_i min(h+1, w_i/gcd(w_i,a_i))`` for one repeated vector action."""
    normalized_widths = _normalize_widths(widths)
    normalized_action = _normalize_vector(action, len(normalized_widths), "action coordinate")
    _require_int("horizon", horizon)
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    return _product(
        min(horizon + 1, width // gcd(width, abs(value)))
        for width, value in zip(normalized_widths, normalized_action)
    )


def single_vector_action_subgroup_order(
    widths: Sequence[int],
    action: Sequence[int],
) -> int:
    """Order of one residue vector: lcm of its coordinate periods."""
    normalized_widths = _normalize_widths(widths)
    normalized_action = _normalize_vector(action, len(normalized_widths), "action coordinate")
    order = 1
    for width, value in zip(normalized_widths, normalized_action):
        order = lcm(order, width // gcd(width, abs(value)))
    return order
