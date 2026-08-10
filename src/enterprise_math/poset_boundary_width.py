"""Width and dominance calculus for finite poset observation boundaries.

For a finite observation poset P, every order ideal is represented exactly by
its maximal antichain boundary.  The largest boundary size over all ideals is
exactly width(P).  Monotone ideal paths correspond to dominance-monotone
antichain paths.

These are classical poset facts; this module exposes the exact resource law
needed by the P025 future-precision pressure test.
"""

from __future__ import annotations

from dataclasses import dataclass

from .poset_observation_boundary import (
    Antichain,
    Element,
    Ideal,
    Relation,
    antichain_dominates,
    down_closure,
    enumerate_antichains,
    enumerate_order_ideals,
    maximal_boundary,
)


@dataclass(frozen=True)
class PosetBoundaryWidthReport:
    width: int
    maximum_boundary_size: int
    width_tight: bool
    chain_case: bool
    witness_antichain: Antichain
    witness_ideal: Ideal


def poset_width(elements: tuple[Element, ...], leq: Relation) -> int:
    antichains = enumerate_antichains(elements, leq)
    return max(len(antichain) for antichain in antichains)


def maximum_ideal_boundary_size(elements: tuple[Element, ...], leq: Relation) -> int:
    ideals = enumerate_order_ideals(elements, leq)
    return max(len(maximal_boundary(elements, leq, ideal)) for ideal in ideals)


def analyze_boundary_width(
    elements: tuple[Element, ...], leq: Relation
) -> PosetBoundaryWidthReport:
    antichains = enumerate_antichains(elements, leq)
    width = max(len(antichain) for antichain in antichains)
    witness_antichain = next(
        antichain for antichain in antichains if len(antichain) == width
    )
    witness_ideal = down_closure(elements, leq, witness_antichain)
    boundary_size = maximum_ideal_boundary_size(elements, leq)
    if maximal_boundary(elements, leq, witness_ideal) != witness_antichain:
        raise AssertionError("a maximum antichain must be the boundary of its down-closure")
    if boundary_size != width:
        raise AssertionError("maximum ideal boundary size must equal poset width")
    return PosetBoundaryWidthReport(
        width=width,
        maximum_boundary_size=boundary_size,
        width_tight=True,
        chain_case=(width == 1),
        witness_antichain=witness_antichain,
        witness_ideal=witness_ideal,
    )


def ideal_path_to_boundaries(
    elements: tuple[Element, ...], leq: Relation, ideals: tuple[Ideal, ...]
) -> tuple[Antichain, ...]:
    if not ideals:
        raise ValueError("ideals must be non-empty")
    for ideal in ideals:
        # maximal_boundary validates idealhood.
        maximal_boundary(elements, leq, ideal)
    if any(not left.issubset(right) for left, right in zip(ideals, ideals[1:])):
        raise ValueError("ideal path must be monotone by inclusion")
    boundaries = tuple(maximal_boundary(elements, leq, ideal) for ideal in ideals)
    if any(
        not antichain_dominates(elements, leq, left, right)
        for left, right in zip(boundaries, boundaries[1:])
    ):
        raise AssertionError("monotone ideals must give a dominance-monotone boundary path")
    return boundaries


def boundaries_to_ideal_path(
    elements: tuple[Element, ...], leq: Relation, boundaries: tuple[Antichain, ...]
) -> tuple[Ideal, ...]:
    if not boundaries:
        raise ValueError("boundaries must be non-empty")
    ideals = tuple(down_closure(elements, leq, boundary) for boundary in boundaries)
    if any(not left.issubset(right) for left, right in zip(ideals, ideals[1:])):
        raise ValueError("boundary path must be dominance-monotone")
    return ideals
