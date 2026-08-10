"""Delayed re-entry of primitive Franel rows at twin-prime centers.

Let p be primitive at Franel rank r>3 and suppose 2r-1,2r+1 are twin
primes.  The immediate current/successor defects do not exist.  Put

    q=2r-1.

Since every twin center r>3 is divisible by three, the odd boundary of D_q is
4r-3, a nontrivial multiple of three.  Thus D_q exists.

The canonical central-binomial relation at q has, above the primitive rank,
exactly

    alpha_(q,r)   = -1,
    alpha_(q,q-1) = +1,

and every other support index is <r.  Therefore a primitive p-adic row obeys

    v_p(D_q)=v_p(F_q)-v_p(F_(q-1))+v_p(F_r).

Adjacent Franel zeros are impossible.  Hence this delayed capture vanishes
only in the equal-depth collision

    p|F_(2r-2),  v_p(F_(2r-2))=v_p(F_r).

Reflection plus primitiveness forces any such collision to satisfy p>=3r-1.
So all primitive twin-center primes in 2r+1 <= p < 3r-1 are guaranteed to
re-enter nontrivially at D_(2r-1).
"""

from __future__ import annotations

from .p022_barlow_low_order_defect_reduction import (
    composite_A_relation_exponents,
    franel_defect_valuation,
)
from .p022_barlow_low_order_identifiability import (
    p_adic_valuation,
    triple_moment_factor,
)
from .p022_barlow_primitive_defect_criterion import is_primitive_franel_divisor
from .p022_barlow_primitive_successor_capture import is_twin_prime_deferral_center


def _require_twin_center(rank: int) -> None:
    if isinstance(rank, bool) or not isinstance(rank, int) or rank <= 3:
        raise ValueError("rank must be an integer greater than three")
    if not is_twin_prime_deferral_center(rank):
        raise ValueError("rank must be a twin-prime deferral center")
    if rank % 3 != 0:
        raise AssertionError("every twin center above three must be divisible by three")


def twin_reentry_segment(rank: int) -> int:
    """Return q=2r-1 and certify D_q exists."""
    _require_twin_center(rank)
    segment = 2 * rank - 1
    odd_boundary = 2 * segment - 1
    if odd_boundary != 4 * rank - 3:
        raise AssertionError("re-entry boundary identity changed")
    if odd_boundary <= 3 or odd_boundary % 3 != 0:
        raise AssertionError("twin-center re-entry boundary must be composite")
    return segment


def twin_reentry_high_relation_support(rank: int) -> tuple[tuple[int, int], ...]:
    """Return the part of alpha_(2r-1) supported at indices >=r."""
    segment = twin_reentry_segment(rank)
    relation = composite_A_relation_exponents(segment)
    high = tuple((index, exponent) for index, exponent in relation if index >= rank)
    expected = ((rank, -1), (segment - 1, 1))
    if high != expected:
        raise AssertionError("twin re-entry relation support changed")
    return high


def primitive_twin_reentry_valuation(rank: int, prime: int) -> tuple[int, int, int, int]:
    """Return (defect valuation,z,w_(2r-2),w_(2r-1))."""
    _require_twin_center(rank)
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at the declared Franel rank")
    segment = twin_reentry_segment(rank)
    twin_reentry_high_relation_support(rank)

    depth = p_adic_valuation(triple_moment_factor(rank), prime)
    previous_depth = p_adic_valuation(triple_moment_factor(segment - 1), prime)
    current_depth = p_adic_valuation(triple_moment_factor(segment), prime)
    if depth <= 0:
        raise AssertionError("primitive depth must be positive")
    if previous_depth > 0 and current_depth > 0:
        raise AssertionError("adjacent Franel zeros are impossible")

    predicted = current_depth - previous_depth + depth
    actual = franel_defect_valuation(segment, prime)
    if actual != predicted:
        raise AssertionError("twin-center delayed re-entry formula failed")
    return actual, depth, previous_depth, current_depth


def twin_reentry_failure_is_equal_depth_collision(rank: int, prime: int) -> bool:
    """Certify the exact vanishing criterion at D_(2r-1)."""
    actual, depth, previous_depth, current_depth = primitive_twin_reentry_valuation(
        rank,
        prime,
    )
    collision = previous_depth == depth and previous_depth > 0
    if collision and current_depth != 0:
        raise AssertionError("collision predecessor excludes the adjacent zero")
    if (actual == 0) != collision:
        raise AssertionError("delayed re-entry vanishes only by equal-depth collision")
    return collision


def twin_reentry_collision_requires_one_third_threshold(rank: int, prime: int) -> bool:
    """Certify that a predecessor collision can occur only for p>=3r-1.

    If p divides F_(2r-2), reflection supplies the zero digit p-2r+1.
    Primitiveness at r forces that reflected digit to be at least r, hence
    p>=3r-1.
    """
    _, _, previous_depth, _ = primitive_twin_reentry_valuation(rank, prime)
    if previous_depth == 0:
        return True
    if prime < 3 * rank - 1:
        raise AssertionError("reflection would create a zero digit below the primitive rank")
    return True


def twin_reentry_is_forced_below_one_third_threshold(rank: int, prime: int) -> bool:
    """For primitive p<3r-1, certify a nonzero delayed pivot at D_(2r-1)."""
    if prime >= 3 * rank - 1:
        raise ValueError("prime must lie below the one-third collision threshold")
    actual, _, previous_depth, _ = primitive_twin_reentry_valuation(rank, prime)
    if previous_depth != 0:
        raise AssertionError("reflection forbids the dangerous predecessor zero below threshold")
    if actual == 0:
        raise AssertionError("twin row must re-enter below the one-third threshold")
    return True
