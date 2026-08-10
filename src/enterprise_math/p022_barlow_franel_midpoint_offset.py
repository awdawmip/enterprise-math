"""Universal midpoint-offset companion for forced Franel zero digits.

For p=5 or 7 (mod 8), let m=(p-1)/2.  The forced midpoint satisfies F_m=0
mod p and recurrence nonadjacency gives F_(m-1)!=0 mod p.  Writing

    F_(m-d) / F_(m-1) = G_d  (mod p)

removes p completely from the Franel recurrence:

    G_0=0, G_1=1,
    8(2d+1)^2 G_(d+1)
      = (2d-1)^2 G_(d-1) - (28d^2+1) G_d.

Hence the entire digit-zero geometry for every forced-midpoint prime is encoded
by one universal rational sequence.  If N_d is the reduced numerator of G_d,
then for 1<=d<m,

    p | F_(m-d)  iff  p | N_d.

Reflection gives the right-side zeros.  Thus the Franel rank of apparition is
m minus the largest companion offset hit.
"""

from __future__ import annotations

from fractions import Fraction
from functools import lru_cache

from .p022_barlow_franel_half_index import half_index, half_index_is_forced_zero
from .p022_barlow_franel_lucas_rank import franel_rank_of_apparition, franel_zero_digits
from .p022_barlow_low_order_defect_reduction import _is_prime


def _require_forced_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
        or not half_index_is_forced_zero(prime)
    ):
        raise ValueError("prime must be an odd prime in 5 or 7 modulo 8")


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


@lru_cache(maxsize=None)
def midpoint_companion_fraction(offset: int) -> Fraction:
    """Exact universal rational G_d."""
    _require_natural("offset", offset)
    if offset == 0:
        return Fraction(0, 1)
    if offset == 1:
        return Fraction(1, 1)
    d = offset - 1
    previous = midpoint_companion_fraction(d - 1)
    current = midpoint_companion_fraction(d)
    return (
        (2 * d - 1) ** 2 * previous
        - (28 * d * d + 1) * current
    ) / (8 * (2 * d + 1) ** 2)


def midpoint_companion_numerator(offset: int) -> int:
    return midpoint_companion_fraction(offset).numerator


def midpoint_companion_denominator(offset: int) -> int:
    return midpoint_companion_fraction(offset).denominator


def midpoint_companion_table_mod(prime: int, max_offset: int) -> tuple[int, ...]:
    """G_0,...,G_max modulo p when all recurrence denominators are units."""
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")
    _require_natural("max_offset", max_offset)
    if 2 * max_offset - 1 >= prime and max_offset > 0:
        raise ValueError("offset range must keep all odd recurrence denominators below p")
    if max_offset == 0:
        return (0,)
    values = [0, 1]
    for d in range(1, max_offset):
        numerator = (
            (2 * d - 1) ** 2 * values[d - 1]
            - (28 * d * d + 1) * values[d]
        ) % prime
        denominator = (8 * (2 * d + 1) ** 2) % prime
        values.append(numerator * pow(denominator, -1, prime) % prime)
    return tuple(values)


def left_zero_offsets_from_companion(prime: int) -> tuple[int, ...]:
    """Offsets d with 1<=d<m and p|N_d."""
    _require_forced_prime(prime)
    midpoint = half_index(prime)
    if midpoint <= 1:
        return ()
    table = midpoint_companion_table_mod(prime, midpoint - 1)
    return tuple(offset for offset in range(1, midpoint) if table[offset] == 0)


def zero_digits_from_companion(prime: int) -> tuple[int, ...]:
    """Reconstruct the complete Franel zero-digit set from companion offsets."""
    _require_forced_prime(prime)
    midpoint = half_index(prime)
    offsets = left_zero_offsets_from_companion(prime)
    predicted = tuple(
        sorted(
            [midpoint]
            + [midpoint - offset for offset in offsets]
            + [midpoint + offset for offset in offsets]
        )
    )
    return predicted


def companion_reconstructs_zero_digits(prime: int) -> bool:
    predicted = zero_digits_from_companion(prime)
    actual = franel_zero_digits(prime)
    if predicted != actual:
        raise AssertionError("midpoint companion must reconstruct the full zero alphabet")
    return True


def rank_from_midpoint_companion(prime: int) -> int:
    """Exact r_p from the largest left zero offset."""
    _require_forced_prime(prime)
    midpoint = half_index(prime)
    offsets = left_zero_offsets_from_companion(prime)
    predicted = midpoint - max(offsets, default=0)
    actual = franel_rank_of_apparition(prime)
    if actual != predicted:
        raise AssertionError("companion offset formula must reproduce Franel rank")
    return predicted


def companion_prime_hits(offset: int, prime: int) -> bool:
    """Exact integer numerator criterion p|N_d for ranges with p>2d-1."""
    _require_natural("offset", offset)
    if offset == 0:
        return True
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")
    if prime <= 2 * offset - 1:
        raise ValueError("prime must exceed every recurrence denominator factor")
    denominator = midpoint_companion_denominator(offset)
    if denominator % prime == 0:
        raise AssertionError("declared range must make the reduced denominator a p-unit")
    return midpoint_companion_numerator(offset) % prime == 0
