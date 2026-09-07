#!/usr/bin/env python3
"""Exact regression for the harmonic rough-state/Duhamel bridge.

This checker validates four finite identities/inequalities used by
RH_HARMONIC_ROUGH_TRANSFER_DUHAMEL_REPAIR_20260907.md:

1. the original floor-weighted rough Duhamel coupling equals
   the harmonic quotient-cell pairing plus an explicit floor repair;
2. the harmonic cell pairing equals its discrete Abel form;
3. unweighted and harmonic rough cumulative states are related by exact
   partial summation and inverse differencing;
4. the finite-measure convolution discrepancy and repeated-label repair
   bounds used in the continuum transfer proof hold on exact rational toys.

The checker is a regression certificate for the algebra only. It is not an
asymptotic proof and is not evidence for the Riemann hypothesis.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import combinations
from math import factorial
from typing import Dict, Iterable, List, Tuple

Measure = Dict[int, Fraction]
Atom = Tuple[int, Fraction]


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
    return [value for value, is_prime in enumerate(sieve) if is_prime]


def mobius_omega_pminus(integer: int, primes: Iterable[int]) -> Tuple[int, int, int]:
    """Return (mu(n), omega(n), least-prime-factor), with p^-(1)=infinity."""
    if integer == 1:
        return 1, 0, 10**18

    residue = integer
    mobius = 1
    omega = 0
    least = 10**18

    for prime in primes:
        if prime * prime > residue:
            break
        if residue % prime:
            continue
        least = min(least, prime)
        exponent = 0
        while residue % prime == 0:
            residue //= prime
            exponent += 1
        if exponent >= 2:
            return 0, omega + 1, least
        mobius = -mobius
        omega += 1

    if residue > 1:
        least = min(least, residue)
        mobius = -mobius
        omega += 1

    return mobius, omega, least


def rough_weights(limit: int, cutoff: int, t: Fraction) -> List[Fraction]:
    primes = primes_up_to(limit)
    weights = [Fraction(0)] * (limit + 1)
    weights[1] = Fraction(1)
    for integer in range(2, limit + 1):
        mobius, omega, least = mobius_omega_pminus(integer, primes)
        if mobius and least > cutoff:
            weights[integer] = mobius * t**omega
    return weights


def verify_harmonic_cell_bridge() -> None:
    limit = 30
    cutoff = 3
    t = Fraction(2, 5)
    weights = rough_weights(limit, cutoff, t)

    # Deliberately nonmultiplicative suffix data: the identity must not depend
    # on any special arithmetic property of the response sequence.
    suffix = [Fraction(0)] + [
        Fraction(((n * n + 3 * n + 1) % 17) - 8, 7)
        for n in range(1, limit + 1)
    ]

    averages = [Fraction(0)] * (limit + 1)
    running = Fraction(0)
    for index in range(1, limit + 1):
        running += suffix[index]
        averages[index] = running / index

    root_average = averages[limit]
    centered = [Fraction(0)] + [
        averages[index] - root_average for index in range(1, limit + 1)
    ]

    harmonic = [Fraction(0)] * (limit + 1)
    running_harmonic = Fraction(0)
    for value in range(1, limit + 1):
        running_harmonic += weights[value] / value
        harmonic[value] = running_harmonic

    original = Fraction(0)
    floor_repair = Fraction(0)
    for divisor in range(1, limit + 1):
        quotient = limit // divisor
        response = centered[quotient]
        original += weights[divisor] * Fraction(quotient, limit) * response
        floor_repair += (
            weights[divisor]
            * (Fraction(quotient, limit) - Fraction(1, divisor))
            * response
        )

    harmonic_cells = Fraction(0)
    for quotient in range(1, limit + 1):
        upper = harmonic[limit // quotient]
        lower = harmonic[limit // (quotient + 1)]
        harmonic_cells += (upper - lower) * centered[quotient]

    harmonic_abel = (harmonic[limit] - 1) * centered[1]
    for quotient in range(2, limit + 1):
        harmonic_abel += (
            harmonic[limit // quotient] - 1
        ) * (centered[quotient] - centered[quotient - 1])

    assert original == harmonic_cells + floor_repair
    assert harmonic_cells == harmonic_abel


def verify_unweighted_harmonic_inversion() -> None:
    limit = 80
    cutoff = 5
    t = Fraction(-3, 7)
    weights = rough_weights(limit, cutoff, t)

    unweighted = [Fraction(0)] * (limit + 1)
    harmonic = [Fraction(0)] * (limit + 1)
    running_unweighted = Fraction(0)
    running_harmonic = Fraction(0)

    for value in range(1, limit + 1):
        running_unweighted += weights[value]
        running_harmonic += weights[value] / value
        unweighted[value] = running_unweighted
        harmonic[value] = running_harmonic

    for endpoint in range(1, limit + 1):
        partial_summation = (
            unweighted[endpoint] / endpoint
            + sum(
                unweighted[value] / (value * (value + 1))
                for value in range(1, endpoint)
            )
        )
        inverse_difference = (
            endpoint * harmonic[endpoint]
            - sum(harmonic[value] for value in range(1, endpoint))
        )
        assert harmonic[endpoint] == partial_summation
        assert unweighted[endpoint] == inverse_difference


def convolve(left: Measure, right: Measure, cutoff: int) -> Measure:
    result: Dict[int, Fraction] = defaultdict(Fraction)
    for left_position, left_weight in left.items():
        for right_position, right_weight in right.items():
            position = left_position + right_position
            if position <= cutoff:
                result[position] += left_weight * right_weight
    return dict(result)


def convolution_power(measure: Measure, power: int, cutoff: int) -> Measure:
    result: Measure = {0: Fraction(1)}
    for _ in range(power):
        result = convolve(result, measure, cutoff)
    return result


def cumulative_mass(measure: Measure, cutoff: int) -> Fraction:
    return sum(
        weight for position, weight in measure.items() if position <= cutoff
    )


def verify_measure_discrepancy_bound() -> None:
    cutoff = 5
    alpha: Measure = {
        1: Fraction(2, 5),
        2: Fraction(1, 3),
        4: Fraction(1, 7),
    }
    beta: Measure = {
        1: Fraction(1, 3),
        3: Fraction(2, 5),
        4: Fraction(1, 8),
    }

    discrepancy = max(
        abs(
            cumulative_mass(alpha, threshold)
            - cumulative_mass(beta, threshold)
        )
        for threshold in range(cutoff + 1)
    )
    mass_bound = max(sum(alpha.values()), sum(beta.values()))

    for power in range(1, cutoff + 1):
        alpha_mass = cumulative_mass(
            convolution_power(alpha, power, cutoff), cutoff
        )
        beta_mass = cumulative_mass(
            convolution_power(beta, power, cutoff), cutoff
        )
        left = abs(alpha_mass - beta_mass) / factorial(power)
        right = (
            2
            * discrepancy
            * mass_bound ** (power - 1)
            / factorial(power - 1)
        )
        assert left <= right


def distinct_partition(atoms: List[Atom], cutoff: int, t: Fraction) -> Fraction:
    total = Fraction(1)
    for cardinality in range(1, len(atoms) + 1):
        for indices in combinations(range(len(atoms)), cardinality):
            if sum(atoms[index][0] for index in indices) > cutoff:
                continue
            weight = Fraction(1)
            for index in indices:
                weight *= atoms[index][1]
            total += (-t) ** cardinality * weight
    return total


def poissonized_partition(
    atoms: List[Atom], cutoff: int, t: Fraction
) -> Fraction:
    atomic_measure: Dict[int, Fraction] = defaultdict(Fraction)
    for position, weight in atoms:
        atomic_measure[position] += weight

    total = Fraction(1)
    current: Measure = {0: Fraction(1)}
    for cardinality in range(1, cutoff + 1):
        current = convolve(current, dict(atomic_measure), cutoff)
        total += (
            (-t) ** cardinality
            * cumulative_mass(current, cutoff)
            / factorial(cardinality)
        )
    return total


def verify_repeated_label_repair_bound() -> None:
    cutoff = 5
    t = Fraction(2, 5)
    atoms: List[Atom] = [
        (1, Fraction(1, 3)),
        (1, Fraction(1, 5)),
        (2, Fraction(1, 7)),
        (3, Fraction(1, 11)),
    ]

    distinct = distinct_partition(atoms, cutoff, t)
    poissonized = poissonized_partition(atoms, cutoff, t)

    total_mass = sum(weight for _, weight in atoms)
    diagonal_mass = sum(weight * weight for _, weight in atoms)
    collision_bound = sum(
        Fraction(cardinality * (cardinality - 1), 2)
        * diagonal_mass
        * total_mass ** (cardinality - 2)
        * abs(t) ** cardinality
        / factorial(cardinality)
        for cardinality in range(2, cutoff + 1)
    )

    assert abs(distinct - poissonized) <= collision_bound


def main() -> None:
    verify_harmonic_cell_bridge()
    verify_unweighted_harmonic_inversion()
    verify_measure_discrepancy_bound()
    verify_repeated_label_repair_bound()
    print("harmonic rough-state/Duhamel bridge exact regression passed")


if __name__ == "__main__":
    main()
