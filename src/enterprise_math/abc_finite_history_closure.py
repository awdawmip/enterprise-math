"""Finite action-history closure for monotone threshold/node extensions.

A current threshold-by-node activation matrix is extended by:
  * selected candidate threshold rows U_i;
  * a monotone prefix of future node columns v_j.

For the scalar activation area, all history responses close exactly at second
order: current area + row marginals + column marginals + mixed corner cells.
No irreducible interaction of order >=3 is needed.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from typing import Iterable, Sequence

from .abc_two_step_history import activation_area, corner_bit, node_rank, threshold_span


@dataclass(frozen=True)
class FiniteHistorySignature:
    area: int
    old_node_count: int
    candidate_thresholds: tuple[Fraction, ...]
    future_values: tuple[Fraction, ...]
    threshold_spans: tuple[int, ...]
    future_node_ranks: tuple[int, ...]
    mixed_corners: tuple[tuple[int, ...], ...]


def _strictly_increasing(values: Sequence[Fraction]) -> bool:
    return all(values[i] < values[i + 1] for i in range(len(values) - 1))


def _nondecreasing(values: Sequence[Fraction]) -> bool:
    return all(values[i] <= values[i + 1] for i in range(len(values) - 1))


def _validate_extension_envelope(
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
    if not _strictly_increasing(thresholds):
        raise ValueError("current thresholds must be strictly increasing")
    if not _strictly_increasing(candidate_thresholds):
        raise ValueError("candidate thresholds must be strictly increasing")
    if set(thresholds).intersection(candidate_thresholds):
        raise ValueError("candidate thresholds must be new rows")
    if not _nondecreasing(values):
        raise ValueError("current values must be nondecreasing")
    if not _nondecreasing(future_values):
        raise ValueError("future values must be nondecreasing")
    if future_values and future_values[0] < values[-1]:
        raise ValueError("future values must extend the current monotone orbit")


def finite_history_signature(
    thresholds: Sequence[Fraction],
    values: Sequence[Fraction],
    candidate_thresholds: Sequence[Fraction],
    future_values: Sequence[Fraction],
) -> FiniteHistorySignature:
    """Compile all first- and mixed-second-order response coordinates."""
    _validate_extension_envelope(thresholds, values, candidate_thresholds, future_values)
    candidates = tuple(candidate_thresholds)
    futures = tuple(future_values)
    spans = tuple(threshold_span(values, threshold) for threshold in candidates)
    ranks = tuple(node_rank(thresholds, value) for value in futures)
    corners = tuple(
        tuple(corner_bit(threshold, value) for value in futures)
        for threshold in candidates
    )
    return FiniteHistorySignature(
        area=activation_area(thresholds, values),
        old_node_count=len(values),
        candidate_thresholds=candidates,
        future_values=futures,
        threshold_spans=spans,
        future_node_ranks=ranks,
        mixed_corners=corners,
    )


def history_area_from_signature(
    signature: FiniteHistorySignature,
    selected_threshold_indices: Iterable[int],
    future_prefix_length: int,
) -> int:
    """Predict area after any threshold subset and a future-node prefix.

    Actual append histories can only take a prefix of the precomputed future-node
    sequence. Threshold rows may be inserted in any order; only their final set
    matters.
    """
    selected = tuple(sorted(set(selected_threshold_indices)))
    a = len(signature.candidate_thresholds)
    b = len(signature.future_values)
    if any(index < 0 or index >= a for index in selected):
        raise ValueError("selected threshold index out of range")
    if isinstance(future_prefix_length, bool) or not isinstance(future_prefix_length, int):
        raise ValueError("future_prefix_length must be an integer")
    if not 0 <= future_prefix_length <= b:
        raise ValueError("future_prefix_length out of range")

    result = signature.area
    result += sum(signature.threshold_spans[index] for index in selected)
    result += sum(signature.future_node_ranks[:future_prefix_length])
    result += sum(
        signature.mixed_corners[index][j]
        for index in selected
        for j in range(future_prefix_length)
    )
    return result


def exact_history_area(
    thresholds: Sequence[Fraction],
    values: Sequence[Fraction],
    candidate_thresholds: Sequence[Fraction],
    future_values: Sequence[Fraction],
    selected_threshold_indices: Iterable[int],
    future_prefix_length: int,
) -> int:
    """Direct area recomputation used to check the second-order compiler."""
    signature = finite_history_signature(
        thresholds, values, candidate_thresholds, future_values
    )
    selected = tuple(sorted(set(selected_threshold_indices)))
    predicted = history_area_from_signature(signature, selected, future_prefix_length)
    final_thresholds = tuple(sorted((*thresholds, *(candidate_thresholds[i] for i in selected))))
    final_values = (*values, *future_values[:future_prefix_length])
    exact = activation_area(final_thresholds, final_values)
    if predicted != exact:
        raise AssertionError("finite-history second-order formula failed")
    return exact


def verify_all_histories(
    thresholds: Sequence[Fraction],
    values: Sequence[Fraction],
    candidate_thresholds: Sequence[Fraction],
    future_values: Sequence[Fraction],
) -> bool:
    """Exhaust all threshold subsets and all physically valid future prefixes."""
    signature = finite_history_signature(
        thresholds, values, candidate_thresholds, future_values
    )
    a = len(candidate_thresholds)
    for count in range(a + 1):
        for selected in combinations(range(a), count):
            for prefix in range(len(future_values) + 1):
                predicted = history_area_from_signature(signature, selected, prefix)
                final_thresholds = tuple(sorted((*thresholds, *(candidate_thresholds[i] for i in selected))))
                final_values = (*values, *future_values[:prefix])
                if predicted != activation_area(final_thresholds, final_values):
                    return False
    return True


def recover_coordinate_from_history_areas(
    signature: FiniteHistorySignature,
    threshold_index: int,
    future_index: int,
) -> dict[str, int]:
    """Recover L_i, R_j and C_ij from area-history queries by differences."""
    if not 0 <= threshold_index < len(signature.candidate_thresholds):
        raise ValueError("threshold_index out of range")
    if not 0 <= future_index < len(signature.future_values):
        raise ValueError("future_index out of range")

    base = signature.area
    row_only = history_area_from_signature(signature, (threshold_index,), 0)
    prefix_before = history_area_from_signature(signature, (), future_index)
    prefix_after = history_area_from_signature(signature, (), future_index + 1)
    mixed_before = history_area_from_signature(signature, (threshold_index,), future_index)
    mixed_after = history_area_from_signature(signature, (threshold_index,), future_index + 1)

    recovered_span = row_only - base
    recovered_rank = prefix_after - prefix_before
    recovered_corner = (mixed_after - mixed_before) - (prefix_after - prefix_before)
    return {
        "threshold_span": recovered_span,
        "future_node_rank": recovered_rank,
        "mixed_corner": recovered_corner,
    }


def multilinear_area(
    signature: FiniteHistorySignature,
    threshold_selection: Sequence[int],
    node_selection: Sequence[int],
) -> int:
    """Algebraic extension to independent row/column selection bits.

    This is a degree-at-most-two Boolean polynomial. Physical node histories are
    the prefix-restricted subfamily of this algebraic envelope.
    """
    if len(threshold_selection) != len(signature.candidate_thresholds):
        raise ValueError("threshold selection has wrong length")
    if len(node_selection) != len(signature.future_values):
        raise ValueError("node selection has wrong length")
    if any(bit not in (0, 1) for bit in (*threshold_selection, *node_selection)):
        raise ValueError("selection entries must be 0 or 1")

    value = signature.area
    value += sum(bit * span for bit, span in zip(threshold_selection, signature.threshold_spans))
    value += sum(bit * rank for bit, rank in zip(node_selection, signature.future_node_ranks))
    value += sum(
        threshold_selection[i] * node_selection[j] * signature.mixed_corners[i][j]
        for i in range(len(threshold_selection))
        for j in range(len(node_selection))
    )
    return value
