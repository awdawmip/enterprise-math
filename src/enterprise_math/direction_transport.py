"""Canonical transport relation between intrinsic direction classes for P019.

A direction class at time t is a set of primitive incidences from A_t to A_{t+1}.
A direction class at time t+1 is a set of primitive incidences from A_{t+1} to
A_{t+2}.  The only transport relation used here is composability through the
shared middle section: (u,v) can continue through (v,w).

The result is generally a relation / integer matrix, not a function.  Split and
merge support is therefore treated as a structural obstruction to assigning a
canonical one-to-one identity to direction classes across time.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable

Vertex = Hashable
DirectedEdge = tuple[Vertex, Vertex]
Channel = tuple[DirectedEdge, ...]


def _channels(channels: Iterable[Iterable[DirectedEdge]]) -> tuple[Channel, ...]:
    result = tuple(tuple(dict.fromkeys(channel)) for channel in channels)
    if not result or any(not channel for channel in result):
        raise ValueError("direction channels must be nonempty")
    flattened = [edge for channel in result for edge in channel]
    if len(flattened) != len(set(flattened)):
        raise ValueError("direction channels at one time must be disjoint")
    return result


def composable_two_path_count(first: Iterable[DirectedEdge], second: Iterable[DirectedEdge]) -> int:
    """Count composable primitive two-paths from one direction class to another."""
    left = tuple(dict.fromkeys(first))
    right = tuple(dict.fromkeys(second))
    if not left or not right:
        raise ValueError("direction channels must be nonempty")
    return sum(1 for _, middle in left for source, _ in right if middle == source)


def direction_transport_matrix(
    current_channels: Iterable[Iterable[DirectedEdge]],
    next_channels: Iterable[Iterable[DirectedEdge]],
) -> tuple[tuple[int, ...], ...]:
    """Return the canonical integer composability matrix T_ij."""
    current = _channels(current_channels)
    nxt = _channels(next_channels)
    return tuple(
        tuple(composable_two_path_count(left, right) for right in nxt)
        for left in current
    )


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
    every row, and one nonzero entry in every column.  Positive weights may vary;
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
    if canonical_one_to_one_transport(tuple(tuple(int(v) for v in row) for row in support)) is not None:
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
