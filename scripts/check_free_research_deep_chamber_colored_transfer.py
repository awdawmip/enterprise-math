#!/usr/bin/env python3
"""Exact finite checks for the colored deepest degree-three transfer.

A deepest triple has exactly two labels above the current cutoff. The unique
uncut coordinate is retained as a color, while the arithmetic product endpoint
lies strictly below the cutoff. Calculations use integers and ``Fraction``.
"""

from __future__ import annotations

from bisect import bisect_right
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from typing import DefaultDict, Iterator


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


@lru_cache(maxsize=None)
def prime_power_base(n: int) -> int | None:
    """Return the unique prime base when ``n`` is a positive prime power."""
    if n < 2:
        return None
    remaining = n
    base: int | None = None
    d = 2
    while d * d <= remaining:
        if remaining % d == 0:
            if not is_prime(d):
                return None
            if base is not None and base != d:
                return None
            base = d
            while remaining % d == 0:
                remaining //= d
        d += 1
    if remaining > 1:
        if base is not None and base != remaining:
            return None
        base = remaining
    return base


def prime_powers(limit: int) -> list[int]:
    return [n for n in range(2, limit + 1) if prime_power_base(n) is not None]


def weight(a: int) -> Fraction:
    p = prime_power_base(a)
    assert p is not None
    return Fraction(p, a)


def unique_uncut_color(labels: tuple[int, int, int], cutoff: int) -> int | None:
    uncut = [index for index, value in enumerate(labels) if value <= cutoff]
    overcut = [index for index, value in enumerate(labels) if value > cutoff]
    if len(uncut) == 1 and len(overcut) == 2:
        return uncut[0]
    return None


def deepest_triples(cutoff: int) -> Iterator[tuple[tuple[int, int, int], int]]:
    """Generate only deepest triples; avoid a cubic scan of the ambient box."""
    budget = cutoff**3
    low = prime_powers(cutoff)
    all_actions = prime_powers(budget)
    high = [value for value in all_actions if value > cutoff]
    if not high:
        return

    for color in range(3):
        for uncut in low:
            pair_budget = budget // uncut
            for first_over in high:
                if first_over * high[0] > pair_budget:
                    break
                stop = bisect_right(high, pair_budget // first_over)
                for second_over in high[:stop]:
                    labels = [0, 0, 0]
                    over_positions = [index for index in range(3) if index != color]
                    labels[color] = uncut
                    labels[over_positions[0]] = first_over
                    labels[over_positions[1]] = second_over
                    triple = tuple(labels)
                    assert unique_uncut_color(triple, cutoff) == color
                    yield triple, color


def permute_tuple(labels: tuple[int, int, int], sigma: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(labels[sigma[index]] for index in range(3))


def inverse_permutation(sigma: tuple[int, int, int]) -> tuple[int, int, int]:
    out = [0, 0, 0]
    for index, value in enumerate(sigma):
        out[value] = index
    return tuple(out)


def check_colored_endpoint_support(max_cutoff: int = 14) -> None:
    for y in range(2, max_cutoff + 1):
        colored: DefaultDict[tuple[int, int], Fraction] = defaultdict(Fraction)
        scalar: DefaultDict[int, Fraction] = defaultdict(Fraction)
        component_mass = [Fraction(0, 1) for _ in range(3)]

        for labels, color in deepest_triples(y):
            product_label = labels[0] * labels[1] * labels[2]
            endpoint = y**3 // product_label
            assert 0 <= endpoint < y
            mass = weight(labels[0]) * weight(labels[1]) * weight(labels[2])
            colored[color, endpoint] += mass
            scalar[endpoint] += mass
            component_mass[color] += mass

        # Coordinate symmetry is fiberwise: at each arithmetic endpoint the
        # three color masses agree exactly, not merely after summing over m.
        for endpoint, mass in scalar.items():
            assert colored[0, endpoint] == colored[1, endpoint] == colored[2, endpoint]
            assert mass == 3 * colored[0, endpoint]

        assert component_mass[0] == component_mass[1] == component_mass[2]
        assert sum(component_mass, Fraction(0, 1)) == sum(scalar.values(), Fraction(0, 1))


def check_s3_covariance(max_cutoff: int = 10) -> None:
    sigmas = list(permutations(range(3)))
    for y in range(2, max_cutoff + 1):
        deepest = list(deepest_triples(y))
        for labels, color in deepest[: min(600, len(deepest))]:
            endpoint = y**3 // (labels[0] * labels[1] * labels[2])
            for sigma in sigmas:
                moved = permute_tuple(labels, sigma)
                moved_color = unique_uncut_color(moved, y)
                assert moved_color is not None
                expected_color = inverse_permutation(sigma)[color]
                assert moved_color == expected_color
                assert y**3 // (moved[0] * moved[1] * moved[2]) == endpoint


def check_scalar_color_information_loss() -> None:
    endpoint = 7
    colored_states = [(color, endpoint) for color in range(3)]
    standard_observable = {0: Fraction(1), 1: Fraction(-1), 2: Fraction(0)}
    assert len({state[1] for state in colored_states}) == 1
    assert len({standard_observable[state[0]] for state in colored_states}) == 3
    assert sum((standard_observable[color] for color in range(3)), Fraction(0, 1)) == 0


def check_standard_scalarization_zero(max_cutoff: int = 14) -> None:
    standard_vectors = [
        (Fraction(1), Fraction(-1), Fraction(0)),
        (Fraction(1), Fraction(1), Fraction(-2)),
        (Fraction(3, 5), Fraction(-7, 11), Fraction(2, 55)),
    ]
    assert all(sum(vector, Fraction(0, 1)) == 0 for vector in standard_vectors)

    for y in range(2, max_cutoff + 1):
        colored: DefaultDict[tuple[int, int], Fraction] = defaultdict(Fraction)
        for labels, color in deepest_triples(y):
            product_label = labels[0] * labels[1] * labels[2]
            endpoint = y**3 // product_label
            colored[color, endpoint] += weight(labels[0]) * weight(labels[1]) * weight(labels[2])

        endpoints = {endpoint for _, endpoint in colored}
        for endpoint in endpoints:
            for vector in standard_vectors:
                scalarized = sum(
                    (colored[color, endpoint] * vector[color] for color in range(3)),
                    Fraction(0, 1),
                )
                assert scalarized == 0


def check_deep_kernel_is_lower_scale(max_cutoff: int = 16) -> None:
    for y in range(2, max_cutoff + 1):
        kernel: DefaultDict[tuple[int, int], Fraction] = defaultdict(Fraction)
        for labels, color in deepest_triples(y):
            product_label = labels[0] * labels[1] * labels[2]
            endpoint = y**3 // product_label
            kernel[color, endpoint] += weight(labels[0]) * weight(labels[1]) * weight(labels[2])
        assert all(endpoint < y for _, endpoint in kernel)


def main() -> None:
    check_colored_endpoint_support()
    check_s3_covariance()
    check_scalar_color_information_loss()
    check_standard_scalarization_zero()
    check_deep_kernel_is_lower_scale()
    print("deepest colored chamber transfer checks: PASS")


if __name__ == "__main__":
    main()
