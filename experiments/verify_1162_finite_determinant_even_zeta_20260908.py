#!/usr/bin/env python3
"""Exact rational checks for #1162 finite determinant / even-zeta carrier.

Python standard library only. No floating-point arithmetic and no numerical
differentiation. The checker validates the finite coefficient formula, dyadic
coefficient transport, and Newton reconstruction through zeta(12)/pi^12.
This is an experiment-local verifier, not a promoted Foundation module.
"""
from __future__ import annotations

from fractions import Fraction
from math import comb, factorial

Q = Fraction


def e_closed(N: int, j: int) -> Fraction:
    if j < 0:
        raise ValueError("j must be nonnegative")
    if j >= N:
        return Q(0)
    out = Q(2, factorial(2 * j + 2))
    for r in range(1, j + 1):
        out *= Q(N * N - r * r, N * N)
    return out


def dyadic_transport(N: int, coeffs: list[Fraction]) -> list[Fraction]:
    c = Q(1, 16 * N * N)
    out: list[Fraction] = []
    for j in range(len(coeffs)):
        total = Q(0)
        for r in range(0, (j + 1) // 2 + 1):
            idx = j - r
            if idx < 0 or idx >= len(coeffs):
                continue
            total += Q(comb(j + 1 - r, r)) * c**r * coeffs[idx]
        out.append(total)
    return out


def newton_power_sums(max_m: int) -> list[Fraction]:
    # e_j(infinity), j>=1. e_0 is not used by Newton here.
    e = [Q(1)] + [Q(2, factorial(2 * j + 2)) for j in range(1, max_m + 1)]
    p = [Q(0)] * (max_m + 1)
    for m in range(1, max_m + 1):
        value = Q(0)
        for j in range(1, m):
            value += (-1) ** (j - 1) * e[j] * p[m - j]
        value += (-1) ** (m + 1) * m * e[m]
        p[m] = value
    return p


def lucas_coefficient(m: int, j: int) -> Fraction:
    if j == 0:
        return Q(1)
    return Q(((-1) ** j) * m * comb(m - j, j), m - j)


def check_child_power_identity() -> None:
    # Abstract quadratic children with sum x and product c*x.
    # Verify the Lucas recurrence symbolically by coefficient dictionaries.
    # S_0=2, S_1=x, S_m=x*S_(m-1)-c*x*S_(m-2).
    # monomial key=(power_x,power_c).
    S: list[dict[tuple[int, int], Fraction]] = [
        {(0, 0): Q(2)},
        {(1, 0): Q(1)},
    ]
    for m in range(2, 13):
        out: dict[tuple[int, int], Fraction] = {}
        for (px, pc), v in S[m - 1].items():
            out[(px + 1, pc)] = out.get((px + 1, pc), Q(0)) + v
        for (px, pc), v in S[m - 2].items():
            key = (px + 1, pc + 1)
            out[key] = out.get(key, Q(0)) - v
        S.append(out)

        expected = {
            (m - j, j): lucas_coefficient(m, j)
            for j in range(0, m // 2 + 1)
        }
        assert out == expected, (m, out, expected)


def main() -> int:
    # Closed coefficient formula vs dyadic composition for many finite N.
    checks = 0
    for N in range(2, 41):
        max_j = min(N - 1, 12)
        coeffs = [e_closed(N, j) for j in range(max_j + 1)]
        transported = dyadic_transport(N, coeffs)
        for j, value in enumerate(transported):
            assert value == e_closed(2 * N, j), (N, j, value, e_closed(2 * N, j))
            checks += 1

    check_child_power_identity()

    p = newton_power_sums(6)
    expected_C = {
        1: Q(1, 12),
        2: Q(1, 720),
        3: Q(1, 30240),
        4: Q(1, 1209600),
        5: Q(1, 47900160),
        6: Q(691, 1307674368000),
    }
    expected_zeta_ratio = {
        1: Q(1, 6),
        2: Q(1, 90),
        3: Q(1, 945),
        4: Q(1, 9450),
        5: Q(1, 93555),
        6: Q(691, 638512875),
    }
    for m in range(1, 7):
        assert p[m] == expected_C[m], (m, p[m], expected_C[m])
        ratio = p[m] * Q(4**m, 2)
        assert ratio == expected_zeta_ratio[m], (m, ratio, expected_zeta_ratio[m])

    print(f"finite coefficient transport checks={checks}")
    for m in range(1, 7):
        print(
            f"m={m} C_m={p[m]} "
            f"zeta(2m)/pi^(2m)={p[m] * Q(4**m, 2)}"
        )
    print("PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
