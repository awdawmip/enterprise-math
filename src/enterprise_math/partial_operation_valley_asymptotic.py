"""Partial-operation constraint valleys share the total Lambert-W scale.

For one partition shape ``lambda=(n_1,...,n_b)`` write

    S_k = sum_j n_j^k.

The exact safe counts are

    N_total   = product_i S_(n_i),
    N_partial = product_i (1 + S_(n_i)).

Therefore

    N_partial / N_total
      = product_i (1 + 1 / S_(n_i)).

Every ``S_(n_i)`` is at least the block count ``b`` because every block size is
positive.  Hence the entire shape-dependent price of permitting the extra
``UNDEFINED`` output obeys

    1 <= N_partial/N_total <= (1+1/b)^b < e.

After normalizing by the two operation universes, the safe probabilities satisfy

    P_partial
      = (n/(n+1))^n * P_total
        * product_i (1 + 1/S_(n_i)).

The first factor depends only on ``n`` and the last factor is globally bounded
by ``(1+1/b)^b``.  Thus partial-operation freedom has the same dominant
partition geometry as total-operation freedom.

For balanced integer partitions combine this identity with the total sandwich

    I(n,b) <= P_total_bal <= 4^b I(n,b),

where ``I(n,b)=b^(b-n)``.  One obtains the exact partial sandwich

    alpha_n I(n,b)
      <= P_partial_bal
      <= alpha_n (1+1/b)^b 4^b I(n,b),

with ``alpha_n=(n/(n+1))^n``.

Consequently the same ideal integer block-count minimizer and Lambert-W
continuous scale control the partial valley.  The true total and partial
minimizers may differ at finite ``n``, but both have mean block size

    W(e*n) * (1 + O(W(e*n)^(-1/2))).

This module keeps every executable statement rational/integer-only.  The
Lambert-W asymptotic is an analytic consequence recorded in the research PR and
is not evaluated here.
"""

from __future__ import annotations

from fractions import Fraction

from .balanced_operation_constraint_valley import balanced_partition_shape
from .balanced_partial_operation_constraint_valley import (
    balanced_safe_partial_count,
    most_constraining_partial_partition,
)
from .operation_valley_asymptotic import (
    ideal_equal_block_probability,
    ideal_integer_block_count,
)
from .safe_operation_collision_moments import (
    safe_partial_probability,
    safe_total_probability,
)


def _block_count(partition) -> int:
    labels = set(partition.values())
    if not partition:
        raise ValueError("partition must be nonempty")
    return len(labels)


def partial_to_total_count_ratio(partition) -> Fraction:
    """Exact ``N_partial/N_total`` using probability/universe normalization."""
    n = len(partition)
    if n <= 0:
        raise ValueError("partition must be nonempty")
    p_partial = safe_partial_probability(partition)
    p_total = safe_total_probability(partition)
    return (
        p_partial
        * (n + 1) ** n
        / (p_total * n**n)
    )


def partial_to_total_shape_factor_upper_bound(partition) -> Fraction:
    """Exact bound ``(1+1/b)^b`` for the undefined-choice shape factor."""
    b = _block_count(partition)
    return Fraction((b + 1) ** b, b**b)


def partial_to_total_shape_factor_bound_holds(partition) -> bool:
    ratio = partial_to_total_count_ratio(partition)
    return Fraction(1, 1) <= ratio <= partial_to_total_shape_factor_upper_bound(
        partition
    )


def partial_universe_scale(state_count: int) -> Fraction:
    """Shape-independent factor ``alpha_n=(n/(n+1))^n``."""
    if isinstance(state_count, bool) or not isinstance(state_count, int):
        raise TypeError("state_count must be an integer")
    if state_count <= 0:
        raise ValueError("state_count must be positive")
    return Fraction(state_count**state_count, (state_count + 1) ** state_count)


def balanced_partial_safe_probability(state_count: int, block_count: int) -> Fraction:
    if isinstance(state_count, bool) or not isinstance(state_count, int):
        raise TypeError("state_count must be an integer")
    if isinstance(block_count, bool) or not isinstance(block_count, int):
        raise TypeError("block_count must be an integer")
    if state_count < 3 or not 2 <= block_count < state_count:
        raise ValueError("requires a genuine intermediate balanced partition")
    return Fraction(
        balanced_safe_partial_count(state_count, block_count),
        (state_count + 1) ** state_count,
    )


def balanced_partial_probability_sandwich_holds(
    state_count: int,
    block_count: int,
) -> bool:
    """Exact partial sandwich around the same ideal equal-block surrogate."""
    ideal = ideal_equal_block_probability(state_count, block_count)
    alpha = partial_universe_scale(state_count)
    actual = balanced_partial_safe_probability(state_count, block_count)
    shape_bound = Fraction(
        (block_count + 1) ** block_count,
        block_count**block_count,
    )
    return alpha * ideal <= actual <= (
        alpha * shape_bound * 4**block_count * ideal
    )


def partial_ideal_candidate_block_counts(state_count: int) -> tuple[int, ...]:
    """Exact ideal-surrogate window guaranteed to contain the partial valley."""
    if isinstance(state_count, bool) or not isinstance(state_count, int):
        raise TypeError("state_count must be an integer")
    if state_count < 3:
        raise ValueError("state_count must be at least three")
    b0 = ideal_integer_block_count(state_count)
    bound = Fraction((b0 + 1) ** b0, b0**b0)
    threshold = (
        bound
        * 4**b0
        * ideal_equal_block_probability(state_count, b0)
    )
    return tuple(
        block_count
        for block_count in range(2, state_count)
        if ideal_equal_block_probability(state_count, block_count) <= threshold
    )


def partial_valley_lies_in_ideal_candidate_window(state_count: int) -> bool:
    valley = most_constraining_partial_partition(state_count)
    return valley.block_count in partial_ideal_candidate_block_counts(state_count)


def total_and_partial_balanced_shapes(
    state_count: int,
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Return the exact total/partial global balanced valley shapes for comparison."""
    from .balanced_operation_constraint_valley import most_constraining_partition

    total = most_constraining_partition(state_count)
    partial = most_constraining_partial_partition(state_count)
    return (
        balanced_partition_shape(state_count, total.block_count),
        balanced_partition_shape(state_count, partial.block_count),
    )
