"""Finite nonnegative LEGO contraction fibers.

A coarse block of capacity m remembers only the total c of indistinguishable
unit-1 objects placed among m fine slots.  The number of fine lifts is the exact
integer count C(c+m-1,m-1).

The primary composition law is structural.  If m=sum_i m_i fine slots are first
grouped into k coarse blocks, every grand-total lift is uniquely a choice of
coarse block totals c_i with sum c together with one fine lift in each block:

    F_m(c) ~= disjoint_union_(c_1+...+c_k=c) product_i F_(m_i)(c_i).

Cardinality gives generalized convolution only as a shadow.  The outer coarse-
total allocation fiber F_k(c) carries exactly the k-1 cross-block redistribution
freedoms; the inner block fibers carry sum_i(m_i-1) internal freedoms.
"""

from __future__ import annotations

from math import comb


def _require_capacity_total(capacity: int, total: int) -> None:
    if isinstance(capacity, bool) or not isinstance(capacity, int) or capacity <= 0:
        raise ValueError("capacity must be a positive integer")
    if isinstance(total, bool) or not isinstance(total, int) or total < 0:
        raise ValueError("total must be a non-negative integer")


def _require_capacities(capacities: tuple[int, ...]) -> None:
    if not isinstance(capacities, tuple) or not capacities:
        raise ValueError("capacities must be a non-empty tuple")
    if any(
        isinstance(capacity, bool) or not isinstance(capacity, int) or capacity <= 0
        for capacity in capacities
    ):
        raise ValueError("capacities must be positive integers")


def hidden_allocation_multiplicity(capacity: int, total: int) -> int:
    """Number of nonnegative fine-slot allocations with one coarse total."""
    _require_capacity_total(capacity, total)
    return comb(total + capacity - 1, capacity - 1)


def balanced_minimizer_multiplicity(capacity: int, total: int) -> int:
    """Number of most-even allocations of `total` units among `capacity` slots."""
    _require_capacity_total(capacity, total)
    _, residue = divmod(total, capacity)
    return comb(capacity, residue)


def coarse_total_allocations(block_count: int, total: int) -> tuple[tuple[int, ...], ...]:
    """All nonnegative k-block total vectors summing to `total`."""
    if isinstance(block_count, bool) or not isinstance(block_count, int) or block_count <= 0:
        raise ValueError("block_count must be a positive integer")
    if isinstance(total, bool) or not isinstance(total, int) or total < 0:
        raise ValueError("total must be a non-negative integer")
    if block_count == 1:
        return ((total,),)
    result = []
    for first in range(total + 1):
        for rest in coarse_total_allocations(block_count - 1, total - first):
            result.append((first,) + rest)
    return tuple(result)


def partition_fiber_multiplicity(
    capacities: tuple[int, ...],
    coarse_totals: tuple[int, ...],
) -> int:
    """Product of independent within-block lift counts for a coarse partition state."""
    _require_capacities(capacities)
    if not isinstance(coarse_totals, tuple) or len(coarse_totals) != len(capacities):
        raise ValueError("coarse_totals must be a tuple matching capacities")
    result = 1
    for capacity, total in zip(capacities, coarse_totals):
        result *= hidden_allocation_multiplicity(capacity, total)
    return result


def decomposed_partition_fiber_count(
    capacities: tuple[int, ...],
    total: int,
) -> int:
    """Count grand-total fine lifts by first choosing all coarse block totals."""
    _require_capacities(capacities)
    if isinstance(total, bool) or not isinstance(total, int) or total < 0:
        raise ValueError("total must be a non-negative integer")
    return sum(
        partition_fiber_multiplicity(capacities, coarse_totals)
        for coarse_totals in coarse_total_allocations(len(capacities), total)
    )


def partition_decomposition_identity(
    capacities: tuple[int, ...],
    total: int,
) -> bool:
    """Generalized LEGO fiber composition cardinality identity."""
    _require_capacities(capacities)
    return decomposed_partition_fiber_count(capacities, total) == hidden_allocation_multiplicity(
        sum(capacities), total
    )


def composed_fiber_count(left_capacity: int, right_capacity: int, total: int) -> int:
    """Binary compatibility wrapper for the generalized partition decomposition."""
    _require_capacity_total(left_capacity, total)
    if isinstance(right_capacity, bool) or not isinstance(right_capacity, int) or right_capacity <= 0:
        raise ValueError("right_capacity must be a positive integer")
    return decomposed_partition_fiber_count((left_capacity, right_capacity), total)


def coupled_fiber_count_by_total_kernel(
    left_capacity: int,
    right_capacity: int,
    total: int,
    coupling_by_split: dict[tuple[int, int], int],
) -> int:
    """Weighted counting shadow when coupling depends only on block totals."""
    _require_capacity_total(left_capacity, total)
    if isinstance(right_capacity, bool) or not isinstance(right_capacity, int) or right_capacity <= 0:
        raise ValueError("right_capacity must be a positive integer")
    if not isinstance(coupling_by_split, dict):
        raise ValueError("coupling_by_split must be a dict")
    required = {(left_total, total - left_total) for left_total in range(total + 1)}
    if set(coupling_by_split) != required:
        raise ValueError("coupling_by_split must define every total split exactly once")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in coupling_by_split.values()
    ):
        raise ValueError("coupling multiplicities must be non-negative integers")
    return sum(
        coupling_by_split[(left_total, total - left_total)]
        * hidden_allocation_multiplicity(left_capacity, left_total)
        * hidden_allocation_multiplicity(right_capacity, total - left_total)
        for left_total in range(total + 1)
    )


def fiber_composition_identity(left_capacity: int, right_capacity: int, total: int) -> bool:
    """Binary cardinality shadow of the LEGO fiber disjoint-union/product law."""
    return partition_decomposition_identity((left_capacity, right_capacity), total)


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
    """Exact difference depth of the hidden-allocation multiplicity."""
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
