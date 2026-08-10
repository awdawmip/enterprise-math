"""Reflection transport obstructions for twin-deferred primitive Franel rows.

The first-reentry kernel theorem reduces a twin-deferred primitive q-row to a
nonnegative Franel depth profile on r,...,T=2r-1.  Complete invisibility through
D_T forces an endpoint zero at T-1 with the same depth as the primitive source
at r, and every positive interior depth must sit at another twin-prime center.
Jarvis--Verrill reflection then transports every q-zero j to q-1-j.

This module records two consequences.

Boundary q=3r-1.
----------------
Reflection swaps r and T-1.  Any interior hidden zero s is a nontrivial twin
center, hence s=0 mod 3.  Its reflected zero s'=3r-2-s is either r+1 (for the
last interior vertex) or another interior vertex.  In the latter case s' would
also have to be a twin center, but s+s'=3r-2=1 mod 3, impossible.  The r+1
case is forbidden by nonadjacency with the primitive zero at r.  Primitivity
and reflection then exclude every remaining digit.  Therefore an actual
complete boundary escape has the exact zero alphabet

    Z_q = {r, 2r-2}.

This strengthens the earlier residue sieve q=17 or 35 (mod 72): complete
boundary escape is not merely sparse; it is a two-zero-digit event.

Intermediate 3r+1 <= q <= 4r-5.
--------------------------------
The reflected endpoint zero lands at

    s = q-2r+1,

strictly inside the first blackout.  Complete escape forces s to be another
twin center.  Since r and s are both 0 mod 3, q=s+2r-1 must be 2 mod 3.  If
q=5 or 7 mod 8, the forced Franel midpoint m=(q-1)/2 is also internal, but
2m-1=q-2 is then divisible by three and m cannot be a twin center.  Hence the
surviving intermediate classes are exactly

    q = 11 or 17 (mod 24)

as necessary residue classes.  Moreover, once s is hidden, no further q-zero
strictly between s and T-1 can remain hidden: its reflection is another vertex
in the same tail, and the two reflected indices sum to q-1=1 mod 3, so they
cannot both be nontrivial twin centers.

These are necessary escape obstructions, not a claim that an escaping Franel
row exists in any surviving residue class.
"""

from __future__ import annotations

from .p022_barlow_franel_lucas_rank import franel_zero_digits
from .p022_barlow_low_order_defect_reduction import _is_prime
from .p022_barlow_primitive_defect_criterion import is_primitive_franel_divisor
from .p022_barlow_primitive_successor_capture import is_twin_prime_deferral_center
from .p022_barlow_twin_defect_difference import (
    primitive_twin_first_defect_incidence,
    twin_blackout_target,
    twin_zero_local_visibility,
)


def _require_twin_rank(rank: int) -> None:
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 3:
        raise ValueError("rank must be an integer at least three")
    if not is_twin_prime_deferral_center(rank):
        raise ValueError("rank must be the center of an odd twin-prime pair")


def boundary_reflection_prime(rank: int) -> int:
    """Return q=3r-1 when it is prime."""
    _require_twin_rank(rank)
    prime = 3 * rank - 1
    if not _is_prime(prime):
        raise ValueError("boundary reflection value 3r-1 must be prime")
    return prime


def boundary_reflection_partner(rank: int, index: int) -> int:
    """Reflection j -> q-1-j at the dangerous boundary q=3r-1."""
    prime = boundary_reflection_prime(rank)
    if isinstance(index, bool) or not isinstance(index, int) or not 0 <= index < prime:
        raise ValueError("index must lie in 0..q-1")
    return prime - 1 - index


def boundary_hidden_interior_reflection_obstruction(rank: int, index: int) -> int:
    """A hidden interior twin vertex reflects to a vertex that cannot be hidden.

    The input index is assumed to be a positive interior kernel site, hence a
    twin center.  Its reflection is never another twin center.  At the final
    interior site the partner is r+1, which is also forbidden as a q-zero by
    recurrence nonadjacency with the primitive source r.
    """
    target = twin_blackout_target(rank)
    if isinstance(index, bool) or not isinstance(index, int):
        raise ValueError("index must be an integer")
    if not rank + 2 <= index <= target - 2:
        raise ValueError("index must be an interior first-blackout vertex")
    if not is_twin_prime_deferral_center(index):
        raise ValueError("a hidden positive interior kernel site must be a twin center")

    partner = boundary_reflection_partner(rank, index)
    if partner % 3 == 0:
        raise AssertionError("boundary reflected partner must be 1 modulo 3")
    if partner >= rank + 2:
        if twin_zero_local_visibility(partner) == (False, False):
            raise AssertionError("reflected interior partner cannot also be a twin center")
    else:
        if partner != rank + 1:
            raise AssertionError("only the last interior vertex may reflect next to the source")
    return partner


