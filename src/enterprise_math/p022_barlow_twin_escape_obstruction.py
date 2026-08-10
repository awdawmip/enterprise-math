"""Necessary arithmetic geometry for complete escape of a twin-deferred row.

Continue the setup of :mod:`p022_barlow_twin_defect_difference`.  Let ``r`` be
an odd twin-prime center, ``T=2r-1``, and let ``q`` be a prime primitive for the
Franel sequence at rank ``r``.  Write ``z_j=v_q(F_j)``.

The depth-difference theorem gives

    v_q(D_n)=z_n-z_(n-1)            for r+2 <= n < T,
    v_q(D_T)=z_T-z_(T-1)+z_r.

Because the Franel recurrence has invertible backward coefficient for indices
below ``q``, two consecutive Franel terms below ``q`` cannot both vanish
modulo ``q``.  Since an odd primitive divisor satisfies ``q>=2r+1>T``, terminal
cancellation has the exact form

    v_q(D_T)=0  iff  z_(T-1)=z_r.

In particular ``z_T=0`` automatically in the cancelling case.  Reflection of
the endpoint zero ``T-1=2r-2`` gives another zero at

    s = q-2r+1.

Primitivity therefore forces ``q>=3r-1``.

Complete invisibility through the first canonical re-entry is even narrower.
If every existing defect column from ``r+2`` through ``T`` has zero q-adic
valuation, then necessarily:

1. ``4r-5`` is prime, so the positive endpoint atom at ``D_(T-1)`` is absent;
2. ``z_(T-1)=z_r`` (terminal equal-depth cancellation);
3. every other q-zero index ``u`` with ``r+2 <= u <= T-2`` is itself a
   twin-prime center, because otherwise either ``D_u`` or ``D_(u+1)`` sees the
   local depth jump;
4. ``q>=3r-1``;
5. when ``3r-1 < q < 4r-3``, the reflected endpoint zero
   ``s=q-2r+1`` lies strictly inside the blackout and is therefore another
   twin-prime center.

Thus a putative escaping valuation row is forced onto a simultaneous Franel
common-depth condition and a sparse prime constellation.  This is a necessary
condition only; existence of such a row is not asserted.
"""

from __future__ import annotations

from .p022_barlow_low_order_defect_reduction import _is_prime, composite_indices
from .p022_barlow_low_order_identifiability import p_adic_valuation, triple_moment_factor
from .p022_barlow_primitive_defect_criterion import is_primitive_franel_divisor
from .p022_barlow_twin_defect_difference import (
    primitive_twin_defect_difference,
    primitive_twin_terminal_depths,
    twin_blackout_target,
    twin_zero_local_visibility,
)


def _require_primitive_twin_row(rank: int, prime: int) -> int:
    target = twin_blackout_target(rank)
    if not is_primitive_franel_divisor(rank, prime):
        raise ValueError("prime must be primitive at the declared twin Franel rank")
    if prime <= target:
        raise AssertionError("primitive prime must lie beyond the first re-entry target")
    return target


def terminal_cancellation_is_equal_depth(rank: int, prime: int) -> bool:
    """Certify ``v_q(D_T)=0`` iff ``v_q(F_(T-1))=v_q(F_r)``.

    The executable check uses the exact valuations; the mathematical reduction
    uses the Franel three-term recurrence to forbid adjacent q-zero terms below
    q.
    """
    target = _require_primitive_twin_row(rank, prime)
    z_rank, z_previous, z_target, defect = primitive_twin_terminal_depths(rank, prime)
    equal_depth = z_previous == z_rank
    if equal_depth and z_rank <= 0:
        raise AssertionError("primitive depth must be positive")
    if z_previous > 0 and z_target > 0:
        raise AssertionError("adjacent Franel zeros below q are impossible")
    if (defect == 0) != equal_depth:
        raise AssertionError("terminal cancellation is not equivalent to equal endpoint depth")
    if defect == 0 and z_target != 0:
        raise AssertionError("terminal cancellation must have z_T=0")
    if target != 2 * rank - 1:
        raise AssertionError("unexpected twin target")
    return defect == 0


def terminal_reflection_index(rank: int, prime: int) -> int | None:
    """Reflection of the terminal endpoint zero, when terminal cancellation occurs."""
    if not terminal_cancellation_is_equal_depth(rank, prime):
        return None
    reflected = prime - 2 * rank + 1
    if reflected < rank:
        raise AssertionError("primitivity forbids terminal cancellation for q<3r-1")
    return reflected


def complete_escape_signature(rank: int, prime: int) -> tuple[int, int, tuple[int, ...], int] | None:
    """Return the necessary signature when the row is invisible through D_T.

    Output is ``(target, endpoint_depth, interior_zero_indices, reflected)``.
    ``None`` means some existing defect in the first re-entry window detects the
    row.  A non-None return certifies all five necessary conditions documented
    in this module.
    """
    target = _require_primitive_twin_row(rank, prime)
    columns = tuple(
        segment
        for segment in composite_indices(target)
        if rank + 2 <= segment <= target
    )
    if any(primitive_twin_defect_difference(rank, prime, segment) != 0 for segment in columns):
        return None

    if not terminal_cancellation_is_equal_depth(rank, prime):
        raise AssertionError("complete escape must cancel at the terminal column")
    if not _is_prime(4 * rank - 5):
        raise AssertionError("complete escape requires D_(T-1) to be absent")

    z_rank, z_previous, z_target, terminal = primitive_twin_terminal_depths(rank, prime)
    if terminal != 0 or z_previous != z_rank or z_target != 0:
        raise AssertionError("complete escape lost the equal-depth terminal signature")
    if prime < 3 * rank - 1:
        raise AssertionError("reflection forces q>=3r-1")

    interior_zeros = tuple(
        index
        for index in range(rank + 2, target - 1)
        if p_adic_valuation(triple_moment_factor(index), prime) > 0
    )
    for index in interior_zeros:
        if twin_zero_local_visibility(index) != (False, False):
            raise AssertionError("every interior zero of an escaping row must be a twin center")

    reflected = prime - 2 * rank + 1
    if 3 * rank - 1 < prime < 4 * rank - 3:
        if not (rank < reflected < target - 1):
            raise AssertionError("reflected endpoint zero should lie inside the blackout")
        if twin_zero_local_visibility(reflected) != (False, False):
            raise AssertionError("internal reflected endpoint zero must be another twin center")

    return target, z_rank, interior_zeros, reflected


def escape_geometry_primes(rank: int) -> tuple[int, int, int]:
    """Three odd primes forced by twin deferral plus endpoint invisibility.

    This helper checks only the geometry side: ``2r-1``, ``2r+1`` and
    ``4r-5``.  It does not assert existence of a matching primitive Franel row.
    """
    target = twin_blackout_target(rank)
    values = (2 * rank - 1, 2 * rank + 1, 4 * rank - 5)
    if not all(_is_prime(value) for value in values):
        raise ValueError("rank does not satisfy the complete-escape prime constellation")
    if target != values[0]:
        raise AssertionError("target/boundary mismatch")
    return values
