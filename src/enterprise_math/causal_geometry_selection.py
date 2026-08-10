"""Causal selection diagnostics for minimum-resolution relation geometries.

This layer keeps two questions distinct:

1. conservation ontology: what fine displacements are allowed before geometry is
   named;
2. continuation isotropy: at what relation arity and future depth do compatible
   primitive-direction contexts first become distinguishable?

The resulting diagnostics are typed and Pareto-like.  They are not a scalar
physical-isotropy score.
"""

from __future__ import annotations

from dataclasses import dataclass

from .causal_primitive_link_profile import (
    Adjacency,
    PrimitiveLinkProfile,
    cliques_of_size,
    flag_future_signature_histogram,
)


@dataclass(frozen=True)
class SplitPoint:
    relation_arity: int
    future_depth: int
    type_count: int


def continuation_type_count(
    adjacency: Adjacency,
    relation_arity: int,
    future_depth: int,
) -> int:
    return len(
        flag_future_signature_histogram(
            adjacency,
            relation_arity,
            future_depth,
        )
    )


def anisotropy_split_frontier(
    adjacency: Adjacency,
    maximum_relation_arity: int,
    maximum_future_depth: int,
) -> tuple[SplitPoint, ...]:
    """Coordinatewise-minimal `(arity,depth)` contexts with >1 future type."""
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in (maximum_relation_arity, maximum_future_depth)
    ):
        raise ValueError("maximum arity and depth must be positive integers")
    split_points = []
    for arity in range(1, maximum_relation_arity + 1):
        if not cliques_of_size(adjacency, arity):
            break
        for depth in range(1, maximum_future_depth + 1):
            count = continuation_type_count(adjacency, arity, depth)
            if count <= 1:
                continue
            split_points.append(SplitPoint(arity, depth, count))
    frontier = []
    for point in split_points:
        dominated = any(
            other.relation_arity <= point.relation_arity
            and other.future_depth <= point.future_depth
            and (
                other.relation_arity < point.relation_arity
                or other.future_depth < point.future_depth
            )
            for other in split_points
        )
        if not dominated:
            frontier.append(point)
    return tuple(sorted(frontier, key=lambda point: (point.relation_arity, point.future_depth)))


def full_rank_flag_coherence(profile: PrimitiveLinkProfile, relation_rank: int) -> bool:
    """Candidate full-rank coherence gate for a declared relation rank.

    Requires compatible flags through exactly the declared rank, singleton
    one-step continuation histograms at every size, and no continuation beyond a
    rank-sized flag.  It does not assert physical uniqueness.
    """
    if isinstance(relation_rank, bool) or not isinstance(relation_rank, int) or relation_rank <= 0:
        raise ValueError("relation_rank must be positive")
    histograms = tuple(dict(hist) for hist in profile.flag_extension_histograms)
    if len(histograms) < relation_rank:
        return False
    if any(len(histograms[index]) != 1 for index in range(relation_rank)):
        return False
    final = histograms[relation_rank - 1]
    return set(final) == {0}


def symmetric_integer_charge_is_total(coefficients: tuple[int, ...]) -> bool:
    """A nonzero linear charge invariant under every slot permutation is total charge up to scale."""
    if not coefficients or any(isinstance(value, bool) or not isinstance(value, int) for value in coefficients):
        raise ValueError("coefficients must be a non-empty integer tuple")
    return coefficients[0] != 0 and len(set(coefficients)) == 1


def minimal_ambient_slots_for_exact_charge(relation_rank: int, exact_charge_rank: int = 1) -> int:
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in (relation_rank, exact_charge_rank)
    ):
        raise ValueError("ranks must be non-negative integers")
    if relation_rank == 0 and exact_charge_rank == 0:
        return 0
    return relation_rank + exact_charge_rank


def anonymous_single_charge_forces_a_dimension(relation_rank: int) -> tuple[int, int]:
    """Return `(slot_count, kernel_rank)` for the minimal anonymous one-charge ontology."""
    if isinstance(relation_rank, bool) or not isinstance(relation_rank, int) or relation_rank <= 0:
        raise ValueError("relation_rank must be positive")
    slot_count = minimal_ambient_slots_for_exact_charge(relation_rank, 1)
    return slot_count, slot_count - 1
