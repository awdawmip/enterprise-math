#!/usr/bin/env python3
"""Exact finite regression for the prime-rooted Volterra/BRC resolvent.

The checker validates:

1. the exact discrete cutoff recursion
       Phi_N(y)=1-t*sum_{q>y} floor(N/q)/N * Phi_floor(N/q)(q);
2. strict population descent and nilpotence of the rooted-prime operator;
3. the exact finite Neumann/Duhamel resolvent
       E=-t(I+tK)^(-1)Q
   against direct triangular solution for arbitrary rational sources;
4. the elementary row-mass bound by the prime harmonic sum.

All arithmetic is exact Fraction arithmetic.  The source in item 3 is a
synthetic rational source because the analytic Dickman quadrature source is
not rational.  This is an algebraic regression certificate, not an
asymptotic theorem or an RH proof.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict, List, Tuple

State = Tuple[int, int]
Field = Dict[State, Fraction]


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


def phase(
    population: int, cutoff: int, t: Fraction, primes: List[int]
) -> Fraction:
    return sum(
        (1 - t) ** sum(
            prime > cutoff
            for prime in distinct_prime_factors(integer, primes)
        )
        for integer in range(1, population + 1)
    ) / population


def verify_discrete_volterra(limit: int, t: Fraction) -> None:
    primes = primes_up_to(limit)
    for population in range(1, limit + 1):
        for cutoff in range(1, population + 1):
            right = Fraction(1)
            for root in primes:
                if root <= cutoff or root > population:
                    continue
                child = population // root
                right -= (
                    t
                    * Fraction(child, population)
                    * phase(child, root, t, primes)
                )
            assert phase(population, cutoff, t, primes) == right


def apply_operator(
    field: Field,
    states: List[State],
    primes: List[int],
) -> Field:
    result: Field = {}
    for population, cutoff in states:
        value = Fraction(0)
        for root in primes:
            if root <= cutoff or root > population:
                continue
            child = population // root
            assert child < population
            value += Fraction(child, population) * field[(child, root)]
        result[(population, cutoff)] = value
    return result


def verify_resolvent(limit: int, t: Fraction) -> None:
    primes = primes_up_to(limit)
    states = [
        (population, cutoff)
        for population in range(1, limit + 1)
        for cutoff in range(1, limit + 1)
    ]

    source: Field = {
        state: Fraction(
            ((3 * state[0] + 5 * state[1]) % 17) - 8,
            11,
        )
        for state in states
    }

    # Direct triangular solution of E=-tQ-tKE.  Every child population is
    # strictly smaller, so values are available in increasing population
    # order.
    direct: Field = {}
    for population in range(1, limit + 1):
        for cutoff in range(limit, 0, -1):
            propagated = Fraction(0)
            for root in primes:
                if root <= cutoff or root > population:
                    continue
                child = population // root
                propagated += (
                    Fraction(child, population) * direct[(child, root)]
                )
            direct[(population, cutoff)] = (
                -t * source[(population, cutoff)] - t * propagated
            )

    # Exact finite Neumann series.  Nilpotence follows from strict population
    # descent and strictly increasing root labels along every path.
    series: Field = {state: Fraction(0) for state in states}
    current = source
    coefficient = -t
    became_zero = False
    for _ in range(limit + 1):
        for state in states:
            series[state] += coefficient * current[state]
        current = apply_operator(current, states, primes)
        coefficient *= -t
        if all(value == 0 for value in current.values()):
            became_zero = True
            break

    assert became_zero
    assert direct == series


def verify_row_mass_bound(limit: int) -> None:
    primes = primes_up_to(limit)
    for population in range(1, limit + 1):
        for cutoff in range(1, population + 1):
            row_mass = sum(
                Fraction(population // root, population)
                for root in primes
                if cutoff < root <= population
            )
            harmonic_bound = sum(
                Fraction(1, root)
                for root in primes
                if cutoff < root <= population
            )
            assert row_mass <= harmonic_bound


def main() -> None:
    limit = 42
    t = Fraction(2, 5)
    verify_discrete_volterra(limit, t)
    verify_resolvent(limit, t)
    verify_row_mass_bound(limit)
    print("prime-rooted Volterra/BRC exact regression passed")


if __name__ == "__main__":
    main()
