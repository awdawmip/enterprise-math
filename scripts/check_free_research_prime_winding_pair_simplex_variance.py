#!/usr/bin/env python3
"""Exact finite checks for the weighted prime-winding pair-simplex carrier.

All identities are weight-generic.  To keep the checker rational, the formal
positive label ``log p`` is replaced by the positive integer label ``p``;
none of the checked algebra depends on the analytic value of that label.
"""

from __future__ import annotations

from collections import defaultdict
from fractions import Fraction
from math import isqrt
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
    """Return p when n is a positive p-power, otherwise None."""
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


def q(a: int, n: int) -> int:
    assert a >= 1 and n >= 0
    return n // a


def field(n: int) -> Fraction:
    numerator = ((31 * n * n + 17 * n + 9) % 101) - 50
    denominator = ((19 * n + 7) % 23) + 1
    return Fraction(numerator, denominator)


def defect(a: int, n: int) -> Fraction:
    return field(n) + field(q(a, n))


def weight(a: int) -> Fraction:
    p = prime_power_base(a)
    assert p is not None
    return Fraction(p, a)


def check_universal_triangles(limit: int = 180) -> None:
    actions = list(range(1, 18))
    for n in range(limit + 1):
        for a in actions:
            for b in actions:
                assert q(b, q(a, n)) == q(a * b, n)
                lhs = 2 * field(n)
                rhs = defect(a, n) + defect(a * b, n) - defect(b, q(a, n))
                assert lhs == rhs, (n, a, b)
                assert 4 * field(n) ** 2 <= 3 * (
                    defect(a, n) ** 2
                    + defect(a * b, n) ** 2
                    + defect(b, q(a, n)) ** 2
                )


def check_weighted_gap(limit: int = 160) -> None:
    for n in range(8, limit + 1):
        y = max(2, isqrt(n))
        actions = prime_powers(y)
        if not actions:
            continue
        u = {a: weight(a) for a in actions}
        total = sum(u.values(), Fraction(0, 1))

        e1 = sum((u[a] * defect(a, n) ** 2 for a in actions), Fraction(0, 1))
        direct = sum(
            (
                u[a] * u[b] * defect(a * b, n) ** 2
                for a in actions
                for b in actions
            ),
            Fraction(0, 1),
        )
        transported = sum(
            (
                u[a] * u[b] * defect(b, q(a, n)) ** 2
                for a in actions
                for b in actions
            ),
            Fraction(0, 1),
        )
        assert 4 * total**2 * field(n) ** 2 <= 3 * (
            total * e1 + direct + transported
        )

        # Direct pair histories group by the recoalesced product action.
        convolution: DefaultDict[int, Fraction] = defaultdict(Fraction)
        for a in actions:
            for b in actions:
                convolution[a * b] += u[a] * u[b]
        grouped = sum(
            (coefficient * defect(c, n) ** 2 for c, coefficient in convolution.items()),
            Fraction(0, 1),
        )
        assert direct == grouped

        # Transport/direct edges control the displacement of each one-step endpoint.
        displacement = total * sum(
            (
                u[a] * (field(q(a, n)) - field(n)) ** 2
                for a in actions
            ),
            Fraction(0, 1),
        )
        assert displacement <= 2 * (direct + transported)


def check_gram_variance(limit: int = 200) -> None:
    for n in range(4, limit + 1):
        actions = prime_powers(max(2, isqrt(n) + 2))
        if not actions:
            continue
        u = {a: weight(a) for a in actions}
        total = sum(u.values(), Fraction(0, 1))
        values = {a: field(q(a, n)) for a in actions}
        mean = sum((u[a] * values[a] for a in actions), Fraction(0, 1)) / total

        e1 = sum((u[a] * (field(n) + values[a]) ** 2 for a in actions), Fraction(0, 1))
        variance = sum(
            (u[a] * (values[a] - mean) ** 2 for a in actions),
            Fraction(0, 1),
        )
        residual = total * field(n) + sum(
            (u[a] * values[a] for a in actions), Fraction(0, 1)
        )
        assert e1 == residual**2 / total + variance

        pair_variance = sum(
            (
                u[a] * u[b] * (values[a] - values[b]) ** 2
                for a in actions
                for b in actions
            ),
            Fraction(0, 1),
        )
        assert pair_variance == 2 * total * variance


def main() -> None:
    check_universal_triangles()
    check_weighted_gap()
    check_gram_variance()
    print("prime-winding pair-simplex variance checks: PASS")


if __name__ == "__main__":
    main()
