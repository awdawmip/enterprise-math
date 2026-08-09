"""Relational extension of the finite collision spectrum for A4.

Semantic replay from the historical E001/A4 route. For one finite relation
``R subset X x Z``, let

    c_z = |{x in X : (x,z) in R}|,
    W_k(R) = sum_z binom(c_z, k).

``W_k`` counts k-source common-target *witnesses*, with multiplicity when one
source group shares several targets.

A second quantity removes witness multiplicity:

    G_k(R) = #{A subset X : |A|=k and all x in A share at least one target}.

For a general multi-valued relation the two spectra differ. Under deterministic
postcomposition of targets, ``G_k`` cannot decrease because every old common
target retains an image, while ``W_k`` can decrease when several old witnesses
coalesce to one target.

If ``R`` is the graph of a total single-valued function ``F : X -> Z``, then

    W_k(graph(F)) = G_k(graph(F))
                  = sum_z binom(|F^{-1}(z)|, k),

which is exactly the P011 finite collision spectrum. Thus A4 retains an explicit
function-graph degeneration rather than duplicating the A1/P011 theory.

Generic relation/hypergraph incidence mathematics is established prior art; this
module records the exact finite specialization and failure boundary consumed by
Enterprise Math.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Hashable, Iterable, Mapping
from itertools import combinations
from math import comb

Source = Hashable
Target = Hashable
Relation = frozenset[tuple[Source, Target]]


def relation_target_occupancies(relation: Relation) -> dict[Target, int]:
    """Count distinct incident sources at every target of a finite relation."""
    occupancies: Counter[Target] = Counter()
    for _source, target in relation:
        occupancies[target] += 1
    return dict(occupancies)


def relation_source_supports(
    sources: Iterable[Source], relation: Relation
) -> dict[Source, frozenset[Target]]:
    """Return each declared source's finite target support, including empty ones."""
    source_tuple = tuple(sources)
    if len(source_tuple) != len(set(source_tuple)):
        raise ValueError("sources must be distinct")
    support: dict[Source, set[Target]] = {source: set() for source in source_tuple}
    for source, target in relation:
        if source not in support:
            raise ValueError("relation contains an undeclared source")
        support[source].add(target)
    return {source: frozenset(targets) for source, targets in support.items()}


def relation_overlap_spectrum(
    relation: Relation, max_order: int | None = None
) -> tuple[tuple[int, int], ...]:
    """Return witness spectrum ``W_k=sum_z binom(c_z,k)``."""
    occupancies = relation_target_occupancies(relation)
    observed_max = max(occupancies.values(), default=0)
    if max_order is None:
        max_order = observed_max
    if isinstance(max_order, bool) or not isinstance(max_order, int) or max_order < 0:
        raise ValueError("max_order must be a non-negative integer")
    return tuple(
        (
            order,
            sum(comb(count, order) for count in occupancies.values() if count >= order),
        )
        for order in range(1, max_order + 1)
    )


def relation_group_collision_spectrum(
    sources: Iterable[Source], relation: Relation, max_order: int | None = None
) -> tuple[tuple[int, int], ...]:
    """Return ``G_k``, the number of k-source groups sharing at least one target."""
    source_tuple = tuple(sources)
    supports = relation_source_supports(source_tuple, relation)
    if max_order is None:
        max_order = len(source_tuple)
    if isinstance(max_order, bool) or not isinstance(max_order, int) or max_order < 0:
        raise ValueError("max_order must be a non-negative integer")
    max_order = min(max_order, len(source_tuple))

    result: list[tuple[int, int]] = []
    for order in range(1, max_order + 1):
        count = 0
        for group in combinations(source_tuple, order):
            shared = set(supports[group[0]])
            for source in group[1:]:
                shared.intersection_update(supports[source])
                if not shared:
                    break
            if shared:
                count += 1
        result.append((order, count))
    return tuple(result)


def postcompose_targets(relation: Relation, target_map: Mapping[Target, Hashable]) -> Relation:
    """Apply one deterministic target map and deduplicate merged memberships."""
    missing = {target for _source, target in relation if target not in target_map}
    if missing:
        raise ValueError("target_map must be defined on every used target")
    return frozenset((source, target_map[target]) for source, target in relation)


def function_graph_relation(mapping: Mapping[Source, Target]) -> Relation:
    """Embed one finite total mapping as its single-valued graph relation."""
    return frozenset(mapping.items())


def function_collision_spectrum(
    mapping: Mapping[Source, Target], max_order: int | None = None
) -> tuple[tuple[int, int], ...]:
    """Direct fiber formula used to verify the relational specialization."""
    fiber_sizes = Counter(mapping.values())
    observed_max = max(fiber_sizes.values(), default=0)
    if max_order is None:
        max_order = observed_max
    if isinstance(max_order, bool) or not isinstance(max_order, int) or max_order < 0:
        raise ValueError("max_order must be a non-negative integer")
    return tuple(
        (
            order,
            sum(comb(count, order) for count in fiber_sizes.values() if count >= order),
        )
        for order in range(1, max_order + 1)
    )
