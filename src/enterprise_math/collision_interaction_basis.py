"""Binomial interaction basis for symmetric finite fiber responses.

For an integer response phi(n) depending only on the number n of indistinguishable
unit histories in one fiber, define interaction coefficients

    a_k = sum_{j=0}^k (-1)^(k-j) C(k,j) phi(j).

Finite binomial inversion gives

    phi(n) = sum_{k=0}^n a_k C(n,k).

Therefore for a finite collapse F with fiber sizes m_y,

    sum_y phi(m_y) = sum_k a_k J_k(F),

where J_k is the P011 collision spectrum. Thus J_k is an exact universal basis
for every bounded symmetric integer fiber-local response. No labels on the
individual unit histories are needed.

For one merge of old fiber sizes b_1,...,b_r, the exact response defect is

    Delta R_phi = sum_k a_k Delta J_k.

Since every Delta J_k is a nonnegative count of newly cross-fiber k-subsets,
nonnegative higher-order interaction coefficients give a direct causal
sufficient condition for monotone irreversibility.
"""

from __future__ import annotations

from math import comb


Counts = tuple[int, ...]


def _require_values(values: tuple[int, ...]) -> None:
    if not isinstance(values, tuple) or not values:
        raise ValueError("values must be a non-empty tuple indexed from n=0")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in values):
        raise ValueError("response values must be integers")


def _require_positive_counts(counts: Counts) -> None:
    if not isinstance(counts, tuple) or not counts:
        raise ValueError("counts must be a non-empty tuple")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in counts
    ):
        raise ValueError("counts must be positive integers")


def binomial_interaction_coefficients(
    values: tuple[int, ...],
) -> tuple[int, ...]:
    """Return exact a_k from the finite response table phi(0),...,phi(N)."""
    _require_values(values)
    return tuple(
        sum(
            (-1 if (order - state) % 2 else 1)
            * comb(order, state)
            * values[state]
            for state in range(order + 1)
        )
        for order in range(len(values))
    )


def reconstruct_response_value(
    coefficients: tuple[int, ...],
    count: int,
) -> int:
    """Reconstruct phi(count)=sum_k a_k C(count,k) exactly."""
    if not isinstance(coefficients, tuple) or not coefficients:
        raise ValueError("coefficients must be a non-empty tuple")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for value in coefficients
    ):
        raise ValueError("coefficients must be integers")
    if isinstance(count, bool) or not isinstance(count, int) or count < 0:
        raise ValueError("count must be a non-negative integer")
    if count >= len(coefficients):
        raise ValueError("count exceeds the response table range")
    return sum(
        coefficients[order] * comb(count, order)
        for order in range(count + 1)
    )


def collision_spectrum_from_fiber_sizes(
    fiber_sizes: Counts,
    maximum_order: int | None = None,
) -> tuple[int, ...]:
    """Return J_0..J_K for positive fiber sizes.

    J_0 is included only as a bookkeeping coordinate counting nonempty fibers.
    P011's canonical collision spectrum starts at J_1.
    """
    if not isinstance(fiber_sizes, tuple):
        raise ValueError("fiber_sizes must be a tuple")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in fiber_sizes
    ):
        raise ValueError("fiber sizes must be positive integers")
    total = sum(fiber_sizes)
    limit = total if maximum_order is None else maximum_order
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 0:
        raise ValueError("maximum_order must be a non-negative integer")
    return tuple(
        sum(comb(size, order) for size in fiber_sizes if size >= order)
        for order in range(limit + 1)
    )


def symmetric_fiber_response(
    fiber_sizes: Counts,
    values: tuple[int, ...],
) -> int:
    """Direct sum_y phi(m_y), requiring phi(0)=0 for empty-fiber neutrality."""
    _require_values(values)
    if values[0] != 0:
        raise ValueError("phi(0) must be zero for a reachable-fiber observable")
    if any(size >= len(values) for size in fiber_sizes):
        raise ValueError("response table does not cover every fiber size")
    return sum(values[size] for size in fiber_sizes)


def symmetric_fiber_response_from_collisions(
    fiber_sizes: Counts,
    values: tuple[int, ...],
) -> int:
    """Compute the same response using only interaction coefficients and J_k."""
    _require_values(values)
    if values[0] != 0:
        raise ValueError("phi(0) must be zero for a reachable-fiber observable")
    coefficients = binomial_interaction_coefficients(values)
    spectrum = collision_spectrum_from_fiber_sizes(
        fiber_sizes,
        maximum_order=len(values) - 1,
    )
    # a_0=phi(0)=0, so the bookkeeping J_0 coordinate is irrelevant.
    return sum(
        coefficients[order] * spectrum[order]
        for order in range(1, len(values))
    )


def merge_collision_increments(
    old_fiber_sizes: Counts,
    maximum_order: int | None = None,
) -> tuple[int, ...]:
    """Exact Delta J_k caused by merging all supplied old fibers into one."""
    _require_positive_counts(old_fiber_sizes)
    merged = sum(old_fiber_sizes)
    limit = merged if maximum_order is None else maximum_order
    if isinstance(limit, bool) or not isinstance(limit, int) or limit < 0:
        raise ValueError("maximum_order must be a non-negative integer")
    return tuple(
        comb(merged, order)
        - sum(comb(size, order) for size in old_fiber_sizes if size >= order)
        for order in range(limit + 1)
    )


def merge_response_defect(
    old_fiber_sizes: Counts,
    values: tuple[int, ...],
) -> int:
    """Direct phi(sum b_i)-sum_i phi(b_i)."""
    _require_positive_counts(old_fiber_sizes)
    _require_values(values)
    merged = sum(old_fiber_sizes)
    if merged >= len(values):
        raise ValueError("response table must cover the merged fiber size")
    return values[merged] - sum(values[size] for size in old_fiber_sizes)


def merge_response_defect_from_collisions(
    old_fiber_sizes: Counts,
    values: tuple[int, ...],
) -> int:
    """Exact same defect as sum_k a_k Delta J_k."""
    _require_positive_counts(old_fiber_sizes)
    _require_values(values)
    merged = sum(old_fiber_sizes)
    if merged >= len(values):
        raise ValueError("response table must cover the merged fiber size")
    coefficients = binomial_interaction_coefficients(values)
    increments = merge_collision_increments(
        old_fiber_sizes,
        maximum_order=len(values) - 1,
    )
    return sum(
        coefficients[order] * increments[order]
        for order in range(1, len(values))
    )


def higher_interactions_nonnegative(values: tuple[int, ...]) -> bool:
    """Whether every a_k for k>=2 is nonnegative."""
    coefficients = binomial_interaction_coefficients(values)
    return all(coefficient >= 0 for coefficient in coefficients[2:])


def pair_interaction_strict(values: tuple[int, ...]) -> bool:
    """Whether a_2>0, sufficient for strict growth under every genuine merge."""
    coefficients = binomial_interaction_coefficients(values)
    return len(coefficients) > 2 and coefficients[2] > 0
