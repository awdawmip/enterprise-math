"""Finite spectral precision tools extracted from Enterprise Math #1159.

This module is a narrow extension candidate of T5_PRECISION_REFINEMENT.
It constructs and checks exact finite Dirichlet/Wallis data, the algebraic
spectral-decimation law, and dyadic completion intervals.

Important boundary: this module does *not* prove that the finite carriers are
primitive G0 Cell rotation, and it does not prove the analytic identification
of the internally completed constant with classical pi. Those are separately
typed theorem layers.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, localcontext
from fractions import Fraction
from math import factorial
from typing import Sequence, TypeVar

T = TypeVar("T")


def wallis_factor(n: int) -> Fraction:
    """Return the n-th exact rational Wallis factor."""
    if n < 1:
        raise ValueError("n must be >= 1")
    return Fraction((2 * n) ** 2, (2 * n - 1) * (2 * n + 1))


def wallis_partial(n: int) -> Fraction:
    """Return W_n = prod_{r=1}^n (2r)^2/((2r-1)(2r+1))."""
    if n < 0:
        raise ValueError("n must be >= 0")
    out = Fraction(1)
    for r in range(1, n + 1):
        out *= wallis_factor(r)
    return out


def wallis_upper(n: int) -> Fraction:
    """Return the target-free Wallis companion Q_n.

    The theorem layer proves W_n < W_infinity <= Q_n and Q_n decreases.
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    return wallis_partial(n) * Fraction(4 * n + 2, 4 * n + 1)


def wallis_upper_step_ratio(n: int) -> Fraction:
    """Return Q_(n+1)/Q_n exactly."""
    if n < 1:
        raise ValueError("n must be >= 1")
    return wallis_upper(n + 1) / wallis_upper(n)


def tau_lt_four_sign_certificate() -> Fraction:
    """Return the exact finite alternating-series sign certificate -268/405.

    The analytic theorem uses this partial sum, together with the alternating
    remainder sign, to prove that the first positive zero tau of S satisfies
    tau < 4.  This function only returns the exact rational finite datum.
    """
    return (
        Fraction(4)
        - Fraction(4**3, factorial(3))
        + Fraction(4**5, factorial(5))
        - Fraction(4**7, factorial(7))
        + Fraction(4**9, factorial(9))
    )


def _poly_add(a: Sequence[Fraction], b: Sequence[Fraction]) -> list[Fraction]:
    n = max(len(a), len(b))
    out = [Fraction(0) for _ in range(n)]
    for i, x in enumerate(a):
        out[i] += x
    for i, x in enumerate(b):
        out[i] += x
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def _poly_scale(a: Sequence[Fraction], c: Fraction) -> list[Fraction]:
    return [c * x for x in a]


def _poly_mul_linear(
    a: Sequence[Fraction], c0: Fraction, c1: Fraction
) -> list[Fraction]:
    out = [Fraction(0) for _ in range(len(a) + 1)]
    for i, x in enumerate(a):
        out[i] += c0 * x
        out[i + 1] += c1 * x
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def dirichlet_normalized_coefficients(M: int) -> tuple[Fraction, ...]:
    """Return the closed-form coefficients of F_M as a polynomial in x^2.

    F_M(x) = sum_j c_j x^(2j), where
    c_j = (-1)^j/(2j+1)! * prod_{r=1}^j (1-r^2/M^2).
    """
    if M < 2:
        raise ValueError("M must be >= 2")
    coeff: list[Fraction] = []
    for j in range(M):
        product = Fraction(1)
        for r in range(1, j + 1):
            product *= Fraction(M * M - r * r, M * M)
        coeff.append(Fraction((-1) ** j, factorial(2 * j + 1)) * product)
    return tuple(coeff)


def dirichlet_normalized_coefficients_from_recurrence(
    M: int,
) -> tuple[Fraction, ...]:
    """Independently compute F_M coefficients by the continuant recurrence."""
    if M < 2:
        raise ValueError("M must be >= 2")
    inv_M2 = Fraction(1, M * M)
    d0 = [Fraction(1)]
    d1 = [Fraction(2), -inv_M2]
    if M == 2:
        return tuple(x / M for x in d1)

    prev2, prev1 = d0, d1
    for _n in range(2, M):
        current = _poly_add(
            _poly_mul_linear(prev1, Fraction(2), -inv_M2),
            _poly_scale(prev2, Fraction(-1)),
        )
        prev2, prev1 = prev1, current
    return tuple(x / M for x in prev1)


def verify_dirichlet_coefficient_identity(M: int) -> bool:
    """Check the closed coefficient formula against the independent recurrence."""
    return dirichlet_normalized_coefficients(
        M
    ) == dirichlet_normalized_coefficients_from_recurrence(M)


def spectral_decimation(u: T) -> T:
    """Apply the exact even-site decimation polynomial R(u)=u(4-u)."""
    return u * (4 - u)  # type: ignore[operator,return-value]


