"""Exact sandwich behind the asymptotic safe-operation constraint scale.

The balancing theorem reduces the global total-operation constraint valley on
``n`` states to balanced partitions, one candidate for each block count
``b=2,...,n-1``.  Let the balanced block sizes be ``q`` and ``q+1`` with mean
``m=n/b``.

Writing normalized block masses relative to the uniform mass ``1/b`` gives, for
one source exponent ``k`` in ``{q,q+1}``, a collision correction

    D_k = sum_j (1/b) * (block_size_j / m)^k.

The weighted mean of the relative block sizes is one.  Convexity of ``t^k``
therefore gives ``D_k>=1``.  Also every relative block size is at most
``(q+1)/q`` and every source exponent is at most ``q+1``; hence

    D_k <= (1+1/q)^(q+1) <= 4.

Consequently the exact balanced safe-total probability satisfies

    b^(b-n) <= P_bal(n,b) <= 4^b * b^(b-n).

The lower term is precisely the continuous equal-block objective, even when
``b`` does not divide ``n``.  Integer imbalance therefore contributes at most
``b log 4`` to the logarithmic objective.

This module keeps the executable theorem integer/rational only.  It also builds
an exact candidate window around the minimizer of the lower surrogate:

    I(n,b) = b^(b-n).

Let ``b0`` minimize ``I`` over integer intermediate block counts.  If ``b_hat``
minimizes the true balanced probability, then

    I(n,b_hat) <= P_bal(n,b_hat)
               <= P_bal(n,b0)
               <= 4^b0 I(n,b0).

Thus every true minimizer lies in the exact finite set

    { b : I(n,b) <= 4^b0 I(n,b0) }.

The continuous minimizer of ``I`` solves

    n/b = 1 + log b,

so its mean block size is ``W(e*n)``.  The sandwich plus the curvature of the
continuous objective implies the global balanced minimizer has

    m_n = W(e*n) * (1 + O(W(e*n)^(-1/2))).

That analytic asymptotic is documented in the research PR; no floating or
Lambert-W evaluation is used here.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .balanced_operation_constraint_valley import (
    balanced_partition_shape,
    balanced_safe_total_count,
    most_constraining_partition,
)


def _state_and_blocks(state_count: int, block_count: int) -> None:
    for name, value in (("state_count", state_count), ("block_count", block_count)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
    if state_count < 3:
        raise ValueError("state_count must be at least three")
    if not 2 <= block_count < state_count:
        raise ValueError("block_count must be a genuine intermediate count")


def ideal_equal_block_probability(state_count: int, block_count: int) -> Fraction:
    """Continuous equal-mass surrogate ``b^(b-n)`` as an exact rational."""
    _state_and_blocks(state_count, block_count)
    return Fraction(1, block_count ** (state_count - block_count))


def balanced_total_safe_probability(state_count: int, block_count: int) -> Fraction:
    """Exact safe-total probability for the balanced integer partition."""
    _state_and_blocks(state_count, block_count)
    return Fraction(
        balanced_safe_total_count(state_count, block_count),
        state_count**state_count,
    )


def balanced_rounding_correction(state_count: int, block_count: int) -> Fraction:
    """Exact multiplicative correction ``P_bal / I``."""
    return balanced_total_safe_probability(
        state_count, block_count
    ) / ideal_equal_block_probability(state_count, block_count)


def balanced_probability_sandwich_holds(state_count: int, block_count: int) -> bool:
    """Check ``I <= P_bal <= 4^b I`` exactly."""
    ideal = ideal_equal_block_probability(state_count, block_count)
    actual = balanced_total_safe_probability(state_count, block_count)
    return ideal <= actual <= (4**block_count) * ideal


def ideal_integer_block_count(state_count: int) -> int:
    """Exact integer minimizer of the continuous equal-block surrogate on b=2..n-1."""
    if isinstance(state_count, bool) or not isinstance(state_count, int):
        raise TypeError("state_count must be an integer")
    if state_count < 3:
        raise ValueError("state_count must be at least three")
    return min(
        range(2, state_count),
        key=lambda block_count: (
            ideal_equal_block_probability(state_count, block_count),
            block_count,
        ),
    )


def ideal_candidate_block_counts(state_count: int) -> tuple[int, ...]:
    """Exact block-count window guaranteed to contain every true balanced minimizer."""
    b0 = ideal_integer_block_count(state_count)
    threshold = (4**b0) * ideal_equal_block_probability(state_count, b0)
    return tuple(
        block_count
        for block_count in range(2, state_count)
        if ideal_equal_block_probability(state_count, block_count) <= threshold
    )


def true_valley_lies_in_ideal_candidate_window(state_count: int) -> bool:
    """Executable consequence of the exact probability sandwich."""
    valley = most_constraining_partition(state_count)
    return valley.block_count in ideal_candidate_block_counts(state_count)


@dataclass(frozen=True)
class OperationValleySandwichReport:
    state_count: int
    true_block_count: int
    true_block_shape: tuple[int, ...]
    ideal_integer_block_count: int
    candidate_block_counts: tuple[int, ...]
    true_safe_probability: Fraction
    ideal_probability_at_true_block_count: Fraction
    rounding_correction: Fraction


def operation_valley_sandwich_report(state_count: int) -> OperationValleySandwichReport:
    valley = most_constraining_partition(state_count)
    b0 = ideal_integer_block_count(state_count)
    candidates = ideal_candidate_block_counts(state_count)
    if valley.block_count not in candidates:
        raise AssertionError("true valley escaped exact ideal candidate window")
    return OperationValleySandwichReport(
        state_count=state_count,
        true_block_count=valley.block_count,
        true_block_shape=balanced_partition_shape(
            state_count, valley.block_count
        ),
        ideal_integer_block_count=b0,
        candidate_block_counts=candidates,
        true_safe_probability=valley.safe_probability,
        ideal_probability_at_true_block_count=ideal_equal_block_probability(
            state_count, valley.block_count
        ),
        rounding_correction=balanced_rounding_correction(
            state_count, valley.block_count
        ),
    )
