"""Strict reflection-transport window for twin-deferred primitive Franel rows.

Let r be a nontrivial twin-prime deferral center, T=2r-1, and let q be a
primitive Franel prime at rank r.  Assume the first-reentry defects through T
all vanish and that q lies in the strict reflection window

    3r-1 < q < 4r-3.

Terminal cancellation gives q|F_(T-1).  Reflecting that endpoint produces

    s = q-2r+1.

Primitivity and the exact first-reentry kernel force s to lie strictly inside
the blackout and to be another twin-prime center.  Hence r=s=0 (mod 3) and
q=2 (mod 3).  Reflection pairs s with T-1.  Any further zero strictly between
s and T-1 would have its reflected partner in the same interval; complete
escape would force both members to be twin centers, but their sum is q-1=1
(mod 3), impossible.  Thus

    q does not divide F_j for s<j<T-1.

In particular the forced Franel midpoint cannot vanish, so strict transport can
survive only for q=1 or 3 (mod 8), equivalently q=11 or 17 (mod 24).

Two finite capture gates then compress the surviving window further.

First put Q=2r+1.  Reflection plus the first kernel forces q not to divide
F_(2r).  If 4r+1 is composite then D_Q exists and

    v_q(D_Q)=v_q(F_Q)-v_q(F_r),
    v_q(D_(Q+1))=v_q(F_(Q+1))-v_q(F_Q).

The second defect always exists because 4r+3 is divisible by three.  If both
were zero, two adjacent Franel depths would both equal the positive primitive
depth, contradicting recurrence nonadjacency.  Therefore escape beyond Q+1
forces 4r+1 to be prime.

Second put n0=3r-1.  This segment always has composite odd boundary
2n0-1=3(2r-1).  Reflection forces both F_(n0-1) and F_n0 to be q-units.  If
n0 is composite, its canonical A-relation has high support only A_r and
A_(n0-1), so v_q(D_n0)=-v_q(F_r).  If n0 is prime, then r is even and the only
additional high relation pair is at

    m-1, m,  where m=3r/2.

The index m-1 is not a twin center and therefore is a q-unit under the first
kernel.  Hence vanishing of D_n0 forces v_q(F_m)=v_q(F_r)>0, so m must itself
be a twin center and 3r+1 must also be prime.  If m>s -- equivalently
2q<7r-2 -- the zero-free transport gap already rules out q|F_m, and D_n0
captures immediately.

Thus the lower part of the strict transport window is closed, while survival in
the upper part forces the enlarged prime constellation

    2r-1, 2r+1, 4r-5, 4r+1, 3r-1, 3r+1

(with the last two required only after the n0 gate is reached).

Franel reflection, p-Lucas, and recurrence nonadjacency are prior art.  The
P022 content is the exact coupling to the deleted-edge defect kernel and the
fixed later capture gates Q,Q+1,n0.
"""

from __future__ import annotations

from .p022_barlow_franel_lucas_rank import franel_midpoint_zero_criterion
from .p022_barlow_low_order_defect_reduction import (
    _is_prime,
    composite_A_relation_exponents,
)
from .p022_barlow_primitive_successor_capture import is_twin_prime_deferral_center
from .p022_barlow_twin_defect_difference import twin_blackout_target, twin_zero_local_visibility


def _require_strict_transport(rank: int, prime: int) -> tuple[int, int]:
    target = twin_blackout_target(rank)
    if not _is_prime(prime):
        raise ValueError("prime must be prime")
    if not 3 * rank - 1 < prime < 4 * rank - 3:
        raise ValueError("prime must lie in the strict transport window")
    reflected_endpoint = prime - 2 * rank + 1
    if reflected_endpoint == rank + 1:
        raise AssertionError("q=3r would be composite")
    if not rank + 2 <= reflected_endpoint <= target - 3:
        raise AssertionError("strict endpoint reflection must lie inside the blackout")
    return target, reflected_endpoint


def strict_transport_front(rank: int, prime: int) -> tuple[int, int]:
    """Return (s,q mod24) after certifying the arithmetic front conditions.

    This helper is the arithmetic part of the complete-escape theorem: callers
    must only use it once the reflected endpoint s is known to be a q-zero and
    therefore must be hidden by the first-reentry kernel.
    """
    _, s = _require_strict_transport(rank, prime)
    if twin_zero_local_visibility(s) != (False, False):
        raise ValueError("complete escape requires the reflected endpoint to be a twin center")
    if rank % 3 or s % 3:
        raise AssertionError("nontrivial twin centers are divisible by three")
    if prime != s + 2 * rank - 1 or prime % 3 != 2:
        raise AssertionError("transport identity must force q=2 modulo three")
    residue = prime % 24
    if residue not in (5, 11, 17, 23):
        raise AssertionError("odd q=2 mod3 has an unexpected residue modulo 24")
    return s, residue


