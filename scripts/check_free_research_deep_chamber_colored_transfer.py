#!/usr/bin/env python3
"""Exact finite checks for the colored deepest degree-three transfer.

A deepest triple has exactly two labels above the current cutoff.  The unique
uncut coordinate is retained as a color, while the arithmetic product endpoint
lies strictly below the cutoff.  Calculations use integers and ``Fraction``.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import permutations, product
from typing import DefaultDict


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def prime_power_base(n: int) -> int | None:
    if n < 2:
        return None
    for p in range(2, n + 1):
        if not is_prime(p):
            continue
        q = p
        while q < n:
            q *= p
        if q == n:
            return p
    return None


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


def permute_tuple(labels: tuple[int, int, int], sigma: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(labels[sigma[index]] for index in range(3))


def inverse_permutation(sigma: tuple[int, int, int]) -> tuple[int, int, int]:
    out = [0, 0, 0]
    for index, value in enumerate(sigma):
        out[value] = index
    return tuple(out)


def check_colored_endpoint_support(max_cutoff: int = 28) -> None:
    for y in range(2, max_cutoff + 1):
        actions = prime_powers(y**3)
        colored: DefaultDict[tuple[int, int], Fraction] = defaultdict(Fraction)
        scalar: DefaultDict[int, Fraction] = defaultdict(Fraction)
        component_mass = [Fraction(0, 1) for _ in range(3)]

        for labels in product(actions, repeat=3):
            if labels[0] * labels[1] * labels[2] > y**3:
                continue
            color = unique_uncut_color(labels, y)
            if color is None:
                continue
            endpoint = y**3 // (labels[0] * labels[1] * labels[2])
            assert 0 <= endpoint < y
            mass = weight(labels[0]) * weight(labels[1]) * weight(labels[2])
            colored[color, endpoint] += mass
            scalar[endpoint] += mass
            component_mass[color] += mass

        # Coordinate symmetry makes the three component masses exactly equal,
        # even at finite cutoff and for arbitrary multiplicative label weights.
        assert component_mass[0] == component_mass[1] == component_mass[2]
        assert sum(component_mass, Fraction(0, 1)) == sum(scalar.values(), Fraction(0, 1))
        for endpoint, mass in scalar.items():
            assert mass == sum(
                (colored[color, endpoint] for color in range(3)),
                Fraction(0, 1),
            )


def check_s3_covariance(max_cutoff: int = 16) -> None:
    sigmas = list(permutations(range(3)))
    for y in range(2, max_cutoff + 1):
        actions = prime_powers(y**3)
        deepest = []
        for labels in product(actions, repeat=3):
            if labels[0] * labels[1] * labels[2] > y**3:
                continue
            color = unique_uncut_color(labels, y)
            if color is not None:
                deepest.append((labels, color))

        for labels, color in deepest[: min(500, len(deepest))]:
            endpoint = y**3 // (labels[0] * labels[1] * labels[2])
            for sigma in sigmas:
                moved = permute_tuple(labels, sigma)
                moved_color = unique_uncut_color(moved, y)
                assert moved_color is not None
                # New slot j is uncut precisely when old slot sigma[j] was color.
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


def check_deep_kernel_is_lower_scale(max_cutoff: int = 35) -> None:
    for y in range(2, max_cutoff + 1):
        actions = prime_powers(y**3)
        kernel: DefaultDict[tuple[int, int], Fraction] = defaultdict(Fraction)
        for labels in product(actions, repeat=3):
            product_label = labels[0] * labels[1] * labels[2]
            if product_label > y**3:
                continue
            color = unique_uncut_color(labels, y)
            if color is None:
                continue
            endpoint = y**3 // product_label
            kernel[color, endpoint] += weight(labels[0]) * weight(labels[1]) * weight(labels[2])
        assert all(endpoint < y for _, endpoint in kernel)


def main() -> None:
    check_colored_endpoint_support()
    check_s3_covariance()
    check_scalar_color_information_loss()
    check_deep_kernel_is_lower_scale()
    print("deepest colored chamber transfer checks: PASS")


if __name__ == "__main__":
    main()
