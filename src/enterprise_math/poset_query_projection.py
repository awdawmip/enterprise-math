"""Task-relative membership projection for finite poset observation states.

If ambient states are order ideals I of a finite poset P and a declared future
asks only labelled membership on Q subseteq P, then the exact semantic state is
I intersect Q.  These signatures are precisely the order ideals of the induced
subposet Q, and their maximal-antichain boundary has worst-case size width(Q).

This is a classical restriction fact for order ideals.  The module exposes it
as an exact task-relative precision compiler; no generic novelty claim is made.
"""

from __future__ import annotations

from dataclasses import dataclass

from .poset_boundary_width import analyze_boundary_width
from .poset_observation_boundary import (
    Antichain,
    Element,
    Ideal,
    Relation,
    down_closure,
    enumerate_order_ideals,
    maximal_boundary,
)


@dataclass(frozen=True)
class PosetQueryProjectionReport:
    query_elements: tuple[Element, ...]
    query_width: int
    query_ideal_count: int
    ambient_ideal_count: int
    signature_count: int
    all_query_ideals_realizable: bool
    scalar_rank_complete: bool


def induced_relation(query_elements: tuple[Element, ...], leq: Relation) -> Relation:
    query_set = set(query_elements)
    if len(query_set) != len(query_elements):
        raise ValueError("query elements must be distinct")
    return frozenset((x, y) for x, y in leq if x in query_set and y in query_set)


def project_ideal_to_query(
    ambient_elements: tuple[Element, ...],
    ambient_leq: Relation,
    ideal: Ideal,
    query_elements: tuple[Element, ...],
) -> Ideal:
    query_set = frozenset(query_elements)
    if not query_set.issubset(set(ambient_elements)):
        raise ValueError("query elements must lie in the ambient poset")
    # maximal_boundary validates ambient idealhood.
    maximal_boundary(ambient_elements, ambient_leq, ideal)
    return frozenset(ideal.intersection(query_set))


def query_boundary(
    ambient_elements: tuple[Element, ...],
    ambient_leq: Relation,
    ideal: Ideal,
    query_elements: tuple[Element, ...],
) -> Antichain:
    projected = project_ideal_to_query(
        ambient_elements, ambient_leq, ideal, query_elements
    )
    q_leq = induced_relation(query_elements, ambient_leq)
    return maximal_boundary(query_elements, q_leq, projected)


def lift_query_ideal(
    ambient_elements: tuple[Element, ...],
    ambient_leq: Relation,
    query_elements: tuple[Element, ...],
    query_ideal: Ideal,
) -> Ideal:
    """Lift a query ideal to one ambient ideal whose query projection is exact."""
    q_leq = induced_relation(query_elements, ambient_leq)
    boundary = maximal_boundary(query_elements, q_leq, query_ideal)
    ambient = down_closure(ambient_elements, ambient_leq, boundary)
    projected = project_ideal_to_query(
        ambient_elements, ambient_leq, ambient, query_elements
    )
    if projected != query_ideal:
        raise AssertionError("query ideal failed to lift exactly")
    return ambient


def analyze_query_projection(
    ambient_elements: tuple[Element, ...],
    ambient_leq: Relation,
    query_elements: tuple[Element, ...],
) -> PosetQueryProjectionReport:
    query_set = set(query_elements)
    if not query_elements:
        raise ValueError("query_elements must be non-empty")
    if not query_set.issubset(set(ambient_elements)):
        raise ValueError("query elements must lie in the ambient poset")

    ambient_ideals = enumerate_order_ideals(ambient_elements, ambient_leq)
    q_leq = induced_relation(query_elements, ambient_leq)
    query_ideals = enumerate_order_ideals(query_elements, q_leq)
    signatures = {
        project_ideal_to_query(
            ambient_elements, ambient_leq, ideal, query_elements
        )
        for ideal in ambient_ideals
    }
    all_realizable = signatures == set(query_ideals)
    if not all_realizable:
        raise AssertionError("query signatures must equal the induced ideal lattice")

    q_width = analyze_boundary_width(query_elements, q_leq).width
    by_size: dict[int, set[Ideal]] = {}
    for ideal in query_ideals:
        by_size.setdefault(len(ideal), set()).add(ideal)
    scalar_complete = all(len(bucket) == 1 for bucket in by_size.values())
    if scalar_complete != (q_width == 1):
        raise AssertionError("query cardinality is complete iff the query poset is a chain")

    return PosetQueryProjectionReport(
        query_elements=query_elements,
        query_width=q_width,
        query_ideal_count=len(query_ideals),
        ambient_ideal_count=len(ambient_ideals),
        signature_count=len(signatures),
        all_query_ideals_realizable=all_realizable,
        scalar_rank_complete=scalar_complete,
    )
