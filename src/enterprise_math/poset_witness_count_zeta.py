"""Witness-count zeta transform on finite order-ideal lattices.

For a finite observation poset P, exact witness states are order ideals.  A
nonnegative multiplicity function w(I) on J(P) induces count queries

    c(K) = sum_{I superset K} w(I).

This is the upper zeta transform on the ideal lattice and is exactly inverted by
descending inclusion.  Raw required sets first normalize to their maximal
antichain/down-closure, so counts on all antichain queries recover the entire
witness multiplicity function.

Incidence-algebra / Möbius inversion is classical.  This module is an exact
P025/A4 pressure-test specialization, not a generic novelty claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from .poset_joint_query_normal import maximal_required_antichain
from .poset_observation_boundary import (
    Element,
    Ideal,
    Relation,
    down_closure,
    enumerate_order_ideals,
    maximal_boundary,
)


@dataclass(frozen=True)
class WitnessCountTransform:
    ideals: tuple[Ideal, ...]
    multiplicities: tuple[int, ...]
    upper_counts: tuple[int, ...]
    total_witness_multiplicity: int


def _ordered_ideals(elements: tuple[Element, ...], leq: Relation) -> tuple[Ideal, ...]:
    # enumerate_order_ideals already orders by cardinality increasing.
    return enumerate_order_ideals(elements, leq)


def _validate_multiplicities(
    ideals: tuple[Ideal, ...], multiplicities: Mapping[Ideal, int]
) -> dict[Ideal, int]:
    ideal_set = set(ideals)
    if any(ideal not in ideal_set for ideal in multiplicities):
        raise ValueError("multiplicity map contains a non-ideal state")
    result: dict[Ideal, int] = {}
    for ideal in ideals:
        value = multiplicities.get(ideal, 0)
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("witness multiplicities must be non-negative integers")
        result[ideal] = value
    return result


def witness_count_transform(
    elements: tuple[Element, ...],
    leq: Relation,
    multiplicities: Mapping[Ideal, int],
) -> WitnessCountTransform:
    ideals = _ordered_ideals(elements, leq)
    weights = _validate_multiplicities(ideals, multiplicities)
    counts = tuple(
        sum(weights[upper] for upper in ideals if required.issubset(upper))
        for required in ideals
    )
    return WitnessCountTransform(
        ideals=ideals,
        multiplicities=tuple(weights[ideal] for ideal in ideals),
        upper_counts=counts,
        total_witness_multiplicity=sum(weights.values()),
    )


def invert_upper_counts(
    elements: tuple[Element, ...],
    leq: Relation,
    counts: Mapping[Ideal, int],
) -> dict[Ideal, int]:
    """Invert c(K)=sum_{I>=K} w(I) by descending inclusion."""
    ideals = _ordered_ideals(elements, leq)
    if set(counts) != set(ideals):
        raise ValueError("counts must be supplied for every ideal exactly once")
    for value in counts.values():
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("counts must be non-negative integers")

    recovered: dict[Ideal, int] = {}
    for required in sorted(ideals, key=len, reverse=True):
        strict_upper_total = sum(
            recovered[upper]
            for upper in recovered
            if required < upper
        )
        value = counts[required] - strict_upper_total
        if value < 0:
            raise ValueError("count table is not the zeta transform of non-negative multiplicities")
        recovered[required] = value
    return recovered


def count_required_labels(
    elements: tuple[Element, ...],
    leq: Relation,
    multiplicities: Mapping[Ideal, int],
    required: frozenset[Element],
) -> int:
    """Count witnesses for a raw query after antichain/down-closure normalization."""
    antichain = maximal_required_antichain(elements, leq, required)
    normalized = down_closure(elements, leq, antichain)
    # Validate normalized is indeed an ideal and then evaluate the zeta count.
    maximal_boundary(elements, leq, normalized)
    ideals = _ordered_ideals(elements, leq)
    weights = _validate_multiplicities(ideals, multiplicities)
    return sum(weight for ideal, weight in weights.items() if normalized.issubset(ideal))


def counts_by_ideal(
    transform: WitnessCountTransform,
) -> dict[Ideal, int]:
    return dict(zip(transform.ideals, transform.upper_counts, strict=True))
