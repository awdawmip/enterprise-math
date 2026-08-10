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

The polynomial P_p satisfies its canonical Picard--Fuchs equation modulo p.
At z=1 that equation degenerates to

    81 theta^2 P_p + 36 theta P_p + 5 P_p = 0.

The indicial polynomial at z=1 is rho(rho-1)(rho-1/2).  Since
deg(P_p)=(p-5)/6<p/2, every zero of P_p at z=1 is simple.  Hence a Franel
one-third zero can never coincide with the scalar-Hasse zero P_p(1)=0: it is
an ordinary first-jet/logarithmic-derivative condition instead.
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


def canonical_period_coefficients_residue(prime: int) -> tuple[int, ...]:
    """Return coefficients A_0,...,A_(M-1) modulo p."""
    M = _require_third_index_prime(prime)
    coefficients = [1]
    term = 1
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
        coefficients.append(term)
    if len(coefficients) != M:
        raise AssertionError("canonical Hasse polynomial degree changed")
    return tuple(coefficients)


def canonical_period_jets_residue(prime: int) -> tuple[int, int, int, int]:
    """Return (M,P_p(1),theta P_p(1),theta^2 P_p(1))."""
    M = _require_third_index_prime(prime)
    coefficients = canonical_period_coefficients_residue(prime)
    period = sum(coefficients) % prime
    theta_period = sum(
        index * coefficient
        for index, coefficient in enumerate(coefficients)
    ) % prime
    theta2_period = sum(
        index * index * coefficient
        for index, coefficient in enumerate(coefficients)
    ) % prime
    return M, period, theta_period, theta2_period


def canonical_period_jet_residue(prime: int) -> tuple[int, int, int]:
    """Compatibility wrapper returning the first two canonical jet values."""
    M, period, theta_period, _ = canonical_period_jets_residue(prime)
    return M, period, theta_period


def canonical_period_terminates_before_franel_tail(prime: int) -> bool:
    """Certify A_M=0 mod p, one index before the Franel obstruction stops."""
    M = _require_third_index_prime(prime)
    if (6 * (M - 1) + 5) % prime != 0:
        raise AssertionError("canonical period must acquire p at A_M")
    if (6 * M - 1) % prime != 0:
        raise AssertionError("Franel contiguous series must stop at C_(M+1)")
    return True


def canonical_picard_fuchs_relation_at_one(prime: int) -> bool:
    """Certify 81 theta^2 P + 36 theta P + 5 P=0 at z=1 modulo p."""
    _, period, theta_period, theta2_period = canonical_period_jets_residue(prime)
    residue = (
        81 * theta2_period + 36 * theta_period + 5 * period
    ) % prime
    if residue != 0:
        raise AssertionError("canonical Picard-Fuchs relation failed at z=1")
    return True


def polynomial_root_multiplicity_at_one(prime: int) -> int:
    """Return the multiplicity of z=1 as a root of P_p, or zero."""
    coefficients = canonical_period_coefficients_residue(prime)
    degree = len(coefficients) - 1
    for order in range(degree + 1):
        value = 0
        for exponent, coefficient in enumerate(coefficients):
            if exponent < order:
                continue
            falling = 1
            for step in range(order):
                falling = falling * (exponent - step) % prime
            value = (value + coefficient * falling) % prime
        if value != 0:
            return order
    raise AssertionError("nonzero Hasse polynomial cannot vanish to all orders")


def canonical_hasse_zero_is_simple(prime: int) -> bool:
    """Certify that P_p(1)=0, when it occurs, has multiplicity exactly one."""
    M, period, _, _ = canonical_period_jets_residue(prime)
    if period != 0:
        return True
    multiplicity = polynomial_root_multiplicity_at_one(prime)
    if multiplicity <= 0:
        raise AssertionError("vanishing period must have positive multiplicity")
    if M - 1 >= (prime + 1) // 2:
        raise AssertionError("degree bound needed by the indicial argument failed")
    inv2 = pow(2, -1, prime)
    indicial = (
        multiplicity
        * (multiplicity - 1)
        * (multiplicity - inv2)
    ) % prime
    if indicial != 0:
        raise AssertionError("root multiplicity must satisfy the indicial equation")
    if multiplicity != 1:
        raise AssertionError("degree bound leaves only the simple integral root")
    return True


def franel_obstruction_from_hasse_jet(prime: int) -> tuple[int, int, int, int]:
    """Return (M, obstruction, period, theta-period) and certify the bridge."""
    M, period, theta_period, _ = canonical_period_jets_residue(prime)
    canonical_period_terminates_before_franel_tail(prime)
    canonical_picard_fuchs_relation_at_one(prime)
    predicted = (-(5 * period + 27 * theta_period)) % prime
    actual = fixed_parameter_full_truncation_residue(prime)
    if actual != predicted:
        raise AssertionError("Franel obstruction and canonical first jet disagree")
    return M, actual, period, theta_period


def franel_zero_avoids_scalar_hasse_zero(prime: int) -> bool:
    """Certify H_p=0 => P_p(1) is nonzero."""
    _, obstruction, period, _ = franel_obstruction_from_hasse_jet(prime)
    canonical_hasse_zero_is_simple(prime)
    if obstruction == 0 and period == 0:
        raise AssertionError("Franel zero cannot coincide with scalar-Hasse zero")
    return obstruction != 0 or period != 0


def franel_zero_is_fixed_log_derivative(prime: int) -> bool:
    """Certify H_p=0 iff theta P/P=-5/27 in the canonical ordinary locus."""
    _, obstruction, period, theta_period = franel_obstruction_from_hasse_jet(prime)
    franel_zero_avoids_scalar_hasse_zero(prime)
    if obstruction != 0:
        return False
    if period == 0:
        raise AssertionError("Franel zero must lie in the scalar ordinary locus")
    target = (-5 * pow(27, -1, prime)) % prime
    actual = theta_period * pow(period, -1, prime) % prime
    if actual != target:
        raise AssertionError("fixed logarithmic-derivative criterion failed")
    return True


def pulled_back_hasse_polynomial_critical_at_one(prime: int) -> bool:
    """Equivalent critical-point form for Q(x)=x^5 P_p(x^27) at x=1."""
    _, obstruction, period, theta_period = franel_obstruction_from_hasse_jet(prime)
    derivative_at_one = (5 * period + 27 * theta_period) % prime
    if (obstruction == 0) != (derivative_at_one == 0):
        raise AssertionError("pulled-back critical-point criterion failed")
    return derivative_at_one == 0


def pulled_back_critical_curvature(prime: int) -> tuple[int, int]:
    """At a Franel zero return (Q'(1),Q''(1)) and prove nondegeneracy for p>5."""
    _, obstruction, period, theta_period = franel_obstruction_from_hasse_jet(prime)
    if obstruction != 0:
        raise ValueError("prime is not a one-third Franel zero")
    _, _, _, theta2_period = canonical_period_jets_residue(prime)
    first = (5 * period + 27 * theta_period) % prime
    second = (
        20 * period + 243 * theta_period + 729 * theta2_period
    ) % prime
    if first != 0:
        raise AssertionError("Franel zero must make the pulled-back first derivative vanish")
    if prime > 5:
        expected = (-10 * period) % prime
        if second != expected or second == 0:
            raise AssertionError("ordinary Franel zero must be a nondegenerate critical point")
    return first, second
