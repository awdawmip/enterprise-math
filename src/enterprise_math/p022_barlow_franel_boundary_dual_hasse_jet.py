"""Dual-Hasse first-jet structure for the P022 Franel boundary kernel.

For prime p=6M-1 the sign-free boundary kernel

    W_M = sum_{j=0}^{2M-1} C(2M,j) C(M+j,j) C(2M-1,j)

has the fixed-parameter reduction

    W_M = sum_{j=0}^{N} (-1/3)_j (2/3)_j (7/6)_j / (j!)^3  (mod p),
    N=2M-1=(p-2)/3.

Let

    D_p(z)=sum_{j=0}^{N} d_j z^j,
    d_j=(1/6)_j (2/3)_j^2/(j!)^3.

This is the Dwork/Galois-conjugate canonical Hasse polynomial to the existing
P022 period

    P_p(z)=sum (5/6)_j (1/3)_j^2/(j!)^3 z^j.

The boundary coefficient c_j and d_j satisfy the exact contiguous Gosper
reduction

    c_j/d_j = -2 -(27/2)j + R_(j+1) d_(j+1)/d_j - R_j,
    R_j = 81 j^3/(3j-1).

The terminal certificate is p-divisible, hence

    W_M = -2 D_p(1) -(27/2) theta D_p(1)                 (mod p).

The conjugate Picard--Fuchs equation degenerates at z=1 to

    81 theta^2 D_p + 36 theta D_p + 4 D_p = 0.

Its local exponent set at z=1 is {0,1,1/2}; since deg D_p=(p-2)/3<p/2,
a scalar Hasse zero D_p(1)=0 is simple.  Consequently W_M=0 can never
coincide with D_p(1)=0 and, on the ordinary locus,

    W_M=0  iff  theta D_p(1)/D_p(1) = -4/27.

There is a second exact structural fact.  The original canonical operator
for alpha=(5/6,1/3,1/3) and the conjugate operator for
alpha^vee=(1/6,2/3,2/3) are negative formal adjoints in ordinary d/dz form.
The associated Lagrange concomitant vanishes at z=0 and therefore identically.
At z=1 this gives

    3(D theta P + P theta D) + P D = 0                  (mod p).

Thus, whenever P(1)D(1) is nonzero,

    theta P/P + theta D/D = -1/3.

The existing Franel first-jet criterion theta P/P=-5/27 and the new conjugate
criterion theta D/D=-4/27 therefore form one adjoint pair, not two independent
obstructions.  This proves that scalar conjugate-Hasse first jets cannot by
themselves close the remaining q=3r-1 boundary; a genuinely matrix/second-order
invariant is required.
"""

from __future__ import annotations

from fractions import Fraction

from .p022_barlow_franel_boundary_double_horizon import sign_free_companion_kernel
from .p022_barlow_franel_third_index_hasse_jet import (
    canonical_period_jets_residue,
    franel_obstruction_from_hasse_jet,
)
from .p022_barlow_low_order_defect_reduction import _is_prime


def _require_one_third_prime(prime: int) -> int:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime < 5
        or not _is_prime(prime)
        or prime % 6 != 5
    ):
        raise ValueError("prime must be 5 modulo 6")
    return (prime + 1) // 6


def conjugate_period_term_ratio(index: int) -> Fraction:
    """Return d_(j+1)/d_j for (1/6,2/3,2/3;1,1)."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be a non-negative integer")
    j = index
    return Fraction(
        (6 * j + 1) * (3 * j + 2) ** 2,
        54 * (j + 1) ** 3,
    )


def boundary_to_conjugate_term_ratio(index: int) -> Fraction:
    """Return c_j/d_j=-(6j+1)/(3j-1) exactly."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be a non-negative integer")
    j = index
    return Fraction(-(6 * j + 1), 3 * j - 1)


