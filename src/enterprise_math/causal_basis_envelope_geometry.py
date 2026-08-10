"""Conservative transfer geometry as an envelope of independent basis-tree charts.

For any connected slot-transfer graph G, every spanning tree is an independent
relation basis of the same incidence lattice.  In a tree's edge-flow coordinates
the primitive word metric is L1/simple-cubic type.

The exact G word metric is the lower envelope

    d_G(x,y) = min_{T spanning tree of G} d_T(x,y).

A minimum-cost integral flow can be chosen without directed cycles; its undirected
support can be reduced to a forest and extended to a spanning tree.  Conversely,
every tree word is a G word.

Second-order basis shadows satisfy

    sum_T P_T(x) = sum_{e in E(G)} tau_e (x_i-x_j)^2,

where tau_e is the number of spanning trees containing e, equivalently the tree
count of G/e.  Complete anonymous geometry is the edge-transitive special case in
which all tau_e are equal.
"""

from __future__ import annotations

from collections import deque

from .causal_conserved_transfer_geometry import minimum_transfer_plan, transfer_distance
from .causal_relation_independence import spanning_relation_bases
from .causal_transfer_graph_geometry import Edge, Vector, complete_transfer_edges, primitive_transfer_moves


def tree_transport_distance(left: Vector, right: Vector, tree_edges: tuple[Edge, ...]) -> int:
    """Exact earth-mover cost on a unit-edge-cost transfer tree."""
    if len(left) != len(right) or not left or sum(left) != sum(right):
        raise ValueError("states must have equal slot count and equal total")
    n = len(left)
    delta = tuple(target - source for source, target in zip(left, right))
    normalized = tuple(sorted(set(tuple(sorted(edge)) for edge in tree_edges)))
    if len(normalized) != n - 1:
        raise ValueError("tree basis must contain N-1 distinct edges")
    total = 0
    for removed in normalized:
        adjacency = {index: set() for index in range(n)}
        for edge in normalized:
            if edge == removed:
                continue
            a, b = edge
            adjacency[a].add(b)
            adjacency[b].add(a)
        seed = removed[0]
        stack = [seed]
        seen = {seed}
        while stack:
            current = stack.pop()
            for nxt in adjacency[current]:
                if nxt not in seen:
                    seen.add(nxt)
                    stack.append(nxt)
        total += abs(sum(delta[index] for index in seen))
    return total


def graph_metric_via_tree_envelope(
    left: Vector,
    right: Vector,
    allowed_edges: tuple[Edge, ...],
) -> int:
    if len(left) != len(right) or not left or sum(left) != sum(right):
        raise ValueError("states must have equal slot count and equal total")
    bases = spanning_relation_bases(len(left), allowed_edges)
    if not bases:
        raise ValueError("allowed transfer graph must connect all slots")
    return min(tree_transport_distance(left, right, tree) for tree in bases)


def graph_word_distance_bfs(
    left: Vector,
    right: Vector,
    allowed_edges: tuple[Edge, ...],
) -> int:
    """Independent exact oracle for small examples; not intended as main algorithm."""
    if len(left) != len(right) or not left or sum(left) != sum(right):
        raise ValueError("states must have equal slot count and equal total")
    if left == right:
        return 0
    moves = primitive_transfer_moves(len(left), allowed_edges)
    if not moves:
        raise ValueError("nontrivial connected transfer law requires primitive moves")
    distance = {left: 0}
    queue = deque([left])
    while queue:
        current = queue.popleft()
        current_distance = distance[current]
        for move in moves:
            nxt = tuple(value + shift for value, shift in zip(current, move))
            if nxt in distance:
                continue
            if nxt == right:
                return current_distance + 1
            distance[nxt] = current_distance + 1
            queue.append(nxt)
    raise ValueError("right state is not reachable from left")


def graph_metric_envelope_identity(
    left: Vector,
    right: Vector,
    allowed_edges: tuple[Edge, ...],
) -> bool:
    return graph_metric_via_tree_envelope(left, right, allowed_edges) == graph_word_distance_bfs(
        left, right, allowed_edges
    )


