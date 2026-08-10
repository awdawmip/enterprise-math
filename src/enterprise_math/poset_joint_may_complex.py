"""Joint-MAY semantics for families of finite poset ideals.

For a nonempty admissible family F of exact ideals, a finite label set S is
jointly MAY iff one admissible ideal contains S.  All such S form a downward-
closed simplicial complex K_F = union_{I in F} 2^I.  Its maximal faces are
exactly the inclusion-maximal admissible ideals, so nonmaximal admissible ideals
are invisible to pure existential joint-MAY queries.

To answer all joint MAY and all joint MUST queries, retain the MUST ideal L as
well: joint MUST(S) iff S subseteq L.  The pair (L, Max(F)) is exact for this
language, but does not recover exact admissible-family identity or witness
counts.
"""

from __future__ import annotations

from dataclasses import dataclass

from .poset_observation_boundary import Element, Ideal, Relation, maximal_boundary


@dataclass(frozen=True)
class JointMayMustState:
    must_ideal: Ideal
    maximal_admissible_ideals: frozenset[Ideal]


def _validate_family(
    elements: tuple[Element, ...], leq: Relation, admissible_ideals: frozenset[Ideal]
) -> None:
    if not admissible_ideals:
        raise ValueError("admissible_ideals must be non-empty")
    for ideal in admissible_ideals:
        maximal_boundary(elements, leq, ideal)


def maximal_admissible_ideals(
    elements: tuple[Element, ...],
    leq: Relation,
    admissible_ideals: frozenset[Ideal],
) -> frozenset[Ideal]:
    _validate_family(elements, leq, admissible_ideals)
    return frozenset(
        ideal
        for ideal in admissible_ideals
        if not any(ideal < other for other in admissible_ideals)
    )


def joint_may_from_maximals(
    maximal_ideals: frozenset[Ideal], required: frozenset[Element]
) -> bool:
    if not maximal_ideals:
        raise ValueError("maximal_ideals must be non-empty")
    return any(required.issubset(ideal) for ideal in maximal_ideals)


def joint_must_from_intersection(must_ideal: Ideal, required: frozenset[Element]) -> bool:
    return required.issubset(must_ideal)


def joint_may_must_state(
    elements: tuple[Element, ...],
    leq: Relation,
    admissible_ideals: frozenset[Ideal],
) -> JointMayMustState:
    _validate_family(elements, leq, admissible_ideals)
    must = frozenset.intersection(*tuple(admissible_ideals))
    maximals = maximal_admissible_ideals(elements, leq, admissible_ideals)
    return JointMayMustState(
        must_ideal=must,
        maximal_admissible_ideals=maximals,
    )


def same_joint_may_must_future(left: JointMayMustState, right: JointMayMustState) -> bool:
    return (
        left.must_ideal == right.must_ideal
        and left.maximal_admissible_ideals == right.maximal_admissible_ideals
    )


def enumerate_joint_may_faces(
    elements: tuple[Element, ...], maximal_ideals: frozenset[Ideal]
) -> frozenset[frozenset[Element]]:
    """Enumerate K_F for finite executable checks only."""
    from itertools import combinations

    faces: set[frozenset[Element]] = set()
    for ideal in maximal_ideals:
        ordered = tuple(x for x in elements if x in ideal)
        for size in range(len(ordered) + 1):
            for subset in combinations(ordered, size):
                faces.add(frozenset(subset))
    return frozenset(faces)
