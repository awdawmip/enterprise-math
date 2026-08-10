"""Merged-threshold generator for Stage102 finite-history responses.

Existing thresholds and candidate thresholds live on one ordered scalar axis.
For each future node, one rank in their labelled merged order reconstructs both:
  * the old-threshold future rank R_j;
  * the full candidate mixed-corner column C_{*,j}.

Thus the expanded first+second-order tensor has a smaller total-order generator.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import comb
from typing import Iterable, Sequence

from .abc_finite_history_closure import finite_history_signature, history_area_from_signature
from .abc_two_step_history import activation_area, threshold_span


@dataclass(frozen=True)
class MergedThresholdLabel:
    value: Fraction
    family: str
    family_index: int


@dataclass(frozen=True)
class MergedThresholdHistorySignature:
    area: int
    candidate_thresholds: tuple[Fraction, ...]
    threshold_spans: tuple[int, ...]
    merged_labels: tuple[MergedThresholdLabel, ...]
    old_max_value: Fraction
    old_max_merged_rank: int
    unresolved_merged_count: int
    future_total_ranks: tuple[int, ...]
    future_rank_state_count: int
    unconstrained_future_rank_tuple_count: int


def _validate(
    thresholds: Sequence[Fraction],
    values: Sequence[Fraction],
    candidate_thresholds: Sequence[Fraction],
    future_values: Sequence[Fraction],
) -> None:
    if not values:
        raise ValueError("current values must be non-empty")
    if any(not isinstance(value, Fraction) for value in (*thresholds, *values, *candidate_thresholds, *future_values)):
        raise ValueError("all thresholds and values must be Fractions")
    if any(value <= 0 for value in (*thresholds, *candidate_thresholds)):
        raise ValueError("thresholds must be positive")
    if any(thresholds[i] >= thresholds[i + 1] for i in range(len(thresholds) - 1)):
        raise ValueError("current thresholds must be strictly increasing")
    if any(candidate_thresholds[i] >= candidate_thresholds[i + 1] for i in range(len(candidate_thresholds) - 1)):
        raise ValueError("candidate thresholds must be strictly increasing")
    if set(thresholds).intersection(candidate_thresholds):
        raise ValueError("candidate thresholds must be distinct from current thresholds")
    if any(values[i] > values[i + 1] for i in range(len(values) - 1)):
        raise ValueError("current values must be nondecreasing")
    if any(future_values[i] > future_values[i + 1] for i in range(len(future_values) - 1)):
        raise ValueError("future values must be nondecreasing")
    if future_values and future_values[0] < values[-1]:
        raise ValueError("future values must extend the current orbit")


def _merged_labels(
    thresholds: Sequence[Fraction], candidate_thresholds: Sequence[Fraction]
) -> tuple[MergedThresholdLabel, ...]:
    labels = [
        *(MergedThresholdLabel(value, "old", index) for index, value in enumerate(thresholds)),
        *(MergedThresholdLabel(value, "candidate", index) for index, value in enumerate(candidate_thresholds)),
    ]
    return tuple(sorted(labels, key=lambda label: label.value))


def merged_threshold_history_signature(
    thresholds: Sequence[Fraction],
    values: Sequence[Fraction],
    candidate_thresholds: Sequence[Fraction],
    future_values: Sequence[Fraction],
) -> MergedThresholdHistorySignature:
    """Compile candidate old-spans plus one labelled merged rank per future node."""
    _validate(thresholds, values, candidate_thresholds, future_values)
    labels = _merged_labels(thresholds, candidate_thresholds)
    old_max = values[-1]
    base_rank = sum(label.value <= old_max for label in labels)
    total_ranks = tuple(
        sum(label.value <= value for label in labels)
        for value in future_values
    )
    if any(total_ranks[i] > total_ranks[i + 1] for i in range(len(total_ranks) - 1)):
        raise AssertionError("future merged ranks are not nondecreasing")
    if any(rank < base_rank for rank in total_ranks):
        raise AssertionError("future merged rank fell below old maximum rank")

    unresolved = len(labels) - base_rank
    b = len(future_values)
    return MergedThresholdHistorySignature(
        area=activation_area(thresholds, values),
        candidate_thresholds=tuple(candidate_thresholds),
        threshold_spans=tuple(threshold_span(values, threshold) for threshold in candidate_thresholds),
        merged_labels=labels,
        old_max_value=old_max,
        old_max_merged_rank=base_rank,
        unresolved_merged_count=unresolved,
        future_total_ranks=total_ranks,
        future_rank_state_count=comb(unresolved + b, b),
        unconstrained_future_rank_tuple_count=(unresolved + 1) ** b,
    )


def _prefix_labels(
    signature: MergedThresholdHistorySignature, total_rank: int
) -> tuple[MergedThresholdLabel, ...]:
    if isinstance(total_rank, bool) or not isinstance(total_rank, int):
        raise ValueError("total_rank must be an integer")
    if not 0 <= total_rank <= len(signature.merged_labels):
        raise ValueError("total_rank out of range")
    return signature.merged_labels[:total_rank]


def decode_future_column(
    signature: MergedThresholdHistorySignature, future_index: int
) -> dict[str, object]:
    """Decode one Stage102 `(R_j, C_{*,j})` column from a merged rank."""
    if not 0 <= future_index < len(signature.future_total_ranks):
        raise ValueError("future_index out of range")
    labels = _prefix_labels(signature, signature.future_total_ranks[future_index])
    old_rank = sum(label.family == "old" for label in labels)
    crossed_candidates = {
        label.family_index for label in labels if label.family == "candidate"
    }
    corners = tuple(
        int(index in crossed_candidates)
        for index in range(len(signature.candidate_thresholds))
    )
    return {
        "old_threshold_rank": old_rank,
        "candidate_corner_column": corners,
    }


def history_area_from_merged_signature(
    signature: MergedThresholdHistorySignature,
    selected_threshold_indices: Iterable[int],
    future_prefix_length: int,
) -> int:
    """Predict every finite history area without storing an explicit corner matrix."""
    selected = tuple(sorted(set(selected_threshold_indices)))
    a = len(signature.candidate_thresholds)
    b = len(signature.future_total_ranks)
    if any(index < 0 or index >= a for index in selected):
        raise ValueError("selected threshold index out of range")
    if isinstance(future_prefix_length, bool) or not isinstance(future_prefix_length, int):
        raise ValueError("future_prefix_length must be an integer")
    if not 0 <= future_prefix_length <= b:
        raise ValueError("future_prefix_length out of range")

    selected_set = set(selected)
    result = signature.area + sum(signature.threshold_spans[i] for i in selected)
    for future_index in range(future_prefix_length):
        labels = _prefix_labels(signature, signature.future_total_ranks[future_index])
        for label in labels:
            if label.family == "old":
                result += 1
            elif label.family_index in selected_set:
                result += 1
    return result


def verify_merged_generator_equivalence(
    thresholds: Sequence[Fraction],
    values: Sequence[Fraction],
    candidate_thresholds: Sequence[Fraction],
    future_values: Sequence[Fraction],
) -> bool:
    """Compare the merged generator against the expanded Stage102 signature."""
    merged = merged_threshold_history_signature(
        thresholds, values, candidate_thresholds, future_values
    )
    expanded = finite_history_signature(
        thresholds, values, candidate_thresholds, future_values
    )

    for j in range(len(future_values)):
        decoded = decode_future_column(merged, j)
        if decoded["old_threshold_rank"] != expanded.future_node_ranks[j]:
            return False
        expected_column = tuple(row[j] for row in expanded.mixed_corners)
        if decoded["candidate_corner_column"] != expected_column:
            return False

    # Exhaust physically valid histories.
    for mask in range(1 << len(candidate_thresholds)):
        selected = tuple(i for i in range(len(candidate_thresholds)) if mask & (1 << i))
        for prefix in range(len(future_values) + 1):
            if history_area_from_merged_signature(merged, selected, prefix) != history_area_from_signature(expanded, selected, prefix):
                return False
    return True
