"""Bridge the partial-action precision-genesis chain to safe-operation freedom.

The finite countdown precision-genesis model has ``n=N+1`` states and horizon
``h=0,...,n-1``.  Its predictive partition shape is

    (n-h, 1, ..., 1),

with ``h`` singleton blocks and class count ``b=h+1``.

The P023 majorization owner proves that, for fixed ``n`` and fixed class count
``b``, the unique partition maximizing deterministic total *and* partial safe
operation counts is exactly

    (n-b+1, 1, ..., 1).

Substituting ``b=h+1`` shows that the countdown precision filtration lies on the
safe-operation upper envelope at every horizon.  The minimal precision-genesis
chain therefore peels one singleton at a time while preserving the greatest
possible operation freedom among all partitions with the same class count.

Along this path:

* class count grows monotonically as ``h+1``;
* pair ambiguity falls monotonically as ``C(n-h,2)``;
* total safe-operation freedom is generally nonmonotone: it is complete at the
  indiscrete endpoint, falls to an intermediate valley, then returns to complete
  freedom at discrete precision;
* partial safe-operation freedom starts below complete freedom because the
  visible ``UNDEFINED`` output already constrains the indiscrete partition, and
  reaches complete freedom only at the discrete endpoint.

Exact path probabilities are

    P_total(h)   = ((n-h)^(n-h) + h)     / n^(n-h),
    P_partial(h) = ((n-h)^(n-h) + h + 1) / (n+1)^(n-h).

These are the fixed-class-count maximum formulas written in horizon coordinates.
The sibling upper-envelope analysis places the total valley at
``h=(1-1/e)n+O(1)`` analytically; this executable bridge stays exact and uses no
floating approximation.

This is a cross-owner specialization: P023/FQ-006 owns precision genesis,
P011 owns collision ambiguity, and the majorization owner owns operation-freedom
extremals.  No new generic invariant is introduced here.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb

from .operation_freedom_majorization import (
    maximum_safe_partial_count_fixed_blocks,
    maximum_safe_total_count_fixed_blocks,
    maximally_imbalanced_partition_shape,
)


def _inputs(state_count: int, horizon: int) -> tuple[int, int]:
    for name, value in (("state_count", state_count), ("horizon", horizon)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
    if state_count < 2:
        raise ValueError("state_count must be at least two")
    if not 0 <= horizon < state_count:
        raise ValueError("horizon must satisfy 0 <= h < state_count")
    return state_count, horizon


def genesis_predictive_shape(state_count: int, horizon: int) -> tuple[int, ...]:
    state_count, horizon = _inputs(state_count, horizon)
    return (state_count - horizon,) + (1,) * horizon


def genesis_class_count(state_count: int, horizon: int) -> int:
    _inputs(state_count, horizon)
    return horizon + 1


def genesis_tail_size(state_count: int, horizon: int) -> int:
    _inputs(state_count, horizon)
    return state_count - horizon


def genesis_collision_ambiguity(
    state_count: int,
    horizon: int,
    order: int,
) -> int:
    state_count, horizon = _inputs(state_count, horizon)
    if isinstance(order, bool) or not isinstance(order, int):
        raise TypeError("order must be an integer")
    if order < 2:
        raise ValueError("collision order must be at least two")
    tail = state_count - horizon
    return comb(tail, order) if tail >= order else 0


def genesis_pair_ambiguity(state_count: int, horizon: int) -> int:
    return genesis_collision_ambiguity(state_count, horizon, 2)


def genesis_total_safe_count(state_count: int, horizon: int) -> int:
    state_count, horizon = _inputs(state_count, horizon)
    block_count = horizon + 1
    return maximum_safe_total_count_fixed_blocks(state_count, block_count)


def genesis_partial_safe_count(state_count: int, horizon: int) -> int:
    state_count, horizon = _inputs(state_count, horizon)
    block_count = horizon + 1
    return maximum_safe_partial_count_fixed_blocks(state_count, block_count)


def genesis_total_safe_probability(state_count: int, horizon: int) -> Fraction:
    state_count, horizon = _inputs(state_count, horizon)
    return Fraction(
        genesis_total_safe_count(state_count, horizon),
        state_count**state_count,
    )


def genesis_partial_safe_probability(state_count: int, horizon: int) -> Fraction:
    state_count, horizon = _inputs(state_count, horizon)
    return Fraction(
        genesis_partial_safe_count(state_count, horizon),
        (state_count + 1) ** state_count,
    )


def genesis_total_safe_probability_closed(
    state_count: int,
    horizon: int,
) -> Fraction:
    state_count, horizon = _inputs(state_count, horizon)
    tail = state_count - horizon
    return Fraction(tail**tail + horizon, state_count**tail)


def genesis_partial_safe_probability_closed(
    state_count: int,
    horizon: int,
) -> Fraction:
    state_count, horizon = _inputs(state_count, horizon)
    tail = state_count - horizon
    return Fraction(
        tail**tail + horizon + 1,
        (state_count + 1) ** tail,
    )


def genesis_shape_is_fixed_class_operation_maximum(
    state_count: int,
    horizon: int,
) -> bool:
    state_count, horizon = _inputs(state_count, horizon)
    block_count = horizon + 1
    return genesis_predictive_shape(
        state_count, horizon
    ) == maximally_imbalanced_partition_shape(state_count, block_count)


def genesis_total_operation_valley_horizon(state_count: int) -> int:
    """Exact horizon minimizing total safe-operation probability along the path."""
    if isinstance(state_count, bool) or not isinstance(state_count, int):
        raise TypeError("state_count must be an integer")
    if state_count < 3:
        raise ValueError("state_count must be at least three")
    return min(
        range(state_count),
        key=lambda horizon: (
            genesis_total_safe_probability(state_count, horizon),
            horizon,
        ),
    )


def genesis_partial_operation_valley_horizon(state_count: int) -> int:
    """Exact horizon minimizing partial safe-operation probability along the path."""
    if isinstance(state_count, bool) or not isinstance(state_count, int):
        raise TypeError("state_count must be an integer")
    if state_count < 3:
        raise ValueError("state_count must be at least three")
    return min(
        range(state_count),
        key=lambda horizon: (
            genesis_partial_safe_probability(state_count, horizon),
            horizon,
        ),
    )


@dataclass(frozen=True)
class GenesisOperationStage:
    horizon: int
    class_count: int
    tail_size: int
    fiber_shape: tuple[int, ...]
    pair_ambiguity: int
    total_safe_probability: Fraction
    partial_safe_probability: Fraction


def genesis_operation_trajectory(
    state_count: int,
) -> tuple[GenesisOperationStage, ...]:
    if isinstance(state_count, bool) or not isinstance(state_count, int):
        raise TypeError("state_count must be an integer")
    if state_count < 2:
        raise ValueError("state_count must be at least two")
    return tuple(
        GenesisOperationStage(
            horizon=horizon,
            class_count=genesis_class_count(state_count, horizon),
            tail_size=genesis_tail_size(state_count, horizon),
            fiber_shape=genesis_predictive_shape(state_count, horizon),
            pair_ambiguity=genesis_pair_ambiguity(state_count, horizon),
            total_safe_probability=genesis_total_safe_probability(
                state_count, horizon
            ),
            partial_safe_probability=genesis_partial_safe_probability(
                state_count, horizon
            ),
        )
        for horizon in range(state_count)
    )
