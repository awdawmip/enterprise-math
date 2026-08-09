"""Finite causal correspondences and their counting shadows.

A causal relation is represented by explicit witnesses connecting source and
target signature classes.  Two correspondences compose by matching the exact
intermediate signature class.  Counting composite witnesses yields ordinary
nonnegative-integer matrix multiplication as a shadow.

If intermediate signature classes are prematurely collapsed, anonymous matrix
multiplication can create false cross-pairings.  Thus shape-compatible matrices
are not enough: the intermediate quotient must be future-safe for composition.
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
    """Forget exact middle identity in one correspondence by adding multiplicities."""
    result: dict[Edge, int] = defaultdict(int)
    for (left, right), count in counts.items():
        middle = right if middle_is_target else left
        if middle not in middle_to_coarse:
            raise ValueError("middle_to_coarse must define every used middle class")
        coarse = middle_to_coarse[middle]
        edge = (left, coarse) if middle_is_target else (coarse, right)
        result[edge] += count
    return dict(result)
