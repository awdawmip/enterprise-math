"""Recover a simply-laced Gram shadow and its rank from primitive relations alone.

For the A/D/E primitive-direction graphs studied in Enterprise Math, every
primitive direction has one unique direction at graph distance three.  That
purely graph-theoretic antipode, together with primitive adjacency, determines
the normalized pair-grade matrix

    2  on the diagonal,
    1  on primitive-adjacent pairs,
   -1  when u is adjacent to antipode(v),
   -2  on antipodal pairs,
    0  otherwise.

No original coordinate vectors are used by the reconstruction.  On simply-laced
A/D/E systems this matrix is exactly `2 <u,v> / <u,u>` and therefore its exact
rational rank recovers the root-system dimension.  The theorem must not be
silently extended to arbitrary minimal-vector shells; laminated/Kappa systems can
require deeper pair witness structure before a Gram observation becomes a
causal shadow.
"""

from __future__ import annotations

from collections import deque
from fractions import Fraction

from .causal_primitive_link_profile import Adjacency, Vector


def graph_distances(adjacency: Adjacency, source: Vector) -> dict[Vector, int]:
    if source not in adjacency:
        raise ValueError("source must belong to adjacency")
    distance = {source: 0}
    queue = deque([source])
    while queue:
        current = queue.popleft()
        for nxt in adjacency[current]:
            if nxt in distance:
                continue
            distance[nxt] = distance[current] + 1
            queue.append(nxt)
    return distance


def graph_antipodes(adjacency: Adjacency) -> dict[Vector, Vector]:
    """Unique distance-three antipode map, raising outside this graph regime."""
    antipodes = {}
    for source in adjacency:
        distance = graph_distances(adjacency, source)
        candidates = tuple(vertex for vertex, depth in distance.items() if depth == 3)
        if len(candidates) != 1:
            raise ValueError("each primitive direction must have one unique distance-three antipode")
        antipodes[source] = candidates[0]
    if any(antipodes[antipodes[source]] != source for source in adjacency):
        raise ValueError("distance-three antipode map must be an involution")
    return antipodes


def causal_simply_laced_gram(adjacency: Adjacency) -> tuple[tuple[int, ...], ...]:
    """Normalized Gram shadow built only from the unlabeled primitive graph."""
    vertices = tuple(adjacency)
    antipode = graph_antipodes(adjacency)
    rows = []
    for left in vertices:
        row = []
        for right in vertices:
            if left == right:
                value = 2
            elif left == antipode[right]:
                value = -2
            elif right in adjacency[left]:
                value = 1
            elif antipode[right] in adjacency[left]:
                value = -1
            else:
                value = 0
            row.append(value)
        rows.append(tuple(row))
    matrix = tuple(rows)
    if any(matrix[i][j] != matrix[j][i] for i in range(len(vertices)) for j in range(len(vertices))):
        raise ValueError("causal pair rules did not produce a symmetric Gram shadow")
    return matrix


def rational_matrix_rank(matrix: tuple[tuple[int, ...], ...]) -> int:
    if not matrix:
        return 0
    width = len(matrix[0])
    if any(len(row) != width for row in matrix):
        raise ValueError("matrix must be rectangular")
    rows = [[Fraction(value, 1) for value in row] for row in matrix]
    pivot_row = 0
    for column in range(width):
        pivot = next((row for row in range(pivot_row, len(rows)) if rows[row][column] != 0), None)
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        pivot_value = rows[pivot_row][column]
        rows[pivot_row] = [value / pivot_value for value in rows[pivot_row]]
        for row in range(len(rows)):
            if row == pivot_row or rows[row][column] == 0:
                continue
            factor = rows[row][column]
            rows[row] = [
                left - factor * right
                for left, right in zip(rows[row], rows[pivot_row])
            ]
        pivot_row += 1
        if pivot_row == len(rows):
            break
    return pivot_row


def causal_graph_dimension(adjacency: Adjacency) -> int:
    return rational_matrix_rank(causal_simply_laced_gram(adjacency))
