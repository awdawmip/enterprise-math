"""E001.4 exact contact information retained by common-collapse supports.

A Boolean collision bit discards structure.  For the current axis-aligned E001
supports, the shared terminal target set is one finite integer rectangle.  Its
axis counts describe *overlap witnesses*.  Separating the supports is a distinct
question: when one interval contains the other, overlap width is not the number
of unit translations required to make the two supports disjoint.

This module therefore keeps witness geometry and separation geometry separate.
All quantities are finite integers.  They are intentionally not interpreted as
force, impulse, energy, or a physical penetration law.
"""

from __future__ import annotations

from dataclasses import dataclass

from .common_collapse import (
    common_collapse_target_bounds,
    common_collapse_witness,
    terminal_collapse_target_bounds,
)
from .engineering_collision import Body2D, Pair

Vector2D = tuple[int, int]


@dataclass(frozen=True)
class CollapseContact2D:
    """Exact finite geometry of one nonempty common-collapse target rectangle.

    ``x_count`` and ``y_count`` count shared terminal targets along each axis.
    ``x_signed_separations`` and ``y_signed_separations`` instead describe the
    signed relative translations of the *right* body (left held fixed) that
    first make the two closed integer support intervals disjoint on that axis.

    A negative entry moves the right body toward decreasing coordinates; a
    positive entry moves it toward increasing coordinates.  The globally
    shortest axis-only relative translations are retained in
    ``minimum_relative_corrections``.
    """

    pair: Pair
    x_count: int
    y_count: int
    shared_target_count: int
    x_signed_separations: tuple[int, int]
    y_signed_separations: tuple[int, int]
    minimum_axis_separation_steps: int
    minimum_axes: tuple[str, ...]
    minimum_relative_corrections: tuple[Vector2D, ...]
    witness: tuple[int, int]


def _signed_interval_separations(
    left_lo: int,
    left_hi: int,
    right_lo: int,
    right_hi: int,
) -> tuple[int, int]:
    """Return exact negative/positive relative shifts that first separate intervals.

    The two input closed integer intervals must overlap.  Translating the right
    interval by ``negative`` puts its upper endpoint immediately below
    ``left_lo``.  Translating it by ``positive`` puts its lower endpoint
    immediately above ``left_hi``.
    """
    if left_hi < right_lo or right_hi < left_lo:
        raise ValueError("intervals must overlap")
    negative = -(right_hi - left_lo + 1)
    positive = left_hi - right_lo + 1
    if negative >= 0 or positive <= 0:
        raise AssertionError("overlapping intervals produced invalid separation shifts")
    return negative, positive


def collapse_contact_profile(left: Body2D, right: Body2D) -> CollapseContact2D | None:
    """Return exact shared-target and minimum relative-separation data.

    ``minimum_axis_separation_steps`` is the minimum L1 magnitude of an
    axis-only *relative* translation that makes the supports disjoint.  It is
    not generally equal to ``min(x_count, y_count)``: containment is the
    smallest counterexample.
    """
    if left.body_id == right.body_id:
        raise ValueError("contact pair must contain two distinct body ids")

    shared_bounds = common_collapse_target_bounds(left, right)
    if shared_bounds is None:
        return None
    x_lo, x_hi, y_lo, y_hi = shared_bounds
    x_count = x_hi - x_lo + 1
    y_count = y_hi - y_lo + 1
    shared = x_count * y_count

    left_x_lo, left_x_hi, left_y_lo, left_y_hi = terminal_collapse_target_bounds(left)
    right_x_lo, right_x_hi, right_y_lo, right_y_hi = terminal_collapse_target_bounds(right)
    x_shifts = _signed_interval_separations(
        left_x_lo, left_x_hi, right_x_lo, right_x_hi
    )
    y_shifts = _signed_interval_separations(
        left_y_lo, left_y_hi, right_y_lo, right_y_hi
    )

    x_minimum = min(abs(shift) for shift in x_shifts)
    y_minimum = min(abs(shift) for shift in y_shifts)
    minimum = min(x_minimum, y_minimum)
    axes = tuple(
        axis
        for axis, count in (("x", x_minimum), ("y", y_minimum))
        if count == minimum
    )

    candidates: set[Vector2D] = set()
    if x_minimum == minimum:
        candidates.update(
            (shift, 0) for shift in x_shifts if abs(shift) == x_minimum
        )
    if y_minimum == minimum:
        candidates.update(
            (0, shift) for shift in y_shifts if abs(shift) == y_minimum
        )

    witness = common_collapse_witness(left, right)
    if witness is None:
        raise AssertionError("nonempty common-collapse bounds lost their witness")
    pair = tuple(sorted((left.body_id, right.body_id)))
    return CollapseContact2D(
        pair=pair,
        x_count=x_count,
        y_count=y_count,
        shared_target_count=shared,
        x_signed_separations=x_shifts,
        y_signed_separations=y_shifts,
        minimum_axis_separation_steps=minimum,
        minimum_axes=axes,
        minimum_relative_corrections=tuple(sorted(candidates)),
        witness=witness,
    )
