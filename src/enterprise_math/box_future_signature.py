"""Componentwise exact future signatures for integer-box bounds under deletions.

The uniform ``h+1`` ranked-facet certificate in ``box_collapse`` is simple and
worst-case sharp, but ties can make it larger than necessary for a concrete
state.  This module compiles the coarsest scalar max/min deletion signature for
each of the ``2n`` box bounds:

* lower bound on axis j -> maximum future signature;
* upper bound on axis j -> minimum future signature.

The product of those signatures reconstructs the exact common-box bounds after
any declared deletion set of size at most h.  It is called *componentwise exact
sufficient*, not globally coarsest for the joint vector output, because shared
box labels can induce cross-axis correlations that a product representation may
still duplicate.
"""

from __future__ import annotations

from dataclasses import dataclass

from .box_collapse import LabeledIntegerBox
from .extremum_future_signature import (
    ExtremumFutureSignature,
    compile_extremum_future_signature,
    extremum_after_deletions,
)


@dataclass(frozen=True)
class BoxDeletionFutureSignature:
    labels: tuple[int, ...]
    dimension: int
    deletion_horizon: int
    lower_signatures: tuple[ExtremumFutureSignature, ...]
    upper_signatures: tuple[ExtremumFutureSignature, ...]


def _validate_boxes(
    boxes: tuple[LabeledIntegerBox, ...] | list[LabeledIntegerBox],
    deletion_horizon: int,
) -> tuple[LabeledIntegerBox, ...]:
    items = tuple(sorted(tuple(boxes), key=lambda box: box.label))
    if len(items) < 2:
        raise ValueError("box family requires at least two boxes")
    labels = [box.label for box in items]
    if len(labels) != len(set(labels)):
        raise ValueError("box labels must be unique")
    dimension = items[0].dimension
    if any(box.dimension != dimension for box in items):
        raise ValueError("all boxes must have the same dimension")
    if (
        isinstance(deletion_horizon, bool)
        or not isinstance(deletion_horizon, int)
        or deletion_horizon < 0
        or deletion_horizon >= len(items)
    ):
        raise ValueError("deletion_horizon must be in 0..len(boxes)-1")
    return items


def compile_box_deletion_future_signature(
    boxes: tuple[LabeledIntegerBox, ...] | list[LabeledIntegerBox],
    deletion_horizon: int,
) -> BoxDeletionFutureSignature:
    """Compile exact per-bound future signatures for <=h labeled deletions."""
    items = _validate_boxes(boxes, deletion_horizon)
    dimension = items[0].dimension
    lower = tuple(
        compile_extremum_future_signature(
            {box.label: box.lows[axis] for box in items},
            deletion_horizon,
            maximize=True,
        )
        for axis in range(dimension)
    )
    upper = tuple(
        compile_extremum_future_signature(
            {box.label: box.highs[axis] for box in items},
            deletion_horizon,
            maximize=False,
        )
        for axis in range(dimension)
    )
    return BoxDeletionFutureSignature(
        labels=tuple(box.label for box in items),
        dimension=dimension,
        deletion_horizon=deletion_horizon,
        lower_signatures=lower,
        upper_signatures=upper,
    )


def box_bounds_after_deletions(
    signature: BoxDeletionFutureSignature,
    removed_labels: frozenset[int] | set[int] | tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Recover exact max-lower/min-upper vectors after an allowed deletion set."""
    removed = frozenset(removed_labels)
    if not removed.issubset(signature.labels):
        raise ValueError("removed labels must belong to the certified box family")
    if len(removed) > signature.deletion_horizon:
        raise ValueError("removal set exceeds deletion horizon")
    lows = tuple(
        extremum_after_deletions(item, removed)
        for item in signature.lower_signatures
    )
    highs = tuple(
        extremum_after_deletions(item, removed)
        for item in signature.upper_signatures
    )
    return lows, highs


def box_intersection_exists_after_deletions(
    signature: BoxDeletionFutureSignature,
    removed_labels: frozenset[int] | set[int] | tuple[int, ...],
) -> bool:
    """Evaluate future common-target existence from the compact bound signature."""
    lows, highs = box_bounds_after_deletions(signature, removed_labels)
    return all(lo <= hi for lo, hi in zip(lows, highs, strict=True))
