"""Dimension lift as causal refinement of primitive relation types.

Let an old primitive direction family R_old embed into a new family R_new by a
specified injection.  The old operation/observation language is retained, while
new primitive states and new primitive relations become available.  Therefore
old future-equivalence classes may split but must not be forgotten.

This module uses the rooted first-link neighborhood signature as one concrete
finite observation language.  It records:

* old local relation types;
* old types refined by new-dimensional context;
* relation types of genuinely added primitive states;
* a P011-style collision drop measuring old distinctions revealed by the lift.

The rooted-neighborhood language is only one probe family; the causal refinement
construction itself is more general.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from math import comb
from typing import Callable

from .causal_primitive_link_profile import (
    Vector,
    neighborhood_signature,
    primitive_direction_graph,
)

Embedding = Callable[[Vector], Vector]


def _sorted_histogram(counter: Counter) -> tuple[tuple[object, int], ...]:
    return tuple(sorted(counter.items(), key=repr))


def collision_spectrum_from_class_sizes(
    sizes: tuple[int, ...],
    maximum_order: int,
) -> tuple[int, ...]:
    if (
        isinstance(maximum_order, bool)
        or not isinstance(maximum_order, int)
        or maximum_order < 1
    ):
        raise ValueError("maximum_order must be a positive integer")
    return tuple(
        sum(comb(size, order) for size in sizes if size >= order)
        for order in range(1, maximum_order + 1)
    )


@dataclass(frozen=True)
class DimensionLiftProfile:
    old_primitive_count: int
    new_primitive_count: int
    added_primitive_count: int
    old_type_sizes: tuple[int, ...]
    refined_old_type_sizes: tuple[int, ...]
    added_type_sizes: tuple[int, ...]
    dimension_revelation_spectrum: tuple[int, ...]
    old_type_count: int
    refined_old_type_count: int
    added_type_count: int


def dimension_lift_profile(
    old_vectors: tuple[Vector, ...],
    new_vectors: tuple[Vector, ...],
    embedding: Embedding,
    maximum_collision_order: int = 4,
) -> DimensionLiftProfile:
    if not old_vectors or not new_vectors:
        raise ValueError("primitive vector families must be non-empty")
    old_adjacency = primitive_direction_graph(old_vectors)
    new_adjacency = primitive_direction_graph(new_vectors)
    new_set = set(new_vectors)

    lifted = {old: embedding(old) for old in old_vectors}
    if len(set(lifted.values())) != len(old_vectors):
        raise ValueError("embedding must be injective on old primitive vectors")
    if not set(lifted.values()) <= new_set:
        raise ValueError("new primitive family must contain every embedded old vector")

    old_signatures = {
        old: neighborhood_signature(old_adjacency, old)
        for old in old_vectors
    }
    new_signatures = {
        new: neighborhood_signature(new_adjacency, new)
        for new in new_vectors
    }

    old_types = Counter(old_signatures.values())
    # Retaining the old signature in the refined key enforces the causal fact that
    # dimension extension adds future contexts rather than erasing old observables.
    refined_old_types = Counter(
        (old_signatures[old], new_signatures[lifted[old]])
        for old in old_vectors
    )

    lifted_set = set(lifted.values())
    added_types = Counter(
        new_signatures[new]
        for new in new_vectors
        if new not in lifted_set
    )

    old_sizes = tuple(sorted(old_types.values(), reverse=True))
    refined_sizes = tuple(sorted(refined_old_types.values(), reverse=True))
    added_sizes = tuple(sorted(added_types.values(), reverse=True))

    before = collision_spectrum_from_class_sizes(
        old_sizes, maximum_collision_order
    )
    after = collision_spectrum_from_class_sizes(
        refined_sizes, maximum_collision_order
    )
    revelation = tuple(left - right for left, right in zip(before, after))
    if any(value < 0 for value in revelation):
        raise AssertionError("dimension lift cannot merge retained old causal types")

    return DimensionLiftProfile(
        old_primitive_count=len(old_vectors),
        new_primitive_count=len(new_vectors),
        added_primitive_count=len(new_vectors) - len(old_vectors),
        old_type_sizes=old_sizes,
        refined_old_type_sizes=refined_sizes,
        added_type_sizes=added_sizes,
        dimension_revelation_spectrum=revelation,
        old_type_count=len(old_types),
        refined_old_type_count=len(refined_old_types),
        added_type_count=len(added_types),
    )


def coordinate_append_zero(vector: Vector) -> Vector:
    return vector + (0,)
