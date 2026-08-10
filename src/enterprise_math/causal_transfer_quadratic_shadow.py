"""Second-order integer shadows of primitive transfer relations.

For a slot-transfer graph G, define edge dispersion

    P_G(x)=sum_{ {i,j} in E(G) } (x_i-x_j)^2.

Traditional graph theory writes this as x^T L_G x. Enterprise Math treats the
edge relation law as primary and the Laplacian/quadratic form as its second-order
observation shadow.

For the complete anonymous transfer graph K_N,

    P_K(x)=N*sum_i x_i^2-(sum_i x_i)^2.

On the exact-total kernel this becomes N*sum_i x_i^2. Polarization generates an
exact integer bilinear shadow. Moreover, any pair-local quadratic observation
with weights invariant under every slot permutation must assign one common weight
to every unordered pair, so this complete dispersion is unique up to scale inside
that observation class.
"""

from __future__ import annotations

from itertools import combinations

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


def weighted_pair_dispersion(state: Vector, pair_weights: dict[Edge, int]) -> int:
    _validate_state(state)
    total = 0
    for (left, right), weight in pair_weights.items():
        if left == right or any(index < 0 or index >= len(state) for index in (left, right)):
            raise ValueError("weighted pair endpoint outside state")
        if isinstance(weight, bool) or not isinstance(weight, int):
            raise ValueError("pair weights must be integers")
        total += weight * (state[left] - state[right]) ** 2
    return total


def pair_weights_are_fully_anonymous(slot_count: int, pair_weights: dict[Edge, int]) -> bool:
    """Full S_N invariance for pair-local weights is equivalent to one common weight."""
    expected_pairs = set(combinations(range(slot_count), 2))
    normalized = {tuple(sorted(edge)): weight for edge, weight in pair_weights.items()}
    return set(normalized) == expected_pairs and len(set(normalized.values())) == 1


def anonymous_pair_weight(slot_count: int, pair_weights: dict[Edge, int]) -> int:
    if not pair_weights_are_fully_anonymous(slot_count, pair_weights):
        raise ValueError("weights are not a complete slot-anonymous pair field")
    return next(iter(pair_weights.values()))


def anonymous_quadratic_shadow_identity(state: Vector, pair_weight: int) -> bool:
    """For equal pair weight w, Q=w*(N sum x_i^2-(sum x_i)^2)."""
    if isinstance(pair_weight, bool) or not isinstance(pair_weight, int):
        raise ValueError("pair_weight must be an integer")
    weights = {edge: pair_weight for edge in complete_transfer_edges(len(state))}
    left = weighted_pair_dispersion(state, weights)
    right = pair_weight * (
        len(state) * sum(value * value for value in state) - sum(state) ** 2
    )
    return left == right


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
