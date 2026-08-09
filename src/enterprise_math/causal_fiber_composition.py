"""Finite LEGO alternative/product composition before semiring shadows.

The primitive operations here are structural:

* tagged disjoint alternative: one fine possibility comes from the left OR right;
* joint product: choose one left possibility AND one right possibility.

Finite set identities force associativity/distributivity before any numeric
algebra is selected.  Different observations then render those same structures
as count (+,*), existence (or,and), or minimum-additive-cost (min,+) laws.
"""

from __future__ import annotations

from typing import Hashable


State = Hashable
Tagged = tuple[str, State]


def tagged_alternative(left: frozenset[State], right: frozenset[State]) -> frozenset[Tagged]:
    """Disjoint alternative even when raw state labels overlap."""
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise ValueError("left and right must be frozensets")
    return frozenset({("L", state) for state in left} | {("R", state) for state in right})


def joint_product(left: frozenset[State], right: frozenset[State]) -> frozenset[tuple[State, State]]:
    """All jointly composable independent choice pairs."""
    if not isinstance(left, frozenset) or not isinstance(right, frozenset):
        raise ValueError("left and right must be frozensets")
    return frozenset((a, b) for a in left for b in right)


def count_observation(states: frozenset[State]) -> int:
    if not isinstance(states, frozenset):
        raise ValueError("states must be a frozenset")
    return len(states)


def existence_observation(states: frozenset[State]) -> bool:
    if not isinstance(states, frozenset):
        raise ValueError("states must be a frozenset")
    return bool(states)


def minimum_cost(costs: dict[State, int]) -> int | None:
    """Minimum integer cost; None is the impossible/empty alternative."""
    if not isinstance(costs, dict):
        raise ValueError("costs must be a dict")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in costs.values()):
        raise ValueError("costs must be integers")
    return None if not costs else min(costs.values())


def alternative_minimum(left: int | None, right: int | None) -> int | None:
    """Observation shadow of alternative composition for minimum cost."""
    if left is None:
        return right
    if right is None:
        return left
    return min(left, right)


def joint_additive_minimum(left: int | None, right: int | None) -> int | None:
    """Observation shadow of joint product when pair costs add."""
    if left is None or right is None:
        return None
    return left + right


def count_distributive_identity(
    left: frozenset[State],
    middle: frozenset[State],
    right: frozenset[State],
) -> bool:
    """Cardinality shadow of A x (B disjoint-union C)."""
    alternative = tagged_alternative(middle, right)
    whole = joint_product(left, alternative)
    return count_observation(whole) == (
        count_observation(joint_product(left, middle))
        + count_observation(joint_product(left, right))
    )
