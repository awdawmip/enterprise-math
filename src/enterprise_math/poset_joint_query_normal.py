"""Antichain normal forms for joint membership queries on finite poset ideals.

For any required label set S and any order ideal I,

    S subseteq I  iff  down(S) subseteq I  iff  Max(S) subseteq I.

Thus joint MAY/MUST membership queries depend only on the maximal antichain of
S.  Raw query arity collapses to the number of incomparable maximal labels,
bounded by poset width.  This is standard poset logic exposed as an exact
operation-language quotient for the P025/A2/A4 pressure test.
"""

from __future__ import annotations

from dataclasses import dataclass

from .poset_boundary_width import poset_width
from .poset_observation_boundary import Antichain, Element, Ideal, Relation


@dataclass(frozen=True)
class JointQueryNormalForm:
    raw_required: frozenset[Element]
    maximal_antichain: Antichain
    raw_arity: int
    essential_arity: int


def maximal_required_antichain(
    elements: tuple[Element, ...], leq: Relation, required: frozenset[Element]
) -> Antichain:
    universe = set(elements)
    if not set(required).issubset(universe):
        raise ValueError("required labels must lie in the poset")
    # Validate relation minimally through width computation.
    poset_width(elements, leq)
    return frozenset(
        x
        for x in required
        if not any(x != y and (x, y) in leq for y in required)
    )


def joint_query_normal_form(
    elements: tuple[Element, ...], leq: Relation, required: frozenset[Element]
) -> JointQueryNormalForm:
    antichain = maximal_required_antichain(elements, leq, required)
    return JointQueryNormalForm(
        raw_required=required,
        maximal_antichain=antichain,
        raw_arity=len(required),
        essential_arity=len(antichain),
    )


def ideal_contains_query(
    elements: tuple[Element, ...], leq: Relation, ideal: Ideal, required: frozenset[Element]
) -> bool:
    from .poset_observation_boundary import maximal_boundary

    maximal_boundary(elements, leq, ideal)  # validates idealhood
    normal = maximal_required_antichain(elements, leq, required)
    return normal.issubset(ideal)


def same_joint_query_future(
    elements: tuple[Element, ...],
    leq: Relation,
    left: frozenset[Element],
    right: frozenset[Element],
) -> bool:
    return maximal_required_antichain(elements, leq, left) == maximal_required_antichain(
        elements, leq, right
    )


def worst_case_essential_arity(
    elements: tuple[Element, ...], leq: Relation, raw_arity_cap: int
) -> int:
    if isinstance(raw_arity_cap, bool) or not isinstance(raw_arity_cap, int) or raw_arity_cap < 0:
        raise ValueError("raw_arity_cap must be a non-negative integer")
    return min(raw_arity_cap, poset_width(elements, leq))
