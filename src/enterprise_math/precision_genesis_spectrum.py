"""Exact growth decomposition for R004 path-history collision spectra.

This module refines the monotonicity theorem in ``precision_genesis``.  For a
serial state-extensional relation it separates collision growth into:

1. branch-copy growth: one already-merged history bundle is copied to more than
   one successor; and
2. cross-source growth: histories coming from distinct current states meet at
   one successor.

All quantities are non-negative integers.  The decomposition is an executable
identity used for discovery/regression; its proof is the finite Vandermonde
expansion recorded in the R004 research discussion and Relay #82.
"""
from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from math import comb

from enterprise_math.precision_genesis import (
    Relation,
    State,
    collision_spectrum,
    merge_excess,
    propagate_history_multiplicities,
    serial_on_support,
    successors,
)


def _nat(value: int, name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _predecessors(relation: Relation, target: State) -> frozenset[State]:
    return frozenset(source for source, current_target in relation if current_target == target)


def _used_targets(n: Mapping[State, int], relation: Relation) -> frozenset[State]:
    return frozenset(
        target
        for source, target in relation
        if n.get(source, 0) > 0
    )


@dataclass(frozen=True)
class CollisionGrowth:
    order: int
    total_growth: int
    branch_copy_growth: int
    cross_source_growth: int


@dataclass(frozen=True)
class MergeGrowth:
    total_growth: int
    branch_copy_growth: int
    cross_source_growth: int


def collision_growth_decomposition(
    n: Mapping[State, int], relation: Relation, order: int
) -> CollisionGrowth:
    """Return the exact non-negative decomposition of ``Delta W_order``."""
    _nat(order, "order")
    if order == 0:
        raise ValueError("order must be positive")
    if not serial_on_support(n, relation):
        raise ValueError("relation must be serial on occupied support")
    for count in n.values():
        _nat(count, "multiplicity")

    after = propagate_history_multiplicities(n, relation)
    before_value = dict(collision_spectrum(n, order))[order]
    after_value = dict(collision_spectrum(after, order))[order]

    branch_copy = sum(
        (len(successors(relation, source)) - 1) * comb(count, order)
        for source, count in n.items()
        if count >= order
    )

    cross_source = 0
    for target in _used_targets(n, relation):
        predecessor_counts = tuple(
            n[source]
            for source in _predecessors(relation, target)
            if n.get(source, 0) > 0
        )
        total = sum(predecessor_counts)
        cross_source += comb(total, order) - sum(
            comb(count, order) for count in predecessor_counts if count >= order
        )

    return CollisionGrowth(
        order=order,
        total_growth=after_value - before_value,
        branch_copy_growth=branch_copy,
        cross_source_growth=cross_source,
    )


def merge_growth_decomposition(
    n: Mapping[State, int], relation: Relation
) -> MergeGrowth:
    """Return the exact non-negative decomposition of merge-excess growth."""
    if not serial_on_support(n, relation):
        raise ValueError("relation must be serial on occupied support")
    for count in n.values():
        _nat(count, "multiplicity")

    after = propagate_history_multiplicities(n, relation)
    branch_copy = sum(
        (len(successors(relation, source)) - 1) * max(count - 1, 0)
        for source, count in n.items()
        if count
    )

    cross_source = 0
    for target in _used_targets(n, relation):
        occupied_predecessors = sum(
            n.get(source, 0) > 0
            for source in _predecessors(relation, target)
        )
        cross_source += max(occupied_predecessors - 1, 0)

    return MergeGrowth(
        total_growth=merge_excess(after) - merge_excess(n),
        branch_copy_growth=branch_copy,
        cross_source_growth=cross_source,
    )


def collision_growth_is_strict(
    n: Mapping[State, int], relation: Relation, order: int
) -> bool:
    report = collision_growth_decomposition(n, relation, order)
    return report.branch_copy_growth > 0 or report.cross_source_growth > 0


def merge_growth_is_strict(n: Mapping[State, int], relation: Relation) -> bool:
    report = merge_growth_decomposition(n, relation)
    return report.branch_copy_growth > 0 or report.cross_source_growth > 0
