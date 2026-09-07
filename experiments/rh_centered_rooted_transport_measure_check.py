#!/usr/bin/env python3
"""Exact finite checker for the centered prime-rooted transport measure.

The checker verifies the discrete part of
RH_CENTERED_ROOTED_CUTOFF_TRANSPORT_20260907.md:

1. normalized cutoff jumps equal the prime-rooted factor-cone masses;
2. the root measure at t=0 is the prime-incidence measure;
3. the root measure at t=1 is the largest-prime/smooth-number measure;
4. its t^r coefficient equals the exact rooted r-face count;
5. Stieltjes summation by parts recovers every weighted source from the
   cumulative signed transport function.

All arithmetic is exact Fraction arithmetic.  A synthetic rational reference
measure is used in item 5 because the continuum Dickman density is not an
exact rational object.  The identity is measure-theoretic and independent of
that choice.  This is a regression certificate, not an asymptotic theorem or
an RH proof.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import combinations
from math import comb
from typing import Callable, Dict, List


def primes_up_to(limit: int) -> List[int]:
    sieve = [True] * (limit + 1)
    if limit >= 0:
        sieve[0] = False
    if limit >= 1:
        sieve[1] = False
    for prime in range(2, int(limit**0.5) + 1):
        if sieve[prime]:
            for multiple in range(prime * prime, limit + 1, prime):
                sieve[multiple] = False
    return [value for value, flag in enumerate(sieve) if flag]


def distinct_prime_factors(integer: int, primes: List[int]) -> List[int]:
    factors: List[int] = []
    residue = integer
    for prime in primes:
        if prime * prime > residue:
            break
        if residue % prime:
            continue
        factors.append(prime)
        while residue % prime == 0:
            residue //= prime
    if residue > 1:
        factors.append(residue)
    return factors


def rough_depth(integer: int, cutoff: int, primes: List[int]) -> int:
    return sum(
        prime > cutoff
        for prime in distinct_prime_factors(integer, primes)
    )


def cutoff_phase(
    limit: int, cutoff: int, t: Fraction, primes: List[int]
) -> Fraction:
    return sum(
        (1 - t) ** rough_depth(integer, cutoff, primes)
        for integer in range(1, limit + 1)
    ) / limit


def rooted_mass(
    limit: int, root: int, t: Fraction, primes: List[int]
) -> Fraction:
    residual = limit // root
    return Fraction(residual, limit) * cutoff_phase(
        residual, root, t, primes
    )


def verify_jump_law(
    limit: int, cutoff: int, t: Fraction, primes: List[int]
) -> Dict[int, Fraction]:
    masses: Dict[int, Fraction] = {}
    for root in primes:
        if root > cutoff:
            break
        jump = (
            cutoff_phase(limit, root, t, primes)
            - cutoff_phase(limit, root - 1, t, primes)
        )
        mass = rooted_mass(limit, root, t, primes)
        assert jump == t * mass
        masses[root] = mass
    return masses


def verify_endpoints(limit: int, cutoff: int, primes: List[int]) -> None:
    active_roots = [prime for prime in primes if prime <= cutoff]

    incidence_mass = sum(
        rooted_mass(limit, root, Fraction(0), primes)
        for root in active_roots
    )
    assert incidence_mass == sum(
        Fraction(limit // root, limit) for root in active_roots
    )

    largest_prime_mass = sum(
        rooted_mass(limit, root, Fraction(1), primes)
        for root in active_roots
    )
    smooth_nonunit_count = 0
    for integer in range(2, limit + 1):
        factors = distinct_prime_factors(integer, primes)
        if factors[-1] <= cutoff:
            smooth_nonunit_count += 1
    assert largest_prime_mass == Fraction(smooth_nonunit_count, limit)


def verify_rooted_face_coefficients(
    limit: int, cutoff: int, primes: List[int], max_order: int = 4
) -> None:
    for root in primes:
        if root > cutoff:
            break
        residual = limit // root
        larger_primes = [
            prime
            for prime in primes
            if prime > root and root * prime <= limit
        ]

        for order in range(max_order + 1):
            population_coefficient = Fraction(
                sum(
                    comb(rough_depth(integer, root, primes), order)
                    for integer in range(1, residual + 1)
                ),
                limit,
            )

            rooted_face_count = Fraction(0)
            for arms in combinations(larger_primes, order):
                product = root
                for prime in arms:
                    product *= prime
                rooted_face_count += Fraction(limit // product, limit)

            assert population_coefficient == rooted_face_count


def verify_stieltjes_summation_by_parts(
    limit: int,
    cutoff: int,
    t: Fraction,
    primes: List[int],
    weight: Callable[[int], Fraction],
) -> None:
    active_roots = [prime for prime in primes if prime <= cutoff]
    discrete = {
        root: rooted_mass(limit, root, t, primes)
        for root in active_roots
    }

    # Any finite signed reference measure is admissible for the algebraic
    # identity.  This deterministic rational one plays the role of a toy
    # continuum carrier.
    reference = {
        root: Fraction((root % 5) + 1, root * (root + 1))
        for root in active_roots
    }
    signed = {
        root: discrete[root] - reference[root] for root in active_roots
    }

    direct = -sum(weight(root) * signed[root] for root in active_roots)

    cumulative: Dict[int, Fraction] = {}
    running = Fraction(0)
    for root in active_roots:
        running += signed[root]
        cumulative[root] = running

    by_parts = -weight(active_roots[-1]) * cumulative[active_roots[-1]]
    for index in range(len(active_roots) - 1):
        left = active_roots[index]
        right = active_roots[index + 1]
        by_parts += (
            weight(right) - weight(left)
        ) * cumulative[left]

    assert direct == by_parts


def main() -> None:
    limit = 84
    cutoff = 11
    t = Fraction(2, 5)
    primes = primes_up_to(limit)

    verify_jump_law(limit, cutoff, t, primes)
    verify_endpoints(limit, cutoff, primes)
    verify_rooted_face_coefficients(limit, cutoff, primes)
    verify_stieltjes_summation_by_parts(
        limit,
        cutoff,
        t,
        primes,
        weight=lambda prime: Fraction(prime * prime + 1, 7),
    )

    print("centered prime-rooted transport exact regression passed")


if __name__ == "__main__":
    main()
