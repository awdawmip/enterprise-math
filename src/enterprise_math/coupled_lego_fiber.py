"""Coupled composition of finite LEGO fibers.

Free LEGO composition pairs a left fine state u and right fine state v whenever
their coarse totals sum to the requested total. Geometry, material rules,
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
from dataclasses import dataclass
from typing import Hashable

State = Hashable


@dataclass(frozen=True)
class FiberCouplingDefect:
    total: int
    free_pairings: int
    coupled_states: int
    missing_support: int
    split_excess: int

    @property
    def signed_count_defect(self) -> int:
        return self.coupled_states - self.free_pairings

    @property
    def identity_holds(self) -> bool:
        return self.coupled_states == self.free_pairings - self.missing_support + self.split_excess


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


def _eligible_pairs(
    left_totals: dict[State, int],
    right_totals: dict[State, int],
    total: int,
) -> tuple[tuple[State, State], ...]:
    if isinstance(total, bool) or not isinstance(total, int):
        raise ValueError("total must be an integer")
    return tuple(
        (left, right)
        for left, left_total in left_totals.items()
        for right, right_total in right_totals.items()
        if left_total + right_total == total
    )


def coupled_fiber_count(
    left_totals: dict[State, int],
    right_totals: dict[State, int],
    total: int,
    coupling: dict[tuple[State, State], int],
) -> int:
    """Count joint states over all lower-dimensional pairs summing to total."""
    result = 0
    for pair in _eligible_pairs(left_totals, right_totals, total):
        multiplicity = coupling.get(pair, 0)
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


def fiber_coupling_defect(
    left_totals: dict[State, int],
    right_totals: dict[State, int],
    total: int,
    coupling: dict[tuple[State, State], int],
) -> FiberCouplingDefect:
    """Typed defect relative to free unique LEGO pairing at one coarse total.

    For eligible lower-dimensional pairs P_total,

        H_kappa = |P_total| - M_total + S_total,

    where M counts pairs with kappa=0 and S=sum max(kappa-1,0).
    Keeping M and S separate prevents forbidden pairings and extra joint states
    from cancelling in one signed scalar.
    """
    pairs = _eligible_pairs(left_totals, right_totals, total)
    missing = 0
    split = 0
    coupled = 0
    for pair in pairs:
        value = coupling.get(pair, 0)
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("coupling multiplicities must be non-negative integers")
        coupled += value
        if value == 0:
            missing += 1
        elif value > 1:
            split += value - 1
    result = FiberCouplingDefect(
        total=total,
        free_pairings=len(pairs),
        coupled_states=coupled,
        missing_support=missing,
        split_excess=split,
    )
    if not result.identity_holds:
        raise AssertionError("typed fiber coupling identity failed")
    return result
