"""Twin-prime blackout defects are a one-dimensional Franel depth difference.

Let ``r>=3`` be the center of an odd twin-prime pair, so

    2r-1 and 2r+1

are both prime, and put ``T=2r-1``.  The primitive-successor theorem therefore
has no defect column at ``r`` or ``r+1``.  The canonical central-binomial
relations are nevertheless much more rigid than a generic delayed capture.

For every composite-boundary segment

    r+2 <= n < T,

the only relation index at least ``r`` is ``n-1``, with coefficient +1.  At
the terminal composite-boundary segment ``T`` the only relation indices at
least ``r`` are

    r   with coefficient -1,
    T-1 with coefficient +1.

The proof is elementary from the recursive central-binomial integer basis.
For ``n<T`` every prime factor of ``n`` is below ``2r-1``.  Since ``2n-1`` is
odd composite, its largest prime factor is at most ``(2n-1)/3``; hence both
integer-basis expansions use only indices below ``r``.  At ``n=T``, the prime
integer ``T=2r-1`` contributes the new basis index ``r`` exactly once, while
``2T-1=4r-3`` is divisible by three because every nontrivial twin-prime center
is divisible by three.

Consequently, for any prime ``q`` primitive for the Franel sequence at rank
``r`` and ``z_j=v_q(F_j)``, the defect valuations satisfy the exact formulas

    v_q(D_n) = z_n - z_(n-1)                  (r+2 <= n < T),
    v_q(D_T) = z_T - z_(T-1) + z_r.           (terminal re-entry)

This separates the geometry from the number theory: inside the twin blackout,
all later arithmetic is carried by the one-dimensional depth sequence ``z``.
A zero digit at index ``s`` produces a positive local atom at ``D_s`` when
``2s-1`` is composite and a negative local atom at ``D_(s+1)`` when ``2s+1``
is composite.  It is locally invisible exactly when both odd boundaries are
prime, i.e. when ``s`` is itself another twin-prime center.

There is also a sharp reflection-safe window.  If ``q`` is primitive at ``r``
and

    2r+1 <= q < 3r-1,

then the Jarvis--Verrill reflection of a hypothetical zero at ``2r-2`` or
``2r-1`` would lie at a positive index below ``r``, contradicting primitivity.
Thus

    v_q(D_(2r-1)) = v_q(F_r) > 0.

At the boundary ``q=3r-1`` the reflection of ``2r-2`` is exactly ``r``; this is
therefore the first genuinely dangerous endpoint for cancellation.  The module
does not claim that such a dangerous primitive divisor exists.

The Franel recurrence, p-Lucas property, and Jarvis--Verrill reflection are
prior art.  The P022 contribution here is their exact interaction with the
canonical Franel-defect basis and the resulting depth-difference/visibility
reduction.
"""

from __future__ import annotations

from .p022_barlow_low_order_defect_reduction import (
    _is_prime,
    composite_A_relation_exponents,
    composite_indices,
    franel_defect_valuation,
)
from .p022_barlow_low_order_identifiability import p_adic_valuation, triple_moment_factor
from .p022_barlow_primitive_defect_criterion import is_primitive_franel_divisor
from .p022_barlow_primitive_successor_capture import is_twin_prime_deferral_center


def _require_twin_rank(rank: int) -> None:
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 3:
        raise ValueError("rank must be an integer at least three")
    if not is_twin_prime_deferral_center(rank):
        raise ValueError("rank must be the center of an odd twin-prime pair")


def twin_blackout_target(rank: int) -> int:
    """First canonical A_r re-entry column after a twin-prime deferral."""
    _require_twin_rank(rank)
    target = 2 * rank - 1
    if _is_prime(2 * target - 1):
        raise AssertionError("4r-3 must be composite for a nontrivial twin center")
    return target


def twin_blackout_high_support(rank: int, segment: int) -> tuple[tuple[int, int], ...]:
    """Exact relation support at indices >=r inside the twin blackout.

    Interior composite columns have only ``(n-1,+1)``.  The terminal column
    additionally has ``(r,-1)``.
    """
    target = twin_blackout_target(rank)
    if isinstance(segment, bool) or not isinstance(segment, int):
        raise ValueError("segment must be an integer")
    if segment < rank + 2 or segment > target:
        raise ValueError("segment must lie in the closed twin-blackout defect range")
    if _is_prime(2 * segment - 1):
        raise ValueError("segment must have composite odd boundary")

    high = tuple(
        (index, exponent)
        for index, exponent in composite_A_relation_exponents(segment)
        if index >= rank
    )
    expected = (
        ((segment - 1, 1),)
        if segment < target
        else ((rank, -1), (target - 1, 1))
    )
    if high != expected:
        raise AssertionError("twin-blackout high support escaped the one-dimensional form")
    return high


