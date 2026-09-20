"""Lift-safe residue sieving for quotient/fiber factor searches.

This module specializes Enterprise Math's existing precision/refinement and
operation-safe quotient principles to arithmetic lifts

    p = r + M*x.

A divisibility observer modulo ell may be pushed down to the coarse prefix r
only when it is constant on the full x-fiber.  Otherwise the smallest exact
repair coordinate is x modulo ell/gcd(M, ell).

Finite exact arithmetic only.  This module does not claim factorization speedups,
primality, or global branch emptiness from a bounded search window.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, lcm
from typing import Iterable


NEVER = "NEVER"
ALL = "ALL"
ONE_CLASS = "ONE_CLASS"


@dataclass(frozen=True, slots=True)
class LiftDivisibilityClass:
    """Exact solution class for ``modulus | (prefix + stride*x)``.

    status:
      * NEVER: no integer x solves the divisibility constraint;
      * ALL: every integer x solves it;
      * ONE_CLASS: exactly one residue class modulo ``period`` solves it.
    """

    modulus: int
    gcd_with_stride: int
    status: str
    period: int
    residue: int | None

    def contains(self, x: int) -> bool:
        if isinstance(x, bool) or not isinstance(x, int):
            raise ValueError("x must be an integer")
        if self.status == NEVER:
            return False
        if self.status == ALL:
            return True
        if self.status != ONE_CLASS or self.residue is None or self.period <= 1:
            raise AssertionError("invalid ONE_CLASS certificate")
        return x % self.period == self.residue


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def lift_divisibility_class(prefix: int, stride: int, modulus: int) -> LiftDivisibilityClass:
    """Solve ``modulus | prefix + stride*x`` exactly over all integer x.

    Let d=gcd(stride, modulus).  A solution exists iff d divides prefix.  When it
    exists, division by d leaves a coprime linear congruence and therefore one
    residue class modulo modulus/d.  If modulus/d == 1, every x is a solution.
    """

    _require_int("prefix", prefix)
    _require_int("stride", stride)
    _require_int("modulus", modulus)
    if stride <= 0:
        raise ValueError("stride must be positive")
    if modulus <= 1:
        raise ValueError("modulus must exceed 1")

    d = gcd(stride, modulus)
    if prefix % d != 0:
        return LiftDivisibilityClass(modulus, d, NEVER, modulus // d, None)

    period = modulus // d
    if period == 1:
        return LiftDivisibilityClass(modulus, d, ALL, 1, 0)

    reduced_stride = stride // d
    reduced_prefix = prefix // d
    residue = (-reduced_prefix * pow(reduced_stride, -1, period)) % period
    return LiftDivisibilityClass(modulus, d, ONE_CLASS, period, residue)


def divisibility_observer_globally_descends(stride: int, modulus: int) -> bool:
    """Whether divisibility modulo ``modulus`` is constant on every stride-fiber.

    For the quotient map p -> p mod stride, the predicate ``modulus | p``
    descends for every prefix exactly when modulus divides stride.
    """

    _require_int("stride", stride)
    _require_int("modulus", modulus)
    if stride <= 0:
        raise ValueError("stride must be positive")
    if modulus <= 1:
        raise ValueError("modulus must exceed 1")
    return stride % modulus == 0


def lift_value(prefix: int, stride: int, x: int) -> int:
    _require_int("prefix", prefix)
    _require_int("stride", stride)
    _require_int("x", x)
    if stride <= 0:
        raise ValueError("stride must be positive")
    return prefix + stride * x


def is_filter_prime_hit(prefix: int, stride: int, x: int, prime: int) -> bool:
    """Return whether the lifted candidate is divisible by the supplied filter prime."""

    return lift_divisibility_class(prefix, stride, prime).contains(x)


def wheel_constraints(prefix: int, stride: int, filter_primes: Iterable[int]) -> tuple[LiftDivisibilityClass, ...]:
    """Compile exact quotient constraints for each supplied wheel prime."""

    primes = tuple(filter_primes)
    if not primes:
        raise ValueError("filter_primes must be nonempty")
    if len(primes) != len(set(primes)):
        raise ValueError("filter_primes must be distinct")
    if any(isinstance(p, bool) or not isinstance(p, int) or p <= 1 for p in primes):
        raise ValueError("filter_primes must contain integers > 1")
    return tuple(lift_divisibility_class(prefix, stride, p) for p in primes)


def repair_period(prefix: int, stride: int, filter_primes: Iterable[int]) -> int:
    """Smallest joint period implied by the compiled divisibility classes.

    This is a sufficient exact repair coordinate for the wheel observer: retaining
    x modulo this period preserves every supplied modular divisibility output.
    """

    period = 1
    for cert in wheel_constraints(prefix, stride, filter_primes):
        if cert.status == ONE_CLASS:
            period = lcm(period, cert.period)
    return period


def wheel_rejects_lift(
    prefix: int,
    stride: int,
    x: int,
    filter_primes: Iterable[int],
    *,
    preserve_equal_prime: bool = True,
) -> bool:
    """Whether a concrete lifted candidate is safely rejected by the wheel.

    ``preserve_equal_prime`` keeps the small-prime factor itself: candidate==p is
    not rejected merely because it is divisible by p.  This mirrors the usual
    factor-search rule that exact small factors are successes, not composites.
    """

    candidate = lift_value(prefix, stride, x)
    for p, cert in zip(tuple(filter_primes), wheel_constraints(prefix, stride, filter_primes)):
        if cert.contains(x):
            if preserve_equal_prime and candidate == p:
                continue
            return True
    return False


def surviving_window(
    prefix: int,
    stride: int,
    start_x: int,
    stop_x: int,
    filter_primes: Iterable[int],
    *,
    preserve_equal_prime: bool = True,
) -> tuple[int, ...]:
    """Return all quotient indices x in [start_x, stop_x) not rejected by the wheel."""

    _require_int("start_x", start_x)
    _require_int("stop_x", stop_x)
    if stop_x < start_x:
        raise ValueError("stop_x must be >= start_x")
    primes = tuple(filter_primes)
    certs = wheel_constraints(prefix, stride, primes)
    survivors: list[int] = []
    for x in range(start_x, stop_x):
        candidate = lift_value(prefix, stride, x)
        rejected = False
        for p, cert in zip(primes, certs):
            if cert.contains(x) and not (preserve_equal_prime and candidate == p):
                rejected = True
                break
        if not rejected:
            survivors.append(x)
    return tuple(survivors)
