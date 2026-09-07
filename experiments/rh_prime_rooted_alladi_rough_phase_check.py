#!/usr/bin/env python3
"""Exact regression for the prime-rooted Alladi / rough-phase transport.

The checker verifies:
1. the averaged collective Alladi polynomial grouped by its least-prime root;
2. the exact prime-cutoff jump identity for the rough phase;
3. the Stieltjes representation of the Alladi average;
4. prime-scale summation by parts and the t=0 / t=1 endpoint observers.

All arithmetic is exact Fraction arithmetic. The checker is a finite
algebraic certificate, not an asymptotic theorem and not evidence for RH.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Callable, List


def primes_up_to(limit: int) -> List[int]:
    sieve = [True] * (limit + 1)
    if limit >= 0:
        sieve[0] = False
    if limit >= 1:
        sieve[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            for multiple in range(p * p, limit + 1, p):
                sieve[multiple] = False
    return [n for n, flag in enumerate(sieve) if flag]


def distinct_prime_factors(n: int, primes: List[int]) -> List[int]:
    factors: List[int] = []
    residue = n
    for p in primes:
        if p * p > residue:
            break
        if residue % p:
            continue
        factors.append(p)
        while residue % p == 0:
            residue //= p
    if residue > 1:
        factors.append(residue)
    return factors


def rough_depth(n: int, cutoff: int, primes: List[int]) -> int:
    return sum(p > cutoff for p in distinct_prime_factors(n, primes))


def rough_phase(limit: int, cutoff: int, t: Fraction, primes: List[int]) -> Fraction:
    return sum(
        (1 - t) ** rough_depth(n, cutoff, primes)
        for n in range(1, limit + 1)
    ) / limit


def alladi_value(
    n: int,
    t: Fraction,
    cutoff: int,
    weight: Callable[[int], Fraction],
    primes: List[int],
) -> Fraction:
    descending = list(reversed(distinct_prime_factors(n, primes)))
    total = Fraction(0)
    for rank, p in enumerate(descending, start=1):
        if p <= cutoff:
            total -= (1 - t) ** (rank - 1) * weight(p)
    return total


def averaged_alladi(
    limit: int,
    t: Fraction,
    cutoff: int,
    weight: Callable[[int], Fraction],
    primes: List[int],
) -> Fraction:
    return sum(
        alladi_value(n, t, cutoff, weight, primes)
        for n in range(1, limit + 1)
    ) / limit


def rooted_alladi(
    limit: int,
    t: Fraction,
    cutoff: int,
    weight: Callable[[int], Fraction],
    primes: List[int],
) -> Fraction:
    total = Fraction(0)
    for q in primes:
        if q > cutoff:
            break
        residual = limit // q
        total -= (
            weight(q)
            * Fraction(residual, limit)
            * rough_phase(residual, q, t, primes)
        )
    return total


def jump_alladi(
    limit: int,
    t: Fraction,
    cutoff: int,
    weight: Callable[[int], Fraction],
    primes: List[int],
) -> Fraction:
    assert t
    total = Fraction(0)
    for q in primes:
        if q > cutoff:
            break
        jump = (
            rough_phase(limit, q, t, primes)
            - rough_phase(limit, q - 1, t, primes)
        )
        total -= weight(q) * jump / t
    return total


def verify_prime_jump(
    limit: int, t: Fraction, cutoff: int, primes: List[int]
) -> None:
    for q in primes:
        if q > cutoff:
            break
        residual = limit // q
        jump = (
            rough_phase(limit, q, t, primes)
            - rough_phase(limit, q - 1, t, primes)
        )
        rooted = (
            t
            * Fraction(residual, limit)
            * rough_phase(residual, q, t, primes)
        )
        assert jump == rooted


def verify_summation_by_parts(
    limit: int,
    t: Fraction,
    cutoff: int,
    weight: Callable[[int], Fraction],
    primes: List[int],
) -> None:
    active = [p for p in primes if p <= cutoff]
    phases = [rough_phase(limit, 1, t, primes)] + [
        rough_phase(limit, p, t, primes) for p in active
    ]

    jump_pairing = sum(
        weight(p) * (phases[index + 1] - phases[index])
        for index, p in enumerate(active)
    )

    centered = (
        weight(active[-1]) * (phases[-1] - 1)
        - weight(active[0]) * (phases[0] - 1)
        - sum(
            (weight(active[index + 1]) - weight(active[index]))
            * (phases[index + 1] - 1)
            for index in range(len(active) - 1)
        )
    )
    assert jump_pairing == centered


def verify_endpoints(
    limit: int,
    cutoff: int,
    weight: Callable[[int], Fraction],
    primes: List[int],
) -> None:
    at_zero = averaged_alladi(
        limit, Fraction(0), cutoff, weight, primes
    )
    prime_source = -sum(
        weight(q) * Fraction(limit // q, limit)
        for q in primes
        if q <= cutoff
    )
    assert at_zero == prime_source

    at_one = averaged_alladi(
        limit, Fraction(1), cutoff, weight, primes
    )
    largest_prime_source = Fraction(0)
    for n in range(2, limit + 1):
        factors = distinct_prime_factors(n, primes)
        largest = factors[-1]
        if largest <= cutoff:
            largest_prime_source -= weight(largest)
    largest_prime_source /= limit
    assert at_one == largest_prime_source


def main() -> None:
    limit = 84
    cutoff = 11
    t = Fraction(2, 5)
    primes = primes_up_to(limit)
    weight = lambda p: Fraction(p + 1, 3)

    direct = averaged_alladi(limit, t, cutoff, weight, primes)
    rooted = rooted_alladi(limit, t, cutoff, weight, primes)
    jump = jump_alladi(limit, t, cutoff, weight, primes)

    assert direct == rooted == jump
    verify_prime_jump(limit, t, cutoff, primes)
    verify_summation_by_parts(limit, t, cutoff, weight, primes)
    verify_endpoints(limit, cutoff, weight, primes)

    print("prime-rooted Alladi/rough-phase exact regression passed")


if __name__ == "__main__":
    main()