def boundary_complete_escape_zero_alphabet(rank: int, prime: int) -> tuple[int, int]:
    """Certify that an actual complete q=3r-1 escape has exactly two zero digits.

    This helper is conditional: it raises when the declared prime is not
    primitive at r or is already observed by a first-reentry defect.  If an
    actual complete escape is supplied, reflection + the exact kernel theorem
    force the full p-Lucas zero alphabet to be ``(r,2r-2)``.
    """
    expected_prime = boundary_reflection_prime(rank)
    if prime != expected_prime:
        raise ValueError("prime must equal the dangerous boundary 3r-1")
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at the declared Franel rank")
    if primitive_twin_first_defect_incidence(rank, prime) is not None:
        raise ValueError("the declared primitive row is not completely invisible through D_(2r-1)")

    target = twin_blackout_target(rank)
    expected = (rank, target - 1)
    actual = franel_zero_digits(prime)
    if actual != expected:
        raise AssertionError("complete boundary escape must have the two-point zero alphabet")
    return expected


def intermediate_transport_index(rank: int, prime: int) -> int:
    """Reflected endpoint index s=q-2r+1 in the strict intermediate window."""
    _require_twin_rank(rank)
    if (
        isinstance(prime, bool)
        or not isinstance(prime, int)
        or not _is_prime(prime)
    ):
        raise ValueError("prime must be prime")
    if not 3 * rank + 1 <= prime <= 4 * rank - 5:
        raise ValueError("prime must lie in 3r+1..4r-5")
    index = prime - 2 * rank + 1
    target = twin_blackout_target(rank)
    if not rank + 2 <= index <= target - 2:
        raise AssertionError("reflected endpoint must lie strictly inside the first blackout")
    return index


def intermediate_transport_survivor(rank: int, prime: int) -> tuple[int, int]:
    """Necessary hidden-endpoint and midpoint residue sieve.

    Returns ``(s, q mod 24)`` only when the reflected endpoint s is itself a
    twin center and the forced midpoint obstruction does not already expose the
    row.  Surviving residues are 11 or 17 modulo 24.
    """
    index = intermediate_transport_index(rank, prime)
    if not is_twin_prime_deferral_center(index):
        raise ValueError("reflected endpoint is visible because it is not a twin center")
    if prime % 3 != 2:
        raise AssertionError("two twin centers force the transported prime to be 2 modulo 3")

    if prime % 8 in (5, 7):
        middle = (prime - 1) // 2
        target = twin_blackout_target(rank)
        if not rank + 2 <= middle <= target - 2:
            raise AssertionError("forced midpoint must be internal in the transport window")
        if (prime - 2) % 3:
            raise AssertionError("q=2 mod3 makes q-2 composite by a factor of three")
        if is_twin_prime_deferral_center(middle):
            raise AssertionError("the forced midpoint cannot be a twin center")
        raise ValueError("forced Franel midpoint zero is visible inside the blackout")

    if prime % 8 not in (1, 3):
        raise AssertionError("odd prime has an unexpected mod-8 class")
    residue24 = prime % 24
    if residue24 not in (11, 17):
        raise AssertionError("intermediate transport residue reduction failed")
    return index, residue24


def intermediate_tail_reflection_obstruction(rank: int, prime: int, index: int) -> int:
    """No additional hidden q-zero may lie strictly above the transported s.

    For a surviving intermediate candidate, any hidden tail zero would have to
    be a twin center.  Its reflected partner stays in the same tail and cannot
    also be a twin center because the two indices sum to q-1=1 mod 3.
    """
    transported, _ = intermediate_transport_survivor(rank, prime)
    target = twin_blackout_target(rank)
    if isinstance(index, bool) or not isinstance(index, int):
        raise ValueError("index must be an integer")
    if not transported + 1 <= index <= target - 2:
        raise ValueError("index must lie strictly above s inside the blackout tail")
    if not is_twin_prime_deferral_center(index):
        raise ValueError("a hidden positive tail site must be a twin center")

    partner = prime - 1 - index
    if not transported + 1 <= partner <= target - 2:
        raise AssertionError("reflection must preserve the strict tail interval")
    if partner % 3 == 0:
        raise AssertionError("reflected partner must be 1 modulo 3")
    if is_twin_prime_deferral_center(partner):
        raise AssertionError("a reflected tail pair cannot contain two twin centers")
    return partner
