"""Midpoint Franel p^2 lifting as a parameter-transversality problem.

For an odd prime p=5 or 7 (mod 8), put m=(p-1)/2.  Jarvis--Verrill forces
p|F_m.  This module implements the exact first-order refinement

    F_m / p == (1/2) * dF/dx |_(x=m)        (mod p),

where

    F(x) = _3F_2(-x,-x,-x;1,1;-1)

and, at a nonnegative integer n,

    F'(n)=3 sum_k C(n,k)^3 (H_n-H_(n-k)).

Equivalently, because the weights are symmetric and F_m=0 mod p,

    F_m/p == -(3/2) sum_k C(m,k)^3 H_k                 (mod p)
          == -(3/2) sum_k (-1)^k C(2k,k)^3 H_k/64^k  (mod p).

Thus p^2|F_m iff the parameter derivative vanishes modulo p.  The proof is a
first-order refinement of the reflected Franel recurrence; the implementation
cross-checks the derivative recurrence, harmonic formula, and existing p^2
recurrence oracle.
"""

from __future__ import annotations

from .p022_barlow_franel_half_index import half_index, half_index_is_forced_zero
from .p022_barlow_half_defect_obstructions import half_index_lift_quotient
from .p022_barlow_low_order_defect_reduction import _is_prime


def _require_forced_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
        or not half_index_is_forced_zero(prime)
    ):
        raise ValueError("prime must be an odd prime in 5 or 7 modulo 8")


def franel_table_mod(prime: int, stop: int) -> tuple[int, ...]:
    """F_0,...,F_stop modulo p from the exact recurrence, with stop<p."""
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")
    if isinstance(stop, bool) or not isinstance(stop, int) or not 0 <= stop < prime:
        raise ValueError("stop must lie in 0..p-1")
    if stop == 0:
        return (1,)
    values = [1, 2 % prime]
    for n in range(1, stop):
        a_n = 7 * n * n + 7 * n + 2
        numerator = (a_n * values[n] + 8 * n * n * values[n - 1]) % prime
        denominator = ((n + 1) * (n + 1)) % prime
        values.append(numerator * pow(denominator, -1, prime) % prime)
    return tuple(values)


def parameter_derivative_table_mod(prime: int, stop: int) -> tuple[int, ...]:
    """F'(0),...,F'(stop) mod p via the differentiated Franel recurrence."""
    values = franel_table_mod(prime, stop)
    if stop == 0:
        return (0,)
    derivative = [0, 3 % prime]
    for n in range(1, stop):
        a_n = 7 * n * n + 7 * n + 2
        forcing = (
            2 * (n + 1) * values[n + 1]
            - 7 * (2 * n + 1) * values[n]
            - 16 * n * values[n - 1]
        ) % prime
        numerator = (
            a_n * derivative[n]
            + 8 * n * n * derivative[n - 1]
            - forcing
        ) % prime
        denominator = ((n + 1) * (n + 1)) % prime
        derivative.append(numerator * pow(denominator, -1, prime) % prime)
    return tuple(derivative)


def parameter_derivative_harmonic_mod(prime: int, index: int) -> int:
    """Direct finite formula 3*sum C(n,k)^3(H_n-H_(n-k)) modulo p."""
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")
    if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < prime:
        raise ValueError("index must lie in 0..p-1")

    harmonic = [0]
    for k in range(1, index + 1):
        harmonic.append((harmonic[-1] + pow(k, -1, prime)) % prime)

    total = 0
    binomial = 1
    for k in range(0, index + 1):
        if k > 0:
            binomial = (
                binomial
                * (index - k + 1)
                * pow(k, -1, prime)
            ) % prime
        weight = pow(binomial, 3, prime)
        total += weight * (harmonic[index] - harmonic[index - k])
    return (3 * total) % prime


def midpoint_derivative_lift_quotient(prime: int) -> int:
    """Return F_m/p mod p using only the mod-p parameter derivative."""
    _require_forced_prime(prime)
    midpoint = half_index(prime)
    derivative = parameter_derivative_table_mod(prime, midpoint)[midpoint]
    return derivative * pow(2, -1, prime) % prime


def midpoint_harmonic_lift_quotient(prime: int) -> int:
    """Equivalent -(3/2) sum C(m,k)^3 H_k formula modulo p."""
    _require_forced_prime(prime)
    midpoint = half_index(prime)
    harmonic = 0
    binomial = 1
    total = 0
    for k in range(0, midpoint + 1):
        if k > 0:
            harmonic = (harmonic + pow(k, -1, prime)) % prime
            binomial = (
                binomial
                * (midpoint - k + 1)
                * pow(k, -1, prime)
            ) % prime
        total = (total + pow(binomial, 3, prime) * harmonic) % prime
    return (-3 * total * pow(2, -1, prime)) % prime


def midpoint_central_harmonic_lift_quotient(prime: int) -> int:
    """Equivalent central-binomial harmonic sum modulo p."""
    _require_forced_prime(prime)
    midpoint = half_index(prime)
    harmonic = 0
    total = 0
    central = 1
    inv64 = pow(64, -1, prime)
    power_inv64 = 1
    sign = 1
    for k in range(0, midpoint + 1):
        if k > 0:
            harmonic = (harmonic + pow(k, -1, prime)) % prime
            central = (
                central
                * (2 * k)
                * (2 * k - 1)
                * pow(k * k, -1, prime)
            ) % prime
            power_inv64 = power_inv64 * inv64 % prime
            sign = -sign
        total = (
            total
            + sign * pow(central, 3, prime) * power_inv64 * harmonic
        ) % prime
    return (-3 * total * pow(2, -1, prime)) % prime


def midpoint_transversality_profile(prime: int) -> tuple[int, int, int, bool]:
    """Return derivative, lift quotient, p^2-oracle quotient, and simple-root flag."""
    _require_forced_prime(prime)
    midpoint = half_index(prime)
    derivative = parameter_derivative_table_mod(prime, midpoint)[midpoint]
    derivative_lift = derivative * pow(2, -1, prime) % prime
    direct_lift = half_index_lift_quotient(prime)
    if derivative_lift != direct_lift:
        raise AssertionError("first-order reflection lift and p^2 recurrence must agree")
    if midpoint_harmonic_lift_quotient(prime) != direct_lift:
        raise AssertionError("harmonic parameter-derivative formula must agree")
    if midpoint_central_harmonic_lift_quotient(prime) != direct_lift:
        raise AssertionError("central-binomial harmonic formula must agree")
    return derivative, derivative_lift, direct_lift, derivative != 0
