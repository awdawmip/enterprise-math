"""Exact C3 -> C6 -> C12 rotation-bisector certificates.

This module works in the quadratic field Q(r), r^2 = 1/3, and with exact
2-by-2 matrices.  It proves by computation that the three-ray right-turn
operator R internally generates a six-state rotor G = I + R, while the Cell
radius r = 1/sqrt(3) uniquely normalizes the adjacent-state sum
H = r(I + G) into a twelve-state rotor.  The quarter-turn operator is
J = H^3 = r(R - R^-1), and J^2 = -I.

The unit orientation character H must be distinguished from the physical gate
displacement.  The latter is rH = (I+G)/3, the centroid/circumcenter vector of
the elementary unit center triangle.

No trigonometric function and no numerical value of pi is used.  The matrices
are a derived rotation-character representation; they are not a replacement
for the native Enterprise length algebra.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import TypeAlias


@dataclass(frozen=True)
class QRadial:
    """An exact element a + b*r of Q(r), where r^2 = 1/3."""

    rational: Fraction = Fraction(0)
    radial: Fraction = Fraction(0)

    @staticmethod
    def coerce(value: "QRadial | Fraction | int") -> "QRadial":
        if isinstance(value, QRadial):
            return value
        return QRadial(Fraction(value), Fraction(0))

    def __add__(self, other: "QRadial | Fraction | int") -> "QRadial":
        value = self.coerce(other)
        return QRadial(
            self.rational + value.rational,
            self.radial + value.radial,
        )

    __radd__ = __add__

    def __neg__(self) -> "QRadial":
        return QRadial(-self.rational, -self.radial)

    def __sub__(self, other: "QRadial | Fraction | int") -> "QRadial":
        return self + (-self.coerce(other))

    def __rsub__(self, other: "QRadial | Fraction | int") -> "QRadial":
        return self.coerce(other) - self

    def __mul__(self, other: "QRadial | Fraction | int") -> "QRadial":
        value = self.coerce(other)
        return QRadial(
            self.rational * value.rational
            + self.radial * value.radial / 3,
            self.rational * value.radial
            + self.radial * value.rational,
        )

    __rmul__ = __mul__

    def conjugate(self) -> "QRadial":
        return QRadial(self.rational, -self.radial)

    def norm(self) -> Fraction:
        return self.rational * self.rational - self.radial * self.radial / 3

    def inverse(self) -> "QRadial":
        norm = self.norm()
        if norm == 0:
            raise ZeroDivisionError("cannot invert a zero-norm QRadial value")
        conjugate = self.conjugate()
        return QRadial(conjugate.rational / norm, conjugate.radial / norm)

    def __truediv__(self, other: "QRadial | Fraction | int") -> "QRadial":
        return self * self.coerce(other).inverse()

    def __pow__(self, exponent: int) -> "QRadial":
        if isinstance(exponent, bool) or not isinstance(exponent, int):
            raise ValueError("exponent must be an integer")
        if exponent < 0:
            return self.inverse() ** (-exponent)
        result = self.coerce(1)
        base = self
        while exponent:
            if exponent & 1:
                result = result * base
            base = base * base
            exponent >>= 1
        return result


Matrix2: TypeAlias = tuple[
    tuple[QRadial, QRadial],
    tuple[QRadial, QRadial],
]


def radial() -> QRadial:
    """The positive Cell-radius symbol r with exact square r^2=1/3."""
    return QRadial(Fraction(0), Fraction(1))


def matrix(a: QRadial | Fraction | int, b: QRadial | Fraction | int,
           c: QRadial | Fraction | int, d: QRadial | Fraction | int) -> Matrix2:
    q = QRadial.coerce
    return ((q(a), q(b)), (q(c), q(d)))


IDENTITY: Matrix2 = matrix(1, 0, 0, 1)
ZERO: Matrix2 = matrix(0, 0, 0, 0)
RIGHT_TURN: Matrix2 = matrix(0, -1, 1, -1)
GRAM: Matrix2 = matrix(2, -1, -1, 2)


def matrix_add(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(left[row][column] + right[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_neg(value: Matrix2) -> Matrix2:
    return tuple(
        tuple(-value[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_sub(left: Matrix2, right: Matrix2) -> Matrix2:
    return matrix_add(left, matrix_neg(right))


def matrix_scale(scalar: QRadial | Fraction | int, value: Matrix2) -> Matrix2:
    scalar = QRadial.coerce(scalar)
    return tuple(
        tuple(scalar * value[row][column] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_mul(left: Matrix2, right: Matrix2) -> Matrix2:
    return tuple(
        tuple(
            sum(
                (left[row][index] * right[index][column] for index in range(2)),
                QRadial.coerce(0),
            )
            for column in range(2)
        )
        for row in range(2)
    )  # type: ignore[return-value]


def matrix_pow(value: Matrix2, exponent: int) -> Matrix2:
    if isinstance(exponent, bool) or not isinstance(exponent, int) or exponent < 0:
        raise ValueError("matrix exponent must be a non-negative integer")
    result = IDENTITY
    base = value
    while exponent:
        if exponent & 1:
            result = matrix_mul(result, base)
        base = matrix_mul(base, base)
        exponent >>= 1
    return result


def matrix_transpose(value: Matrix2) -> Matrix2:
    return tuple(
        tuple(value[column][row] for column in range(2))
        for row in range(2)
    )  # type: ignore[return-value]


def gram_pullback(value: Matrix2) -> Matrix2:
    """Return value^T * GRAM * value."""
    return matrix_mul(matrix_mul(matrix_transpose(value), GRAM), value)


def six_state_rotor() -> Matrix2:
    """The internally generated short square root G=I+R of the C3 right turn."""
    return matrix_add(IDENTITY, RIGHT_TURN)


def gate_rotor() -> Matrix2:
    """The unit gate-ray orientation character H=r(I+G)."""
    return matrix_scale(radial(), matrix_add(IDENTITY, six_state_rotor()))


def physical_gate_displacement() -> Matrix2:
    """Physical gate displacement: Cell radius times its unit orientation."""
    return matrix_scale(radial(), gate_rotor())


def physical_gate_centroid_form() -> Matrix2:
    """The same displacement as one third of the adjacent center-vector sum."""
    return matrix_scale(
        Fraction(1, 3),
        matrix_add(IDENTITY, six_state_rotor()),
    )


def quarter_turn() -> Matrix2:
    """The gate-level quarter-turn J=H^3."""
    return matrix_pow(gate_rotor(), 3)


def chiral_difference() -> Matrix2:
    """The Cell-radius-normalized difference r(R-R^-1)."""
    return matrix_scale(
        radial(),
        matrix_sub(RIGHT_TURN, matrix_pow(RIGHT_TURN, 2)),
    )


def adjacent_sum_gram() -> Matrix2:
    """Gram pullback of I+G; exactly three times the invariant Gram form."""
    return gram_pullback(matrix_add(IDENTITY, six_state_rotor()))


def gate_normalizer_square() -> Fraction:
    """Unique positive squared scalar making I+G a GRAM-isometry."""
    return Fraction(1, 3)


def interleaved_phase_states() -> tuple[Matrix2, ...]:
    """The twelve exact Cell-direction/gate character states H^0,...,H^11."""
    rotor = gate_rotor()
    return tuple(matrix_pow(rotor, index) for index in range(12))


@dataclass(frozen=True)
class NativeBisectorCertificate:
    radial_square: QRadial
    right_turn_cube: Matrix2
    right_turn_relation: Matrix2
    six_square: Matrix2
    six_cube: Matrix2
    six_sixth: Matrix2
    gate_square: Matrix2
    gate_cube: Matrix2
    gate_sixth: Matrix2
    gate_twelfth: Matrix2
    physical_gate: Matrix2
    physical_gate_centroid: Matrix2
    quarter_chiral: Matrix2
    quarter_square: Matrix2
    adjacent_gram: Matrix2
    distinct_phase_states: int

    @property
    def valid(self) -> bool:
        return (
            self.radial_square == QRadial.coerce(Fraction(1, 3))
            and self.right_turn_cube == IDENTITY
            and self.right_turn_relation == ZERO
            and self.six_square == RIGHT_TURN
            and self.six_cube == matrix_neg(IDENTITY)
            and self.six_sixth == IDENTITY
            and self.gate_square == six_state_rotor()
            and self.gate_cube == quarter_turn()
            and self.gate_sixth == matrix_neg(IDENTITY)
            and self.gate_twelfth == IDENTITY
            and self.physical_gate == self.physical_gate_centroid
            and self.quarter_chiral == quarter_turn()
            and self.quarter_square == matrix_neg(IDENTITY)
            and self.adjacent_gram == matrix_scale(3, GRAM)
            and self.distinct_phase_states == 12
        )


def native_bisector_certificate() -> NativeBisectorCertificate:
    """Return the complete exact C3 -> C6 -> C12 theorem certificate."""
    right_square = matrix_pow(RIGHT_TURN, 2)
    six = six_state_rotor()
    gate = gate_rotor()
    quarter = quarter_turn()
    states = interleaved_phase_states()
    return NativeBisectorCertificate(
        radial_square=radial() * radial(),
        right_turn_cube=matrix_pow(RIGHT_TURN, 3),
        right_turn_relation=matrix_add(matrix_add(IDENTITY, RIGHT_TURN), right_square),
        six_square=matrix_pow(six, 2),
        six_cube=matrix_pow(six, 3),
        six_sixth=matrix_pow(six, 6),
        gate_square=matrix_pow(gate, 2),
        gate_cube=matrix_pow(gate, 3),
        gate_sixth=matrix_pow(gate, 6),
        gate_twelfth=matrix_pow(gate, 12),
        physical_gate=physical_gate_displacement(),
        physical_gate_centroid=physical_gate_centroid_form(),
        quarter_chiral=chiral_difference(),
        quarter_square=matrix_pow(quarter, 2),
        adjacent_gram=adjacent_sum_gram(),
        distinct_phase_states=len(set(states)),
    )


def all_rotors_preserve_gram() -> bool:
    """Check R, G, H, and J against the same exact invariant form."""
    return all(
        gram_pullback(value) == GRAM
        for value in (RIGHT_TURN, six_state_rotor(), gate_rotor(), quarter_turn())
    )


def interleaving_identity() -> bool:
    """Even H-powers are directions G^j; odd H-powers are intervening gates."""
    gate = gate_rotor()
    six = six_state_rotor()
    return all(
        matrix_pow(gate, 2 * index) == matrix_pow(six, index)
        and matrix_pow(gate, 2 * index + 1)
        == matrix_mul(gate, matrix_pow(six, index))
        for index in range(6)
    )
