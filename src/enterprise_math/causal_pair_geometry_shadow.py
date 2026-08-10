"""Pair geometry across causal and traditional Gram observations.

For an equal-norm integral minimal-vector shell, primitive-link adjacency detects
one exact pair relation: v-u is again minimal.  A traditional Gram inner product
may split the non-adjacent remainder into several values, while deeper causal
continuation can also split pairs that have the same inner product.

This module keeps both directions of non-equivalence explicit.  It is intended to
prevent the causal precision hierarchy from being silently identified with an
Euclidean-angle hierarchy.
"""

from __future__ import annotations

from collections import Counter

from .causal_gram_lattice import Gram
from .causal_primitive_link_profile import Vector, primitive_direction_graph


def gram_inner_product(gram: Gram, left: Vector, right: Vector) -> int:
    if len(left) != len(gram) or len(right) != len(gram):
        raise ValueError("vectors must match Gram dimension")
    return sum(
        left[i] * gram[i][j] * right[j]
        for i in range(len(gram))
        for j in range(len(gram))
    )


def negate(vector: Vector) -> Vector:
    return tuple(-value for value in vector)


def primitive_pair_class(
    adjacency,
    left: Vector,
    right: Vector,
) -> str:
    if left == right:
        return "same"
    if left == negate(right):
        return "antipode"
    if right in adjacency[left]:
        return "+adj"
    anti = negate(right)
    if anti in adjacency[left]:
        return "-adj"
    return "other"


def causal_class_inner_product_histogram(
    gram: Gram,
    vectors: tuple[Vector, ...],
) -> dict[str, dict[int, int]]:
    adjacency = primitive_direction_graph(vectors)
    result: dict[str, Counter] = {}
    for index, left in enumerate(vectors):
        for right in vectors[index:]:
            causal_class = primitive_pair_class(adjacency, left, right)
            result.setdefault(causal_class, Counter())[
                gram_inner_product(gram, left, right)
            ] += 1
    return {
        causal_class: dict(sorted(histogram.items()))
        for causal_class, histogram in result.items()
    }


def adjacent_pair_extension_histogram(
    vectors: tuple[Vector, ...],
) -> dict[int, int]:
    """How deeper causal context splits primitive-adjacent pairs."""
    adjacency = primitive_direction_graph(vectors)
    seen = set()
    histogram = Counter()
    for left in vectors:
        for right in adjacency[left]:
            edge = tuple(sorted((left, right)))
            if edge in seen:
                continue
            seen.add(edge)
            histogram[len(adjacency[left].intersection(adjacency[right]))] += 1
    return dict(sorted(histogram.items()))


def pair_angle_shadow_is_complete(
    gram: Gram,
    vectors: tuple[Vector, ...],
) -> bool:
    """True iff every primitive causal pair class has one Gram inner-product value."""
    return all(
        len(histogram) == 1
        for histogram in causal_class_inner_product_histogram(gram, vectors).values()
    )
