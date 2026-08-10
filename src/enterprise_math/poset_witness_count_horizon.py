"""Sharp poset-width horizon for bounded-arity witness-count recovery.

Counts of required labels first normalize to antichains.  If count queries are
available for every antichain of size at most k, then k>=width(P) exposes the
count of every ideal boundary and the full witness multiplicity function is
recovered by zeta inversion.

The width bound is sharp in the worst case.  On a w-element antichain, the
Boolean families of even-cardinality ideals and odd-cardinality ideals give the
same witness count for every proper required subset, while the full-set query
distinguishes them.  Hence every k<w can fail to recover exact family identity.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .poset_boundary_width import poset_width
from .poset_observation_boundary import Element, Ideal, Relation, enumerate_antichains
from .poset_witness_count_zeta import count_required_labels


@dataclass(frozen=True)
class WitnessCountHorizonReport:
    poset_width: int
    arity_cap: int
    saturated: bool
    exact_recovery_guaranteed: bool
    essential_query_count: int


def count_signature_up_to_arity(
    elements: tuple[Element, ...],
    leq: Relation,
    multiplicities: dict[Ideal, int],
    arity_cap: int,
) -> dict[frozenset[Element], int]:
    if isinstance(arity_cap, bool) or not isinstance(arity_cap, int) or arity_cap < 0:
        raise ValueError("arity_cap must be a non-negative integer")
    antichains = enumerate_antichains(elements, leq)
    return {
        antichain: count_required_labels(elements, leq, multiplicities, antichain)
        for antichain in antichains
        if len(antichain) <= arity_cap
    }


def analyze_count_horizon(
    elements: tuple[Element, ...], leq: Relation, arity_cap: int
) -> WitnessCountHorizonReport:
    if isinstance(arity_cap, bool) or not isinstance(arity_cap, int) or arity_cap < 0:
        raise ValueError("arity_cap must be a non-negative integer")
    width = poset_width(elements, leq)
    query_count = sum(
        1 for antichain in enumerate_antichains(elements, leq) if len(antichain) <= arity_cap
    )
    saturated = arity_cap >= width
    return WitnessCountHorizonReport(
        poset_width=width,
        arity_cap=arity_cap,
        saturated=saturated,
        exact_recovery_guaranteed=saturated,
        essential_query_count=query_count,
    )


def parity_families_on_antichain(
    width: int,
) -> tuple[
    tuple[int, ...],
    Relation,
    dict[Ideal, int],
    dict[Ideal, int],
]:
    if isinstance(width, bool) or not isinstance(width, int) or width < 1:
        raise ValueError("width must be a positive integer")
    elements = tuple(range(width))
    leq = frozenset((x, x) for x in elements)
    even: dict[Ideal, int] = {}
    odd: dict[Ideal, int] = {}
    for size in range(width + 1):
        for subset in combinations(elements, size):
            ideal = frozenset(subset)
            if size % 2 == 0:
                even[ideal] = 1
            else:
                odd[ideal] = 1
    return elements, leq, even, odd


def parity_collision_signature(
    width: int, arity_cap: int
) -> tuple[
    dict[frozenset[int], int],
    dict[frozenset[int], int],
]:
    elements, leq, even, odd = parity_families_on_antichain(width)
    return (
        count_signature_up_to_arity(elements, leq, even, arity_cap),
        count_signature_up_to_arity(elements, leq, odd, arity_cap),
    )
