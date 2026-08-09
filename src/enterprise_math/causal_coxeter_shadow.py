"""Coxeter-number formulas as shadows of primitive causal direction-link density.

This file deliberately does not use the Coxeter number as an ontology primitive.
For a regular primitive-direction link with even degree k, define the integer
causal relation-density coordinate

    h_causal = 2 + k/2.

For irreducible simply-laced crystallographic root systems A,D,E, classical root
system formulas give

    |Phi| = rank * h,
    link_degree = 2(h-2),
    edge-common-neighbor graph degree = h-3.

Hence h_causal equals the traditional Coxeter number in this regime.  The
classical formulas are prior mathematics; the project-specific point is the
causal ordering: primitive relation data are primary and h is a compressed
shadow coordinate.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SimplyLacedShadowProfile:
    family: str
    rank: int
    coxeter_shadow: int
    primitive_direction_count: int
    direction_link_degree: int
    edge_common_neighbor_count: int
    edge_common_graph_degree: int
    edge_common_graph_edge_count: int


def causal_h_from_link_degree(link_degree: int) -> int:
    if (
        isinstance(link_degree, bool)
        or not isinstance(link_degree, int)
        or link_degree < 0
        or link_degree % 2 != 0
    ):
        raise ValueError("simply-laced causal link degree must be a non-negative even integer")
    return 2 + link_degree // 2


def _profile(family: str, rank: int, h: int) -> SimplyLacedShadowProfile:
    link_degree = 2 * (h - 2)
    common = link_degree
    common_degree = h - 3
    return SimplyLacedShadowProfile(
        family=family,
        rank=rank,
        coxeter_shadow=h,
        primitive_direction_count=rank * h,
        direction_link_degree=link_degree,
        edge_common_neighbor_count=common,
        edge_common_graph_degree=common_degree,
        edge_common_graph_edge_count=common * common_degree // 2,
    )


def a_shadow_profile(rank: int) -> SimplyLacedShadowProfile:
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 1:
        raise ValueError("A rank must be positive")
    return _profile("A", rank, rank + 1)


def d_shadow_profile(rank: int) -> SimplyLacedShadowProfile:
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 4:
        raise ValueError("irreducible D rank must be at least four")
    return _profile("D", rank, 2 * rank - 2)


def exceptional_shadow_profile(family: str) -> SimplyLacedShadowProfile:
    data = {
        "E6": (6, 12),
        "E7": (7, 18),
        "E8": (8, 30),
    }
    if family not in data:
        raise ValueError("family must be E6, E7, or E8")
    rank, h = data[family]
    return _profile(family, rank, h)


def a_has_lower_local_relation_load_than_d(rank: int) -> bool:
    if rank < 4:
        raise ValueError("comparison requires rank at least four")
    a = a_shadow_profile(rank)
    d = d_shadow_profile(rank)
    return (
        a.primitive_direction_count < d.primitive_direction_count
        and a.direction_link_degree < d.direction_link_degree
    )


def a_is_minimum_ade_shadow_at_rank(rank: int) -> bool:
    a = a_shadow_profile(rank)
    competitors = []
    if rank >= 4:
        competitors.append(d_shadow_profile(rank))
    if rank == 6:
        competitors.append(exceptional_shadow_profile("E6"))
    elif rank == 7:
        competitors.append(exceptional_shadow_profile("E7"))
    elif rank == 8:
        competitors.append(exceptional_shadow_profile("E8"))
    return all(
        a.primitive_direction_count < other.primitive_direction_count
        and a.direction_link_degree < other.direction_link_degree
        for other in competitors
    )
