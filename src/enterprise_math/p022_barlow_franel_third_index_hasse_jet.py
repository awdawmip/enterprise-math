"""First-jet reduction of the Franel one-third hypergeometric obstruction.

Let

    A_k = (5/6)_k (1/3)_k^2 / (k!)^3

be the coefficients of the monodromy-normalized rank-three period, and let

    C_k = (-1/6)_k (1/3)_k (4/3)_k / (k!)^3

be the coefficients of the fixed Franel one-third obstruction.

An exact Gosper reduction gives

    C_k/A_k = -5 - 27k + R_(k+1) A_(k+1)/A_k - R_k,
    R_k = 324 k^3 / (6k-1).

For p=6M-1, A_M is zero modulo p, as is the terminal certificate
R_(M+1)A_(M+1).  Therefore if

    P_p(z)=sum_(k=0)^(M-1) A_k z^k,

then the Franel obstruction satisfies

    H_p = -(5 P_p(1) + 27 theta P_p(1))  (mod p),
    theta=z d/dz.

Thus the Franel zero is a first-jet condition on the canonical period
truncation, not the zero of the canonical scalar period itself.
"""

from __future__ import annotations

from fractions import Fraction

from .p022_barlow_franel_third_index_fixed_hypergeom import (
    fixed_parameter_full_truncation_residue,
)
from .p022_barlow_low_order_defect_reduction import _is_prime


def _require_third_index_prime(prime: int) -> int:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 5
        or not _is_prime(prime)
        or prime % 6 != 5
    ):
        raise ValueError("prime must be 5 modulo 6")
    return (prime + 1) // 6


def canonical_period_term_ratio(index: int) -> Fraction:
    """Return A_(k+1)/A_k for (5/6,1/3,1/3;1,1)."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be a non-negative integer")
    k = index
    return Fraction(
        (6 * k + 5) * (3 * k + 1) ** 2,
        54 * (k + 1) ** 3,
    )


def franel_to_canonical_term_ratio(index: int) -> Fraction:
    """Return C_k/A_k exactly."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be a non-negative integer")
    k = index
    return Fraction(-(3 * k + 1), 6 * k - 1)


def gosper_boundary_factor(index: int) -> Fraction:
    """Return R_k=324 k^3/(6k-1)."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be a non-negative integer")
    k = index
    return Fraction(324 * k**3, 6 * k - 1)


def contiguous_gosper_reduction(index: int) -> tuple[Fraction, Fraction]:
    """Certify C_k/A_k as a linear jet term plus an exact difference."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be a non-negative integer")
    k = index
    left = franel_to_canonical_term_ratio(k)
    right = (
        Fraction(-5 - 27 * k)
        + gosper_boundary_factor(k + 1) * canonical_period_term_ratio(k)
        - gosper_boundary_factor(k)
    )
    if left != right:
        raise AssertionError("contiguous Gosper reduction failed")
    return left, right


def canonical_period_jet_residue(prime: int) -> tuple[int, int, int]:
    """Return (M,P_p(1),theta P_p(1)) for p=6M-1."""
    M = _require_third_index_prime(prime)
    term = 1
    period = 1
    theta_period = 0
    inv54 = pow(54, -1, prime)

    for k in range(M - 1):
        numerator = (6 * k + 5) * (3 * k + 1) ** 2
        denominator_unit = pow(k + 1, 3, prime)
        term = (
            term
            * (numerator % prime)
            * inv54
            * pow(denominator_unit, -1, prime)
        ) % prime
        index = k + 1
        period = (period + term) % prime
        theta_period = (theta_period + index * term) % prime

    return M, period, theta_period


def canonical_period_terminates_before_franel_tail(prime: int) -> bool:
    """Certify A_M=0 mod p, one index before the Franel obstruction stops."""
    M, _, _ = canonical_period_jet_residue(prime)
    if (6 * (M - 1) + 5) % prime != 0:
        raise AssertionError("canonical period must acquire p at A_M")
    if (6 * M - 1) % prime != 0:
        raise AssertionError("Franel contiguous series must stop at C_(M+1)")
    return True


def franel_obstruction_from_hasse_jet(prime: int) -> tuple[int, int, int, int]:
    """Return (M, obstruction, period, theta-period) and certify the bridge."""
    M, period, theta_period = canonical_period_jet_residue(prime)
    canonical_period_terminates_before_franel_tail(prime)
    predicted = (-(5 * period + 27 * theta_period)) % prime
    actual = fixed_parameter_full_truncation_residue(prime)
    if actual != predicted:
        raise AssertionError("Franel obstruction and canonical first jet disagree")
    return M, actual, period, theta_period


def franel_zero_is_fixed_log_derivative(prime: int) -> bool:
    """When P_p(1) is nonzero, test theta P/P = -5/27 mod p."""
    _, obstruction, period, theta_period = franel_obstruction_from_hasse_jet(prime)
    if period == 0:
        return False
    target = (-5 * pow(27, -1, prime)) % prime
    actual = theta_period * pow(period, -1, prime) % prime
    if (obstruction == 0) != (actual == target):
        raise AssertionError("fixed logarithmic-derivative criterion failed")
    return obstruction == 0


def pulled_back_hasse_polynomial_critical_at_one(prime: int) -> bool:
    """Equivalent critical-point form for Q(x)=x^5 P_p(x^27) at x=1."""
    _, obstruction, period, theta_period = franel_obstruction_from_hasse_jet(prime)
    derivative_at_one = (5 * period + 27 * theta_period) % prime
    if (obstruction == 0) != (derivative_at_one == 0):
        raise AssertionError("pulled-back critical-point criterion failed")
    return derivative_at_one == 0
