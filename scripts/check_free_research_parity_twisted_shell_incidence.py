#!/usr/bin/env python3
"""Exact checks for the parity-twisted shell-incidence calculation.

All theorem-level checks use ``fractions.Fraction``.  The script verifies the
monomial matrix of the radial up/down operator, its self-adjointness in the
Beta(1,R) moment form, the closed eigenvalue diagonal, the top/leaf overlap,
and the parity conversion of signless edges into ordinary gradients.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial
from typing import List


Polynomial = List[Fraction]  # coefficient of x^degree


def add_polynomial(left: Polynomial, right: Polynomial) -> Polynomial:
    size = max(len(left), len(right))
    result = [Fraction(0) for _ in range(size)]
    for degree, value in enumerate(left):
        result[degree] += value
    for degree, value in enumerate(right):
        result[degree] += value
    return result


def scale_polynomial(scale: Fraction, polynomial: Polynomial) -> Polynomial:
    return [scale * value for value in polynomial]


def beta_one_rminusone_moment(power: int, r: int) -> Fraction:
    """E[Z^power] for Z ~ Beta(1,r-1)."""
    if r < 2:
        raise ValueError("r must be at least two")
    return Fraction(factorial(power) * factorial(r - 1), factorial(r + power - 1))


def beta_one_r_moment(power: int, r: int) -> Fraction:
    """E[S^power] for S ~ Beta(1,r)."""
    return Fraction(factorial(power) * factorial(r), factorial(r + power))


def down_monomial(power: int, r: int) -> Polynomial:
    """D(l^power), where l=s+(1-s)Z and Z~Beta(1,r-1)."""
    result: Polynomial = [Fraction(0) for _ in range(power + 1)]
    for h in range(power + 1):
        # Choose h copies of (1-s)Z and power-h copies of s.
        prefactor = Fraction(comb(power, h)) * beta_one_rminusone_moment(h, r)
        for j in range(h + 1):
            degree = power - h + j
            result[degree] += prefactor * comb(h, j) * ((-1) ** j)
    return result


def up_down_monomial(power: int, r: int) -> Polynomial:
    """T(s^power)=D(U(s^power))=D(l^power)/(power+1)."""
    return scale_polynomial(Fraction(1, power + 1), down_monomial(power, r))


def operator_matrix(max_degree: int, r: int) -> list[list[Fraction]]:
    matrix = [
        [Fraction(0) for _ in range(max_degree + 1)]
        for _ in range(max_degree + 1)
    ]
    for column in range(max_degree + 1):
        polynomial = up_down_monomial(column, r)
        for row, coefficient in enumerate(polynomial):
            matrix[row][column] = coefficient
    return matrix


def matmul(left: list[list[Fraction]], right: list[list[Fraction]]) -> list[list[Fraction]]:
    rows = len(left)
    inner = len(right)
    columns = len(right[0])
    return [
        [
            sum((left[i][k] * right[k][j] for k in range(inner)), Fraction(0))
            for j in range(columns)
        ]
        for i in range(rows)
    ]


def transpose(matrix: list[list[Fraction]]) -> list[list[Fraction]]:
    return [list(row) for row in zip(*matrix)]


def gram_matrix(max_degree: int, r: int) -> list[list[Fraction]]:
    return [
        [beta_one_r_moment(i + j, r) for j in range(max_degree + 1)]
        for i in range(max_degree + 1)
    ]


def check_spectrum() -> None:
    for r in range(2, 10):
        for max_degree in range(1, 8):
            matrix = operator_matrix(max_degree, r)
            # Degree filtration is preserved, so entries above the degree of
            # the input monomial vanish.
            for column in range(max_degree + 1):
                for row in range(column + 1, max_degree + 1):
                    assert matrix[row][column] == 0
                expected = Fraction(r - 1, (column + 1) * (r + column - 1))
                assert matrix[column][column] == expected

            # Self-adjointness in L^2(Beta(1,r)): G T = T^T G.
            gram = gram_matrix(max_degree, r)
            assert matmul(gram, matrix) == matmul(transpose(matrix), gram)

        first_nonconstant = Fraction(r - 1, 2 * r)
        assert first_nonconstant < Fraction(1, 2)
        for degree in range(2, 12):
            eigenvalue = Fraction(r - 1, (degree + 1) * (r + degree - 1))
            assert eigenvalue < first_nonconstant


def integrate_polynomial(polynomial: Polynomial, upper: Fraction) -> Fraction:
    return sum(
        (coefficient * upper ** (degree + 1) / (degree + 1)
         for degree, coefficient in enumerate(polynomial)),
        Fraction(0),
    )


def one_minus_x_power(power: int) -> Polynomial:
    return [Fraction(comb(power, j) * ((-1) ** j)) for j in range(power + 1)]


def check_overlap() -> None:
    for r in range(2, 15):
        # nu-lambda = r(1-s)^(r-2)(1-rs).
        base = one_minus_x_power(r - 2)
        difference = [Fraction(0) for _ in range(r)]
        for degree, coefficient in enumerate(base):
            difference[degree] += r * coefficient
            difference[degree + 1] -= r * r * coefficient
        crossing = Fraction(1, r)
        defect = integrate_polynomial(difference, crossing)
        expected = Fraction(r - 1, r) ** (r - 1)
        assert defect == expected
        assert 0 < defect < 1


def check_parity_edge_identity() -> None:
    samples = [
        (0, Fraction(2, 3), Fraction(-7, 5)),
        (1, Fraction(11, 4), Fraction(3, 8)),
        (6, Fraction(-5, 9), Fraction(13, 7)),
    ]
    for shell, parent, child in samples:
        twisted_parent = ((-1) ** shell) * parent
        twisted_child = ((-1) ** (shell + 1)) * child
        gradient = twisted_child - twisted_parent
        signless = ((-1) ** (shell + 1)) * (child + parent)
        assert gradient == signless
        assert gradient**2 == (child + parent) ** 2


def main() -> None:
    check_spectrum()
    check_overlap()
    check_parity_edge_identity()
    print("parity-twisted radial shell incidence: exact checks passed")


if __name__ == "__main__":
    main()
