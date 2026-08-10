"""Full labelled merged-rank path as a common incidence generator.

Stage104 used a response-specific compressed generator for activation area.
Stage109 keeps one merged rank for every current and future node relative to the
labelled union of old and candidate thresholds.  This monotone path reconstructs
the complete incidence geometry and therefore generates both linear area and
quadratic rank-energy responses, including the Stage108 cubic action jet.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb
from typing import Sequence

from .abc_merged_threshold_history import MergedThresholdLabel


@dataclass(frozen=True)
class MergedRankPath:
    merged_labels: tuple[MergedThresholdLabel, ...]
    current_node_count: int
    future_node_count: int
    current_ranks: tuple[int, ...]
    future_ranks: tuple[int, ...]
    full_rank_path: tuple[int, ...]
    compatible_path_count: int
    unconstrained_incidence_count: int


def _validate(
    thresholds: Sequence[Fraction],
    current_values: Sequence[Fraction],
    candidate_thresholds: Sequence[Fraction],
    future_values: Sequence[Fraction],
) -> None:
    if not current_values:
        raise ValueError("current_values must be non-empty")
    if any(not isinstance(value, Fraction) for value in (*thresholds, *current_values, *candidate_thresholds, *future_values)):
        raise ValueError("thresholds and values must be Fractions")
    if any(value <= 0 for value in (*thresholds, *candidate_thresholds)):
        raise ValueError("thresholds must be positive")
    if any(thresholds[i] >= thresholds[i + 1] for i in range(len(thresholds) - 1)):
        raise ValueError("old thresholds must be strictly increasing")
    if any(candidate_thresholds[i] >= candidate_thresholds[i + 1] for i in range(len(candidate_thresholds) - 1)):
        raise ValueError("candidate thresholds must be strictly increasing")
    if set(thresholds).intersection(candidate_thresholds):
        raise ValueError("candidate thresholds must be new")
    if any(current_values[i] > current_values[i + 1] for i in range(len(current_values) - 1)):
        raise ValueError("current values must be nondecreasing")
    if any(future_values[i] > future_values[i + 1] for i in range(len(future_values) - 1)):
        raise ValueError("future values must be nondecreasing")
    if future_values and future_values[0] < current_values[-1]:
        raise ValueError("future values must extend the current path")


def _labels(
    thresholds: Sequence[Fraction], candidate_thresholds: Sequence[Fraction]
) -> tuple[MergedThresholdLabel, ...]:
    labels = [
        *(MergedThresholdLabel(value, "old", i) for i, value in enumerate(thresholds)),
        *(MergedThresholdLabel(value, "candidate", i) for i, value in enumerate(candidate_thresholds)),
    ]
    return tuple(sorted(labels, key=lambda item: item.value))


def merged_rank_path(
    thresholds: Sequence[Fraction],
    current_values: Sequence[Fraction],
    candidate_thresholds: Sequence[Fraction],
    future_values: Sequence[Fraction],
) -> MergedRankPath:
    _validate(thresholds, current_values, candidate_thresholds, future_values)
    labels = _labels(thresholds, candidate_thresholds)
    all_values = (*current_values, *future_values)
    ranks = tuple(sum(label.value <= value for label in labels) for value in all_values)
    if any(ranks[i] > ranks[i + 1] for i in range(len(ranks) - 1)):
        raise AssertionError("merged rank path must be nondecreasing")
    n_current = len(current_values)
    m = len(labels)
    n = len(all_values)
    return MergedRankPath(
        merged_labels=labels,
        current_node_count=n_current,
        future_node_count=len(future_values),
        current_ranks=ranks[:n_current],
        future_ranks=ranks[n_current:],
        full_rank_path=ranks,
        compatible_path_count=comb(m + n, n),
        unconstrained_incidence_count=1 << (m * n),
    )


def _active_selected_rank(
    path: MergedRankPath,
    merged_rank: int,
    selected_candidates: set[int],
) -> int:
    active = path.merged_labels[:merged_rank]
    return sum(
        label.family == "old"
        or (label.family == "candidate" and label.family_index in selected_candidates)
        for label in active
    )


def area_from_merged_rank_path(
    path: MergedRankPath,
    threshold_selection: Sequence[int],
    future_selection: Sequence[int],
) -> int:
    """Evaluate activation area from the common incidence generator."""
    candidate_count = sum(label.family == "candidate" for label in path.merged_labels)
    if len(threshold_selection) != candidate_count:
        raise ValueError("threshold selection has wrong length")
    if len(future_selection) != path.future_node_count:
        raise ValueError("future selection has wrong length")
    if any(bit not in (0, 1) for bit in (*threshold_selection, *future_selection)):
        raise ValueError("selection bits must be 0 or 1")
    selected = {i for i, bit in enumerate(threshold_selection) if bit}
    ranks = [
        _active_selected_rank(path, rank, selected)
        for rank in path.current_ranks
    ]
    ranks.extend(
        _active_selected_rank(path, path.future_ranks[j], selected)
        for j, bit in enumerate(future_selection)
        if bit
    )
    return sum(ranks)


def quadratic_energy_from_merged_rank_path(
    path: MergedRankPath,
    threshold_selection: Sequence[int],
    future_selection: Sequence[int],
) -> int:
    """Evaluate quadratic rank energy from the same common generator."""
    candidate_count = sum(label.family == "candidate" for label in path.merged_labels)
    if len(threshold_selection) != candidate_count:
        raise ValueError("threshold selection has wrong length")
    if len(future_selection) != path.future_node_count:
        raise ValueError("future selection has wrong length")
    if any(bit not in (0, 1) for bit in (*threshold_selection, *future_selection)):
        raise ValueError("selection bits must be 0 or 1")
    selected = {i for i, bit in enumerate(threshold_selection) if bit}
    ranks = [
        _active_selected_rank(path, rank, selected)
        for rank in path.current_ranks
    ]
    ranks.extend(
        _active_selected_rank(path, path.future_ranks[j], selected)
        for j, bit in enumerate(future_selection)
        if bit
    )
    return sum(rank * rank for rank in ranks)