def parity_curvature(mode_radii: Sequence[T]) -> T:
    """Return the scale-free odd/even multiplicative curvature.

    Input must be the positive radii s_1,...,s_(2q-1), with q>=2.
    Multiplicity is not inferred or erased: callers must supply the already
    declared mode list appropriate to their typed carrier.
    """
    m = len(mode_radii)
    if m < 3 or m % 2 == 0:
        raise ValueError("need an odd-length list s_1,...,s_(2q-1) with q>=2")
    q = (m + 1) // 2
    out = mode_radii[0] / mode_radii[0]  # type: ignore[operator]
    for r in range(1, q):
        even = mode_radii[2 * r - 1]
        left = mode_radii[2 * r - 2]
        right = mode_radii[2 * r]
        out = out * (even * even) / (left * right)  # type: ignore[operator]
    return out


def integer_mode_parity_curvature(q: int) -> Fraction:
    """Evaluate parity curvature on the integer ladder 1,...,2q-1."""
    if q < 2:
        raise ValueError("q must be >= 2")
    return parity_curvature([Fraction(k) for k in range(1, 2 * q)])


def _require_power_of_two(q: int) -> None:
    if q < 2 or q & (q - 1):
        raise ValueError("q must be a power of two with q >= 2")


def dyadic_smallest_eigenvalue(q: int, precision: int = 80) -> Decimal:
    """Construct the dyadic first-mode eigenvalue by inverse decimation.

    Starts from a_2=2 and iterates a_(2q)=2-sqrt(4-a_q).
    No trigonometric or pi value is used.
    """
    _require_power_of_two(q)
    with localcontext() as ctx:
        ctx.prec = precision
        a = Decimal(2)
        current = 2
        while current < q:
            a = Decimal(2) - (Decimal(4) - a).sqrt()
            current *= 2
        return +a


def dyadic_radical_expression(q: int) -> str:
    """Return a target-free symbolic expression for a_q."""
    _require_power_of_two(q)
    expr = "2"
    current = 2
    while current < q:
        expr = f"2 - sqrt(4 - ({expr}))"
        current *= 2
    return expr


@dataclass(frozen=True)
class CompletionCertificate:
    """Finite dyadic completion interval constructed from the spectral state."""

    q: int
    a_q: Decimal
    a_2q: Decimal
    lower: Decimal
    upper: Decimal
    width: Decimal
    width_exact: Fraction
    radical_a_q: str
    radical_a_2q: str


def dyadic_completion_certificate(
    q: int, precision: int = 80
) -> CompletionCertificate:
    """Construct the #1159 dyadic fourth-order completion interval.

    The finite algorithm computes
        T_q = q*sqrt(a_q),
        R_q = (4*T_(2q)-T_q)/3,
        width = 2/(15*q^4).

    The theorem layer, not this Decimal routine, proves for the internally
    defined completion constant tau that R_q < tau < R_q + width.
    """
    _require_power_of_two(q)
    with localcontext() as ctx:
        ctx.prec = precision
        a_q = dyadic_smallest_eigenvalue(q, precision=precision)
        a_2q = Decimal(2) - (Decimal(4) - a_q).sqrt()
        t_q = Decimal(q) * a_q.sqrt()
        t_2q = Decimal(2 * q) * a_2q.sqrt()
        lower = (Decimal(4) * t_2q - t_q) / Decimal(3)
        width_exact = Fraction(2, 15 * q**4)
        width = Decimal(width_exact.numerator) / Decimal(width_exact.denominator)
        upper = lower + width
        return CompletionCertificate(
            q=q,
            a_q=+a_q,
            a_2q=+a_2q,
            lower=+lower,
            upper=+upper,
            width=+width,
            width_exact=width_exact,
            radical_a_q=dyadic_radical_expression(q),
            radical_a_2q=dyadic_radical_expression(2 * q),
        )


def self_check(max_M: int = 16, max_wallis_n: int = 16) -> dict[str, bool]:
    """Run independent exact finite consistency checks for the extracted tool."""
    return {
        "dirichlet_coefficients": all(
            verify_dirichlet_coefficient_identity(M) for M in range(2, max_M + 1)
        ),
        "wallis_squeeze": all(
            wallis_upper_step_ratio(n)
            == 1 - Fraction(1, (2 * n + 1) ** 2 * (4 * n + 5))
            for n in range(1, max_wallis_n + 1)
        ),
        "tau_lt_four_sign": tau_lt_four_sign_certificate() == Fraction(-268, 405),
        "integer_mode_curvature": all(
            integer_mode_parity_curvature(q) == wallis_partial(q - 1)
            for q in range(2, max_wallis_n + 2)
        ),
        "dyadic_certificate": all(
            dyadic_completion_certificate(q, precision=60).width_exact
            == Fraction(2, 15 * q**4)
            for q in (2, 4, 8, 16, 32, 64)
        ),
    }
