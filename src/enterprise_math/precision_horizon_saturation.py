"""Finite-horizon precision repair and saturated actuation for E002.

This stage keeps the centered odd-width quotient from precision-locked actuation
and asks two narrower questions:

1. if only action words up to a finite horizon matter, how much within-cell
   detail is actually forced by that finite future language?
2. does actuator clipping/saturation create a new escape from the exact
   divisibility condition for physical translations?

The answers remain finite and integer-only.  Finite-horizon repair is governed
by reachable action residues modulo the centered cell width.  Saturation leaves
the translation divisibility criterion intact unless the entire clipped output
range already collapses into one coarse precision cell.
"""

from __future__ import annotations

from math import gcd
from typing import Iterable

from .precision_locked_actuation import (
    centered_precision_state,
    precision_cell_width,
)


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _require_nonnegative(name: str, value: int) -> None:
    _require_int(name, value)
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")


def _require_positive_odd(name: str, value: int) -> None:
    _require_int(name, value)
    if value <= 0 or value % 2 == 0:
        raise ValueError(f"{name} must be a positive odd integer")


def _normalize_actions(increments: Iterable[int]) -> tuple[int, ...]:
    actions = tuple(increments)
    if not actions:
        raise ValueError("at least one action increment is required")
    for action in actions:
        _require_int("action increment", action)
    return actions


def reachable_action_residues(
    cell_width: int,
    increments: Iterable[int],
    horizon: int,
) -> tuple[int, ...]:
    """Residues reachable by action words of length at most ``horizon``.

    The empty word contributes residue zero.  Only total physical increment
    modulo ``cell_width`` matters to within-cell future distinguishability.
    """
    _require_positive_odd("cell_width", cell_width)
    _require_nonnegative("horizon", horizon)
    actions = _normalize_actions(increments)
    reachable = {0}
    exact_length = {0}
    for _ in range(horizon):
        exact_length = {
            (residue + action) % cell_width
            for residue in exact_length
            for action in actions
        }
        reachable.update(exact_length)
    return tuple(sorted(reachable))


def finite_horizon_class_count(
    precision: int,
    increments: Iterable[int],
    horizon: int,
) -> int:
    """Exact number of within-cell classes forced by the finite future language."""
    width = precision_cell_width(precision)
    return len(reachable_action_residues(width, increments, horizon))


def finite_horizon_repair_rank(
    error: int,
    precision: int,
    increments: Iterable[int],
    horizon: int,
) -> int:
    """Canonical scalar repair coordinate for all action words up to one horizon.

    Every nonzero reachable residue ``s`` contributes one boundary at ``w-s``.
    These boundaries are nested on the one-dimensional detail fiber, so their
    full truth-vector compresses exactly to the number already crossed.
    """
    _require_int("error", error)
    state = centered_precision_state(error, precision)
    residues = reachable_action_residues(state.width, increments, horizon)
    return sum(
        1
        for residue in residues
        if residue != 0 and state.detail + residue >= state.width
    )


def finite_horizon_repaired_key(
    error: int,
    precision: int,
    increments: Iterable[int],
    horizon: int,
) -> tuple[int, int]:
    """Coarse quotient plus the coarsest scalar detail required up to horizon."""
    state = centered_precision_state(error, precision)
    return (
        state.quotient,
        finite_horizon_repair_rank(error, precision, increments, horizon),
    )


def single_action_horizon_class_count(
    precision: int,
    increment: int,
    horizon: int,
) -> int:
    """Closed form for a one-action finite future: ``min(h+1, w/gcd(w,a))``."""
    _require_int("increment", increment)
    _require_nonnegative("horizon", horizon)
    width = precision_cell_width(precision)
    period = width // gcd(width, abs(increment))
    return min(horizon + 1, period)


def action_family_stable_class_count(
    precision: int,
    increments: Iterable[int],
) -> int:
    """Arbitrary-horizon class count ``w/gcd(w, actions)`` from Stage 2."""
    actions = _normalize_actions(increments)
    width = precision_cell_width(precision)
    common = width
    for action in actions:
        common = gcd(common, abs(action))
    return width // common


def horizon_stabilization_depth(
    precision: int,
    increments: Iterable[int],
) -> int:
    """Smallest horizon at which reachable residues equal the full action subgroup."""
    actions = _normalize_actions(increments)
    target = action_family_stable_class_count(precision, actions)
    width = precision_cell_width(precision)
    horizon = 0
    while True:
        if len(reachable_action_residues(width, actions, horizon)) == target:
            return horizon
        horizon += 1
        if horizon >= target:
            raise AssertionError("finite residue closure exceeded subgroup-size bound")


def clip_integer(value: int, lower: int, upper: int) -> int:
    """Inclusive integer clipping."""
    _require_int("value", value)
    _require_int("lower", lower)
    _require_int("upper", upper)
    if lower > upper:
        raise ValueError("lower must not exceed upper")
    return max(lower, min(upper, value))


def saturation_range_collapses(
    precision: int,
    lower: int,
    upper: int,
) -> bool:
    """Whether the entire clipping output interval belongs to one precision cell."""
    _require_int("lower", lower)
    _require_int("upper", upper)
    if lower > upper:
        raise ValueError("lower must not exceed upper")
    return (
        centered_precision_state(lower, precision).quotient
        == centered_precision_state(upper, precision).quotient
    )


def saturated_translation_descends(
    precision: int,
    increment: int,
    lower: int,
    upper: int,
) -> bool:
    """Exact global compatibility criterion for clipped integer translation.

    ``Q(clip(e+a,L,U))`` is constant on every centered quotient fiber iff
    either the translation is aligned (``w|a``) or the entire saturation range
    already lies inside one output precision cell.
    """
    _require_int("increment", increment)
    width = precision_cell_width(precision)
    return increment % width == 0 or saturation_range_collapses(
        precision,
        lower,
        upper,
    )


def saturated_quotient_step(
    quotient: int,
    precision: int,
    increment: int,
    lower: int,
    upper: int,
) -> int:
    """Apply a compatible saturated translation directly to a coarse quotient.

    A centered representative is sufficient because this function is exposed
    only when the saturated operation is fiber-constant by the theorem above.
    """
    _require_int("quotient", quotient)
    if not saturated_translation_descends(precision, increment, lower, upper):
        raise ValueError("saturated translation does not descend through this precision")
    width = precision_cell_width(precision)
    center = (width - 1) // 2
    representative = width * quotient - center
    output = clip_integer(representative + increment, lower, upper)
    return centered_precision_state(output, precision).quotient
