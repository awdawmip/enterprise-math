"""Exact finite counting boundary for fixed BRC vertical residue wheels.

A fixed modulus wheel is periodic in the vertical offset t.  If its period is P
and one-period support S has size s, then the exact number of retained offsets in
0<=t<T is

    floor(T/P)*s + #{r in S : r < T mod P}.

Hence every fixed nonempty wheel retains Theta(T) offsets.  This module also
records two elementary reasons the support is nonempty on every classically
admissible difference-of-squares strip and gives the exact local support count
for one odd prime modulus.

All number theory in this module is classical.  The purpose is to freeze a
negative/complexity boundary for the BRC vertical-wheel route so fixed tables
are not mistaken for an exponent-changing mechanism.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _ceil_sqrt(value: int) -> int:
    root = isqrt(value)
    return root if root * root == value else root + 1


def periodic_support_count(
    period: int, offsets: tuple[int, ...], t_limit: int
) -> int:
    """Exact count of translated wheel offsets in ``0 <= t < t_limit``."""
    _require_positive("period", period)
    _require_natural("t_limit", t_limit)
    if any(isinstance(r, bool) or not isinstance(r, int) or not 0 <= r < period for r in offsets):
        raise ValueError("offsets must be integers in one period")
    if tuple(sorted(set(offsets))) != offsets:
        raise ValueError("offsets must be unique and sorted")
    q, tail = divmod(t_limit, period)
    return q * len(offsets) + sum(r < tail for r in offsets)


@dataclass(frozen=True)
class DifferenceSquarePair:
    value: int
    x: int
    y: int
    t_from_ceiling: int

    def __post_init__(self) -> None:
        _require_positive("value", self.value)
        _require_natural("x", self.x)
        _require_natural("y", self.y)
        _require_natural("t_from_ceiling", self.t_from_ceiling)
        if self.x < self.y:
            raise ValueError("difference-square pair requires x>=y")
        if self.x * self.x - self.y * self.y != self.value:
            raise ValueError("difference-square pair failed reconstruction")
        if self.x - _ceil_sqrt(self.value) != self.t_from_ceiling:
            raise ValueError("stored vertical offset disagrees with ceiling root")


def canonical_difference_square_pair(value: int) -> DifferenceSquarePair:
    """Construct one classical x^2-y^2=value representation when possible.

    Positive integers are differences of two integer squares exactly when they
    are not 2 modulo 4.
    """
    _require_positive("value", value)
    if value % 4 == 2:
        raise ValueError("integers congruent to 2 mod 4 are not differences of squares")
    if value % 2:
        x = (value + 1) // 2
        y = (value - 1) // 2
    else:
        q = value // 4
        x = q + 1
        y = abs(q - 1)
    return DifferenceSquarePair(
        value=value,
        x=x,
        y=y,
        t_from_ceiling=x - _ceil_sqrt(value),
    )


def fixed_squarehood_wheel_must_be_nonempty(value: int, modulus: int) -> bool:
    """Certificate that a fixed QR wheel has at least one live t residue.

    For an admissible difference-of-squares value, use the canonical global
    representation x^2-y^2=value.  At t=x-ceil(sqrt(value)), the gap is y^2,
    hence a square residue modulo every modulus.
    """
    _require_positive("modulus", modulus)
    pair = canonical_difference_square_pair(value)
    t = pair.t_from_ceiling % modulus
    base = _ceil_sqrt(value)
    gap_mod = ((base + t) * (base + t) - value) % modulus
    target = pair.y * pair.y % modulus
    # t may differ from the original offset by a multiple of modulus; the
    # quadratic polynomial is periodic modulo modulus.
    return gap_mod == target


def _is_odd_prime_reference(p: int) -> bool:
    if p < 3 or p % 2 == 0:
        return False
    d = 3
    while d * d <= p:
        if p % d == 0:
            return False
        d += 2
    return True


def legendre_symbol_reference(value: int, p: int) -> int:
    """Reference Legendre symbol for an odd prime p."""
    if not _is_odd_prime_reference(p):
        raise ValueError("p must be an odd prime")
    residue = value % p
    if residue == 0:
        return 0
    result = pow(residue, (p - 1) // 2, p)
    return -1 if result == p - 1 else int(result)


def prime_shift_square_support_count(p: int, c: int) -> int:
    """Count x mod p with x^2-c a quadratic residue (zero included).

    For odd prime p:
    - c == 0 mod p -> p;
    - c a nonzero QR -> (p+1)/2;
    - c a nonresidue -> (p-1)/2.
    """
    if not _is_odd_prime_reference(p):
        raise ValueError("p must be an odd prime")
    symbol = legendre_symbol_reference(c, p)
    if symbol == 0:
        return p
    return (p + symbol) // 2


@dataclass(frozen=True)
class FixedWheelBoundary:
    period: int
    support_size: int
    t_limit: int
    exact_candidates: int
    full_periods: int
    tail: int

    @property
    def positive_density_numerator(self) -> int:
        return self.support_size

    @property
    def positive_density_denominator(self) -> int:
        return self.period


def fixed_wheel_boundary(
    period: int, offsets: tuple[int, ...], t_limit: int
) -> FixedWheelBoundary:
    """Return exact finite data witnessing the fixed-wheel linear law."""
    _require_positive("period", period)
    _require_natural("t_limit", t_limit)
    if not offsets:
        raise ValueError("boundary theorem requires a nonempty wheel")
    count = periodic_support_count(period, offsets, t_limit)
    q, tail = divmod(t_limit, period)
    return FixedWheelBoundary(
        period=period,
        support_size=len(offsets),
        t_limit=t_limit,
        exact_candidates=count,
        full_periods=q,
        tail=tail,
    )


__all__ = [
    "DifferenceSquarePair",
    "FixedWheelBoundary",
    "periodic_support_count",
    "canonical_difference_square_pair",
    "fixed_squarehood_wheel_must_be_nonempty",
    "legendre_symbol_reference",
    "prime_shift_square_support_count",
    "fixed_wheel_boundary",
]
