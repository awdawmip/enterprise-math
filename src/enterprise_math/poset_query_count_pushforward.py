"""Task-relative pushforward of witness multiplicities to a queried subposet.

Let w be a nonnegative multiplicity on ambient ideals J(P), and let Q subseteq P
be the declared query poset.  Push multiplicity forward by restriction:

    w_Q(K) = sum_{I : I intersect Q = K} w(I).

Every count query using labels from Q is exactly the upper zeta transform of
w_Q on J(Q).  Hence full essential query counts recover the projected
multiplicity distribution w_Q, not ambient witness identity.  The exact arity
horizon is width(Q).

This is finite pushforward + incidence-algebra prior mathematics, exposed as a
P025/A2/A4 precision compiler.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from .poset_query_projection import induced_relation, project_ideal_to_query
from .poset_observation_boundary import Element, Ideal, Relation, enumerate_order_ideals
from .poset_witness_count_zeta import (
    count_required_labels,
    counts_by_ideal,
    invert_upper_counts,
    witness_count_transform,
)
from .poset_boundary_width import poset_width


@dataclass(frozen=True)
class QueryCountPushforward:
    query_elements: tuple[Element, ...]
    query_width: int
    projected_multiplicities: tuple[tuple[Ideal, int], ...]
    projected_counts: tuple[tuple[Ideal, int], ...]
    ambient_total: int
    projected_total: int


def _ambient_weights(
    ambient_elements: tuple[Element, ...],
    ambient_leq: Relation,
    multiplicities: Mapping[Ideal, int],
) -> tuple[tuple[Ideal, ...], dict[Ideal, int]]:
    ideals = enumerate_order_ideals(ambient_elements, ambient_leq)
    ideal_set = set(ideals)
    if any(ideal not in ideal_set for ideal in multiplicities):
        raise ValueError("multiplicity map contains a non-ideal ambient state")
    weights: dict[Ideal, int] = {}
    for ideal in ideals:
        value = multiplicities.get(ideal, 0)
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("multiplicities must be non-negative integers")
        weights[ideal] = value
    return ideals, weights


def query_multiplicity_pushforward(
    ambient_elements: tuple[Element, ...],
    ambient_leq: Relation,
    query_elements: tuple[Element, ...],
    multiplicities: Mapping[Ideal, int],
) -> QueryCountPushforward:
    if not query_elements:
        raise ValueError("query_elements must be non-empty")
    if not set(query_elements).issubset(set(ambient_elements)):
        raise ValueError("query elements must lie in the ambient poset")

    ambient_ideals, weights = _ambient_weights(
        ambient_elements, ambient_leq, multiplicities
    )
    q_leq = induced_relation(query_elements, ambient_leq)
    query_ideals = enumerate_order_ideals(query_elements, q_leq)
    projected: dict[Ideal, int] = {ideal: 0 for ideal in query_ideals}
    for ideal in ambient_ideals:
        restricted = project_ideal_to_query(
            ambient_elements, ambient_leq, ideal, query_elements
        )
        projected[restricted] += weights[ideal]

    transform = witness_count_transform(query_elements, q_leq, projected)
    recovered = invert_upper_counts(
        query_elements, q_leq, counts_by_ideal(transform)
    )
    if recovered != projected:
        raise AssertionError("query zeta counts failed to recover projected multiplicities")

    ambient_total = sum(weights.values())
    projected_total = sum(projected.values())
    if ambient_total != projected_total:
        raise AssertionError("restriction pushforward must conserve total multiplicity")

    return QueryCountPushforward(
        query_elements=query_elements,
        query_width=poset_width(query_elements, q_leq),
        projected_multiplicities=tuple((ideal, projected[ideal]) for ideal in query_ideals),
        projected_counts=tuple(zip(transform.ideals, transform.upper_counts, strict=True)),
        ambient_total=ambient_total,
        projected_total=projected_total,
    )


def ambient_query_count(
    ambient_elements: tuple[Element, ...],
    ambient_leq: Relation,
    multiplicities: Mapping[Ideal, int],
    required_in_query: frozenset[Element],
) -> int:
    return count_required_labels(
        ambient_elements, ambient_leq, multiplicities, required_in_query
    )
