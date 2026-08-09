"""E001.3 relational extension of the finite collision spectrum.

For one finite relation ``R subset X x Z``, let

    c_z = |{x in X : (x,z) in R}|,
    W_k(R) = sum_z binom(c_z, k).

This counts k-source common-target witnesses, with multiplicity when one source
group shares several targets.

If ``R`` is the graph of a total single-valued function ``F : X -> Z``, its
target columns are exactly the ordinary fibers of ``F``.  Therefore

    W_k(graph(F)) = sum_z binom(|F^{-1}(z)|, k),

which is precisely the P011 finite collision-spectrum construction.  The
relational version replaces a fiber partition by a possibly overlapping target
cover.  Generic relation/hypergraph incidence mathematics is established prior
art; this module records the exact bridge needed by the Enterprise Math
engineering pressure test.
"""

from __future__ import annotations

from collections import Counter
from collections.abc import Hashable, Mapping
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


def relation_overlap_spectrum(
    relation: Relation, max_order: int | None = None
) -> tuple[tuple[int, int], ...]:
    """Return W_k=sum_z binom(c_z,k) for orders 1..max_order.

    Order 1 is included here so the functional specialization exposes the fixed
    domain-size coefficient used by P011.  Higher orders count shared-target
    witnesses.
    """
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
