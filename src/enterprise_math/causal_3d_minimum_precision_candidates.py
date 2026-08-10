"""Conditional 3D minimum-precision comparison of SC, BCC, FCC, and ideal HCP.

This module does not claim that physical 3-space is FCC.  It makes two precise
conditional statements inside four standard nearest-neighbor candidate structures.

Local-direction contract:
1. primitive-direction link is nonempty and connected;
2. primitive directions remain one continuation type through two compatible-
   relation future steps.

Global one-state reconstruction contract:
1. the first-shell relation graph has a unique graph-theoretic antipode for every
   primitive direction;
2. its simply-laced causal pair matrix has rank three;
3. primitive-adjacent direction differences close back into the primitive set.

Under these explicit languages FCC passes both.  SC/BCC fail relational adequacy.
Ideal HCP has a connected 12-direction first link but splits into two direction
continuation types and, for six out-of-plane directions, has two distance-three
candidates rather than a unique graph antipode.  Thus HCP requires extra
stacking/basis continuation information before a global translation world can be
reconstructed from local first-shell relations alone.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product

from .causal_directional_revelation import minimum_precision_direction_contract
from .causal_primitive_link_profile import (
    a_roots,
    hcp_direction_graph,
    primitive_direction_graph,
)
from .causal_root_lattice_reconstruction import causal_translation_module_summary

Vector = tuple[int, ...]


def simple_cubic_roots() -> tuple[Vector, ...]:
    roots = []
    for axis in range(3):
        for sign in (-1, 1):
            vector = [0, 0, 0]
            vector[axis] = sign
            roots.append(tuple(vector))
    return tuple(roots)


def bcc_roots() -> tuple[Vector, ...]:
    return tuple(product((-1, 1), repeat=3))


def fcc_roots() -> tuple[Vector, ...]:
    return a_roots(3)


def global_one_state_reconstruction_contract(adjacency) -> bool:
    try:
        summary = causal_translation_module_summary(adjacency)
    except ValueError:
        return False
    return (
        summary.translation_rank == 3
        and summary.antipode_relations_verified
        and summary.primitive_difference_relations_verified
    )


@dataclass(frozen=True)
class CandidateVerdict:
    name: str
    primitive_count: int
    passes_horizon_two_contract: bool
    passes_global_one_state_reconstruction: bool


def three_dimensional_candidate_verdicts() -> tuple[CandidateVerdict, ...]:
    candidates = (
        ("SC", primitive_direction_graph(simple_cubic_roots())),
        ("BCC", primitive_direction_graph(bcc_roots())),
        ("FCC", primitive_direction_graph(fcc_roots())),
        ("HCP", hcp_direction_graph()),
    )
    return tuple(
        CandidateVerdict(
            name=name,
            primitive_count=len(adjacency),
            passes_horizon_two_contract=minimum_precision_direction_contract(adjacency, 2),
            passes_global_one_state_reconstruction=global_one_state_reconstruction_contract(adjacency),
        )
        for name, adjacency in candidates
    )


def unique_passing_candidate() -> str | None:
    passing = [
        verdict.name
        for verdict in three_dimensional_candidate_verdicts()
        if verdict.passes_horizon_two_contract
        and verdict.passes_global_one_state_reconstruction
    ]
    return passing[0] if len(passing) == 1 else None
