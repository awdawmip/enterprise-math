#!/usr/bin/env python3
"""Exact/local checker for the #1160 rational complementary-turn Pell chain.

Native assertions use integer/Fraction arithmetic only. Floating logarithms are used
only for the analytic generalized-Lehmer readout after the exact turn identities
have been certified.
"""

from __future__ import annotations

import math
from fractions import Fraction


def mul(z: tuple[int, int], w: tuple[int, int]) -> tuple[int, int]:
    return (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])


def complement(v: tuple[int, int]) -> tuple[int, int]:
    b, a = v
    return (b + a, b - a)


def defect(v: tuple[int, int]) -> int:
    b, a = v
    return b * b - 2 * a * b - a * a


def generalized_lehmer(v: tuple[int, int]) -> float:
    b, a = v
    x = a / b
    y = (b - a) / (b + a)
    return 1.0 / math.log10(1.0 / x) + 1.0 / math.log10(1.0 / y)


def main() -> None:
    v = (2, 1)
    mu_star = 2.0 / math.log10(1.0 + math.sqrt(2.0))
    previous_mu = float("inf")

    rows = []
    for n in range(8):
        b, a = v
        c = complement(v)
        bp, ap = c

        # Exact complementary diagonal factorization.
        product = mul((b, a), (bp, ap))
        scale = a * a + b * b
        assert product == (scale, scale)

        # C is an involution after positive projective scaling.
        assert complement(c) == (2 * b, 2 * a)

        q = defect(v)
        assert abs(q) == 1
        assert q == (-1) ** (n + 1)

        # The two rational slopes form an exact unimodular bracket.
        x = Fraction(a, b)
        y = Fraction(b - a, b + a)
        assert y - x == Fraction(q, b * (b + a))
        assert abs(y - x) == Fraction(1, b * (b + a))

        # The next state is the Farey mediant of the complementary bracket.
        next_v = (b + bp, a + ap)
        assert next_v == (2 * b + a, b)
        assert defect(next_v) == -q

        mu = generalized_lehmer(v)
        assert mu > mu_star
        assert mu < previous_mu
        previous_mu = mu
        rows.append((n, b, a, c, q, float(abs(y - x)), mu))
        v = next_v

    print(f"sharp_generalized_two_factor_infimum={mu_star:.15f}")
    print("n  v=(b,a)  C(v)  Q  bracket_width  generalized_mu")
    for n, b, a, c, q, width, mu in rows:
        print(f"{n:2d} ({b},{a}) {c} {q:+d} {width:.15g} {mu:.15f}")

    expected = [
        (2, 1),
        (5, 2),
        (12, 5),
        (29, 12),
        (70, 29),
        (169, 70),
        (408, 169),
        (985, 408),
    ]
    assert [(row[1], row[2]) for row in rows] == expected
    assert abs(rows[0][-1] - 5.4178313691767475) < 1e-13
    assert abs(rows[3][-1] - 5.224997050034012) < 1e-13
    print("rational complementary-turn Pell regression certificate: PASS")


if __name__ == "__main__":
    main()
