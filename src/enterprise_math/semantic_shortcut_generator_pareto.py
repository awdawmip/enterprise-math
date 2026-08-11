"""Semantic shortcut-generator Pareto on the Boolean effect semilattice.

Start from the k-bit commuting-idempotent effect algebra under bitwise OR.  The
primitive singleton generators give worst-case target geodesic k.

For a shortcut depth d, promote every nonzero effect mask of Hamming weight at
most d to a primitive semantic generator.  The catalogue size is

    G(k,d)=sum_{i=1}^d C(k,i).

Any target mask T of weight s can be reached in exactly

    ceil(s/d)

shortcut applications:

* lower bound: one primitive contributes at most d target bits;
* upper bound: partition the support of T into chunks of size at most d.

Hence worst-case semantic execution distance is ceil(k/d).

This is a Stage131 shortcut-table Pareto **after** literal syntax has already
been quotiented by the commuting-idempotent algebra.  It should be contrasted
with literal free-word block caching, whose depth-d storage is sum k^i.  Semantic
quotienting before precomputation can therefore change the storage side of the
same shortcut-depth idea from literal-word growth to subset/binomial growth.

The catalogue studied here is canonical but not claimed globally minimum among
all possible shortcut sets achieving a given diameter.  The theorem is exact
inside the declared bounded-support shortcut family.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import comb
from typing import Sequence


def _generator_count(value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError("generator_count must be a positive integer")
    return value


def _shortcut_depth(generator_count: int, depth: int) -> int:
    k = _generator_count(generator_count)
    if isinstance(depth, bool) or not isinstance(depth, int) or not 1 <= depth <= k:
        raise ValueError("shortcut_depth must lie in 1..generator_count")
    return depth


def semantic_shortcut_generator_count(generator_count: int, shortcut_depth: int) -> int:
    k = _generator_count(generator_count)
    d = _shortcut_depth(k, shortcut_depth)
    return sum(comb(k, size) for size in range(1, d + 1))


def shortcut_masks(generator_count: int, shortcut_depth: int) -> tuple[int, ...]:
    k = _generator_count(generator_count)
    d = _shortcut_depth(k, shortcut_depth)
    return tuple(
        mask
        for mask in range(1, 1 << k)
        if mask.bit_count() <= d
    )


def semantic_shortcut_distance(
    target_mask: int,
    generator_count: int,
    shortcut_depth: int,
) -> int:
    k = _generator_count(generator_count)
    d = _shortcut_depth(k, shortcut_depth)
    if isinstance(target_mask, bool) or not isinstance(target_mask, int) or not 0 <= target_mask < (1 << k):
        raise ValueError("target_mask outside semantic effect space")
    support = target_mask.bit_count()
    if support == 0:
        return 0
    return (support + d - 1) // d


def worst_case_semantic_shortcut_distance(generator_count: int, shortcut_depth: int) -> int:
    k = _generator_count(generator_count)
    d = _shortcut_depth(k, shortcut_depth)
    return (k + d - 1) // d


def decompose_target_into_shortcuts(
    target_mask: int,
    generator_count: int,
    shortcut_depth: int,
) -> tuple[int, ...]:
    k = _generator_count(generator_count)
    d = _shortcut_depth(k, shortcut_depth)
    if isinstance(target_mask, bool) or not isinstance(target_mask, int) or not 0 <= target_mask < (1 << k):
        raise ValueError("target_mask outside semantic effect space")
    bits = tuple(index for index in range(k) if target_mask & (1 << index))
    result = []
    for start in range(0, len(bits), d):
        mask = 0
        for bit in bits[start : start + d]:
            mask |= 1 << bit
        if mask:
            result.append(mask)
    if len(result) != semantic_shortcut_distance(target_mask, k, d):
        raise AssertionError("chunk decomposition failed exact geodesic count")
    if result:
        combined = 0
        for mask in result:
            if mask.bit_count() > d:
                raise AssertionError("decomposition used oversized shortcut")
            combined |= mask
        if combined != target_mask:
            raise AssertionError("shortcut decomposition changed target effect")
    elif target_mask != 0:
        raise AssertionError("nonzero target lost shortcut decomposition")
    return tuple(result)


@dataclass(frozen=True)
class SemanticShortcutParetoPoint:
    generator_count: int
    shortcut_depth: int
    primitive_shortcut_count: int
    worst_case_geodesic: int


def semantic_shortcut_pareto_point(
    generator_count: int,
    shortcut_depth: int,
) -> SemanticShortcutParetoPoint:
    k = _generator_count(generator_count)
    d = _shortcut_depth(k, shortcut_depth)
    return SemanticShortcutParetoPoint(
        generator_count=k,
        shortcut_depth=d,
        primitive_shortcut_count=semantic_shortcut_generator_count(k, d),
        worst_case_geodesic=worst_case_semantic_shortcut_distance(k, d),
    )


def shortcut_point_dominates(
    left: SemanticShortcutParetoPoint,
    right: SemanticShortcutParetoPoint,
) -> bool:
    weak = (
        left.primitive_shortcut_count <= right.primitive_shortcut_count
        and left.worst_case_geodesic <= right.worst_case_geodesic
    )
    strict = (
        left.primitive_shortcut_count < right.primitive_shortcut_count
        or left.worst_case_geodesic < right.worst_case_geodesic
    )
    return weak and strict


def semantic_shortcut_pareto_frontier(
    generator_count: int,
) -> tuple[SemanticShortcutParetoPoint, ...]:
    k = _generator_count(generator_count)
    points = tuple(semantic_shortcut_pareto_point(k, depth) for depth in range(1, k + 1))
    return tuple(
        point
        for point in points
        if not any(
            shortcut_point_dominates(other, point)
            for other in points
            if other != point
        )
    )


def minimum_shortcut_depth_for_geodesic_budget(
    generator_count: int,
    geodesic_budget: int,
) -> int:
    k = _generator_count(generator_count)
    if isinstance(geodesic_budget, bool) or not isinstance(geodesic_budget, int) or geodesic_budget < 1:
        raise ValueError("geodesic_budget must be positive")
    effective = min(k, geodesic_budget)
    return (k + effective - 1) // effective


def minimum_canonical_shortcut_storage_for_geodesic_budget(
    generator_count: int,
    geodesic_budget: int,
) -> int:
    depth = minimum_shortcut_depth_for_geodesic_budget(generator_count, geodesic_budget)
    return semantic_shortcut_generator_count(generator_count, depth)


def literal_free_word_cache_entries(generator_count: int, cache_depth: int) -> int:
    k = _generator_count(generator_count)
    if isinstance(cache_depth, bool) or not isinstance(cache_depth, int) or cache_depth < 1:
        raise ValueError("cache_depth must be positive")
    if k == 1:
        return cache_depth
    return k * (k**cache_depth - 1) // (k - 1)


def semantic_to_literal_storage_ratio(
    generator_count: int,
    depth: int,
) -> tuple[int, int]:
    """Return exact (semantic shortcut count, literal free-word cache count)."""
    k = _generator_count(generator_count)
    if depth > k:
        raise ValueError("semantic shortcut depth cannot exceed generator_count")
    return (
        semantic_shortcut_generator_count(k, depth),
        literal_free_word_cache_entries(k, depth),
    )
