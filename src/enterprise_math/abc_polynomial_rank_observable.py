"""Polynomial rank observables over the common merged-rank generator.

For a nonzero polynomial P(r)=sum_k c_k r^k of degree d, the finite action
response has degree at most d+1.  A single exact dyadic edge with d candidate
thresholds between its old and future pressures realizes the top mixed
coefficient c_d*d!, so the worst-case interaction order is exactly d+1.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import product
from math import factorial
from typing import Sequence

from .abc_merged_rank_path_generator import MergedRankPath, merged_rank_path
from .abc_rank_moment_closure import rational_candidates_between
from .abc_signed_exponent_transport import dyadic_difference_pressure_tower


def normalize_polynomial(coefficients: Sequence[Fraction]) -> tuple[Fraction, ...]:
    if not coefficients:
        raise ValueError("polynomial coefficients must be non-empty")
    if any(not isinstance(value, Fraction) for value in coefficients):
        raise ValueError("coefficients must be Fractions")
    result = list(coefficients)
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    if len(result) == 1 and result[0] == 0:
        raise ValueError("zero polynomial has no finite leading degree for this theorem")
    return tuple(result)


def polynomial_degree(coefficients: Sequence[Fraction]) -> int:
    return len(normalize_polynomial(coefficients)) - 1


def polynomial_value(coefficients: Sequence[Fraction], rank: int) -> Fraction:
    if isinstance(rank, bool) or not isinstance(rank, int) or rank < 0:
        raise ValueError("rank must be a non-negative integer")
    coefficients = normalize_polynomial(coefficients)
    value = Fraction(0, 1)
    for coefficient in reversed(coefficients):
        value = value * rank + coefficient
    return value


def polynomial_rank_observable_from_path(
    path: MergedRankPath,
    coefficients: Sequence[Fraction],
    threshold_selection: Sequence[int],
    future_selection: Sequence[int],
) -> Fraction:
    coefficients = normalize_polynomial(coefficients)
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
    return sum((polynomial_value(coefficients, rank) for rank in ranks), Fraction(0, 1))


def polynomial_boolean_difference(
    path: MergedRankPath,
    coefficients: Sequence[Fraction],
    candidate_indices: Sequence[int],
    future_indices: Sequence[int],
) -> Fraction:
    candidate_indices = tuple(candidate_indices)
    future_indices = tuple(future_indices)
    if len(set(candidate_indices)) != len(candidate_indices) or len(set(future_indices)) != len(future_indices):
        raise ValueError("difference indices must be distinct within each family")
    candidate_count = sum(label.family == "candidate" for label in path.merged_labels)
    if any(not 0 <= index < candidate_count for index in candidate_indices):
        raise ValueError("candidate index out of range")
    if any(not 0 <= index < path.future_node_count for index in future_indices):
        raise ValueError("future index out of range")

    order = len(candidate_indices) + len(future_indices)
    total = Fraction(0, 1)
    for assignment in product((0, 1), repeat=order):
        x = [0] * candidate_count
        y = [0] * path.future_node_count
        for position, index in enumerate(candidate_indices):
            x[index] = assignment[position]
        offset = len(candidate_indices)
        for position, index in enumerate(future_indices):
            y[index] = assignment[offset + position]
        sign = -1 if (order - sum(assignment)) % 2 else 1
        total += sign * polynomial_rank_observable_from_path(path, coefficients, x, y)
    return total


def stage111_exact_polynomial_fixture(coefficients: Sequence[Fraction]) -> dict[str, object]:
    coefficients = normalize_polynomial(coefficients)
    degree = len(coefficients) - 1
    leading = coefficients[-1]
    pressures = dyadic_difference_pressure_tower(3, 41, 2, 1).pressures
    low, high = pressures
    candidates = rational_candidates_between(low, high, degree)
    path = merged_rank_path((), (low,), candidates, (high,))
    top = polynomial_boolean_difference(
        path,
        coefficients,
        tuple(range(degree)),
        (0,),
    )
    expected = leading * factorial(degree)
    if top != expected:
        raise AssertionError("top polynomial interaction coefficient mismatch")
    return {
        "coefficients": coefficients,
        "degree": degree,
        "leading_coefficient": leading,
        "pressures": pressures,
        "candidate_thresholds": candidates,
        "path": path,
        "top_interaction_order": degree + 1,
        "top_coefficient": top,
    }
