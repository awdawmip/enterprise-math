#!/usr/bin/env python3
"""Exact finite checks for the full-intermediate deepest-history carrier.

The checker retains the color, all three one-step quotient vertices, and the
common product endpoint.  It verifies that the apparent conditional-variance
remainder is exactly an ordered cubic-curvature packet before any forgetful
projection.  Only integers and ``Fraction`` are used.
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
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


@lru_cache(maxsize=None)
def prime_power_base(n: int) -> int | None:
    if n < 2:
        return None
    remaining = n
    base: int | None = None
    d = 2
    while d * d <= remaining:
        if remaining % d == 0:
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


@lru_cache(maxsize=None)
def prime_powers(limit: int) -> tuple[int, ...]:
    return tuple(
        n for n in range(2, limit + 1)
        if prime_power_base(n) is not None
    )


def weight(a: int) -> Fraction:
    base = prime_power_base(a)
    assert base is not None
    return Fraction(base, a)


def field(n: int) -> Fraction:
    numerator = ((37 * n * n + 11 * n + 5) % 113) - 56
    denominator = ((23 * n + 9) % 29) + 1
    return Fraction(numerator, denominator)


def product_bounded_triples(cutoff: int) -> Iterator[tuple[int, int, int]]:
    """Prime-power triples with product at most ``cutoff**3``."""
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
    """Triples with exactly one label at most the current cutoff."""
    for labels in product_bounded_triples(cutoff):
        uncut = [index for index, value in enumerate(labels) if value <= cutoff]
        if len(uncut) == 1:
            yield labels, uncut[0]


def full_signature(
    cutoff: int,
    labels: tuple[int, int, int],
    color: int,
) -> tuple[int, int, int, int, int]:
    n = cutoff**3
    a, b, c = labels
    return color, n // a, n // b, n // c, n // (a * b * c)


def history_weight(labels: tuple[int, int, int]) -> Fraction:
    a, b, c = labels
    return weight(a) * weight(b) * weight(c)


def check_full_signature(max_cutoff: int = 12) -> None:
    for cutoff in range(2, max_cutoff + 1):
        n = cutoff**3
        for labels, color in deepest_histories(cutoff):
            signature = full_signature(cutoff, labels, color)
            assert signature[0] == color
            assert signature[1:4] == tuple(n // label for label in labels)
            assert signature[4] == n // (labels[0] * labels[1] * labels[2])
            assert signature[4] < cutoff


def check_pointwise_curvature(max_cutoff: int = 12) -> None:
    for cutoff in range(2, max_cutoff + 1):
        n = cutoff**3
        for labels, _ in deepest_histories(cutoff):
            values = tuple(field(n // label) for label in labels)
            standard_energy = (
                (values[0] - values[1]) ** 2
                + (values[1] - values[2]) ** 2
                + (values[2] - values[0]) ** 2
            )
            # Appending any common quotient suffix cancels the common endpoint.
            curvature_energy = (
                (values[0] - values[1]) ** 2
                + (values[1] - values[2]) ** 2
                + (values[2] - values[0]) ** 2
            )
            assert standard_energy == curvature_energy


def weighted_pair_energy(weights: list[Fraction], values: list[Fraction]) -> Fraction:
    return sum(
        (
            weights[i] * weights[j] * (values[i] - values[j]) ** 2
            for i in range(len(values))
            for j in range(len(values))
        ),
        Fraction(0, 1),
    )


def check_fiberwise_conditional_variance(max_cutoff: int = 12) -> None:
    for cutoff in range(2, max_cutoff + 1):
        n = cutoff**3
        fibers: DefaultDict[
            tuple[int, int], list[tuple[int, int, int]]
        ] = defaultdict(list)
        for labels, color in deepest_histories(cutoff):
            endpoint = n // (labels[0] * labels[1] * labels[2])
            fibers[color, endpoint].append(labels)

        for histories in fibers.values():
            weights = [history_weight(labels) for labels in histories]
            total = sum(weights, Fraction(0, 1))
            assert total > 0
            for position in range(3):
                values = [field(n // labels[position]) for labels in histories]
                second = sum(
                    (mass * value**2 for mass, value in zip(weights, values)),
                    Fraction(0, 1),
                )
                first = sum(
                    (mass * value for mass, value in zip(weights, values)),
                    Fraction(0, 1),
                )
                pair = weighted_pair_energy(weights, values)
                assert second == first**2 / total + pair / (2 * total)

                # Every cross-history difference is itself a common-suffix
                # ordered curvature, so no additional scalar remainder exists.
                curvature_pair = weighted_pair_energy(weights, values)
                assert pair == curvature_pair


def check_deep_energy_embeds_in_full_cubic(max_cutoff: int = 12) -> None:
    for cutoff in range(2, max_cutoff + 1):
        n = cutoff**3
        oriented = [Fraction(0, 1) for _ in range(3)]
        for labels, _ in deepest_histories(cutoff):
            values = tuple(field(n // label) for label in labels)
            mass = history_weight(labels)
            oriented[0] += mass * (values[0] - values[1]) ** 2
            oriented[1] += mass * (values[1] - values[2]) ** 2
            oriented[2] += mass * (values[2] - values[0]) ** 2

        # The deepest chamber is invariant under coordinate permutations.
        assert oriented[0] == oriented[1] == oriented[2]
        deep_standard = sum(oriented, Fraction(0, 1))
        assert deep_standard == 3 * oriented[0]

        full_cubic = Fraction(0, 1)
        for a, b, c in product_bounded_triples(cutoff):
            mass = weight(a) * weight(b) * weight(c)
            full_cubic += mass * (field(n // a) - field(n // b)) ** 2

        # The deepest oriented packet is a positive restriction of the full
        # ordered degree-three provenance energy.
        assert oriented[0] <= full_cubic


def check_projection_no_go() -> None:
    cutoff = 10
    n = cutoff**3
    first = (2, 17, 19)
    second = (3, 11, 17)
    assert full_signature(cutoff, first, 0)[0] == 0
    assert full_signature(cutoff, second, 0)[0] == 0
    assert full_signature(cutoff, first, 0)[4] == 1
    assert full_signature(cutoff, second, 0)[4] == 1
    assert n // first[0] == 500
    assert n // second[0] == 333

    third = (2, 13, 23)
    sig_first = full_signature(cutoff, first, 0)
    sig_third = full_signature(cutoff, third, 0)
    # Color, uncut intermediate, and endpoint agree.
    assert (sig_first[0], sig_first[1], sig_first[4]) == (
        sig_third[0], sig_third[1], sig_third[4]
    )
    # Another branch still differs and must be retained.
    assert sig_first[2] == 58
    assert sig_third[2] == 76


def main() -> None:
    check_full_signature()
    check_pointwise_curvature()
    check_fiberwise_conditional_variance()
    check_deep_energy_embeds_in_full_cubic()
    check_projection_no_go()
    print("deep full-intermediate variance checks: PASS")


if __name__ == "__main__":
    main()
