"""Reduce the residual Gessel--Lucas copy-depth failure to one fixed rank gcd.

Let F'_r be Straub's formal derivative of the Franel recurrence.  Its harmonic
formula has denominator supported only on primes <=r.  Hence any primitive
Franel prime q at rank r satisfies q>=2r+1 and sees that denominator as a
q-adic unit.

The mod-q^2 copy analysis leaves only the double-stationary source

    q^2 | F_r  and  q | F'_r.

Therefore q must divide the fixed integer

    G_r = gcd(F_r, numerator(F'_r)).

This module packages that exact reduction.  A bounded pressure helper also
records the current empirical observation that G_r is r-smooth on tested
ranges.  That smoothness is NOT asserted as a uniform theorem here.
"""

from __future__ import annotations

from math import gcd, lcm

from .p022_barlow_franel_gessel_lucas_copy import (
    copy_depth_obstruction,
    franel_formal_derivative,
)
from .p022_barlow_low_order_defect_reduction import _factor_integer
from .p022_barlow_low_order_identifiability import p_adic_valuation, triple_moment_factor
from .p022_barlow_primitive_defect_criterion import is_primitive_franel_divisor


def harmonic_denominator_bound(rank: int) -> int:
    """LCM(1,...,r), a denominator bound for the Franel formal derivative."""
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 0:
        raise ValueError("rank must be non-negative")
    result = 1
    for value in range(1, rank + 1):
        result = lcm(result, value)
    derivative = franel_formal_derivative(rank)
    if result % derivative.denominator:
        raise AssertionError("formal derivative denominator must divide lcm(1..r)")
    return result


def stationary_fixed_gcd(rank: int) -> int:
    """G_r=gcd(F_r,num(F'_r)), the fixed double-stationary obstruction."""
    if isinstance(rank, bool) or not isinstance(rank, int) or rank <= 0:
        raise ValueError("rank must be positive")
    derivative = franel_formal_derivative(rank)
    harmonic_denominator_bound(rank)
    return gcd(triple_moment_factor(rank), abs(derivative.numerator))


def primitive_double_stationary_forces_fixed_gcd(rank: int, prime: int) -> int:
    """Exact reduction of a primitive double-stationary source to q|G_r."""
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at rank")
    if prime <= rank:
        raise AssertionError("primitive Franel prime must exceed the source rank")
    if harmonic_denominator_bound(rank) % prime == 0:
        raise AssertionError("primitive prime must be a unit on the harmonic denominator")
    depth, derivative, exceptional = copy_depth_obstruction(rank, prime)
    if depth < 2 or derivative != 0 or not exceptional:
        raise ValueError("source is not the double-stationary copy obstruction")
    fixed = stationary_fixed_gcd(rank)
    if fixed % prime:
        raise AssertionError("double-stationary primitive prime must divide the fixed gcd")
    if p_adic_valuation(triple_moment_factor(rank), prime) < 2:
        raise AssertionError("double-stationary obstruction requires source depth at least two")
    return fixed


def stationary_gcd_large_prime_factors(rank: int) -> tuple[int, ...]:
    """Prime factors of G_r strictly above r; empty means the rank is smooth."""
    fixed = stationary_fixed_gcd(rank)
    return tuple(prime for prime, _ in _factor_integer(fixed) if prime > rank)


def bounded_stationary_gcd_is_rank_smooth(max_rank: int) -> bool:
    """Finite pressure check only: G_r has no prime factor >r through max_rank."""
    if isinstance(max_rank, bool) or not isinstance(max_rank, int) or max_rank < 1:
        raise ValueError("max_rank must be positive")
    for rank in range(1, max_rank + 1):
        if stationary_gcd_large_prime_factors(rank):
            return False
    return True
