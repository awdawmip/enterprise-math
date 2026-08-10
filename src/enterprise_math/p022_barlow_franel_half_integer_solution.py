"""Integer normalization of the universal midpoint companion.

Let G_d be the rational midpoint-offset companion.  The gauge transform

    Y_d = (-8)^d G_d

satisfies

    (2d+1)^2 Y_(d+1)
      = (28d^2+1) Y_d + 8(2d-1)^2 Y_(d-1),

which is exactly four times the classical Franel recurrence after evaluating
its polynomial coefficients at the half-integer n=d-1/2.

Clearing the natural odd-double-factorial denominator gives the positive
integer sequence

    K_0=0, K_1=1,
    K_(d+1)=(28d^2+1)K_d+8(2d-1)^4K_(d-1).

For every forced-midpoint prime p and every 1<=d<(p-1)/2, the normalizing
factor is a p-adic unit, hence p divides the Franel offset iff p divides K_d.

The classical integer-index Franel recurrence space and its continued-fraction
recurrence are prior art.  This module records the P022 half-integer
specialization and its use as a zero-geometry integer coordinate.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache

from .p022_barlow_franel_half_index import half_index, half_index_is_forced_zero
from .p022_barlow_franel_midpoint_offset import midpoint_companion_fraction
from .p022_barlow_low_order_defect_reduction import _is_prime


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_forced_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
        or not half_index_is_forced_zero(prime)
    ):
        raise ValueError("prime must be an odd prime in 5 or 7 modulo 8")


def odd_double_factorial(odd: int) -> int:
    if isinstance(odd, bool) or not isinstance(odd, int) or odd < -1 or odd % 2 == 0:
        raise ValueError("argument must be an odd integer >=-1")
    result = 1
    for value in range(1, odd + 1, 2):
        result *= value
    return result


@lru_cache(maxsize=None)
def half_integer_franel_solution(offset: int) -> Fraction:
    """Y_d=(-8)^d G_d, the canonical half-integer-lattice solution."""
    _require_natural("offset", offset)
    return ((-8) ** offset) * midpoint_companion_fraction(offset)


def half_integer_franel_recurrence_residual(offset: int) -> Fraction:
    """Exact residual of the polynomial Franel recurrence at n=d-1/2."""
    if isinstance(offset, bool) or not isinstance(offset, int) or offset < 1:
        raise ValueError("offset must be positive")
    previous = half_integer_franel_solution(offset - 1)
    current = half_integer_franel_solution(offset)
    following = half_integer_franel_solution(offset + 1)
    return (
        (2 * offset + 1) ** 2 * following
        - (28 * offset * offset + 1) * current
        - 8 * (2 * offset - 1) ** 2 * previous
    )


@lru_cache(maxsize=None)
def integer_midpoint_companion(offset: int) -> int:
    """Positive integer K_d obtained by denominator-clearing the half solution."""
    _require_natural("offset", offset)
    if offset == 0:
        return 0
    if offset == 1:
        return 1
    d = offset - 1
    return (
        (28 * d * d + 1) * integer_midpoint_companion(d)
        + 8 * (2 * d - 1) ** 4 * integer_midpoint_companion(d - 1)
    )


def integer_normalization_identity(offset: int) -> tuple[Fraction, int]:
    """Cross-check K_d = -((2d-1)!!)^2 Y_d/8 for d>=1."""
    if isinstance(offset, bool) or not isinstance(offset, int) or offset < 1:
        raise ValueError("offset must be positive")
    odd_factorial = odd_double_factorial(2 * offset - 1)
    normalized = -Fraction(odd_factorial * odd_factorial, 8) * half_integer_franel_solution(offset)
    integer = integer_midpoint_companion(offset)
    if normalized.denominator != 1 or normalized.numerator != integer:
        raise AssertionError("half-integer solution normalization must equal K_d")
    return normalized, integer


def midpoint_zero_from_integer_companion(prime: int, offset: int) -> bool:
    """For d<m, certify p|F_(m-d) iff p|K_d."""
    _require_forced_prime(prime)
    midpoint = half_index(prime)
    if isinstance(offset, bool) or not isinstance(offset, int) or not 1 <= offset < midpoint:
        raise ValueError("offset must lie in 1..m-1")
    # p>2d+1 in this range, so 8*((2d-1)!!)^2 is a p-adic unit.
    return integer_midpoint_companion(offset) % prime == 0


def half_integer_standard_basis(max_offset: int) -> tuple[tuple[Fraction, ...], tuple[Fraction, ...]]:
    """Two canonical solutions X,Y of the half-integer recurrence.

    X_0=1,X_1=0; Y_0=0,Y_1=-8.  Y is the midpoint companion gauge transform.
    """
    _require_natural("max_offset", max_offset)
    if max_offset == 0:
        return (Fraction(1, 1),), (Fraction(0, 1),)

    x = [Fraction(1, 1), Fraction(0, 1)]
    y = [Fraction(0, 1), Fraction(-8, 1)]
    for d in range(1, max_offset):
        denominator = (2 * d + 1) ** 2
        x.append(
            Fraction(
                (28 * d * d + 1) * x[d]
                + 8 * (2 * d - 1) ** 2 * x[d - 1],
                denominator,
            )
        )
        y.append(
            Fraction(
                (28 * d * d + 1) * y[d]
                + 8 * (2 * d - 1) ** 2 * y[d - 1],
                denominator,
            )
        )
    return tuple(x), tuple(y)


def half_integer_casoratian(offset: int) -> Fraction:
    """W_d=X_dY_(d+1)-X_(d+1)Y_d."""
    _require_natural("offset", offset)
    x, y = half_integer_standard_basis(offset + 1)
    return x[offset] * y[offset + 1] - x[offset + 1] * y[offset]


def half_integer_casoratian_closed(offset: int) -> Fraction:
    _require_natural("offset", offset)
    return Fraction((-8) ** (offset + 1), (2 * offset + 1) ** 2)


def continued_fraction_half_step_state(offset: int) -> Fraction:
    """P_d=K_d/4^(d-1), the half-step Euler--Wallis recurrence state."""
    if isinstance(offset, bool) or not isinstance(offset, int) or offset < 1:
        raise ValueError("offset must be positive")
    return Fraction(integer_midpoint_companion(offset), 4 ** (offset - 1))


def continued_fraction_half_step_residual(offset: int) -> Fraction:
    """Residual at the polynomial recurrence parameter n=d-1/2.

    P_(d+1) = (7x^2+7x+2)P_d + 8x^4 P_(d-1), x=d-1/2.
    """
    if isinstance(offset, bool) or not isinstance(offset, int) or offset < 2:
        raise ValueError("offset must be at least two")
    x = Fraction(2 * offset - 1, 2)
    return (
        continued_fraction_half_step_state(offset + 1)
        - (7 * x * x + 7 * x + 2) * continued_fraction_half_step_state(offset)
        - 8 * x**4 * continued_fraction_half_step_state(offset - 1)
    )
