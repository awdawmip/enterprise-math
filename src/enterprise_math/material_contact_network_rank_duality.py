"""Rank ledger for E001 contact state redundancy and impulse witness ambiguity.

This module records a standard incidence-linear-algebra consequence of the
Stage-2 contact network.  It is an E001 specialization/diagnostic, not a novelty
claim or a replacement for canonical A3 relation algebra.

For ``N`` bodies, ``E`` declared contact channels and ``c`` connected components,
let ``B`` be the signed body/contact incidence matrix and ``D`` the positive
integer diagonal mass scale.  Then

    r = B^T D p,
    K = B^T D B,
    beta = E - N + c.

Over the rational span,

    rank(B) = rank(B^T D) = rank(K) = N-c,
    nullity(K) = beta.

Thus the same cycle-rank number ``beta`` has two simultaneous meanings:

1. ``E-(N-c)=beta`` contact-score coordinates are redundant at body-state level;
2. ``beta`` independent contact-impulse circulation directions are invisible to
   body momentum updates.

For a connected graph, the independent contact-relative state dimension is
``N-1``, exactly the canonical A3 weighted-relation dimension.  A spanning tree
therefore has the right number of edge relation coordinates; together with the
one total momentum coordinate it can determine the full momentum state on
legal data.  For ``c`` disconnected components, a spanning forest supplies
``N-c`` relation coordinates and one component-total coordinate per component;
using only one global total leaves ``c-1`` component-offset degrees unresolved.

Cyclic declared contact graphs need not be realizable by strict nonoverlapping
hard intervals on a line.  The cycle statements are algebraic contact-network
facts and are relevant only when the world/contact language permits such a
constraint topology (for example a more general or higher-dimensional contact
system).
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_contact_network_cycle_kernel import (
    contact_cycle_rank,
    contact_graph_component_count,
)
from .material_contact_network_impulse_1d import ContactNetworkMomentum1D


@dataclass(frozen=True)
class ContactRankDualityReport:
    body_count: int
    contact_count: int
    component_count: int
    independent_relative_state_rank: int
    contact_score_redundancy: int
    impulse_kernel_dimension: int
    spanning_forest_edge_count: int
    component_total_coordinates_needed: int
    unresolved_component_offsets_with_global_total_only: int

    @property
    def body_coordinate_balance(self) -> int:
        return (
            self.independent_relative_state_rank
            + self.component_total_coordinates_needed
        )

    @property
    def contact_coordinate_balance(self) -> int:
        return (
            self.independent_relative_state_rank
            + self.contact_score_redundancy
        )


def contact_rank_duality_report(
    state: ContactNetworkMomentum1D,
) -> ContactRankDualityReport:
    """Return the exact graph-theoretic dimension ledger for this contact network."""
    body_count = len(state.masses)
    contact_count = len(state.contacts)
    components = contact_graph_component_count(state)
    relative_rank = body_count - components
    cycle_rank = contact_cycle_rank(state)

    if relative_rank + cycle_rank != contact_count:
        raise AssertionError("contact edge rank/nullity balance failed")
    if relative_rank + components != body_count:
        raise AssertionError("body relation/component-total balance failed")

    return ContactRankDualityReport(
        body_count=body_count,
        contact_count=contact_count,
        component_count=components,
        independent_relative_state_rank=relative_rank,
        contact_score_redundancy=cycle_rank,
        impulse_kernel_dimension=cycle_rank,
        spanning_forest_edge_count=relative_rank,
        component_total_coordinates_needed=components,
        unresolved_component_offsets_with_global_total_only=max(0, components - 1),
    )
