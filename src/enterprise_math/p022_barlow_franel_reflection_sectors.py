"""Reflection sectors and universal midpoint companions for Franel recurrence.

The Franel recurrence is

    (n+1)^2 y_(n+1) = (7n(n+1)+2)y_n + 8n^2 y_(n-1).

For an odd prime p and 0<=n<p, define the reflected solution

    (R_p y)_n = (-8)^n y_(p-1-n).

A direct substitution in the recurrence shows that R_p is an involution on
the two-dimensional mod-p solution space.  In initial coordinates (y_0,y_1)
it acts by

    (y_0,y_1) -> (y_0, 4y_0-y_1).

Thus the Franel solution F_0=1,F_1=2 is the +1 sector, while the standard
second solution G_0=0,G_1=1 is the -1 sector:

    F_n =  (+1)(-8)^n F_(p-1-n),
    G_n =  (-1)(-8)^n G_(p-1-n)             (mod p).

The existence of the Franel recurrence, its standard second solution, and its
Casoratian are prior art.  The P022 contribution here is the reflection-sector
packaging and its use to remove the moving prime from the special-third-index
zero problem.

Let p=6d+5 be prime, m=(p-1)/2 and r=(p+1)/3=m-d.  The universal midpoint
recurrence

    U_(j+1)=-(28j^2+1)U_j + 8(2j-1)^4 U_(j-1)

has two convenient integer sectors:

    A_0=0, A_1=1,
    E_0=2, E_1=-1.

A is the existing zero-at-midpoint companion.  E is the complementary
nonzero-at-midpoint companion.  Exactly:

* p=5 or 7 (mod 8):  p|F_r iff p|A_d;
* p=1 or 3 (mod 8):  p|F_r iff p|E_d.

For the second line, midpoint reflection gives F_(m-1)/F_m=-1/16.  Applying
the same universal offset recurrence and clearing denominators gives E.
Therefore the dangerous P022 boundary q=3r-1 in its surviving mod-8 classes
is reduced to the fixed diagonal divisibility question

    q=6d+5,  q | E_d.

The two universal sectors cannot vanish together at such a diagonal prime,
because their integer Casoratian is

    A_d E_(d+1)-A_(d+1)E_d
      = -2(-8)^d ((2d-1)!!)^4,

which is a p-unit when p=6d+5.
"""

from __future__ import annotations

from functools import lru_cache

from .p022_barlow_franel_half_index import half_index
from .p022_barlow_franel_integer_companion import (
    midpoint_integer_companion,
    odd_double_factorial,
)
from .p022_barlow_franel_lucas_rank import franel_midpoint_zero_criterion
from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_low_order_identifiability import triple_moment_factor


def _require_odd_prime(prime: int) -> None:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 2
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be an odd prime")


def _franel_residue(index: int, prime: int) -> int:
    if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < prime:
        raise ValueError("index must lie in 0..p-1")
    return 1 if index == 0 else triple_moment_factor(index) % prime


def franel_second_solution_residue(index: int, prime: int) -> int:
    """Return G_index mod p for the standard second solution G_0=0,G_1=1."""
    _require_odd_prime(prime)
    if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < prime:
        raise ValueError("index must lie in 0..p-1")
    if index == 0:
        return 0
    previous, current = 0, 1
    for n in range(1, index):
        numerator = (
            (7 * n * (n + 1) + 2) * current + 8 * n * n * previous
        ) % prime
        denominator = (n + 1) * (n + 1) % prime
        following = numerator * pow(denominator, -1, prime) % prime
        previous, current = current, following
    return current


def franel_reflection_sectors_hold(index: int, prime: int) -> bool:
    """Certify the + Franel and - second-solution reflection sectors."""
    _require_odd_prime(prime)
    if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < prime:
        raise ValueError("index must lie in 0..p-1")
    reflected = prime - 1 - index
    multiplier = pow(-8, index, prime)

    franel_left = _franel_residue(index, prime)
    franel_right = multiplier * _franel_residue(reflected, prime) % prime
    if franel_left != franel_right:
        raise AssertionError("Franel + reflection sector failed")

    second_left = franel_second_solution_residue(index, prime)
    second_right = -multiplier * franel_second_solution_residue(reflected, prime) % prime
    if second_left != second_right:
        raise AssertionError("Franel second solution must lie in the - reflection sector")
    return True


