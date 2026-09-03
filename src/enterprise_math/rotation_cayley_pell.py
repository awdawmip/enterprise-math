"""Exact Cayley-coordinate and paired-Pell certificates for the Euler/precision-pi line.

This module proves finite algebraic identities only.  It does not derive the modular
lambda special value or identify the carrier phase metric with native line length.
Quadratic surds are represented exactly by integer coefficient pairs ``a+b*sqrt(D)``.
Biquadratic values use the basis ``1, sqrt(D), sqrt(E), sqrt(D*E)``.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from numbers import Integral
from typing import TypeAlias

from enterprise_math.paired_pell_shell import PairedPellCertificate, n58_certificate

QuadraticPair: TypeAlias = tuple[int, int]
BiquadraticTuple: TypeAlias = tuple[int, int, int, int]


def _int(value: int, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, Integral):
        raise TypeError(f"{name} must be an integer")
    return int(value)


def quadratic_add(left: QuadraticPair, right: QuadraticPair) -> QuadraticPair:
    return left[0] + right[0], left[1] + right[1]


def quadratic_scale(scale: int, value: QuadraticPair) -> QuadraticPair:
    scale = _int(scale, "scale")
    return scale * value[0], scale * value[1]


def quadratic_mul(
    left: QuadraticPair, right: QuadraticPair, radicand: int
) -> QuadraticPair:
    """Multiply ``a+b*sqrt(D)`` and ``c+d*sqrt(D)`` exactly."""

    radicand = _int(radicand, "radicand")
    if radicand <= 0:
        raise ValueError("radicand must be positive")
    a, b = left
    c, d = right
    return a * c + radicand * b * d, a * d + b * c


def quadratic_pow(value: QuadraticPair, exponent: int, radicand: int) -> QuadraticPair:
    """Raise an exact quadratic surd pair to a nonnegative integer power."""

    exponent = _int(exponent, "exponent")
    radicand = _int(radicand, "radicand")
    if exponent < 0:
        raise ValueError("exponent must be nonnegative")
    if radicand <= 0:
        raise ValueError("radicand must be positive")
    result: QuadraticPair = (1, 0)
    base = value
    power = exponent
    while power:
        if power & 1:
            result = quadratic_mul(result, base, radicand)
        base = quadratic_mul(base, base, radicand)
        power //= 2
    return result


def quadratic_conjugate(value: QuadraticPair) -> QuadraticPair:
    return value[0], -value[1]


def quadratic_norm(value: QuadraticPair, radicand: int) -> int:
    """Return ``a^2-D*b^2``."""

    radicand = _int(radicand, "radicand")
    if radicand <= 0:
        raise ValueError("radicand must be positive")
    a, b = value
    return a * a - radicand * b * b


def biquadratic_mul(
    left: BiquadraticTuple,
    right: BiquadraticTuple,
    first_radicand: int,
    second_radicand: int,
) -> BiquadraticTuple:
    """Multiply in ``Z[sqrt(D),sqrt(E)]`` using basis ``1,r,s,rs``."""

    d = _int(first_radicand, "first_radicand")
    e = _int(second_radicand, "second_radicand")
    if d <= 0 or e <= 0:
        raise ValueError("radicands must be positive")
    a, b, c, f = left
    g, h, i, j = right
    return (
        a * g + d * b * h + e * c * i + d * e * f * j,
        a * h + b * g + e * c * j + e * f * i,
        a * i + c * g + d * b * j + d * f * h,
        a * j + f * g + b * i + c * h,
    )


def cayley_compose(left: Fraction | int, right: Fraction | int) -> Fraction:
    """Compose two rational Cayley defects: ``(a+b)/(1-a*b)``.

    The denominator-zero case is the omitted half-turn chart point.
    """

    a = Fraction(left)
    b = Fraction(right)
    denominator = 1 - a * b
    if denominator == 0:
        raise ZeroDivisionError("Cayley composition reaches the omitted half-turn")
    return (a + b) / denominator


def cayley_double(value: Fraction | int) -> Fraction:
    return cayley_compose(value, value)


@dataclass(frozen=True)
class N58CayleyPellCertificate:
    paired_pell: PairedPellCertificate
    first_post_gate_defect_sqrt2: QuadraticPair
    first_post_gate_defect_square_sqrt2: QuadraticPair
    first_post_gate_defect_sixth_sqrt2: QuadraticPair
    positive_pell_unit_sqrt2: QuadraticPair
    negative_pell_unit_sqrt58: QuadraticPair
    negative_pell_inverse_sqrt58: QuadraticPair
    lambda_star_coefficients: BiquadraticTuple

    @property
    def valid(self) -> bool:
        r = self.first_post_gate_defect_sqrt2
        return (
            self.paired_pell.P == 99
            and self.paired_pell.d_positive == 2
            and self.paired_pell.y_positive == 70
            and self.paired_pell.d_negative == 58
            and self.paired_pell.y_negative == 13
            and self.first_post_gate_defect_square_sqrt2 == quadratic_mul(r, r, 2)
            and quadratic_add(
                (1, 0),
                quadratic_scale(-1, self.first_post_gate_defect_square_sqrt2),
            )
            == quadratic_scale(2, r)
            and self.first_post_gate_defect_sixth_sqrt2 == (99, -70)
            and self.positive_pell_unit_sqrt2 == (99, 70)
            and quadratic_mul(
                self.first_post_gate_defect_sixth_sqrt2,
                self.positive_pell_unit_sqrt2,
                2,
            )
            == (1, 0)
            and quadratic_norm(self.positive_pell_unit_sqrt2, 2) == 1
            and self.negative_pell_unit_sqrt58 == (99, 13)
            and self.negative_pell_inverse_sqrt58 == (-99, 13)
            and quadratic_mul(
                self.negative_pell_unit_sqrt58,
                self.negative_pell_inverse_sqrt58,
                58,
            )
            == (1, 0)
            and quadratic_norm(self.negative_pell_unit_sqrt58, 58) == -1
            and biquadratic_mul(
                self.lambda_star_coefficients,
                biquadratic_mul(
                    (99, 70, 0, 0),
                    (99, 0, 13, 0),
                    2,
                    58,
                ),
                2,
                58,
            )
            == (1, 0, 0, 0)
        )


def n58_cayley_pell_certificate() -> N58CayleyPellCertificate:
    """Return the exact unit-level bridge behind the N=58 factorization.

    ``(-1,1)`` represents ``sqrt(2)-1``.  Its sixth power is the inverse of
    ``99+70*sqrt(2)``.  ``(-99,13)`` represents ``13*sqrt(58)-99`` and is the
    inverse of ``99+13*sqrt(58)``.  Their product is the coefficient tuple of
    the classical positive singular-modulus root, conditional on that modular
    special value being supplied externally.
    """

    paired = n58_certificate()
    dyadic_defect: QuadraticPair = (-1, 1)
    dyadic_square = quadratic_pow(dyadic_defect, 2, 2)
    dyadic_sixth = quadratic_pow(dyadic_defect, 6, 2)
    positive_unit: QuadraticPair = (99, 70)
    negative_unit: QuadraticPair = (99, 13)
    negative_inverse: QuadraticPair = (-99, 13)
    lambda_star = biquadratic_mul(
        (dyadic_sixth[0], dyadic_sixth[1], 0, 0),
        (negative_inverse[0], 0, negative_inverse[1], 0),
        2,
        58,
    )
    certificate = N58CayleyPellCertificate(
        paired_pell=paired,
        first_post_gate_defect_sqrt2=dyadic_defect,
        first_post_gate_defect_square_sqrt2=dyadic_square,
        first_post_gate_defect_sixth_sqrt2=dyadic_sixth,
        positive_pell_unit_sqrt2=positive_unit,
        negative_pell_unit_sqrt58=negative_unit,
        negative_pell_inverse_sqrt58=negative_inverse,
        lambda_star_coefficients=lambda_star,
    )
    if not certificate.valid:
        raise AssertionError("N=58 Cayley/Pell unit certificate failed")
    return certificate


def certificate() -> dict[str, object]:
    cert = n58_cayley_pell_certificate()
    return {
        "cayley_rational_example": str(cayley_compose(Fraction(1, 2), Fraction(1, 3))),
        "first_post_gate_defect_sqrt2": cert.first_post_gate_defect_sqrt2,
        "first_post_gate_defect_square_sqrt2": cert.first_post_gate_defect_square_sqrt2,
        "first_post_gate_defect_sixth_sqrt2": cert.first_post_gate_defect_sixth_sqrt2,
        "positive_pell_unit_sqrt2": cert.positive_pell_unit_sqrt2,
        "negative_pell_unit_sqrt58": cert.negative_pell_unit_sqrt58,
        "negative_pell_inverse_sqrt58": cert.negative_pell_inverse_sqrt58,
        "lambda_star_basis": ("1", "sqrt(2)", "sqrt(58)", "sqrt(116)"),
        "lambda_star_coefficients": cert.lambda_star_coefficients,
        "valid": cert.valid,
        "boundary": "the modular lambda special value is external analytic input",
    }


if __name__ == "__main__":
    import json

    print(json.dumps(certificate(), indent=2, ensure_ascii=False))
