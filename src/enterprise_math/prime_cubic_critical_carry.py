"""Cubic specialization of the generic R005-B reciprocal-gap carry compiler.

The mother arithmetic now lives in ``prime_reciprocal_gap_carry``.  This module
retains cubic names used by the p=3 research notes/tests and adds only the cubic
full-nonforcing upgrade ``q>k``.
"""

from .prime_reciprocal_gap_carry import (
    reciprocal_boundary_prime,
    reciprocal_endpoint_state,
    reciprocal_integer_depth,
    reciprocal_jump_carry,
    reciprocal_prime_lag_budget,
    reciprocal_real_gap_threshold,
    reciprocal_three_layer_carry,
    reciprocal_threshold,
    reciprocal_threshold_ladder,
)


def cubic_real_gap_threshold(a: int, k: int) -> int:
    return reciprocal_real_gap_threshold(k, 3, a)


def cubic_reciprocal_endpoint_state(a: int, k: int) -> tuple[int, int, int, int]:
    return reciprocal_endpoint_state(k, 3, a)


def cubic_reciprocal_integer_depth(a: int, b: int, k: int) -> int:
    return reciprocal_integer_depth(k, 3, a, b)


def cubic_reciprocal_threshold(a: int, k: int, depth: int = 0) -> int:
    return reciprocal_threshold(k, 3, a, depth)


def cubic_reciprocal_jump_carry(a: int, k: int) -> tuple[int, int, int]:
    return reciprocal_jump_carry(k, 3, a)


def cubic_reciprocal_three_layer_carry(a: int, k: int) -> tuple[int, int, int, int]:
    return reciprocal_three_layer_carry(k, 3, a)


def cubic_reciprocal_threshold_ladder(a: int, k: int, max_depth: int) -> tuple[int, ...]:
    return reciprocal_threshold_ladder(k, 3, a, max_depth)


def cubic_lower_boundary_prime(a: int, b: int, k: int) -> int | None:
    return reciprocal_boundary_prime(k, 3, a, b)


def cubic_lower_full_nonforced_candidate(a: int, b: int, k: int) -> int | None:
    q = reciprocal_boundary_prime(k, 3, a, b)
    return q if q is not None and q > k else None


def cubic_prime_lag_budget(a: int, b: int, k: int) -> tuple[int, int, int, int]:
    return reciprocal_prime_lag_budget(k, 3, a, b)
