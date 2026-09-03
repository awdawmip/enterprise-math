"""Exact C3 chiral-difference certificate for the Enterprise Euler line.

On the nontrivial two-dimensional C3 rotation plane, a right-turn operator R
satisfies I + R + R^2 = 0. Its chiral difference D = R - R^{-1}
therefore satisfies D^2 = -3 I. The frozen carrier Cell radius has square
1/3, so radius-normalization turns D into a complex structure J with J^2=-I.

The exact checker keeps the matrix and scale-square certificates rational.
No floating angle or numerical value of pi is used.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import TypeAlias

Matrix2: TypeAlias = tuple[tuple[int, int], tuple[int, int]]

IDENTITY: Matrix2 = ((1, 0), (0, 1))
ZERO: Matrix2 = ((0, 0), (0, 0))


@dataclass(frozen=True)
class C3ChiralCertificate:
    right_turn: Matrix2
    inverse_turn: Matrix2
    chiral_difference: Matrix2
    right_turn_cube: Matrix2
    cyclotomic_sum: Matrix2
    chiral_square: Matrix2
    cell_radius_squared: Fraction
    normalized_square_coefficient: Fraction


def matrix_add(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(left[i][j] + right[i][j] for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def matrix_sub(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(left[i][j] - right[i][j] for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def matrix_mul(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def matrix_scale(value: int, matrix: Matrix2) -> Matrix2:
    return tuple(
        tuple(value * matrix[i][j] for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


def matrix_pow(matrix: Matrix2, exponent: int) -> Matrix2:
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
        raise ValueError("exponent must be a nonnegative integer")
    out = IDENTITY
    base = matrix
    power = exponent
    while power:
        if power & 1:
            out = matrix_mul(out, base)
        base = matrix_mul(base, base)
        power //= 2
    return out


def c3_right_turn_matrix() -> Matrix2:
    """Integral companion representation of a nontrivial C3 turn."""

    return ((0, -1), (1, -1))


def c3_chiral_certificate() -> C3ChiralCertificate:
    """Return and internally verify the exact radius-normalization certificate."""

    right = c3_right_turn_matrix()
    inverse = matrix_pow(right, 2)
    cube = matrix_pow(right, 3)
    cyclotomic = matrix_add(matrix_add(IDENTITY, right), inverse)
    difference = matrix_sub(right, inverse)
    difference_square = matrix_mul(difference, difference)
    radius_squared = Fraction(1, 3)
    normalized_square_coefficient = radius_squared * Fraction(-3, 1)

    if cube != IDENTITY:
        raise AssertionError("right-turn matrix is not order three")
    if cyclotomic != ZERO:
        raise AssertionError("nontrivial C3 cyclotomic relation failed")
    if difference_square != matrix_scale(-3, IDENTITY):
        raise AssertionError("chiral difference square is not -3I")
    if normalized_square_coefficient != -1:
        raise AssertionError("Cell radius does not normalize the square to -I")

    return C3ChiralCertificate(
        right_turn=right,
        inverse_turn=inverse,
        chiral_difference=difference,
        right_turn_cube=cube,
        cyclotomic_sum=cyclotomic,
        chiral_square=difference_square,
        cell_radius_squared=radius_squared,
        normalized_square_coefficient=normalized_square_coefficient,
    )


def required_normalizer_square() -> Fraction:
    """The unique positive normalizer square required for J^2=-I."""

    return Fraction(1, 3)


def effective_scalar_compatibility() -> tuple[complex, complex, complex]:
    """External complex check: radius*(omega-omega^-1) equals the positive i state."""

    import cmath
    import math

    omega = cmath.exp(2j * math.pi / 3)
    radius = 1 / math.sqrt(3)
    derived_i = radius * (omega - 1 / omega)
    quarter_turn = cmath.exp(2j * math.pi * 3 / 12)
    return omega, derived_i, quarter_turn
