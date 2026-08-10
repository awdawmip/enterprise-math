"""Primitive relation body-order needed to generate a translation kernel.

Given an exact centrally symmetric primitive-move realization, consider only
zero-sum relations made from distinct primitive unit moves with unit coefficients.
For each arity q, collect every subset of at most q primitive directions whose
integer vector sum is zero.  Their row span is a causal local-relation candidate.

The minimum q at which these relations span the full rational kernel of the
primitive-generator realization is the *unit-subset relation arity* for this
specified language.  It measures how many primitive moves must participate at
once before the global translation dimension is fully forced.

This is an audit tool, not a universal definition: some systems may require
repeated directions or non-unit integer coefficients.  In the standard 3D
SC/FCC/BCC primitive shells it cleanly gives 2,3,4 respectively.
"""

from __future__ import annotations

from itertools import combinations

from .causal_primitive_group_presentation import (
    dense_coordinate_rank_mod_prime,
    sparse_rank_mod_prime,
)
from .causal_primitive_link_profile import Vector


def zero_sum_subset_relation_rows(
    primitive_vectors: tuple[Vector, ...],
    maximum_arity: int,
) -> tuple[dict[int, int], ...]:
    if not primitive_vectors:
        raise ValueError("primitive_vectors must be non-empty")
    if (
        isinstance(maximum_arity, bool)
        or not isinstance(maximum_arity, int)
        or maximum_arity < 2
    ):
        raise ValueError("maximum_arity must be at least two")
    dimension = len(primitive_vectors[0])
    if any(len(vector) != dimension for vector in primitive_vectors):
        raise ValueError("primitive vectors must share one realization dimension")

    rows = []
    for arity in range(2, min(maximum_arity, len(primitive_vectors)) + 1):
        for indices in combinations(range(len(primitive_vectors)), arity):
            if all(
                sum(primitive_vectors[index][coordinate] for index in indices) == 0
                for coordinate in range(dimension)
            ):
                rows.append({index: 1 for index in indices})
    return tuple(rows)


def full_translation_kernel_rank(
    primitive_vectors: tuple[Vector, ...],
    prime: int = 1_000_003,
) -> int:
    span_rank = dense_coordinate_rank_mod_prime(primitive_vectors, prime)
    return len(primitive_vectors) - span_rank


def relation_rank_through_arity(
    primitive_vectors: tuple[Vector, ...],
    maximum_arity: int,
    prime: int = 1_000_003,
) -> int:
    rows = zero_sum_subset_relation_rows(primitive_vectors, maximum_arity)
    return sparse_rank_mod_prime(rows, len(primitive_vectors), prime)


def minimum_unit_subset_relation_arity(
    primitive_vectors: tuple[Vector, ...],
    maximum_arity: int,
    prime: int = 1_000_003,
) -> int | None:
    target_rank = full_translation_kernel_rank(primitive_vectors, prime)
    for arity in range(2, maximum_arity + 1):
        if relation_rank_through_arity(primitive_vectors, arity, prime) == target_rank:
            return arity
    return None
