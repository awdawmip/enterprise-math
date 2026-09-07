#!/usr/bin/env python3
"""Exact/finite regression for the adjoint rooted-resolvent observer.

The checker verifies:

1. the root functional applied after r Volterra steps equals the explicit
   increasing-prime path sum (exact rational arithmetic);
2. root-to-terminal edge telescoping is exact;
3. the weighted Cauchy factors used for f(p)=sqrt(p) satisfy their factorial
   majorants;
4. the finite nilpotent resolvent obeys the two-sided sup-norm bounds.

The finite calculations are regression certificates only. They are not
asymptotic proofs and are not evidence for the Riemann hypothesis.
"""

from __future__ import annotations

from fractions import Fraction
from math import factorial, log, sqrt
from typing import Callable

State = tuple[int, int]


def primes_up_to(limit: int) -> list[int]:
    sieve = bytearray(b"\x01") * (limit + 1)
    if limit >= 0:
        sieve[0] = 0
    if limit >= 1:
        sieve[1] = 0
    for prime in range(2, int(limit**0.5) + 1):
        if sieve[prime]:
            sieve[prime * prime : limit + 1 : prime] = b"\x00" * (
                (limit - prime * prime) // prime + 1
            )
    return [value for value in range(2, limit + 1) if sieve[value]]


def k_apply(
    field: Callable[[int, int], Fraction],
    population: int,
    cutoff: int,
    primes: list[int],
) -> Fraction:
    total = Fraction(0)
    for prime in primes:
        if prime <= cutoff:
            continue
        if prime > population:
            break
        child = population // prime
        total += Fraction(child, population) * field(child, prime)
    return total


def k_power_value(
    source: Callable[[int, int], Fraction],
    depth: int,
    population: int,
    cutoff: int,
    primes: list[int],
) -> Fraction:
    if depth == 0:
        return source(population, cutoff)
    return k_apply(
        lambda child_population, child_cutoff: k_power_value(
            source,
            depth - 1,
            child_population,
            child_cutoff,
            primes,
        ),
        population,
        cutoff,
        primes,
    )


def root_functional_operator(
    limit: int,
    root_cutoff: int,
    depth: int,
    root_weight: Callable[[int], Fraction],
    source: Callable[[int, int], Fraction],
    primes: list[int],
) -> Fraction:
    total = Fraction(0)
    for root in primes:
        if root > root_cutoff:
            break
        child = limit // root
        total += (
            root_weight(root)
            * Fraction(child, limit)
            * k_power_value(source, depth, child, root, primes)
        )
    return total


def explicit_path_sum(
    limit: int,
    root_cutoff: int,
    depth: int,
    root_weight: Callable[[int], Fraction],
    source: Callable[[int, int], Fraction],
    primes: list[int],
) -> Fraction:
    total = Fraction(0)

    for root_index, root in enumerate(primes):
        if root > root_cutoff:
            break

        def visit(
            start: int,
            remaining: int,
            path: list[int],
            product_value: int,
        ) -> None:
            nonlocal total
            if remaining == 0:
                terminal_population = limit // product_value
                terminal_prime = path[-1]
                total += (
                    root_weight(root)
                    * Fraction(terminal_population, limit)
                    * source(terminal_population, terminal_prime)
                )
                return

            for index in range(start, len(primes)):
                prime = primes[index]
                next_product = product_value * prime
                if next_product > limit:
                    break
                visit(
                    index + 1,
                    remaining - 1,
                    [*path, prime],
                    next_product,
                )

        visit(root_index + 1, depth, [root], root)

    return total


def explicit_edge_decomposition(
    limit: int,
    root_cutoff: int,
    depth: int,
    root_weight: Callable[[int], Fraction],
    source: Callable[[int, int], Fraction],
    primes: list[int],
) -> tuple[Fraction, Fraction]:
    original = Fraction(0)
    decomposed = Fraction(0)

    for root_index, root in enumerate(primes):
        if root > root_cutoff:
            break

        def visit(
            start: int,
            remaining: int,
            path: list[int],
            product_value: int,
        ) -> None:
            nonlocal original, decomposed
            if remaining == 0:
                terminal_population = limit // product_value
                terminal_prime = path[-1]
                common = (
                    Fraction(terminal_population, limit)
                    * source(terminal_population, terminal_prime)
                )
                original += root_weight(path[0]) * common
                terminal = root_weight(path[-1])
                edge_sum = sum(
                    root_weight(path[index + 1])
                    - root_weight(path[index])
                    for index in range(len(path) - 1)
                )
                decomposed += (terminal - edge_sum) * common
                return

            for index in range(start, len(primes)):
                prime = primes[index]
                next_product = product_value * prime
                if next_product > limit:
                    break
                visit(
                    index + 1,
                    remaining - 1,
                    [*path, prime],
                    next_product,
                )

        visit(root_index + 1, depth, [root], root)

    return original, decomposed


