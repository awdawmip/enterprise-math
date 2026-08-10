"""Second-order integer shadows of primitive transfer relations.

For a slot-transfer graph G, define edge dispersion

    P_G(x)=sum_{ {i,j} in E(G) } (x_i-x_j)^2.

Traditional graph theory writes this as x^T L_G x.  Enterprise Math treats the
edge relation law as primary and the Laplacian/quadratic form as its second-order
observation shadow.

For the complete anonymous transfer graph K_N,

    P_K(x)=N*sum_i x_i^2-(sum_i x_i)^2.

On the exact-total kernel this becomes N*sum_i x_i^2, recovering the P019 pair
dispersion relation for A_(N-1) without requiring Euclidean distance as ontology.
"""

from __future__ import annotations

from .causal_transfer_graph_geometry import Edge, Vector, complete_transfer_edges


def edge_dispersion(state: Vector, edges: tuple[Edge, ...]) -> int:
    if not state or any(isinstance(value, bool) or not isinstance(value, int) for value in state):
        raise ValueError("state must be a non-empty integer tuple")
    total = 0
    seen = set()
    for left, right in edges:
        if left == right or any(index < 0 or index >= len(state) for index in (left, right)):
            raise ValueError("edge endpoint outside state")
        edge = tuple(sorted((left, right)))
        if edge in seen:
            continue
        seen.add(edge)
        total += (state[left] - state[right]) ** 2
    return total


def complete_edge_dispersion(state: Vector) -> int:
    return edge_dispersion(state, complete_transfer_edges(len(state)))


def complete_dispersion_identity(state: Vector) -> bool:
    n = len(state)
    left = complete_edge_dispersion(state)
    right = n * sum(value * value for value in state) - sum(state) ** 2
    return left == right


def complete_zero_sum_quadratic_shadow(state: Vector) -> int:
    if sum(state) != 0:
        raise ValueError("state must lie in exact total-charge kernel")
    dispersion = complete_edge_dispersion(state)
    n = len(state)
    if dispersion % n != 0:
        raise AssertionError("complete zero-sum dispersion must be divisible by slot count")
    return dispersion // n


def primitive_second_moment_matrix(slot_count: int, edges: tuple[Edge, ...]) -> tuple[tuple[int, ...], ...]:
    """Sum b_e b_e^T over one orientation of each undirected primitive relation."""
    matrix = [[0] * slot_count for _ in range(slot_count)]
    seen = set()
    for left, right in edges:
        edge = tuple(sorted((left, right)))
        if edge in seen:
            continue
        seen.add(edge)
        vector = [0] * slot_count
        vector[left] = 1
        vector[right] = -1
        for row in range(slot_count):
            for column in range(slot_count):
                matrix[row][column] += vector[row] * vector[column]
    return tuple(tuple(row) for row in matrix)


def quadratic_from_second_moment(state: Vector, matrix: tuple[tuple[int, ...], ...]) -> int:
    if len(matrix) != len(state) or any(len(row) != len(state) for row in matrix):
        raise ValueError("matrix and state dimensions must match")
    return sum(
        state[row] * matrix[row][column] * state[column]
        for row in range(len(state))
        for column in range(len(state))
    )


def second_moment_matches_edge_dispersion(state: Vector, edges: tuple[Edge, ...]) -> bool:
    matrix = primitive_second_moment_matrix(len(state), edges)
    return quadratic_from_second_moment(state, matrix) == edge_dispersion(state, edges)
