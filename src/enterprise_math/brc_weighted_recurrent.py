"""Exact finite recurrent positive Weighted-BRC mass calculus.

This module implements the finite non-negative rational recurrence layer proved
in PR #1112.  It uses Fraction arithmetic only.  Spectral/eigenvalue routines
are intentionally not part of the decision path.

The matrix records the positive *total-mass* projection.  Signed/amplitude
cancellation and infinite-state recurrence remain outside this interface.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd, lcm
from typing import Iterable, Sequence

RationalInput = int | Fraction
RationalMatrixInput = Sequence[Sequence[RationalInput]]
RationalMatrix = tuple[tuple[Fraction, ...], ...]
RationalVector = tuple[Fraction, ...]
IntegerMatrix = tuple[tuple[int, ...], ...]


def _fraction(value: RationalInput) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, Fraction)):
        raise TypeError("matrix entries must be int or Fraction")
    return Fraction(value)


def _mass_matrix(matrix: RationalMatrixInput) -> RationalMatrix:
    rows = tuple(tuple(_fraction(value) for value in row) for row in matrix)
    n = len(rows)
    if n == 0 or any(len(row) != n for row in rows):
        raise ValueError("mass matrix must be nonempty and square")
    if any(value < 0 for row in rows for value in row):
        raise ValueError("mass matrix entries must be non-negative")
    return rows


def _square_matrix(matrix: Sequence[Sequence[Fraction]]) -> RationalMatrix:
    rows = tuple(tuple(Fraction(value) for value in row) for row in matrix)
    n = len(rows)
    if n == 0 or any(len(row) != n for row in rows):
        raise ValueError("matrix must be nonempty and square")
    return rows


def _identity(n: int) -> RationalMatrix:
    return tuple(
        tuple(Fraction(int(i == j), 1) for j in range(n))
        for i in range(n)
    )


def _subtract(left: RationalMatrix, right: RationalMatrix) -> RationalMatrix:
    n = len(left)
    return tuple(
        tuple(left[i][j] - right[i][j] for j in range(n))
        for i in range(n)
    )


def _multiply(left: RationalMatrix, right: RationalMatrix) -> RationalMatrix:
    n = len(left)
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(n)), Fraction(0, 1))
            for j in range(n)
        )
        for i in range(n)
    )


def _inverse(matrix: RationalMatrix) -> RationalMatrix | None:
    matrix = _square_matrix(matrix)
    n = len(matrix)
    aug = [
        list(matrix[i]) + [Fraction(int(i == j), 1) for j in range(n)]
        for i in range(n)
    ]
    for col in range(n):
        pivot = next((row for row in range(col, n) if aug[row][col] != 0), None)
        if pivot is None:
            return None
        aug[col], aug[pivot] = aug[pivot], aug[col]
        pivot_value = aug[col][col]
        aug[col] = [value / pivot_value for value in aug[col]]
        for row in range(n):
            if row == col:
                continue
            factor = aug[row][col]
            if factor != 0:
                aug[row] = [
                    aug[row][j] - factor * aug[col][j]
                    for j in range(2 * n)
                ]
    return tuple(tuple(row[n:]) for row in aug)


def _matrix_vector(matrix: RationalMatrix, vector: RationalVector) -> RationalVector:
    n = len(matrix)
    if len(vector) != n:
        raise ValueError("vector dimension must match matrix")
    return tuple(
        sum((matrix[i][j] * vector[j] for j in range(n)), Fraction(0, 1))
        for i in range(n)
    )


def _row_sums(matrix: RationalMatrix) -> RationalVector:
    return tuple(sum(row, Fraction(0, 1)) for row in matrix)


def _common_denominator(matrix: RationalMatrix) -> int:
    result = 1
    for row in matrix:
        for value in row:
            result = lcm(result, value.denominator)
    return result


def _integer_mass_matrix(matrix: RationalMatrix, denominator: int) -> IntegerMatrix:
    return tuple(
        tuple(int(value * denominator) for value in row)
        for row in matrix
    )


def _primitive_positive_integer_vector(vector: RationalVector) -> tuple[int, ...]:
    if any(value <= 0 for value in vector):
        raise ValueError("vector must be strictly positive")
    denominator = 1
    for value in vector:
        denominator = lcm(denominator, value.denominator)
    integers = [int(value * denominator) for value in vector]
    common = 0
    for value in integers:
        common = gcd(common, value)
    if common > 1:
        integers = [value // common for value in integers]
    return tuple(integers)


def recurrent_mass_power(matrix: RationalMatrixInput, exponent: int) -> RationalMatrix:
    """Return the exact length-``exponent`` total-walk-mass matrix ``W^k``."""
    mass = _mass_matrix(matrix)
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
        raise ValueError("exponent must be a non-negative integer")
    result = _identity(len(mass))
    base = mass
    power = exponent
    while power:
        if power & 1:
            result = _multiply(result, base)
        base = _multiply(base, base)
        power >>= 1
    return result


def gauge_recurrent_mass_matrix(
    matrix: RationalMatrixInput,
    potential: Iterable[RationalInput],
) -> RationalMatrix:
    """Apply the state gauge ``B_ij=W_ij*h_j/h_i``."""
    mass = _mass_matrix(matrix)
    h = tuple(_fraction(value) for value in potential)
    n = len(mass)
    if len(h) != n or any(value <= 0 for value in h):
        raise ValueError("potential must be a positive vector matching the matrix")
    return tuple(
        tuple(mass[i][j] * h[j] / h[i] for j in range(n))
        for i in range(n)
    )


def verify_recurrent_integer_stable_certificate(
    matrix: RationalMatrixInput,
    certificate: Sequence[int],
) -> bool:
    """Verify ``A h < D h`` after exact common-denominator clearing."""
    mass = _mass_matrix(matrix)
    if (
        len(certificate) != len(mass)
        or any(isinstance(value, bool) or not isinstance(value, int) or value <= 0 for value in certificate)
    ):
        return False
    denominator = _common_denominator(mass)
    integer_matrix = _integer_mass_matrix(mass, denominator)
    for i in range(len(mass)):
        lhs = sum(integer_matrix[i][j] * certificate[j] for j in range(len(mass)))
        if lhs >= denominator * certificate[i]:
            return False
    return True


def verify_recurrent_integer_divergence_certificate(
    matrix: RationalMatrixInput,
    certificate: Sequence[int],
) -> bool:
    """Verify a nonzero ``y>=0`` with ``y^T A >= D y^T``."""
    mass = _mass_matrix(matrix)
    if (
        len(certificate) != len(mass)
        or any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in certificate)
        or not any(certificate)
    ):
        return False
    y = tuple(Fraction(value, 1) for value in certificate)
    for j in range(len(mass)):
        stepped = sum((y[i] * mass[i][j] for i in range(len(mass))), Fraction(0, 1))
        if stepped < y[j]:
            return False
    return True


@dataclass(frozen=True)
class FiniteRecurrentMassAnalysis:
    """Exact stable/unstable classification for finite rational total mass."""

    mass_matrix: RationalMatrix
    stable: bool
    common_denominator: int
    integer_mass_matrix: IntegerMatrix
    star: RationalMatrix | None
    canonical_potential: RationalVector | None
    primitive_integer_potential: tuple[int, ...] | None
    gauged_mass_matrix: RationalMatrix | None
    gauged_row_sums: RationalVector | None

    def verify_stable_certificate(self) -> bool:
        if not self.stable or self.primitive_integer_potential is None:
            return False
        return verify_recurrent_integer_stable_certificate(
            self.mass_matrix,
            self.primitive_integer_potential,
        )


def finite_recurrent_mass_analysis(matrix: RationalMatrixInput) -> FiniteRecurrentMassAnalysis:
    """Classify a finite non-negative rational recurrent total-mass matrix.

    Stability is decided exactly through the positive rational potential
    ``x=(I-W)^(-1) 1``.  On the stable side ``star`` is the exact Neumann star
    ``(I-W)^(-1)``.  On the unstable side no object is mislabeled as a star.
    """
    mass = _mass_matrix(matrix)
    n = len(mass)
    denominator = _common_denominator(mass)
    integer_matrix = _integer_mass_matrix(mass, denominator)
    resolvent = _subtract(_identity(n), mass)
    inverse = _inverse(resolvent)
    if inverse is None:
        return FiniteRecurrentMassAnalysis(
            mass, False, denominator, integer_matrix, None, None, None, None, None
        )

    potential = _row_sums(inverse)
    if any(value <= 0 for value in potential):
        return FiniteRecurrentMassAnalysis(
            mass, False, denominator, integer_matrix, None, None, None, None, None
        )

    # Positive potential is already the exact stability certificate.  The
    # inverse must therefore be the non-negative Neumann star.
    if any(value < 0 for row in inverse for value in row):
        raise AssertionError("positive recurrent potential produced a negative star entry")
    stepped = _matrix_vector(mass, potential)
    if stepped != tuple(value - 1 for value in potential):
        raise AssertionError("canonical recurrent potential identity failed")

    primitive = _primitive_positive_integer_vector(potential)
    if not verify_recurrent_integer_stable_certificate(mass, primitive):
        raise AssertionError("primitive integer potential failed its exact certificate")
    gauged = gauge_recurrent_mass_matrix(mass, potential)
    gauged_rows = _row_sums(gauged)
    if any(value >= 1 for value in gauged_rows):
        raise AssertionError("canonical gauge must be row-subcritical")

    return FiniteRecurrentMassAnalysis(
        mass,
        True,
        denominator,
        integer_matrix,
        inverse,
        potential,
        primitive,
        gauged,
        gauged_rows,
    )
