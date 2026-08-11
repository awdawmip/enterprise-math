"""General fixed-transfer reduction for the simple high-digit terminal branch.

After complete primitive-twin escape has crossed the seven-rank barrier, the
secondary quadratic index

    Q = 2(2r-3)^2 = 8r^2-24r+18

may enter the quotient-zero branch.  Suppose the high base-q digit is another
hidden simple zero

    a = r+h,

with r and a nontrivial twin centers.  Hence 3 divides r and h.  Write

    Q = a*q+b,
    q = 8(r-h)-1-c.

The reflection-symmetric primitive band r<=b<=q-1-r is equivalent to

    ceil((24r-8h^2-h-18)/(r+h)) <= c
      <= floor((30r-8h^2-9h-20)/(r+h+1)).

The real width of this interval is strictly less than six.  Since r-h is a
multiple of three, the forced-midpoint classes q=5 or 23 (mod 24) require

    c=18 (mod 24)   or   c=0 (mod 24),

respectively.  Those two residue lattices are separated by at least six, so for
fixed (r,h) there is at most one forced q candidate.

More importantly, the moving source parameter disappears modulo q.  Put

    rho   = h + (c+1)/8,
    delta = 8h+c = 8rho-1,
    x     = 2(rho-1)^2 = (delta-7)^2/32.

Then r=rho (mod q).  If both r and r+h are Franel q-zeros, the normalized
Franel recurrence forces

    q | num H_h(rho),

where H_0=0,H_1=1 is the standard forward zero-transfer solution.

Complete escape also forces the universal quadratic transported zeros

    K_- = 2(r-1)^2,
    K_+ = 2(r+1)^2-1.

Modulo q their low digits start at x and differ by delta.  Under q>7r+3,
0<delta<r.  If both remainders lie in the primitive symmetric band, their
actual difference is therefore delta (not delta-q).  A second normalized
transfer then forces

    q | num H_delta(x).

Thus every simple high-digit branch is reduced to two fixed integers depending
only on (h,c), not on r.  If those numerators have no common prime in the
required q residue class, that entire affine branch is impossible.  The source-
high coprime C18/C24 closure is the h=0 predecessor of this more general
mechanism, although h=0 is intentionally outside the API below.

The Franel recurrence and p-Lucas/reflection inputs are prior art.  The c-window,
parameter elimination, and paired fixed-transfer reduction are P022-local.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd

from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_twin_source_high_18step import forward_zero_transfer


def _ceil_div(numerator: int, denominator: int) -> int:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    return -((-numerator) // denominator)


def _require_gap(rank: int, gap: int) -> None:
    if isinstance(rank, bool) or not isinstance(rank, int) or rank <= 0:
        raise ValueError("rank must be positive")
    if isinstance(gap, bool) or not isinstance(gap, int) or gap <= 0:
        raise ValueError("gap must be positive")
    if rank % 3 or gap % 3:
        raise ValueError("hidden twin source/high gap requires 3|rank and 3|gap")
    if gap >= rank:
        raise ValueError("high digit r+h must stay below 2r")


def general_high_c_interval(rank: int, gap: int) -> tuple[int, int]:
    """Exact integer c-window equivalent to r<=b<=q-1-r."""
    _require_gap(rank, gap)
    lower_num = 24 * rank - 8 * gap * gap - gap - 18
    lower_den = rank + gap
    upper_num = 30 * rank - 8 * gap * gap - 9 * gap - 20
    upper_den = rank + gap + 1
    lower = _ceil_div(lower_num, lower_den)
    upper = upper_num // upper_den

    # The real interval width is
    #   (6r^2-2hr-26r-h+18)/((r+h)(r+h+1)) < 6,
    # since subtracting its numerator from six times the denominator gives
    #   6h^2+14hr+7h+32r-18 > 0.
    width_numerator = 6 * rank * rank - 2 * gap * rank - 26 * rank - gap + 18
    width_denominator = (rank + gap) * (rank + gap + 1)
    if 6 * width_denominator <= width_numerator:
        raise AssertionError("general high c-window must have real width below six")
    return lower, upper


def forced_midpoint_c_candidates(rank: int, gap: int) -> tuple[int, ...]:
    """Forced q=5,23 mod24 leaves at most one c in the sub-six window."""
    lower, upper = general_high_c_interval(rank, gap)
    candidates = tuple(
        value
        for value in range(lower, upper + 1)
        if value % 24 in (0, 18)
    )
    if len(candidates) > 1:
        raise AssertionError("a sub-six interval cannot hit two forced c residue lattices")
    return candidates


def general_high_affine_data(rank: int, gap: int, c: int) -> tuple[int, int, int, int]:
    """Return (a,q,b,delta) and certify the affine/band arithmetic."""
    _require_gap(rank, gap)
    lower, upper = general_high_c_interval(rank, gap)
    if not lower <= c <= upper:
        raise ValueError("c lies outside the symmetric-band interval")
    if c % 24 not in (0, 18):
        raise ValueError("c must correspond to forced q=23 or 5 modulo 24")

    high = rank + gap
    prime = 8 * (rank - gap) - 1 - c
    secondary = 8 * rank * rank - 24 * rank + 18
    low = secondary - high * prime
    delta = 8 * gap + c
    if prime % 24 not in (5, 23):
        raise AssertionError("forced c residue must give the target q residue class")
    if not rank <= low <= prime - 1 - rank:
        raise AssertionError("c-window must be exactly the symmetric primitive band")
    if secondary != high * prime + low:
        raise AssertionError("secondary affine digit decomposition changed")
    return high, prime, low, delta


def fixed_general_high_parameters(gap: int, c: int) -> tuple[Fraction, int, Fraction]:
    """Return (rho,delta,x) after eliminating the moving rank modulo q."""
    if isinstance(gap, bool) or not isinstance(gap, int) or gap <= 0 or gap % 3:
        raise ValueError("gap must be a positive multiple of three")
    if c % 24 not in (0, 18):
        raise ValueError("c must lie in a forced residue class")
    rho = Fraction(8 * gap + c + 1, 8)
    delta = 8 * gap + c
    if delta <= 0:
        raise ValueError("transport gap delta must be positive")
    x = Fraction((delta - 7) ** 2, 32)
    if delta != 8 * rho - 1 or x != 2 * (rho - 1) ** 2:
        raise AssertionError("fixed parameter identities changed")
    return rho, delta, x


def fixed_general_high_transfers(gap: int, c: int) -> tuple[Fraction, Fraction]:
    """Return the two rational transfer values H_h(rho), H_delta(x)."""
    rho, delta, x = fixed_general_high_parameters(gap, c)
    return forward_zero_transfer(rho, gap), forward_zero_transfer(x, delta)


def fixed_general_high_numerator_gcd(gap: int, c: int) -> int:
    """Exact gcd of the two fixed transfer numerators for one (h,c) branch."""
    first, second = fixed_general_high_transfers(gap, c)
    return gcd(abs(first.numerator), abs(second.numerator))


def quadratic_remainder_gap(rank: int, gap: int, c: int) -> tuple[int, int, int]:
    """Return (b_-,b_+,delta) and certify the actual quadratic remainder gap.

    This is the arithmetic part of the complete-escape implication.  The caller
    supplies a c whose secondary low digit lies in the symmetric band and must
    additionally be beyond the seven-rank horizon.
    """
    _, prime, _, delta = general_high_affine_data(rank, gap, c)
    if not _is_prime(prime):
        raise ValueError("affine q candidate must be prime")
    if prime <= 7 * rank + 3:
        raise ValueError("seven-rank complete-escape barrier must be crossed")
    if not 0 < delta < rank:
        raise AssertionError("seven-rank barrier must force 0<delta<r")

    left = 2 * (rank - 1) ** 2
    right = 2 * (rank + 1) ** 2 - 1
    low_left = left % prime
    low_right = right % prime
    for low in (low_left, low_right):
        if not rank <= low <= prime - 1 - rank:
            raise ValueError("quadratic transported remainder is outside the primitive band")

    if (low_right - low_left) % prime != delta % prime:
        raise AssertionError("quadratic remainder congruence gap changed")
    band_width = prime - 1 - 2 * rank
    if prime - delta <= band_width:
        raise AssertionError("negative wrapped gap must exceed the whole primitive band")
    if low_right - low_left != delta:
        raise AssertionError("two in-band quadratic remainders must differ by +delta")
    return low_left, low_right, delta


def fixed_transfer_residue_class_is_compatible(gap: int, c: int, prime: int) -> bool:
    """Whether a common transfer prime lies in the q residue class required by c."""
    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    if c % 24 not in (0, 18):
        raise ValueError("c must lie in a forced residue class")
    required = (-1 - c) % 24
    return prime % 24 == required
