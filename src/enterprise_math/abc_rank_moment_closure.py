"""History interaction order for rank moments M_d=sum_j r_j^d.

The operation algebra is unchanged: candidate threshold rows and future node
columns are Boolean-selected.  For moment degree d>=1, the exact response
polynomial has degree at most d+1 because a future-column selector gates a
degree-d rank polynomial.  Exact P025 dyadic fixtures realize the top order with
coefficient d!.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import factorial
from typing import Sequence

from .abc_merged_rank_path_generator import MergedRankPath, merged_rank_path
from .abc_signed_exponent_transport import dyadic_difference_pressure_tower


def rank_moment_from_path(
    path: MergedRankPath,
    degree: int,
    threshold_selection: Sequence[int],
    future_selection: Sequence[int],
) -> int:
    """Evaluate M_d from the common labelled merged-rank path."""
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 1:
        raise ValueError("degree must be a positive integer")
    candidate_count = sum(label.family == "candidate" for label in path.merged_labels)
    if len(threshold_selection) != candidate_count:
        raise ValueError("threshold selection has wrong length")
    if len(future_selection) != path.future_node_count:
        raise ValueError("future selection has wrong length")
    if any(bit not in (0, 1) for bit in (*threshold_selection, *future_selection)):
        raise ValueError("selection bits must be 0 or 1")

    selected = {i for i, bit in enumerate(threshold_selection) if bit}

    def selected_rank(merged_rank: int) -> int:
        return sum(
            label.family == "old"
            or (label.family == "candidate" and label.family_index in selected)
            for label in path.merged_labels[:merged_rank]
        )

    ranks = [selected_rank(rank) for rank in path.current_ranks]
    ranks.extend(
        selected_rank(path.future_ranks[j])
        for j, bit in enumerate(future_selection)
        if bit
    )
    return sum(rank**degree for rank in ranks)


def boolean_difference(
    path: MergedRankPath,
    degree: int,
    candidate_indices: Sequence[int],
    future_indices: Sequence[int],
) -> int:
    """Mixed Boolean finite difference over chosen row/column action variables."""
    candidate_indices = tuple(candidate_indices)
    future_indices = tuple(future_indices)
    if len(set(candidate_indices)) != len(candidate_indices):
        raise ValueError("candidate indices must be distinct")
    if len(set(future_indices)) != len(future_indices):
        raise ValueError("future indices must be distinct")
    candidate_count = sum(label.family == "candidate" for label in path.merged_labels)
    if any(not 0 <= i < candidate_count for i in candidate_indices):
        raise ValueError("candidate index out of range")
    if any(not 0 <= j < path.future_node_count for j in future_indices):
        raise ValueError("future index out of range")

    variables = len(candidate_indices) + len(future_indices)
    total = 0
    for assignment in product((0, 1), repeat=variables):
        x = [0] * candidate_count
        y = [0] * path.future_node_count
        for position, index in enumerate(candidate_indices):
            x[index] = assignment[position]
        offset = len(candidate_indices)
        for position, index in enumerate(future_indices):
            y[index] = assignment[offset + position]
        sign = -1 if (variables - sum(assignment)) % 2 else 1
        total += sign * rank_moment_from_path(path, degree, x, y)
    return total


def rational_candidates_between(low: Fraction, high: Fraction, count: int) -> tuple[Fraction, ...]:
    """Choose exact ordered rational thresholds strictly between low and high."""
    if not isinstance(low, Fraction) or not isinstance(high, Fraction) or low >= high:
        raise ValueError("require Fraction low < high")
    if isinstance(count, bool) or not isinstance(count, int) or count < 0:
        raise ValueError("count must be a non-negative integer")
    gap = high - low
    return tuple(low + gap * Fraction(k, count + 1) for k in range(1, count + 1))


def stage110_exact_order_fixture(degree: int) -> dict[str, object]:
    """Realize exact interaction order d+1 inside the `(3,41)` dyadic orbit.

    No old thresholds.  One old node lies below d candidate thresholds and one
    future node lies above all of them.  The future contribution is

        y * (x_1+...+x_d)^d.

    Its top Boolean coefficient is d!.
    """
    if isinstance(degree, bool) or not isinstance(degree, int) or degree < 1:
        raise ValueError("degree must be a positive integer")
    pressures = dyadic_difference_pressure_tower(3, 41, 2, 1).pressures
    low, high = pressures
    candidates = rational_candidates_between(low, high, degree)
    path = merged_rank_path((), (low,), candidates, (high,))
    top = boolean_difference(
        path,
        degree,
        tuple(range(degree)),
        (0,),
    )
    if top != factorial(degree):
        raise AssertionError("top interaction coefficient should be degree factorial")
    return {
        "degree": degree,
        "pressures": pressures,
        "candidate_thresholds": candidates,
        "path": path,
        "top_interaction_order": degree + 1,
        "top_coefficient": top,
    }
