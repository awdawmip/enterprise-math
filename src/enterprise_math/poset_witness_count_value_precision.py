"""Value-precision hierarchy for witness counts on finite poset ideal states.

For a positive total witness multiplicity N and a required query S, exact count
c(S) refines the three-valued support status:

    c=0       -> IMPOSSIBLE
    0<c<N     -> MAY
    c=N       -> MUST

Thus joint MAY/MUST semantics is a quotient of exact integer count semantics.
Even with the exact positive-support family and total N fixed, multiplicity
assignments can have different count tables.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from .poset_observation_boundary import Element, Ideal, Relation, enumerate_order_ideals
from .poset_witness_count_zeta import count_required_labels


@dataclass(frozen=True)
class WitnessCountValueState:
    total_multiplicity: int
    exact_count: int
    support_status: str


def total_multiplicity(
    elements: tuple[Element, ...],
    leq: Relation,
    multiplicities: Mapping[Ideal, int],
) -> int:
    ideals = enumerate_order_ideals(elements, leq)
    ideal_set = set(ideals)
    if any(ideal not in ideal_set for ideal in multiplicities):
        raise ValueError("multiplicity map contains a non-ideal state")
    total = 0
    for ideal in ideals:
        value = multiplicities.get(ideal, 0)
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("multiplicities must be non-negative integers")
        total += value
    return total


def count_support_status(count: int, total: int) -> str:
    if isinstance(count, bool) or not isinstance(count, int) or count < 0:
        raise ValueError("count must be a non-negative integer")
    if isinstance(total, bool) or not isinstance(total, int) or total <= 0:
        raise ValueError("total must be a positive integer")
    if count > total:
        raise ValueError("count cannot exceed total witness multiplicity")
    if count == 0:
        return "IMPOSSIBLE"
    if count == total:
        return "MUST"
    return "MAY"


def witness_count_value_state(
    elements: tuple[Element, ...],
    leq: Relation,
    multiplicities: Mapping[Ideal, int],
    required: frozenset[Element],
) -> WitnessCountValueState:
    total = total_multiplicity(elements, leq, multiplicities)
    if total <= 0:
        raise ValueError("at least one positive witness multiplicity is required")
    count = count_required_labels(elements, leq, multiplicities, required)
    return WitnessCountValueState(
        total_multiplicity=total,
        exact_count=count,
        support_status=count_support_status(count, total),
    )


def positive_support_family(
    elements: tuple[Element, ...],
    leq: Relation,
    multiplicities: Mapping[Ideal, int],
) -> frozenset[Ideal]:
    ideals = enumerate_order_ideals(elements, leq)
    return frozenset(ideal for ideal in ideals if multiplicities.get(ideal, 0) > 0)
