"""Local transfer form of the P022 composite Franel defects.

The central-binomial recurrence gives a canonical multiplicative expression of
every positive integer in the A_j=C(2j,j) basis.  Substitute F_j for A_j in
that expression and call the resulting positive rational Psi(m).

For every n>=2 define

    Delta_n = F_n * Psi(n) / (2*F_(n-1)*Psi(2n-1)).

If 2n-1 is prime, the prime recursion defining Psi forces Delta_n=1 exactly.
If 2n-1 is composite, Delta_n is exactly the pure Franel defect D_n from the
A-coordinate elimination theorem.

At each valuation prime p, psi_p=v_p(Psi) is completely additive and obeys a
smaller-index prime recursion.  Thus every composite defect coordinate is
computed from the prime factors of n and 2n-1 plus local Franel valuation
increments, without a joint determinant.
"""

from __future__ import annotations

from fractions import Fraction

from .p022_barlow_low_order_defect_reduction import (
    composite_A_relation_exponents,
    evaluate_F_exponents,
    franel_defect,
    franel_defect_valuation,
    integer_in_central_binomial_basis,
    primes_through,
)
from .p022_barlow_low_order_identifiability import (
    p_adic_valuation,
    triple_moment_factor,
)


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _is_prime(value: int) -> bool:
    return value in primes_through(value)


def franel_transfer(value: int) -> Fraction:
    """Psi(value): substitute F_j for A_j in the canonical integer A-basis."""
    _require_positive("value", value)
    return evaluate_F_exponents(integer_in_central_binomial_basis(value))


def franel_transfer_valuation(value: int, prime: int) -> int:
    """psi_p(value)=v_p(Psi(value)) from the canonical exponent vector."""
    _require_positive("value", value)
    _require_positive("prime", prime)
    return sum(
        exponent * p_adic_valuation(triple_moment_factor(index), prime)
        for index, exponent in integer_in_central_binomial_basis(value)
    )


def boundary_transfer_defect(segment: int) -> Fraction:
    """Unified Delta_n, equal to one at prime odd boundaries and D_n at composite ones."""
    _require_positive("segment", segment)
    if segment < 2:
        raise ValueError("boundary defect starts at segment two")
    numerator = Fraction(triple_moment_factor(segment), 1) * franel_transfer(segment)
    denominator = (
        Fraction(2 * triple_moment_factor(segment - 1), 1)
        * franel_transfer(2 * segment - 1)
    )
    return numerator / denominator


def boundary_transfer_defect_valuation(segment: int, prime: int) -> int:
    """Local p-adic formula for Delta_n."""
    _require_positive("segment", segment)
    _require_positive("prime", prime)
    if segment < 2:
        raise ValueError("boundary defect starts at segment two")
    delta_2 = 1 if prime == 2 else 0
    return (
        p_adic_valuation(triple_moment_factor(segment), prime)
        - p_adic_valuation(triple_moment_factor(segment - 1), prime)
        + franel_transfer_valuation(segment, prime)
        - delta_2
        - franel_transfer_valuation(2 * segment - 1, prime)
    )


def odd_prime_transfer_recursion(prime_boundary: int, valuation_prime: int) -> tuple[int, int]:
    """Return both sides of the exact valuation recursion for one odd prime q.

    If q=2j-1 is prime, then

        psi_p(q)
          = psi_p(j) - 1_(p=2) + f_p(j)-f_p(j-1).
    """
    _require_positive("prime_boundary", prime_boundary)
    _require_positive("valuation_prime", valuation_prime)
    if prime_boundary == 2 or not _is_prime(prime_boundary):
        raise ValueError("prime_boundary must be an odd prime")
    j = (prime_boundary + 1) // 2
    lhs = franel_transfer_valuation(prime_boundary, valuation_prime)
    rhs = (
        franel_transfer_valuation(j, valuation_prime)
        - (1 if valuation_prime == 2 else 0)
        + p_adic_valuation(triple_moment_factor(j), valuation_prime)
        - p_adic_valuation(triple_moment_factor(j - 1), valuation_prime)
    )
    return lhs, rhs


def prime_boundary_defect_is_trivial(segment: int) -> bool:
    _require_positive("segment", segment)
    if segment < 2 or not _is_prime(2 * segment - 1):
        raise ValueError("segment must have prime odd boundary")
    return boundary_transfer_defect(segment) == 1


def composite_boundary_defect_matches_reduction(segment: int) -> bool:
    _require_positive("segment", segment)
    if segment < 2 or _is_prime(2 * segment - 1):
        raise ValueError("segment must have composite odd boundary")
    return boundary_transfer_defect(segment) == franel_defect(segment)


def composite_defect_local_formula(
    segment: int, prime: int
) -> tuple[int, int]:
    """Compare transfer-local valuation with the A-elimination defect valuation."""
    _require_positive("segment", segment)
    _require_positive("prime", prime)
    if segment < 2 or _is_prime(2 * segment - 1):
        raise ValueError("segment must have composite odd boundary")
    return (
        boundary_transfer_defect_valuation(segment, prime),
        franel_defect_valuation(segment, prime),
    )