def greedy_plan_support(left: Vector, right: Vector) -> tuple[Edge, ...]:
    """Acyclic support witness specialized to the complete transfer graph."""
    plan = minimum_transfer_plan(left, right)
    return tuple(sorted({tuple(sorted((step.receiver, step.donor))) for step in plan}))


def edge_set_is_forest(slot_count: int, edges: tuple[Edge, ...]) -> bool:
    parent = list(range(slot_count))

    def find(value):
        while parent[value] != value:
            parent[value] = parent[parent[value]]
            value = parent[value]
        return value

    for left, right in edges:
        a = find(left)
        b = find(right)
        if a == b:
            return False
        parent[a] = b
    return True


def spanning_tree_containing_support(slot_count: int, support: tuple[Edge, ...]) -> tuple[Edge, ...]:
    if not edge_set_is_forest(slot_count, support):
        raise ValueError("support must be acyclic")
    selected = set(tuple(sorted(edge)) for edge in support)
    parent = list(range(slot_count))

    def find(value):
        while parent[value] != value:
            parent[value] = parent[parent[value]]
            value = parent[value]
        return value

    def union(left, right):
        a = find(left)
        b = find(right)
        if a == b:
            return False
        parent[a] = b
        return True

    for left, right in sorted(selected):
        union(left, right)
    for edge in complete_transfer_edges(slot_count):
        if len(selected) == slot_count - 1:
            break
        if union(*edge):
            selected.add(edge)
    if len(selected) != slot_count - 1:
        raise AssertionError("forest support must extend to a spanning tree")
    return tuple(sorted(selected))


def complete_metric_has_tree_witness(left: Vector, right: Vector) -> tuple[tuple[Edge, ...], int]:
    support = greedy_plan_support(left, right)
    if not edge_set_is_forest(len(left), support):
        raise AssertionError("greedy donor/receiver plan support must be a forest")
    tree = spanning_tree_containing_support(len(left), support)
    distance = tree_transport_distance(left, right, tree)
    if distance != transfer_distance(left, right):
        raise AssertionError("witness tree must attain complete-transfer distance")
    return tree, distance


def complete_distance_is_minimum_tree_distance(left: Vector, right: Vector) -> bool:
    complete = transfer_distance(left, right)
    minimum = graph_metric_via_tree_envelope(left, right, complete_transfer_edges(len(left)))
    return complete == minimum


def spanning_tree_count(slot_count: int, allowed_edges: tuple[Edge, ...]) -> int:
    return len(spanning_relation_bases(slot_count, allowed_edges))


def edge_tree_multiplicity(slot_count: int, allowed_edges: tuple[Edge, ...], edge: Edge) -> int:
    target = tuple(sorted(edge))
    return sum(target in tree for tree in spanning_relation_bases(slot_count, allowed_edges))


def fixed_edge_tree_multiplicity(slot_count: int) -> int:
    """K_N specialization: one fixed edge lies in 2*N^(N-3) spanning trees."""
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count < 2:
        raise ValueError("slot_count must be at least two")
    if slot_count == 2:
        return 1
    return 2 * slot_count ** (slot_count - 3)


def complete_tree_count(slot_count: int) -> int:
    if slot_count < 2:
        return 1
    return slot_count ** (slot_count - 2)


def basis_quadratic_edge_weights(slot_count: int, allowed_edges: tuple[Edge, ...]) -> dict[Edge, int]:
    """Weight each primitive edge by the number of independent bases containing it."""
    edges = tuple(sorted(set(tuple(sorted(edge)) for edge in allowed_edges)))
    return {edge: edge_tree_multiplicity(slot_count, edges, edge) for edge in edges}


def sum_tree_edge_dispersion(
    state: Vector,
    allowed_edges: tuple[Edge, ...],
) -> int:
    """Sum P_T(state) over all spanning-tree basis charts without enumerating P_T separately."""
    weights = basis_quadratic_edge_weights(len(state), allowed_edges)
    return sum(weights[edge] * (state[edge[0]] - state[edge[1]]) ** 2 for edge in weights)
