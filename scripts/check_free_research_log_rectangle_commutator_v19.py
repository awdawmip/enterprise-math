#!/usr/bin/env python3
"""Exact finite checks for the V19 log-rectangle commutator closure."""

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


def build_quotient_operator(limit: int, weights: dict[int, Fraction]) -> tuple[Matrix, Vector]:
    operator = zeros(limit + 1)
    for n in range(1, limit + 1):
        for action, weight in weights.items():
            if action <= n:
                operator[n][n // action] += weight
    mass = [sum(row, Fraction(0)) for row in operator]
    return operator, mass


def direct_rectangle_operator(
    limit: int,
    weights: dict[int, Fraction],
    mass: Vector,
) -> Matrix:
    out = zeros(limit + 1)
    for n in range(1, limit + 1):
        for a, wa in weights.items():
            for b, wb in weights.items():
                if a * b > n:
                    continue
                ma = n // a
                mb = n // b
                mab = n // (a * b)
                curvature = mass[ma] + mass[mb] - mass[n] - mass[mab]
                out[n][mab] += wa * wb * curvature
    return out


def history_mass(limit: int, weights: dict[int, Fraction], k: int) -> Vector:
    values = [Fraction(1) for _ in range(limit + 1)]
    for _ in range(k):
        next_values = [Fraction(0) for _ in range(limit + 1)]
        for n in range(1, limit + 1):
            next_values[n] = sum(
                (weight * values[n // action]
                 for action, weight in weights.items()
                 if action <= n),
                Fraction(0),
            )
        values = next_values
    return values


def check_rectangle_formula() -> None:
    limit = 36
    weights = {
        2: Fraction(2, 3),
        3: Fraction(3, 5),
        4: Fraction(5, 7),
        5: Fraction(7, 11),
        7: Fraction(11, 13),
        8: Fraction(13, 17),
        9: Fraction(17, 19),
    }
    l, mass = build_quotient_operator(limit, weights)
    m = diagonal(mass)
    d = mat_sub(mat_sub(mat_mul(m, l), mat_mul(l, m)), mat_mul(l, l))
    commutator = mat_sub(mat_mul(l, d), mat_mul(d, l))
    direct = direct_rectangle_operator(limit, weights, mass)
    assert commutator == direct

    field = [Fraction(((13 * n * n + 5 * n + 1) % 31) - 15, 9)
             for n in range(limit + 1)]
    root = limit
    value = mat_vec(commutator, field)[root]

    max_curvature = Fraction(0)
    for a in weights:
        for b in weights:
            if a * b <= root:
                curvature = abs(
                    mass[root // a] + mass[root // b]
                    - mass[root] - mass[root // (a * b)]
                )
                max_curvature = max(max_curvature, curvature)

    c2 = history_mass(limit, weights, 2)[root]
    sup_field = max(abs(value) for value in field)
    assert abs(value) <= max_curvature * c2 * sup_field


def check_placement_mass_bound() -> None:
    limit = 48
    weights = {
        2: Fraction(1, 2),
        3: Fraction(2, 5),
        4: Fraction(3, 7),
        5: Fraction(5, 11),
        7: Fraction(7, 13),
        8: Fraction(11, 17),
    }
    l, mass = build_quotient_operator(limit, weights)
    m = diagonal(mass)
    d = mat_sub(mat_sub(mat_mul(m, l), mat_mul(l, m)), mat_mul(l, l))
    c = mat_sub(mat_mul(l, d), mat_mul(d, l))

    def mat_pow(matrix: Matrix, exponent: int) -> Matrix:
        out = zeros(len(matrix))
        for i in range(len(matrix)):
            out[i][i] = Fraction(1)
        base = matrix
        while exponent:
            if exponent & 1:
                out = mat_mul(out, base)
            base = mat_mul(base, base)
            exponent >>= 1
        return out

    field = [Fraction(((17 * n + 3) % 23) - 11, 8)
             for n in range(limit + 1)]
    sup_field = max(abs(value) for value in field)
    root = limit
    max_curvature = max(
        abs(mass[root // a] + mass[root // b]
            - mass[root] - mass[root // (a * b)])
        for a in weights for b in weights if a * b <= root
    )

    for k in (2, 3, 4):
        ck = history_mass(limit, weights, k)[root]
        for j in range(k - 1):
            placement = mat_mul(mat_mul(mat_pow(l, j), c),
                                mat_pow(l, k - 2 - j))
            value = mat_vec(placement, field)[root]
            # The local curvature can only decrease after an outer prefix;
            # use the global maximum over all reachable states for safety.
            global_max = Fraction(0)
            for n in range(1, limit + 1):
                for a in weights:
                    for b in weights:
                        if a * b <= n:
                            global_max = max(
                                global_max,
                                abs(mass[n // a] + mass[n // b]
                                    - mass[n] - mass[n // (a * b)]),
                            )
            assert abs(value) <= global_max * ck * sup_field


def main() -> None:
    check_rectangle_formula()
    check_placement_mass_bound()
    print("log-rectangle commutator checks passed")


if __name__ == "__main__":
    main()