def path_weight_factors(
    limit: int,
    root_cutoff: int,
    depth: int,
    source: Callable[[int, int], Fraction],
    primes: list[int],
) -> tuple[float, Fraction, Fraction, Fraction]:
    """Return pairing, A=sum p0*m, B=sum m*Q^2, and total path mass."""
    pairing = 0.0
    first_factor = Fraction(0)
    second_factor = Fraction(0)
    path_mass = Fraction(0)

    for root_index, root in enumerate(primes):
        if root > root_cutoff:
            break

        def visit(
            start: int,
            remaining: int,
            product_value: int,
            terminal_prime: int,
        ) -> None:
            nonlocal pairing, first_factor, second_factor, path_mass
            if remaining == 0:
                terminal_population = limit // product_value
                mass = Fraction(terminal_population, limit)
                value = source(terminal_population, terminal_prime)
                pairing += sqrt(root) * float(mass * value)
                first_factor += root * mass
                second_factor += mass * value * value
                path_mass += mass
                return

            for index in range(start, len(primes)):
                prime = primes[index]
                next_product = product_value * prime
                if next_product > limit:
                    break
                visit(index + 1, remaining - 1, next_product, prime)

        visit(root_index + 1, depth, root, root)

    return pairing, first_factor, second_factor, path_mass


def verify_path_and_edge_identities() -> None:
    limit = 120
    root_cutoff = 13
    primes = primes_up_to(limit)

    def root_weight(prime: int) -> Fraction:
        return Fraction(2 * prime + 3, prime + 1)

    def source(population: int, cutoff: int) -> Fraction:
        return Fraction((3 * population + 5 * cutoff) % 19 - 9, 11)

    for depth in range(4):
        operator_value = root_functional_operator(
            limit, root_cutoff, depth, root_weight, source, primes
        )
        path_value = explicit_path_sum(
            limit, root_cutoff, depth, root_weight, source, primes
        )
        assert operator_value == path_value
        original, decomposed = explicit_edge_decomposition(
            limit, root_cutoff, depth, root_weight, source, primes
        )
        assert original == decomposed == path_value


def verify_weighted_cauchy_and_factorial_bounds() -> None:
    limit = 1_000
    root_cutoff = int(log(limit) ** 2)
    primes = primes_up_to(limit)
    harmonic = sum((Fraction(1, prime) for prime in primes), Fraction(0))
    root_count = sum(prime <= root_cutoff for prime in primes)

    def source(population: int, cutoff: int) -> Fraction:
        return Fraction((population + 2 * cutoff) % 13 - 6, 7)

    source_sup = max(
        abs(source(population, cutoff))
        for population in range(1, limit + 1)
        for cutoff in (2, 3, 5, 7, 11)
    )

    for depth in range(4):
        pairing, first, second, path_mass = path_weight_factors(
            limit, root_cutoff, depth, source, primes
        )
        assert pairing * pairing <= float(first * second) + 1e-12

        first_upper = (
            root_count * harmonic**depth / factorial(depth)
            if depth > 0
            else Fraction(root_count)
        )
        second_upper = (
            source_sup**2
            * harmonic ** (depth + 1)
            / factorial(depth + 1)
        )
        assert first <= first_upper
        assert second <= source_sup**2 * path_mass
        assert path_mass <= (
            harmonic ** (depth + 1) / factorial(depth + 1)
        )
        assert second <= second_upper


def verify_sup_resolvent_bounds() -> None:
    limit = 30
    primes = primes_up_to(limit)
    states = [
        (population, cutoff)
        for population in range(1, limit + 1)
        for cutoff in [1, *[p for p in primes if p <= population]]
    ]

    def source(population: int, cutoff: int) -> Fraction:
        return Fraction((7 * population + 3 * cutoff) % 23 - 11, 13)

    t = Fraction(2, 7)
    source_norm = max(abs(source(*state)) for state in states)
    current = {state: source(*state) for state in states}
    error = {state: Fraction(0) for state in states}

    max_depth = len(primes) + 1
    coefficient = -t
    for _ in range(max_depth + 1):
        for state in states:
            error[state] += coefficient * current[state]
        next_field = {}
        for population, cutoff in states:
            next_field[(population, cutoff)] = k_apply(
                lambda child_population, child_cutoff: current.get(
                    (child_population, child_cutoff), Fraction(0)
                ),
                population,
                cutoff,
                primes,
            )
        current = next_field
        coefficient *= -t

    error_norm = max(abs(value) for value in error.values())
    harmonic = sum((Fraction(1, prime) for prime in primes), Fraction(0))
    lower = abs(t) * source_norm / (1 + abs(t) * harmonic)
    exponential_upper = sum(
        (abs(t) * harmonic) ** degree / factorial(degree)
        for degree in range(max_depth + 10)
    )
    upper = abs(t) * exponential_upper * source_norm
    assert float(lower) <= float(error_norm) + 1e-12
    assert float(error_norm) <= float(upper) + 1e-12


def finite_table() -> None:
    print(
        "X        r  pairing         sqrt(A)         sqrt(B)         bound"
    )
    for limit in (10_000, 100_000, 1_000_000):
        root_cutoff = int(log(limit) ** 2)
        depth = max(1, round(0.5 * log(limit) / log(log(limit))))
        primes = primes_up_to(limit)

        def source(population: int, cutoff: int) -> Fraction:
            if population <= cutoff:
                return Fraction(0)
            return Fraction(1, 1 + cutoff)

        pairing, first, second, _ = path_weight_factors(
            limit, root_cutoff, depth, source, primes
        )
        bound = sqrt(float(first * second))
        print(
            f"{limit:<8d} {depth:<2d} {pairing: .10e}  "
            f"{sqrt(float(first)): .10e}  "
            f"{sqrt(float(second)): .10e}  {bound: .10e}"
        )
        assert abs(pairing) <= bound + 1e-12


def main() -> None:
    verify_path_and_edge_identities()
    verify_weighted_cauchy_and_factorial_bounds()
    verify_sup_resolvent_bounds()
    finite_table()
    print("adjoint rooted-resolvent edge/energy regression passed")


if __name__ == "__main__":
    main()
