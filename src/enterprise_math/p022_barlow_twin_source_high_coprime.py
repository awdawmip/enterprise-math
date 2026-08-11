"""Close the forced source-high secondary branch by two coprime transfers.

This module combines three already established P022 ingredients.

1. In the simple forced-midpoint source-high branch, the secondary digit
   interval collapses to

       q=8r-25,

   and the secondary low digit is r+18.  Continued complete escape therefore
   forces q|F_r and q|F_(r+18).

2. The universal quadratic re-entry pair forces q-zero transported indices

       K_-=2(r-1)^2,
       K_+=2(r+1)^2-1.

   Because q=8r-25, modulo q one has

       32 K_- = 289,
       32 K_+ = 1057.

   Their single-digit zero remainders lie in the symmetric primitive band.  The
   band width is less than q-24 for r>=49, so the congruence

       K_+-K_-=8r-1 = 24 (mod q)

   lifts to an actual remainder gap of exactly 24.  If b is the K_- remainder,
   then q|F_b and q|F_(b+24), with

       b = 289/32 (mod q).

3. A zero/unit-normalized Franel recurrence over a fixed gap can eliminate the
   moving starting index.  The two zero pairs above yield

       q | C18,   C18=num H_18(25/8),
       q | C24,   C24=num H_24(289/32).

   Exact computation gives

       C18 =
       29829053990598777866100618466285344298546940755664483184651210283,

       C24 =
       7979433434235605675134518175700710746694525034931862068953026110057891172450177132200752379889173037705504458903956027406587,

   and

       gcd(C18,C24)=1.

The recurrence denominators are q-units on the actual branch: r+j and b+j
stay strictly between 0 and q for the required fixed gaps.  Therefore no q can
satisfy both fixed transfer obstructions.  The forced simple source-high branch
is impossible.

This is a P022 transport-rigidity theorem.  It avoids factoring either fixed
integer; only their exact Euclidean gcd matters.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd

from .p022_barlow_twin_source_high_18step import (
    SOURCE_HIGH_18_NUMERATOR,
    forward_zero_transfer,
)

SOURCE_HIGH_24_NUMERATOR = (
    7_979_433_434_235_605_675_134_518_175_700_710_746_694_525_034_931_862_068_953_026_110_057_891_172_450_177_132_200_752_379_889_173_037_705_504_458_903_956_027_406_587
)
SOURCE_HIGH_24_DENOMINATOR = (
    48_940_480_372_669_530_986_700_859_696_055_406_101_181_060_118_092_032_219_400_945_118_680_835_583_240_687_787_873_648_167_747_363_242_125
)


def fixed_quadratic_remainder_transfer() -> Fraction:
    """Return H_24(289/32) exactly."""
    value = forward_zero_transfer(Fraction(289, 32), 24)
    if value.numerator != SOURCE_HIGH_24_NUMERATOR:
        raise AssertionError("fixed 24-step numerator changed")
    if value.denominator != SOURCE_HIGH_24_DENOMINATOR:
        raise AssertionError("fixed 24-step denominator changed")
    return value


def source_high_fixed_transfer_gcd() -> int:
    """Exact Euclidean obstruction: gcd(C18,C24)=1."""
    fixed_quadratic_remainder_transfer()
    value = gcd(SOURCE_HIGH_18_NUMERATOR, SOURCE_HIGH_24_NUMERATOR)
    if value != 1:
        raise AssertionError("source-high fixed transfer numerators ceased to be coprime")
    return value


def quadratic_remainder_gap_is_twenty_four(rank: int, prime: int) -> bool:
    """Certify the modular arithmetic behind the two fixed quadratic remainders.

    Assumes q=8r-25 and r>=49.  If b_-,b_+ are any two representatives in the
    symmetric primitive band [r,q-1-r] congruent to K_-,K_+ respectively, their
    difference is forced to be +24 rather than 24-q.
    """
    if rank < 49:
        raise ValueError("rank must be at least 49")
    if prime != 8 * rank - 25:
        raise ValueError("prime must lie on the surviving source-high affine line")
    if prime <= 2 * rank + 24:
        raise AssertionError("primitive band must be narrower than q-24")
    left = 2 * (rank - 1) ** 2
    right = 2 * (rank + 1) ** 2 - 1
    if (32 * left - 289) % prime:
        raise AssertionError("left quadratic residue specialization changed")
    if (32 * right - 1057) % prime:
        raise AssertionError("right quadratic residue specialization changed")
    if (right - left - 24) % prime:
        raise AssertionError("quadratic transported residues must differ by 24 modulo q")
    return True


def source_high_branch_coprime_obstruction(rank: int, prime: int) -> int:
    """Return the impossible common divisor required by complete source-high escape.

    The theorem-side zero assumptions imply q divides both fixed numerators.
    This helper certifies all parameter eliminations and returns their gcd,
    which is exactly one.
    """
    if prime != 8 * rank - 25:
        raise ValueError("prime must lie on q=8r-25")
    quadratic_remainder_gap_is_twenty_four(rank, prime)
    # 8r=q+25 and 32b=289 modulo q are the two fixed substitutions.
    if (8 * rank - 25) % prime:
        raise AssertionError("18-step affine substitution changed")
    if source_high_fixed_transfer_gcd() != 1:
        raise AssertionError("fixed transfer obstruction must be coprime")
    return 1
