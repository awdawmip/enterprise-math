"""Balanced partitions minimize safe total-operation freedom at fixed block count.

For a partition shape ``lambda=(n_1,...,n_b)`` define the power sums

    S_k(lambda) = sum_j n_j^k.

The safe-total endomap count is

    N(lambda) = product_i S_(n_i)(lambda).

Suppose two block sizes satisfy ``a>=b+2``.  Replace them by ``a-1,b+1``.
Two standard facts imply that this Robin-Hood balancing strictly lowers ``N``:

1. Discrete convexity: for every ``k>=2``,

       (a-1)^k + (b+1)^k < a^k + b^k,

   so every target power sum ``S_k`` with ``k>=2`` strictly decreases while
   ``S_1`` is unchanged.

2. The positive power-sum sequence is log-convex, equivalently
   ``S_(k+1)/S_k`` is nondecreasing in ``k``.  Since ``a-1>=b``,

       S_(a-1) S_(b+1) <= S_a S_b.

Combining target balancing with the source-exponent change yields

    N(...,a-1,b+1,...) < N(...,a,b,...).

Repeated balancing preserves the number of blocks and terminates uniquely at
the shape whose block sizes differ by at most one.  Therefore, for fixed state
count ``n`` and block count ``b``, the unique most operation-constraining shape
is

    n = q*b + r,  0<=r<b,

with ``r`` blocks of size ``q+1`` and ``b-r`` blocks of size ``q``.

For that balanced shape let

    A_k = r*(q+1)^k + (b-r)*q^k.

Its exact safe-total count is

    A_(q+1)^r * A_q^(b-r),

with the obvious omission of an exponent-zero factor when ``r=0``.

Hence the global most-constraining nontrivial partition on ``n`` states is found
by a one-dimensional exact search over ``b=2,...,n-1``.  No enumeration of all
integer partitions is required.

Convex balancing, power-sum log-convexity and majorization are standard prior
mathematics.  The Enterprise Math result is their exact safe-operation / finite
precision specialization and the resulting constraint-valley compiler.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import reduce
from operator import mul
from typing import Iterable


def _shape(shape: Iterable[int]) -> tuple[int, ...]:
    values = tuple(shape)
    if not values:
        raise ValueError("partition shape must be nonempty")
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("partition block sizes must be integers")
        if value <= 0:
            raise ValueError("partition block sizes must be positive")
    return tuple(sorted(values, reverse=True))


def shape_state_count(shape: Iterable[int]) -> int:
    return sum(_shape(shape))


def shape_power_sum(shape: Iterable[int], exponent: int) -> int:
    values = _shape(shape)
    if isinstance(exponent, bool) or not isinstance(exponent, int):
        raise TypeError("exponent must be an integer")
    if exponent < 0:
        raise ValueError("exponent must be non-negative")
    return sum(value**exponent for value in values)


def safe_total_count_from_shape(shape: Iterable[int]) -> int:
    values = _shape(shape)
    return reduce(
        mul,
        (shape_power_sum(values, source_size) for source_size in values),
        1,
    )


def power_sum_log_convex(shape: Iterable[int], exponent: int) -> bool:
    """Executable Cauchy/log-convex inequality ``S_k^2<=S_(k-1)S_(k+1)``."""
    values = _shape(shape)
    if isinstance(exponent, bool) or not isinstance(exponent, int):
        raise TypeError("exponent must be an integer")
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    center = shape_power_sum(values, exponent)
    return center * center <= (
        shape_power_sum(values, exponent - 1)
        * shape_power_sum(values, exponent + 1)
    )


def balance_shape_pair(
    shape: Iterable[int],
    large_index: int,
    small_index: int,
) -> tuple[int, ...]:
    """Move one state from a block at least two larger than another block."""
    values = list(_shape(shape))
    for name, index in (("large_index", large_index), ("small_index", small_index)):
        if isinstance(index, bool) or not isinstance(index, int):
            raise TypeError(f"{name} must be an integer")
        if not 0 <= index < len(values):
            raise ValueError(f"{name} is outside the partition shape")
    if large_index == small_index:
        raise ValueError("balancing indices must be distinct")
    large = values[large_index]
    small = values[small_index]
    if large < small + 2:
        raise ValueError("selected block sizes must differ by at least two")
    values[large_index] -= 1
    values[small_index] += 1
    return tuple(sorted(values, reverse=True))


def balancing_strictly_reduces_safe_total_count(
    shape: Iterable[int],
    large_index: int,
    small_index: int,
) -> bool:
    values = _shape(shape)
    balanced = balance_shape_pair(values, large_index, small_index)
    if sum(values) != sum(balanced) or len(values) != len(balanced):
        raise AssertionError("balancing changed state count or block count")
    return safe_total_count_from_shape(balanced) < safe_total_count_from_shape(values)


def balanced_partition_shape(state_count: int, block_count: int) -> tuple[int, ...]:
    for name, value in (("state_count", state_count), ("block_count", block_count)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be positive")
    if block_count > state_count:
        raise ValueError("block_count cannot exceed state_count")
    quotient, remainder = divmod(state_count, block_count)
    return (quotient + 1,) * remainder + (quotient,) * (block_count - remainder)


def balanced_safe_total_count(state_count: int, block_count: int) -> int:
    """Closed safe-total count for the unique balanced shape at fixed block count."""
    shape = balanced_partition_shape(state_count, block_count)
    quotient, remainder = divmod(state_count, block_count)
    low_power_sum = (
        remainder * (quotient + 1) ** quotient
        + (block_count - remainder) * quotient**quotient
    )
    if remainder == 0:
        result = low_power_sum**block_count
    else:
        high_power_sum = (
            remainder * (quotient + 1) ** (quotient + 1)
            + (block_count - remainder) * quotient ** (quotient + 1)
        )
        result = high_power_sum**remainder * low_power_sum ** (block_count - remainder)
    direct = safe_total_count_from_shape(shape)
    if result != direct:
        raise AssertionError("balanced closed count disagrees with direct power-sum product")
    return result


@dataclass(frozen=True)
class OperationConstraintValley:
    state_count: int
    block_count: int
    block_shape: tuple[int, ...]
    safe_total_count: int
    safe_probability: Fraction


def most_constraining_partition(state_count: int) -> OperationConstraintValley:
    """Exact global minimum over every genuine intermediate partition shape.

    The balancing theorem reduces the search to one balanced candidate per block
    count.  ``state_count>=3`` is required for a genuine intermediate partition.
    """
    if isinstance(state_count, bool) or not isinstance(state_count, int):
        raise TypeError("state_count must be an integer")
    if state_count < 3:
        raise ValueError("state_count must be at least three")
    candidates = [
        (balanced_safe_total_count(state_count, block_count), block_count)
        for block_count in range(2, state_count)
    ]
    safe_count, block_count = min(candidates)
    return OperationConstraintValley(
        state_count=state_count,
        block_count=block_count,
        block_shape=balanced_partition_shape(state_count, block_count),
        safe_total_count=safe_count,
        safe_probability=Fraction(safe_count, state_count**state_count),
    )
