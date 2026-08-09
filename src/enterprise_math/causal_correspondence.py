"""Finite causal correspondences and their counting shadows.

A causal relation is represented by explicit witnesses connecting source and
target signature classes.  Two correspondences compose by matching the exact
intermediate signature class.  Counting composite witnesses yields ordinary
nonnegative-integer matrix multiplication as a shadow.

If intermediate signature classes are collapsed, two distinct operations must
not be confused:

* incoming witness multiplicities push forward by addition;
* a future transition descends only when all fine middle states in one coarse
  class have the same continuation profile, in which case the coarse transition
  is that common profile once, not the sum of repeated equal profiles.

Blindly aggregating both sides and multiplying can double-count a coarse fiber.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Hashable


State = Hashable
Witness = Hashable
Edge = tuple[State, State]


def witness_multiplicity(witness_edges: dict[Witness, Edge]) -> dict[Edge, int]:
    """Count explicit witnesses over each source-target pair."""
    if not isinstance(witness_edges, dict):
        raise ValueError("witness_edges must be a dict")
    counts: dict[Edge, int] = defaultdict(int)
    for witness, edge in witness_edges.items():
        try:
            hash(witness)
            hash(edge)
        except TypeError as error:
            raise ValueError("witnesses and edge labels must be hashable") from error
        if not isinstance(edge, tuple) or len(edge) != 2:
            raise ValueError("each witness edge must be a source-target pair")
        counts[edge] += 1
    return dict(counts)


def compose_witness_correspondences(
    left: dict[Witness, Edge],
    right: dict[Witness, Edge],
) -> tuple[tuple[Witness, Witness, State, State, State], ...]:
    """All exact witness pairs whose intermediate signature labels match."""
    result: list[tuple[Witness, Witness, State, State, State]] = []
    for left_witness, (source, middle_left) in left.items():
        for right_witness, (middle_right, target) in right.items():
            if middle_left == middle_right:
                result.append(
                    (left_witness, right_witness, source, middle_left, target)
                )
    return tuple(result)


def composite_multiplicity_from_witnesses(
    left: dict[Witness, Edge],
    right: dict[Witness, Edge],
) -> dict[Edge, int]:
    """Count composite witness pairs over each source-target pair."""
    counts: dict[Edge, int] = defaultdict(int)
    for _, _, source, _, target in compose_witness_correspondences(left, right):
        counts[(source, target)] += 1
    return dict(counts)


def matrix_shadow_composition(
    left_counts: dict[Edge, int],
    right_counts: dict[Edge, int],
) -> dict[Edge, int]:
    """Sum-product composition of multiplicity shadows over exact middle labels."""
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in tuple(left_counts.values()) + tuple(right_counts.values())
    ):
        raise ValueError("multiplicities must be non-negative integers")
    result: dict[Edge, int] = defaultdict(int)
    for (source, middle_left), left_count in left_counts.items():
        for (middle_right, target), right_count in right_counts.items():
            if middle_left == middle_right:
                result[(source, target)] += left_count * right_count
    return {edge: count for edge, count in result.items() if count != 0}


def coarse_middle_shadow(
    counts: dict[Edge, int],
    middle_to_coarse: dict[State, State],
    middle_is_target: bool,
) -> dict[Edge, int]:
    """Push multiplicities through a coarse middle label by addition."""
    result: dict[Edge, int] = defaultdict(int)
    for (left, right), count in counts.items():
        middle = right if middle_is_target else left
        if middle not in middle_to_coarse:
            raise ValueError("middle_to_coarse must define every used middle class")
        coarse = middle_to_coarse[middle]
        edge = (left, coarse) if middle_is_target else (coarse, right)
        result[edge] += count
    return dict(result)


def induced_continuation_profile(
    right_counts: dict[Edge, int],
    middle_to_coarse: dict[State, State],
) -> dict[Edge, int]:
    """Descend an outgoing relation through a future-safe middle quotient.

    Every fine middle state in one coarse class must have the same target-count
    profile.  The induced coarse transition stores that common profile once.
    """
    profiles: dict[State, dict[State, int]] = defaultdict(dict)
    used_middles: set[State] = set()
    for (middle, target), count in right_counts.items():
        if isinstance(count, bool) or not isinstance(count, int) or count < 0:
            raise ValueError("multiplicities must be non-negative integers")
        if middle not in middle_to_coarse:
            raise ValueError("middle_to_coarse must define every used middle class")
        used_middles.add(middle)
        if count != 0:
            profiles[middle][target] = count

    coarse_to_middles: dict[State, list[State]] = defaultdict(list)
    for middle in used_middles:
        coarse_to_middles[middle_to_coarse[middle]].append(middle)

    result: dict[Edge, int] = {}
    for coarse, middles in coarse_to_middles.items():
        first_profile = profiles[middles[0]]
        if any(profiles[middle] != first_profile for middle in middles[1:]):
            raise ValueError("middle quotient is not future-safe for this continuation")
        for target, count in first_profile.items():
            result[(coarse, target)] = count
    return result
