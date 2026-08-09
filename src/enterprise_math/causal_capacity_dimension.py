"""Exact finite-difference dimension of integer continuation-capacity sequences.

If the minimum exact continuation-state count C(d) is an integer-valued
polynomial in slot depth d, define its causal state-growth dimension as the last
nonzero finite-difference order.  Equivalently Delta^(p+1) C vanishes while
Delta^p C is a nonzero constant on a sufficiently long exact sample.

This is a task/state growth invariant, not automatically physical spatial
dimension.  It is useful because bounded-increment additive bulk schemas give
polynomial capacity bounds whose degree is at most the number of nontrivial bulk
channels, while copy/history tasks have exponential capacity and no finite
polynomial difference depth.
"""

from __future__ import annotations


def finite_difference(values: tuple[int, ...]) -> tuple[int, ...]:
    if not isinstance(values, tuple) or len(values) < 2:
        raise ValueError("values must contain at least two integers")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in values):
        raise ValueError("values must be integers")
    return tuple(values[index + 1] - values[index] for index in range(len(values) - 1))


def sampled_polynomial_difference_degree(values: tuple[int, ...]) -> int | None:
    """Return the exact finite-difference degree visible on the full sample.

    The result is a proof about the supplied finite sequence only.  Promotion to
    an all-depth theorem requires an independent formula/recurrence proof.
    """
    if not isinstance(values, tuple) or not values:
        raise ValueError("values must be a non-empty tuple")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in values):
        raise ValueError("values must be integers")
    if len(values) == 1:
        return 0
    current = values
    for degree in range(len(values)):
        if len(set(current)) == 1:
            return degree
        if len(current) < 2:
            break
        current = finite_difference(current)
    return None


def exact_polynomial_sequence(values: tuple[int, ...], degree: int) -> bool:
    """Finite-sample check that Delta^degree is constant and next difference is zero."""
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 0:
        raise ValueError("degree must be a non-negative integer")
    if len(values) < degree + 2:
        raise ValueError("sample must be long enough to check the next difference")
    current = values
    for _ in range(degree):
        current = finite_difference(current)
    if len(set(current)) != 1:
        return False
    next_difference = finite_difference(current)
    return all(value == 0 for value in next_difference)


def product_capacity(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    """Pointwise product for independent same-depth state capacities."""
    if len(left) != len(right) or not left:
        raise ValueError("capacity sequences must have the same nonzero length")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in left + right
    ):
        raise ValueError("capacities must be non-negative integers")
    return tuple(a * b for a, b in zip(left, right))
