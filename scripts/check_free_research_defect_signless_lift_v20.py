#!/usr/bin/env python3
"""Exact finite checks for the V20 signless lift of the first defect."""

from __future__ import annotations

from fractions import Fraction
from itertools import product


Vector = list[Fraction]
Matrix = list[list[Fraction]]


def zeros(n: int) -> Matrix:
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    n = len(left)
    out = zeros(n)
    for i, j, k in product(range(n), repeat=3):
        out[i][j] += left[i][k] * right[k][j]
    return out


def mat_add(left: Matrix, right: Matrix) -> Matrix:
    return [[left[i][j] + right[i][j] for j in range(len(left))]
            for i in range(len(left))]


def mat_sub(left: Matrix, right: Matrix) -> Matrix:
    return [[left[i][j] - right[i][j] for j in range(len(left))]
            for i in range(len(left))]


def mat_vec(matrix: Matrix, vector: Vector) -> Vector:
    return [sum((matrix[i][j] * vector[j] for j in range(len(vector))),
                Fraction(0))
            for i in range(len(vector))]


def diagonal(values: Vector) -> Matrix:
    out = zeros(len(values))
    for i, value in enumerate(values):
        out[i][i] = value
    return out


def quotient_operator(limit: int, action: int) -> Matrix:
    out = zeros(limit + 1)
    for n in range(limit + 1):
        out[n][n // action] = Fraction(1)
    return out


def build_l(limit: int, weights: dict[int, Fraction]) -> tuple[Matrix, Vector]:
    l = zeros(limit + 1)
    for n in range(1, limit + 1):
        for action, weight in weights.items():
            if action <= n:
                l[n][n // action] += weight
    mass = [sum(row, Fraction(0)) for row in l]
    return l, mass


def direct_q_commutator(
    limit: int,
    c: int,
    weights: dict[int, Fraction],
    mass: Vector,
) -> Matrix:
    out = zeros(limit + 1)
    for n in range(1, limit + 1):
        for a, weight in weights.items():
            if a * c <= n:
                kappa = (
                    mass[n // a] + mass[n // c]
                    - mass[n] - mass[n // (a * c)]
                )
                out[n][n // (a * c)] += weight * kappa
    return out


def parity_fold_value(
    n: int,
    weights: dict[int, Fraction],
    field: Vector,
) -> Fraction:
    total = Fraction(0)
    for a, wa in weights.items():
        if a > n:
            continue
        for b, wb in weights.items():
            if b > n:
                continue
            if a * b <= n:
                total -= wa * wb * field[n // (a * b)]
            else:
                total += wa * wb * field[n // a]
    return total


def stopped_square(
    n: int,
    weights: dict[int, Fraction],
    field: Vector,
) -> Fraction:
    total = Fraction(0)
    for a, wa in weights.items():
        if a > n:
            continue
        for b, wb in weights.items():
            if b > n:
                continue
            endpoint = n // (a * b) if a * b <= n else n // a
            total += wa * wb * field[endpoint] ** 2
    return total


def check_signless_lift() -> None:
    limit = 42
    weights = {
        2: Fraction(2, 3),
        3: Fraction(3, 5),
        4: Fraction(5, 7),
        5: Fraction(7, 11),
        7: Fraction(11, 13),
        8: Fraction(13, 17),
        9: Fraction(17, 19),
    }
    l, mass = build_l(limit, weights)
    m = diagonal(mass)
    d = mat_sub(mat_sub(mat_mul(m, l), mat_mul(l, m)), mat_mul(l, l))
    identity = zeros(limit + 1)
    for i in range(limit + 1):
        identity[i][i] = Fraction(1)

    field = [Fraction(0)] + [
        Fraction(((19 * n * n + 7 * n + 5) % 37) - 18, 11)
        for n in range(1, limit + 1)
    ]

    for c in (2, 3, 5, 8):
        q = quotient_operator(limit, c)
        delta = mat_add(identity, q)
        q_comm = mat_sub(mat_mul(q, d), mat_mul(d, q))
        direct = direct_q_commutator(limit, c, weights, mass)
        assert q_comm == direct
        assert mat_mul(delta, d) == mat_add(mat_mul(d, delta), q_comm)

        # Pointwise coefficient-mass bound for the commutator.
        for n in range(c, limit + 1):
            max_kappa = Fraction(0)
            for a in weights:
                if a * c <= n:
                    max_kappa = max(
                        max_kappa,
                        abs(mass[n // a] + mass[n // c]
                            - mass[n] - mass[n // (a * c)]),
                    )
            lhs = abs(mat_vec(q_comm, field)[n])
            rhs = max_kappa * mass[n // c] * max(abs(x) for x in field)
            assert lhs <= rhs

    # Exact parity-fold realization and Cauchy stopped-square bound.
    dfield = mat_vec(d, field)
    for n in range(2, limit + 1):
        assert dfield[n] == parity_fold_value(n, weights, field)
        assert dfield[n] ** 2 <= mass[n] ** 2 * stopped_square(n, weights, field)


def main() -> None:
    check_signless_lift()
    print("defect signless-lift checks passed")


if __name__ == "__main__":
    main()
