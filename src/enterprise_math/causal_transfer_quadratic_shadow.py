"""Second-order integer shadows of primitive transfer relations.

For a slot-transfer graph G, define edge dispersion

    P_G(x)=sum_{ {i,j} in E(G) } (x_i-x_j)^2.

Traditional graph theory writes this as x^T L_G x. Enterprise Math treats the
edge relation law as primary and the Laplacian/quadratic form as its second-order
observation shadow.

For the complete anonymous transfer graph K_N,

    P_K(x)=N*sum_i x_i^2-(sum_i x_i)^2.

On the exact-total kernel this becomes N*sum_i x_i^2. Polarization of P_G also
generates an exact integer bilinear shadow. On the complete zero-sum relation
space it is simply N times the slot dot product. A real inner-product completion,
if later used, is therefore downstream of the discrete relation aggregate rather
than primitive ontology.
"""

from __future__ import annotations

from .causal_transfer_graph_geometry import Edge, Vector, complete_transfer_edges


def _validate_state(state: Vector) -> None:
    if not state or any(isinstance(value, bool) or not isinstance(value, int) for value in state):
        raise ValueError("state must be a non-empty integer tuple")


def _subtract(left: Vector, right: Vector) -> Vector:
    if len(left) != len(right):
        raise ValueError("states must have equal coordinate counts")
    return tuple(a - b for a, b in zip(left, right))


def edge_dispersion(state: Vector, edges: tuple[Edge, ...]) -> int:
    _validate_state(state)
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


def polarized_edge_dispersion(left: Vector, right: Vector, edges: tuple[Edge, ...]) -> int:
    """Integer polarization B_G(x,y)=(P_G(x)+P_G(y)-P_G(x-y))/2."""
    _validate_state(left)
    _validate_state(right)
    if len(left) != len(right):
        raise ValueError("states must have equal coordinate counts")
    numerator = (
        edge_dispersion(left, edges)
        + edge_dispersion(right, edges)
        - edge_dispersion(_subtract(left, right), edges)
    )
    if numerator % 2 != 0:
        raise AssertionError("quadratic polarization numerator must be even")
    return numerator // 2


def complete_zero_sum_bilinear_shadow(left: Vector, right: Vector) -> int:
    if len(left) != len(right) or sum(left) != 0 or sum(right) != 0:
        raise ValueError("states must lie in the same complete zero-sum relation space")
    return polarized_edge_dispersion(left, right, complete_transfer_edges(len(left)))


def complete_zero_sum_bilinear_identity(left: Vector, right: Vector) -> bool:
    if len(left) != len(right) or sum(left) != 0 or sum(right) != 0:
        raise ValueError("states must lie in same zero-sum space")
    expected = len(left) * sum(a * b for a, b in zip(left, right))
    return complete_zero_sum_bilinear_shadow(left, right) == expected


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
