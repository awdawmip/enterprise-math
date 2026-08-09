"""Topology boundary for schedule-independent E001 contact least action.

This module explains exactly why the weighted-chain least-action theorem does
not extend blindly to arbitrary simple contact networks.  It consumes the
contact-network incidence/Gram owner and the weighted-path solver; standard
incidence, graph, Z-matrix and M-matrix facts remain prior art.

For a simple declared contact graph with signed body/contact incidence ``B`` and
positive diagonal mass scale ``D``, distinct contacts share at most one body, so

    K_ef = (B^T D B)_ef

is zero when the contacts are disjoint and is ``+/- D_v`` when they meet at body
``v``.  Therefore ``K`` has non-positive off-diagonal entries exactly when, at
every body,

* the contact degree is at most two; and
* if the degree is two, the two incidence signs are opposite.

A connected nontrivial Z-coupled component is consequently either a coherently
oriented path or a coherently oriented cycle.  On a cycle the all-ones contact
vector lies in ``ker B``.  Hence the contact-score vector ``r=B^T D p`` sums to
zero around that component.  If every cycle score is also non-positive, every
cycle score is exactly zero and the zero impulse is already the componentwise
least response.

Each path component is independent of the others and can be traversed from its
unique source endpoint (incidence sign -1) to its sink endpoint (sign +1).  In
that order it is exactly the weighted-chain Z-coupling already solved by
``solve_weighted_chain_least_action``.  Thus any simple Z-coupled network with
no initially separating contact has a unique global componentwise-least impulse:
solve each path independently and use zero on each cycle.

The degree-three star is the sharp branching boundary.  With equal masses,
center momentum one, three leaf momenta zero and all normals pointing away from
the center,

    r = (-1,-1,-1),
    K = [[2,1,1],[1,2,1],[1,1,2]].

Each of ``(1,0,0)``, ``(0,1,0)``, ``(0,0,1)`` is feasible and inclusion-minimal,
while their coordinatewise meet is zero and is infeasible.  There is therefore
no global componentwise-least impulse.  The failure is structural, not a solver
bug or a need to wait for another branch.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_contact_network_impulse_1d import (
    ContactNetworkMomentum1D,
    apply_contact_impulse_vector,
    contact_coupling_gram,
    contact_incidence_matrix,
    contact_relative_scores,
)
from .material_weighted_chain_least_action_1d import (
    solve_weighted_chain_least_action,
)

PATH = "PATH"
CYCLE = "CYCLE"


@dataclass(frozen=True)
class ZContactComponent1D:
    kind: str
    bodies: tuple[int, ...]
    contacts: tuple[int, ...]


@dataclass(frozen=True)
class ZContactTopologyReport1D:
    body_degrees: tuple[int, ...]
    maximum_degree: int
    local_sign_condition: bool
    coupling_is_z_matrix: bool
    components: tuple[ZContactComponent1D, ...]


def _body_incident_edges(state: ContactNetworkMomentum1D) -> tuple[tuple[int, ...], ...]:
    incident: list[list[int]] = [[] for _ in state.masses]
    for edge, contact in enumerate(state.contacts):
        incident[contact.body_a].append(edge)
        incident[contact.body_b].append(edge)
    return tuple(tuple(edges) for edges in incident)


def _edge_other_body(state: ContactNetworkMomentum1D, edge: int, body: int) -> int:
    contact = state.contacts[edge]
    if contact.body_a == body:
        return contact.body_b
    if contact.body_b == body:
        return contact.body_a
    raise ValueError("body is not incident to contact")


def contact_coupling_is_z_matrix(state: ContactNetworkMomentum1D) -> bool:
    """Whether every off-diagonal contact coupling entry is non-positive."""
    gram = contact_coupling_gram(state)
    return all(
        row == col or gram[row][col] <= 0
        for row in range(len(gram))
        for col in range(len(gram))
    )


def contact_z_local_sign_condition(state: ContactNetworkMomentum1D) -> bool:
    """Check the exact degree/sign condition equivalent to Z-coupling."""
    incidence = contact_incidence_matrix(state)
    incident = _body_incident_edges(state)
    for body, edges in enumerate(incident):
        if len(edges) > 2:
            return False
        if len(edges) == 2:
            left, right = edges
            if incidence[body][left] != -incidence[body][right]:
                return False
    return True


def _edge_components(state: ContactNetworkMomentum1D) -> tuple[ZContactComponent1D, ...]:
    """Return path/cycle edge components after the Z local condition is known."""
    incident = _body_incident_edges(state)
    unseen = set(range(len(state.contacts)))
    components: list[ZContactComponent1D] = []

    while unseen:
        seed = min(unseen)
        stack = [seed]
        edges: set[int] = set()
        bodies: set[int] = set()
        while stack:
            edge = stack.pop()
            if edge in edges:
                continue
            edges.add(edge)
            unseen.discard(edge)
            contact = state.contacts[edge]
            for body in (contact.body_a, contact.body_b):
                bodies.add(body)
                for neighbor in incident[body]:
                    if neighbor not in edges:
                        stack.append(neighbor)

        degrees = [len(incident[body]) for body in bodies]
        if all(degree == 2 for degree in degrees):
            kind = CYCLE
        elif degrees.count(1) == 2 and all(degree in (1, 2) for degree in degrees):
            kind = PATH
        else:
            raise AssertionError("Z-coupled edge component is neither path nor cycle")
        components.append(
            ZContactComponent1D(
                kind=kind,
                bodies=tuple(sorted(bodies)),
                contacts=tuple(sorted(edges)),
            )
        )
    return tuple(components)


def z_contact_topology_report(
    state: ContactNetworkMomentum1D,
) -> ZContactTopologyReport1D:
    """Audit the exact topology/sign condition behind a Z contact Gram."""
    incident = _body_incident_edges(state)
    local = contact_z_local_sign_condition(state)
    direct = contact_coupling_is_z_matrix(state)
    if local != direct:
        raise AssertionError("local degree/sign criterion disagrees with contact Gram")
    components = _edge_components(state) if local else ()
    return ZContactTopologyReport1D(
        body_degrees=tuple(len(edges) for edges in incident),
        maximum_degree=max((len(edges) for edges in incident), default=0),
        local_sign_condition=local,
        coupling_is_z_matrix=direct,
        components=components,
    )


def _path_traversal(
    state: ContactNetworkMomentum1D,
    component: ZContactComponent1D,
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Return source-to-sink body order and corresponding original edge order."""
    if component.kind != PATH:
        raise ValueError("path traversal requires a path component")
    incidence = contact_incidence_matrix(state)
    incident = _body_incident_edges(state)
    component_edges = set(component.contacts)
    endpoints = [
        body
        for body in component.bodies
        if sum(edge in component_edges for edge in incident[body]) == 1
    ]
    if len(endpoints) != 2:
        raise AssertionError("path component lost its two endpoints")

    sources = []
    for body in endpoints:
        edge = next(edge for edge in incident[body] if edge in component_edges)
        if incidence[body][edge] == -1:
            sources.append(body)
    if len(sources) != 1:
        raise AssertionError("coherent Z path lost unique source endpoint")

    body_order = [sources[0]]
    edge_order: list[int] = []
    previous_edge: int | None = None
    current = sources[0]
    while True:
        choices = [
            edge
            for edge in incident[current]
            if edge in component_edges and edge != previous_edge
        ]
        if not choices:
            break
        if len(choices) != 1:
            raise AssertionError("path traversal encountered branching")
        edge = choices[0]
        if incidence[current][edge] != -1:
            raise AssertionError("Z path traversal encountered non-outgoing next edge")
        following = _edge_other_body(state, edge, current)
        if incidence[following][edge] != 1:
            raise AssertionError("contact column lost opposite endpoint signs")
        edge_order.append(edge)
        body_order.append(following)
        previous_edge = edge
        current = following

    if set(edge_order) != component_edges:
        raise AssertionError("path traversal did not cover its whole component")
    return tuple(body_order), tuple(edge_order)