def conjugate_gosper_boundary_factor(index: int) -> Fraction:
    """Return R_j=81j^3/(3j-1)."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be a non-negative integer")
    j = index
    return Fraction(81 * j**3, 3 * j - 1)


def conjugate_contiguous_gosper_reduction(index: int) -> tuple[Fraction, Fraction]:
    """Certify c_j/d_j as a conjugate first-jet term plus exact difference."""
    if isinstance(index, bool) or not isinstance(index, int) or index < 0:
        raise ValueError("index must be a non-negative integer")
    j = index
    left = boundary_to_conjugate_term_ratio(j)
    right = (
        Fraction(-2) - Fraction(27, 2) * j
        + conjugate_gosper_boundary_factor(j + 1) * conjugate_period_term_ratio(j)
        - conjugate_gosper_boundary_factor(j)
    )
    if left != right:
        raise AssertionError("conjugate contiguous Gosper reduction failed")
    return left, right


def conjugate_period_coefficients_residue(prime: int) -> tuple[int, ...]:
    """Return d_0,...,d_N modulo p, where N=(p-2)/3."""
    M = _require_one_third_prime(prime)
    N = 2 * M - 1
    coefficients = [1]
    term = 1
    inv54 = pow(54, -1, prime)
    for j in range(N):
        numerator = (6 * j + 1) * (3 * j + 2) ** 2
        denominator_unit = pow(j + 1, 3, prime)
        term = (
            term
            * (numerator % prime)
            * inv54
            * pow(denominator_unit, -1, prime)
        ) % prime
        coefficients.append(term)
    if len(coefficients) != N + 1:
        raise AssertionError("conjugate Hasse polynomial degree changed")
    return tuple(coefficients)


def conjugate_period_jets_residue(prime: int) -> tuple[int, int, int, int]:
    """Return (N,D_p(1),theta D_p(1),theta^2 D_p(1))."""
    M = _require_one_third_prime(prime)
    N = 2 * M - 1
    coefficients = conjugate_period_coefficients_residue(prime)
    period = sum(coefficients) % prime
    theta_period = sum(
        index * coefficient
        for index, coefficient in enumerate(coefficients)
    ) % prime
    theta2_period = sum(
        index * index * coefficient
        for index, coefficient in enumerate(coefficients)
    ) % prime
    return N, period, theta_period, theta2_period


def conjugate_period_terminal_certificate(prime: int) -> bool:
    """Certify that the Gosper terminal R_(N+1)d_(N+1) is 0 modulo p.

    At N=(p-2)/3, the d_(N+1)/d_N numerator contains (3N+2)^2=p^2,
    while R_(N+1) has the single denominator factor 3N+2=p.  All remaining
    factors are p-units, leaving positive p-adic valuation.
    """
    M = _require_one_third_prime(prime)
    N = 2 * M - 1
    if 3 * N + 2 != prime:
        raise AssertionError("conjugate truncation endpoint changed")
    if (6 * N + 1) % prime == 0:
        raise AssertionError("unexpected extra terminal factor")
    if (N + 1) % prime == 0:
        raise AssertionError("terminal factorial denominator must be a p-unit")
    return True


def conjugate_picard_fuchs_relation_at_one(prime: int) -> bool:
    """Certify 81 theta^2 D + 36 theta D + 4D = 0 at z=1 modulo p."""
    _, period, theta_period, theta2_period = conjugate_period_jets_residue(prime)
    residue = (81 * theta2_period + 36 * theta_period + 4 * period) % prime
    if residue != 0:
        raise AssertionError("conjugate Picard--Fuchs relation failed")
    return True


def conjugate_polynomial_root_multiplicity_at_one(prime: int) -> int:
    """Return the multiplicity of z=1 as a root of D_p, or zero."""
    coefficients = conjugate_period_coefficients_residue(prime)
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
    raise AssertionError("nonzero conjugate Hasse polynomial cannot vanish to all orders")


def conjugate_hasse_zero_is_simple(prime: int) -> bool:
    """Certify that D_p(1)=0, when it occurs, has multiplicity exactly one."""
    N, period, _, _ = conjugate_period_jets_residue(prime)
    if period != 0:
        return True
    multiplicity = conjugate_polynomial_root_multiplicity_at_one(prime)
    if N >= prime // 2:
        raise AssertionError("degree bound needed by the indicial argument failed")
    inv2 = pow(2, -1, prime)
    indicial = multiplicity * (multiplicity - 1) * (multiplicity - inv2) % prime
    if indicial != 0:
        raise AssertionError("conjugate root multiplicity must satisfy the indicial equation")
    if multiplicity != 1:
        raise AssertionError("degree bound leaves only the simple integral root")
    return True


def boundary_kernel_from_conjugate_hasse_jet(prime: int) -> tuple[int, int, int, int]:
    """Return (M,W_M,D,theta D) and certify the conjugate first-jet bridge."""
    M = _require_one_third_prime(prime)
    conjugate_period_terminal_certificate(prime)
    conjugate_picard_fuchs_relation_at_one(prime)
    _, period, theta_period, _ = conjugate_period_jets_residue(prime)
    predicted = (
        -2 * period
        - 27 * pow(2, -1, prime) * theta_period
    ) % prime
    actual = sign_free_companion_kernel(M) % prime
    if actual != predicted:
        raise AssertionError("boundary kernel and conjugate Hasse first jet disagree")
    return M, actual, period, theta_period


def boundary_zero_avoids_conjugate_scalar_hasse(prime: int) -> bool:
    """Certify W_M=0 => D_p(1) != 0."""
    _, boundary, period, _ = boundary_kernel_from_conjugate_hasse_jet(prime)
    conjugate_hasse_zero_is_simple(prime)
    if boundary == 0 and period == 0:
        raise AssertionError("boundary zero cannot coincide with conjugate scalar-Hasse zero")
    return boundary != 0 or period != 0


def boundary_zero_is_conjugate_fixed_log_derivative(prime: int) -> bool:
    """Certify W_M=0 iff theta D/D=-4/27 on the conjugate ordinary locus."""
    _, boundary, period, theta_period = boundary_kernel_from_conjugate_hasse_jet(prime)
    boundary_zero_avoids_conjugate_scalar_hasse(prime)
    if boundary != 0:
        return False
    target = (-4 * pow(27, -1, prime)) % prime
    actual = theta_period * pow(period, -1, prime) % prime
    if actual != target:
        raise AssertionError("conjugate fixed logarithmic-derivative criterion failed")
    return True


def original_and_conjugate_operators_are_formal_adjoints() -> bool:
    """Certify the conjugate d/dz operator is the negative formal adjoint.

    The original standard-form coefficients are

        a3=z^2(1-z),
        a2=3z-(9/2)z^2,
        a1=1-(19/6)z,
        a0=-5/54.

    For -L* the coefficients are

        b3=a3,
        b2=3a3'-a2,
        b1=3a3''-2a2'+a1,
        b0=a3'''-a2''+a1'-a0,

    which equal the conjugate coefficients with b0=-2/27.
    """
    for value in (Fraction(0), Fraction(1, 7), Fraction(1), Fraction(5, 3)):
        z = value
        a3 = z * z * (1 - z)
        a2 = 3 * z - Fraction(9, 2) * z * z
        a1 = 1 - Fraction(19, 6) * z
        a0 = Fraction(-5, 54)
        a3p = 2 * z - 3 * z * z
        a3pp = 2 - 6 * z
        a3ppp = -6
        a2p = 3 - 9 * z
        a2pp = -9
        a1p = Fraction(-19, 6)
        b3 = a3
        b2 = 3 * a3p - a2
        b1 = 3 * a3pp - 2 * a2p + a1
        b0 = a3ppp - a2pp + a1p - a0
        if b3 != z * z * (1 - z):
            raise AssertionError("adjoint leading coefficient changed")
        if b2 != 3 * z - Fraction(9, 2) * z * z:
            raise AssertionError("adjoint second coefficient changed")
        if b1 != 1 - Fraction(19, 6) * z:
            raise AssertionError("adjoint first coefficient changed")
        if b0 != Fraction(-2, 27):
            raise AssertionError("adjoint constant must equal conjugate parameter product")
    return True


def dual_hasse_lagrange_relation_at_one(prime: int) -> bool:
    """Certify 3(D theta P + P theta D)+PD=0 modulo p.

    The identity is the z=1 value of the Lagrange concomitant for the
    original operator and its exact formal adjoint.  The concomitant vanishes
    at z=0 because a3(0)=a2(0)=a3'(0)=0 and
    a3''(0)-a2'(0)+a1(0)=0.
    """
    _require_one_third_prime(prime)
    original_and_conjugate_operators_are_formal_adjoints()
    _, original, theta_original, _ = canonical_period_jets_residue(prime)
    _, conjugate, theta_conjugate, _ = conjugate_period_jets_residue(prime)
    residue = (
        3 * (conjugate * theta_original + original * theta_conjugate)
        + original * conjugate
    ) % prime
    if residue != 0:
        raise AssertionError("dual-Hasse Lagrange relation failed")
    return True


def dual_hasse_log_derivative_sum(prime: int) -> tuple[int, int, int]:
    """Return the two logarithmic derivatives and certify their sum is -1/3."""
    _require_one_third_prime(prime)
    dual_hasse_lagrange_relation_at_one(prime)
    _, original, theta_original, _ = canonical_period_jets_residue(prime)
    _, conjugate, theta_conjugate, _ = conjugate_period_jets_residue(prime)
    if original == 0 or conjugate == 0:
        raise ValueError("both scalar Hasse values must be nonzero")
    left = theta_original * pow(original, -1, prime) % prime
    right = theta_conjugate * pow(conjugate, -1, prime) % prime
    target = (-pow(3, -1, prime)) % prime
    if (left + right) % prime != target:
        raise AssertionError("dual Hasse logarithmic derivatives must sum to -1/3")
    return left, right, target


def franel_zero_dual_hasse_first_jet_pair(prime: int) -> bool:
    """At a one-third Franel zero certify the paired -5/27 and -4/27 jets."""
    _require_one_third_prime(prime)
    _, obstruction, original, theta_original = franel_obstruction_from_hasse_jet(prime)
    _, boundary, conjugate, theta_conjugate = boundary_kernel_from_conjugate_hasse_jet(prime)
    if obstruction != boundary:
        # The two integerizations differ by p-adic units in general, so only
        # their zero loci are required to agree.
        if (obstruction == 0) != (boundary == 0):
            raise AssertionError("original and conjugate boundary zero loci disagree")
    if obstruction != 0:
        return False
    if original == 0 or conjugate == 0:
        raise AssertionError("Franel zero must lie in both scalar ordinary loci")
    original_log = theta_original * pow(original, -1, prime) % prime
    conjugate_log = theta_conjugate * pow(conjugate, -1, prime) % prime
    if original_log != (-5 * pow(27, -1, prime)) % prime:
        raise AssertionError("original Franel first-jet target changed")
    if conjugate_log != (-4 * pow(27, -1, prime)) % prime:
        raise AssertionError("conjugate Franel first-jet target changed")
    dual_hasse_lagrange_relation_at_one(prime)
    return True
