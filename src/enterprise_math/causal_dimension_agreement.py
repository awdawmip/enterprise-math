"""Agreement and separation between several exact integer dimension witnesses.

Enterprise Math now has several independently generated integer growth orders:

* hidden-allocation multiplicity H_m(c) has difference degree m-1;
* A_p graph-ball cardinality has difference degree p;
* independent task capacities multiply, so polynomial causal growth degrees add;
* a relation module may have free rank p.

These numbers must not be identified by definition.  This module provides finite
exact certificates and explicit disagreement witnesses.  A dimension agreement
claim is a bridge theorem about a specified causal regime, not a universal
meaning of the word dimension.
"""

from __future__ import annotations

from dataclasses import dataclass

from .causal_capacity_dimension import (
    exact_polynomial_sequence,
    sampled_polynomial_difference_degree,
)
from .lattice_geometry import a_ball_count
from .lego_partition_fiber import hidden_allocation_multiplicity


@dataclass(frozen=True)
class DimensionAgreement:
    declared_relation_rank: int
    fiber_growth_degree: int | None
    ball_growth_degree: int | None

    @property
    def agrees(self) -> bool:
        return (
            self.fiber_growth_degree == self.declared_relation_rank
            and self.ball_growth_degree == self.declared_relation_rank
        )


def free_slot_fiber_growth_degree(slot_count: int) -> int:
    """Exact finite-difference degree of c -> H_m(c), certified on a long sample."""
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count <= 0:
        raise ValueError("slot_count must be a positive integer")
    expected = slot_count - 1
    values = tuple(
        hidden_allocation_multiplicity(slot_count, total)
        for total in range(2 * slot_count + 3)
    )
    degree = sampled_polynomial_difference_degree(values)
    if degree != expected or not exact_polynomial_sequence(values, expected):
        raise AssertionError("free-slot allocation growth did not show expected exact degree")
    return expected


def a_ball_growth_degree(p: int) -> int:
    """Exact finite-difference degree of the represented A_p graph-ball count.

    The executable check uses the existing closed integer formula.  The all-radii
    theorem follows from that formula: it is a positive sum of binomial
    polynomials of degree at most p with a nonzero degree-p term.
    """
    if isinstance(p, bool) or not isinstance(p, int) or p <= 0:
        raise ValueError("p must be a positive integer")
    values = tuple(a_ball_count(p, radius) for radius in range(2 * p + 5))
    degree = sampled_polynomial_difference_degree(values)
    if degree != p or not exact_polynomial_sequence(values, p):
        raise AssertionError("A_p ball growth did not show expected exact degree")
    return p


def free_a_p_dimension_agreement(p: int) -> DimensionAgreement:
    """Three-way agreement for the free A_p / p+1-slot working model."""
    if isinstance(p, bool) or not isinstance(p, int) or p <= 0:
        raise ValueError("p must be a positive integer")
    return DimensionAgreement(
        declared_relation_rank=p,
        fiber_growth_degree=free_slot_fiber_growth_degree(p + 1),
        ball_growth_degree=a_ball_growth_degree(p),
    )


def capacity_growth_degree(values: tuple[int, ...]) -> int | None:
    """Finite-sample polynomial degree of a task's exact state-capacity sequence."""
    return sampled_polynomial_difference_degree(values)


def task_growth_can_disagree_with_substrate_rank(
    relation_rank: int,
    task_capacity: tuple[int, ...],
) -> bool:
    if isinstance(relation_rank, bool) or not isinstance(relation_rank, int) or relation_rank < 0:
        raise ValueError("relation_rank must be a non-negative integer")
    return capacity_growth_degree(task_capacity) != relation_rank


def independent_capacity_product(
    left: tuple[int, ...],
    right: tuple[int, ...],
) -> tuple[int, ...]:
    """Independent signature products multiply same-depth class capacities."""
    if not left or len(left) != len(right):
        raise ValueError("capacity sequences must have the same nonzero length")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in left + right
    ):
        raise ValueError("capacities must be non-negative integers")
    return tuple(a * b for a, b in zip(left, right))


def independent_polynomial_growth_degree_adds(
    left: tuple[int, ...],
    left_degree: int,
    right: tuple[int, ...],
    right_degree: int,
) -> bool:
    """Finite exact check of degree additivity for independent polynomial capacities.

    Promotion to an all-depth theorem requires the independent polynomial formulas;
    then ordinary integer-polynomial degree multiplication gives p+q provided the
    leading coefficients are nonzero.  This function only audits the supplied
    exact samples.
    """
    if not exact_polynomial_sequence(left, left_degree):
        return False
    if not exact_polynomial_sequence(right, right_degree):
        return False
    product = independent_capacity_product(left, right)
    return exact_polynomial_sequence(product, left_degree + right_degree)
