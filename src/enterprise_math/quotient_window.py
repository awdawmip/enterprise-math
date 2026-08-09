"""Exact integer quotient-window transport.

This module is an executable reference for the P007 quotient-window
supplement.  It treats open-closed integer intervals ``(A, B]`` and the
exact quotient coordinate forced by multiplication by a positive factor.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class IntegerWindow:
    """A nonempty closed integer interval."""

    lo: int
    hi: int

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("IntegerWindow must be nonempty")

    @property
    def cardinality(self) -> int:
        return self.hi - self.lo + 1

    def contains(self, value: int) -> bool:
        return self.lo <= value <= self.hi


def quotient_window(a: int, b: int, factor: int) -> IntegerWindow | None:
    """Return ``{q : a < factor*q <= b}`` as an exact integer window."""

    if a < 0:
        raise ValueError("a must be nonnegative")
    if b <= a:
        raise ValueError("require a < b")
    if factor < 1:
        raise ValueError("factor must be positive")

    lo = a // factor + 1
    hi = b // factor
    if lo > hi:
        return None
    return IntegerWindow(lo, hi)


def exact_separation_criterion(a: int, b: int, d: int, e: int) -> bool:
    """Exact endpoint criterion for ``W_e`` to lie below ``W_d``.

    For ``d < e`` and nonempty windows, this is equivalent to every state in
    ``W_e(a,b)`` being strictly smaller than every state in ``W_d(a,b)``.
    Empty windows are harmless and are treated as separated by callers.
    """

    if not (0 <= a < b):
        raise ValueError("require 0 <= a < b")
    if not (1 <= d < e):
        raise ValueError("require 1 <= d < e")
    return b // e <= a // d


def cross_product_separation_sufficient(a: int, b: int, d: int, e: int) -> bool:
    """Pure-integer sufficient condition ``d*b <= e*a`` for separation."""

    if not (0 <= a < b):
        raise ValueError("require 0 <= a < b")
    if not (1 <= d < e):
        raise ValueError("require 1 <= d < e")
    return d * b <= e * a


def windows_strictly_separated(a: int, b: int, d: int, e: int) -> bool:
    """Whether the two realized windows are disjoint in strict order."""

    wd = quotient_window(a, b, d)
    we = quotient_window(a, b, e)
    if wd is None or we is None:
        return True
    return we.hi < wd.lo


def separation_gap(a: int, b: int, d: int, e: int) -> int | None:
    """Number of unused quotient states between separated nonempty windows.

    Returns ``None`` when either window is empty or when the windows are not
    strictly ordered.  A return value of zero means that the windows are
    adjacent.
    """

    wd = quotient_window(a, b, d)
    we = quotient_window(a, b, e)
    if wd is None or we is None or we.hi >= wd.lo:
        return None
    return wd.lo - we.hi - 1


def square_basin_window(k: int, factor: int) -> IntegerWindow | None:
    """Exact quotient window for the open consecutive-square basin.

    The source interval is ``(k^2, k(k+2)]``.
    """

    if k < 1:
        raise ValueError("k must be positive")
    return quotient_window(k * k, k * (k + 2), factor)


def square_spacing_condition(k: int, d: int, e: int) -> bool:
    """Equivalent cross-product condition ``k(e-d) >= 2d``."""

    if k < 1:
        raise ValueError("k must be positive")
    if not (1 <= d < e):
        raise ValueError("require 1 <= d < e")
    return k * (e - d) >= 2 * d
