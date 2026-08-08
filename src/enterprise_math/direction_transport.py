"""Canonical transport relation between intrinsic direction classes for P019.

A direction class at time t is a set of primitive incidences from A_t to A_{t+1}.
A direction class at time t+1 is a set of primitive incidences from A_{t+1} to
A_{t+2}. The primitive transport datum is composability through the shared
middle section: (u,v) can continue through (v,w).

Two levels are deliberately separated:

1. witness transport: the actual composable incidence pairs, which retain the
   shared middle incidence needed for exact multi-step composition;
2. matrix transport: integer cardinalities of those witness sets, useful as a
   finite summary but not composition-complete in general.

Direction evolution is generally a relation rather than a function. Split,
merge, birth, and death therefore obstruct a canonical one-to-one direction
identity unless the support matrix is a permutation matrix.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable

Vertex = Hashable
DirectedEdge = tuple[Vertex, Vertex]
Channel = tuple[DirectedEdge, ...]
TwoPathWitness = tuple[DirectedEdge, DirectedEdge]
ThreePathWitness = tuple[DirectedEdge, DirectedEdge, DirectedEdge]


def _channels(channels: Iterable[Iterable[DirectedEdge]]) -> tuple[Channel, ...]:
    result = tuple(tuple(dict.fromkeys(channel)) for channel in channels)
    if not result or any(not channel for channel in result):
        raise ValueError("direction channels must be nonempty")
    flattened = [edge for channel in result for edge in channel]
    if len(flattened) != len(set(flattened)):
        raise ValueError("direction channels at one time must be disjoint")
    return result


def composable_two_path_witnesses(
    first: Iterable[DirectedEdge], second: Iterable[DirectedEdge]
) -> tuple[TwoPathWitness, ...]:
    """Return all primitive two-path witnesses between two direction classes."""
    left = tuple(dict.fromkeys(first))
    right = tuple(dict.fromkeys(second))
    if not left or not right:
        raise ValueError("direction channels must be nonempty")
    return tuple(
        (incoming, outgoing)
        for incoming in left
        for outgoing in right
        if incoming[1] == outgoing[0]
    )


def composable_two_path_count(first: Iterable[DirectedEdge], second: Iterable[DirectedEdge]) -> int:
    """Count composable primitive two-paths from one direction class to another."""
    return len(composable_two_path_witnesses(first, second))


def direction_transport_witnesses(
    current_channels: Iterable[Iterable[DirectedEdge]],
    next_channels: Iterable[Iterable[DirectedEdge]],
) -> tuple[tuple[tuple[TwoPathWitness, ...], ...], ...]:
    """Return witness sets W_ij for every pair of successive direction classes."""
    current = _channels(current_channels)
    nxt = _channels(next_channels)
    return tuple(
        tuple(composable_two_path_witnesses(left, right) for right in nxt)
        for left in current
    )


def direction_transport_matrix(
    current_channels: Iterable[Iterable[DirectedEdge]],
    next_channels: Iterable[Iterable[DirectedEdge]],
) -> tuple[tuple[int, ...], ...]:
    """Return the integer cardinality shadow T_ij=|W_ij|."""
    witnesses = direction_transport_witnesses(current_channels, next_channels)
    return tuple(tuple(len(cell) for cell in row) for row in witnesses)


def compose_two_path_witnesses(
    first: Iterable[TwoPathWitness], second: Iterable[TwoPathWitness]
) -> tuple[ThreePathWitness, ...]:
    """Join two witness relations on the exact shared middle incidence.

    ``(e0,e1)`` composes with ``(e1,e2)`` and only with a witness carrying the
    same primitive middle incidence ``e1``. This exact join is the information
    lost by multiplying only the cardinality matrices.
    """
    left = tuple(first)
    right = tuple(second)
    return tuple(
        (e0, e1, e2)
        for e0, e1 in left
        for middle, e2 in right
        if e1 == middle
    )


def exact_three_path_count(
    first: Iterable[DirectedEdge],
    second: Iterable[DirectedEdge],
    third: Iterable[DirectedEdge],
) -> int:
    """Count primitive three-edge chains without aggregating away witnesses."""
    first_witnesses = composable_two_path_witnesses(first, second)
    second_witnesses = composable_two_path_witnesses(second, third)
    return len(compose_two_path_witnesses(first_witnesses, second_witnesses))


def naive_matrix_product_entry(left_count: int, right_count: int) -> int:
    """Return the one-intermediate-class matrix product contribution.

    This helper exists only to expose the Stage-11 no-go: the product of two
    aggregated witness cardinalities generally overcounts exact three-paths.
    """
    if left_count < 0 or right_count < 0:
        raise ValueError("transport counts must be nonnegative")
    return left_count * right_count


def transport_support(matrix: Iterable[Iterable[int]]) -> tuple[tuple[bool, ...], ...]:
    """Return the zero/nonzero support of a transport matrix."""
    rows = tuple(tuple(row) for row in matrix)
    if not rows or not rows[0] or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError("transport matrix must be nonempty and rectangular")
    if any(value < 0 for row in rows for value in row):
        raise ValueError("transport counts must be nonnegative")
    return tuple(tuple(value > 0 for value in row) for row in rows)


def transport_branching_profile(matrix: Iterable[Iterable[int]]) -> tuple[int, ...]:
    """Number of next direction classes reached by each current class."""
    support = transport_support(matrix)
    return tuple(sum(row) for row in support)


def transport_merging_profile(matrix: Iterable[Iterable[int]]) -> tuple[int, ...]:
    """Number of current direction classes feeding each next class."""
    support = transport_support(matrix)
    width = len(support[0])
    return tuple(sum(1 for row in support if row[column]) for column in range(width))


def canonical_one_to_one_transport(matrix: Iterable[Iterable[int]]) -> tuple[int, ...] | None:
    """Return the unique support-defined class matching, or ``None``.

    A canonical one-to-one class identity exists from composability alone exactly
    when the support matrix is a permutation matrix: square, one nonzero entry in
    every row, and one nonzero entry in every column. Positive weights may vary;
    they encode path multiplicity rather than class identity.
    """
    support = transport_support(matrix)
    if len(support) != len(support[0]):
        return None
    row_counts = tuple(sum(row) for row in support)
    column_counts = tuple(
        sum(1 for row in support if row[column]) for column in range(len(support))
    )
    if any(value != 1 for value in row_counts + column_counts):
        return None
    return tuple(next(index for index, present in enumerate(row) if present) for row in support)


def transport_obstruction(matrix: Iterable[Iterable[int]]) -> str | None:
    """Classify why a one-to-one direction identity cannot be transported."""
    support = transport_support(matrix)
    integer_support = tuple(tuple(int(value) for value in row) for row in support)
    if canonical_one_to_one_transport(integer_support) is not None:
        return None
    row_counts = tuple(sum(row) for row in support)
    column_counts = tuple(
        sum(1 for row in support if row[column]) for column in range(len(support[0]))
    )
    if any(value == 0 for value in row_counts) or any(value == 0 for value in column_counts):
        return "birth_or_death"
    if any(value > 1 for value in row_counts) and any(value > 1 for value in column_counts):
        return "split_and_merge"
    if any(value > 1 for value in row_counts):
        return "split"
    if any(value > 1 for value in column_counts):
        return "merge"
    return "cardinality_mismatch"
