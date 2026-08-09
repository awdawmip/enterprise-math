"""Exact multibody common-target repair for axis-aligned integer boxes.

Two complementary finite representations are kept explicit.

**Pair-first.**  Axis-aligned boxes have Helly number 2.  Build the conflict
graph whose edges are disjoint box pairs.  A deletion set restores one
whole-family common target iff it is a vertex cover of that conflict graph.

**Target-first.**  For any finite source-to-target relation, minimum source
deletions needed to obtain a whole-family common target are

    |X| - max_z c_z,

where ``c_z`` is target occupancy.  For boxes, a maximum-occupancy witness can
always be chosen at a point whose coordinate on each axis is one of the input
lower bounds: take the componentwise maximum lower bound of any maximum common
subfamily.  Thus a finite product of lower-bound coordinates is an exact target
candidate set independent of the ambient coordinate span.

The pair-first minimum vertex-cover oracle is exponential and used only as a
small reference.  The target-first candidate-grid oracle is polynomial in the
number of boxes for fixed dimension (naively O(N^(n+1))) and is retained as the
engineering counterpart of common-collapse incidence inversion.  Neither graph
vertex cover nor box stabbing/depth is claimed as new mathematics.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product

from .box_collapse import LabeledIntegerBox, pair_intersection_cardinality

ConflictEdge = tuple[int, int]
Point = tuple[int, ...]


@dataclass(frozen=True)
class BoxConflictRepair:
    labels: tuple[int, ...]
    conflict_edges: tuple[ConflictEdge, ...]
    minimum_deletions: int
    minimum_deletion_sets: tuple[frozenset[int], ...]


@dataclass(frozen=True)
class BoxTargetOccupancyRepair:
    labels: tuple[int, ...]
    maximum_occupancy: int
    minimum_deletions: int
    witness_points: tuple[Point, ...]
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


def box_contains_point(box: LabeledIntegerBox, point: Point) -> bool:
    """Whether one integer point lies in one inclusive box."""
    if len(point) != box.dimension:
        raise ValueError("point dimension must match box dimension")
    for coordinate in point:
        if isinstance(coordinate, bool) or not isinstance(coordinate, int):
            raise ValueError("point coordinates must be integers")
    return all(
        lo <= coordinate <= hi
        for coordinate, lo, hi in zip(point, box.lows, box.highs, strict=True)
    )


def target_first_common_target_repair(
    boxes: tuple[LabeledIntegerBox, ...] | list[LabeledIntegerBox],
) -> BoxTargetOccupancyRepair:
    """Return exact maximum occupancy and optimal deletion sets from target incidence.

    Candidate points are the Cartesian product of unique lower-bound coordinates
    on every axis.  At least one maximum-occupancy common-target witness occurs
    on this finite grid.
    """
    items = _validated_boxes(boxes)
    labels = frozenset(box.label for box in items)
    coordinates = tuple(
        tuple(sorted({box.lows[axis] for box in items}))
        for axis in range(items[0].dimension)
    )

    best_occupancy = -1
    witness_points: list[Point] = []
    deletion_sets: set[frozenset[int]] = set()
    for point in product(*coordinates):
        occupants = frozenset(
            box.label for box in items if box_contains_point(box, point)
        )
        occupancy = len(occupants)
        if occupancy > best_occupancy:
            best_occupancy = occupancy
            witness_points = [point]
            deletion_sets = {labels - occupants}
        elif occupancy == best_occupancy:
            witness_points.append(point)
            deletion_sets.add(labels - occupants)

    if best_occupancy <= 0:
        raise AssertionError("candidate lower-bound grid lost every box")
    minimum_deletions = len(items) - best_occupancy
    repairs = tuple(sorted(deletion_sets, key=lambda item: tuple(sorted(item))))
    if any(len(repair) != minimum_deletions for repair in repairs):
        raise AssertionError("maximum occupancy produced nonminimum deletion set")
    return BoxTargetOccupancyRepair(
        labels=tuple(sorted(labels)),
        maximum_occupancy=best_occupancy,
        minimum_deletions=minimum_deletions,
        witness_points=tuple(sorted(set(witness_points))),
        minimum_deletion_sets=repairs,
    )
