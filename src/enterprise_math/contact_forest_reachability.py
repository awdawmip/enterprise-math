"""Exact integer reachability for equal-weight forest contact Grams.

Let an oriented finite contact forest have incidence matrix ``B`` and equal body
weight, so the contact Gram is

    K = B^T B.

Because a forest has no cycle lattice, ``B`` has full column rank and every
reachable contact-score target has a unique integer impulse witness.  Integer
*reachability* is nevertheless not automatic.

For one tree component of size ``n``, a target vector ``c`` determines integer
vertex potentials ``s`` (unique up to an additive constant) by

    s_head - s_tail = c_e

on every oriented contact edge.  The residue

    Phi(c) = sum_v s_v mod n

is independent of the chosen root/constant.  The target has an integer solution
``K j = c`` exactly when ``Phi(c)=0``.  More generally, for forest component
sizes ``n_1,...,n_q`` the component residues give an explicit quotient map

    Z^E / K Z^E  ~=  direct_sum_alpha Z/n_alpha Z,

with size-one isolated components contributing no nontrivial factor.

When all component residues vanish, the module constructs the unique integer
impulse exactly: center each potential by its component mean and solve
``B j = centered_potential`` by leaf peeling.

This is the arbitrary-tree/forest extension of the earlier chain modulo-n
reachability obstruction.  Root-lattice discriminant groups and tree incidence
bases are standard prior mathematics; the project use is the contact-network
precision/reachability interface, especially after memory-driven topology
changes turn a cyclic contact graph into a forest.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Iterable, Sequence


Edge = tuple[int, int]
Vector = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _forest(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
) -> tuple[Edge, ...]:
    _require_int("num_vertices", num_vertices)
    if num_vertices <= 0:
        raise ValueError("num_vertices must be positive")
    normalized = []
    parent = list(range(num_vertices))

    def find(value: int) -> int:
        while parent[value] != value:
            parent[value] = parent[parent[value]]
            value = parent[value]
        return value

    for raw in tuple(edges):
        if len(raw) != 2:
            raise ValueError("each edge must have two endpoints")
        tail, head = raw
        _require_int("edge endpoint", tail)
        _require_int("edge endpoint", head)
        if not (0 <= tail < num_vertices and 0 <= head < num_vertices):
            raise ValueError("edge endpoint is outside the vertex set")
        if tail == head:
            raise ValueError("self loops are not supported")
        left = find(tail)
        right = find(head)
        if left == right:
            raise ValueError("contact graph must be a forest")
        parent[right] = left
        normalized.append((tail, head))
    return tuple(normalized)


def _vector(values: Iterable[int], length: int, *, name: str) -> Vector:
    result = tuple(values)
    if len(result) != length:
        raise ValueError(f"{name} must have length {length}")
    for value in result:
        _require_int(name, value)
    return result


def forest_incidence_matrix(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
) -> Matrix:
    graph = _forest(num_vertices, edges)
    rows = [[0] * len(graph) for _ in range(num_vertices)]
    for index, (tail, head) in enumerate(graph):
        rows[tail][index] = -1
        rows[head][index] = 1
    return tuple(tuple(row) for row in rows)


def equal_weight_forest_contact_gram(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
) -> Matrix:
    incidence = forest_incidence_matrix(num_vertices, edges)
    edge_count = len(incidence[0]) if incidence else 0
    return tuple(
        tuple(
            sum(
                incidence[body][left] * incidence[body][right]
                for body in range(num_vertices)
            )
            for right in range(edge_count)
        )
        for left in range(edge_count)
    )


def apply_integer_matrix(matrix: Matrix, vector: Iterable[int]) -> Vector:
    rows = tuple(tuple(row) for row in matrix)
    if not rows:
        if tuple(vector):
            raise ValueError("empty matrix requires empty vector")
        return ()
    width = len(rows[0])
    if any(len(row) != width for row in rows):
        raise ValueError("matrix must be rectangular")
    values = _vector(vector, width, name="vector")
    return tuple(
        sum(a * b for a, b in zip(row, values, strict=True))
        for row in rows
    )


@dataclass(frozen=True)
class ForestComponent:
    vertices: tuple[int, ...]
    edges: tuple[int, ...]

    @property
    def size(self) -> int:
        return len(self.vertices)


def forest_components(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
) -> tuple[ForestComponent, ...]:
    graph = _forest(num_vertices, edges)
    adjacency: list[list[tuple[int, int]]] = [
        [] for _ in range(num_vertices)
    ]
    for index, (tail, head) in enumerate(graph):
        adjacency[tail].append((head, index))
        adjacency[head].append((tail, index))

    seen: set[int] = set()
    result = []
    for start in range(num_vertices):
        if start in seen:
            continue
        vertices = []
        edge_set: set[int] = set()
        seen.add(start)
        queue: deque[int] = deque([start])
        while queue:
            current = queue.popleft()
            vertices.append(current)
            for neighbor, edge in adjacency[current]:
                edge_set.add(edge)
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        result.append(
            ForestComponent(
                tuple(sorted(vertices)),
                tuple(sorted(edge_set)),
            )
        )
    return tuple(result)


def integrated_vertex_potential(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
    target: Iterable[int],
) -> Vector:
    """Integrate edge differences, choosing potential zero at each component root."""
    graph = _forest(num_vertices, edges)
    values = _vector(target, len(graph), name="target")
    adjacency: list[list[tuple[int, int, int]]] = [
        [] for _ in range(num_vertices)
    ]
    for index, (tail, head) in enumerate(graph):
        adjacency[tail].append((head, index, 1))
        adjacency[head].append((tail, index, -1))

    potential: list[int | None] = [None] * num_vertices
    for root in range(num_vertices):
        if potential[root] is not None:
            continue
        potential[root] = 0
        queue: deque[int] = deque([root])
        while queue:
            current = queue.popleft()
            assert potential[current] is not None
            for neighbor, edge, sign in adjacency[current]:
                if potential[neighbor] is not None:
                    continue
                potential[neighbor] = potential[current] + sign * values[edge]
                queue.append(neighbor)
    return tuple(int(value) for value in potential)


def forest_target_residues(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
    target: Iterable[int],
) -> tuple[int, ...]:
    graph = _forest(num_vertices, edges)
    values = _vector(target, len(graph), name="target")
    potential = integrated_vertex_potential(
        num_vertices,
        graph,
        values,
    )
    return tuple(
        sum(potential[vertex] for vertex in component.vertices)
        % component.size
        for component in forest_components(num_vertices, graph)
        if component.edges
    )


def forest_target_is_reachable(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
    target: Iterable[int],
) -> bool:
    return all(
        residue == 0
        for residue in forest_target_residues(
            num_vertices,
            edges,
            target,
        )
    )


def forest_cokernel_component_factors(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
) -> tuple[int, ...]:
    """Cyclic direct-sum factors ``Z/n_component`` (trivial size-one omitted)."""
    graph = _forest(num_vertices, edges)
    return tuple(
        component.size
        for component in forest_components(num_vertices, graph)
        if component.edges
    )


def forest_contact_gram_determinant(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
) -> int:
    """Order of the finite cokernel, product of nontrivial component sizes."""
    result = 1
    for factor in forest_cokernel_component_factors(num_vertices, edges):
        result *= factor
    return result


def _solve_incidence_forest(
    num_vertices: int,
    graph: tuple[Edge, ...],
    body_vector: Vector,
) -> Vector:
    """Solve ``B j = body_vector`` by leaf peeling; component sums must vanish."""
    if len(body_vector) != num_vertices:
        raise ValueError("body_vector dimension mismatch")
    residual = list(body_vector)
    adjacency: list[list[tuple[int, int]]] = [
        [] for _ in range(num_vertices)
    ]
    for edge, (tail, head) in enumerate(graph):
        adjacency[tail].append((head, edge))
        adjacency[head].append((tail, edge))

    counts: list[int | None] = [None] * len(graph)
    alive = [True] * num_vertices
    degree = [len(row) for row in adjacency]
    queue: deque[int] = deque(
        vertex for vertex, value in enumerate(degree) if value <= 1
    )

    while queue:
        vertex = queue.popleft()
        if not alive[vertex]:
            continue
        neighbors = [
            pair for pair in adjacency[vertex] if alive[pair[0]]
        ]
        if len(neighbors) > 1:
            continue
        if not neighbors:
            if residual[vertex] != 0:
                raise ValueError("body_vector does not sum to zero on a component")
            alive[vertex] = False
            continue

        other, edge = neighbors[0]
        tail, _ = graph[edge]
        sign_here = -1 if vertex == tail else 1
        count = sign_here * residual[vertex]
        counts[edge] = count
        sign_other = -1 if other == tail else 1
        residual[vertex] -= sign_here * count
        residual[other] -= sign_other * count
        alive[vertex] = False
        degree[other] -= 1
        if degree[other] <= 1:
            queue.append(other)

    if any(residual) or any(value is None for value in counts):
        raise ValueError("forest incidence solve did not close")
    return tuple(int(value) for value in counts)


def solve_forest_contact_target(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
    target: Iterable[int],
) -> Vector | None:
    """Return the unique integer ``j`` solving ``B^T B j=target``, else None."""
    graph = _forest(num_vertices, edges)
    values = _vector(target, len(graph), name="target")
    potential = integrated_vertex_potential(
        num_vertices,
        graph,
        values,
    )
    centered = list(potential)
    for component in forest_components(num_vertices, graph):
        total = sum(potential[vertex] for vertex in component.vertices)
        if total % component.size:
            return None
        mean = total // component.size
        for vertex in component.vertices:
            centered[vertex] -= mean

    impulse = _solve_incidence_forest(
        num_vertices,
        graph,
        tuple(centered),
    )
    gram = equal_weight_forest_contact_gram(num_vertices, graph)
    if apply_integer_matrix(gram, impulse) != values:
        raise AssertionError("constructed forest impulse does not hit target")
    return impulse


@dataclass(frozen=True)
class ForestReachabilityReport:
    component_sizes: tuple[int, ...]
    cokernel_component_factors: tuple[int, ...]
    determinant: int
    residues: tuple[int, ...]
    reachable: bool
    unique_integer_impulse: Vector | None


def forest_reachability_report(
    num_vertices: int,
    edges: Iterable[Sequence[int]],
    target: Iterable[int],
) -> ForestReachabilityReport:
    graph = _forest(num_vertices, edges)
    values = _vector(target, len(graph), name="target")
    components = forest_components(num_vertices, graph)
    residues = forest_target_residues(
        num_vertices,
        graph,
        values,
    )
    impulse = solve_forest_contact_target(
        num_vertices,
        graph,
        values,
    )
    return ForestReachabilityReport(
        component_sizes=tuple(component.size for component in components),
        cokernel_component_factors=forest_cokernel_component_factors(
            num_vertices,
            graph,
        ),
        determinant=forest_contact_gram_determinant(
            num_vertices,
            graph,
        ),
        residues=residues,
        reachable=impulse is not None,
        unique_integer_impulse=impulse,
    )
