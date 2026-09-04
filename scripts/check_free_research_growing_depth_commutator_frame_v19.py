#!/usr/bin/env python3
"""Exact finite checks for the V19 growing-depth Volterra/placement frame.

The theorem-level algebra uses ``fractions.Fraction`` only.  The script checks:

1. comparison-model convolution masses;
2. the exact discrete Volterra derivation identity;
3. the stopped/valid mass identity;
4. the commutator-placement path ANOVA;
5. the full positive reverse frame;
6. the first parametrix identity;
7. the nilpotent high-order-tail no-go.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import comb, factorial
from typing import Iterable


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
    return [
        [left[i][j] + right[i][j] for j in range(len(left))]
        for i in range(len(left))
    ]


def mat_sub(left: Matrix, right: Matrix) -> Matrix:
    return [
        [left[i][j] - right[i][j] for j in range(len(left))]
        for i in range(len(left))
    ]


def mat_scale(c: Fraction, matrix: Matrix) -> Matrix:
    return [[c * value for value in row] for row in matrix]


def mat_mul(left: Matrix, right: Matrix) -> Matrix:
    n = len(left)
    out = zeros(n)
    for i, j, k in product(range(n), repeat=3):
        out[i][j] += left[i][k] * right[k][j]
    return out


def mat_vec(matrix: Matrix, vector: Vector) -> Vector:
    return [
        sum((matrix[i][j] * vector[j] for j in range(len(vector))), Fraction(0))
        for i in range(len(vector))
    ]


def mat_pow(matrix: Matrix, exponent: int) -> Matrix:
    out = identity(len(matrix))
    base = matrix
    power = exponent
    while power:
        if power & 1:
            out = mat_mul(out, base)
        base = mat_mul(base, base)
        power >>= 1
    return out


def diagonal(values: Iterable[int]) -> Matrix:
    vals = list(values)
    out = zeros(len(vals))
    for i, value in enumerate(vals):
        out[i][i] = Fraction(value)
    return out


def exact_grid_history_mass(t: int, k: int) -> int:
    """Atoms of weight one at 1,2,...; count positive k-tuples of sum <= t."""
    if t < k:
        return 0
    return comb(t, k)


def upper_comparison_mass(t: int, k: int, c: int) -> Fraction:
    return sum(
        (
            Fraction(comb(k, j) * c ** (k - j) * t**j, factorial(j))
            for j in range(k + 1)
        ),
        Fraction(0),
    )


def check_convolution_comparison() -> None:
    # For the integer grid, |floor(x)-x| <= 1, so C=1 is valid.
    c = 1
    for t in (8, 12, 20, 35):
        for k in range(1, min(7, t) + 1):
            actual = Fraction(exact_grid_history_mass(t, k))
            lower = Fraction(max(t - k * c, 0) ** k, factorial(k))
            upper = upper_comparison_mass(t, k, c)
            assert lower <= actual <= upper

            # Algebraic exponential-series majorant, truncated at k.
            normalized_upper = upper * factorial(k) / t**k
            exponential_truncation = sum(
                (Fraction((c * k * k) ** ell, t**ell * factorial(ell))
                 for ell in range(k + 1)),
                Fraction(0),
            )
            assert normalized_upper <= exponential_truncation


def fixture() -> tuple[Matrix, Matrix, Vector, int]:
    n = 7
    # Positive strict-lower-triangular history operator.  Row i transports
    # to earlier states j<i.
    l = zeros(n)
    for i in range(1, n):
        for j in range(i):
            l[i][j] = Fraction(((3 * i + 5 * j + 1) % 7) + 1, i + j + 3)
    m = diagonal([0, 2, 5, 7, 11, 13, 17])
    f = [Fraction(((11 * i * i + 7 * i + 3) % 29) - 14, 9) for i in range(n)]
    root = n - 1
    return m, l, f, root


def first_defect(m: Matrix, l: Matrix) -> Matrix:
    return mat_sub(mat_sub(mat_mul(m, l), mat_mul(l, m)), mat_mul(l, l))


def kth_defect(m: Matrix, l: Matrix, k: int) -> Matrix:
    lk = mat_pow(l, k)
    return mat_sub(
        mat_sub(mat_mul(m, lk), mat_mul(lk, m)),
        mat_scale(Fraction(k), mat_pow(l, k + 1)),
    )


def check_derivation_and_mass() -> None:
    m, l, _, root = fixture()
    d = first_defect(m, l)
    one = [Fraction(1) for _ in range(len(l))]
    a = m[root][root]

    for k in range(1, 5):
        delta = kth_defect(m, l, k)
        placement_sum = zeros(len(l))
        for j in range(k):
            placement_sum = mat_add(
                placement_sum,
                mat_mul(mat_mul(mat_pow(l, j), d), mat_pow(l, k - 1 - j)),
            )
        assert delta == placement_sum

        c_k = mat_vec(mat_pow(l, k), one)[root]
        c_k1 = mat_vec(mat_pow(l, k + 1), one)[root]
        mass_defect = mat_vec(delta, one)[root]
        assert mass_defect == a * c_k - (k + 1) * c_k1


def check_placement_frame() -> None:
    m, l, f, root = fixture()
    d = first_defect(m, l)
    g = mat_vec(d, f)
    one = [Fraction(1) for _ in range(len(l))]

    for k in (2, 3, 4):
        history = mat_pow(l, k - 1)
        c = mat_vec(history, one)[root]
        assert c > 0

        placements = []
        for j in range(k):
            operator = mat_mul(
                mat_mul(mat_pow(l, j), d),
                mat_pow(l, k - 1 - j),
            )
            placements.append(mat_vec(operator, f)[root])

        delta_value = mat_vec(kth_defect(m, l, k), f)[root]
        assert sum(placements, Fraction(0)) == delta_value

        adjacent = [
            placements[j + 1] - placements[j]
            for j in range(k - 1)
        ]
        commutator = mat_sub(mat_mul(l, d), mat_mul(d, l))
        for j in range(k - 1):
            expected = mat_vec(
                mat_mul(
                    mat_mul(mat_pow(l, j), commutator),
                    mat_pow(l, k - 2 - j),
                ),
                f,
            )[root]
            assert adjacent[j] == expected

        z_last = placements[-1]
        placement_rhs = (
            Fraction(2, k * k) * delta_value**2
            + Fraction((k - 1) * (2 * k - 1), 3 * k)
            * sum((value**2 for value in adjacent), Fraction(0))
        )
        assert z_last**2 <= placement_rhs

        star = sum(
            (
                history[root][endpoint]
                * (g[root] - g[endpoint]) ** 2
                for endpoint in range(len(l))
            ),
            Fraction(0),
        )
        full_rhs = (
            Fraction(4, k * k * c * c) * delta_value**2
            + Fraction(2 * (k - 1) * (2 * k - 1), 3 * k * c * c)
            * sum((value**2 for value in adjacent), Fraction(0))
            + Fraction(2, c) * star
        )
        assert g[root] ** 2 <= full_rhs


def check_parametrix() -> None:
    m, l, f, root = fixture()
    d = first_defect(m, l)
    residual = mat_vec(mat_add(m, l), f)
    left = m[root][root] ** 2 * f[root]
    right = (
        mat_vec(mat_sub(m, l), residual)[root]
        - mat_vec(d, f)[root]
    )
    assert left == right


def check_nilpotent_no_go() -> None:
    l = [
        [Fraction(0), Fraction(0)],
        [Fraction(1), Fraction(0)],
    ]
    m = diagonal([0, 1])
    d = first_defect(m, l)
    assert d != zeros(2)
    assert mat_pow(l, 2) == zeros(2)
    for k in range(2, 6):
        assert kth_defect(m, l, k) == zeros(2)


def main() -> None:
    check_convolution_comparison()
    check_derivation_and_mass()
    check_placement_frame()
    check_parametrix()
    check_nilpotent_no_go()
    print("growing-depth Volterra simplex and commutator frame: exact checks passed")


if __name__ == "__main__":
    main()
