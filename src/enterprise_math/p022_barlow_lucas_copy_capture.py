"""Force a composite defect at a p-Lucas copy of a primitive Franel zero.

Let r be a nontrivial twin-prime deferral center and q an odd primitive Franel
prime at rank r.  Since r is divisible by three, choose a in {1,2} by

    a=1 if q=2 mod3,  a=2 if q=1 mod3,

and put N=a*q+r.  Then 3 divides 2N-1, so D_N always exists.  The base-q digits
of N are (r,a), and F_a is a q-unit, hence p-Lucas forces q|F_N.

This gives a global capture interface independent of terminal cancellation.
If every q-divisible Franel support term in the canonical A_N relation has
nonpositive exponent, then

    v_q(D_N)=v_q(F_N)-sum alpha_j v_q(F_j) > 0.

Digit-local helpers below deliberately use the p-Lucas residue product rather
than constructing the full copied Franel number.  Exact huge-integer valuation
is deferred to the final capture verifier only.
"""

from __future__ import annotations

from .p022_barlow_franel_lucas_rank import (
    base_p_digits,
    franel_lucas_residue,
    franel_residue,
)
from .p022_barlow_low_order_defect_reduction import (
    _is_prime,
    composite_A_relation_exponents,
    franel_defect_valuation,
)
from .p022_barlow_low_order_identifiability import p_adic_valuation, triple_moment_factor
from .p022_barlow_primitive_defect_criterion import is_primitive_franel_divisor
from .p022_barlow_primitive_successor_capture import is_twin_prime_deferral_center


def forced_copy_multiplier(prime: int) -> int:
    if isinstance(prime, bool) or not isinstance(prime, int) or prime <= 3 or not _is_prime(prime):
        raise ValueError("prime must exceed three")
    residue = prime % 3
    if residue == 2:
        return 1
    if residue == 1:
        return 2
    raise AssertionError("prime greater than three is nonzero modulo three")


def forced_composite_copy_segment(rank: int, prime: int) -> tuple[int, int]:
    """Return (a,N) with N=a*q+r and 3|(2N-1)."""
    if not is_twin_prime_deferral_center(rank):
        raise ValueError("rank must be a twin-prime deferral center")
    if rank % 3:
        raise AssertionError("nontrivial twin centers are divisible by three")
    a = forced_copy_multiplier(prime)
    segment = a * prime + rank
    boundary = 2 * segment - 1
    if boundary <= 3 or boundary % 3:
        raise AssertionError("forced copy boundary must be a nontrivial multiple of three")
    if _is_prime(boundary):
        raise AssertionError("forced copy defect must exist")
    return a, segment


def forced_copy_is_q_divisible(rank: int, prime: int) -> bool:
    """p-Lucas certifies q|F_(a*q+r) without constructing F_(a*q+r)."""
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at rank")
    a, segment = forced_composite_copy_segment(rank, prime)
    if base_p_digits(segment, prime) != (rank, a):
        raise AssertionError("forced copy must have digits (r,a)")
    if franel_residue(a, prime) == 0:
        raise AssertionError("small leading copy digit must be a q-unit")
    if franel_lucas_residue(segment, prime) != 0:
        raise AssertionError("p-Lucas digit product must reproduce the primitive zero")
    return True


def forced_copy_q_divisible_support(rank: int, prime: int) -> tuple[tuple[int, int], ...]:
    """Canonical support terms predicted q-divisible by the p-Lucas digit product."""
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at rank")
    _, segment = forced_composite_copy_segment(rank, prime)
    exponents = composite_A_relation_exponents(segment)
    return tuple(
        (index, exponent)
        for index, exponent in exponents
        if franel_lucas_residue(index, prime) == 0
    )


def forced_copy_nonpositive_support_captures(rank: int, prime: int) -> int:
    """Sufficient global theorem: nonpositive q-support forces D_N>0."""
    forced_copy_is_q_divisible(rank, prime)
    _, segment = forced_composite_copy_segment(rank, prime)
    support = forced_copy_q_divisible_support(rank, prime)
    if any(exponent > 0 for _, exponent in support):
        raise ValueError("positive q-divisible support remains an unresolved cancellation channel")
    numerator_depth = p_adic_valuation(triple_moment_factor(segment), prime)
    if numerator_depth <= 0:
        raise AssertionError("forced p-Lucas copy must have positive q-depth")
    actual = franel_defect_valuation(segment, prime)
    if actual < numerator_depth or actual <= 0:
        raise AssertionError("nonpositive q-support can only strengthen the copy pivot")
    return actual
