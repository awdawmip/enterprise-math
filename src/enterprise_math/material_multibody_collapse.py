"""Multibody common-collapse geometry for the current E001 square-support family.

General admissible-support relations need not be Helly: pairwise common targets
can fail to imply one target shared by the whole family.  The current E001
terminal supports are more special.  Every ``Body2D`` target set is an
axis-aligned integer rectangle, and finite families of such boxes have Helly
number 2.

Hence, for this geometry only,

    every pair shares a terminal collapse target

is equivalent to

    all bodies share at least one terminal collapse target.

The pairwise Boolean clique certifies existence, but it does not recover the
common rectangle, deterministic witness, or common-target multiplicity.  Those
remain higher-information material/contact observables.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .common_collapse import (
    Target2D,
    TargetBounds2D,
    common_collapse_collision,
    terminal_collapse_target_bounds,
)
from .engineering_collision import Body2D


@dataclass(frozen=True)
class MultiBodyCollapse2D:
    """Exact terminal target intersection of a finite square-body family."""

    body_ids: tuple[int, ...]
    bounds: TargetBounds2D
    x_count: int
    y_count: int
    target_count: int
    witness: Target2D


def _validated_bodies(
    bodies: tuple[Body2D, ...] | list[Body2D],
) -> tuple[Body2D, ...]:
    items = tuple(bodies)
    if len(items) < 2:
        raise ValueError("multibody collapse requires at least two bodies")
    ids = [body.body_id for body in items]
    if len(ids) != len(set(ids)):
        raise ValueError("body ids must be unique")
    return tuple(sorted(items, key=lambda body: body.body_id))


def multibody_common_collapse_bounds(
    bodies: tuple[Body2D, ...] | list[Body2D],
) -> TargetBounds2D | None:
    """Return the exact intersection box of every body's terminal target set."""
    items = _validated_bodies(bodies)
    bounds = [terminal_collapse_target_bounds(body) for body in items]
    x_lo = max(bound[0] for bound in bounds)
    x_hi = min(bound[1] for bound in bounds)
    y_lo = max(bound[2] for bound in bounds)
    y_hi = min(bound[3] for bound in bounds)
    if x_lo > x_hi or y_lo > y_hi:
        return None
    return (x_lo, x_hi, y_lo, y_hi)


def pairwise_common_collapse_clique(
    bodies: tuple[Body2D, ...] | list[Body2D],
) -> bool:
    """Whether every body pair has a common terminal collapse target."""
    items = _validated_bodies(bodies)
    return all(
        common_collapse_collision(left, right)
        for left, right in combinations(items, 2)
    )


def box_helly_equivalence(
    bodies: tuple[Body2D, ...] | list[Body2D],
) -> bool:
    """Verify pairwise-clique iff whole-family intersection for E001 boxes."""
    items = _validated_bodies(bodies)
    pairwise = pairwise_common_collapse_clique(items)
    global_common = multibody_common_collapse_bounds(items) is not None
    return pairwise == global_common


def multibody_common_collapse_profile(
    bodies: tuple[Body2D, ...] | list[Body2D],
) -> MultiBodyCollapse2D | None:
    """Return common rectangle/multiplicity and assert the box-Helly specialization."""
    items = _validated_bodies(bodies)
    pairwise = pairwise_common_collapse_clique(items)
    bounds = multibody_common_collapse_bounds(items)
    if pairwise != (bounds is not None):
        raise AssertionError("axis-aligned E001 boxes violated their Helly-2 property")
    if bounds is None:
        return None
    x_lo, x_hi, y_lo, y_hi = bounds
    x_count = x_hi - x_lo + 1
    y_count = y_hi - y_lo + 1
    return MultiBodyCollapse2D(
        body_ids=tuple(body.body_id for body in items),
        bounds=bounds,
        x_count=x_count,
        y_count=y_count,
        target_count=x_count * y_count,
        witness=(x_lo, y_lo),
    )