def strict_transport_zero_free_gap(rank: int, prime: int, zero_digits: tuple[int, ...]) -> tuple[int, int]:
    """Certify that an escaping reflection front leaves (s,T-1) zero-free."""
    target, s = _require_strict_transport(rank, prime)
    strict_transport_front(rank, prime)
    zero_set = set(zero_digits)
    if s not in zero_set or target - 1 not in zero_set:
        raise ValueError("transport endpoints s and T-1 must both be q-zero digits")
    for digit in zero_digits:
        if not s < digit < target - 1:
            continue
        reflected = prime - 1 - digit
        if not s < reflected < target - 1:
            raise AssertionError("reflection must preserve the open transport gap")
        if reflected not in zero_set:
            raise AssertionError("zero alphabet must be reflection symmetric")
        if twin_zero_local_visibility(digit) != (False, False):
            raise ValueError("complete escape requires every gap zero to be a twin center")
        if twin_zero_local_visibility(reflected) != (False, False):
            raise ValueError("reflected gap zero must also be a twin center")
        if digit % 3 or reflected % 3:
            raise AssertionError("nontrivial twin centers must be divisible by three")
        if (digit + reflected) % 3 != (prime - 1) % 3:
            raise AssertionError("reflection sum changed")
        raise AssertionError("two hidden gap zeros cannot sum to 1 modulo three")
    return s, target - 1


def strict_transport_surviving_residue(rank: int, prime: int) -> int:
    """Midpoint obstruction: complete strict transport needs q=11 or17 mod24."""
    target, s = _require_strict_transport(rank, prime)
    _, residue = strict_transport_front(rank, prime)
    midpoint = (prime - 1) // 2
    if not s < midpoint < target - 1:
        raise AssertionError("midpoint must lie in the strict zero-free gap")
    if prime % 8 in (5, 7):
        if not franel_midpoint_zero_criterion(prime):
            raise AssertionError("forced midpoint criterion changed")
        raise ValueError("q=5 or7 mod8 is incompatible with the zero-free transport gap")
    if prime % 8 not in (1, 3) or residue not in (11, 17):
        raise AssertionError("strict transport CRT reduction failed")
    return residue


def strict_transport_Q_high_support(rank: int) -> tuple[tuple[int, int], ...]:
    """High relation at Q=2r+1 when 4r+1 is composite."""
    twin_blackout_target(rank)
    segment = 2 * rank + 1
    if _is_prime(4 * rank + 1):
        raise ValueError("D_(2r+1) is absent when 4r+1 is prime")
    high = tuple(
        (index, exponent)
        for index, exponent in composite_A_relation_exponents(segment)
        if index >= rank
    )
    expected = ((rank, 1), (rank + 1, -1), (2 * rank, 1))
    if high != expected:
        raise AssertionError("Q-gate relation escaped the three-term high support")
    return high


def strict_transport_Q_plus_one_high_support(rank: int) -> tuple[tuple[int, int], ...]:
    """D_(2r+2) always exists and only sees the previous high index."""
    twin_blackout_target(rank)
    segment = 2 * rank + 2
    if (4 * rank + 3) % 3 or _is_prime(4 * rank + 3):
        raise AssertionError("4r+3 must be a nontrivial multiple of three")
    high = tuple(
        (index, exponent)
        for index, exponent in composite_A_relation_exponents(segment)
        if index >= rank
    )
    expected = ((2 * rank + 1, 1),)
    if high != expected:
        raise AssertionError("Q+1 gate relation escaped the one-edge high support")
    return high


def strict_transport_n0_high_support(rank: int) -> tuple[tuple[int, int], ...]:
    """Canonical high support at the fixed later segment n0=3r-1."""
    twin_blackout_target(rank)
    segment = 3 * rank - 1
    if _is_prime(2 * segment - 1):
        raise AssertionError("2n0-1=3(2r-1) must be composite")
    high = tuple(
        (index, exponent)
        for index, exponent in composite_A_relation_exponents(segment)
        if index >= rank
    )
    if _is_prime(segment):
        if rank % 2:
            raise AssertionError("3r-1 prime forces r even")
        middle = 3 * rank // 2
        expected = (
            (rank, 1),
            (middle - 1, 1),
            (middle, -1),
            (segment - 1, 1),
        )
    else:
        expected = ((rank, 1), (segment - 1, 1))
    if high != expected:
        raise AssertionError("n0 gate relation has unexpected high support")
    return high


def strict_transport_lower_window_is_captured(rank: int, prime: int) -> bool:
    """Structural lower-window theorem: 2q<7r-2 leaves no n0 cancellation.

    Returns True after checking that either n0 is composite (direct -z_r
    capture) or, when n0 is prime, its sole candidate middle index lies inside
    the zero-free interval (s,T-1).
    """
    target, s = _require_strict_transport(rank, prime)
    if not 2 * prime < 7 * rank - 2:
        raise ValueError("prime is not in the strict lower transport subwindow")
    strict_transport_n0_high_support(rank)
    segment = 3 * rank - 1
    if not _is_prime(segment):
        return True
    middle = 3 * rank // 2
    if not s < middle < target - 1:
        raise AssertionError("lower-window inequality must place m in the zero-free gap")
    return True


def strict_transport_survival_requires_scaled_twin(rank: int, prime: int) -> tuple[int, int]:
    """Upper n0 gate: survival forces m=3r/2 to be another twin center."""
    _, s = _require_strict_transport(rank, prime)
    segment = 3 * rank - 1
    if not _is_prime(segment):
        raise ValueError("survival at n0 first requires 3r-1 prime")
    if rank % 2:
        raise AssertionError("3r-1 prime forces r even")
    middle = 3 * rank // 2
    if middle > s:
        raise ValueError("m lies in the zero-free transport gap and cannot cancel n0")
    if not is_twin_prime_deferral_center(middle):
        raise ValueError("n0 cancellation requires m to be a twin-prime center")
    if not _is_prime(3 * rank + 1):
        raise AssertionError("scaled twin center must force 3r+1 prime")
    return middle, 3 * rank + 1
