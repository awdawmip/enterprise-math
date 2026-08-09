"""Exact finite interaction decomposition for LEGO unit subsets.

A response T on finite sets of labeled unit blocks is decomposed by Boolean
inclusion-exclusion.  The interaction attached to S is the effect that remains
after every lower-order subset contribution is removed:

    I(S) = sum_{A subset S} (-1)^(|S|-|A|) T(A).

Möbius inversion gives the exact reconstruction

    T(S) = sum_{A subset S} I(A).

This is finite integer interaction accounting, not a derivative/Taylor
approximation.  Vanishing interactions of order >=2 is the exact LEGO analogue
of additive independent-unit behavior on the tested unit family.
"""

from __future__ import annotations

from itertools import combinations
from typing import Hashable


Label = Hashable
Vector = tuple[int, ...]
ResponseTable = dict[frozenset[Label], Vector]


def _subsets(items: frozenset[Label]):
    ordered = tuple(sorted(items, key=repr))
    for size in range(len(ordered) + 1):
        for combo in combinations(ordered, size):
            yield frozenset(combo)


def _require_response_table(table: ResponseTable) -> int:
    if not isinstance(table, dict) or not table:
        raise ValueError("response table must be a non-empty dict")
    if frozenset() not in table:
        raise ValueError("response table must include the empty unit state")
    dimension = len(table[frozenset()])
    if dimension == 0:
        raise ValueError("response vectors must have positive dimension")
    for state, value in table.items():
        if not isinstance(state, frozenset):
            raise ValueError("response states must be frozensets")
        if not isinstance(value, tuple) or len(value) != dimension:
            raise ValueError("response vectors must share one dimension")
        if any(isinstance(entry, bool) or not isinstance(entry, int) for entry in value):
            raise ValueError("response entries must be integers")
    return dimension


def _add(left: Vector, right: Vector) -> Vector:
    return tuple(a + b for a, b in zip(left, right))


def _scale(sign: int, value: Vector) -> Vector:
    return tuple(sign * entry for entry in value)


def interaction_for_subset(table: ResponseTable, subset: frozenset[Label]) -> Vector:
    """Exact interaction I(S) for one labeled unit subset S."""
    dimension = _require_response_table(table)
    if not isinstance(subset, frozenset):
        raise ValueError("subset must be a frozenset")
    missing = [part for part in _subsets(subset) if part not in table]
    if missing:
        raise ValueError("response table must contain every subset of the requested state")

    total = tuple(0 for _ in range(dimension))
    for part in _subsets(subset):
        sign = -1 if (len(subset) - len(part)) % 2 else 1
        total = _add(total, _scale(sign, table[part]))
    return total


def interaction_spectrum(table: ResponseTable) -> ResponseTable:
    """Compute I(S) for every state present in a downward-closed response table."""
    _require_response_table(table)
    for state in table:
        if any(part not in table for part in _subsets(state)):
            raise ValueError("response table must be downward closed")
    return {state: interaction_for_subset(table, state) for state in table}


def reconstruct_response(
    interactions: ResponseTable, subset: frozenset[Label]
) -> Vector:
    """Exact reconstruction T(S)=sum_{A subset S} I(A)."""
    dimension = _require_response_table(interactions)
    if not isinstance(subset, frozenset):
        raise ValueError("subset must be a frozenset")
    total = tuple(0 for _ in range(dimension))
    for part in _subsets(subset):
        if part not in interactions:
            raise ValueError("interaction table must contain every subset")
        total = _add(total, interactions[part])
    return total


def interaction_order(interactions: ResponseTable) -> int:
    """Largest unit-set size carrying a nonzero interaction, or 0 if none."""
    _require_response_table(interactions)
    result = 0
    for subset, value in interactions.items():
        if any(value):
            result = max(result, len(subset))
    return result


def has_higher_interactions(interactions: ResponseTable, minimum_order: int = 2) -> bool:
    """Whether any nonzero interaction of at least the requested order exists."""
    if (
        isinstance(minimum_order, bool)
        or not isinstance(minimum_order, int)
        or minimum_order < 0
    ):
        raise ValueError("minimum_order must be a non-negative integer")
    _require_response_table(interactions)
    return any(
        len(subset) >= minimum_order and any(value)
        for subset, value in interactions.items()
    )
