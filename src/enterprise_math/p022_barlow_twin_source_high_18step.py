"""Fixed eighteen-step obstruction on the forced source-high affine branch.

A late P022 secondary-quadratic branch can collapse, for the forced-midpoint
prime family, to

    q = 8r-25,

with r the primitive twin rank and r+18 another hidden Franel zero.  This file
records a finite reduction of that branch.

Assume q divides F_r and F_(r+18).  Since r is a first zero digit, F_(r+1) is
a q-unit.  Normalize the forward Franel recurrence by

    H_0=0, H_1=1,

    (r+j)^2 H_j
      = (7(r+j-1)^2+7(r+j-1)+2) H_(j-1)
        +8(r+j-1)^2 H_(j-2).

Then F_(r+j)=F_(r+1) H_j modulo q.  The affine identity q=8r-25 gives

    r = 25/8  (mod q).

For r>=49 all recurrence denominators through j=18 are q-units, so a second
zero at r+18 forces

    H_18(25/8)=0  (mod q).

The exact rational value is

    H_18(25/8)
      = C18 / D18,

where

    C18 = 29829053990598777866100618466285344298546940755664483184651210283,
    D18 = 71605938162735013309331494053780007352411567386725.

Every prime factor of D18 is at most 137, hence any affine branch with r>=49
has q>=367 and sees D18 as a unit.  Therefore the infinite-looking affine line
is reduced to the finite factor set of the single 65-digit integer C18.

A cheap partial factorization is

    C18 = 71 * 5329603 * C56,

    C56 = 78829046177426158013943285378194909173299708148238928191.

The first factor corresponds to the formal affine value r=12 and is outside the
nontrivial source-high theorem range; 5329603 is 19 modulo 24 and hence outside
the forced q=23 modulo 24 branch.  C56 remains composite but is intentionally
not asserted factored here.  Thus the remaining arithmetic task is finite:
factor C56 (or otherwise exclude its prime divisors satisfying the twin-source
conditions), not prove a new infinite congruence theorem.

The Franel recurrence is classical.  The affine specialization and fixed
18-step elimination are P022-local.
"""

from __future__ import annotations

from fractions import Fraction

from .p022_barlow_low_order_defect_reduction import _is_prime

SOURCE_HIGH_18_NUMERATOR = (
    29_829_053_990_598_777_866_100_618_466_285_344_298_546_940_755_664_483_184_651_210_283
)
SOURCE_HIGH_18_DENOMINATOR = (
    71_605_938_162_735_013_309_331_494_053_780_007_352_411_567_386_725
)
SOURCE_HIGH_18_COFACTOR = (
    78_829_046_177_426_158_013_943_285_378_194_909_173_299_708_148_238_928_191
)


def forward_zero_transfer(parameter: Fraction, steps: int) -> Fraction:
    """Return H_steps for the zero/unit normalized Franel recurrence."""
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 0:
        raise ValueError("steps must be a non-negative integer")
    if steps == 0:
        return Fraction(0, 1)
    if steps == 1:
        return Fraction(1, 1)
    previous = Fraction(0, 1)
    current = Fraction(1, 1)
    for j in range(2, steps + 1):
        n = parameter + j - 1
        denominator = (parameter + j) ** 2
        if denominator == 0:
            raise ValueError("recurrence denominator vanished")
        previous, current = (
            current,
            ((7 * n * n + 7 * n + 2) * current + 8 * n * n * previous)
            / denominator,
        )
    return current


def fixed_source_high_transfer() -> Fraction:
    """Return H_18(25/8) exactly and certify the frozen constants."""
    value = forward_zero_transfer(Fraction(25, 8), 18)
    if value.numerator != SOURCE_HIGH_18_NUMERATOR:
        raise AssertionError("fixed 18-step numerator changed")
    if value.denominator != SOURCE_HIGH_18_DENOMINATOR:
        raise AssertionError("fixed 18-step denominator changed")
    return value


def fixed_source_high_partial_factorization() -> tuple[int, int, int]:
    """Certify the cheap partial factorization C18=71*5329603*C56."""
    factors = (71, 5_329_603, SOURCE_HIGH_18_COFACTOR)
    if factors[0] * factors[1] * factors[2] != SOURCE_HIGH_18_NUMERATOR:
        raise AssertionError("fixed 18-step partial factorization changed")
    return factors


def affine_source_high_prime(rank: int) -> int:
    """Return q=8r-25 and require the declared affine value to be prime."""
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 1:
        raise ValueError("rank must be a positive integer")
    prime = 8 * rank - 25
    if not _is_prime(prime):
        raise ValueError("8r-25 must be prime")
    return prime


def source_high_denominator_is_unit(rank: int) -> bool:
    """For r>=49 certify q=8r-25 exceeds every fixed denominator prime factor."""
    if rank < 49:
        raise ValueError("source-high interval reduction uses rank at least 49")
    prime = affine_source_high_prime(rank)
    if prime <= 137:
        raise AssertionError("late source-high prime must exceed the fixed denominator factors")
    if SOURCE_HIGH_18_DENOMINATOR % prime == 0:
        raise AssertionError("affine prime unexpectedly divides the fixed transfer denominator")
    return True


def source_high_double_zero_forces_fixed_divisor(rank: int) -> int:
    """Algebraic consequence of q=8r-25 and zeros at r,r+18.

    This helper certifies the denominator/unit part of the implication and
    returns C18, the fixed integer which any such q must divide.  The Franel
    zero assumptions are theorem-side hypotheses and are not recomputed here.
    """
    prime = affine_source_high_prime(rank)
    source_high_denominator_is_unit(rank)
    if (8 * rank - 25) != prime:
        raise AssertionError("affine source-high relation changed")
    if (8 * Fraction(25, 8) - 25) != 0:
        raise AssertionError("fixed affine specialization changed")
    fixed_source_high_transfer()
    return SOURCE_HIGH_18_NUMERATOR
