"""Finite-action response polynomial for quadratic threshold-rank energy.

For rank energy E=sum_j r_j^2, candidate threshold rows are Boolean variables
x_i and prospective future node columns are Boolean variables y_j.  The exact
response polynomial has degree at most three.  Genuine x_i*x_k*y_j terms occur
when one future node crosses two candidate thresholds.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from typing import Sequence

from .abc_quadratic_rank_energy import rank_energy_state
from .abc_signed_exponent_transport import dyadic_difference_pressure_tower
from .abc_two_step_history import node_rank


@dataclass(frozen=True)
class QuadraticEnergyJet:
    base_energy: int
    threshold_linear: tuple[int, ...]
    threshold_pair: tuple[tuple[int, int, int], ...]
    future_linear: tuple[int, ...]
    threshold_future: tuple[tuple[int, ...], ...]
    threshold_pair_future: tuple[tuple[int, int, int, int], ...]


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
        raise ValueError("candidate thresholds must be new")
    if any(values[i] > values[i + 1] for i in range(len(values) - 1)):
        raise ValueError("current values must be nondecreasing")
    if any(future_values[i] > future_values[i + 1] for i in range(len(future_values) - 1)):
        raise ValueError("future values must be nondecreasing")
    if future_values and future_values[0] < values[-1]:
        raise ValueError("future values must extend the current orbit")


def quadratic_energy_jet(
    thresholds: Sequence[Fraction],
    values: Sequence[Fraction],
    candidate_thresholds: Sequence[Fraction],
    future_values: Sequence[Fraction],
) -> QuadraticEnergyJet:
    """Return exact Boolean polynomial coefficients through order three."""
    _validate(thresholds, values, candidate_thresholds, future_values)
    thresholds = tuple(thresholds)
    values = tuple(values)
    candidates = tuple(candidate_thresholds)
    futures = tuple(future_values)

    old_ranks = tuple(node_rank(thresholds, value) for value in values)
    base_energy = sum(rank * rank for rank in old_ranks)
    old_active = tuple(
        tuple(int(value >= threshold) for value in values)
        for threshold in candidates
    )

    threshold_linear = tuple(
        2 * sum(rank * bit for rank, bit in zip(old_ranks, row)) + sum(row)
        for row in old_active
    )

    threshold_pair_entries: list[tuple[int, int, int]] = []
    for i, k in combinations(range(len(candidates)), 2):
        coefficient = 2 * sum(a * b for a, b in zip(old_active[i], old_active[k]))
        threshold_pair_entries.append((i, k, coefficient))

    old_future_ranks = tuple(node_rank(thresholds, value) for value in futures)
    future_linear = tuple(rank * rank for rank in old_future_ranks)
    corners = tuple(
        tuple(int(value >= threshold) for value in futures)
        for threshold in candidates
    )
    threshold_future = tuple(
        tuple(corners[i][j] * (2 * old_future_ranks[j] + 1) for j in range(len(futures)))
        for i in range(len(candidates))
    )

    cubic_entries: list[tuple[int, int, int, int]] = []
    for i, k in combinations(range(len(candidates)), 2):
        for j in range(len(futures)):
            coefficient = 2 * corners[i][j] * corners[k][j]
            cubic_entries.append((i, k, j, coefficient))

    return QuadraticEnergyJet(
        base_energy=base_energy,
        threshold_linear=threshold_linear,
        threshold_pair=tuple(threshold_pair_entries),
        future_linear=future_linear,
        threshold_future=threshold_future,
        threshold_pair_future=tuple(cubic_entries),
    )


def evaluate_quadratic_energy_jet(
    jet: QuadraticEnergyJet,
    threshold_selection: Sequence[int],
    future_selection: Sequence[int],
) -> int:
    """Evaluate the exact degree-three Boolean response polynomial."""
    if len(threshold_selection) != len(jet.threshold_linear):
        raise ValueError("threshold selection has wrong length")
    if len(future_selection) != len(jet.future_linear):
        raise ValueError("future selection has wrong length")
    if any(bit not in (0, 1) for bit in (*threshold_selection, *future_selection)):
        raise ValueError("selection bits must be 0 or 1")

    value = jet.base_energy
    value += sum(bit * coefficient for bit, coefficient in zip(threshold_selection, jet.threshold_linear))
    for i, k, coefficient in jet.threshold_pair:
        value += threshold_selection[i] * threshold_selection[k] * coefficient
    value += sum(bit * coefficient for bit, coefficient in zip(future_selection, jet.future_linear))
    for i, row in enumerate(jet.threshold_future):
        value += threshold_selection[i] * sum(
            future_selection[j] * row[j] for j in range(len(row))
        )
    for i, k, j, coefficient in jet.threshold_pair_future:
        value += threshold_selection[i] * threshold_selection[k] * future_selection[j] * coefficient
    return value


def direct_quadratic_energy(
    thresholds: Sequence[Fraction],
    values: Sequence[Fraction],
    candidate_thresholds: Sequence[Fraction],
    future_values: Sequence[Fraction],
    threshold_selection: Sequence[int],
    future_selection: Sequence[int],
) -> int:
    """Direct recomputation for arbitrary independent candidate/future selections."""
    _validate(thresholds, values, candidate_thresholds, future_values)
    if len(threshold_selection) != len(candidate_thresholds) or len(future_selection) != len(future_values):
        raise ValueError("selection has wrong length")
    selected_thresholds = tuple(
        candidate_thresholds[i] for i, bit in enumerate(threshold_selection) if bit
    )
    selected_futures = tuple(
        future_values[j] for j, bit in enumerate(future_selection) if bit
    )
    final_thresholds = tuple(sorted((*thresholds, *selected_thresholds)))
    final_values = (*values, *selected_futures)
    return rank_energy_state(final_thresholds, final_values).quadratic_rank_energy


def third_boolean_difference_two_thresholds_one_future(
    jet: QuadraticEnergyJet, i: int, k: int, j: int
) -> int:
    """Return the irreducible x_i x_k y_j coefficient by cube differencing."""
    if i == k:
        raise ValueError("threshold indices must be distinct")
    a = len(jet.threshold_linear)
    b = len(jet.future_linear)
    if not (0 <= i < a and 0 <= k < a and 0 <= j < b):
        raise ValueError("index out of range")

    total = 0
    for xi in (0, 1):
        for xk in (0, 1):
            for yj in (0, 1):
                x = [0] * a
                y = [0] * b
                x[i] = xi
                x[k] = xk
                y[j] = yj
                sign = -1 if (3 - (xi + xk + yj)) % 2 else 1
                total += sign * evaluate_quadratic_energy_jet(jet, x, y)
    return total


def stage108_arithmetic_cubic_fixture() -> dict[str, object]:
    """Exact P025 fixture with a nonzero third-order interaction coefficient."""
    pressures = dyadic_difference_pressure_tower(3, 41, 2, 1).pressures
    thresholds: tuple[Fraction, ...] = ()
    current = pressures[:1]
    candidates = (Fraction(1, 10), Fraction(1, 2))
    futures = pressures[1:]
    jet = quadratic_energy_jet(thresholds, current, candidates, futures)
    third = third_boolean_difference_two_thresholds_one_future(jet, 0, 1, 0)
    if third != 2:
        raise AssertionError("fixture should realize cubic coefficient two")
    return {
        "pressures": pressures,
        "candidates": candidates,
        "jet": jet,
        "third_difference": third,
    }
