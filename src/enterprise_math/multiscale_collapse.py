"""E001.2 exact multi-scale collision from shared collapse domains.

A coarse cell is not itself a collision decision.  Instead, for each body and
cell the finite terminal collapse-target relation is classified as:

* EMPTY: no terminal target of the body lies in the cell;
* FULL: every terminal state in the cell is a collapse target of the body;
* PARTIAL: some but not all terminal states in the cell are targets.

If one body is FULL in a cell and another body is nonempty there, a shared
terminal target already exists and their collision is certified at that scale.
Pairs among PARTIAL bodies refine only through child cells that remain jointly
reachable.  At terminal cell size 1 every nonempty membership is FULL, so the
algorithm is exact and terminates without hidden real coordinates.

This is an inverted refinement tree over a relation, not a test that two object
centers have the same coarse label.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from itertools import combinations
from typing import Iterator

from .common_collapse import terminal_collapse_target_bounds
from .engineering_collision import Body2D, Pair, validate_refinement_schedule

EMPTY = "EMPTY"
FULL = "FULL"
PARTIAL = "PARTIAL"
CellRelation = str
CellKey2D = tuple[int, int]
ParentCell2D = tuple[int, int, int]


@dataclass(frozen=True)
class MultiscaleCollapseReport:
    """Exact collision output plus structural work done by the collapse tree."""

    body_count: int
    possible_pairs: int
    collision_pairs: tuple[Pair, ...]
    emitted_memberships: int
    visited_shared_cells: int
    decisions_by_cell_size: tuple[tuple[int, int], ...]


def _cell_bounds(cell_x: int, cell_y: int, cell_size: int) -> tuple[int, int, int, int]:
    x_lo = cell_x * cell_size
    y_lo = cell_y * cell_size
    return x_lo, x_lo + cell_size - 1, y_lo, y_lo + cell_size - 1


def collapse_cell_relation(
    body: Body2D, cell_x: int, cell_y: int, cell_size: int
) -> CellRelation:
    """Classify one aligned finite cell against a body's exact target domain."""
    if isinstance(cell_size, bool) or not isinstance(cell_size, int) or cell_size <= 0:
        raise ValueError("cell_size must be a positive integer")
    body_x_lo, body_x_hi, body_y_lo, body_y_hi = terminal_collapse_target_bounds(body)
    cell_x_lo, cell_x_hi, cell_y_lo, cell_y_hi = _cell_bounds(
        cell_x, cell_y, cell_size
    )
    if (
        cell_x_hi < body_x_lo
        or body_x_hi < cell_x_lo
        or cell_y_hi < body_y_lo
        or body_y_hi < cell_y_lo
    ):
        return EMPTY
    if (
        body_x_lo <= cell_x_lo <= cell_x_hi <= body_x_hi
        and body_y_lo <= cell_y_lo <= cell_y_hi <= body_y_hi
    ):
        return FULL
    return PARTIAL


def _intersecting_cells(
    body: Body2D,
    cell_size: int,
    parent: ParentCell2D | None = None,
) -> Iterator[CellKey2D]:
    body_x_lo, body_x_hi, body_y_lo, body_y_hi = terminal_collapse_target_bounds(body)
    cell_x_lo = body_x_lo // cell_size
    cell_x_hi = body_x_hi // cell_size
    cell_y_lo = body_y_lo // cell_size
    cell_y_hi = body_y_hi // cell_size

    if parent is not None:
        parent_x, parent_y, parent_size = parent
        parent_x_lo, parent_x_hi, parent_y_lo, parent_y_hi = _cell_bounds(
            parent_x, parent_y, parent_size
        )
        cell_x_lo = max(cell_x_lo, parent_x_lo // cell_size)
        cell_x_hi = min(cell_x_hi, parent_x_hi // cell_size)
        cell_y_lo = max(cell_y_lo, parent_y_lo // cell_size)
        cell_y_hi = min(cell_y_hi, parent_y_hi // cell_size)

    for cell_x in range(cell_x_lo, cell_x_hi + 1):
        for cell_y in range(cell_y_lo, cell_y_hi + 1):
            yield (cell_x, cell_y)


def multiscale_common_collapse(
    bodies: list[Body2D],
    cell_sizes: tuple[int, ...] | list[int],
) -> MultiscaleCollapseReport:
    """Find all exact collisions by refining only shared PARTIAL collapse cells."""
    schedule = validate_refinement_schedule(cell_sizes)
    ids = [body.body_id for body in bodies]
    if len(ids) != len(set(ids)):
        raise ValueError("body ids must be unique")
    by_id = {body.body_id: body for body in bodies}

    current: dict[CellKey2D, list[tuple[int, CellRelation]]] = defaultdict(list)
    emitted_memberships = 0
    first_size = schedule[0]
    for body in sorted(bodies):
        for cell_x, cell_y in _intersecting_cells(body, first_size):
            relation = collapse_cell_relation(body, cell_x, cell_y, first_size)
            if relation == EMPTY:
                raise AssertionError("intersecting-cell generator emitted an empty relation")
            current[(cell_x, cell_y)].append((body.body_id, relation))
            emitted_memberships += 1

    collisions: set[Pair] = set()
    decisions = {cell_size: 0 for cell_size in schedule}
    visited_shared_cells = 0

    for index, cell_size in enumerate(schedule):
        next_cells: dict[CellKey2D, list[tuple[int, CellRelation]]] = defaultdict(list)
        next_size = schedule[index + 1] if index + 1 < len(schedule) else None

        for (cell_x, cell_y), entries in current.items():
            if len(entries) < 2:
                continue
            visited_shared_cells += 1
            full_ids = [body_id for body_id, relation in entries if relation == FULL]
            partial_ids = [body_id for body_id, relation in entries if relation == PARTIAL]
            occupant_ids = [body_id for body_id, _relation in entries]

            # A FULL body's target set contains the whole cell.  Any other
            # occupant has at least one target in that cell, so the pair already
            # has a shared terminal witness and needs no further refinement here.
            for full_id in full_ids:
                for other_id in occupant_ids:
                    if full_id == other_id:
                        continue
                    pair = tuple(sorted((full_id, other_id)))
                    if pair not in collisions:
                        collisions.add(pair)
                        decisions[cell_size] += 1

            if next_size is None:
                if partial_ids:
                    raise AssertionError("singleton terminal cell remained partial")
                continue

            # Pairs involving a FULL member are already decided.  Only PARTIAL
            # members can still contain an undecided pair inside this cell.
            if len(partial_ids) < 2:
                continue
            parent = (cell_x, cell_y, cell_size)
            for body_id in partial_ids:
                body = by_id[body_id]
                for child_x, child_y in _intersecting_cells(body, next_size, parent):
                    relation = collapse_cell_relation(body, child_x, child_y, next_size)
                    if relation == EMPTY:
                        continue
                    next_cells[(child_x, child_y)].append((body_id, relation))
                    emitted_memberships += 1

        current = next_cells

    count = len(bodies)
    return MultiscaleCollapseReport(
        body_count=count,
        possible_pairs=count * (count - 1) // 2,
        collision_pairs=tuple(sorted(collisions)),
        emitted_memberships=emitted_memberships,
        visited_shared_cells=visited_shared_cells,
        decisions_by_cell_size=tuple((size, decisions[size]) for size in schedule),
    )
