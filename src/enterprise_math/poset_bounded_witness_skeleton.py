"""Bounded-arity joint-MAY witness skeletons for finite poset ideal families.

For a nonempty admissible ideal family F and an arity cap k, retain only joint-
MAY queries on label sets S with |S|<=k.  Their semantic signature is the
k-truncation of the full joint-MAY complex.  It is generated exactly by the
inclusion-maximal faces of that truncation.

At k=1 this reduces to pointwise MAY support; as k reaches the ambient size it
recovers the full maximal-witness complex.  Hypergraph/simplicial-complex facts
are standard; this is an executable P025/A4 pressure-test specialization.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .poset_joint_may_complex import maximal_admissible_ideals
from .poset_observation_boundary import Element, Ideal, Relation

Face = frozenset[Element]


@dataclass(frozen=True)
class BoundedWitnessSkeleton:
    arity: int
    faces: frozenset[Face]
    maximal_faces: frozenset[Face]
    may_support: frozenset[Element]


def _validate_arity(arity: int, element_count: int) -> None:
    if isinstance(arity, bool) or not isinstance(arity, int) or arity < 1:
        raise ValueError("arity must be a positive integer")
    if arity > element_count:
        raise ValueError("arity cannot exceed the number of ambient elements")


def bounded_witness_skeleton(
    elements: tuple[Element, ...],
    leq: Relation,
    admissible_ideals: frozenset[Ideal],
    arity: int,
) -> BoundedWitnessSkeleton:
    _validate_arity(arity, len(elements))
    maximals = maximal_admissible_ideals(elements, leq, admissible_ideals)

    faces: set[Face] = set()
    for ideal in maximals:
        ordered = tuple(x for x in elements if x in ideal)
        for size in range(min(arity, len(ordered)) + 1):
            for subset in combinations(ordered, size):
                faces.add(frozenset(subset))

    maximal_faces = frozenset(
        face for face in faces if not any(face < other for other in faces)
    )
    may_support = frozenset(x for face in maximal_faces for x in face)

    # Exact regeneration check.
    regenerated: set[Face] = set()
    for top in maximal_faces:
        ordered = tuple(top)
        for size in range(len(ordered) + 1):
            for subset in combinations(ordered, size):
                regenerated.add(frozenset(subset))
    if regenerated != faces:
        raise AssertionError("maximal truncated faces failed to regenerate the skeleton")

    return BoundedWitnessSkeleton(
        arity=arity,
        faces=frozenset(faces),
        maximal_faces=maximal_faces,
        may_support=may_support,
    )


def jointly_may_up_to_k(skeleton: BoundedWitnessSkeleton, required: Face) -> bool:
    if len(required) > skeleton.arity:
        raise ValueError("required set exceeds the declared arity cap")
    return required in skeleton.faces