@dataclass(frozen=True)
class ZContactLeastActionSolution1D:
    before: ContactNetworkMomentum1D
    impulse_vector: tuple[int, ...]
    final_scores: tuple[int, ...]
    final_momenta: tuple[int, ...]
    component_solutions: tuple[tuple[str, tuple[int, ...], tuple[int, ...]], ...]


def solve_z_contact_network_least_action(
    state: ContactNetworkMomentum1D,
) -> ZContactLeastActionSolution1D:
    """Solve every Z-coupled path component and leave trivial cycles at zero."""
    report = z_contact_topology_report(state)
    if not report.coupling_is_z_matrix:
        raise ValueError("least-action decomposition requires a Z-coupled contact network")
    initial_scores = contact_relative_scores(state)
    if any(score > 0 for score in initial_scores):
        raise ValueError("least-action decomposition requires no initially separating contact")

    global_impulses = [0] * len(state.contacts)
    component_records: list[tuple[str, tuple[int, ...], tuple[int, ...]]] = []

    for component in report.components:
        if component.kind == CYCLE:
            cycle_scores = tuple(initial_scores[edge] for edge in component.contacts)
            if sum(cycle_scores) != 0:
                raise AssertionError("coherent cycle scores lost incidence-kernel zero sum")
            if any(cycle_scores):
                raise AssertionError("non-positive coherent cycle scores must all be zero")
            component_records.append((CYCLE, component.contacts, (0,) * len(component.contacts)))
            continue

        body_order, edge_order = _path_traversal(state, component)
        substate = ContactNetworkMomentum1D(
            masses=tuple(state.masses[body] for body in body_order),
            momenta=tuple(state.momenta[body] for body in body_order),
            contacts=tuple(
                # Traversal is already aligned with the original incidence signs.
                # Canonical local labels therefore preserve each contact score.
                __import__(
                    "enterprise_math.material_contact_network_impulse_1d",
                    fromlist=["ContactChannel1D"],
                ).ContactChannel1D(index, index + 1, 1)
                for index in range(len(edge_order))
            ),
        )
        local_scores = contact_relative_scores(substate)
        original_scores = tuple(initial_scores[edge] for edge in edge_order)
        if local_scores != original_scores:
            raise AssertionError("path relabeling changed contact-score orientation")
        local = solve_weighted_chain_least_action(substate)
        for edge, impulse in zip(edge_order, local.impulse_vector):
            global_impulses[edge] = impulse
        component_records.append((PATH, edge_order, local.impulse_vector))

    step = apply_contact_impulse_vector(state, tuple(global_impulses))
    if any(score < 0 for score in step.relative_scores_after):
        raise AssertionError("Z-contact least-action decomposition left a closing contact")
    return ZContactLeastActionSolution1D(
        before=state,
        impulse_vector=tuple(global_impulses),
        final_scores=step.relative_scores_after,
        final_momenta=step.after.momenta,
        component_solutions=tuple(component_records),
    )
