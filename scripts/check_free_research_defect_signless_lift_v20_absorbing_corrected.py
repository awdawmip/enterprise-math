#!/usr/bin/env python3
"""Corrected exact checks for the V20 signless lift.

The deterministic quotient and adaptive history operator commute only on the
absorbing-zero subspace ``f(0)=0``.  Accordingly this checker compares their
action on exact rational test fields in that subspace instead of asserting an
incorrect full-matrix equality including the unused absorbing column.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product


Vector = list[Fraction]
Matrix = list[list[Fraction]]


def zeros(n: int) -> Matrix:
    return [[Fraction(0) for _ in range(n)] for _ in range(n)]


def identity(n: int) -> Matrix:
    out = zeros(n)
    for i in range(n):
        out[i][i] = Fraction(1)
    return out


def mat_add(left: Matrix, right: Matrix) -> Matrix:
    return [[left[i][j] + right[i][j] for j in range(len(left))]
            for i in range(len(left))]


def mat_sub(left: Matrix, right: Matrix) -> Matrix:
    return [[left[i][j] - right[i][j] for j in range(len(left))]
            for i in range(len(left))]


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    n = len(left)
    out = zeros(n)
    for i, j, k in product(range(n), repeat=3):
        out[i][j] += left[i][k] * right[k][j]
    return out


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


def build_history_operator(
    limit: int,
    weights: dict[int, Fraction],
) -> tuple[Matrix, Vector]:
    operator = zeros(limit + 1)
    for n in range(1, limit + 1):
        for action, weight in weights.items():
            if action <= n:
                operator[n][n // action] += weight
    mass = [sum(row, Fraction(0)) for row in operator]
    return operator, mass


def direct_q_commutator_value(
    n: int,
    c: int,
    weights: dict[int, Fraction],
    mass: Vector,
    field: Vector,
) -> Fraction:
    return sum(
        (
            weight
            * (mass[n // a] + mass[n // c]
               - mass[n] - mass[n // (a * c)])
            * field[n // (a * c)]
            for a, weight in weights.items()
            if a * c <= n
        ),
        Fraction(0),
    )


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


def check_absorbing_subspace_lift() -> None:
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
    history, mass = build_history_operator(limit, weights)
    multiplier = diagonal(mass)
    defect = mat_sub(
        mat_sub(mat_mul(multiplier, history),
                mat_mul(history, multiplier)),
        mat_mul(history, history),
    )
    ident = identity(limit + 1)

    fields: list[Vector] = []
    for seed in (3, 7, 13):
        fields.append(
            [Fraction(0)]
            + [Fraction(((seed * n * n + 5 * n + 1) % 41) - 20, 13)
               for n in range(1, limit + 1)]
        )

    for c in (2, 3, 5, 8):
        quotient = quotient_operator(limit, c)
        delta = mat_add(ident, quotient)
        commutator = mat_sub(mat_mul(quotient, defect),
                             mat_mul(defect, quotient))

        # Q_c L = L Q_c only after evaluation on f(0)=0.
        ql_minus_lq = mat_sub(mat_mul(quotient, history),
                              mat_mul(history, quotient))
        for field in fields:
            assert field[0] == 0
            assert mat_vec(ql_minus_lq, field) == [Fraction(0)] * (limit + 1)

            comm_value = mat_vec(commutator, field)
            for n in range(1, limit + 1):
                assert comm_value[n] == direct_q_commutator_value(
                    n, c, weights, mass, field
                )

            lhs = mat_vec(mat_mul(delta, defect), field)
            rhs = mat_vec(mat_add(mat_mul(defect, delta), commutator), field)
            assert lhs == rhs

            defect_field = mat_vec(defect, field)
            for n in range(2, limit + 1):
                assert defect_field[n] == parity_fold_value(n, weights, field)
                assert defect_field[n] ** 2 <= (
                    mass[n] ** 2 * stopped_square(n, weights, field)
                )


def main() -> None:
    check_absorbing_subspace_lift()
    print("absorbing-corrected defect signless-lift checks passed")


if __name__ == "__main__":
    main()
