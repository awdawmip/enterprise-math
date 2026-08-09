"""E001.4 exact contact information retained by the common-collapse witness set.

A Boolean collision bit discards structure.  For the current axis-aligned E001
supports, the shared terminal target set is itself one finite integer rectangle.
Its axis counts give exact witness multiplicity and the minimum number of unit
axis translations needed to make the two target rectangles disjoint.

This is intentionally *not* a force, impulse, energy, or physical penetration
law.  It is a finite geometric contact certificate that can be preserved for a
later dynamics layer instead of collapsing immediately to True/False.
"""

from __future__ import annotations

from dataclasses import dataclass

from .common_collapse import common_collapse_bounds, common_collapse_witness
from .engineering_collision import Body2D, Pair


@dataclass(frozen=True)
class CollapseContact2D:
    """Exact finite geometry of one nonempty common-collapse target rectangle."""

    pair: Pair
    x_count: int
    y_count: int
    shared_target_count: int
    minimum_axis_separation_steps: int
    minimum_axes: tuple[str, ...]
    witness: tuple[int, int]


def collapse_contact_profile(left: Body2D, right: Body2D) -> CollapseContact2D | None:
    """Return exact shared-target contact data, or None when supports are separate."""
    if left.body_id == right.body_id:
        raise ValueError("contact pair must contain two distinct body ids")
    bounds = common_collapse_bounds(left, right)
    if bounds is None:
        return None
    x_lo, x_hi, y_lo, y_hi = bounds
    x_count = x_hi - x_lo + 1
    y_count = y_hi - y_lo + 1
    shared = x_count * y_count
    minimum = min(x_count, y_count)
    axes = tuple(
        axis
        for axis, count in (("x", x_count), ("y", y_count))
        if count == minimum
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
        minimum_axis_separation_steps=minimum,
        minimum_axes=axes,
        witness=witness,
    )
