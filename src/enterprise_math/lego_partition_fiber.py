"""Finite nonnegative LEGO contraction fibers.

A coarse block of capacity m remembers only the total c of indistinguishable
unit-1 objects placed among m fine slots.  The number of fine lifts is the exact
integer count C(c+m-1,m-1).  The same (m,c) pair already used by tagged
contraction therefore determines the whole fiber multiplicity, the balanced
minimum collision cost, and the number of balanced minimizers.

The primary composition law is at the fiber level: an (m+n)-slot lift with total
c is uniquely a choice of left total a, an m-slot lift of a, and an n-slot lift
of c-a.  Cardinality therefore produces ordinary convolution as a shadow.  The
same decomposition produces min-plus convolution when the observation is an
additive minimum cost.
"""

from __future__ import annotations

from math import comb


def _require_capacity_total(capacity: int, total: int) -> None:
    if isinstance(capacity, bool) or not isinstance(capacity, int) or capacity <= 0:
        raise ValueError("capacity must be a positive integer")
    if isinstance(total, bool) or not isinstance(total, int) or total < 0:
        raise ValueError("total must be a non-negative integer")


def hidden_allocation_multiplicity(capacity: int, total: int) -> int:
    """Number of nonnegative fine-slot allocations with one coarse total."""
    _require_capacity_total(capacity, total)
    return comb(total + capacity - 1, capacity - 1)


def balanced_minimizer_multiplicity(capacity: int, total: int) -> int:
    """Number of most-even allocations of `total` units among `capacity` slots.

    If total=capacity*q+r, every square/power-balanced minimizer has r slots at
    q+1 and the remaining slots at q.  The only choice is which r slots receive
    the extra unit, hence C(capacity,r).
    """
    _require_capacity_total(capacity, total)
    _, residue = divmod(total, capacity)
    return comb(capacity, residue)


def partition_fiber_multiplicity(
    capacities: tuple[int, ...],
    coarse_totals: tuple[int, ...],
) -> int:
    """Product of independent within-block lift counts for a coarse partition state."""
    if not isinstance(capacities, tuple) or not isinstance(coarse_totals, tuple):
        raise ValueError("capacities and coarse_totals must be tuples")
    if not capacities or len(capacities) != len(coarse_totals):
        raise ValueError("capacities and coarse_totals must have the same nonzero length")
    result = 1
    for capacity, total in zip(capacities, coarse_totals):
        result *= hidden_allocation_multiplicity(capacity, total)
    return result


def composed_fiber_count(left_capacity: int, right_capacity: int, total: int) -> int:
    """Count an (m+n)-slot fiber by splitting the total between two LEGO blocks."""
    _require_capacity_total(left_capacity, total)
    if isinstance(right_capacity, bool) or not isinstance(right_capacity, int) or right_capacity <= 0:
        raise ValueError("right_capacity must be a positive integer")
    return sum(
        hidden_allocation_multiplicity(left_capacity, left_total)
        * hidden_allocation_multiplicity(right_capacity, total - left_total)
        for left_total in range(total + 1)
    )


def fiber_composition_identity(left_capacity: int, right_capacity: int, total: int) -> bool:
    """Exact cardinality shadow of the LEGO fiber disjoint-union/product law."""
    _require_capacity_total(left_capacity, total)
    if isinstance(right_capacity, bool) or not isinstance(right_capacity, int) or right_capacity <= 0:
        raise ValueError("right_capacity must be a positive integer")
    return composed_fiber_count(left_capacity, right_capacity, total) == hidden_allocation_multiplicity(
        left_capacity + right_capacity,
        total,
    )


def one_step_dimension_lowering_identity(capacity: int, total: int) -> bool:
    """H_m(c+1)-H_m(c)=H_(m-1)(c+1) for m>=2."""
    _require_capacity_total(capacity, total)
    if capacity < 2:
        raise ValueError("capacity must be at least two")
    left = hidden_allocation_multiplicity(capacity, total + 1) - hidden_allocation_multiplicity(
        capacity,
        total,
    )
    right = hidden_allocation_multiplicity(capacity - 1, total + 1)
    return left == right


def finite_difference(values: tuple[int, ...]) -> tuple[int, ...]:
    if not isinstance(values, tuple) or len(values) < 2:
        raise ValueError("values must contain at least two integers")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in values):
        raise ValueError("values must be integers")
    return tuple(values[index + 1] - values[index] for index in range(len(values) - 1))


def allocation_growth_difference_order(capacity: int) -> int:
    """Exact difference depth of the hidden-allocation multiplicity.

    The result is capacity-1.  This is the number of hidden relation freedoms in
    an m-slot block after only the total has been retained.
    """
    if isinstance(capacity, bool) or not isinstance(capacity, int) or capacity <= 0:
        raise ValueError("capacity must be a positive integer")
    degree = capacity - 1
    values = tuple(
        hidden_allocation_multiplicity(capacity, total)
        for total in range(2 * capacity + 2)
    )
    current = values
    for _ in range(degree):
        current = finite_difference(current)
    if len(set(current)) != 1 or current[0] != 1:
        raise AssertionError("expected constant one at the hidden relation degree")
    current = finite_difference(current)
    if any(current):
        raise AssertionError("expected next finite difference to vanish")
    return degree
