"""Necessary prime-window and root-incidence conditions for P022 half defects.

For the target primes p=5 or 23 (mod 24), m=(p-1)/2, a non-adjacent
canonical support hit at j=m-d must satisfy the support-tree location bounds.
Together with 0<d<m this traps a dangerous companion prime in a thin interval:

    p=5  (mod 24):  2d+3 <= p <= 3d+2,
    p=23 (mod 24):  2d+3 <= p <= 4d+3.

If a candidate comes directly from an odd prime root q|p-2, write
p-2=(2t+1)q.  Then its two A-indices correspond exactly to offsets

    d=tq        for j=(q+1)/2,
    d=tq+1      for j=(q-1)/2.

Because all target primes satisfy p=2 (mod 3), every such root q!=3 forces
2t+1=0 (mod 3), hence t=1 (mod 3).  The q=3 root is automatically harmless
for p>5 because its A-indices are 1 and 2 and F_1=2,F_2=10 are p-units.

These are necessary conditions only; descendant nodes remain the open case.
"""

from __future__ import annotations

from .p022_barlow_franel_half_index import composite_boundary_half_witness
from .p022_barlow_franel_integer_companion import midpoint_integer_companion
from .p022_barlow_half_defect_support_tree import target_low_support_bound
from .p022_barlow_low_order_defect_reduction import _factor_integer, _is_prime


def dangerous_prime_window(offset: int, residue_class: int) -> tuple[int, int]:
    """Return inclusive necessary p-window for a target non-adjacent hit."""
    if isinstance(offset, bool) or not isinstance(offset, int) or offset <= 0:
        raise ValueError("offset must be a positive integer")
    if residue_class == 5:
        return 2 * offset + 3, 3 * offset + 2
    if residue_class == 23:
        return 2 * offset + 3, 4 * offset + 3
    raise ValueError("residue_class must be 5 or 23 modulo 24")


def target_prime_lies_in_dangerous_window(prime: int, offset: int) -> bool:
    composite_boundary_half_witness(prime)
    lower, upper = dangerous_prime_window(offset, prime % 24)
    return lower <= prime <= upper


def target_companion_zero_is_automatically_off_support(prime: int, offset: int) -> bool:
    """True when p|H_d but the AP location bound alone excludes support."""
    segment, _ = composite_boundary_half_witness(prime)
    if isinstance(offset, bool) or not isinstance(offset, int) or not 1 <= offset < segment:
        raise ValueError("offset must lie in 1..m-1")
    if midpoint_integer_companion(offset) % prime:
        raise ValueError("declared offset is not a companion zero modulo p")
    return not target_prime_lies_in_dangerous_window(prime, offset)


def p_minus_two_odd_prime_roots(prime: int) -> tuple[int, ...]:
    """Odd prime roots q of p-2 for the target family."""
    _, _ = composite_boundary_half_witness(prime)
    return tuple(q for q, _ in _factor_integer(prime - 2) if q != 2)


def root_quotient_parameters(prime: int, root_prime: int) -> tuple[int, int]:
    """Return (a,t) with p-2=a*q=(2t+1)q for a root q|p-2."""
    composite_boundary_half_witness(prime)
    if (
        isinstance(root_prime, bool)
        or not isinstance(root_prime, int)
        or root_prime <= 2
        or not _is_prime(root_prime)
        or (prime - 2) % root_prime
    ):
        raise ValueError("root_prime must be an odd prime divisor of p-2")
    quotient = (prime - 2) // root_prime
    if quotient % 2 == 0:
        raise AssertionError("odd divided by odd must give an odd quotient")
    return quotient, (quotient - 1) // 2


def root_candidate_offsets(prime: int, root_prime: int) -> tuple[int, int]:
    """Offsets for j=(q+1)/2 and j=(q-1)/2 respectively."""
    _, t = root_quotient_parameters(prime, root_prime)
    return t * root_prime, t * root_prime + 1


def target_root_mod3_condition(prime: int, root_prime: int) -> bool:
    """Certify q=3 harmless or t=1 mod3 for every other p-2 root."""
    composite_boundary_half_witness(prime)
    quotient, t = root_quotient_parameters(prime, root_prime)
    if root_prime == 3:
        return True
    if quotient % 3:
        raise AssertionError("target p=2 mod3 forces the cofactor to be divisible by three")
    if t % 3 != 1:
        raise AssertionError("odd cofactor divisible by three means t=1 mod3")
    return True


def root_candidate_indices(prime: int, root_prime: int) -> tuple[int, int]:
    """The two adjacent A-indices produced by one p-2 root q."""
    root_quotient_parameters(prime, root_prime)
    return (root_prime + 1) // 2, (root_prime - 1) // 2


def root_incidence_is_companion_zero(prime: int, root_prime: int) -> tuple[bool, bool]:
    """Whether either direct p-2-root candidate is a companion zero."""
    offsets = root_candidate_offsets(prime, root_prime)
    return tuple(midpoint_integer_companion(d) % prime == 0 for d in offsets)  # type: ignore[return-value]


def target_window_matches_support_bound(prime: int) -> bool:
    """Algebraic cross-check of the p/d window against the j-bound."""
    segment, _ = composite_boundary_half_witness(prime)
    bound = target_low_support_bound(prime)
    floor = segment - bound
    lower, upper = dangerous_prime_window(floor, prime % 24)
    # The lower endpoint is automatic from d<m; the upper endpoint is the
    # rearranged support location inequality and should contain p.
    return lower <= prime <= upper
