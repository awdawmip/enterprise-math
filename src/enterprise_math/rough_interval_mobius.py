"""Exact finite Mobius counts for p-rough integers in integer intervals.

An integer is p-rough exactly when it is coprime to the square-free primorial of
all primes below p.  Inclusion-exclusion over the divisors of that primorial
therefore gives an exact interval count.  This is a reference implementation,
not an asymptotically efficient sieve.
"""

from __future__ import annotations

from math import gcd

from .legendre import primes_up_to, squarefree_divisors_with_mu


def lower_primorial(prime: int) -> int:
    """Product of all primes strictly below ``prime``."""

    if isinstance(prime, bool) or not isinstance(prime, int) or prime < 2:
        raise ValueError("prime threshold must be an integer >=2")
    product = 1
    for q in primes_up_to(prime - 1):
        product *= q
    return product


def rough_interval_mobius_count(lower: int, upper: int, prime: int) -> int:
    """Exact count of integers in [lower,upper] with no prime divisor < prime."""

    if isinstance(lower, bool) or isinstance(upper, bool):
        raise ValueError("interval endpoints must be integers")
    if not isinstance(lower, int) or not isinstance(upper, int) or lower < 1 or upper < lower:
        raise ValueError("require positive integer interval with lower <= upper")
    if isinstance(prime, bool) or not isinstance(prime, int) or prime < 2:
        raise ValueError("prime threshold must be an integer >=2")

    small_primes = primes_up_to(prime - 1)
    total = 0
    for divisor, mu in squarefree_divisors_with_mu(small_primes):
        multiples = upper // divisor - (lower - 1) // divisor
        total += mu * multiples
    if total < 0:
        raise AssertionError("Mobius rough count became negative")
    return total


def rough_interval_direct_count(lower: int, upper: int, prime: int) -> int:
    """Direct gcd oracle used only for bounded differential tests."""

    primorial = lower_primorial(prime)
    return sum(gcd(value, primorial) == 1 for value in range(lower, upper + 1))


def rough_interval_occupied(lower: int, upper: int, prime: int) -> bool:
    return rough_interval_mobius_count(lower, upper, prime) > 0