def twin_zero_local_visibility(index: int) -> tuple[bool, bool]:
    """Return whether a zero at ``index`` has direct/successor defect atoms.

    The pair is ``(D_index exists, D_(index+1) exists)``.  ``(False,False)`` is
    exactly the twin-prime hidden case.
    """
    if isinstance(index, bool) or not isinstance(index, int) or index < 2:
        raise ValueError("index must be an integer at least two")
    direct = not _is_prime(2 * index - 1)
    successor = not _is_prime(2 * index + 1)
    return direct, successor


def primitive_twin_defect_difference(rank: int, prime: int, segment: int) -> int:
    """Return the exact q-adic defect valuation via the depth-difference law."""
    target = twin_blackout_target(rank)
    twin_blackout_high_support(rank, segment)
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at the declared Franel rank")

    z_segment = p_adic_valuation(triple_moment_factor(segment), prime)
    z_previous = p_adic_valuation(triple_moment_factor(segment - 1), prime)
    expected = z_segment - z_previous
    if segment == target:
        expected += p_adic_valuation(triple_moment_factor(rank), prime)

    actual = franel_defect_valuation(segment, prime)
    if actual != expected:
        raise AssertionError("defect valuation disagrees with twin depth-difference law")
    return actual


def primitive_twin_first_defect_incidence(rank: int, prime: int) -> tuple[int, int] | None:
    """First nonzero defect incidence after the twin-deferred primitive rank."""
    target = twin_blackout_target(rank)
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at the declared Franel rank")
    for segment in composite_indices(target):
        if segment < rank + 2:
            continue
        value = primitive_twin_defect_difference(rank, prime, segment)
        if value:
            return segment, value
    return None


def primitive_twin_terminal_depths(rank: int, prime: int) -> tuple[int, int, int, int]:
    """Return ``(z_r,z_(T-1),z_T,v_q(D_T))`` for the terminal re-entry."""
    target = twin_blackout_target(rank)
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at the declared Franel rank")
    z_rank = p_adic_valuation(triple_moment_factor(rank), prime)
    z_previous = p_adic_valuation(triple_moment_factor(target - 1), prime)
    z_target = p_adic_valuation(triple_moment_factor(target), prime)
    value = primitive_twin_defect_difference(rank, prime, target)
    if value != z_target - z_previous + z_rank:
        raise AssertionError("terminal depth identity changed")
    return z_rank, z_previous, z_target, value


def primitive_twin_reflection_safe_target(rank: int, prime: int) -> tuple[int, int]:
    """Safe-window theorem: q<3r-1 forces the terminal pivot to equal z_r.

    Primitivity already forces an odd primitive prime to be at least ``2r+1``.
    In the strict window below ``3r-1``, reflection of a zero at ``2r-2`` or
    ``2r-1`` would create a positive zero below ``r``.  Hence both endpoint
    depths vanish and the terminal defect valuation is exactly the primitive
    depth.
    """
    target = twin_blackout_target(rank)
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at the declared Franel rank")
    if prime < 2 * rank + 1:
        raise AssertionError("primitive twin marker violates the reflection size bound")
    if prime >= 3 * rank - 1:
        raise ValueError("prime is outside the strict reflection-safe window")

    z_rank, z_previous, z_target, value = primitive_twin_terminal_depths(rank, prime)
    if z_previous != 0 or z_target != 0:
        raise AssertionError("reflection-safe endpoint must contain no later Franel zero")
    if value != z_rank or value <= 0:
        raise AssertionError("safe-window terminal pivot must recover primitive depth")
    return target, value


def primitive_twin_terminal_cancellation_signature(
    rank: int, prime: int
) -> tuple[int, int, int] | None:
    """If the terminal pivot vanishes, expose its necessary endpoint signature.

    A zero terminal valuation forces ``z_(T-1)=z_T+z_r``.  Since consecutive
    Franel zero digits below ``prime`` are impossible by the Franel recurrence,
    this specializes to ``z_T=0`` and ``z_(T-1)=z_r`` for genuine primes.  The
    reflection argument then requires ``prime>=3r-1``.  This helper records the
    exact arithmetic quantities; it does not assert existence of cancellation.
    """
    target = twin_blackout_target(rank)
    z_rank, z_previous, z_target, value = primitive_twin_terminal_depths(rank, prime)
    if value != 0:
        return None
    if z_previous != z_target + z_rank:
        raise AssertionError("vanishing terminal pivot has the wrong depth balance")
    if prime < 3 * rank - 1:
        raise AssertionError("terminal cancellation cannot occur inside the safe window")
    return z_rank, z_previous, z_target
