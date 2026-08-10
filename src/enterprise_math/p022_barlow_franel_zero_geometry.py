"""Geometry of Franel zero digits inside one p-Lucas digit table.

Combines three exact ingredients:
- p-Lucas identifies digit zeros as the complete divisibility alphabet;
- Jarvis--Verrill reflects zeros by d -> p-1-d;
- the second-order Franel recurrence forbids adjacent zero digits.

For p=5 or 7 mod 8, the midpoint is a forced zero.  Reflection then shows that
it is primitive exactly when it is the *only* zero digit, i.e. when the p-Lucas
divisibility basin has its minimal alphabet size one.
"""

from __future__ import annotations

from .p022_barlow_franel_half_index import half_index, half_index_is_forced_zero
from .p022_barlow_franel_lucas_rank import (
    franel_rank_of_apparition,
    franel_zero_digits,
)
from .p022_barlow_low_order_defect_reduction import _is_prime


def _require_odd_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")


def zero_digits_are_reflection_symmetric(prime: int) -> bool:
    _require_odd_prime(prime)
    zeros = set(franel_zero_digits(prime))
    reflected = {prime - 1 - digit for digit in zeros}
    if reflected != zeros:
        raise AssertionError("Jarvis--Verrill reflection must preserve zero digits")
    return True


def zero_digits_are_nonadjacent(prime: int) -> bool:
    """No two positive digit indices can be consecutive zeros modulo p.

    If F_k=F_(k+1)=0 for 1<=k<=p-2, the Franel recurrence at k forces
    F_(k-1)=0 because 8*k^2 is a unit modulo p.  Backward propagation reaches
    F_0=1, a contradiction.
    """
    _require_odd_prime(prime)
    zeros = franel_zero_digits(prime)
    if any(right == left + 1 for left, right in zip(zeros, zeros[1:])):
        raise AssertionError("Franel recurrence forbids adjacent zero digits")
    return True


def forced_midpoint_zero_count_is_odd(prime: int) -> bool:
    _require_odd_prime(prime)
    if not half_index_is_forced_zero(prime):
        raise ValueError("midpoint is not forced in this residue class")
    zero_digits_are_reflection_symmetric(prime)
    midpoint = half_index(prime)
    zeros = franel_zero_digits(prime)
    if midpoint not in zeros:
        raise AssertionError("forced midpoint must be a zero digit")
    if len(zeros) % 2 != 1:
        raise AssertionError("fixed midpoint plus reflected pairs gives odd size")
    return True


def forced_midpoint_is_primitive(prime: int) -> bool:
    """Primitive-at-midpoint iff the forced zero alphabet is the singleton midpoint."""
    _require_odd_prime(prime)
    if not half_index_is_forced_zero(prime):
        raise ValueError("midpoint is not forced in this residue class")
    midpoint = half_index(prime)
    zeros = franel_zero_digits(prime)
    primitive_by_rank = franel_rank_of_apparition(prime) == midpoint
    primitive_by_alphabet = zeros == (midpoint,)
    if primitive_by_rank != primitive_by_alphabet:
        raise AssertionError("mirror symmetry makes midpoint primitivity equivalent to z_p=1")
    return primitive_by_rank


def forced_midpoint_profile(prime: int) -> tuple[int, int, int, bool]:
    """Return (midpoint, rank, zero_count, primitive_at_midpoint)."""
    _require_odd_prime(prime)
    if not half_index_is_forced_zero(prime):
        raise ValueError("midpoint is not forced in this residue class")
    midpoint = half_index(prime)
    rank = franel_rank_of_apparition(prime)
    if rank is None:
        raise AssertionError("forced midpoint guarantees finite rank")
    zero_count = len(franel_zero_digits(prime))
    primitive = forced_midpoint_is_primitive(prime)
    if rank > midpoint:
        raise AssertionError("forced midpoint gives rank <= midpoint")
    if zero_count % 2 != 1:
        raise AssertionError("forced zero alphabet must have odd size")
    return midpoint, rank, zero_count, primitive
