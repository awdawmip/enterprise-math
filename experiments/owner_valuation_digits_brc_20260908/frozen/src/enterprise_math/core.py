"""Integer-only reference operations for Enterprise Math v0.1.

No floating-point values or true division are used in this module.
"""

from __future__ import annotations


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def integer_nth_root(n: int, p: int) -> int:
    """Return the unique k such that k**p <= n < (k+1)**p."""
    _require_natural("n", n)
    _require_positive("p", p)

    if n < 2 or p == 1:
        return n

    lo = 0
    hi = 1
    while hi**p <= n:
        hi *= 2

    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if mid**p <= n:
            lo = mid
        else:
            hi = mid
    return lo


def collapse(n: int, p: int = 2) -> int:
    """Project n downward to the greatest perfect p-th power not exceeding n."""
    k = integer_nth_root(n, p)
    return k**p


def basin_for_root(k: int, p: int = 2) -> tuple[int, int]:
    """Return the inclusive input interval whose p-collapse is k**p."""
    _require_natural("k", k)
    _require_positive("p", p)
    return k**p, (k + 1) ** p - 1


def preimage_count(k: int, p: int = 2) -> int:
    """Return the number of natural states in the collapse basin of k**p."""
    start, end = basin_for_root(k, p)
    return end - start + 1


def scaled_root(n: int, p: int, base: int, level: int) -> int:
    """Root state after refining the input by base**(p*level)."""
    _require_natural("n", n)
    _require_positive("p", p)
    _require_positive("base", base)
    _require_natural("level", level)
    return integer_nth_root(n * base ** (p * level), p)


def project_scale(value: int, base: int, levels: int = 1) -> int:
    """Project an integer state to a coarser scale by integer division."""
    _require_natural("value", value)
    _require_positive("base", base)
    _require_natural("levels", levels)
    return value // base**levels
