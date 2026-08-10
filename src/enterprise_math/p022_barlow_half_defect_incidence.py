"""Exact companion-incidence form of half-index Franel defect cancellation.

This module is deliberately broader than the target p=5 or 23 (mod 24) AP:
it accepts any forced-midpoint prime p=5 or 7 (mod 8) for which p-2 is
composite.  This includes p=157, the clean negative-boundary example.

For m=(p-1)/2 and canonical A-elimination exponents alpha_j,

    v_p(D_m) = v_p(F_m) - sum_j alpha_j v_p(F_j).

The integer midpoint companion converts the *support-level* zero test into

    p | F_j  iff  p | H_(m-j),   j<m.

Thus all possible cancellation locations are exact incidences between the
canonical A-support and the universal integer companion zero set.
"""

from __future__ import annotations

from .p022_barlow_franel_half_index import half_index, half_index_is_forced_zero
from .p022_barlow_franel_integer_companion import midpoint_integer_companion
from .p022_barlow_low_order_defect_reduction import (
    _is_prime,
    composite_A_relation_exponents,
    franel_defect_valuation,
)
from .p022_barlow_low_order_identifiability import p_adic_valuation, triple_moment_factor


def _require_generic_forced_composite_prime(prime: int) -> int:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
        or not half_index_is_forced_zero(prime)
    ):
        raise ValueError("prime must be a forced-midpoint odd prime")
    segment = half_index(prime)
    if _is_prime(2 * segment - 1):
        raise ValueError("p-2 must be composite so the canonical defect is defined")
    return segment


def half_defect_support_exponents_generic(prime: int) -> tuple[tuple[int, int], ...]:
    segment = _require_generic_forced_composite_prime(prime)
    return composite_A_relation_exponents(segment)


def half_defect_companion_zero_hits(prime: int) -> tuple[tuple[int, int, int], ...]:
    """Return exact support hits as (index j, offset d=m-j, exponent alpha_j)."""
    segment = _require_generic_forced_composite_prime(prime)
    hits = []
    for index, exponent in composite_A_relation_exponents(segment):
        offset = segment - index
        if offset <= 0:
            raise AssertionError("canonical composite support must be earlier than the segment")
        if midpoint_integer_companion(offset) % prime == 0:
            hits.append((index, offset, exponent))
    return tuple(hits)


def half_defect_support_avoidance_generic(prime: int) -> bool:
    return not half_defect_companion_zero_hits(prime)


def half_defect_valuation_terms(prime: int) -> tuple[int, tuple[tuple[int, int, int], ...], int]:
    """Return (midpoint valuation, nonzero correction terms, total defect valuation).

    A correction term is (j, alpha_j, v_p(F_j)) and is included only when the
    Franel valuation is positive.  The returned total is independently checked
    against the canonical defect-valuation implementation.
    """
    segment = _require_generic_forced_composite_prime(prime)
    midpoint_valuation = p_adic_valuation(triple_moment_factor(segment), prime)
    corrections = []
    correction_sum = 0
    for index, exponent in composite_A_relation_exponents(segment):
        valuation = p_adic_valuation(triple_moment_factor(index), prime)
        if valuation:
            corrections.append((index, exponent, valuation))
            correction_sum += exponent * valuation
    total = midpoint_valuation - correction_sum
    canonical = franel_defect_valuation(segment, prime)
    if total != canonical:
        raise AssertionError("valuation decomposition must match canonical Franel defect")
    return midpoint_valuation, tuple(corrections), total


def companion_hits_match_direct_franel_zeros(prime: int) -> bool:
    """Cross-check integer-companion support hits against direct Franel residues."""
    segment = _require_generic_forced_composite_prime(prime)
    companion_hits = {index for index, _, _ in half_defect_companion_zero_hits(prime)}
    direct_hits = {
        index
        for index, _ in composite_A_relation_exponents(segment)
        if triple_moment_factor(index) % prime == 0
    }
    if companion_hits != direct_hits:
        raise AssertionError("integer companion and direct Franel support zeros disagree")
    return True


def residual_prime_candidates(prime: int, index: int) -> tuple[int, ...]:
    """Prime q values for which j=(q+/-1)/2 at this support index.

    With d=m-j these are exactly q=p-2d and q=p-2d-2.
    Membership in the actual prime-halving tree is a separate stricter test.
    """
    segment = _require_generic_forced_composite_prime(prime)
    if isinstance(index, bool) or not isinstance(index, int) or not 1 <= index < segment:
        raise ValueError("index must be an earlier positive support index")
    offset = segment - index
    candidates = []
    for value in (prime - 2 * offset, prime - 2 * offset - 2):
        if value > 2 and _is_prime(value):
            candidates.append(value)
    return tuple(sorted(set(candidates)))
