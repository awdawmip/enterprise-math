"""Primitive causal-link profiles for simply-laced ADE root systems.

This module treats the classical ADE root data as a pressure-test family for
minimum-precision relation geometry.  The project-level primitive is the local
relation graph, not the Coxeter number itself.

For an irreducible simply-laced root system of rank ``r`` and Coxeter number
``h``, the root-direction graph has the following uniform local counts:

* primitive directions: ``r*h``;
* neighbors of one primitive direction: ``2*(h-2)``;
* common-neighbor vertices around one primitive edge: ``2*(h-2)``;
* the induced common-neighbor graph is ``(h-3)``-regular;
* hence it has ``(h-2)*(h-3)`` internal edges.

Thus ``h`` can be recovered from the primitive causal relation graph as
``2 + degree/2``.  In this use, Coxeter number is a traditional coordinate
shadow of local causal branching, not an assumed geometric primitive.

The formulas are standard root-system data specialized to the project's
relation-link observation.  The project does not claim the ADE classification,
Coxeter-number identities, or classical sphere-packing results as original.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RootSystemProfile:
    family: str
    rank: int
    coxeter_number: int
    primitive_directions: int
    direction_link_degree: int
    edge_context_vertices: int
    edge_context_degree: int
    edge_context_edges: int


def _require_rank(rank: int) -> None:
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 1:
        raise ValueError("rank must be a positive integer")


def profile_from_rank_and_coxeter(
    family: str,
    rank: int,
    coxeter_number: int,
) -> RootSystemProfile:
    _require_rank(rank)
    if (
        isinstance(coxeter_number, bool)
        or not isinstance(coxeter_number, int)
        or coxeter_number < 2
    ):
        raise ValueError("coxeter_number must be an integer at least two")
    link_degree = 2 * (coxeter_number - 2)
    context_degree = coxeter_number - 3
    return RootSystemProfile(
        family=family,
        rank=rank,
        coxeter_number=coxeter_number,
        primitive_directions=rank * coxeter_number,
        direction_link_degree=link_degree,
        edge_context_vertices=link_degree,
        edge_context_degree=context_degree,
        edge_context_edges=(coxeter_number - 2) * (coxeter_number - 3),
    )


def a_profile(rank: int) -> RootSystemProfile:
    _require_rank(rank)
    return profile_from_rank_and_coxeter(f"A_{rank}", rank, rank + 1)


def d_profile(rank: int) -> RootSystemProfile:
    _require_rank(rank)
    if rank < 4:
        raise ValueError("D_n is irreducible in this family for rank at least four")
    return profile_from_rank_and_coxeter(f"D_{rank}", rank, 2 * rank - 2)


def e_profile(rank: int) -> RootSystemProfile:
    if rank == 6:
        return profile_from_rank_and_coxeter("E_6", 6, 12)
    if rank == 7:
        return profile_from_rank_and_coxeter("E_7", 7, 18)
    if rank == 8:
        return profile_from_rank_and_coxeter("E_8", 8, 30)
    raise ValueError("exceptional simply-laced E family exists here only at ranks 6, 7, 8")


def causal_branching_number(profile: RootSystemProfile) -> int:
    """Recover the Coxeter-number shadow from primitive direction branching."""
    degree = profile.direction_link_degree
    if degree % 2:
        raise ValueError("simply-laced profile must have even direction-link degree")
    return 2 + degree // 2


def simply_laced_candidates(rank: int) -> tuple[RootSystemProfile, ...]:
    """Return irreducible ADE pressure-test candidates available at ``rank``."""
    _require_rank(rank)
    result = [a_profile(rank)]
    if rank >= 4:
        result.append(d_profile(rank))
    if rank in (6, 7, 8):
        result.append(e_profile(rank))
    return tuple(result)


def richest_primitive_relation_candidates(rank: int) -> tuple[RootSystemProfile, ...]:
    """Maximize primitive direction count within the ADE pressure-test family.

    This is intentionally only a first competition gate.  It is not a theorem
    that the maximizing family is the physical or unique minimum-precision
    geometry; higher contextual, global, dynamical, and future-language tests
    remain necessary.
    """
    candidates = simply_laced_candidates(rank)
    best = max(candidate.primitive_directions for candidate in candidates)
    return tuple(
        candidate for candidate in candidates if candidate.primitive_directions == best
    )


def low_rank_richest_sequence(
    start_rank: int = 2,
    end_rank: int = 8,
) -> tuple[tuple[int, tuple[str, ...], int], ...]:
    if start_rank > end_rank:
        raise ValueError("start_rank must not exceed end_rank")
    output = []
    for rank in range(start_rank, end_rank + 1):
        winners = richest_primitive_relation_candidates(rank)
        output.append(
            (
                rank,
                tuple(profile.family for profile in winners),
                winners[0].primitive_directions,
            )
        )
    return tuple(output)
