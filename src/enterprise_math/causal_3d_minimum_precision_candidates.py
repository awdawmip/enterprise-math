"""Conditional 3D minimum-precision comparison of SC, BCC, FCC, and ideal HCP.

This module does not claim that physical 3-space is FCC.  It makes a precise
conditional statement inside four standard nearest-neighbor candidate structures.
A candidate passes the current minimum-precision causal contract when:

1. its primitive-direction link is nonempty and connected, so unit directions
   already possess relational context rather than vacuous equality;
2. all primitive directions remain one continuation type through two steps of
   compatible-direction future.

Under this explicit language, FCC passes, simple cubic and BCC fail the first
condition, and ideal HCP splits into two 6-direction types at horizon two.
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
    """Eight nearest directions, scaled to integer cube-corner vectors."""
    return tuple(product((-1, 1), repeat=3))


def fcc_roots() -> tuple[Vector, ...]:
    """A3 root system in a 4-slot zero-sum representation."""
    return a_roots(3)


@dataclass(frozen=True)
class CandidateVerdict:
    name: str
    primitive_count: int
    passes_horizon_two_contract: bool


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
        )
        for name, adjacency in candidates
    )


def unique_passing_candidate() -> str | None:
    passing = [
        verdict.name
        for verdict in three_dimensional_candidate_verdicts()
        if verdict.passes_horizon_two_contract
    ]
    return passing[0] if len(passing) == 1 else None
