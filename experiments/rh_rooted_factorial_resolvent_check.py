#!/usr/bin/env python3
"""Exact finite checker for factorial suppression in the rooted resolvent.

The checker verifies that strict prime-label ordering gives

    ||K^r||_infinity <= Lambda^r / r!

on a finite state system, and that the exact Neumann remainder for an
arbitrary rational source is bounded by the corresponding factorial tail.
All arithmetic is exact Fraction arithmetic.  This is an algebraic
regression certificate, not an asymptotic theorem or an RH proof.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial
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


def apply_operator(
    field: Field,
    states: List[State],
    primes: List[int],
) -> Field:
    result: Field = {}
    for population, cutoff in states:
        total = Fraction(0)
        for root in primes:
            if root <= cutoff or root > population:
                continue
            child = population // root
            total += Fraction(child, population) * field[(child, root)]
        result[(population, cutoff)] = total
    return result


def sup_norm(field: Field) -> Fraction:
    return max(abs(value) for value in field.values())


def verify_factorial_power_bound(limit: int) -> None:
    primes = primes_up_to(limit)
    states = [
        (population, cutoff)
        for population in range(1, limit + 1)
        for cutoff in range(1, limit + 1)
    ]
    harmonic_mass = sum(Fraction(1, prime) for prime in primes)

    current: Field = {state: Fraction(1) for state in states}
    became_zero = False
    for power in range(1, limit + 1):
        current = apply_operator(current, states, primes)
        bound = harmonic_mass**power / factorial(power)
        assert sup_norm(current) <= bound
        if all(value == 0 for value in current.values()):
            became_zero = True
            break

    assert became_zero


def verify_factorial_neumann_tail(limit: int, t: Fraction) -> None:
    primes = primes_up_to(limit)
    states = [
        (population, cutoff)
        for population in range(1, limit + 1)
        for cutoff in range(1, limit + 1)
    ]
    harmonic_mass = sum(Fraction(1, prime) for prime in primes)

    source: Field = {
        state: Fraction(
            ((7 * state[0] + 11 * state[1]) % 23) - 11,
            13,
        )
        for state in states
    }
    source_norm = sup_norm(source)

    powers: List[Field] = [source]
    while True:
        next_power = apply_operator(powers[-1], states, primes)
        powers.append(next_power)
        if all(value == 0 for value in next_power.values()):
            break
        assert len(powers) <= limit + 1

    full: Field = {state: Fraction(0) for state in states}
    coefficient = -t
    for power in powers[:-1]:
        for state in states:
            full[state] += coefficient * power[state]
        coefficient *= -t

    for truncation in range(len(powers) - 1):
        partial: Field = {state: Fraction(0) for state in states}
        coefficient = -t
        for power in powers[: truncation + 1]:
            for state in states:
                partial[state] += coefficient * power[state]
            coefficient *= -t

        exact_remainder = sup_norm(
            {state: full[state] - partial[state] for state in states}
        )
        factorial_tail = (
            abs(t)
            * source_norm
            * sum(
                (abs(t) * harmonic_mass) ** power / factorial(power)
                for power in range(truncation + 1, len(powers) - 1)
            )
        )
        assert exact_remainder <= factorial_tail


def main() -> None:
    limit = 42
    verify_factorial_power_bound(limit)
    verify_factorial_neumann_tail(limit, Fraction(2, 5))
    print("rooted factorial resolvent exact regression passed")


if __name__ == "__main__":
    main()
