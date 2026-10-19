#!/usr/bin/env python3
"""Exact finite checks for the prime-winding partition geometry.

Everything here is finite and rational/integer.  No numerical pi/tau target,
logarithm, or floating Euler product is used.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import lcm


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def primes_upto(limit: int) -> list[int]:
    return [n for n in range(2, limit + 1) if is_prime(n)]


def vp_int(n: int, p: int) -> int:
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def winding_weight(primes: list[int], exponents: tuple[int, ...]) -> Fraction:
    w = Fraction(1, 1)
    for p, e in zip(primes, exponents):
        w *= Fraction(1, p ** (2 * e))
    return w


def winding_mass_sum(M: int, K: int) -> Fraction:
    primes = primes_upto(M)
    return sum(
        (winding_weight(primes, exps)
         for exps in product(range(K + 1), repeat=len(primes))),
        Fraction(0, 1),
    )


def winding_mass_product(M: int, K: int) -> Fraction:
    z = Fraction(1, 1)
    for p in primes_upto(M):
        local = sum(
            (Fraction(1, p ** (2 * e)) for e in range(K + 1)),
            Fraction(0, 1),
        )
        z *= local
    return z


def winding_mass_closed(M: int, K: int) -> Fraction:
    z = Fraction(1, 1)
    for p in primes_upto(M):
        z *= Fraction(p ** (2 * (K + 1)) - 1, p ** (2 * K) * (p * p - 1))
    return z


def z_birth(M: int) -> Fraction:
    z = Fraction(1, 1)
    for p in primes_upto(M):
        z *= Fraction(p * p, p * p - 1)
    return z


def max_winding_below(M: int, p: int) -> int:
    a = 0
    power = 1
    while power * p <= M:
        power *= p
        a += 1
    return a


def check_finite_partition() -> None:
    # Keep the brute-force Cartesian product modest; every identity is exact.
    for M in (1, 2, 3, 5, 7, 11):
        previous = Fraction(0, 1)
        for K in range(0, 5):
            by_sum = winding_mass_sum(M, K)
            by_product = winding_mass_product(M, K)
            by_closed = winding_mass_closed(M, K)
            assert by_sum == by_product == by_closed, (M, K)
            assert previous <= by_sum
            previous = by_sum

            # Exact finite truncation sits below the all-winding Euler factor.
            assert by_sum <= z_birth(M)
            if primes_upto(M):
                assert by_sum < z_birth(M)


def check_lcm_winding_envelope(limit: int = 120) -> None:
    current_lcm = 1
    for M in range(1, limit + 1):
        current_lcm = lcm(current_lcm, M)
        reconstructed = 1
        for p in primes_upto(M):
            a = max_winding_below(M, p)
            reconstructed *= p**a
            assert vp_int(current_lcm, p) == a, (M, p, a)
        assert reconstructed == current_lcm, M


def check_pure_winding_labels(limit: int = 100) -> None:
    # Prime powers are exactly one-coordinate occupation states.
    for n in range(2, limit + 1):
        support = []
        residual = n
        for p in primes_upto(n):
            e = vp_int(n, p)
            if e:
                support.append((p, e))
                residual //= p**e
        assert residual == 1
        is_prime_power = len(support) == 1
        if is_prime_power:
            p, e = support[0]
            assert n == p**e
        else:
            assert len(support) >= 2


def main() -> None:
    check_finite_partition()
    check_lcm_winding_envelope()
    check_pure_winding_labels()
    print("pi-prime winding partition finite checks: PASS")


if __name__ == "__main__":
    main()
