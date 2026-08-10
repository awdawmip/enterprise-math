"""Structural localization of the canonical half-defect A-elimination support.

For the target infinite residue family p=5 or 23 (mod 24), m=(p-1)/2 and
p-2 is an odd multiple of three.  The canonical A-relation is built from
A_(m-1), the integer central-binomial-basis expansion of p-2, and that of m.

If P(v) is the largest prime factor of v, the recursive basis expansion of an
integer v uses no A-index above (P(v)+1)/2.  This yields:

- p=5 mod 24: aside from m-1, support j <= floor((m+1)/3);
- p=23 mod 24: aside from m-1, support j <= (m+1)/2.

Therefore only far midpoint-companion offsets can ever cancel the forced
Franel witness.  Near-midpoint zero digits are automatically support-safe.
"""

from __future__ import annotations

from .p022_barlow_franel_half_index import composite_boundary_half_witness
from .p022_barlow_low_order_defect_reduction import (
    _factor_integer,
    composite_A_relation_exponents,
    integer_in_central_binomial_basis,
)


def largest_prime_factor(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 1:
        raise ValueError("value must exceed one")
    return _factor_integer(value)[-1][0]


def integer_basis_index_bound(value: int) -> int:
    """Universal support bound (P(value)+1)/2 for the A-basis of an integer."""
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError("value must be positive")
    if value == 1:
        return 0
    prime = largest_prime_factor(value)
    return (prime + 1) // 2


def integer_basis_respects_index_bound(value: int) -> bool:
    """Executable check of the recursive prime-halving support bound."""
    bound = integer_basis_index_bound(value)
    support = tuple(index for index, _ in integer_in_central_binomial_basis(value))
    if support and max(support) > bound:
        raise AssertionError("central-binomial integer basis exceeded prime-halving bound")
    return True


def target_half_support_small_index_bound(prime: int) -> int:
    """Bound for every canonical support index except the explicit m-1 term."""
    midpoint, _ = composite_boundary_half_witness(prime)
    residue = prime % 24
    if residue == 5:
        # m is even (>2), so P(m)<=m/2.  Also p-2=2m-1 is an odd
        # composite multiple of three, hence P(p-2)<=(p-2)/3.
        return (midpoint + 1) // 3
    if residue == 23:
        # m may itself be prime, so only P(m)<=m is universal.
        return (midpoint + 1) // 2
    raise AssertionError("composite_boundary_half_witness must lie in 5 or 23 mod24")


def target_half_support_localization(prime: int) -> tuple[int, tuple[int, ...]]:
    """Return (small-index bound, canonical support) and certify localization."""
    midpoint, _ = composite_boundary_half_witness(prime)
    relation = composite_A_relation_exponents(midpoint)
    support = tuple(index for index, _ in relation)
    bound = target_half_support_small_index_bound(prime)
    exceptional = midpoint - 1
    if any(index != exceptional and index > bound for index in support):
        raise AssertionError("target half-support localization failed")
    return bound, support


def dangerous_companion_offset_floor(prime: int) -> int:
    """Smallest nontrivial offset that can possibly hit the small support.

    Offset 1 corresponds to the explicit support index m-1.  Every other
    support index j is <=B, hence its offset d=m-j is >=m-B.
    """
    midpoint, _ = composite_boundary_half_witness(prime)
    bound = target_half_support_small_index_bound(prime)
    return midpoint - bound


def automatically_safe_companion_offset(prime: int, offset: int) -> bool:
    """Whether localization alone proves an offset cannot be in A-support."""
    midpoint, _ = composite_boundary_half_witness(prime)
    if isinstance(offset, bool) or not isinstance(offset, int) or not 1 <= offset < midpoint:
        raise ValueError("offset must lie in 1..m-1")
    if offset == 1:
        return False
    return offset < dangerous_companion_offset_floor(prime)


def target_support_offsets(prime: int) -> tuple[int, ...]:
    midpoint, _ = composite_boundary_half_witness(prime)
    _, support = target_half_support_localization(prime)
    return tuple(sorted(midpoint - index for index in support))
