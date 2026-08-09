"""Box common-target existence under deletions as a finite conflict-graph problem.

Axis-aligned integer boxes have Helly number 2.  Therefore a remaining box
family has one whole-family common target iff every remaining pair intersects.
Create the conflict graph whose edges are disjoint box pairs.  For a deletion
set D:

    remaining boxes have a common target
      iff every conflict edge touches D
      iff D is a vertex cover of the conflict graph.

Thus the pairwise conflict graph is an exact sufficient state for the future
language “delete labeled boxes, then observe only common-target existence”.  It
is generally much smaller in semantic content than the extremal numeric state
needed to reconstruct the future common box or its target multiplicity.

Minimum deletion-to-common-target is exactly the graph vertex-cover number.  The
small exact oracle below is intentionally exponential and only supports finite
pressure tests; vertex cover is established graph theory, not a novelty claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .box_collapse import LabeledIntegerBox, pair_intersection_cardinality

ConflictEdge = tuple[int, int]


@dataclass(frozen=True)
class BoxConflictRepair:
    labels: tuple[int, ...]
    conflict_edges: tuple[ConflictEdge, ...]
    minimum_deletions: int
    minimum_deletion_sets: tuple[frozenset[int], ...]


def _validated_boxes(
    boxes: tuple[LabeledIntegerBox, ...] | list[LabeledIntegerBox],
) -> tuple[LabeledIntegerBox, ...]:
    items = tuple(sorted(tuple(boxes), key=lambda box: box.label))
    if len(items) < 2:
        raise ValueError("box conflict analysis requires at least two boxes")
    labels = [box.label for box in items]
    if len(labels) != len(set(labels)):
        raise ValueError("box labels must be unique")
    dimension = items[0].dimension
    if any(box.dimension != dimension for box in items):
        raise ValueError("all boxes must have the same dimension")
    return items


def box_conflict_edges(
    boxes: tuple[LabeledIntegerBox, ...] | list[LabeledIntegerBox],
) -> tuple[ConflictEdge, ...]:
    """Return every labeled pair whose integer boxes are disjoint."""
    items = _validated_boxes(boxes)
    return tuple(
        (left.label, right.label)
        for left, right in combinations(items, 2)
        if pair_intersection_cardinality(left, right) == 0
    )


def deletion_set_is_vertex_cover(
    conflict_edges: tuple[ConflictEdge, ...] | list[ConflictEdge],
    removed_labels: frozenset[int] | set[int] | tuple[int, ...],
) -> bool:
    """Whether every conflict edge loses at least one endpoint."""
    removed = frozenset(removed_labels)
    return all(left in removed or right in removed for left, right in conflict_edges)


def common_target_exists_after_deletions(
    boxes: tuple[LabeledIntegerBox, ...] | list[LabeledIntegerBox],
    removed_labels: frozenset[int] | set[int] | tuple[int, ...],
) -> bool:
    """Evaluate future common-target existence using only the conflict graph."""
    items = _validated_boxes(boxes)
    labels = {box.label for box in items}
    removed = frozenset(removed_labels)
    if not removed.issubset(labels):
        raise ValueError("removed labels must belong to the box family")
    if len(removed) == len(labels):
        raise ValueError("at least one box must remain")
    return deletion_set_is_vertex_cover(box_conflict_edges(items), removed)


def minimum_common_target_deletion_sets(
    boxes: tuple[LabeledIntegerBox, ...] | list[LabeledIntegerBox],
) -> BoxConflictRepair:
    """Return all minimum vertex covers / deletion repairs for one finite family."""
    items = _validated_boxes(boxes)
    labels = tuple(box.label for box in items)
    edges = box_conflict_edges(items)
    for count in range(len(labels)):
        repairs = tuple(
            frozenset(candidate)
            for candidate in combinations(labels, count)
            if deletion_set_is_vertex_cover(edges, candidate)
        )
        if repairs:
            return BoxConflictRepair(
                labels=labels,
                conflict_edges=edges,
                minimum_deletions=count,
                minimum_deletion_sets=repairs,
            )
    raise AssertionError("deleting all but one box must always cover every conflict edge")
