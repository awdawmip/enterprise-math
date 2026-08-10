"""Primitive geometry from a graph of allowed conservative unit transfers.

Vertices are integer relation slots.  An undirected graph edge {i,j} means one
indivisible unit may move directly between slots i and j; both orientations give
primitive displacement vectors +/- (e_i-e_j).

For any connected transfer graph on N slots, the generated integer displacement
lattice is the same zero-sum lattice A_(N-1).  The primitive operation metric is
not the same: it depends on the transfer graph.  The complete graph K_N gives the
A_(N-1) root metric.  A star K_(1,p) with a marked reservoir gives, after keeping
only its p leaves as visible coordinates, the standard Z^p axis moves and L1
metric.  Thus FCC-vs-simple-cubic can be studied as primitive-operation symmetry
breaking on one conserved state lattice rather than as two unrelated ontologies.
"""

from __future__ import annotations

from collections import deque
from itertools import combinations

Vector = tuple[int, ...]
Edge = tuple[int, int]


def _normalized_edges(slot_count: int, edges: tuple[Edge, ...]) -> tuple[Edge, ...]:
    if isinstance(slot_count, bool) or not isinstance(slot_count, int) or slot_count < 1:
        raise ValueError("slot_count must be positive")
    normalized = set()
    for left, right in edges:
        if any(
            isinstance(index, bool)
            or not isinstance(index, int)
            or not (0 <= index < slot_count)
            for index in (left, right)
        ):
            raise ValueError("edge endpoint outside slot range")
        if left == right:
            raise ValueError("transfer graph cannot contain loops")
        normalized.add(tuple(sorted((left, right))))
    return tuple(sorted(normalized))


def complete_transfer_edges(slot_count: int) -> tuple[Edge, ...]:
    return tuple(combinations(range(slot_count), 2))


def star_transfer_edges(slot_count: int, hub: int = 0) -> tuple[Edge, ...]:
    if isinstance(hub, bool) or not isinstance(hub, int) or not (0 <= hub < slot_count):
        raise ValueError("hub must be a valid slot")
    return tuple(tuple(sorted((hub, leaf))) for leaf in range(slot_count) if leaf != hub)


def transfer_components(slot_count: int, edges: tuple[Edge, ...]) -> tuple[tuple[int, ...], ...]:
    normalized = _normalized_edges(slot_count, edges)
    adjacency = {slot: set() for slot in range(slot_count)}
    for left, right in normalized:
        adjacency[left].add(right)
        adjacency[right].add(left)
    unseen = set(range(slot_count))
    components = []
    while unseen:
        seed = min(unseen)
        unseen.remove(seed)
        queue = deque([seed])
        component = []
        while queue:
            current = queue.popleft()
            component.append(current)
            for nxt in adjacency[current]:
                if nxt in unseen:
                    unseen.remove(nxt)
                    queue.append(nxt)
        components.append(tuple(sorted(component)))
    return tuple(sorted(components))


def transfer_relation_rank(slot_count: int, edges: tuple[Edge, ...]) -> int:
    """Integer incidence rank N-c for c connected components."""
    return slot_count - len(transfer_components(slot_count, edges))


def primitive_transfer_moves(slot_count: int, edges: tuple[Edge, ...]) -> tuple[Vector, ...]:
    normalized = _normalized_edges(slot_count, edges)
    moves = []
    for left, right in normalized:
        for receiver, donor in ((left, right), (right, left)):
            vector = [0] * slot_count
            vector[receiver] = 1
            vector[donor] = -1
            moves.append(tuple(vector))
    return tuple(moves)


def component_charge_constraints(
    state: Vector,
    components: tuple[tuple[int, ...], ...],
) -> tuple[int, ...]:
    return tuple(sum(state[index] for index in component) for component in components)


def generated_lattice_membership(
    vector: Vector,
    slot_count: int,
    edges: tuple[Edge, ...],
) -> bool:
    """Exact incidence-lattice criterion: sum is zero on every graph component."""
    if len(vector) != slot_count or any(isinstance(value, bool) or not isinstance(value, int) for value in vector):
        raise ValueError("vector must be an integer state of the declared slot count")
    components = transfer_components(slot_count, edges)
    return all(total == 0 for total in component_charge_constraints(vector, components))


def complete_graph_transfer_distance(left: Vector, right: Vector) -> int:
    if len(left) != len(right) or sum(left) != sum(right):
        raise ValueError("states must have equal slot count and equal total")
    return sum(max(0, target - source) for source, target in zip(left, right))


def star_visible_coordinates(state: Vector, hub: int = 0) -> Vector:
    if isinstance(hub, bool) or not isinstance(hub, int) or not (0 <= hub < len(state)):
        raise ValueError("hub must be a valid state coordinate")
    return tuple(value for index, value in enumerate(state) if index != hub)


def star_transfer_distance(left: Vector, right: Vector, hub: int = 0) -> int:
    if len(left) != len(right) or sum(left) != sum(right):
        raise ValueError("states must have equal slot count and equal total")
    visible_left = star_visible_coordinates(left, hub)
    visible_right = star_visible_coordinates(right, hub)
    return sum(abs(a - b) for a, b in zip(visible_left, visible_right))


def projected_star_primitive_moves(slot_count: int, hub: int = 0) -> tuple[Vector, ...]:
    """Project star primitive transfers to non-hub coordinates: exactly +/-e_i."""
    return tuple(
        star_visible_coordinates(move, hub)
        for move in primitive_transfer_moves(slot_count, star_transfer_edges(slot_count, hub))
    )


def complete_graph_is_fully_slot_exchange_symmetric(slot_count: int) -> bool:
    """The unique nonempty simple edge set invariant under all slot permutations is K_N.

    For simple pair relations, the full symmetric group acts transitively on
    unordered distinct pairs.  Hence an invariant nonempty edge set contains the
    full orbit, i.e. every pair.  This function records the resulting theorem.
    """
    return set(complete_transfer_edges(slot_count)) == set(combinations(range(slot_count), 2))
