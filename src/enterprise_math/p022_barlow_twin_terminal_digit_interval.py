"""Arithmetic interval for the source-high secondary quadratic digit branch.

Let r be a nontrivial primitive twin rank and suppose the deep secondary
quadratic transport

    Q=2(2r-3)^2=8r^2-24r+18

has entered its two-zero-digit branch.  Write Q=a*q+b with q the valuation
prime and impose the reflection-symmetric primitive band

    r <= b <= q-1-r.

For a fixed high digit a this is equivalent to the elementary interval

    ceil((Q+r+1)/(a+1)) <= q <= floor((Q-r)/a).

The most constrained quotient-zero branch is a=r, where the high digit is the
original primitive source.  For r>=49 the interval becomes

    8r-30 <= q <= 8r-25.

Every nontrivial twin center has 3|r.  Hence, among these six consecutive
integers, primality leaves only

    q=8r-29  or  q=8r-25.

Their low digits are respectively

    b=5r+18  or  b=r+18.

For the forced-midpoint prime family q=5 or 23 (mod 24), the first line is
impossible because 8r-29=19 (mod 24), while the second lies in the required
23 (mod 24) sector.  Therefore the forced source-high branch collapses to

    q=8r-25,  b=r+18.

If complete defect escape continues and r>=19, the new low zero r+18 lies in
the original twin blackout.  It must therefore be another nontrivial twin
center, forcing 2r+35 and 2r+37 to be prime.  This is the upstream arithmetic
source of the fixed eighteen-step transfer obstruction.

All statements in this file are elementary consequences of the already proved
P022 transport/digit-band hypotheses; no new Franel congruence is assumed.
"""

from __future__ import annotations

from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_primitive_successor_capture import is_twin_prime_deferral_center
from .p022_barlow_twin_terminal_quadratic_transport import terminal_secondary_index


def secondary_digit_prime_interval(rank: int, high: int) -> tuple[int, int]:
    """Return the exact integer q interval imposed by r<=b<=q-1-r."""
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 1:
        raise ValueError("rank must be positive")
    if isinstance(high, bool) or not isinstance(high, int) or high < 1:
        raise ValueError("high digit must be positive")
    qindex = terminal_secondary_index(rank)
    lower_num = qindex + rank + 1
    upper_num = qindex - rank
    lower = (lower_num + high) // (high + 1)
    upper = upper_num // high
    return lower, upper


def source_high_interval(rank: int) -> tuple[int, int]:
    """For high digit a=r>=49 return [8r-30,8r-25]."""
    if rank < 49:
        raise ValueError("source-high six-integer collapse uses r>=49")
    lower, upper = secondary_digit_prime_interval(rank, rank)
    expected = (8 * rank - 30, 8 * rank - 25)
    if (lower, upper) != expected:
        raise AssertionError("source-high secondary interval changed")
    return expected


def source_high_prime_lines(rank: int) -> tuple[int, int]:
    """For a nontrivial twin r return the two possible prime affine lines."""
    if rank < 49 or not is_twin_prime_deferral_center(rank):
        raise ValueError("rank must be a nontrivial twin center at least 49")
    if rank % 3:
        raise AssertionError("nontrivial twin centers must be divisible by three")
    lower, upper = source_high_interval(rank)
    candidates = tuple(
        value
        for value in range(lower, upper + 1)
        if value > 3 and value % 2 and value % 3
    )
    expected = (8 * rank - 29, 8 * rank - 25)
    if candidates != expected:
        raise AssertionError("prime-residue filtering of the source-high interval changed")
    return expected


def source_high_low_digits(rank: int) -> tuple[tuple[int, int], tuple[int, int]]:
    """Return ((q1,b1),(q2,b2)) for the two affine source-high candidates."""
    qindex = terminal_secondary_index(rank)
    q1, q2 = source_high_prime_lines(rank)
    b1 = qindex - rank * q1
    b2 = qindex - rank * q2
    expected = ((q1, 5 * rank + 18), (q2, rank + 18))
    if ((q1, b1), (q2, b2)) != expected:
        raise AssertionError("source-high low-digit formulas changed")
    return expected


def forced_source_high_affine_line(rank: int) -> tuple[int, int]:
    """In q=5,23 mod24 target family return the sole (q,b) source-high line."""
    first, second = source_high_low_digits(rank)
    if first[0] % 24 != 19 or second[0] % 24 != 23:
        raise AssertionError("source-high affine residue classes changed")
    return second


def forced_source_high_hidden_twin_constellation(rank: int) -> tuple[int, ...]:
    """Prime forms forced if the surviving low digit r+18 also stays hidden."""
    if rank < 49 or not is_twin_prime_deferral_center(rank):
        raise ValueError("rank must be a twin center at least 49")
    prime, low = forced_source_high_affine_line(rank)
    if low != rank + 18 or prime != 8 * rank - 25:
        raise AssertionError("forced source-high affine line changed")
    forms = (
        2 * rank - 1,
        2 * rank + 1,
        2 * rank + 35,
        2 * rank + 37,
        8 * rank - 25,
    )
    # The first pair is guaranteed by the input twin center.  The second pair
    # and q itself are theorem-side necessities of continued complete escape;
    # this helper exposes the exact constellation without asserting existence.
    if not _is_prime(forms[0]) or not _is_prime(forms[1]):
        raise AssertionError("input twin-center primes changed")
    return forms
