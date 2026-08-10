"""Midpoint-zero obstruction for complete twin-row escape.

The exact twin escape kernel says that every positive Franel depth strictly
inside the first-reentry blackout must sit at a twin-prime center.  Prior-art
Franel congruences give a universal fixed point of the Jarvis--Verrill
reflection: for an odd prime q,

    q | F_((q-1)/2)  iff  q = 5 or 7 (mod 8).

Let M=(q-1)/2.  Whenever M lies strictly inside the twin blackout of a primitive
row born at rank r, complete escape therefore forces M itself to be a twin
center.  Since 2M+1=q is already prime, this is equivalent to requiring q-2 to
be prime as well.

The most dangerous reflection boundary from the first-reentry analysis is

    q = 3r-1.

Here a nontrivial twin center r is divisible by three; primality of q also
forces r even, hence r is divisible by six and q=8 (mod 9).  Moreover

    M=(3r-2)/2,
    2M-1=q-2=3(r-1),

so M can never be a twin center for r>2.  Therefore a boundary row with
q=3r-1 cannot completely escape when q=5 or 7 (mod 8).  Any complete boundary
escape must satisfy

    q = 1 or 3 (mod 8),
    q = 8 (mod 9),

or equivalently

    q = 17 or 35 (mod 72).

This is a strict arithmetic narrowing, not a claim that either remaining class
actually contains an escaping primitive Franel row.
"""

from __future__ import annotations

from .p022_barlow_franel_lucas_rank import franel_midpoint_zero_criterion
from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_primitive_defect_criterion import is_primitive_franel_divisor
from .p022_barlow_twin_defect_difference import twin_blackout_target, twin_zero_local_visibility


def midpoint_index(prime: int) -> int:
    if isinstance(prime, bool) or not isinstance(prime, int) or prime <= 2 or not _is_prime(prime):
        raise ValueError("prime must be an odd prime")
    return (prime - 1) // 2


def midpoint_is_internal_to_twin_blackout(rank: int, prime: int) -> bool:
    target = twin_blackout_target(rank)
    middle = midpoint_index(prime)
    return rank + 2 <= middle <= target - 2


def midpoint_zero_forces_twin_visibility(rank: int, prime: int) -> tuple[int, bool]:
    """If the forced midpoint zero is internal, report whether it is hidden.

    A midpoint q-zero can belong to the complete escape kernel only when both
    adjacent defect edges are deleted, i.e. when the midpoint is a twin center.
    """
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at the declared twin rank")
    middle = midpoint_index(prime)
    if not midpoint_is_internal_to_twin_blackout(rank, prime):
        raise ValueError("Franel midpoint is not strictly inside the first blackout")
    if not franel_midpoint_zero_criterion(prime):
        return middle, False
    hidden = twin_zero_local_visibility(middle) == (False, False)
    return middle, hidden


def boundary_escape_residue_classes(rank: int, prime: int) -> tuple[int, int]:
    """Certify the necessary mod-8/mod-72 classes at q=3r-1.

    Returns ``(q mod 8, q mod 72)`` after excluding the midpoint-visible
    residue classes 5 and 7 modulo 8.
    """
    target = twin_blackout_target(rank)
    if prime != 3 * rank - 1:
        raise ValueError("this helper is for the reflection boundary q=3r-1")
    if not _is_prime(prime):
        raise ValueError("boundary q must be prime")
    if rank % 3 != 0:
        raise AssertionError("nontrivial twin centers are divisible by three")
    if rank % 2 != 0:
        raise AssertionError("q=3r-1 prime forces the twin center r to be even")
    if prime % 9 != 8:
        raise AssertionError("boundary prime must be 8 modulo 9")
    if target != 2 * rank - 1:
        raise AssertionError("unexpected twin target")

    residue8 = prime % 8
    if residue8 in (5, 7):
        middle = midpoint_index(prime)
        if not franel_midpoint_zero_criterion(prime):
            raise AssertionError("midpoint criterion changed")
        if 2 * middle - 1 != 3 * (rank - 1):
            raise AssertionError("boundary midpoint identity changed")
        if _is_prime(2 * middle - 1):
            raise AssertionError("boundary midpoint cannot be a twin center")
        raise ValueError("q=5 or 7 mod 8 is excluded by the visible midpoint zero")

    if residue8 not in (1, 3):
        raise AssertionError("odd prime has an unexpected mod-8 class")
    residue72 = prime % 72
    if residue72 not in (17, 35):
        raise AssertionError("CRT reduction to mod 72 failed")
    return residue8, residue72
