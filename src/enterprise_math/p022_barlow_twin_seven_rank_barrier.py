"""Reflection amplification of the fivefold twin-source re-entry.

Let q be primitive at a nontrivial twin center r>=9.  Earlier P022 work gives
exact defect rows through the first terminal re-entry and then the threefold and
fivefold source-prime gates.  The fivefold gate is

    N = 5r+3,   2N-1 = 5(2r+1),

with high support -e_r+e_(r+1)+e_(N-1).

Assume *complete* escape through the first twin blackout, not merely terminal
cancellation.  If the threefold or fivefold gate is nonzero, the row is already
captured.  Otherwise the fivefold theorem gives q>6r+3 and q|F_(5r+2), with
5r+2<q.  Jarvis--Verrill reflection therefore gives another q-zero at

    s = q-5r-3.

If s lies in r+2,...,2r-2, complete blackout escape forces s itself to be a
nontrivial twin center.  Hence 3|s.  But r is divisible by three, so

    s == q (mod 3),

which is impossible for a prime q>3.  The endpoint s=2r-1 is also impossible,
because terminal cancellation has z_(2r-1)=0.  The adjacent value s=r+1 is
excluded by prime parity/nonadjacency.  Thus s>=2r, whence q>=7r+3; equality is
a nontrivial multiple of three.  Therefore

    complete primitive twin escape => q > 7r+3.

This theorem is a reflection amplification of the existing fivefold re-entry;
it uses no new Franel congruence beyond the prior-art mirror and nonadjacency
facts.
"""

from __future__ import annotations

from .p022_barlow_franel_lucas_rank import franel_zero_digits
from .p022_barlow_low_order_identifiability import (
    p_adic_valuation,
    triple_moment_factor,
)
from .p022_barlow_twin_defect_difference import (
    primitive_twin_first_defect_incidence,
    primitive_twin_terminal_cancellation_signature,
    twin_blackout_target,
    twin_zero_local_visibility,
)
from .p022_barlow_twin_source_reentry_barrier import (
    fivefold_reentry_or_barrier,
    right_fivefold_segment,
    threefold_reentry_or_barrier,
)


def fivefold_reflected_zero_index(rank: int, prime: int) -> int:
    """Reflection of the transported fivefold zero 5r+2."""
    return prime - right_fivefold_segment(rank)


def complete_escape_or_seven_rank_barrier(
    rank: int,
    prime: int,
) -> tuple[str, int, int]:
    """Return an earlier capture or certify q>7r+3.

    A ``("capture",n,v)`` result is the first/threefold/fivefold nonzero defect
    encountered.  The only ``barrier`` result is

        ("barrier", 7r+4, q),

    meaning that prime arithmetic forces q>7r+3.
    """
    earlier = primitive_twin_first_defect_incidence(rank, prime)
    if earlier is not None:
        return "capture", earlier[0], earlier[1]
    if primitive_twin_terminal_cancellation_signature(rank, prime) is None:
        raise AssertionError("complete first-blackout escape must cancel the terminal row")

    threefold = threefold_reentry_or_barrier(rank, prime)
    if threefold[0] == "capture":
        return threefold
    fivefold = fivefold_reentry_or_barrier(rank, prime)
    if fivefold[0] == "capture":
        return fivefold

    transported = right_fivefold_segment(rank) - 1
    if transported >= prime:
        raise AssertionError("six-rank barrier must put the fivefold zero below q")
    zeros = set(franel_zero_digits(prime))
    if transported not in zeros:
        raise AssertionError("vanishing fivefold gate must create the transported zero")
    reflected = fivefold_reflected_zero_index(rank, prime)
    if reflected not in zeros:
        raise AssertionError("Jarvis--Verrill reflection must preserve the zero alphabet")

    target = twin_blackout_target(rank)
    if reflected == rank:
        raise AssertionError("q=6r+3 is composite and cannot be the valuation prime")
    if reflected == rank + 1:
        raise AssertionError("a primitive zero cannot have an adjacent reflected zero")
    if rank + 2 <= reflected < target:
        if twin_zero_local_visibility(reflected) != (False, False):
            raise AssertionError("a reflected blackout zero would have an earlier defect incidence")
        if reflected % 3:
            raise AssertionError("nontrivial twin centers are divisible by three")
        if prime % 3 == 0:
            raise AssertionError("valuation prime exceeds three")
        raise AssertionError("reflected index is congruent to q modulo three")
    if reflected == target:
        if p_adic_valuation(triple_moment_factor(target), prime) != 0:
            raise AssertionError("terminal cancellation requires z_(2r-1)=0")
        raise AssertionError("reflection cannot create the terminal zero")
    if reflected < 2 * rank:
        raise AssertionError("all reflected positions below 2r have been excluded")

    if prime < 7 * rank + 3:
        raise AssertionError("reflected fivefold zero must force q>=7r+3")
    if prime == 7 * rank + 3:
        raise AssertionError("7r+3 is a nontrivial multiple of three")
    return "barrier", 7 * rank + 4, prime
