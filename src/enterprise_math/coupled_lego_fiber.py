"""Coupled composition of finite LEGO fibers.

Free LEGO composition pairs a left fine state u and right fine state v whenever
their coarse totals sum to the requested total.  Geometry, material rules,
support constraints, or extra cross-future distinctions are represented by a
local nonnegative-integer coupling multiplicity

    kappa(u,v) in N_0.

0 forbids the pairing, 1 is ordinary unique composition, and values >1 mean
multiple joint causal states lie over the same lower-dimensional pair.

Thus constrained/high-dimensional counting is generated from lower-dimensional
fine states plus a coupling law; the unit values themselves are unchanged.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Hashable

State = Hashable


def states_by_total(
    state_totals: dict[State, int],
) -> dict[int, tuple[State, ...]]:
    if not isinstance(state_totals, dict):
        raise ValueError("state_totals must be a dict")
    grouped: dict[int, list[State]] = defaultdict(list)
    for state, total in state_totals.items():
        if isinstance(total, bool) or not isinstance(total, int):
            raise ValueError("totals must be integers")
        grouped[total].append(state)
    return {
        total: tuple(sorted(states, key=repr))
        for total, states in grouped.items()
    }


def coupled_fiber_count(
    left_totals: dict[State, int],
    right_totals: dict[State, int],
    total: int,
    coupling: dict[tuple[State, State], int],
) -> int:
    """Count joint states over all lower-dimensional pairs summing to total."""
    if isinstance(total, bool) or not isinstance(total, int):
        raise ValueError("total must be an integer")
    result = 0
    for left, left_total in left_totals.items():
        for right, right_total in right_totals.items():
            if left_total + right_total != total:
                continue
            multiplicity = coupling.get((left, right), 0)
            if isinstance(multiplicity, bool) or not isinstance(multiplicity, int) or multiplicity < 0:
                raise ValueError("coupling multiplicities must be non-negative integers")
            result += multiplicity
    return result


def free_coupling(
    left_states: tuple[State, ...],
    right_states: tuple[State, ...],
) -> dict[tuple[State, State], int]:
    """Independent unique composition: every lower-dimensional pair has kappa=1."""
    return {
        (left, right): 1
        for left in left_states
        for right in right_states
    }


def coupling_support(
    coupling: dict[tuple[State, State], int],
) -> frozenset[tuple[State, State]]:
    """Pairs with at least one admissible joint state."""
    for value in coupling.values():
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("coupling multiplicities must be non-negative integers")
    return frozenset(pair for pair, value in coupling.items() if value > 0)


def coupling_split_excess(
    coupling: dict[tuple[State, State], int],
) -> int:
    """Extra joint distinctions beyond one state per supported pair."""
    for value in coupling.values():
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("coupling multiplicities must be non-negative integers")
    return sum(max(value - 1, 0) for value in coupling.values())
