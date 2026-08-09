"""Finite nonnegative LEGO contraction fibers.

A coarse block of capacity m remembers only the total c of indistinguishable
unit-1 objects placed among m fine slots.  The number of fine lifts is the exact
integer stars-and-bars count C(c+m-1,m-1).  The same (m,c) pair already used by
tagged contraction therefore determines both fiber multiplicity and, in the
collision-power family, the minimum collision cost.
"""

from __future__ import annotations

from math import comb


def hidden_allocation_multiplicity(capacity: int, total: int) -> int:
    """Number of nonnegative fine-slot allocations with one coarse total."""
    if isinstance(capacity, bool) or not isinstance(capacity, int) or capacity <= 0:
        raise ValueError("capacity must be a positive integer")
    if isinstance(total, bool) or not isinstance(total, int) or total < 0:
        raise ValueError("total must be a non-negative integer")
    return comb(total + capacity - 1, capacity - 1)


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


def finite_difference(values: tuple[int, ...]) -> tuple[int, ...]:
    if not isinstance(values, tuple) or len(values) < 2:
        raise ValueError("values must contain at least two integers")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in values):
        raise ValueError("values must be integers")
    return tuple(values[index + 1] - values[index] for index in range(len(values) - 1))


def allocation_growth_difference_order(capacity: int) -> int:
    """Exact finite-difference degree of c -> C(c+m-1,m-1).

    Returns m-1 by verifying the (m-1)-st difference is nonzero constant and the
    next difference vanishes on a sufficiently long exact integer sample.
    """
    if isinstance(capacity, bool) or not isinstance(capacity, int) or capacity <= 0:
        raise ValueError("capacity must be a positive integer")
    degree = capacity - 1
    values = tuple(
        hidden_allocation_multiplicity(capacity, total)
        for total in range(2 * capacity + 2)
    )
    current = values
    for order in range(degree):
        current = finite_difference(current)
    if len(set(current)) != 1 or current[0] == 0:
        raise AssertionError("expected nonzero constant at the hidden relation degree")
    current = finite_difference(current)
    if any(current):
        raise AssertionError("expected next finite difference to vanish")
    return degree
