"""Integer-only division semantics for Enterprise Math.

Quotient, same-state-space multiple collapse, and reversible Euclidean state
are intentionally represented as different operations.
"""

from __future__ import annotations


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def integer_quotient(n: int, divisor: int) -> int:
    """Return the greatest q such that divisor*q <= n."""
    _require_natural("n", n)
    _require_positive("divisor", divisor)
    return n // divisor


def multiple_collapse(n: int, divisor: int) -> int:
    """Project n to the greatest multiple of divisor not exceeding n."""
    return divisor * integer_quotient(n, divisor)


def division_gap(n: int, divisor: int) -> int:
    """Return the derived Euclidean gap n - multiple_collapse(n, divisor)."""
    return n - multiple_collapse(n, divisor)


def euclidean_state(n: int, divisor: int) -> tuple[int, int]:
    """Return the explicit reversible quotient/remainder state (q, r)."""
    quotient = integer_quotient(n, divisor)
    remainder = n - divisor * quotient
    return quotient, remainder


def reconstruct_euclidean(quotient: int, remainder: int, divisor: int) -> int:
    """Reconstruct n from an explicitly represented Euclidean state."""
    _require_natural("quotient", quotient)
    _require_natural("remainder", remainder)
    _require_positive("divisor", divisor)
    if remainder >= divisor:
        raise ValueError("remainder must be smaller than divisor")
    return divisor * quotient + remainder
