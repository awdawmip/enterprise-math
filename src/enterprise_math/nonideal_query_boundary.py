"""Exact boundary for antichain query normalization outside ideal semantics.

For a finite poset P and an arbitrary exact Boolean state X subseteq P, the
query normalization

    S subseteq X  iff  Max_P(S) subseteq X   for every S subseteq P

holds exactly when X is an order ideal.  Thus the width/antichain collapse from
P025 Stages 119-124 is powered by the downward-closure law, not by the mere
presence of a poset label system.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .poset_joint_query_normal import maximal_required_antichain
from .poset_observation_boundary import Element, Relation

State = frozenset[Element]


@dataclass(frozen=True)
class NonIdealBoundaryReport:
    is_ideal: bool
    normalization_valid: bool
    violating_pair: tuple[Element, Element] | None
    violating_query: frozenset[Element] | None


def is_downward_closed(
    elements: tuple[Element, ...], leq: Relation, state: State
) -> bool:
    universe = set(elements)
    if not set(state).issubset(universe):
        raise ValueError("state contains an element outside the universe")
    return all(
        lower in state
        for upper in state
        for lower in elements
        if (lower, upper) in leq
    )


def find_downward_closure_defect(
    elements: tuple[Element, ...], leq: Relation, state: State
) -> tuple[Element, Element] | None:
    for upper in state:
        for lower in elements:
            if lower != upper and (lower, upper) in leq and lower not in state:
                return (lower, upper)
    return None


def query_normalization_holds_for_state(
    elements: tuple[Element, ...], leq: Relation, state: State
) -> bool:
    if not set(state).issubset(set(elements)):
        raise ValueError("state contains an element outside the universe")
    for size in range(len(elements) + 1):
        for subset in combinations(elements, size):
            required = frozenset(subset)
            normal = maximal_required_antichain(elements, leq, required)
            if required.issubset(state) != normal.issubset(state):
                return False
    return True


def analyze_nonideal_boundary(
    elements: tuple[Element, ...], leq: Relation, state: State
) -> NonIdealBoundaryReport:
    ideal = is_downward_closed(elements, leq, state)
    valid = query_normalization_holds_for_state(elements, leq, state)
    if ideal != valid:
        raise AssertionError("antichain normalization is valid iff the state is an ideal")
    defect = find_downward_closure_defect(elements, leq, state)
    violating_query = frozenset(defect) if defect is not None else None
    if defect is not None:
        lower, upper = defect
        normal = maximal_required_antichain(elements, leq, violating_query)
        if normal != frozenset({upper}):
            raise AssertionError("a comparable defect pair should normalize to its upper label")
        if violating_query.issubset(state) == normal.issubset(state):
            raise AssertionError("defect pair failed to witness normalization failure")
    return NonIdealBoundaryReport(
        is_ideal=ideal,
        normalization_valid=valid,
        violating_pair=defect,
        violating_query=violating_query,
    )
