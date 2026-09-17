#!/usr/bin/env python3
"""Exact finite regression for the E001 current-hold passivity-budget theorem."""

from __future__ import annotations

import json
from itertools import combinations, product

TASK_ID = "RS-E001-IMPULSE-V2"
RESEARCHER_ID = "EM-E001-7C4A21"
CLAIM_ID = "chatgpt-e001imp-20260830-2140-7c4a21"


def increasing_schedules(peak: int) -> tuple[tuple[int, ...], ...]:
    middle = tuple(range(1, peak))
    schedules = []
    for count in range(peak):
        for chosen in combinations(middle, count):
            schedules.append((0, *chosen, peak))
    return tuple(schedules)


def returning_schedules(peak: int) -> tuple[tuple[int, ...], ...]:
    return tuple(tuple(reversed(schedule)) for schedule in increasing_schedules(peak))


def static_chord_work2(grid, loading, returning, peak):
    load = 0
    ret = 0
    for depth in range(1, peak + 1):
        width = grid[depth] - grid[depth - 1]
        load += (loading[depth - 1] + loading[depth]) * width
        ret += (returning[depth - 1] + returning[depth]) * width
    return load, ret


def current_loading_work2(grid, loading, schedule):
    return sum(
        2 * loading[left] * (grid[right] - grid[left])
        for left, right in zip(schedule, schedule[1:])
    )


def current_returning_work2(grid, returning, schedule):
    return sum(
        2 * returning[high] * (grid[high] - grid[low])
        for high, low in zip(schedule, schedule[1:])
    )


def verify_case(grid, loading, returning, peak):
    chord_load, chord_return = static_chord_work2(grid, loading, returning, peak)
    static_loss = chord_load - chord_return
    losses = []
    pair_checks = 0

    for load_schedule in increasing_schedules(peak):
        for return_schedule in returning_schedules(peak):
            pair_checks += 1
            current_load = current_loading_work2(grid, loading, load_schedule)
            current_return = current_returning_work2(grid, returning, return_schedule)
            current_loss = current_load - current_return
            load_deficit = chord_load - current_load
            return_excess = current_return - chord_return

            assert current_loss == static_loss - load_deficit - return_excess
            assert load_deficit >= 0
            assert return_excess >= 0
            losses.append(current_loss)

    worst = 2 * (loading[0] - returning[peak]) * (grid[peak] - grid[0])
    full = 2 * sum(
        (loading[depth - 1] - returning[depth])
        * (grid[depth] - grid[depth - 1])
        for depth in range(1, peak + 1)
    )
    full_defect = sum(
        (
            (loading[depth] - loading[depth - 1])
            + (returning[depth] - returning[depth - 1])
        )
        * (grid[depth] - grid[depth - 1])
        for depth in range(1, peak + 1)
    )

    assert min(losses) == worst
    assert max(losses) == full
    assert full == static_loss - full_defect
    assert (all(loss >= 0 for loss in losses)) == (loading[0] >= returning[peak])
    return pair_checks


def run_exhaustion():
    law_grid_cases = 0
    schedule_pair_checks = 0
    per_peak = []

    for peak in range(1, 5):
        monotone_sequences = tuple(
            seq
            for seq in product(range(4), repeat=peak + 1)
            if all(seq[i] <= seq[i + 1] for i in range(peak))
        )
        peak_cases = 0
        peak_pairs = 0
        for widths in product((1, 2), repeat=peak):
            grid = [0]
            for width in widths:
                grid.append(grid[-1] + width)
            grid = tuple(grid)
            for loading in monotone_sequences:
                for returning in monotone_sequences:
                    peak_cases += 1
                    peak_pairs += verify_case(grid, loading, returning, peak)
        law_grid_cases += peak_cases
        schedule_pair_checks += peak_pairs
        per_peak.append(
            {
                "peak": peak,
                "monotone_sequences": len(monotone_sequences),
                "law_grid_cases": peak_cases,
                "schedule_pair_checks": peak_pairs,
            }
        )

    assert law_grid_cases == 61776
    assert schedule_pair_checks == 3374664
    return law_grid_cases, schedule_pair_checks, per_peak


def verify_witnesses():
    # Strong two-state witness: pointwise R<=L and static passive, but current active.
    grid = (0, 1)
    loading = (0, 2)
    returning = (0, 1)
    chord_load, chord_return = static_chord_work2(grid, loading, returning, 1)
    current_load = current_loading_work2(grid, loading, (0, 1))
    current_return = current_returning_work2(grid, returning, (1, 0))
    assert all(r <= l for l, r in zip(loading, returning))
    assert (chord_load, chord_return, chord_load - chord_return) == (2, 1, 1)
    assert (current_load, current_return, current_load - current_return) == (0, 2, -2)

    # Saved-state refinement can repair passivity without changing the table.
    grid2 = (0, 1, 2)
    loading2 = (0, 1, 1)
    returning2 = (0, 0, 1)
    chord_load2, chord_return2 = static_chord_work2(grid2, loading2, returning2, 2)
    coarse = current_loading_work2(grid2, loading2, (0, 2)) - current_returning_work2(
        grid2, returning2, (2, 0)
    )
    full = current_loading_work2(grid2, loading2, (0, 1, 2)) - current_returning_work2(
        grid2, returning2, (2, 1, 0)
    )
    assert chord_load2 - chord_return2 == 2
    assert coarse == -4
    assert full == 0
    return {
        "strong_two_state": {"static_loss2": 1, "current_loss2": -2},
        "refinement_repair": {"static_loss2": 2, "coarse_loss2": -4, "full_loss2": 0},
    }


def main():
    cases, pairs, per_peak = run_exhaustion()
    witnesses = verify_witnesses()
    report = {
        "schema": "ENTERPRISE_MATH_E001_CURRENT_HOLD_PASSIVITY_BUDGET_CHECK_V1",
        "task_id": TASK_ID,
        "researcher_id": RESEARCHER_ID,
        "claim_id": CLAIM_ID,
        "verdict": "PASS",
        "law_grid_cases": cases,
        "schedule_pair_checks": pairs,
        "force_alphabet": [0, 1, 2, 3],
        "cell_width_alphabet": [1, 2],
        "peak_range": [1, 4],
        "per_peak": per_peak,
        "witnesses": witnesses,
        "verified_claims": [
            "exact_budget_identity",
            "monotone_nonnegative_sampling_defects",
            "coarsest_exact_global_minimum",
            "fully_refined_exact_global_maximum",
            "full_grid_sampling_defect_formula",
            "universal_saved_schedule_passivity_iff_L0_ge_RK",
        ],
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
