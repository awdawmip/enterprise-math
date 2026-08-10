"""Canonical half-defect support as a universal companion-avoidance problem.

For any forced-midpoint prime p=5 or 7 (mod 8) whose A-boundary p-2 is
composite, let m=(p-1)/2 and write the canonical central-binomial elimination

    A_m = product_(j<m) A_j^alpha_j.

The elimination support meets an earlier Franel zero exactly when one of the
universal midpoint companion numerators N_(m-j) is divisible by p.  This is an
exact coordinate change, not a new conjecture.

The prime p=157 is a sharp negative boundary: m=78 and the canonical support
contains j=16 with exponent +1.  Since 157 divides both F_78 and F_16 once,
the forced midpoint valuation cancels completely and v_157(D_78)=0.
"""

from __future__ import annotations

from .p022_barlow_franel_half_index import half_index, half_index_is_forced_zero
from .p022_barlow_franel_midpoint_offset import midpoint_companion_table_mod
from .p022_barlow_low_order_defect_reduction import (
    _is_prime,
    composite_A_relation_exponents,
    franel_defect_valuation,
)
from .p022_barlow_low_order_identifiability import (
    p_adic_valuation,
    triple_moment_factor,
)


def _require_forced_composite_boundary_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 5
        or not _is_prime(prime)
        or not half_index_is_forced_zero(prime)
    ):
        raise ValueError("prime must exceed five and lie in 5 or 7 modulo 8")
    midpoint = half_index(prime)
    boundary = 2 * midpoint - 1
    if _is_prime(boundary):
        raise ValueError("forced midpoint must lie on a composite A-boundary")


def canonical_half_A_relation(prime: int) -> tuple[tuple[int, int], ...]:
    _require_forced_composite_boundary_prime(prime)
    return composite_A_relation_exponents(half_index(prime))


def canonical_half_support(prime: int) -> tuple[int, ...]:
    return tuple(index for index, _ in canonical_half_A_relation(prime))


def canonical_half_support_offsets(prime: int) -> tuple[int, ...]:
    midpoint = half_index(prime)
    return tuple(sorted(midpoint - index for index in canonical_half_support(prime)))


def companion_support_hits(prime: int) -> tuple[tuple[int, int, int], ...]:
    """Return (Franel index j, A exponent alpha_j, midpoint offset d) hits."""
    _require_forced_composite_boundary_prime(prime)
    midpoint = half_index(prime)
    relation = canonical_half_A_relation(prime)
    offsets = tuple(midpoint - index for index, _ in relation)
    max_offset = max(offsets, default=0)
    table = midpoint_companion_table_mod(prime, max_offset)
    return tuple(
        (index, exponent, midpoint - index)
        for index, exponent in relation
        if table[midpoint - index] == 0
    )


def companion_support_avoidance_holds(prime: int) -> bool:
    return not companion_support_hits(prime)


def direct_support_zero_hits(prime: int) -> tuple[int, ...]:
    """Direct Franel-table definition used to cross-check the companion coordinate."""
    _require_forced_composite_boundary_prime(prime)
    return tuple(
        index
        for index in canonical_half_support(prime)
        if triple_moment_factor(index) % prime == 0
    )


def companion_support_equivalence(prime: int) -> bool:
    """Certify direct zero hits == companion numerator hits."""
    direct = direct_support_zero_hits(prime)
    companion = tuple(index for index, _, _ in companion_support_hits(prime))
    if direct != companion:
        raise AssertionError("companion offsets must exactly encode support zero hits")
    return True


def support_valuation_correction(prime: int) -> int:
    """Sum alpha_j*v_p(F_j) over the canonical A-elimination support."""
    _require_forced_composite_boundary_prime(prime)
    return sum(
        exponent * p_adic_valuation(triple_moment_factor(index), prime)
        for index, exponent in canonical_half_A_relation(prime)
    )


def midpoint_defect_valuation(prime: int) -> int:
    """Exact v_p(D_m) from the existing pure Franel defect definition."""
    _require_forced_composite_boundary_prime(prime)
    return franel_defect_valuation(half_index(prime), prime)


def p157_cancellation_certificate() -> tuple[
    tuple[tuple[int, int], ...], tuple[tuple[int, int, int], ...], int, int, int
]:
    """Exact negative boundary at the first observed support-cancellation prime.

    Returns (A_relation, companion_hits, v_157(F_78), support_correction,
    v_157(D_78)).
    """
    prime = 157
    midpoint = 78
    relation = canonical_half_A_relation(prime)
    hits = companion_support_hits(prime)
    midpoint_valuation = p_adic_valuation(triple_moment_factor(midpoint), prime)
    correction = support_valuation_correction(prime)
    defect = midpoint_defect_valuation(prime)
    expected_relation = (
        (1, 2),
        (2, -1),
        (3, 2),
        (4, -1),
        (6, 1),
        (7, -1),
        (15, -1),
        (16, 1),
        (77, 1),
    )
    if relation != expected_relation:
        raise AssertionError("p=157 canonical A-relation changed")
    if hits != ((16, 1, 62),):
        raise AssertionError("p=157 must hit exactly the offset-62 companion zero")
    if (midpoint_valuation, correction, defect) != (1, 1, 0):
        raise AssertionError("p=157 forced midpoint valuation must cancel exactly")
    return relation, hits, midpoint_valuation, correction, defect
