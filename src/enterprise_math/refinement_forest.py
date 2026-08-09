"""Integer lattice-index tools for P019 Refinement Forest coordinates.

For blocks of capacities m_i, choose a spanning tree and store the weighted
edge relations Z_uv=m_v*c_u-m_u*c_v together with the grand total C=sum c_i.
The augmented integer coordinate map has determinant

    M * product_i m_i**(deg(i)-1),  M=sum_i m_i,

for at least two blocks.  The fixed-total relation-tree chart has the same
index in its ambient Z^(r-1) relation-coordinate space.
"""

from __future__ import annotations

from itertools import product


def _require_capacities(capacities: tuple[int, ...]) -> None:
    if not isinstance(capacities, tuple) or not capacities:
        raise ValueError("capacities must be a non-empty tuple")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in capacities
    ):
        raise ValueError("capacities must be positive integers")


def _tree_edges(parents: tuple[int, ...], root: int) -> tuple[tuple[int, int], ...]:
    if not isinstance(parents, tuple) or not parents:
        raise ValueError("parents must be a non-empty tuple")
    count = len(parents)
    if isinstance(root, bool) or not isinstance(root, int) or not 0 <= root < count:
        raise ValueError("root must index parents")
    if parents[root] != -1:
        raise ValueError("root parent must be -1")

    children = [[] for _ in range(count)]
    edges = []
    for vertex, parent in enumerate(parents):
        if vertex == root:
            continue
        if (
            isinstance(parent, bool)
            or not isinstance(parent, int)
            or not 0 <= parent < count
        ):
            raise ValueError("every non-root parent must be a valid vertex")
        children[parent].append(vertex)
        edges.append((parent, vertex))

    seen: set[int] = set()

    def visit(vertex: int) -> None:
        if vertex in seen:
            raise ValueError("parents must define an acyclic rooted tree")
        seen.add(vertex)
        for child in children[vertex]:
            visit(child)

    visit(root)
    if len(seen) != count:
        raise ValueError("parents must define one connected rooted tree")
    return tuple(edges)


def relation_tree_degrees(parents: tuple[int, ...], root: int) -> tuple[int, ...]:
    """Return undirected degrees of the rooted relation tree."""
    edges = _tree_edges(parents, root)
    degrees = [0] * len(parents)
    for left, right in edges:
        degrees[left] += 1
        degrees[right] += 1
    return tuple(degrees)


def refinement_tree_index_formula(
    capacities: tuple[int, ...], parents: tuple[int, ...], root: int
) -> int:
    """Closed index formula for fixed-total weighted relation-tree coordinates."""
    _require_capacities(capacities)
    if len(capacities) != len(parents):
        raise ValueError("capacities and parents must have the same size")
    if len(capacities) == 1:
        _tree_edges(parents, root)
        return 1
    degrees = relation_tree_degrees(parents, root)
    result = sum(capacities)
    for capacity, degree in zip(capacities, degrees):
        result *= capacity ** (degree - 1)
    return result


def augmented_relation_tree_matrix(
    capacities: tuple[int, ...], parents: tuple[int, ...], root: int
) -> tuple[tuple[int, ...], ...]:
    """Matrix c -> (grand_total, weighted tree-edge relations)."""
    _require_capacities(capacities)
    if len(capacities) != len(parents):
        raise ValueError("capacities and parents must have the same size")
    edges = _tree_edges(parents, root)
    count = len(capacities)
    rows = [[1] * count]
    for parent, child in edges:
        row = [0] * count
        row[parent] = capacities[child]
        row[child] = -capacities[parent]
        rows.append(row)
    return tuple(tuple(row) for row in rows)


def _determinant_bareiss(matrix: tuple[tuple[int, ...], ...]) -> int:
    """Exact fraction-free determinant."""
    if not matrix:
        return 1
    size = len(matrix)
    if any(len(row) != size for row in matrix):
        raise ValueError("matrix must be square")
    data = [list(row) for row in matrix]
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        if data[pivot_index][pivot_index] == 0:
            swap = next(
                (
                    row
                    for row in range(pivot_index + 1, size)
                    if data[row][pivot_index] != 0
                ),
                None,
            )
            if swap is None:
                return 0
            data[pivot_index], data[swap] = data[swap], data[pivot_index]
            sign = -sign
        pivot = data[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    data[row][column] * pivot
                    - data[row][pivot_index] * data[pivot_index][column]
                )
                if numerator % previous != 0:
                    raise AssertionError("Bareiss exact division failed")
                data[row][column] = numerator // previous
        previous = pivot
    return sign * data[-1][-1]


def refinement_tree_chart_determinant(
    capacities: tuple[int, ...], parents: tuple[int, ...], root: int
) -> int:
    """Absolute determinant of the augmented total+edge-relation chart."""
    return abs(_determinant_bareiss(augmented_relation_tree_matrix(capacities, parents, root)))


def refinement_tree_index_identity(
    capacities: tuple[int, ...], parents: tuple[int, ...], root: int
) -> tuple[int, int]:
    """Return direct determinant and the closed index formula."""
    return (
        refinement_tree_chart_determinant(capacities, parents, root),
        refinement_tree_index_formula(capacities, parents, root),
    )


def star_parents(block_count: int, center: int) -> tuple[int, ...]:
    """Return a star tree rooted at its center."""
    if isinstance(block_count, bool) or not isinstance(block_count, int) or block_count <= 0:
        raise ValueError("block_count must be a positive integer")
    if isinstance(center, bool) or not isinstance(center, int) or not 0 <= center < block_count:
        raise ValueError("center must index the blocks")
    return tuple(-1 if vertex == center else center for vertex in range(block_count))


def minimum_refinement_tree_index(capacities: tuple[int, ...]) -> int:
    """Minimum index over all spanning trees: star at a minimum-capacity vertex."""
    _require_capacities(capacities)
    count = len(capacities)
    if count == 1:
        return 1
    return sum(capacities) * min(capacities) ** (count - 2)


def maximum_refinement_tree_index(capacities: tuple[int, ...]) -> int:
    """Maximum index over all spanning trees: star at a maximum-capacity vertex."""
    _require_capacities(capacities)
    count = len(capacities)
    if count == 1:
        return 1
    return sum(capacities) * max(capacities) ** (count - 2)


def prufer_degrees(sequence: tuple[int, ...], vertex_count: int) -> tuple[int, ...]:
    """Degree sequence of the labeled tree encoded by a Prüfer sequence."""
    if isinstance(vertex_count, bool) or not isinstance(vertex_count, int) or vertex_count < 2:
        raise ValueError("vertex_count must be at least two")
    if not isinstance(sequence, tuple) or len(sequence) != vertex_count - 2:
        raise ValueError("Prüfer sequence must have length vertex_count-2")
    if any(
        isinstance(vertex, bool)
        or not isinstance(vertex, int)
        or not 0 <= vertex < vertex_count
        for vertex in sequence
    ):
        raise ValueError("Prüfer entries must be valid vertex indices")
    degrees = [1] * vertex_count
    for vertex in sequence:
        degrees[vertex] += 1
    return tuple(degrees)


def all_prufer_degree_sequences(vertex_count: int) -> tuple[tuple[int, ...], ...]:
    """Enumerate degree sequences with multiplicity over all labeled Prüfer trees."""
    if isinstance(vertex_count, bool) or not isinstance(vertex_count, int) or vertex_count < 2:
        raise ValueError("vertex_count must be at least two")
    return tuple(
        prufer_degrees(sequence, vertex_count)
        for sequence in product(range(vertex_count), repeat=vertex_count - 2)
    )
