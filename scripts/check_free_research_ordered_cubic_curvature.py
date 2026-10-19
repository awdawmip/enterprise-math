#!/usr/bin/env python3
"""Exact finite checks for ordered quotient curvature and cubic polarization.

The checker uses integers and ``Fraction`` only.  Formal ``log p`` labels are
replaced by positive integer prime labels when checking convolution algebra;
all verified identities depend only on additivity of the logarithmic label.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from itertools import product
from math import isqrt
from typing import DefaultDict, Dict


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def factorization(n: int) -> Dict[int, int]:
    assert n >= 1
    out: Dict[int, int] = {}
    d = 2
    while d * d <= n:
        if n % d == 0:
            e = 0
            while n % d == 0:
                n //= d
                e += 1
            out[d] = e
        d += 1
    if n > 1:
        out[n] = 1
    return out


def mobius(n: int) -> int:
    factors = factorization(n)
    if any(e > 1 for e in factors.values()):
        return 0
    return -1 if len(factors) % 2 else 1


def divisors(n: int) -> list[int]:
    return [d for d in range(1, n + 1) if n % d == 0]


def prime_power_base(n: int) -> int | None:
    if n < 2:
        return None
    factors = factorization(n)
    if len(factors) != 1:
        return None
    return next(iter(factors))


def prime_powers(limit: int) -> list[int]:
    return [n for n in range(2, limit + 1) if prime_power_base(n) is not None]


def log_label(n: int) -> int:
    """An exact additive surrogate for log(n): sum v_p(n) * X_p with X_p=p."""
    return sum(p * e for p, e in factorization(n).items())


def mangoldt_label(n: int) -> int:
    p = prime_power_base(n)
    return 0 if p is None else p


def q(a: int, n: int) -> int:
    assert a >= 1 and n >= 0
    return n // a


def field(n: int) -> Fraction:
    numerator = ((37 * n * n + 11 * n + 5) % 113) - 56
    denominator = ((23 * n + 9) % 29) + 1
    return Fraction(numerator, denominator)


def defect(a: int, n: int) -> Fraction:
    return field(n) + field(q(a, n))


def common_suffix_curvature(a: int, b: int, suffix: int, n: int) -> Fraction:
    return defect(b * suffix, q(a, n)) - defect(a * suffix, q(b, n))


def action_weight(a: int) -> Fraction:
    p = prime_power_base(a)
    assert p is not None
    return Fraction(p, a)


def check_pointwise_curvature(limit: int = 120) -> None:
    actions = list(range(1, 11))
    for n in range(limit + 1):
        for a, b, c in product(actions, repeat=3):
            curvature = common_suffix_curvature(a, b, c, n)
            expected = field(q(a, n)) - field(q(b, n))
            assert curvature == expected, (n, a, b, c)
            assert curvature == -common_suffix_curvature(b, a, c, n)

        for a, b, c, suffix in product(range(1, 7), repeat=4):
            cocycle = (
                common_suffix_curvature(a, b, suffix, n)
                + common_suffix_curvature(b, c, suffix, n)
                + common_suffix_curvature(c, a, suffix, n)
            )
            assert cocycle == 0

            # Cylindrical degree lift: changing the common suffix changes no curvature.
            assert common_suffix_curvature(a, b, suffix, n) == (
                common_suffix_curvature(a, b, c, n)
            )


def check_weighted_cubic_polarization(limit: int = 180) -> None:
    for n in range(8, limit + 1):
        cutoff = max(2, isqrt(n))
        actions = prime_powers(cutoff)
        if not actions:
            continue

        u = {a: action_weight(a) for a in actions}
        total = sum(u.values(), Fraction(0, 1))
        pair_energy = sum(
            (
                u[a]
                * u[b]
                * (field(q(a, n)) - field(q(b, n))) ** 2
                for a in actions
                for b in actions
            ),
            Fraction(0, 1),
        )
        cubic_energy = sum(
            (
                u[a]
                * u[b]
                * u[c]
                * common_suffix_curvature(a, b, c, n) ** 2
                for a in actions
                for b in actions
                for c in actions
            ),
            Fraction(0, 1),
        )
        assert cubic_energy == total * pair_energy

        quotient_cloud_variance = pair_energy / (2 * total)
        assert quotient_cloud_variance == cubic_energy / (2 * total * total)

        # Hodge polarization of the transported signless-edge tensor.
        transported_norm = sum(
            (
                u[a] * u[b] * u[c] * defect(b * c, q(a, n)) ** 2
                for a in actions
                for b in actions
                for c in actions
            ),
            Fraction(0, 1),
        )
        antisymmetric_norm = sum(
            (
                u[a]
                * u[b]
                * u[c]
                * (
                    (
                        defect(b * c, q(a, n))
                        - defect(a * c, q(b, n))
                    )
                    / 2
                )
                ** 2
                for a in actions
                for b in actions
                for c in actions
            ),
            Fraction(0, 1),
        )
        assert antisymmetric_norm == cubic_energy / 4
        assert quotient_cloud_variance == 2 * antisymmetric_norm / (total * total)
        assert cubic_energy <= 4 * transported_norm


def check_all_degree_lifts(limit: int = 80, max_degree: int = 5) -> None:
    for n in range(8, limit + 1):
        actions = prime_powers(max(2, isqrt(n)))
        if not actions:
            continue
        u = {a: action_weight(a) for a in actions}
        total = sum(u.values(), Fraction(0, 1))
        pair_energy = sum(
            (
                u[a]
                * u[b]
                * (field(q(a, n)) - field(q(b, n))) ** 2
                for a in actions
                for b in actions
            ),
            Fraction(0, 1),
        )

        for degree in range(2, max_degree + 1):
            suffix_length = degree - 2
            lifted = Fraction(0, 1)
            for a in actions:
                for b in actions:
                    for suffix_word in product(actions, repeat=suffix_length):
                        suffix = 1
                        suffix_weight = Fraction(1, 1)
                        for c in suffix_word:
                            suffix *= c
                            suffix_weight *= u[c]
                        lifted += (
                            u[a]
                            * u[b]
                            * suffix_weight
                            * common_suffix_curvature(a, b, suffix, n) ** 2
                        )
            assert lifted == total**suffix_length * pair_energy


def triple_convolution_value(n: int, cutoff: int | None = None) -> int:
    total = 0
    for a in divisors(n):
        if cutoff is not None and a > cutoff:
            continue
        for b in divisors(n // a):
            c = n // (a * b)
            if cutoff is not None and (b > cutoff or c > cutoff):
                continue
            total += mangoldt_label(a) * mangoldt_label(b) * mangoldt_label(c)
    return total


def check_cubic_collision_support(limit: int = 100) -> None:
    for cutoff in range(2, 18):
        actions = prime_powers(cutoff)
        grouped: DefaultDict[int, Fraction] = defaultdict(Fraction)
        for a, b, c in product(actions, repeat=3):
            grouped[a * b * c] += action_weight(a) * action_weight(b) * action_weight(c)

        for n, coefficient in grouped.items():
            expected = Fraction(triple_convolution_value(n, cutoff), n)
            assert coefficient == expected, (cutoff, n, coefficient, expected)

    # Lambda_3 = D^2 Lambda + 3 Lambda * D Lambda + Lambda^{*3}.
    for n in range(1, limit + 1):
        lambda3 = sum(
            mobius(d) * log_label(n // d) ** 3 for d in divisors(n)
        )
        d2_lambda = mangoldt_label(n) * log_label(n) ** 2
        pair_sector = sum(
            mangoldt_label(d)
            * mangoldt_label(n // d)
            * log_label(n // d)
            for d in divisors(n)
        )
        cubic_sector = triple_convolution_value(n)
        assert lambda3 == d2_lambda + 3 * pair_sector + cubic_sector, n
        assert d2_lambda >= 0 and pair_sector >= 0 and cubic_sector >= 0


def main() -> None:
    check_pointwise_curvature()
    check_weighted_cubic_polarization()
    check_all_degree_lifts()
    check_cubic_collision_support()
    print("ordered cubic quotient curvature checks: PASS")


if __name__ == "__main__":
    main()
