"""Exact upper-envelope valleys of safe-operation freedom at fixed class count.

The parent majorization theorem gives, for fixed state count ``n`` and observation
block count ``b``, a unique maximum safe-operation shape

    (L,1,...,1),   L=n-b+1.

For total endomaps its normalized safe probability is exactly

    P_total_max(n,L) = (L^L + n-L) / n^L.

For deterministic partial endomaps it is

    P_partial_max(n,L) = (L^L + n-L+1) / (n+1)^L.

The leading ideal surrogates are

    J_total(n,L)   = (L/n)^L,
    J_partial(n,L) = (L/(n+1))^L.

The exact multiplicative corrections are therefore

    1 + (n-L)/L^L,
    1 + (n-L+1)/L^L.

This makes the upper-envelope problem one-dimensional in the giant-fiber size
``L``.  The continuous total surrogate has unique minimum at ``L=n/e`` and the
partial surrogate at ``L=(n+1)/e``.  Because the correction is exponentially
small when ``L`` is a positive fraction of ``n`` and the surrogate has curvature
``1/L``, the true discrete envelope minimizers satisfy

    L_total  = n/e       + O(1),
    L_partial= (n+1)/e   + O(1).

Consequently the block counts are

    b_total  = (1-1/e)n + O(1),
    b_partial= n+1-(n+1)/e + O(1),

and the minimum upper-envelope probabilities have logarithms

    -n/e       + O(1/n),
    -(n+1)/e   + O(1/n).

The executable layer remains integer/rational-only.  It computes exact true and
ideal envelope minimizers and exact candidate windows obtained from the ideal
surrogate plus the correction at its integer minimizer.  The asymptotic
statements are ordinary analytic consequences documented in the research PR.

This upper envelope has a different scale from the balanced lower envelope:
its extremal shape has one giant fiber of size about ``n/e`` and about
``(1-1/e)n`` singleton fibers, whereas the globally most constraining balanced
partition has typical block size about ``W(e*n)``.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from .operation_freedom_majorization import (
    maximum_safe_partial_count_fixed_blocks,
    maximum_safe_total_count_fixed_blocks,
    maximally_imbalanced_partition_shape,
)


def _state_count(state_count: int) -> None:
    if isinstance(state_count, bool) or not isinstance(state_count, int):
        raise TypeError("state_count must be an integer")
    if state_count < 3:
        raise ValueError("state_count must be at least three")


def _giant_size(state_count: int, giant_size: int) -> None:
    _state_count(state_count)
    if isinstance(giant_size, bool) or not isinstance(giant_size, int):
        raise TypeError("giant_size must be an integer")
    if not 2 <= giant_size < state_count:
        raise ValueError("giant_size must correspond to a genuine intermediate partition")


def block_count_from_giant_size(state_count: int, giant_size: int) -> int:
    _giant_size(state_count, giant_size)
    return state_count - giant_size + 1


def giant_size_from_block_count(state_count: int, block_count: int) -> int:
    _state_count(state_count)
    if isinstance(block_count, bool) or not isinstance(block_count, int):
        raise TypeError("block_count must be an integer")
    if not 2 <= block_count < state_count:
        raise ValueError("block_count must be a genuine intermediate count")
    return state_count - block_count + 1


def maximum_total_safe_probability_by_giant_size(
    state_count: int,
    giant_size: int,
) -> Fraction:
    """Exact fixed-class-count upper envelope in total-operation probability."""
    block_count = block_count_from_giant_size(state_count, giant_size)
    count = maximum_safe_total_count_fixed_blocks(state_count, block_count)
    return Fraction(count, state_count**state_count)


def maximum_partial_safe_probability_by_giant_size(
    state_count: int,
    giant_size: int,
) -> Fraction:
    """Exact fixed-class-count upper envelope in partial-operation probability."""
    block_count = block_count_from_giant_size(state_count, giant_size)
    count = maximum_safe_partial_count_fixed_blocks(state_count, block_count)
    return Fraction(count, (state_count + 1) ** state_count)


def ideal_total_upper_envelope_probability(
    state_count: int,
    giant_size: int,
) -> Fraction:
    """Ideal total surrogate ``(L/n)^L``."""
    _giant_size(state_count, giant_size)
    return Fraction(giant_size**giant_size, state_count**giant_size)


def ideal_partial_upper_envelope_probability(
    state_count: int,
    giant_size: int,
) -> Fraction:
    """Ideal partial surrogate ``(L/(n+1))^L``."""
    _giant_size(state_count, giant_size)
    return Fraction(giant_size**giant_size, (state_count + 1) ** giant_size)


def total_upper_envelope_correction(
    state_count: int,
    giant_size: int,
) -> Fraction:
    return maximum_total_safe_probability_by_giant_size(
        state_count, giant_size
    ) / ideal_total_upper_envelope_probability(state_count, giant_size)


def partial_upper_envelope_correction(
    state_count: int,
    giant_size: int,
) -> Fraction:
    return maximum_partial_safe_probability_by_giant_size(
        state_count, giant_size
    ) / ideal_partial_upper_envelope_probability(state_count, giant_size)


def ideal_total_giant_size(state_count: int) -> int:
    """Exact integer minimizer of ``(L/n)^L`` over genuine intermediate L."""
    _state_count(state_count)
    return min(
        range(2, state_count),
        key=lambda giant_size: (
            ideal_total_upper_envelope_probability(state_count, giant_size),
            giant_size,
        ),
    )


def ideal_partial_giant_size(state_count: int) -> int:
    """Exact integer minimizer of ``(L/(n+1))^L``."""
    _state_count(state_count)
    return min(
        range(2, state_count),
        key=lambda giant_size: (
            ideal_partial_upper_envelope_probability(state_count, giant_size),
            giant_size,
        ),
    )


def true_total_upper_envelope_giant_size(state_count: int) -> int:
    """Exact minimizer of the maximum total-safe probability over class counts."""
    _state_count(state_count)
    return min(
        range(2, state_count),
        key=lambda giant_size: (
            maximum_total_safe_probability_by_giant_size(
                state_count, giant_size
            ),
            giant_size,
        ),
    )


def true_partial_upper_envelope_giant_size(state_count: int) -> int:
    """Exact minimizer of the maximum partial-safe probability over class counts."""
    _state_count(state_count)
    return min(
        range(2, state_count),
        key=lambda giant_size: (
            maximum_partial_safe_probability_by_giant_size(
                state_count, giant_size
            ),
            giant_size,
        ),
    )


def total_upper_envelope_candidate_giant_sizes(state_count: int) -> tuple[int, ...]:
    """Exact ideal-surrogate window guaranteed to contain the true total minimizer."""
    ideal_size = ideal_total_giant_size(state_count)
    threshold = maximum_total_safe_probability_by_giant_size(
        state_count, ideal_size
    )
    return tuple(
        giant_size
        for giant_size in range(2, state_count)
        if ideal_total_upper_envelope_probability(
            state_count, giant_size
        ) <= threshold
    )


def partial_upper_envelope_candidate_giant_sizes(state_count: int) -> tuple[int, ...]:
    """Exact ideal-surrogate window guaranteed to contain the true partial minimizer."""
    ideal_size = ideal_partial_giant_size(state_count)
    threshold = maximum_partial_safe_probability_by_giant_size(
        state_count, ideal_size
    )
    return tuple(
        giant_size
        for giant_size in range(2, state_count)
        if ideal_partial_upper_envelope_probability(
            state_count, giant_size
        ) <= threshold
    )


@dataclass(frozen=True)
class OperationFreedomEnvelopeValley:
    state_count: int
    total_giant_size: int
    total_block_count: int
    total_shape: tuple[int, ...]
    total_probability: Fraction
    partial_giant_size: int
    partial_block_count: int
    partial_shape: tuple[int, ...]
    partial_probability: Fraction
    total_ideal_giant_size: int
    partial_ideal_giant_size: int


def operation_freedom_envelope_valley(
    state_count: int,
) -> OperationFreedomEnvelopeValley:
    _state_count(state_count)
    total_giant = true_total_upper_envelope_giant_size(state_count)
    partial_giant = true_partial_upper_envelope_giant_size(state_count)
    total_blocks = block_count_from_giant_size(state_count, total_giant)
    partial_blocks = block_count_from_giant_size(state_count, partial_giant)
    if total_giant not in total_upper_envelope_candidate_giant_sizes(state_count):
        raise AssertionError("true total upper-envelope valley escaped exact candidate window")
    if partial_giant not in partial_upper_envelope_candidate_giant_sizes(state_count):
        raise AssertionError("true partial upper-envelope valley escaped exact candidate window")
    return OperationFreedomEnvelopeValley(
        state_count=state_count,
        total_giant_size=total_giant,
        total_block_count=total_blocks,
        total_shape=maximally_imbalanced_partition_shape(
            state_count, total_blocks
        ),
        total_probability=maximum_total_safe_probability_by_giant_size(
            state_count, total_giant
        ),
        partial_giant_size=partial_giant,
        partial_block_count=partial_blocks,
        partial_shape=maximally_imbalanced_partition_shape(
            state_count, partial_blocks
        ),
        partial_probability=maximum_partial_safe_probability_by_giant_size(
            state_count, partial_giant
        ),
        total_ideal_giant_size=ideal_total_giant_size(state_count),
        partial_ideal_giant_size=ideal_partial_giant_size(state_count),
    )
