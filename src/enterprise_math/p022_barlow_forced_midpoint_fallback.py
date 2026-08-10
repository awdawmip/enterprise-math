"""Forced-midpoint fallback capture for the infinite q=5,23 (mod 24) family.

Let q be one of the target forced-midpoint primes, m=(q-1)/2, and suppose q
first divides the Franel sequence at a nontrivial twin-center rank r.  If

    r > (q+1)/6     (equivalently q < 6r-1),

then the midpoint defect gives a fallback capture, except for one explicit
q=23 (mod 24), m-prime support index which, if it vanishes, is itself captured
earlier inside the original twin blackout.

The central-binomial relation at m is much more localized than the generic
half-support bound suggests.

* q=5 (mod 24): every support index except m-1 is <=(q+1)/6.
* q=23 (mod 24), m composite: the same statement holds.
* q=23 (mod 24), m prime: put h=(m+1)/2=(q+1)/4.  Above (q+1)/6 the exact
  support is

      (h-1,+1), (h,-1), (m-1,+1).

  The h term can only strengthen the midpoint valuation.  The m-1 term is a
  q-unit by zero nonadjacency.  The sole cancellation candidate h-1 has odd
  boundary m-2, a nontrivial multiple of three.  If h-1 is a q-zero and lies
  after the primitive rank, the twin-blackout depth-difference theorem captures
  it positively at D_(h-1) before the midpoint is reached.

Thus every target-family primitive twin row with q<6r-1 is captured no later
than D_m.  This theorem is purely a fallback for an already-primitive row; it
does not assert that every target prime has twin primitive rank.
"""

from __future__ import annotations

from .p022_barlow_half_defect_obstructions import franel_recurrence_table_mod
from .p022_barlow_low_order_defect_reduction import (
    _is_prime,
    composite_A_relation_exponents,
)
from .p022_barlow_primitive_successor_capture import is_twin_prime_deferral_center


def _require_target_prime(prime: int) -> int:
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or prime <= 5
        or not _is_prime(prime)
        or prime % 24 not in (5, 23)
    ):
        raise ValueError("prime must exceed five and be 5 or 23 modulo 24")
    return (prime - 1) // 2


def forced_midpoint_small_support_bound(prime: int) -> int:
    """The uniform small-support threshold B=(q+1)/6."""
    _require_target_prime(prime)
    if (prime + 1) % 6:
        raise AssertionError("target prime must be 5 modulo 6")
    return (prime + 1) // 6


def forced_midpoint_signed_high_support(
    prime: int,
) -> tuple[int, tuple[tuple[int, int], ...]]:
    """Return (B, support above B) with exact signs.

    For q=23 mod24 and prime midpoint m, the only extra pair is h-1,+1 and
    h,-1.  In all cases the explicit recurrence predecessor m-1 has +1.
    """
    midpoint = _require_target_prime(prime)
    bound = forced_midpoint_small_support_bound(prime)
    relation = composite_A_relation_exponents(midpoint)
    high = tuple((index, exponent) for index, exponent in relation if index > bound)

    if prime % 24 == 23 and _is_prime(midpoint):
        half = (midpoint + 1) // 2
        expected = ((half - 1, 1), (half, -1), (midpoint - 1, 1))
    else:
        expected = ((midpoint - 1, 1),)
    if high != expected:
        raise AssertionError("forced-midpoint signed localization changed")
    return bound, high


def forced_midpoint_fallback_capture_location(rank: int, prime: int) -> int:
    """Return an earlier positive defect or the guaranteed midpoint fallback.

    Preconditions are checked by the recurrence modulo q: q first vanishes at
    the declared twin rank r, and q<6r-1.  The return value is the segment of a
    defect which must have positive q-valuation by the structural argument.
    """
    midpoint = _require_target_prime(prime)
    if (
        isinstance(rank, bool)
        or not isinstance(rank, int)
        or rank <= 3
        or not is_twin_prime_deferral_center(rank)
    ):
        raise ValueError("rank must be a nontrivial twin-prime center")
    bound, high = forced_midpoint_signed_high_support(prime)
    if rank <= bound or prime >= 6 * rank - 1:
        raise ValueError("fallback theorem requires r>(q+1)/6")

    table = franel_recurrence_table_mod(prime, prime, midpoint)
    first_zero = next((index for index in range(1, midpoint + 1) if table[index] == 0), None)
    if first_zero != rank:
        raise ValueError("declared rank must be the first Franel zero modulo q")
    if table[midpoint] != 0:
        raise AssertionError("target prime must have the forced midpoint zero")
    if table[midpoint - 1] == 0:
        raise AssertionError("Franel midpoint zero cannot have an adjacent zero")

    # Every small support index is below the primitive rank and hence a q-unit.
    relation = composite_A_relation_exponents(midpoint)
    if any(
        index <= bound and table[index] == 0
        for index, _ in relation
    ):
        raise AssertionError("primitive rank must make the localized small support q-unit")

    if prime % 24 != 23 or not _is_prime(midpoint):
        # Only m-1 remains above B, and it is a q-unit.  Hence the midpoint
        # numerator depth survives unchanged.
        return midpoint

    half = (midpoint + 1) // 2
    if high != ((half - 1, 1), (half, -1), (midpoint - 1, 1)):
        raise AssertionError("m-prime signed support changed")

    dangerous = half - 1
    if table[dangerous] == 0:
        # If dangerous<r, primitivity was already contradicted.  Equality is
        # impossible in the target congruence class; otherwise q<6r-1 puts the
        # index strictly inside the original twin blackout.
        if dangerous < rank:
            raise AssertionError("primitive rank forbids the dangerous high zero")
        if dangerous == rank:
            raise AssertionError("q=23 mod24 cannot satisfy (q-3)/4=r at a twin center")
        target = 2 * rank - 1
        if not rank + 2 <= dangerous < target:
            raise AssertionError("dangerous high zero must lie inside the twin blackout")
        odd_boundary = 2 * dangerous - 1
        if odd_boundary != midpoint - 2 or odd_boundary <= 3 or odd_boundary % 3:
            raise AssertionError("dangerous direct boundary must be composite by mod three")
        if _is_prime(odd_boundary):
            raise AssertionError("dangerous direct boundary cannot be prime")
        if table[dangerous - 1] == 0:
            raise AssertionError("adjacent Franel zeros are impossible")
        # Inside the twin blackout, v_q(D_s)=z_s-z_(s-1)>0.
        return dangerous

    # h has coefficient -1 and can only strengthen the marker if it vanishes;
    # m-1 and all positive small support are q-units.  Hence D_m is positive.
    return midpoint
