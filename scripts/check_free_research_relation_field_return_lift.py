#!/usr/bin/env python3
"""Exact finite checks for the quotient relation-field return lift.

All calculations use ``Fraction``.  Prime-power logarithmic weights are replaced
by the exact positive surrogate ``p/a``; the identities require only positive
weights and quotient composition.
"""

from __future__ import annotations

from fractions import Fraction
from math import isqrt


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


def q(a: int, n: int) -> int:
    return n // a


def field(n: int) -> Fraction:
    return Fraction(
        ((41 * n * n + 13 * n + 7) % 127) - 63,
        ((29 * n + 11) % 31) + 1,
    )


def defect(a: int, n: int) -> Fraction:
    return field(n) + field(q(a, n))


def relation(u: dict[int, Fraction], a: int, b: int, n: int) -> Fraction:
    return u[a] * u[b] * (field(q(a, n)) - field(q(b, n)))


def residual(actions: list[int], u: dict[int, Fraction], n: int) -> Fraction:
    return sum((u[c] * defect(c, n) for c in actions), Fraction(0, 1))


def relation_norm(
    actions: list[int],
    u: dict[int, Fraction],
    entries: dict[tuple[int, int], Fraction],
) -> Fraction:
    return sum(
        (
            entries[a, b] ** 2 / (u[a] * u[b])
            for a in actions
            for b in actions
        ),
        Fraction(0, 1),
    )


def weighted_variance(
    actions: list[int],
    u: dict[int, Fraction],
    values: dict[int, Fraction],
) -> Fraction:
    total = sum(u.values(), Fraction(0, 1))
    mean = sum(
        (u[a] * values[a] for a in actions), Fraction(0, 1)
    ) / total
    return sum(
        (u[a] * (values[a] - mean) ** 2 for a in actions),
        Fraction(0, 1),
    )


def check_return_lift(limit: int = 240) -> None:
    for n in range(8, limit + 1):
        actions = prime_powers(max(2, isqrt(n)))
        if not actions:
            continue
        u = {a: weight(a) for a in actions}
        total = sum(u.values(), Fraction(0, 1))

        for a in actions:
            for b in actions:
                transported = sum(
                    (u[c] * relation(u, a, b, q(c, n)) for c in actions),
                    Fraction(0, 1),
                )
                lhs = total * relation(u, a, b, n) + transported
                rhs = u[a] * u[b] * (
                    residual(actions, u, q(a, n))
                    - residual(actions, u, q(b, n))
                )
                assert lhs == rhs, (n, a, b, lhs, rhs)

                normalized = relation(u, a, b, n) + transported / total
                normalized_rhs = u[a] * u[b] / total * (
                    residual(actions, u, q(a, n))
                    - residual(actions, u, q(b, n))
                )
                assert normalized == normalized_rhs


def check_norm_identity(limit: int = 220) -> None:
    for n in range(8, limit + 1):
        actions = prime_powers(max(2, isqrt(n)))
        if not actions:
            continue
        u = {a: weight(a) for a in actions}
        total = sum(u.values(), Fraction(0, 1))

        z = {
            (a, b): relation(u, a, b, n)
            for a in actions
            for b in actions
        }
        pz = {
            (a, b): sum(
                (u[c] * relation(u, a, b, q(c, n)) for c in actions),
                Fraction(0, 1),
            )
            / total
            for a in actions
            for b in actions
        }
        return_field = {
            key: z[key] + pz[key]
            for key in z
        }
        residual_values = {
            a: residual(actions, u, q(a, n))
            for a in actions
        }

        z_norm = relation_norm(actions, u, z)
        endpoint_pair_energy = sum(
            (
                u[a]
                * u[b]
                * (field(q(a, n)) - field(q(b, n))) ** 2
                for a in actions
                for b in actions
            ),
            Fraction(0, 1),
        )
        assert z_norm == endpoint_pair_energy

        return_norm = relation_norm(actions, u, return_field)
        residual_variance = weighted_variance(actions, u, residual_values)
        assert return_norm == 2 * residual_variance / total

        # The suffix-transport average is a Markov nonexpansion in the relation norm.
        average_future_norm = sum(
            (
                u[c]
                * relation_norm(
                    actions,
                    u,
                    {
                        (a, b): relation(u, a, b, q(c, n))
                        for a in actions
                        for b in actions
                    },
                )
                for c in actions
            ),
            Fraction(0, 1),
        ) / total
        assert relation_norm(actions, u, pz) <= average_future_norm


def main() -> None:
    check_return_lift()
    check_norm_identity()
    print("relation-field return-lift checks: PASS")


if __name__ == "__main__":
    main()
