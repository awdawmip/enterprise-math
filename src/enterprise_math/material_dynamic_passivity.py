"""Static material passivity versus saved-state current-force cycle passivity.

A passive loading/returning force table does not automatically remain passive
when an explicit world samples only the **current** force at each saved jump.
This module keeps those two notions separate.

For an increasing loading schedule ``i_0<...<i_m`` current-hold absorption is

    2 W_load^cur = 2 sum_j L[i_j] * (x[i_{j+1}]-x[i_j]).

For a decreasing returning schedule ``r_0>...>r_n`` current-hold release is

    2 W_ret^cur = 2 sum_j R[r_j] * (x[r_j]-x[r_{j+1}]).

Their sampled cycle loss is ``W_load^cur-W_ret^cur``.  It can be negative even
when the static symmetric/chord material cycle is passive or exactly elastic.
The two-state elastic table ``L=R=(0,F)`` is the minimal witness: loading 0->1
samples force 0 while returning 1->0 samples force F, creating negative sampled
loss.

This is not a defect of the material table itself.  It is a force-sampling policy
effect.  A time integrator can close kinetic/work accounting for whichever force
it is given and still reproduce this sampled passivity failure.

For comparison, endpoint/chord branch work is schedule-independent: summing the
declared chord work between each saved pair telescopes to the same static branch
work.  Turning that work into a dynamical force requires an endpoint-aware or
implicit finite policy and is intentionally not hidden inside this diagnostic.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_force_work import FiniteForceLaw, force_cycle_work_report
from .material_hysteresis import LOADING, RETURNING


def _loading_schedule(law: FiniteForceLaw, depths: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    values = tuple(depths)
    if len(values) < 2:
        raise ValueError("loading schedule must contain at least two depths")
    if any(isinstance(v, bool) or not isinstance(v, int) for v in values):
        raise ValueError("loading depths must be integers")
    if any(b <= a for a, b in zip(values, values[1:])):
        raise ValueError("loading schedule must be strictly increasing")
    if values[0] != 0 or values[-1] >= len(law.profile.loading):
        raise ValueError("loading schedule must start at zero and stay inside force law")
    return values


def _returning_schedule(law: FiniteForceLaw, depths: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    values = tuple(depths)
    if len(values) < 2:
        raise ValueError("returning schedule must contain at least two depths")
    if any(isinstance(v, bool) or not isinstance(v, int) for v in values):
        raise ValueError("returning depths must be integers")
    if any(b >= a for a, b in zip(values, values[1:])):
        raise ValueError("returning schedule must be strictly decreasing")
    if values[-1] != 0 or values[0] >= len(law.profile.returning):
        raise ValueError("returning schedule must end at zero and stay inside force law")
    return values


def current_hold_branch_work_numerator2(
    law: FiniteForceLaw,
    depths: tuple[int, ...] | list[int],
    branch: str,
) -> int:
    """Return positive-oriented branch work magnitude under current-force hold."""
    grid = law.deformation_counts
    if branch == LOADING:
        values = _loading_schedule(law, depths)
        samples = law.profile.loading
        return sum(
            2 * samples[left] * (grid[right] - grid[left])
            for left, right in zip(values, values[1:])
        )
    if branch == RETURNING:
        values = _returning_schedule(law, depths)
        samples = law.profile.returning
        return sum(
            2 * samples[left] * (grid[left] - grid[right])
            for left, right in zip(values, values[1:])
        )
    raise ValueError("branch must be LOADING or RETURNING")


def chord_branch_work_between_depths_numerator2(
    law: FiniteForceLaw,
    lower_depth: int,
    upper_depth: int,
    branch: str,
) -> int:
    """Return static symmetric branch work between two depth endpoints."""
    for name, value in (("lower_depth", lower_depth), ("upper_depth", upper_depth)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    if not 0 <= lower_depth < upper_depth < len(law.profile.loading):
        raise ValueError("require 0 <= lower_depth < upper_depth within force law")
    if branch == LOADING:
        samples = law.profile.loading
    elif branch == RETURNING:
        samples = law.profile.returning
    else:
        raise ValueError("branch must be LOADING or RETURNING")
    grid = law.deformation_counts
    return sum(
        (samples[k - 1] + samples[k]) * (grid[k] - grid[k - 1])
        for k in range(lower_depth + 1, upper_depth + 1)
    )


def chord_branch_work_over_saved_schedule_numerator2(
    law: FiniteForceLaw,
    depths: tuple[int, ...] | list[int],
    branch: str,
) -> int:
    """Sum endpoint/chord work over a saved schedule; internal cells are analytic data, not saved states."""
    if branch == LOADING:
        values = _loading_schedule(law, depths)
        return sum(
            chord_branch_work_between_depths_numerator2(law, left, right, LOADING)
            for left, right in zip(values, values[1:])
        )
    if branch == RETURNING:
        values = _returning_schedule(law, depths)
        return sum(
            chord_branch_work_between_depths_numerator2(law, right, left, RETURNING)
            for left, right in zip(values, values[1:])
        )
    raise ValueError("branch must be LOADING or RETURNING")


@dataclass(frozen=True)
class SampledCyclePassivityReport:
    loading_depths: tuple[int, ...]
    returning_depths: tuple[int, ...]
    peak_depth: int
    current_loading_work_numerator2: int
    current_returning_work_numerator2: int
    current_sampled_loss_numerator2: int
    current_sampled_passive: bool
    chord_loading_work_numerator2: int
    chord_returning_work_numerator2: int
    static_chord_loss_numerator2: int
    static_chord_passive: bool
    force_sampling_changes_passivity: bool


def sampled_cycle_passivity_report(
    law: FiniteForceLaw,
    loading_depths: tuple[int, ...] | list[int],
    returning_depths: tuple[int, ...] | list[int],
) -> SampledCyclePassivityReport:
    loading = _loading_schedule(law, loading_depths)
    returning = _returning_schedule(law, returning_depths)
    if loading[-1] != returning[0]:
        raise ValueError("loading and returning schedules must share one peak depth")
    peak = loading[-1]
    current_load = current_hold_branch_work_numerator2(law, loading, LOADING)
    current_return = current_hold_branch_work_numerator2(law, returning, RETURNING)
    current_loss = current_load - current_return
    chord_load = chord_branch_work_over_saved_schedule_numerator2(law, loading, LOADING)
    chord_return = chord_branch_work_over_saved_schedule_numerator2(law, returning, RETURNING)
    static = force_cycle_work_report(law, peak)
    if chord_load != static.loading_work_numerator2 or chord_return != static.returned_work_numerator2:
        raise AssertionError("saved chord schedule failed static work telescoping")
    chord_loss = chord_load - chord_return
    if chord_loss != static.dissipated_work_numerator2:
        raise AssertionError("saved chord cycle failed static loss identity")
    return SampledCyclePassivityReport(
        loading_depths=loading,
        returning_depths=returning,
        peak_depth=peak,
        current_loading_work_numerator2=current_load,
        current_returning_work_numerator2=current_return,
        current_sampled_loss_numerator2=current_loss,
        current_sampled_passive=current_loss >= 0,
        chord_loading_work_numerator2=chord_load,
        chord_returning_work_numerator2=chord_return,
        static_chord_loss_numerator2=chord_loss,
        static_chord_passive=chord_loss >= 0,
        force_sampling_changes_passivity=(current_loss >= 0) != (chord_loss >= 0),
    )
