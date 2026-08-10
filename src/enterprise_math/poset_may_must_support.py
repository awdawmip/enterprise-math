"""MAY/MUST support for nonempty families of finite poset ideals.

A coarse state may admit several exact ideal states.  Pointwise membership then
splits into MUST (present in every admissible ideal) and MAY (present in at
least one).  The intersection L and union U of the family are again order
ideals, and the nested pair L subseteq U is exact for all pointwise MAY/MUST
queries.  It does not determine joint/correlation queries between labels.

This is elementary lattice/set theory and an A4-facing specialization; no
generic novelty claim is made.
"""

from __future__ import annotations

from dataclasses import dataclass

from .poset_observation_boundary import (
    Antichain,
    Element,
    Ideal,
    Relation,
    maximal_boundary,
)


@dataclass(frozen=True)
class MayMustSupportState:
    must_ideal: Ideal
    may_ideal: Ideal
    must_boundary: Antichain
    may_boundary: Antichain



def may_must_support(
    elements: tuple[Element, ...],
    leq: Relation,
    admissible_ideals: frozenset[Ideal],
) -> MayMustSupportState:
    if not admissible_ideals:
        raise ValueError("admissible_ideals must be non-empty")
    validated: list[Ideal] = []
    for ideal in admissible_ideals:
        maximal_boundary(elements, leq, ideal)  # validates idealhood
        validated.append(ideal)

    must = frozenset.intersection(*validated)
    may = frozenset.union(*validated)
    if not must.issubset(may):
        raise AssertionError("MUST support must be contained in MAY support")
    # Intersections and unions of ideals are ideals; validation makes this executable.
    must_boundary = maximal_boundary(elements, leq, must)
    may_boundary = maximal_boundary(elements, leq, may)
    return MayMustSupportState(
        must_ideal=must,
        may_ideal=may,
        must_boundary=must_boundary,
        may_boundary=may_boundary,
    )


def pointwise_status(state: MayMustSupportState, element: Element) -> str:
    if element in state.must_ideal:
        return "MUST"
    if element in state.may_ideal:
        return "MAY"
    return "IMPOSSIBLE"


def same_pointwise_future(
    left: MayMustSupportState, right: MayMustSupportState
) -> bool:
    return (
        left.must_ideal == right.must_ideal
        and left.may_ideal == right.may_ideal
    )


def joint_may(admissible_ideals: frozenset[Ideal], required: frozenset[Element]) -> bool:
    """Whether one admissible exact ideal contains all required labels at once."""
    if not admissible_ideals:
        raise ValueError("admissible_ideals must be non-empty")
    return any(required.issubset(ideal) for ideal in admissible_ideals)
