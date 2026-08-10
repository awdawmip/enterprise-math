"""Directional ball boundaries of conservative transfer graphs lower by edge contraction.

For an undirected connected slot-transfer graph G, primitive moves are oriented
incidence vectors +/- (e_i-e_j). The word ball B_G(r) is finite in the zero-sum
relation lattice. Fix an oriented edge e with primitive vector b_e. The positive
directional cut consists of x in B_G(r) with x+b_e outside the ball.

Contracting the two endpoint slots gives G/e and a lattice projection pi_e. The
research theorem implemented and exhaustively pressure-tested here is that pi_e
restricts to a bijection

    C_(G,e)(r)  <->  B_(G/e)(r).

Summing over both orientations of every graph edge gives the exact relation
boundary identity

    |partial_rel B_G(r)| = 2 * sum_{e in E(G)} |B_(G/e)(r)|.

When all edge contractions are isomorphic this becomes one local direction factor
times a single lower-rank ball count.

A proof route uses the integer min-cost-flow representation of the word norm.
The quotient norm along pi_e is exactly the contracted-graph word norm, while the
norm restricted to each integer fiber x+Z*b_e is discrete convex; hence every
nonempty radius-r fiber is an integer interval with one positive endpoint. Total
unimodularity / min-cost-flow duality is a mature proof tool, not foundational
ontology.
"""

from __future__ import annotations

from collections import deque

from .causal_transfer_graph_geometry import Edge, Vector, primitive_transfer_moves


def _add(left: Vector, right: Vector) -> Vector:
    return tuple(a + b for a, b in zip(left, right))


def _edge_set(slot_count: int, edges: tuple[Edge, ...]) -> frozenset[Edge]:
    normalized = set()
    for left, right in edges:
        if left == right or any(index < 0 or index >= slot_count for index in (left, right)):
            raise ValueError("edges must contain distinct valid slots")
        normalized.add(tuple(sorted((left, right))))
    return frozenset(normalized)


def _require_graph_edge(slot_count: int, edges: tuple[Edge, ...], edge: Edge) -> None:
    if tuple(sorted(edge)) not in _edge_set(slot_count, edges):
        raise ValueError("declared oriented edge must belong to the transfer graph")


def word_ball(slot_count: int, edges: tuple[Edge, ...], radius: int) -> frozenset[Vector]:
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    origin = (0,) * slot_count
    moves = primitive_transfer_moves(slot_count, edges)
    distance = {origin: 0}
    queue = deque([origin])
    while queue:
        current = queue.popleft()
        current_distance = distance[current]
        if current_distance == radius:
            continue
        for move in moves:
            nxt = _add(current, move)
            if nxt in distance:
                continue
            distance[nxt] = current_distance + 1
            queue.append(nxt)
    return frozenset(distance)


def oriented_edge_vector(slot_count: int, edge: Edge) -> Vector:
    receiver, donor = edge
    if receiver == donor or any(index < 0 or index >= slot_count for index in edge):
        raise ValueError("edge must contain two distinct valid slots")
    vector = [0] * slot_count
    vector[receiver] = 1
    vector[donor] = -1
    return tuple(vector)


def contract_transfer_graph(
    slot_count: int,
    edges: tuple[Edge, ...],
    edge: Edge,
) -> tuple[int, tuple[Edge, ...], tuple[int, ...]]:
    """Contract the endpoints of `edge`; return `(new_n,new_edges,old_to_new)`."""
    _require_graph_edge(slot_count, edges, edge)
    left, right = edge
    keep = min(left, right)
    remove = max(left, right)
    representatives = [keep if index == remove else index for index in range(slot_count)]
    unique = sorted(set(representatives))
    new_index = {old: index for index, old in enumerate(unique)}
    old_to_new = tuple(new_index[representative] for representative in representatives)
    contracted = set()
    for a, b in _edge_set(slot_count, edges):
        na = old_to_new[a]
        nb = old_to_new[b]
        if na == nb:
            continue
        contracted.add(tuple(sorted((na, nb))))
    return slot_count - 1, tuple(sorted(contracted)), old_to_new


def contract_state(state: Vector, old_to_new: tuple[int, ...]) -> Vector:
    if len(state) != len(old_to_new):
        raise ValueError("state and contraction map must have same old slot count")
    result = [0] * (max(old_to_new) + 1)
    for old, value in enumerate(state):
        result[old_to_new[old]] += value
    return tuple(result)


def directional_cut_states(
    slot_count: int,
    edges: tuple[Edge, ...],
    oriented_edge: Edge,
    radius: int,
) -> frozenset[Vector]:
    _require_graph_edge(slot_count, edges, oriented_edge)
    ball = word_ball(slot_count, edges, radius)
    move = oriented_edge_vector(slot_count, oriented_edge)
    return frozenset(state for state in ball if _add(state, move) not in ball)


def boundary_contraction_projection(
    slot_count: int,
    edges: tuple[Edge, ...],
    oriented_edge: Edge,
    radius: int,
) -> dict[Vector, Vector]:
    new_n, new_edges, old_to_new = contract_transfer_graph(slot_count, edges, oriented_edge)
    cut = directional_cut_states(slot_count, edges, oriented_edge, radius)
    projected = {state: contract_state(state, old_to_new) for state in cut}
    target_ball = word_ball(new_n, new_edges, radius)
    if set(projected.values()) != set(target_ball):
        raise AssertionError("directional cut projection is not surjective onto contracted ball")
    if len(set(projected.values())) != len(projected):
        raise AssertionError("directional cut projection is not injective on the cut")
    return projected


def boundary_contraction_bijection_holds(
    slot_count: int,
    edges: tuple[Edge, ...],
    oriented_edge: Edge,
    radius: int,
) -> bool:
    projection = boundary_contraction_projection(slot_count, edges, oriented_edge, radius)
    new_n, new_edges, _ = contract_transfer_graph(slot_count, edges, oriented_edge)
    return len(projection) == len(word_ball(new_n, new_edges, radius))


def total_relation_boundary_count(slot_count: int, edges: tuple[Edge, ...], radius: int) -> int:
    """Count all directed primitive relations crossing from B_G(r) to its complement."""
    normalized = tuple(sorted(_edge_set(slot_count, edges)))
    return sum(
        len(directional_cut_states(slot_count, normalized, oriented, radius))
        for left, right in normalized
        for oriented in ((left, right), (right, left))
    )


def contracted_ball_boundary_sum(slot_count: int, edges: tuple[Edge, ...], radius: int) -> int:
    """The contraction-side formula 2*sum_e |B_(G/e)(r)|."""
    normalized = tuple(sorted(_edge_set(slot_count, edges)))
    total = 0
    for edge in normalized:
        new_n, new_edges, _ = contract_transfer_graph(slot_count, normalized, edge)
        total += 2 * len(word_ball(new_n, new_edges, radius))
    return total


def total_relation_boundary_identity(slot_count: int, edges: tuple[Edge, ...], radius: int) -> bool:
    return total_relation_boundary_count(slot_count, edges, radius) == contracted_ball_boundary_sum(
        slot_count, edges, radius
    )
