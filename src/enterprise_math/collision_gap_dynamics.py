"""E001.6 gap-update certificates connecting collapse contact to P018 carry.

The macro contact observable ``Q_d(g)=g//d`` is not future-sufficient under gap
updates by itself.  Write

    g = d*q + r,  0 <= r < d.

For a non-negative separating increment ``a``, exact projection gives

    Q_d(g+a) = q + (a//d) + floor((r + (a mod d))/d).

The final term is exactly the bounded addition carry across the current
``d``-fiber boundary.  This module reuses P018 ``addition_carry`` with ratio
``d`` as an arithmetic identity; it does not equate E001's physical/macroscopic
meaning of ``d`` with every scale-tag convention used elsewhere.

Consequently, even states with the same coarse gap/contact bit can have
different next coarse states under the same fine update unless enough boundary
information is retained.  For one fixed update language a smaller threshold
observable may suffice; choosing the coarsest future-compatible repair belongs
to A2/P023 rather than E001.
"""

from __future__ import annotations

from dataclasses import dataclass

from .collision_phase_diagram import macro_contact_from_gap
from .precision import addition_carry


@dataclass(frozen=True)
class GapSeparationUpdate:
    """Exact finite coarse/fiber response of one non-negative gap increment."""

    primitive_gap: int
    collapse_factor: int
    separation_increment: int
    coarse_before: int
    detail_before: int
    increment_coarse_part: int
    increment_detail: int
    carry: int
    coarse_after: int
    detail_after: int
    macro_contact_before: bool
    macro_contact_after: bool


def _require_nonnegative_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def gap_separation_update(
    primitive_gap: int,
    collapse_factor: int,
    separation_increment: int,
) -> GapSeparationUpdate:
    """Return exact P018-compatible carry data for ``g -> g+a``."""
    _require_nonnegative_int("primitive_gap", primitive_gap)
    _require_positive_int("collapse_factor", collapse_factor)
    _require_nonnegative_int("separation_increment", separation_increment)

    coarse_before, detail_before = divmod(primitive_gap, collapse_factor)
    increment_coarse, increment_detail = divmod(
        separation_increment, collapse_factor
    )
    coarse_after, carry, detail_after = addition_carry(
        primitive_gap,
        separation_increment,
        coarse=1,
        fine=collapse_factor,
    )
    if coarse_after != coarse_before + increment_coarse + carry:
        raise AssertionError("gap projection disagrees with coarse-part plus carry identity")
    if detail_after != (detail_before + increment_detail) % collapse_factor:
        raise AssertionError("gap detail update disagrees with fiber arithmetic")
    if coarse_after != (primitive_gap + separation_increment) // collapse_factor:
        raise AssertionError("gap coarse update disagrees with direct integer projection")

    return GapSeparationUpdate(
        primitive_gap=primitive_gap,
        collapse_factor=collapse_factor,
        separation_increment=separation_increment,
        coarse_before=coarse_before,
        detail_before=detail_before,
        increment_coarse_part=increment_coarse,
        increment_detail=increment_detail,
        carry=carry,
        coarse_after=coarse_after,
        detail_after=detail_after,
        macro_contact_before=macro_contact_from_gap(
            primitive_gap, collapse_factor
        ),
        macro_contact_after=macro_contact_from_gap(
            primitive_gap + separation_increment, collapse_factor
        ),
    )


def contact_exit_threshold_within_fiber(
    collapse_factor: int,
    separation_increment: int,
) -> int:
    """Smallest contact-fiber detail that exits ``Q_d=0`` after this increment.

    Return value lies in ``0..d``.  ``d`` means no current contact-fiber detail
    exits (only possible for zero increment).  ``0`` means every contact-fiber
    detail exits because the increment is at least one full collapse factor.

    For ``0 < a < d`` the exact threshold is ``d-a``:
    a contact state with detail ``r`` exits iff ``r >= d-a``.
    """
    _require_positive_int("collapse_factor", collapse_factor)
    _require_nonnegative_int("separation_increment", separation_increment)
    if separation_increment == 0:
        return collapse_factor
    if separation_increment >= collapse_factor:
        return 0
    return collapse_factor - separation_increment


def contact_exit_bit(
    primitive_gap: int,
    collapse_factor: int,
    separation_increment: int,
) -> bool:
    """Whether a currently collapsed contact leaves the contact fiber after update."""
    update = gap_separation_update(
        primitive_gap, collapse_factor, separation_increment
    )
    if not update.macro_contact_before:
        raise ValueError("contact_exit_bit requires a current macro-contact state")
    return not update.macro_contact_after
