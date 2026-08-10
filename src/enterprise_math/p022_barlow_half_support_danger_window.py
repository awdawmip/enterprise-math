"""Linear prime-size window for target half-defect support cancellation.

Combine the target-family A-support localization with the integer midpoint
companion K_d.  If a target prime p divides K_d and the reflected index
j=m-d actually lies in the canonical A-support, then p cannot be arbitrarily
large compared with d.

Necessary windows:

    p = 5  (mod 24):   2d+1 < p <= 3d+2,
    p = 23 (mod 24):   2d+1 < p <= 4d+3.

The lower bound is just d<m=(p-1)/2.  The upper bounds are the support
localization inequalities rewritten in terms of d.  Hence all sufficiently
large prime divisors of K_d are automatically harmless for the target defect
family, even when they generate a Franel zero.
"""

from __future__ import annotations

from .p022_barlow_franel_half_index import composite_boundary_half_witness
from .p022_barlow_franel_half_integer_solution import integer_midpoint_companion
from .p022_barlow_half_support_localization import (
    target_half_support_localization,
    target_support_offsets,
)
from .p022_barlow_low_order_defect_reduction import _is_prime


def _require_offset(offset: int) -> None:
    if isinstance(offset, bool) or not isinstance(offset, int) or offset <= 0:
        raise ValueError("offset must be positive")


def target_danger_window(offset: int, residue: int) -> tuple[int, int]:
    """Return (strict lower bound, inclusive upper bound) for target p."""
    _require_offset(offset)
    if residue == 5:
        return 2 * offset + 1, 3 * offset + 2
    if residue == 23:
        return 2 * offset + 1, 4 * offset + 3
    raise ValueError("residue must be 5 or 23 modulo 24")


def target_prime_is_in_danger_window(offset: int, prime: int) -> bool:
    _require_offset(offset)
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 5
        or not _is_prime(prime)
        or prime % 24 not in (5, 23)
    ):
        raise ValueError("prime must exceed five and lie in 5 or 23 modulo 24")
    lower, upper = target_danger_window(offset, prime % 24)
    return lower < prime <= upper


def large_companion_prime_is_automatically_safe(offset: int, prime: int) -> bool:
    """A target K_d prime above the danger window cannot be an A-support hit."""
    _require_offset(offset)
    if integer_midpoint_companion(offset) % prime:
        raise ValueError("prime must divide the declared integer companion term K_d")
    if prime <= 2 * offset + 1:
        raise ValueError("prime does not define a valid forced-midpoint offset d<m")
    return not target_prime_is_in_danger_window(offset, prime)


def actual_support_offset_obeys_danger_window(prime: int, offset: int) -> bool:
    """Certify the necessary bound for one actual nontrivial support offset."""
    midpoint, _ = composite_boundary_half_witness(prime)
    if isinstance(offset, bool) or not isinstance(offset, int) or not 1 <= offset < midpoint:
        raise ValueError("offset must lie in 1..m-1")
    offsets = target_support_offsets(prime)
    if offset not in offsets:
        raise ValueError("offset is not in the canonical A-support")
    if offset == 1:
        # The theorem concerns the nontrivial far-support part. K_1=1 anyway.
        return True
    if not target_prime_is_in_danger_window(offset, prime):
        raise AssertionError("localized support offset must lie in the prime danger window")
    return True


def possible_target_cancellation_at_offset(offset: int, prime: int) -> bool:
    """Necessary-condition filter for a target support cancellation.

    True means only that:
    - p is a target-family prime in the required size window;
    - p divides K_d.

    Actual A-support membership remains an additional condition.
    """
    if not target_prime_is_in_danger_window(offset, prime):
        return False
    return integer_midpoint_companion(offset) % prime == 0


def target_support_window_profile(prime: int) -> tuple[int, tuple[int, ...], tuple[int, ...]]:
    """Return (bound, actual nontrivial offsets, window-certified offsets)."""
    bound, _ = target_half_support_localization(prime)
    offsets = tuple(offset for offset in target_support_offsets(prime) if offset != 1)
    certified = tuple(
        offset for offset in offsets if target_prime_is_in_danger_window(offset, prime)
    )
    if certified != offsets:
        raise AssertionError("every nontrivial support offset must satisfy the danger window")
    return bound, offsets, certified
