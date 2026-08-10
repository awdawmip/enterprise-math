"""Endpoint normal forms for finite threshold/node action histories.

For the endpoint-area future language, threshold insertions commute with each
other and with future-node appends: only the final candidate-threshold subset
and the number of appended future nodes matter.  The same collapse is false for
full area traces, where intermediate responses retain action order.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import factorial
from typing import Iterable, Sequence

from .abc_merged_threshold_history import (
    MergedThresholdHistorySignature,
    history_area_from_merged_signature,
)

Action = tuple[str, int | None]


@dataclass(frozen=True)
class EndpointWordNormalForm:
    selected_threshold_indices: tuple[int, ...]
    future_prefix_length: int


@dataclass(frozen=True)
class GeneratorRecovery:
    threshold_spans: tuple[int, ...]
    future_total_ranks: tuple[int, ...]


def normalize_action_word(
    word: Sequence[Action],
    candidate_count: int,
    future_count: int,
) -> EndpointWordNormalForm:
    """Collapse a valid action word to endpoint normal form `(I,t)`."""
    selected: set[int] = set()
    node_count = 0
    for kind, index in word:
        if kind == "T":
            if index is None or isinstance(index, bool) or not isinstance(index, int):
                raise ValueError("threshold action requires an integer index")
            if not 0 <= index < candidate_count:
                raise ValueError("threshold action index out of range")
            if index in selected:
                raise ValueError("candidate threshold may be inserted at most once")
            selected.add(index)
        elif kind == "J":
            if index is not None:
                raise ValueError("node action index must be None")
            node_count += 1
            if node_count > future_count:
                raise ValueError("action word exceeds declared future-node prefix")
        else:
            raise ValueError("unknown action kind")
    return EndpointWordNormalForm(tuple(sorted(selected)), node_count)


def endpoint_area_for_word(
    signature: MergedThresholdHistorySignature,
    word: Sequence[Action],
) -> int:
    normal = normalize_action_word(
        word,
        len(signature.candidate_thresholds),
        len(signature.future_total_ranks),
    )
    return history_area_from_merged_signature(
        signature,
        normal.selected_threshold_indices,
        normal.future_prefix_length,
    )


def area_trace_for_word(
    signature: MergedThresholdHistorySignature,
    word: Sequence[Action],
) -> tuple[int, ...]:
    """Return endpoint area after every prefix; unlike final area this keeps order."""
    selected: set[int] = set()
    node_count = 0
    trace: list[int] = []
    for position, (kind, index) in enumerate(word):
        if kind == "T":
            if index is None or isinstance(index, bool) or not isinstance(index, int):
                raise ValueError("threshold action requires an integer index")
            if not 0 <= index < len(signature.candidate_thresholds):
                raise ValueError("threshold action index out of range")
            if index in selected:
                raise ValueError("candidate threshold may be inserted at most once")
            selected.add(index)
        elif kind == "J":
            if index is not None:
                raise ValueError("node action index must be None")
            node_count += 1
            if node_count > len(signature.future_total_ranks):
                raise ValueError("action word exceeds declared future-node prefix")
        else:
            raise ValueError(f"unknown action kind at position {position}")
        trace.append(
            history_area_from_merged_signature(signature, tuple(sorted(selected)), node_count)
        )
    return tuple(trace)


def endpoint_class_count(candidate_count: int, future_count: int) -> int:
    if candidate_count < 0 or future_count < 0:
        raise ValueError("counts must be non-negative")
    return (1 << candidate_count) * (future_count + 1)


def endpoint_fiber_size(selected_threshold_count: int, future_prefix_length: int) -> int:
    """Number of valid interleavings collapsing to one endpoint `(I,t)`."""
    if selected_threshold_count < 0 or future_prefix_length < 0:
        raise ValueError("counts must be non-negative")
    return factorial(selected_threshold_count + future_prefix_length) // factorial(future_prefix_length)


def raw_valid_word_count(candidate_count: int, future_count: int) -> int:
    """Count all valid words across every threshold subset and node-prefix length."""
    if candidate_count < 0 or future_count < 0:
        raise ValueError("counts must be non-negative")
    from math import comb

    total = 0
    for selected_count in range(candidate_count + 1):
        subset_count = comb(candidate_count, selected_count)
        for prefix in range(future_count + 1):
            total += subset_count * endpoint_fiber_size(selected_count, prefix)
    return total


def recover_generator_from_endpoint_responses(
    signature: MergedThresholdHistorySignature,
) -> GeneratorRecovery:
    """Recover `(L_i,Q_j)` using only endpoint-area response queries."""
    base = history_area_from_merged_signature(signature, (), 0)
    spans = tuple(
        history_area_from_merged_signature(signature, (i,), 0) - base
        for i in range(len(signature.candidate_thresholds))
    )

    ranks: list[int] = []
    for j in range(len(signature.future_total_ranks)):
        old_increment = (
            history_area_from_merged_signature(signature, (), j + 1)
            - history_area_from_merged_signature(signature, (), j)
        )
        candidate_crossed = 0
        for i in range(len(signature.candidate_thresholds)):
            mixed_increment = (
                history_area_from_merged_signature(signature, (i,), j + 1)
                - history_area_from_merged_signature(signature, (i,), j)
            )
            candidate_crossed += mixed_increment - old_increment
        ranks.append(old_increment + candidate_crossed)

    return GeneratorRecovery(spans, tuple(ranks))
