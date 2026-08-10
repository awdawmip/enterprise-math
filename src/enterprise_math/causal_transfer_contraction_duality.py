"""Dual response-cell effect of primitive relation contraction.

For a transfer graph G, unit-response probes are integer/rational potentials phi
with |phi_i-phi_j|<=1 on every primitive edge.  Contracting an edge identifies two
slots in the primal relation state.  On the dual side, exactly those probes that
cannot distinguish the identified slots survive: phi_i=phi_j.

Hence the response cell of G/e is canonically the central section of the G
response cell by the annihilator of e.  Contracting a forest F forces phi to be
constant on every F-component.  Each independent contracted edge removes one
primal relation freedom and one dual probe freedom.

This is finite integer/rational linear duality; no continuous normal-vector
ontology is assumed.
"""

from __future__ import annotations

from fractions import Fraction

from .causal_transfer_boundary_contraction import contract_transfer_graph
from .causal_transfer_graph_geometry import Edge

Potential = tuple[Fraction, ...]


def _normalize_potential(values) -> Potential:
    return tuple(Fraction(value) for value in values)


def response_potential_is_valid(potential: Potential, edges: tuple[Edge, ...]) -> bool:
    if not potential:
        raise ValueError("potential must be nonempty")
    return all(abs(potential[left] - potential[right]) <= 1 for left, right in edges)


def pullback_contracted_potential(
    contracted_potential: Potential,
    old_to_new: tuple[int, ...],
) -> Potential:
    if len(contracted_potential) != max(old_to_new) + 1:
        raise ValueError("contracted potential dimension does not match contraction map")
    return tuple(contracted_potential[index] for index in old_to_new)


def descend_potential_to_contraction(
    potential: Potential,
    old_to_new: tuple[int, ...],
) -> Potential:
    """Descend iff potential is constant on every contraction fiber."""
    if len(potential) != len(old_to_new):
        raise ValueError("potential and contraction map must have equal old dimension")
    values: dict[int, Fraction] = {}
    for old, new in enumerate(old_to_new):
        value = Fraction(potential[old])
        previous = values.get(new)
        if previous is not None and previous != value:
            raise ValueError("potential distinguishes slots that were contracted")
        values[new] = value
    return tuple(values[index] for index in range(max(old_to_new) + 1))


def edge_contraction_response_section_identity(
    slot_count: int,
    edges: tuple[Edge, ...],
    edge: Edge,
    contracted_potential,
) -> bool:
    new_n, new_edges, old_to_new = contract_transfer_graph(slot_count, edges, edge)
    psi = _normalize_potential(contracted_potential)
    if len(psi) != new_n:
        raise ValueError("contracted potential has wrong size")
    phi = pullback_contracted_potential(psi, old_to_new)
    return response_potential_is_valid(psi, new_edges) == response_potential_is_valid(phi, edges)


def contraction_annihilator_condition(
    potential: Potential,
    edge: Edge,
) -> bool:
    left, right = edge
    return potential[left] == potential[right]


def forest_components(slot_count: int, forest_edges: tuple[Edge, ...]) -> tuple[tuple[int, ...], ...]:
    adjacency = {index: set() for index in range(slot_count)}
    for left, right in forest_edges:
        adjacency[left].add(right)
        adjacency[right].add(left)
    unseen = set(range(slot_count))
    components = []
    while unseen:
        seed = min(unseen)
        stack = [seed]
        unseen.remove(seed)
        component = []
        while stack:
            current = stack.pop()
            component.append(current)
            for nxt in adjacency[current]:
                if nxt in unseen:
                    unseen.remove(nxt)
                    stack.append(nxt)
        components.append(tuple(sorted(component)))
    return tuple(sorted(components))


def potential_is_constant_on_forest_components(
    potential: Potential,
    forest_edges: tuple[Edge, ...],
) -> bool:
    components = forest_components(len(potential), forest_edges)
    return all(len({potential[index] for index in component}) == 1 for component in components)


def forest_contraction_probe_rank(slot_count: int, forest_edges: tuple[Edge, ...]) -> int:
    """Probe freedom modulo global additive gauge after contracting the forest."""
    components = forest_components(slot_count, forest_edges)
    return max(0, len(components) - 1)


def independent_contraction_rank_drop(slot_count: int, forest_edges: tuple[Edge, ...]) -> int:
    return slot_count - len(forest_components(slot_count, forest_edges))
