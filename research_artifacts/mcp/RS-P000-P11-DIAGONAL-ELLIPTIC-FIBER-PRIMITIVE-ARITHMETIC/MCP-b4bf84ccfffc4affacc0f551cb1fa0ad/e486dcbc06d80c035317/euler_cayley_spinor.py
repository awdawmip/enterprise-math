"""Exact Pythagorean-spinor and Cayley rotation certificates.

The source state is a nonzero integer or rational pair (a,b), interpreted as a
projective half-angle/spinor coordinate. Its rotation character is

    ((a^2-b^2) + J(2ab)) / (a^2+b^2),  J^2=-1.

All core routines use exact integers and fractions. No trigonometric function
and no numerical value of pi is imported. The target character algebra is a
derived rotation readout, not the native Enterprise length algebra.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from typing import TypeAlias

Spinor: TypeAlias = tuple[int, int]
Character: TypeAlias = tuple[Fraction, Fraction]


def _integer(value: int, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")
    return value


def primitive_spinor(a: int, b: int) -> Spinor:
    """Normalize a nonzero integer pair modulo nonzero rational scale and sign."""
    a = _integer(a, "a")
    b = _integer(b, "b")
    if a == 0 and b == 0:
        raise ValueError("spinor pair must be nonzero")
    common = gcd(abs(a), abs(b))
    a //= common
    b //= common
    if a < 0 or (a == 0 and b < 0):
        a, b = -a, -b
    return a, b


def spinor_norm_squared(spinor: Spinor) -> int:
    """Native Pythagorean norm-square of an integer spinor pair."""
    a, b = primitive_spinor(*spinor)
    return a * a + b * b


def spinor_conjugate(spinor: Spinor) -> Spinor:
    """Projective conjugation, corresponding to reversing rotation orientation."""
    a, b = primitive_spinor(*spinor)
    return primitive_spinor(a, -b)


def spinor_product(left: Spinor, right: Spinor) -> Spinor:
    """Gaussian/projective composition (a+Jb)(c+Jd), with J^2=-1."""
    a, b = primitive_spinor(*left)
    c, d = primitive_spinor(*right)
    return primitive_spinor(a * c - b * d, a * d + b * c)


def spinor_power(spinor: Spinor, exponent: int) -> Spinor:
    """Exact integral projective power."""
    exponent = _integer(exponent, "exponent")
    if exponent < 0:
        return spinor_power(spinor_conjugate(spinor), -exponent)
    result = (1, 0)
    base = primitive_spinor(*spinor)
    while exponent:
        if exponent & 1:
            result = spinor_product(result, base)
        base = spinor_product(base, base)
        exponent >>= 1
    return result


def rotation_triple(spinor: Spinor) -> tuple[int, int, int]:
    """Return the exact Pythagorean triple (a^2-b^2, 2ab, a^2+b^2)."""
    a, b = primitive_spinor(*spinor)
    return a * a - b * b, 2 * a * b, a * a + b * b


def rotation_character(spinor: Spinor) -> Character:
    """Unit character coordinates associated with a projective spinor."""
    x, y, radius = rotation_triple(spinor)
    return Fraction(x, radius), Fraction(y, radius)


def character_product(left: Character, right: Character) -> Character:
    """Multiplication in the formal J-plane, J^2=-1."""
    x, y = left
    u, v = right
    return x * u - y * v, x * v + y * u


def character_conjugate(value: Character) -> Character:
    x, y = value
    return x, -y


def character_norm_squared(value: Character) -> Fraction:
    x, y = value
    return x * x + y * y


def compose_certificate(left: Spinor, right: Spinor) -> tuple[Character, Character]:
    """Both sides of rot(left*right)=rot(left)rot(right)."""
    return (
        rotation_character(spinor_product(left, right)),
        character_product(rotation_character(left), rotation_character(right)),
    )


def cayley_spinor(parameter: Fraction | int | None) -> Spinor:
    """Projective spinor for a Cayley half-angle parameter.

    ``None`` denotes the projective point at infinity and maps to the half-turn.
    """
    if parameter is None:
        return 0, 1
    parameter = Fraction(parameter)
    return primitive_spinor(parameter.denominator, parameter.numerator)


def cayley_parameter(spinor: Spinor) -> Fraction | None:
    """Recover b/a, with ``None`` for the projective point at infinity."""
    a, b = primitive_spinor(*spinor)
    if a == 0:
        return None
    return Fraction(b, a)


def cayley_character(parameter: Fraction | int | None) -> Character:
    """Exact Cayley character ((1-t^2)/(1+t^2), 2t/(1+t^2))."""
    return rotation_character(cayley_spinor(parameter))


def cayley_compose(
    left: Fraction | int | None, right: Fraction | int | None
) -> Fraction | None:
    """Projective composition without angle or inverse trigonometry."""
    return cayley_parameter(
        spinor_product(cayley_spinor(left), cayley_spinor(right))
    )


def spinor_from_rational_character(x: Fraction | int, y: Fraction | int) -> Spinor:
    """Inverse rational parametrization of x^2+y^2=1."""
    x = Fraction(x)
    y = Fraction(y)
    if x * x + y * y != 1:
        raise ValueError("character must lie on the rational unit circle")
    if x == -1:
        return 0, 1
    a = 1 + x
    b = y
    common = a.denominator * b.denominator
    return primitive_spinor(int(a * common), int(b * common))


def quarter_turn_spinors() -> tuple[Spinor, Spinor]:
    """The two projective roots of the half-turn."""
    return (1, 1), (1, -1)


def verify_quarter_turn_certificate() -> bool:
    positive, negative = quarter_turn_spinors()
    half = rotation_character((0, 1))
    return (
        character_product(rotation_character(positive), rotation_character(positive))
        == half
        and character_product(rotation_character(negative), rotation_character(negative))
        == half
        and rotation_character(positive) == (Fraction(0), Fraction(1))
        and rotation_character(negative) == (Fraction(0), Fraction(-1))
    )


@dataclass(frozen=True)
class PellCayleyCertificate:
    p: int
    q: int
    d: int
    pell_value: int
    radial_square: int
    inverse_product_coefficients: tuple[int, int, int]
    character_x_square: tuple[int, int]
    character_y_square: tuple[int, int]

    @property
    def valid(self) -> bool:
        return (
            self.pell_value == -1
            and self.radial_square == self.p * self.p + 1
            and self.inverse_product_coefficients == (1, 0, 0)
            and self.character_x_square
            == (self.p * self.p * self.radial_square, self.radial_square**2)
            and self.character_y_square
            == (self.radial_square, self.radial_square**2)
        )


def pell_cayley_certificate(p: int, q: int, d: int) -> PellCayleyCertificate:
    """Certify the near-axis negative-Pell segment p^2+1=d*q^2.

    The Cayley parameter is tau=q*sqrt(d)-p. Symbolically:
      tau*(q*sqrt(d)+p)=1,
      Cayley(tau)=(p/(q*sqrt(d)), 1/(q*sqrt(d))).
    The returned integer fields certify the polynomial identities after
    squaring and comparing rational/radical coefficients.
    """
    p = _integer(p, "p")
    q = _integer(q, "q")
    d = _integer(d, "d")
    if p < 0 or q <= 0 or d <= 0:
        raise ValueError("require p>=0, q>0, d>0")
    pell = p * p - d * q * q
    radial_square = d * q * q
    inverse_product = (radial_square - p * p, 0, 0)
    character_x_square = (
        p * p * radial_square,
        radial_square * radial_square,
    )
    character_y_square = (
        radial_square,
        radial_square * radial_square,
    )
    return PellCayleyCertificate(
        p=p,
        q=q,
        d=d,
        pell_value=pell,
        radial_square=radial_square,
        inverse_product_coefficients=inverse_product,
        character_x_square=character_x_square,
        character_y_square=character_y_square,
    )


def pell_defect_decimal(
    p: int, q: int, d: int, *, precision: int = 80
):
    """Numerically evaluate q*sqrt(d)-p only for display/regression."""
    from decimal import Decimal, localcontext

    cert = pell_cayley_certificate(p, q, d)
    if not cert.valid:
        raise ValueError("not a negative Pell segment")
    if isinstance(precision, bool) or not isinstance(precision, int) or precision < 20:
        raise ValueError("precision must be an integer at least 20")
    with localcontext() as context:
        context.prec = precision + 12
        value = Decimal(q) * Decimal(d).sqrt() - Decimal(p)
        context.prec = precision
        return +value


def machin_spinor_certificate() -> tuple[Spinor, Spinor]:
    """Exact projective certificate for the Machin quarter-turn composition.

    No inverse tangent is evaluated: the identity is checked in the exact
    Cayley/spinor composition law.
    """
    left = spinor_product(spinor_power((5, 1), 4), (239, -1))
    return left, (1, 1)


def cayley_euler_approximant(theta: Fraction | int, steps: int) -> Character:
    """Exact norm-one rational Cayley product approximating exp(J*theta).

    Each step uses the projective half-angle parameter theta/(2*steps), and the
    same exact rotation is composed ``steps`` times.
    """
    theta = Fraction(theta)
    steps = _integer(steps, "steps")
    if steps <= 0:
        raise ValueError("steps must be positive")
    one_step = cayley_spinor(theta / (2 * steps))
    return rotation_character(spinor_power(one_step, steps))
