"""Signed integer-state extensions for Enterprise Math.

This module deliberately separates ordinary-order roots from signed-magnitude
quantization. The two operations agree on non-negative inputs but are not the
same operation on negative states.

No floating-point values or true division are used here.
"""

from __future__ import annotations

from .core import integer_nth_root


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _sign(value: int) -> int:
    if value > 0:
        return 1
    if value < 0:
        return -1
    return 0


def signed_order_root(n: int, p: int) -> int:
    """Greatest integer k with k**p <= n, for odd positive p.

    Even powers are intentionally rejected because k -> k**p is not monotone
    on the ordinary integer order and therefore has no ordinary-order right
    adjoint on all of Z.
    """
    _require_integer("n", n)
    _require_positive("p", p)
    if p % 2 == 0:
        raise ValueError("signed_order_root requires an odd exponent")

    if n >= 0:
        return integer_nth_root(n, p)

    magnitude = -n
    floor_root = integer_nth_root(magnitude, p)
    ceiling_root = floor_root if floor_root**p == magnitude else floor_root + 1
    return -ceiling_root


def signed_order_collapse(n: int, p: int) -> int:
    """Ordinary-order collapse induced by signed_order_root."""
    root = signed_order_root(n, p)
    return root**p


def signed_magnitude_root(n: int, p: int) -> int:
    """Root the explicit magnitude and restore the sign, for any positive p."""
    _require_integer("n", n)
    _require_positive("p", p)
    return _sign(n) * integer_nth_root(abs(n), p)


def signed_magnitude_collapse(n: int, p: int) -> int:
    """Quantize magnitude downward while preserving sign, for any positive p."""
    _require_integer("n", n)
    _require_positive("p", p)
    root = integer_nth_root(abs(n), p)
    return _sign(n) * root**p
