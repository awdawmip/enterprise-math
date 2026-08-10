"""Fourth-power counter-pressure for P025 cyclotomic forcing.

Odd-prime exponents have one linear and one nonlinear cyclotomic layer in each
sign, so threshold-one projective activation forces repetition in the nonlinear
factor.  Exponent four separates the two signs:

    p^4 + q^4 = Phi_8(p,q)

still has one top cyclotomic carrier (apart from its simple factor two), while

    p^4 - q^4 = Phi_1(p,q) Phi_2(p,q) Phi_4(p,q)

has two lower linear layers.  In centered coordinates A=(p-q)/2,
B=(p+q)/2 the difference atom becomes

    rho_4,- = m(A) m(A^2+B^2) / rad(B).

Thus the lower centered layer A can activate the atom even when the top
Phi_4=p^2+q^2 is squarefree.  This module records that exact negative boundary.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd

from .abc_support import multiplicity_residual, prime_factorization, radical
from .legendre import is_prime


@dataclass(frozen=True)
class FourthPowerCyclotomicBoundaryState:
    q: int
    p: int
    center: int
    radius: int
    centered_quadratic: int
    sum_top_half: int
    difference_component: int
    sum_component: int
    phi4: int
    phi4_squarefree: bool
    phi8_odd_part_squarefree: bool
    rho_difference: Fraction
    rho_sum: Fraction
    difference_lower_carrier_residual: int
    difference_top_residual: int
    sum_top_residual: int


def _squarefree(n: int) -> bool:
    return all(exponent == 1 for _prime, exponent in prime_factorization(n))


def fourth_power_cyclotomic_boundary_state(
    q: int, p: int
) -> FourthPowerCyclotomicBoundaryState:
    """Return exact centered/cyclotomic data for distinct odd primes p>q."""
    if any(isinstance(value, bool) or not isinstance(value, int) for value in (q, p)):
        raise ValueError("q and p must be integers")
    if not (3 <= q < p and is_prime(q) and is_prime(p)):
        raise ValueError("require distinct odd primes 3 <= q < p")

    A = (p - q) // 2
    B = (p + q) // 2
    if B + A != p or B - A != q:
        raise AssertionError("centered coordinates failed")
    if gcd(A, B) != 1:
        raise AssertionError("center and radius must be coprime")
    if A % 2 == B % 2:
        raise AssertionError("center and radius must have opposite parity")

    Q = A * A + B * B
    if gcd(A, Q) != 1 or gcd(B, Q) != 1:
        raise AssertionError("A, B, A^2+B^2 must be pairwise coprime")
    if Q % 2 != 1:
        raise AssertionError("centered quadratic factor must be odd")

    diff = p**4 - q**4
    summ = p**4 + q**4
    if diff != 8 * A * B * Q:
        raise AssertionError("fourth-power difference factorization failed")

    phi4 = p * p + q * q
    if phi4 != 2 * Q:
        raise AssertionError("Phi_4 lost centered quadratic form")

    H = B**4 + 6 * A * A * B * B + A**4
    if summ != 2 * H or H % 2 != 1:
        raise AssertionError("Phi_8 centered half-factorization failed")

    mA = multiplicity_residual(A)
    mB = multiplicity_residual(B)
    mQ = multiplicity_residual(Q)
    m_diff = multiplicity_residual(diff)
    if m_diff != 8 * mA * mB * mQ:
        raise AssertionError("fourth-power difference residual recomposition failed")

    rho_diff_direct = Fraction(m_diff, 4 * (p + q))
    rho_diff_centered = Fraction(mA * mQ, radical(B))
    if rho_diff_direct != rho_diff_centered:
        raise AssertionError("centered fourth-power difference atom disagreed")

    m_sum = multiplicity_residual(summ)
    mH = multiplicity_residual(H)
    if m_sum != mH:
        raise AssertionError("simple factor two should contribute no sum residual")
    rho_sum = Fraction(m_sum, 4 * (p + q))
    if rho_sum != Fraction(mH, 8 * B):
        raise AssertionError("centered fourth-power sum atom disagreed")

    # Every repeated odd prime in Phi_8 has ratio p/q of exact order 8.
    for r, exponent in prime_factorization(H):
        if exponent >= 2:
            if r % 8 != 1:
                raise AssertionError("repeated Phi_8 prime escaped 1 mod 8")
            modulus = r**exponent
            x = p * pow(q, -1, modulus) % modulus
            if pow(x, 8, modulus) != 1 or pow(x, 4, modulus) == 1:
                raise AssertionError("repeated Phi_8 ratio lost exact order eight")

    return FourthPowerCyclotomicBoundaryState(
        q=q,
        p=p,
        center=B,
        radius=A,
        centered_quadratic=Q,
        sum_top_half=H,
        difference_component=diff,
        sum_component=summ,
        phi4=phi4,
        phi4_squarefree=_squarefree(phi4),
        phi8_odd_part_squarefree=_squarefree(H),
        rho_difference=rho_diff_direct,
        rho_sum=rho_sum,
        difference_lower_carrier_residual=mA,
        difference_top_residual=mQ,
        sum_top_residual=mH,
    )


def fourth_power_top_forcing_boundary(q: int, p: int) -> dict[str, bool | Fraction]:
    """Expose the sign-dependent top-cyclotomic forcing boundary."""
    state = fourth_power_cyclotomic_boundary_state(q, p)
    sum_active = state.rho_sum >= 1
    diff_active = state.rho_difference >= 1
    if sum_active and state.phi8_odd_part_squarefree:
        raise AssertionError("sum activation must force repeated Phi_8 support")
    return {
        "sum_active": sum_active,
        "sum_top_repetition_forced": not state.phi8_odd_part_squarefree if sum_active else False,
        "difference_active": diff_active,
        "difference_top_squarefree": state.phi4_squarefree,
        "difference_counterexample_to_top_forcing": diff_active and state.phi4_squarefree,
        "rho_sum": state.rho_sum,
        "rho_difference": state.rho_difference,
    }
