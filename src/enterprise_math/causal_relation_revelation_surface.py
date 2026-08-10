"""Two-axis causal revelation profile for primitive relation geometry.

For compatible flags of size r and future lookahead h, let

    T(r,h) = number of distinct continuation-tree signature types.

The table separates primitive-direction homogeneity (r=1) from pair, triangle,
and higher relation-context fragmentation.  It is intentionally not collapsed to
a scalar isotropy score.  Relation capacity (number of flags/states) and causal
fragmentation (number of future types) are retained as separate coordinates.
"""

from __future__ import annotations

from dataclasses import dataclass

from .causal_primitive_link_profile import (
    Adjacency,
    cliques_of_size,
    flag_future_signature_histogram,
)


@dataclass(frozen=True)
class RelationRevelationCell:
    flag_size: int
    lookahead: int
    flag_count: int
    continuation_type_count: int
    type_multiplicities: tuple[int, ...]


def relation_revelation_cell(
    adjacency: Adjacency,
    flag_size: int,
    lookahead: int,
) -> RelationRevelationCell:
    flags = cliques_of_size(adjacency, flag_size)
    histogram = flag_future_signature_histogram(adjacency, flag_size, lookahead)
    return RelationRevelationCell(
        flag_size=flag_size,
        lookahead=lookahead,
        flag_count=len(flags),
        continuation_type_count=len(histogram),
        type_multiplicities=tuple(sorted(histogram.values(), reverse=True)),
    )


def relation_revelation_surface(
    adjacency: Adjacency,
    maximum_flag_size: int,
    maximum_lookahead: int,
) -> tuple[RelationRevelationCell, ...]:
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 1
        for value in (maximum_flag_size, maximum_lookahead)
    ):
        raise ValueError("maximum flag size and lookahead must be positive integers")
    cells = []
    for flag_size in range(1, maximum_flag_size + 1):
        if not cliques_of_size(adjacency, flag_size):
            break
        for lookahead in range(1, maximum_lookahead + 1):
            cells.append(relation_revelation_cell(adjacency, flag_size, lookahead))
    return tuple(cells)


def type_count_matrix(
    surface: tuple[RelationRevelationCell, ...],
) -> dict[tuple[int, int], int]:
    return {
        (cell.flag_size, cell.lookahead): cell.continuation_type_count
        for cell in surface
    }


def causal_fragmentation_dominates(
    left: tuple[RelationRevelationCell, ...],
    right: tuple[RelationRevelationCell, ...],
) -> bool:
    """Return True iff left has no more continuation types on every shared cell.

    This is only the fragmentation coordinate.  It deliberately ignores relation
    capacity/flag counts, so it is not a universal geometry ordering.
    """
    left_map = type_count_matrix(left)
    right_map = type_count_matrix(right)
    shared = set(left_map).intersection(right_map)
    if not shared:
        raise ValueError("surfaces must share at least one (flag_size,lookahead) cell")
    return all(left_map[key] <= right_map[key] for key in shared)
