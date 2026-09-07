#!/usr/bin/env python3
"""Finite checks for the rough/smooth product-budget covariance law.

The checker performs two tasks:

1. With integer prime weights, it verifies exactly that the first derivative of
   the centered rough-prefix/small-suffix coupling is the covariance obtained
   from the prime-pair floor formula.
2. With the RH-critical choices Y=(log X)^2 and f(q)=sqrt(q), it prints a
   finite numerical pilot approaching the proved continuum main term -2.

The asymptotic theorem is proved in the accompanying research note.  The
finite table is a regression/diagnostic only and is not evidence for RH.
"""

from __future__ import annotations

from bisect import bisect_right
from fractions import Fraction
from math import log, sqrt


def primes_up_to(limit: int) -> list[int]:
    if limit < 2:
        return []
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0] = sieve[1] = 0
    for prime in range(2, int(limit**0.5) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start : limit + 1 : prime] = b"\x00" * (
                (limit - start) // prime + 1
            )
    return [integer for integer, flag in enumerate(sieve) if flag]


def exact_pair_covariance(limit: int, cutoff: int, weight) -> Fraction:
    primes = primes_up_to(limit)
    small = [prime for prime in primes if prime <= cutoff]
    rough = [prime for prime in primes if prime > cutoff]

    joint = Fraction(0)
    for small_prime in small:
        for rough_prime in rough:
            if small_prime * rough_prime > limit:
                break
            joint += Fraction(
                weight(small_prime) * (limit // (small_prime * rough_prime)),
                limit,
            )

    rough_mean = sum(
        Fraction(limit // prime, limit) for prime in rough
    )
    small_mean = sum(
        Fraction(weight(prime) * (limit // prime), limit)
        for prime in small
    )
    return joint - rough_mean * small_mean


def exact_direct_covariance(limit: int, cutoff: int, weight) -> Fraction:
    primes = primes_up_to(limit)
    small = [prime for prime in primes if prime <= cutoff]
    rough = [prime for prime in primes if prime > cutoff]

    rough_total = 0
    small_total = 0
    product_total = 0
    for integer in range(1, limit + 1):
        rough_count = sum(integer % prime == 0 for prime in rough)
        small_source = sum(
            weight(prime) for prime in small if integer % prime == 0
        )
        rough_total += rough_count
        small_total += small_source
        product_total += rough_count * small_source

    return (
        Fraction(product_total, limit)
        - Fraction(rough_total, limit) * Fraction(small_total, limit)
    )


def critical_covariance(limit: int) -> tuple[int, float, float]:
    cutoff = int(log(limit) ** 2)
    primes = primes_up_to(limit)
    split = bisect_right(primes, cutoff)
    small = primes[:split]
    rough = primes[split:]

    rough_mean = sum(limit // prime for prime in rough) / limit
    small_mean = sum(
        sqrt(prime) * (limit // prime) for prime in small
    ) / limit

    joint = 0.0
    for small_prime in small:
        upper = bisect_right(primes, limit // small_prime)
        joint += sqrt(small_prime) * sum(
            limit // (small_prime * rough_prime)
            for rough_prime in primes[split:upper]
        ) / limit

    covariance = joint - rough_mean * small_mean
    continuum_main = -2.0 * sqrt(cutoff) / log(limit)
    return cutoff, covariance, continuum_main


def main() -> None:
    integer_weight = lambda prime: prime + 1
    for limit in (30, 60, 100):
        cutoff = int(log(limit) ** 2)
        assert exact_pair_covariance(
            limit, cutoff, integer_weight
        ) == exact_direct_covariance(limit, cutoff, integer_weight)

    print("exact prime-pair covariance identities passed")
    print("X          Y        covariance          continuum main")
    last_error = None
    for limit in (10_000, 100_000, 1_000_000):
        cutoff, covariance, main_term = critical_covariance(limit)
        error = abs(covariance + 2.0)
        if last_error is not None:
            assert error < last_error
        last_error = error
        print(
            f"{limit:<10d} {cutoff:<8d} "
            f"{covariance: .12f}    {main_term: .12f}"
        )

    assert last_error is not None and last_error < 0.1
    print("critical finite pilot is consistent with covariance -> -2")


if __name__ == "__main__":
    main()
