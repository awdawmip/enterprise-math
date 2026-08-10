"""Exact safe-operation freedom range at fixed observation class count.

The balancing theorem proves that one Robin-Hood transfer

    (a,b) -> (a-1,b+1),   a>=b+2,

strictly lowers both deterministic total and deterministic partial safe-endomap
counts.  Repeating such transfers moves every positive integer partition of
``n`` with exactly ``b`` blocks toward the unique balanced partition.  Reversing
the order moves toward the unique most imbalanced shape

    (n-b+1, 1, ..., 1).

Hence safe-operation count is strictly ordered by this majorization direction at
fixed block count:

* balanced shape = unique minimum operation freedom;
* one-giant-plus-singletons shape = unique maximum operation freedom.

Let ``L=n-b+1``.  For the most imbalanced shape the power sums are

    S_k = L^k + (b-1).

There is one source block of size ``L`` and ``b-1`` singleton source blocks.
Therefore the exact maximum counts are

    N_total_max   = (L^L + b - 1) * n^(b-1),
    N_partial_max = (L^L + b)     * (n+1)^(b-1).

The minima are the balanced closed forms from the parent owners.

Thus observation class count alone does not determine safe-operation freedom.
Two partitions with the same ``n`` and ``b`` can lie anywhere inside a strict
shape-dependent interval.  Precision needs at least enough information to know
its fiber shape before one can infer operation-language capacity.

Majorization and Schur-convexity are standard prior mathematics.  This module
owns only the exact safe-operation specialization and finite extremal formulas.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Iterable

from .balanced_operation_constraint_valley import (
    balanced_partition_shape,
    balanced_safe_total_count,
    safe_total_count_from_shape,
)
from .balanced_partial_operation_constraint_valley import (
    balanced_safe_partial_count,
    safe_partial_count_from_shape,
)


def _state_and_blocks(state_count: int, block_count: int) -> None:
    for name, value in (("state_count", state_count), ("block_count", block_count)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be positive")
    if block_count > state_count:
        raise ValueError("block_count cannot exceed state_count")


def maximally_imbalanced_partition_shape(
    state_count: int,
    block_count: int,
) -> tuple[int, ...]:
    _state_and_blocks(state_count, block_count)
    return (state_count - block_count + 1,) + (1,) * (block_count - 1)


def maximum_safe_total_count_fixed_blocks(
    state_count: int,
    block_count: int,
) -> int:
    _state_and_blocks(state_count, block_count)
    large = state_count - block_count + 1
    result = (large**large + block_count - 1) * state_count ** (block_count - 1)
    direct = safe_total_count_from_shape(
        maximally_imbalanced_partition_shape(state_count, block_count)
    )
    if result != direct:
        raise AssertionError("total maximum closed form disagrees with direct count")
    return result


def maximum_safe_partial_count_fixed_blocks(
    state_count: int,
    block_count: int,
) -> int:
    _state_and_blocks(state_count, block_count)
    large = state_count - block_count + 1
    result = (large**large + block_count) * (state_count + 1) ** (block_count - 1)
    direct = safe_partial_count_from_shape(
        maximally_imbalanced_partition_shape(state_count, block_count)
    )
    if result != direct:
        raise AssertionError("partial maximum closed form disagrees with direct count")
    return result


def minimum_safe_total_count_fixed_blocks(
    state_count: int,
    block_count: int,
) -> int:
    _state_and_blocks(state_count, block_count)
    return balanced_safe_total_count(state_count, block_count)


def minimum_safe_partial_count_fixed_blocks(
    state_count: int,
    block_count: int,
) -> int:
    _state_and_blocks(state_count, block_count)
    return balanced_safe_partial_count(state_count, block_count)


@dataclass(frozen=True)
class OperationFreedomRange:
    state_count: int
    block_count: int
    balanced_shape: tuple[int, ...]
    imbalanced_shape: tuple[int, ...]
    minimum_total_count: int
    maximum_total_count: int
    minimum_partial_count: int
    maximum_partial_count: int
    total_max_to_min_ratio: Fraction
    partial_max_to_min_ratio: Fraction


def operation_freedom_range(
    state_count: int,
    block_count: int,
) -> OperationFreedomRange:
    _state_and_blocks(state_count, block_count)
    min_total = minimum_safe_total_count_fixed_blocks(state_count, block_count)
    max_total = maximum_safe_total_count_fixed_blocks(state_count, block_count)
    min_partial = minimum_safe_partial_count_fixed_blocks(state_count, block_count)
    max_partial = maximum_safe_partial_count_fixed_blocks(state_count, block_count)
    if min_total > max_total or min_partial > max_partial:
        raise AssertionError("operation freedom extremals reversed")
    return OperationFreedomRange(
        state_count=state_count,
        block_count=block_count,
        balanced_shape=balanced_partition_shape(state_count, block_count),
        imbalanced_shape=maximally_imbalanced_partition_shape(
            state_count, block_count
        ),
        minimum_total_count=min_total,
        maximum_total_count=max_total,
        minimum_partial_count=min_partial,
        maximum_partial_count=max_partial,
        total_max_to_min_ratio=Fraction(max_total, min_total),
        partial_max_to_min_ratio=Fraction(max_partial, min_partial),
    )


def shape_safe_counts_lie_in_fixed_block_range(
    shape: Iterable[int],
) -> bool:
    values = tuple(shape)
    if not values:
        raise ValueError("shape must be nonempty")
    state_count = sum(values)
    block_count = len(values)
    report = operation_freedom_range(state_count, block_count)
    total = safe_total_count_from_shape(values)
    partial = safe_partial_count_from_shape(values)
    return (
        report.minimum_total_count <= total <= report.maximum_total_count
        and report.minimum_partial_count <= partial <= report.maximum_partial_count
    )
