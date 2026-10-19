#!/usr/bin/env python3
"""Exact checks for the strict high/low history-mean cascade.

A deepest triple at scale ``Y**3`` has one action at most ``Y``.  Its quotient
vertex is at least ``Y**2``; the other two quotient vertices are strictly below
``Y**2``.  The history-mean relation admits a sharp square-certified split
with high coefficient ``1/2`` and low coefficient ``2``.
"""

from __future__ import annotations

from bisect import bisect_right
from collections import defaultdict
from fractions import Fraction
from functools import lru_cache
from typing import DefaultDict, Iterator


@lru_cache(maxsize=None)
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


@lru_cache(maxsize=None)
def prime_power_base(n: int) -> int | None:
    if n < 2:
        return None
    remaining = n
    base: int | None = None
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            if base is not None and base != divisor:
                return None
            base = divisor
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        if base is not None and base != remaining:
            return None
        base = remaining
    return base


@lru_cache(maxsize=None)
def prime_powers(limit: int) -> tuple[int, ...]:
    return tuple(
        n for n in range(2, limit + 1)
        if prime_power_base(n) is not None
    )


def weight(action: int) -> Fraction:
    base = prime_power_base(action)
    assert base is not None
    return Fraction(base, action)


def product_bounded_triples(cutoff: int) -> Iterator[tuple[int, int, int]]:
    budget = cutoff**3
    actions = prime_powers(budget)
    if not actions:
        return
    least = actions[0]
    for a in actions:
        if a * least * least > budget:
            break
        for b in actions:
            if a * b * least > budget:
                break
            stop = bisect_right(actions, budget // (a * b))
            for c in actions[:stop]:
                yield a, b, c


def deepest_histories(cutoff: int) -> Iterator[tuple[tuple[int, int, int], int]]:
    for labels in product_bounded_triples(cutoff):
        uncut = [index for index, action in enumerate(labels) if action <= cutoff]
        if len(uncut) == 1:
            yield labels, uncut[0]


def mean3(values: tuple[Fraction, Fraction, Fraction]) -> Fraction:
    return sum(values, Fraction(0, 1)) / 3


def high_low_bound(
    high: Fraction,
    high_other: Fraction,
    low_one: Fraction,
    low_one_other: Fraction,
    low_two: Fraction,
    low_two_other: Fraction,
) -> tuple[Fraction, Fraction, Fraction]:
    dh = high - high_other
    d1 = low_one - low_one_other
    d2 = low_two - low_two_other
    lhs = 3 * ((dh + d1 + d2) / 3) ** 2
    rhs = Fraction(1, 2) * dh**2 + 2 * (d1**2 + d2**2)
    certificate = ((dh - 2 * (d1 + d2)) ** 2 + 6 * (d1 - d2) ** 2) / 6
    return lhs, rhs, certificate


def field(vertex: int) -> Fraction:
    numerator = ((43 * vertex * vertex + 17 * vertex + 11) % 131) - 65
    denominator = ((29 * vertex + 3) % 37) + 1
    return Fraction(numerator, denominator)


def ordered_high_low_values(
    cutoff: int, labels: tuple[int, int, int], color: int
) -> tuple[Fraction, Fraction, Fraction]:
    n = cutoff**3
    other = [index for index in range(3) if index != color]
    return (
        field(n // labels[color]),
        field(n // labels[other[0]]),
        field(n // labels[other[1]]),
    )


def check_square_certificate() -> None:
    samples = [
        (
            Fraction(7, 3), Fraction(-2, 5), Fraction(1, 7),
            Fraction(9, 4), Fraction(-3, 11), Fraction(8, 9),
        ),
        (
            Fraction(-5), Fraction(4), Fraction(2),
            Fraction(-1), Fraction(7), Fraction(3, 2),
        ),
    ]
    for sample in samples:
        lhs, rhs, certificate = high_low_bound(*sample)
        assert rhs - lhs == certificate
        assert certificate >= 0
        assert lhs <= rhs

    # Equality certificate: d1=d2=t and dh=4t.
    lhs, rhs, certificate = high_low_bound(
        Fraction(4), Fraction(0), Fraction(1), Fraction(0),
        Fraction(1), Fraction(0)
    )
    assert lhs == rhs
    assert certificate == 0


def check_scale_landing(max_cutoff: int = 16) -> None:
    for cutoff in range(2, max_cutoff + 1):
        n = cutoff**3
        for labels, color in deepest_histories(cutoff):
            high_vertex = n // labels[color]
            low_vertices = [
                n // labels[index]
                for index in range(3)
                if index != color
            ]
            endpoint = n // (labels[0] * labels[1] * labels[2])
            assert high_vertex >= cutoff**2
            assert all(vertex < cutoff**2 for vertex in low_vertices)
            assert endpoint < cutoff


def check_fiberwise_high_low_coercivity(max_cutoff: int = 12) -> None:
    for cutoff in range(2, max_cutoff + 1):
        n = cutoff**3
        fibers: DefaultDict[
            tuple[int, int], list[tuple[int, int, int]]
        ] = defaultdict(list)
        for labels, color in deepest_histories(cutoff):
            endpoint = n // (labels[0] * labels[1] * labels[2])
            fibers[color, endpoint].append(labels)

        for (color, _), histories in fibers.items():
            weighted_lhs = Fraction(0, 1)
            weighted_rhs = Fraction(0, 1)
            for first in histories:
                first_values = ordered_high_low_values(cutoff, first, color)
                first_weight = (
                    weight(first[0]) * weight(first[1]) * weight(first[2])
                )
                for second in histories:
                    second_values = ordered_high_low_values(cutoff, second, color)
                    second_weight = (
                        weight(second[0]) * weight(second[1]) * weight(second[2])
                    )
                    lhs, rhs, certificate = high_low_bound(
                        first_values[0], second_values[0],
                        first_values[1], second_values[1],
                        first_values[2], second_values[2],
                    )
                    assert rhs - lhs == certificate
                    assert lhs <= rhs
                    mass = first_weight * second_weight
                    weighted_lhs += mass * lhs
                    weighted_rhs += mass * rhs
            assert weighted_lhs <= weighted_rhs


def main() -> None:
    check_square_certificate()
    check_scale_landing()
    check_fiberwise_high_low_coercivity()
    print("deep high-low coercivity checks: PASS")


if __name__ == "__main__":
    main()
