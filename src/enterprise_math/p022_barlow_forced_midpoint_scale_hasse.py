"""Exact scale identity reducing forced-midpoint escape to one Hasse depth.

Let

    Psi(v) = product_j F_j^beta_j(v),

where beta(v) is the canonical central-binomial A-basis expansion of the
positive integer v, and put

    Delta_n = F_n Psi(n) / (2 F_(n-1) Psi(2n-1)).

When 2n-1 is composite, Delta_n is exactly the canonical pure Franel defect
D_n.  When 2n-1 is prime, the prime-generator identity gives Delta_n=1.

Now let q=6k-1 be prime and m=3k-1.  Using

    Psi(q) = Psi(3k) F_(3k)/(2F_(3k-1)),
    Psi(3k)/Psi(2k) = Psi(3)/Psi(2),
    2q-1 = 3(4k-1),

and the definition of Delta_(2k), one obtains the exact identity

    D_q = Delta_(2k)
          * F_q F_(m+1) F_(2k-1)
          / (4 F_(q-1) F_m F_(2k)).

For target primes q=5 or 23 (mod 24), m is the forced Franel midpoint.  If the
q-adic row has escaped every earlier defect, then v_q(Delta_(2k))=0: it is the
earlier defect D_(2k) when 4k-1 is composite, and is identically one when
4k-1 is prime.  The factors F_q,F_(q-1),F_(m+1) are q-units.  Therefore

    v_q(D_q)
      = v_q(F_(2k-1)) - v_q(F_(2k)) - v_q(F_m).

Consecutive single-digit Franel zeros are impossible.  Hence continued escape
through D_q forces the unique depth signature

    v_q(F_(2k-1)) = v_q(F_m) > 0,
    v_q(F_(2k)) = 0.

The companion Whipple theorem identifies F_(2k-1)=0 mod q with the canonical
scalar-Hasse condition P_q(1)=0.  Thus scalar-Hasse vanishing alone is not
enough for escape: its Franel depth must exactly match the forced midpoint
depth.
"""

from __future__ import annotations

from fractions import Fraction

from .p022_barlow_franel_half_index import (
    composite_boundary_half_witness,
)
from .p022_barlow_franel_third_index_minus_hasse import (
    third_minus_zero_iff_scalar_hasse_zero,
)
from .p022_barlow_low_order_defect_reduction import (
    _is_prime,
    evaluate_F_exponents,
    franel_defect,
    integer_in_central_binomial_basis,
)
from .p022_barlow_low_order_identifiability import (
    p_adic_valuation,
    triple_moment_factor,
)


def franel_transfer(value: int) -> Fraction:
    """Psi(v), the F-shadow of the canonical integer A-basis expansion."""
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("value must be positive")
    return evaluate_F_exponents(integer_in_central_binomial_basis(value))


def delta_value(segment: int) -> Fraction:
    """Exact Delta_n over Q."""
    if isinstance(segment, bool) or not isinstance(segment, int) or segment < 2:
        raise ValueError("segment must be at least two")
    return (
        Fraction(triple_moment_factor(segment), 1)
        * franel_transfer(segment)
        / (
            2
            * triple_moment_factor(segment - 1)
            * franel_transfer(2 * segment - 1)
        )
    )


def delta_matches_defect_or_prime_unit(segment: int) -> bool:
    """Certify Delta_n=D_n on composite boundaries and Delta_n=1 on prime ones."""
    if isinstance(segment, bool) or not isinstance(segment, int) or segment < 2:
        raise ValueError("segment must be at least two")
    boundary = 2 * segment - 1
    delta = delta_value(segment)
    if _is_prime(boundary):
        if delta != 1:
            raise AssertionError("prime odd boundary must make Delta_n exactly one")
        return True
    if delta != franel_defect(segment):
        raise AssertionError("composite odd boundary must make Delta_n equal D_n")
    return True


def forced_midpoint_scale_identity(prime: int) -> tuple[Fraction, Fraction]:
    """Return the two exact forms of D_q for q=6k-1 target primes."""
    midpoint, _ = composite_boundary_half_witness(prime)
    if prime % 6 != 5:
        raise AssertionError("target residue class must be 5 modulo six")
    k = (prime + 1) // 6
    if midpoint != 3 * k - 1:
        raise AssertionError("forced midpoint arithmetic changed")

    left = franel_defect(prime)
    right = (
        delta_value(2 * k)
        * triple_moment_factor(prime)
        * triple_moment_factor(midpoint + 1)
        * triple_moment_factor(2 * k - 1)
        / (
            4
            * triple_moment_factor(prime - 1)
            * triple_moment_factor(midpoint)
            * triple_moment_factor(2 * k)
        )
    )
    if left != right:
        raise AssertionError("forced-midpoint scale identity failed")
    return left, right


def earlier_delta_has_zero_q_valuation(
    prime: int,
    earlier_defect_valuation: int | None = None,
) -> bool:
    """Certify v_q(Delta_(2k))=0 under the declared earlier-escape hypothesis.

    If 4k-1 is composite, the caller supplies the already-observed valuation of
    D_(2k), which must be zero.  If 4k-1 is prime, Delta_(2k)=1 exactly and no
    supplied valuation is needed.
    """
    composite_boundary_half_witness(prime)
    k = (prime + 1) // 6
    segment = 2 * k
    boundary = 4 * k - 1
    delta_matches_defect_or_prime_unit(segment)
    if _is_prime(boundary):
        if earlier_defect_valuation is not None:
            raise ValueError("prime boundary has no D_(2k) valuation to supply")
        return True
    if earlier_defect_valuation != 0:
        raise ValueError("complete earlier escape requires v_q(D_(2k))=0")
    return True


def forced_escape_at_q_depth_signature(
    prime: int,
    earlier_defect_valuation: int | None = None,
) -> tuple[int, int, int]:
    """Under earlier escape, return the three depths controlling v_q(D_q).

    The output is

        (v_q(F_(2k-1)), v_q(F_(2k)), v_q(F_m)).

    If v_q(D_q)=0, the function additionally certifies the unique equality
    signature first=third>0 and second=0.
    """
    midpoint, _ = composite_boundary_half_witness(prime)
    k = (prime + 1) // 6
    earlier_delta_has_zero_q_valuation(prime, earlier_defect_valuation)

    first = p_adic_valuation(triple_moment_factor(2 * k - 1), prime)
    second = p_adic_valuation(triple_moment_factor(2 * k), prime)
    middle = p_adic_valuation(triple_moment_factor(midpoint), prime)
    if middle <= 0:
        raise AssertionError("target midpoint must have positive q-depth")
    if first > 0 and second > 0:
        raise AssertionError("adjacent single-digit Franel zeros are impossible")

    actual = p_adic_valuation(
        forced_midpoint_scale_identity(prime)[0].numerator,
        prime,
    ) - p_adic_valuation(
        forced_midpoint_scale_identity(prime)[0].denominator,
        prime,
    )
    predicted = first - second - middle
    if actual != predicted:
        raise AssertionError("D_q valuation disagrees with the scale reduction")
    if actual == 0:
        if not (first == middle and first > 0 and second == 0):
            raise AssertionError("continued escape has the wrong depth signature")
        if not third_minus_zero_iff_scalar_hasse_zero(prime):
            raise AssertionError("continued escape must be scalar-Hasse exceptional")
    return first, second, middle
