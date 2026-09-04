#!/usr/bin/env python3
"""Exact checks for the V18 positive-recanonicalization barrier.

All theorem-level arithmetic uses ``fractions.Fraction``. The checker
contains no floating prime-distribution experiment and promotes no
unproved arithmetic asymptotic.
"""

from __future__ import annotations

from fractions import Fraction


Matrix = list[list[Fraction]]


def matmul(left: Matrix, right: Matrix) -> Matrix:
    return [
        [
            sum(
                (left[i][k] * right[k][j] for k in range(len(right))),
                Fraction(0),
            )
            for j in range(len(right[0]))
        ]
        for i in range(len(left))
    ]


def matrix_power(matrix: Matrix, exponent: int) -> Matrix:
    if exponent < 0:
        raise ValueError("exponent must be nonnegative")
    size = len(matrix)
    result = [
        [Fraction(int(i == j)) for j in range(size)]
        for i in range(size)
    ]
    base = matrix
    power = exponent
    while power:
        if power & 1:
            result = matmul(result, base)
        base = matmul(base, base)
        power //= 2
    return result


def mellin_entries(
    beta: Fraction,
    gamma: Fraction = Fraction(1, 9),
) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    one = Fraction(1)
    if not (Fraction(0) <= beta < one):
        raise ValueError("beta must lie in [0,1)")
    a = (
        one / (one - beta)
        - 4 * one / (2 - beta)
        + 4 * one / (3 - beta)
    )
    b = one / (2 - beta)
    d = 4 * (
        one / (2 - beta)
        - one / (3 - beta)
    )
    c = gamma * d
    return a, b, c, d


def delayed_coefficients(
    beta: Fraction,
    depth: int,
    gamma: Fraction = Fraction(1, 9),
) -> tuple[Fraction, Fraction]:
    a, b, c, _ = mellin_entries(beta, gamma)
    matrix = [[a, Fraction(0)], [c, b]]
    power = matrix_power(matrix, depth)

    # Terminal norm L_(1/gamma)(R,V) = R + V/gamma.
    root_ratio = power[0][0] + power[1][0] / gamma
    standard_ratio = power[1][1]
    return root_ratio, standard_ratio


def check_local_partition() -> None:
    for numerator in range(0, 25):
        s = Fraction(numerator, 24)
        theta = 1 - 2 * s
        assert theta**2 + 4 * s * (1 - s) == 1


def check_universal_one_step_no_go() -> None:
    for beta in (
        Fraction(0),
        Fraction(1, 5),
        Fraction(2, 5),
        Fraction(1, 2),
    ):
        a, _, _, d = mellin_entries(beta)
        assert a + d == 1 / (1 - beta)
        if beta == 0:
            assert a + d == 1
        else:
            assert a + d > 1

    # Balanced-row equality witness. Any root-recovery weight must obey
    # lambda * gamma >= 1.
    gamma = Fraction(1, 9)
    s = Fraction(1, 2)
    root = Fraction(7, 5)
    output_mean = (1 - 2 * s) ** 2 * root
    output_standard = 4 * gamma * s * (1 - s) * root
    assert output_mean == 0
    assert output_standard == gamma * root
    assert output_mean + Fraction(9) * output_standard == root


def check_delay_two_fifths() -> None:
    beta = Fraction(2, 5)
    a, b, _, d = mellin_entries(beta)
    assert a == Fraction(55, 78)
    assert b == Fraction(5, 8)
    assert d == Fraction(25, 26)

    root5, _ = delayed_coefficients(beta, 5)
    root6, standard6 = delayed_coefficients(beta, 6)

    assert root5 == Fraction(63775271875, 56855126016)
    assert root5 > 1
    assert root6 == Fraction(15657198015625, 17738799316992)
    assert root6 < 1
    assert standard6 == Fraction(15625, 262144)
    assert standard6 < root6

    # Exact positive-cone test on a grid of nonnegative states.
    for root in map(Fraction, range(8)):
        for standard in map(Fraction, range(8)):
            input_norm = root + 9 * standard
            output_norm = root6 * root + 9 * standard6 * standard
            assert output_norm <= root6 * input_norm


def check_delay_one_half() -> None:
    beta = Fraction(1, 2)
    a, b, _, d = mellin_entries(beta)
    assert a == Fraction(14, 15)
    assert b == Fraction(2, 3)
    assert d == Fraction(16, 15)

    root23, _ = delayed_coefficients(beta, 23)
    root24, standard24 = delayed_coefficients(beta, 24)

    assert root23 == Fraction(
        76501897628993831827406848,
        74818276426792144775390625,
    )
    assert root23 > 1
    assert root24 == Fraction(
        3213399700417740936751087616,
        3366822439205646514892578125,
    )
    assert root24 < 1
    assert standard24 == Fraction(16777216, 282429536481)
    assert standard24 < root24

    # Closed form d_k = 5(14/15)^k - 4(2/3)^k.
    for depth in range(1, 30):
        root_ratio, _ = delayed_coefficients(beta, depth)
        closed = 5 * a**depth - 4 * b**depth
        assert root_ratio == closed


def check_every_subcritical_test_has_delay() -> None:
    # Rational samples below the critical root 0.522... .
    for beta in (
        Fraction(0),
        Fraction(1, 4),
        Fraction(1, 3),
        Fraction(2, 5),
        Fraction(9, 20),
        Fraction(1, 2),
    ):
        found = False
        for depth in range(1, 80):
            root_ratio, standard_ratio = delayed_coefficients(beta, depth)
            if root_ratio < 1 and standard_ratio < 1:
                found = True
                break
        assert found, beta


def main() -> None:
    check_local_partition()
    check_universal_one_step_no_go()
    check_delay_two_fifths()
    check_delay_one_half()
    check_every_subcritical_test_has_delay()
    print("V18 delayed recanonicalization: exact checks passed")


if __name__ == "__main__":
    main()
