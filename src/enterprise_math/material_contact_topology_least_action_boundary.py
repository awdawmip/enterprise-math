"""Topology boundary for schedule-independent E001 contact least action.

This owner asks when the contact coupling

    K = B^T D B

inherits the Z-matrix sign pattern used by the weighted-chain least-action
solver.  The result is purely at the declared contact-network layer and makes
no continuum or contact-discovery claim.

For a simple contact graph with positive body weights ``D_i``, two distinct
contact columns can overlap at at most one body.  Hence, when contacts ``e``
and ``f`` share body ``v``,

    K_ef = D_v * B_ve * B_vf.

Therefore every off-diagonal entry is non-positive iff two local conditions
hold:

1. no body has contact degree greater than two;
2. at every degree-two body, the two incident incidence signs are opposite.

Equivalently, every nontrivial connected component is an incidence-consistent
path or directed cycle.  This is a sign-pattern characterization, not a new
generic graph-theory theorem.

There is a further exact boundary for a directed cycle.  Its incidence columns
sum to zero, so for ``r=B^T D p``

    sum_e r_e = 0.

Consequently, if every cycle contact is closing or comoving (``r_e<=0``), then
all cycle scores are exactly zero.  Thus the nontrivial all-nonseparating
Z-coupled contact components are paths: directed cycles are already comoving.

Branching is the first topology where the Z-sign guarantee is impossible.  A
three-edge equal-mass star gives the minimal policy counterexample: all three
contacts can start at score ``-1``, while one unit impulse on *any* single edge
makes every score non-negative.  The three feasible unit vectors are
incomparable and their coordinatewise meet is infeasible.  Hence a generic
"update any violated contact" rule becomes schedule/policy dependent once the
Z-pattern is lost.

This module only certifies the topology/sign boundary.  It does not claim that
every non-Z contact network is schedule dependent, only that the path
least-action proof no longer follows from the contact Gram sign structure.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_contact_network_impulse_1d import (
    ContactNetworkMomentum1D,
    contact_coupling_gram,
    contact_incidence_matrix,
    contact_relative_scores,
)


@dataclass(frozen=True)
class ContactTopologyComponent1D:
    body_indices: tuple[int, ...]
    contact_indices: tuple[int, ...]
    kind: str


@dataclass(frozen=True)
class ContactZTopologyCertificate1D:
    body_degrees: tuple[int, ...]
    branching_bodies: tuple[int, ...]
    degree_two_orientation_defects: tuple[int, ...]
    coupling_gram: tuple[tuple[int, ...], ...]
    gram_is_z_matrix: bool
    topology_condition_holds: bool
    components: tuple[ContactTopologyComponent1D, ...]
    cycle_score_sums: tuple[tuple[tuple[int, ...], int], ...]

    @property
    def z_components_are_paths_or_cycles(self) -> bool:
        if not self.gram_is_z_matrix:
            return False
        return all(component.kind in ("PATH", "CYCLE") for component in self.components)


def _incident_contact_indices(state: ContactNetworkMomentum1D) -> tuple[tuple[int, ...], ...]:
    incident: list[list[int]] = [[] for _ in state.masses]
    for edge_index, contact in enumerate(state.contacts):
        incident[contact.body_a].append(edge_index)
        incident[contact.body_b].append(edge_index)
    return tuple(tuple(edges) for edges in incident)


def _contact_components(
    state: ContactNetworkMomentum1D,
    incident: tuple[tuple[int, ...], ...],
) -> tuple[ContactTopologyComponent1D, ...]:
    unseen = {body for body, edges in enumerate(incident) if edges}
    components: list[ContactTopologyComponent1D] = []

    while unseen:
        start = min(unseen)
        stack = [start]
        bodies: set[int] = set()
        edges: set[int] = set()
        while stack:
            body = stack.pop()
            if body in bodies:
                continue
            bodies.add(body)
            unseen.discard(body)
            for edge_index in incident[body]:
                edges.add(edge_index)
                contact = state.contacts[edge_index]
                other = contact.body_b if contact.body_a == body else contact.body_a
                if other not in bodies:
                    stack.append(other)

        degrees = tuple(len(incident[body]) for body in bodies)
        if all(degree == 2 for degree in degrees):
            kind = "CYCLE"
        elif degrees.count(1) == 2 and all(degree in (1, 2) for degree in degrees):
            kind = "PATH"
        else:
            kind = "OTHER"
        components.append(
            ContactTopologyComponent1D(
                body_indices=tuple(sorted(bodies)),
                contact_indices=tuple(sorted(edges)),
                kind=kind,
            )
        )

    return tuple(components)


def contact_gram_is_z_matrix(state: ContactNetworkMomentum1D) -> bool:
    """Return whether every off-diagonal contact coupling is non-positive."""
    gram = contact_coupling_gram(state)
    return all(
        row == col or gram[row][col] <= 0
        for row in range(len(gram))
        for col in range(len(gram))
    )


def contact_z_topology_certificate(
    state: ContactNetworkMomentum1D,
) -> ContactZTopologyCertificate1D:
    """Certify the exact local-topology criterion for a contact Gram Z-pattern."""
    incident = _incident_contact_indices(state)
    incidence = contact_incidence_matrix(state)
    degrees = tuple(len(edges) for edges in incident)
    branching = tuple(body for body, degree in enumerate(degrees) if degree > 2)

    orientation_defects: list[int] = []
    for body, edges in enumerate(incident):
        if len(edges) != 2:
            continue
        left, right = edges
        if incidence[body][left] * incidence[body][right] >= 0:
            orientation_defects.append(body)

    topology_condition = not branching and not orientation_defects
    gram = contact_coupling_gram(state)
    z_matrix = all(
        row == col or gram[row][col] <= 0
        for row in range(len(gram))
        for col in range(len(gram))
    )
    if z_matrix != topology_condition:
        raise AssertionError("contact Gram Z-pattern disagrees with local topology criterion")

    components = _contact_components(state, incident)
    if z_matrix and any(component.kind == "OTHER" for component in components):
        raise AssertionError("Z-coupled simple contact component is neither path nor cycle")

    scores = contact_relative_scores(state)
    cycle_sums: list[tuple[tuple[int, ...], int]] = []
    for component in components:
        if component.kind != "CYCLE" or not z_matrix:
            continue
        score_sum = sum(scores[index] for index in component.contact_indices)
        if score_sum != 0:
            raise AssertionError("incidence-consistent cycle lost zero score-sum identity")
        cycle_sums.append((component.contact_indices, score_sum))

    return ContactZTopologyCertificate1D(
        body_degrees=degrees,
        branching_bodies=branching,
        degree_two_orientation_defects=tuple(orientation_defects),
        coupling_gram=gram,
        gram_is_z_matrix=z_matrix,
        topology_condition_holds=topology_condition,
        components=components,
        cycle_score_sums=tuple(cycle_sums),
    )


def z_cycle_nonseparating_scores_are_comoving(
    state: ContactNetworkMomentum1D,
) -> bool:
    """Return the directed-cycle consequence under an all-nonseparating state.

    The function requires a Z-coupled network and no separating contact.  Every
    contact belonging to a cycle component must then have score exactly zero.
    Path components may still contain strictly closing contacts.
    """
    certificate = contact_z_topology_certificate(state)
    if not certificate.gram_is_z_matrix:
        raise ValueError("cycle consequence requires a Z-coupled contact network")
    scores = contact_relative_scores(state)
    if any(score > 0 for score in scores):
        raise ValueError("cycle consequence requires no separating contact")
    return all(
        scores[index] == 0
        for component in certificate.components
        if component.kind == "CYCLE"
        for index in component.contact_indices
    )
