"""Cycle-space non-identifiability for delivered E001 contact impulses.

This module is a contact-world specialization of standard graph-incidence
algebra.  It does not claim a new graph theorem.

For a declared simple contact network with signed incidence matrix ``B`` and
positive diagonal mass scale ``D``, Stage 2 defines

    K = B^T D B.

Because ``D`` has strictly positive integer diagonal entries,

    ker(K) = ker(B).

For an undirected simple graph with ``V`` bodies, ``E`` contacts and ``c``
connected components (isolated bodies included), the incidence-kernel dimension
is the cycle rank

    beta = E - V + c.

Consequently the delivered contact-impulse map ``j -> B j`` is injective exactly
when the contact graph is a forest.  On a cyclic graph, distinct contact impulse
vectors can produce the same body momentum increment and therefore the same
contact relative-score increment.  Body-level state then cannot reconstruct the
contact-witness allocation without additional history/state.

This is an exact finite instance of the project's broader witness-history
boundary: equality of compressed values does not imply equality of causal
witnesses.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_contact_network_impulse_1d import (
    ContactNetworkMomentum1D,
    contact_coupling_gram,
    contact_incidence_matrix,
)


def _require_edge_vector(
    state: ContactNetworkMomentum1D,
    values: tuple[int, ...] | list[int],
    name: str,
) -> tuple[int, ...]:
    vector = tuple(values)
    if len(vector) != len(state.contacts):
        raise ValueError(f"{name} must match contact count")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in vector):
        raise ValueError(f"{name} entries must be integers")
    return vector


def contact_graph_component_count(state: ContactNetworkMomentum1D) -> int:
    """Count graph components, including isolated bodies, by exact union-find."""
    parent = list(range(len(state.masses)))

    def find(vertex: int) -> int:
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    def union(left: int, right: int) -> None:
        root_left = find(left)
        root_right = find(right)
        if root_left != root_right:
            parent[root_right] = root_left

    for contact in state.contacts:
        union(contact.body_a, contact.body_b)
    return len({find(vertex) for vertex in range(len(state.masses))})


def contact_cycle_rank(state: ContactNetworkMomentum1D) -> int:
    """Return ``E-V+c``, the exact dimension of the incidence cycle space."""
    rank = len(state.contacts) - len(state.masses) + contact_graph_component_count(state)
    if rank < 0:
        raise AssertionError("simple contact graph produced negative cycle rank")
    return rank


def contact_graph_is_forest(state: ContactNetworkMomentum1D) -> bool:
    return contact_cycle_rank(state) == 0


def incidence_image(
    state: ContactNetworkMomentum1D,
    edge_vector: tuple[int, ...] | list[int],
) -> tuple[int, ...]:
    """Return ``B x`` for one integer contact-coordinate vector."""
    vector = _require_edge_vector(state, edge_vector, "edge_vector")
    incidence = contact_incidence_matrix(state)
    return tuple(
        sum(
            incidence[body][edge] * vector[edge]
            for edge in range(len(vector))
        )
        for body in range(len(state.masses))
    )


def coupling_image(
    state: ContactNetworkMomentum1D,
    edge_vector: tuple[int, ...] | list[int],
) -> tuple[int, ...]:
    """Return ``K x`` for ``K=B^T D B``."""
    vector = _require_edge_vector(state, edge_vector, "edge_vector")
    gram = contact_coupling_gram(state)
    return tuple(
        sum(gram[row][col] * vector[col] for col in range(len(vector)))
        for row in range(len(vector))
    )


def verify_incidence_coupling_kernel_equivalence(
    state: ContactNetworkMomentum1D,
    edge_vector: tuple[int, ...] | list[int],
) -> bool:
    """Verify on one integer vector that ``Bx=0`` iff ``Kx=0``."""
    body_zero = all(value == 0 for value in incidence_image(state, edge_vector))
    score_zero = all(value == 0 for value in coupling_image(state, edge_vector))
    if body_zero != score_zero:
        raise AssertionError("contact coupling kernel disagrees with incidence kernel")
    return body_zero


def contact_impulse_vectors_same_body_update(
    state: ContactNetworkMomentum1D,
    left: tuple[int, ...] | list[int],
    right: tuple[int, ...] | list[int],
) -> bool:
    """Whether two delivered contact vectors have the same ``B j`` body update."""
    left_vector = _require_edge_vector(state, left, "left")
    right_vector = _require_edge_vector(state, right, "right")
    difference = tuple(a - b for a, b in zip(left_vector, right_vector))
    return all(value == 0 for value in incidence_image(state, difference))


def contact_impulse_vectors_same_score_update(
    state: ContactNetworkMomentum1D,
    left: tuple[int, ...] | list[int],
    right: tuple[int, ...] | list[int],
) -> bool:
    """Whether two delivered contact vectors have the same ``K j`` score update."""
    left_vector = _require_edge_vector(state, left, "left")
    right_vector = _require_edge_vector(state, right, "right")
    difference = tuple(a - b for a, b in zip(left_vector, right_vector))
    return all(value == 0 for value in coupling_image(state, difference))


def verify_impulse_identifiability_equivalence(
    state: ContactNetworkMomentum1D,
) -> bool:
    """Return whether the contact-impulse update is injective: exactly the forest case."""
    # Standard incidence theorem: rank(B)=V-c, so nullity(B)=E-V+c.
    injective = contact_cycle_rank(state) == 0
    if injective != contact_graph_is_forest(state):
        raise AssertionError("forest/impulse-identifiability equivalence failed")
    return injective


@dataclass(frozen=True)
class ContactKernelReport1D:
    body_count: int
    contact_count: int
    component_count: int
    cycle_rank: int
    contact_graph_is_forest: bool
    impulse_update_is_injective: bool


def contact_kernel_report(state: ContactNetworkMomentum1D) -> ContactKernelReport1D:
    components = contact_graph_component_count(state)
    cycle_rank = len(state.contacts) - len(state.masses) + components
    forest = cycle_rank == 0
    return ContactKernelReport1D(
        body_count=len(state.masses),
        contact_count=len(state.contacts),
        component_count=components,
        cycle_rank=cycle_rank,
        contact_graph_is_forest=forest,
        impulse_update_is_injective=forest,
    )


def declared_cycle_circulation(
    state: ContactNetworkMomentum1D,
    cycle_bodies: tuple[int, ...] | list[int],
) -> tuple[int, ...]:
    """Construct one ±1 integer incidence-kernel witness on a declared simple cycle.

    ``cycle_bodies=(v0,...,v{k-1})`` means traverse
    ``v0->v1->...->v{k-1}->v0``.  Every required graph edge must exist.
    Contact normal/orientation only changes the coefficient sign needed to
    realize the same oriented cycle flow.
    """
    bodies = tuple(cycle_bodies)
    if len(bodies) < 3 or len(set(bodies)) != len(bodies):
        raise ValueError("cycle_bodies must contain at least three distinct bodies")
    if any(
        isinstance(body, bool)
        or not isinstance(body, int)
        or body < 0
        or body >= len(state.masses)
        for body in bodies
    ):
        raise ValueError("cycle body is outside the network")

    edge_lookup = {
        contact.unordered_key: (index, contact)
        for index, contact in enumerate(state.contacts)
    }
    vector = [0] * len(state.contacts)
    used_edges: set[int] = set()
    for source, target in zip(bodies, bodies[1:] + bodies[:1]):
        key = tuple(sorted((source, target)))
        if key not in edge_lookup:
            raise ValueError("declared cycle uses a missing contact edge")
        edge_index, contact = edge_lookup[key]
        if edge_index in used_edges:
            raise ValueError("declared cycle reused a contact edge")
        used_edges.add(edge_index)
        if contact.body_a == source and contact.body_b == target:
            coefficient = contact.normal_from_a_to_b
        elif contact.body_a == target and contact.body_b == source:
            coefficient = -contact.normal_from_a_to_b
        else:
            raise AssertionError("contact lookup lost declared endpoints")
        vector[edge_index] = coefficient

    result = tuple(vector)
    if not any(result):
        raise AssertionError("cycle circulation must be nonzero")
    if any(incidence_image(state, result)):
        raise AssertionError("declared cycle circulation failed Bx=0")
    if any(coupling_image(state, result)):
        raise AssertionError("declared cycle circulation failed Kx=0")
    return result