def second_solution_midpoint_zero_criterion(prime: int) -> bool:
    """G_((p-1)/2)=0 exactly for p=1 or 3 mod 8, for p>3.

    The - reflection sector forces G_m=0 when (-8/p)=+1.  In the other two
    residue classes F_m=0 by the prior-art Franel midpoint criterion, and the
    nonzero Casoratian of the two standard solutions forbids G_m from also
    vanishing.
    """
    _require_odd_prime(prime)
    if prime == 3:
        raise ValueError("the complementary midpoint criterion is stated for p>3")
    middle = half_index(prime)
    franel_zero = franel_midpoint_zero_criterion(prime)
    actual = franel_second_solution_residue(middle, prime) == 0
    predicted = prime % 8 in (1, 3)
    if actual != predicted:
        raise AssertionError("second-solution midpoint reflection criterion failed")
    if actual == franel_zero:
        raise AssertionError("the two reflection sectors cannot vanish together at midpoint")
    return actual


@lru_cache(maxsize=None)
def midpoint_even_companion(offset: int) -> int:
    """Integer complementary midpoint sector E_0=2,E_1=-1."""
    if isinstance(offset, bool) or not isinstance(offset, int) or offset < 0:
        raise ValueError("offset must be a non-negative integer")
    if offset == 0:
        return 2
    if offset == 1:
        return -1
    d = offset - 1
    return (
        -(28 * d * d + 1) * midpoint_even_companion(d)
        + 8 * (2 * d - 1) ** 4 * midpoint_even_companion(d - 1)
    )


def midpoint_sector_casoratian(offset: int) -> int:
    """Exact integer Casoratian of A=(0,1) and E=(2,-1)."""
    if isinstance(offset, bool) or not isinstance(offset, int) or offset < 0:
        raise ValueError("offset must be a non-negative integer")
    left = (
        midpoint_integer_companion(offset) * midpoint_even_companion(offset + 1)
        - midpoint_integer_companion(offset + 1) * midpoint_even_companion(offset)
    )
    expected = -2 * (-8) ** offset * odd_double_factorial(offset) ** 4
    if left != expected:
        raise AssertionError("midpoint-sector Casoratian changed")
    return left


def third_index_parameters(prime: int) -> tuple[int, int, int]:
    """For p=5 mod 6 return (r,m,d) with r=(p+1)/3=m-d."""
    _require_odd_prime(prime)
    if prime % 6 != 5:
        raise ValueError("prime must be 5 modulo 6")
    rank = (prime + 1) // 3
    middle = half_index(prime)
    offset = (prime - 5) // 6
    if middle - offset != rank:
        raise AssertionError("third-index midpoint offset identity failed")
    return rank, middle, offset


def third_index_franel_zero_via_companion(
    prime: int,
) -> tuple[int, int, str, bool]:
    """Reduce p|F_((p+1)/3) to one fixed midpoint companion.

    Returns ``(rank, offset, sector, is_zero)``.  ``sector`` is ``A`` in the
    forced Franel-midpoint classes 5,7 mod 8 and ``E`` in the complementary
    classes 1,3 mod 8.
    """
    rank, _, offset = third_index_parameters(prime)
    actual = _franel_residue(rank, prime) == 0
    if prime % 8 in (5, 7):
        sector = "A"
        predicted = midpoint_integer_companion(offset) % prime == 0
    else:
        sector = "E"
        if prime == 3:
            raise AssertionError("p=5 mod 6 excludes the p=3 exceptional case")
        second_solution_midpoint_zero_criterion(prime)
        predicted = midpoint_even_companion(offset) % prime == 0
    if actual != predicted:
        raise AssertionError("universal midpoint companion disagrees with the Franel special value")
    return rank, offset, sector, actual


def diagonal_companion_mutual_exclusion(prime: int) -> bool:
    """At p=6d+5, p cannot divide both A_d and E_d."""
    _, _, offset = third_index_parameters(prime)
    casoratian = midpoint_sector_casoratian(offset)
    if casoratian % prime == 0:
        raise AssertionError("p=6d+5 must be a unit on the companion Casoratian")
    if (
        midpoint_integer_companion(offset) % prime == 0
        and midpoint_even_companion(offset) % prime == 0
    ):
        raise AssertionError("independent midpoint sectors cannot vanish together")
    return True
