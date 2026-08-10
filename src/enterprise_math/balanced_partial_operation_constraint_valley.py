"""Balanced partitions also minimize deterministic partial safe-operation freedom.

For partition shape ``lambda=(n_1,...,n_b)``, the deterministic partial safe
endomap count has source-block factors

    P_k(lambda) = 1 + S_k(lambda)
                = 1^k + sum_j n_j^k,

where the extra ``1`` is the single all-UNDEFINED behavior available to one
source block.  Hence ``P_k`` is itself an ordinary power-sum sequence of the
augmented positive multiset ``(1,n_1,...,n_b)`` and is log-convex.

A Robin-Hood balancing step ``a,b -> a-1,b+1`` with ``a>=b+2`` leaves ``P_1``
fixed and strictly lowers every ``P_k`` for ``k>=2``.  The same log-convex ratio
argument used by the total-operation owner then proves strict decrease of the
full partial-safe count.

Therefore for fixed state count and fixed observation block count, the unique
partition minimizing deterministic partial safe-operation freedom is the same
balanced shape whose block sizes differ by at most one.  Only the one-dimensional
choice of block count remains for the global partial-operation constraint valley.

The extra undefined choice changes the selected global block count in general;
this module does not identify total and partial valleys.  It only proves that
both have the same fixed-block-count balancing normal form.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from functools import reduce
from operator import mul
from typing import Iterable

from .balanced_operation_constraint_valley import (
    _shape,
    balance_shape_pair,
    balanced_partition_shape,
    shape_power_sum,
)


def augmented_partial_power_sum(shape: Iterable[int], exponent: int) -> int:
    """Return ``1 + sum_j n_j^exponent`` for the augmented undefined target."""
    values = _shape(shape)
    if isinstance(exponent, bool) or not isinstance(exponent, int):
        raise TypeError("exponent must be an integer")
    if exponent < 0:
        raise ValueError("exponent must be non-negative")
    return 1 + shape_power_sum(values, exponent)


def safe_partial_count_from_shape(shape: Iterable[int]) -> int:
    values = _shape(shape)
    return reduce(
        mul,
        (
            augmented_partial_power_sum(values, source_size)
            for source_size in values
        ),
        1,
    )


def augmented_power_sum_log_convex(shape: Iterable[int], exponent: int) -> bool:
    """Log-convexity of ``1+S_k`` as a genuine augmented power-sum sequence."""
    values = _shape(shape)
    if isinstance(exponent, bool) or not isinstance(exponent, int):
        raise TypeError("exponent must be an integer")
    if exponent <= 0:
        raise ValueError("exponent must be positive")
    center = augmented_partial_power_sum(values, exponent)
    return center * center <= (
        augmented_partial_power_sum(values, exponent - 1)
        * augmented_partial_power_sum(values, exponent + 1)
    )


def partial_balancing_strictly_reduces_safe_count(
    shape: Iterable[int],
    large_index: int,
    small_index: int,
) -> bool:
    values = _shape(shape)
    balanced = balance_shape_pair(values, large_index, small_index)
    return safe_partial_count_from_shape(balanced) < safe_partial_count_from_shape(values)


def balanced_safe_partial_count(state_count: int, block_count: int) -> int:
    """Exact partial-safe count of the unique balanced fixed-block-count shape."""
    shape = balanced_partition_shape(state_count, block_count)
    quotient, remainder = divmod(state_count, block_count)
    low_factor = (
        1
        + remainder * (quotient + 1) ** quotient
        + (block_count - remainder) * quotient**quotient
    )
    if remainder == 0:
        result = low_factor**block_count
    else:
        high_factor = (
            1
            + remainder * (quotient + 1) ** (quotient + 1)
            + (block_count - remainder) * quotient ** (quotient + 1)
        )
        result = high_factor**remainder * low_factor ** (block_count - remainder)
    direct = safe_partial_count_from_shape(shape)
    if result != direct:
        raise AssertionError("balanced partial closed count disagrees with direct product")
    return result


@dataclass(frozen=True)
class PartialOperationConstraintValley:
    state_count: int
    block_count: int
    block_shape: tuple[int, ...]
    safe_partial_count: int
    safe_probability: Fraction


def most_constraining_partial_partition(state_count: int) -> PartialOperationConstraintValley:
    """Exact global minimum over genuine intermediate partition shapes."""
    if isinstance(state_count, bool) or not isinstance(state_count, int):
        raise TypeError("state_count must be an integer")
    if state_count < 3:
        raise ValueError("state_count must be at least three")
    candidates = [
        (balanced_safe_partial_count(state_count, block_count), block_count)
        for block_count in range(2, state_count)
    ]
    safe_count, block_count = min(candidates)
    return PartialOperationConstraintValley(
        state_count=state_count,
        block_count=block_count,
        block_shape=balanced_partition_shape(state_count, block_count),
        safe_partial_count=safe_count,
        safe_probability=Fraction(safe_count, (state_count + 1) ** state_count),
    )
