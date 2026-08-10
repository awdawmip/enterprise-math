"""Complete anonymous transfer geometry as an envelope of basis-tree charts.

Every spanning tree of K_N is an independent relation basis of the same zero-sum
state lattice.  In that tree's edge-flow coordinates the primitive word metric is
L1/simple-cubic type.  The full K_N transfer law allows every pair shortcut.

For equal-total integer states x,y,

    d_KN(x,y) = min_T d_T(x,y)

over spanning trees T of K_N.  A shortest complete-graph transportation plan can
be chosen with acyclic support (the greedy donor/receiver plan is a forest), then
extended to a spanning tree; conversely a tree word is also a K_N word.

Thus A_(N-1)/FCC-type geometry is the lower envelope of all basis-only tree
metrics rather than an unrelated state space.
"""

from __future__ import annotations

from itertools import combinations

from .causal_conserved_transfer_geometry import minimum_transfer_plan, transfer_distance
from .causal_relation_independence import spanning_relation_bases
from .causal_transfer_graph_geometry import Edge, Vector, complete_transfer_edges, slot_shortest_path_distance


def _pair_unit_cost(edges: tuple[Edge, ...], slot_count: int, donor: int, receiver: int) -> int:
    distance = slot_shortest_path_distance(slot_count, edges, donor, receiver)
    if distance is None:
        raise ValueError("basis tree must connect every slot")
    return distance


def tree_transport_distance(left: Vector, right: Vector, tree_edges: tuple[Edge, ...]) -> int:
    """Exact earth-mover cost on a unit-edge-cost transfer tree.

    On a tree, deleting edge e splits vertices into S and S^c.  The net number of
    units that must cross e is the absolute charge imbalance on either side.  The
    total word distance is the sum of these mandatory edge flows.
    """
    if len(left) != len(right) or not left or sum(left) != sum(right):
        raise ValueError("states must have equal slot count and equal total")
    n = len(left)
    delta = tuple(target - source for source, target in zip(left, right))
    normalized = tuple(sorted(tuple(sorted(edge)) for edge in tree_edges))
    if len(normalized) != n - 1:
        raise ValueError("tree basis must contain N-1 edges")
    total = 0
    for removed in normalized:
        remaining = [edge for edge in normalized if edge != removed]
        adjacency = {index: set() for index in range(n)}
        for a, b in remaining:
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


def greedy_plan_support(left: Vector, right: Vector) -> tuple[Edge, ...]:
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
    if len(left) != len(right) or not left:
        raise ValueError("states must have equal nonzero slot count")
    complete = transfer_distance(left, right)
    bases = spanning_relation_bases(len(left), complete_transfer_edges(len(left)))
    minimum = min(tree_transport_distance(left, right, tree) for tree in bases)
    return complete == minimum


def fixed_edge_tree_multiplicity(slot_count: int) -> int:
    """Number of K_N spanning trees containing one fixed edge: 2*N^(N-3)."""
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count < 2:
        raise ValueError("slot_count must be at least two")
    if slot_count == 2:
        return 1
    return 2 * slot_count ** (slot_count - 3)


def complete_tree_count(slot_count: int) -> int:
    if slot_count < 2:
        return 1
    return slot_count ** (slot_count - 2)
