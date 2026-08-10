"""Generic powerset adjunction induced by any finite relation.

For ``R subset X x Y`` define the existential direct image

    R_exists(A) = {y | exists x in A, x R y}

and the universal residual

    R_forall(B) = {x | every R-successor of x lies in B}.

Then ``R_exists(A) subset B`` iff ``A subset R_forall(B)``.  This is standard
relation/Galois-connection mathematics.  R004 records it mainly as a negative
interpretive boundary: an adjunction that exists for every relation cannot by
itself certify a special Big-Bang/black-hole physical duality.
"""
from __future__ import annotations

from collections.abc import Iterable
from typing import Hashable

State = Hashable
Relation = frozenset[tuple[State, State]]


def existential_image(relation: Relation, subset: Iterable[State]) -> frozenset[State]:
    source_subset = frozenset(subset)
    return frozenset(
        target for source, target in relation if source in source_subset
    )


def universal_residual(
    relation: Relation, sources: Iterable[State], target_subset: Iterable[State]
) -> frozenset[State]:
    source_set = frozenset(sources)
    allowed_targets = frozenset(target_subset)
    return frozenset(
        source
        for source in source_set
        if all(
            target in allowed_targets
            for current_source, target in relation
            if current_source == source
        )
    )


def powerset_adjunction_holds(
    relation: Relation,
    sources: Iterable[State],
    source_subset: Iterable[State],
    target_subset: Iterable[State],
) -> bool:
    source_set = frozenset(sources)
    source_part = frozenset(source_subset)
    if not source_part.issubset(source_set):
        raise ValueError("source_subset must lie in declared sources")
    target_part = frozenset(target_subset)
    return existential_image(relation, source_part).issubset(target_part) == (
        source_part.issubset(universal_residual(relation, source_set, target_part))
    )
