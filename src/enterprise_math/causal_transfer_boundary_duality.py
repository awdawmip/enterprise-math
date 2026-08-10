"""Discrete primal/dual certificates for directional relation boundaries.

For a connected transfer graph, x is in the positive directional cut of the
radius-r word ball along primitive move b_e iff there exists an integer
unit-response potential phi such that

    <phi,x> = r
    <phi,b_e> = 1.

Proof: x+b_e has word norm r+1.  Integer transfer-response duality gives a
potential attaining r+1 on x+b_e.  Since separately <phi,x><=r and
<phi,b_e><=1, both inequalities must saturate.  Conversely saturation gives a
dual lower bound r+1 on x+b_e, while one primitive step gives the matching upper
bound.

Thus a primitive relation controls two different dual constructions:
- boundary orientation: response facet <phi,b_e>=1;
- relation contraction: response section <phi,b_e>=0.

This is a discrete supporting-probe certificate, not a continuous normal-vector
ontology.
"""

from __future__ import annotations

from .causal_transfer_boundary_contraction import (
    directional_cut_states,
    oriented_edge_vector,
    word_ball,
)
from .causal_transfer_duality import (
    dual_response_value,
    integer_unit_response_potentials,
    primal_transfer_distance,
)
from .causal_transfer_graph_geometry import Edge, Vector


def directional_boundary_probe_witnesses(
    slot_count: int,
    edges: tuple[Edge, ...],
    oriented_edge: Edge,
    radius: int,
    state: Vector,
) -> tuple[Vector, ...]:
    """All anchored integer unit-response probes certifying one cut state."""
    cut = directional_cut_states(slot_count, edges, oriented_edge, radius)
    if state not in cut:
        return ()
    move = oriented_edge_vector(slot_count, oriented_edge)
    witnesses = []
    for potential in integer_unit_response_potentials(slot_count, edges, anchor=0):
        if dual_response_value(state, potential) != radius:
            continue
        if dual_response_value(move, potential) != 1:
            continue
        witnesses.append(potential)
    return tuple(witnesses)


def directional_boundary_probe_certificate_holds(
    slot_count: int,
    edges: tuple[Edge, ...],
    oriented_edge: Edge,
    radius: int,
    state: Vector,
) -> bool:
    in_cut = state in directional_cut_states(slot_count, edges, oriented_edge, radius)
    has_witness = bool(
        directional_boundary_probe_witnesses(
            slot_count, edges, oriented_edge, radius, state
        )
    )
    return in_cut == has_witness


def witness_forces_next_radius(
    state: Vector,
    potential: Vector,
    slot_count: int,
    edges: tuple[Edge, ...],
    oriented_edge: Edge,
    radius: int,
) -> bool:
    move = oriented_edge_vector(slot_count, oriented_edge)
    if dual_response_value(state, potential) != radius:
        return False
    if dual_response_value(move, potential) != 1:
        return False
    next_state = tuple(value + shift for value, shift in zip(state, move))
    return primal_transfer_distance(next_state, edges) == radius + 1


def all_cut_states_have_supporting_probes(
    slot_count: int,
    edges: tuple[Edge, ...],
    oriented_edge: Edge,
    radius: int,
) -> bool:
    return all(
        directional_boundary_probe_witnesses(
            slot_count, edges, oriented_edge, radius, state
        )
        for state in directional_cut_states(slot_count, edges, oriented_edge, radius)
    )


def boundary_probe_partition(
    slot_count: int,
    edges: tuple[Edge, ...],
    oriented_edge: Edge,
    radius: int,
) -> dict[Vector, tuple[Vector, ...]]:
    """Classify cut states by the full set of supporting unit-response probes."""
    return {
        state: directional_boundary_probe_witnesses(
            slot_count, edges, oriented_edge, radius, state
        )
        for state in directional_cut_states(slot_count, edges, oriented_edge, radius)
    }
