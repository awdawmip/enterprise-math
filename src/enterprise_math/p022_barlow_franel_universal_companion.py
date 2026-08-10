"""Universal midpoint companions for all odd-prime Franel zero digits.

For an odd prime p put m=(p-1)/2.  Reflection and the Franel recurrence split
at the midpoint according to p modulo 8.

If p=5 or 7 mod8 then F_m=0 and the existing integer companion H has
H_0=0,H_1=1.  If p=1 or 3 mod8 then F_m is a unit.  Reflection at m together
with the recurrence gives

    F_(m-1) / F_m = -1/16 (mod p).

After the same denominator clearing, the complementary integer sequence K is

    K_0=2, K_1=-1,
    K_(d+1)=-(28d^2+1)K_d+8(2d-1)^4 K_(d-1).

For 1<=d<m, p divides F_(m-d) iff p divides H_d in the first residue pair and
iff p divides K_d in the second.  Reflection reconstructs the right half.
Thus H and K together encode the full zero-digit alphabet for every odd prime.

For a primitive rank r with q>4r-3, terminal cancellation at 2r-2 is a left
midpoint zero at offset d=(q-4r+3)/2, while the primitive zero itself has offset
e=(q-2r-1)/2.  Hence q must divide the same companion at both d and e and

    e-d=r-2,  q=4e-2d+5.

This converts the large-prime terminal problem to an affine common-zero problem
for one fixed integer recurrence.
"""

from __future__ import annotations

from functools import lru_cache

from .p022_barlow_franel_integer_companion import midpoint_integer_companion
from .p022_barlow_franel_lucas_rank import franel_zero_digits
from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_low_order_identifiability import triple_moment_factor


def _require_odd_prime(prime: int) -> None:
    if isinstance(prime, bool) or not isinstance(prime, int) or prime <= 2 or not _is_prime(prime):
        raise ValueError("prime must be an odd prime")


@lru_cache(maxsize=None)
def nonforced_midpoint_integer_companion(offset: int) -> int:
    """Complementary companion K_d for p=1 or3 mod8."""
    if isinstance(offset, bool) or not isinstance(offset, int) or offset < 0:
        raise ValueError("offset must be a non-negative integer")
    if offset == 0:
        return 2
    if offset == 1:
        return -1
    d = offset - 1
    return (
        -(28 * d * d + 1) * nonforced_midpoint_integer_companion(d)
        + 8 * (2 * d - 1) ** 4 * nonforced_midpoint_integer_companion(d - 1)
    )


def nonforced_midpoint_center_ratio_holds(prime: int) -> bool:
    """Certify 16 F_(m-1)+F_m=0 mod p for p=1 or3 mod8."""
    _require_odd_prime(prime)
    if prime % 8 not in (1, 3):
        raise ValueError("prime must be 1 or 3 modulo eight")
    middle = (prime - 1) // 2
    current = triple_moment_factor(middle) % prime
    previous = triple_moment_factor(middle - 1) % prime
    if current == 0:
        raise AssertionError("nonforced midpoint must be a p-unit")
    if (16 * previous + current) % prime:
        raise AssertionError("nonforced midpoint ratio must be -1/16")
    return True


def companion_kind(prime: int) -> str:
    _require_odd_prime(prime)
    return "H" if prime % 8 in (5, 7) else "K"


def universal_companion_value(prime: int, offset: int) -> int:
    """Return the integer companion selected by the prime residue class."""
    _require_odd_prime(prime)
    if isinstance(offset, bool) or not isinstance(offset, int) or offset < 0:
        raise ValueError("offset must be a non-negative integer")
    if companion_kind(prime) == "H":
        return midpoint_integer_companion(offset)
    return nonforced_midpoint_integer_companion(offset)


def universal_left_zero_offsets(prime: int) -> tuple[int, ...]:
    """All positive left-half zero offsets 1<=d<m from the selected companion."""
    _require_odd_prime(prime)
    middle = (prime - 1) // 2
    if companion_kind(prime) == "K":
        nonforced_midpoint_center_ratio_holds(prime)
    return tuple(
        offset
        for offset in range(1, middle)
        if universal_companion_value(prime, offset) % prime == 0
    )


def universal_zero_digits_from_companion(prime: int) -> tuple[int, ...]:
    """Reconstruct the complete nonzero q-digit Franel zero alphabet."""
    _require_odd_prime(prime)
    middle = (prime - 1) // 2
    offsets = universal_left_zero_offsets(prime)
    zeros = [middle - offset for offset in offsets]
    zeros.extend(middle + offset for offset in offsets)
    if companion_kind(prime) == "H":
        zeros.append(middle)
    return tuple(sorted(zeros))


def universal_companion_reconstructs_zero_digits(prime: int) -> bool:
    predicted = universal_zero_digits_from_companion(prime)
    actual = franel_zero_digits(prime)
    if predicted != actual:
        raise AssertionError("universal midpoint companions must reconstruct the zero alphabet")
    return True


def terminal_companion_offsets(rank: int, prime: int) -> tuple[int, int]:
    """Return (d,e) for terminal and primitive left-midpoint zeros."""
    _require_odd_prime(prime)
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 2:
        raise ValueError("rank must be an integer at least two")
    if prime <= 4 * rank - 3:
        raise ValueError("terminal and primitive zeros must both lie left of the midpoint")
    middle = (prime - 1) // 2
    d = middle - (2 * rank - 2)
    e = middle - rank
    if d <= 0 or e <= d or e - d != rank - 2:
        raise AssertionError("terminal companion offset arithmetic changed")
    if prime != 4 * e - 2 * d + 5:
        raise AssertionError("affine companion-prime identity changed")
    return d, e


def terminal_common_zero_companion_condition(rank: int, prime: int) -> tuple[int, int, str]:
    """Necessary companion condition for q|F_r and q|F_(2r-2), q>4r-3."""
    d, e = terminal_companion_offsets(rank, prime)
    if triple_moment_factor(rank) % prime or triple_moment_factor(2 * rank - 2) % prime:
        raise ValueError("prime must divide both declared Franel terms")
    kind = companion_kind(prime)
    if universal_companion_value(prime, d) % prime:
        raise AssertionError("terminal zero must hit the selected companion")
    if universal_companion_value(prime, e) % prime:
        raise AssertionError("primitive-side zero must hit the selected companion")
    return d, e, kind


def first_large_terminal_offsets_are_excluded(rank: int, prime: int) -> bool:
    """Exclude prime q=4r-1 and q=4r+1 terminal zeros by d=1,2 companions."""
    _require_odd_prime(prime)
    if prime not in (4 * rank - 1, 4 * rank + 1):
        raise ValueError("prime must be one of the first two large terminal candidates")
    if prime == 4 * rank - 1:
        offset = 1
    else:
        offset = 2
    value = universal_companion_value(prime, offset)
    if value % prime == 0:
        raise AssertionError("first large terminal candidate unexpectedly hits its companion")
    return True
