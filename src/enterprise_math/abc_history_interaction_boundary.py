"""Adaptive Ferrers compression of the Stage102 mixed history block.

Candidate thresholds already reached by the old orbit force all future mixed
corner bits to one. Only the unresolved candidate-threshold suffix can carry new
second-order information. That unresolved mixed block is itself Ferrers and is
represented exactly by a monotone crossing/rank boundary.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb
from typing import Sequence


@dataclass(frozen=True)
class InteractionBoundary:
    old_max_value: Fraction
    candidate_thresholds: tuple[Fraction, ...]
    future_values: tuple[Fraction, ...]
    resolved_candidate_count: int
    unresolved_candidate_count: int
    unresolved_thresholds: tuple[Fraction, ...]
    unresolved_crossing_depths: tuple[int | None, ...]
    future_unresolved_ranks: tuple[int, ...]
    unresolved_corner_matrix: tuple[tuple[int, ...], ...]
    compatible_interaction_state_count: int
    unconstrained_interaction_state_count: int


def _validate(
    old_max_value: Fraction,
    candidate_thresholds: Sequence[Fraction],
    future_values: Sequence[Fraction],
) -> None:
    if not isinstance(old_max_value, Fraction):
        raise ValueError("old_max_value must be a Fraction")
    if any(not isinstance(value, Fraction) for value in (*candidate_thresholds, *future_values)):
        raise ValueError("thresholds and values must be Fractions")
    if any(value <= 0 for value in candidate_thresholds):
        raise ValueError("candidate thresholds must be positive")
    if any(candidate_thresholds[i] >= candidate_thresholds[i + 1] for i in range(len(candidate_thresholds) - 1)):
        raise ValueError("candidate thresholds must be strictly increasing")
    if any(future_values[i] > future_values[i + 1] for i in range(len(future_values) - 1)):
        raise ValueError("future values must be nondecreasing")
    if future_values and future_values[0] < old_max_value:
        raise ValueError("future values must extend the old maximum")


def interaction_boundary(
    old_max_value: Fraction,
    candidate_thresholds: Sequence[Fraction],
    future_values: Sequence[Fraction],
) -> InteractionBoundary:
    """Return the exact unresolved mixed-interaction Ferrers boundary."""
    _validate(old_max_value, candidate_thresholds, future_values)
    candidates = tuple(candidate_thresholds)
    futures = tuple(future_values)
    resolved = sum(threshold <= old_max_value for threshold in candidates)
    unresolved_thresholds = candidates[resolved:]
    u = len(unresolved_thresholds)
    b = len(futures)

    matrix = tuple(
        tuple(int(value >= threshold) for value in futures)
        for threshold in unresolved_thresholds
    )
    crossings = tuple(
        next((j for j, bit in enumerate(row) if bit), None)
        for row in matrix
    )
    ranks = tuple(
        sum(value >= threshold for threshold in unresolved_thresholds)
        for value in futures
    )

    encoded_crossings = tuple(b if depth is None else depth for depth in crossings)
    if any(encoded_crossings[i] > encoded_crossings[i + 1] for i in range(len(encoded_crossings) - 1)):
        raise AssertionError("unresolved crossing depths are not monotone")
    if any(ranks[i] > ranks[i + 1] for i in range(len(ranks) - 1)):
        raise AssertionError("future unresolved ranks are not monotone")

    return InteractionBoundary(
        old_max_value=old_max_value,
        candidate_thresholds=candidates,
        future_values=futures,
        resolved_candidate_count=resolved,
        unresolved_candidate_count=u,
        unresolved_thresholds=unresolved_thresholds,
        unresolved_crossing_depths=crossings,
        future_unresolved_ranks=ranks,
        unresolved_corner_matrix=matrix,
        compatible_interaction_state_count=comb(u + b, u),
        unconstrained_interaction_state_count=1 << (u * b),
    )


def reconstruct_unresolved_matrix(
    future_count: int,
    crossing_depths: Sequence[int | None],
) -> tuple[tuple[int, ...], ...]:
    """Reconstruct the unresolved Ferrers block from row crossings."""
    if isinstance(future_count, bool) or not isinstance(future_count, int) or future_count < 0:
        raise ValueError("future_count must be a non-negative integer")
    encoded = tuple(future_count if depth is None else depth for depth in crossing_depths)
    if any(depth < 0 or depth > future_count for depth in encoded):
        raise ValueError("crossing depth out of range")
    if any(encoded[i] > encoded[i + 1] for i in range(len(encoded) - 1)):
        raise ValueError("crossing depths must be weakly increasing")
    return tuple(
        tuple(int(depth < future_count and j >= depth) for j in range(future_count))
        for depth in encoded
    )


def crossings_from_future_ranks(
    unresolved_count: int,
    future_ranks: Sequence[int],
) -> tuple[int | None, ...]:
    """Dual reconstruction: future ranks -> unresolved threshold crossings."""
    if isinstance(unresolved_count, bool) or not isinstance(unresolved_count, int) or unresolved_count < 0:
        raise ValueError("unresolved_count must be a non-negative integer")
    if any(isinstance(rank, bool) or not isinstance(rank, int) or not 0 <= rank <= unresolved_count for rank in future_ranks):
        raise ValueError("future ranks out of range")
    if any(future_ranks[i] > future_ranks[i + 1] for i in range(len(future_ranks) - 1)):
        raise ValueError("future ranks must be weakly increasing")
    crossings: list[int | None] = []
    for threshold_index in range(unresolved_count):
        target_rank = threshold_index + 1
        depth = next((j for j, rank in enumerate(future_ranks) if rank >= target_rank), None)
        crossings.append(depth)
    return tuple(crossings)


def full_corner_matrix(boundary: InteractionBoundary) -> tuple[tuple[int, ...], ...]:
    """Restore forced resolved rows followed by the unresolved Ferrers block."""
    forced = (tuple(1 for _ in boundary.future_values),) * boundary.resolved_candidate_count
    return (*forced, *boundary.unresolved_corner_matrix)
