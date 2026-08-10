"""Finite poset observation states and antichain boundaries.

Stage 113 pressure-tests the total-order merged-rank normal form from P025
Stages 91-112.  When declared observations are partially ordered, an activated
state is modeled as an order ideal.  Cardinality is complete for all such
states exactly when the poset is a chain.  Every finite ideal is instead
reconstructed exactly from its unique maximal antichain boundary.

Order ideals / antichains are classical finite-poset mathematics.  This module
keeps a small exact executable contract for the Enterprise Math precision
specialization; it makes no generic novelty claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Hashable

Element = Hashable
Relation = frozenset[tuple[Element, Element]]
Ideal = frozenset[Element]
Antichain = frozenset[Element]


@dataclass(frozen=True)
class PosetObservationReport:
    elements: tuple[Element, ...]
    is_chain: bool
    ideal_count: int
    antichain_count: int
    rank_complete: bool
    equal_rank_collision: tuple[Ideal, Ideal] | None


def _validate_poset(elements: tuple[Element, ...], leq: Relation) -> None:
    if not isinstance(elements, tuple) or not elements:
        raise ValueError("elements must be a non-empty tuple")
    if len(set(elements)) != len(elements):
        raise ValueError("elements must be distinct")
    universe = set(elements)
    if any(a not in universe or b not in universe for a, b in leq):
        raise ValueError("order relation contains an element outside the universe")
    for x in elements:
        if (x, x) not in leq:
            raise ValueError("order relation must be reflexive")
    for x in elements:
        for y in elements:
            if x != y and (x, y) in leq and (y, x) in leq:
                raise ValueError("order relation must be antisymmetric")
    for x in elements:
        for y in elements:
            if (x, y) not in leq:
                continue
            for z in elements:
                if (y, z) in leq and (x, z) not in leq:
                    raise ValueError("order relation must be transitive")


def is_chain(elements: tuple[Element, ...], leq: Relation) -> bool:
    _validate_poset(elements, leq)
    return all((x, y) in leq or (y, x) in leq for x in elements for y in elements)


def is_order_ideal(elements: tuple[Element, ...], leq: Relation, subset: Ideal) -> bool:
    _validate_poset(elements, leq)
    universe = set(elements)
    if not set(subset).issubset(universe):
        raise ValueError("subset contains an element outside the poset")
    return all(
        lower in subset
        for upper in subset
        for lower in elements
        if (lower, upper) in leq
    )


def enumerate_order_ideals(elements: tuple[Element, ...], leq: Relation) -> tuple[Ideal, ...]:
    _validate_poset(elements, leq)
    ideals: list[Ideal] = []
    for size in range(len(elements) + 1):
        for subset in combinations(elements, size):
            candidate = frozenset(subset)
            if is_order_ideal(elements, leq, candidate):
                ideals.append(candidate)
    return tuple(ideals)


def maximal_boundary(elements: tuple[Element, ...], leq: Relation, ideal: Ideal) -> Antichain:
    if not is_order_ideal(elements, leq, ideal):
        raise ValueError("ideal must be an order ideal")
    return frozenset(
        x
        for x in ideal
        if not any(x != y and (x, y) in leq for y in ideal)
    )


def down_closure(elements: tuple[Element, ...], leq: Relation, boundary: Antichain) -> Ideal:
    _validate_poset(elements, leq)
    universe = set(elements)
    if not set(boundary).issubset(universe):
        raise ValueError("boundary contains an element outside the poset")
    # Requiring an antichain avoids noncanonical redundant generators.
    for x in boundary:
        for y in boundary:
            if x != y and ((x, y) in leq or (y, x) in leq):
                raise ValueError("boundary must be an antichain")
    return frozenset(
        x for x in elements if any((x, top) in leq for top in boundary)
    )


def enumerate_antichains(elements: tuple[Element, ...], leq: Relation) -> tuple[Antichain, ...]:
    _validate_poset(elements, leq)
    antichains: list[Antichain] = []
    for size in range(len(elements) + 1):
        for subset in combinations(elements, size):
            candidate = frozenset(subset)
            if all(
                x == y or ((x, y) not in leq and (y, x) not in leq)
                for x in candidate
                for y in candidate
            ):
                antichains.append(candidate)
    return tuple(antichains)


def antichain_dominates(
    elements: tuple[Element, ...], leq: Relation, left: Antichain, right: Antichain
) -> bool:
    """Return whether down(left) is contained in down(right)."""
    return down_closure(elements, leq, left).issubset(
        down_closure(elements, leq, right)
    )


def analyze_poset_observation(
    elements: tuple[Element, ...], leq: Relation
) -> PosetObservationReport:
    ideals = enumerate_order_ideals(elements, leq)
    antichains = enumerate_antichains(elements, leq)

    # Boundary reconstruction is exact and unique on finite ideals.
    boundaries = tuple(maximal_boundary(elements, leq, ideal) for ideal in ideals)
    reconstructed = tuple(down_closure(elements, leq, boundary) for boundary in boundaries)
    if reconstructed != ideals:
        raise AssertionError("maximal-antichain boundary failed to reconstruct an ideal")
    if len(set(boundaries)) != len(ideals):
        raise AssertionError("distinct ideals must have distinct maximal boundaries")
    if len(ideals) != len(antichains):
        raise AssertionError("finite ideals and antichains must be equinumerous")

    by_size: dict[int, list[Ideal]] = {}
    for ideal in ideals:
        by_size.setdefault(len(ideal), []).append(ideal)
    collision: tuple[Ideal, Ideal] | None = None
    for bucket in by_size.values():
        if len(bucket) > 1:
            collision = (bucket[0], bucket[1])
            break
    rank_complete = collision is None
    chain = is_chain(elements, leq)
    if rank_complete != chain:
        raise AssertionError("ideal cardinality is complete iff the poset is a chain")

    return PosetObservationReport(
        elements=elements,
        is_chain=chain,
        ideal_count=len(ideals),
        antichain_count=len(antichains),
        rank_complete=rank_complete,
        equal_rank_collision=collision,
    )
