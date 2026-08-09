"""Decompose hardening-material work loss into sampling and integrator defects.

For a nondecreasing finite loading force law and an explicit increasing saved
schedule S=(s_0,...,s_m), the causal current-force world performs doubled work

    W_S^2 = 2 sum_j F_{s_j}(x_{s_{j+1}}-x_{s_j}).

Between the same endpoints define the fully sampled left-hold work

    W_L^2 = 2 sum_{k=i}^{j-1} F_k (x_{k+1}-x_k)

and the static symmetric chord work

    W_C^2 = sum_{k=i}^{j-1} (F_k+F_{k+1})(x_{k+1}-x_k).

For nondecreasing force:

    W_S^2 <= W_L^2 <= W_C^2,

with the exact decomposition

    W_C^2-W_S^2
      = (W_L^2-W_S^2) + (W_C^2-W_L^2).

The first term is the **saved-state sampling deficit**: intermediate material
states were not visited.  The second is the **force-pairing/integrator deficit**:
even visiting every material depth still samples only the left/current force.

Inserting one saved depth m into one schedule interval i<j increases the causal
work by exactly

    2 Delta W = 2 (F_m-F_i)(x_j-x_m),

so time/saved-state refinement monotonically increases absorbed work for a
hardening branch.  It cannot by itself remove the remaining left-vs-chord
integrator defect.

These are algorithmic sampling resources.  They are not material hysteresis and
must not be fitted as a real strain-rate effect without separate evidence.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_force_sampling_work import current_hold_work_over_explicit_saved_schedule
from .material_force_work import FiniteForceLaw


def _schedule(law: FiniteForceLaw, saved_depths: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    depths = tuple(saved_depths)
    if len(depths) < 2:
        raise ValueError("saved schedule must contain at least two depths")
    if any(isinstance(depth, bool) or not isinstance(depth, int) for depth in depths):
        raise ValueError("saved depths must be integers")
    if any(right <= left for left, right in zip(depths, depths[1:])):
        raise ValueError("saved loading depths must be strictly increasing")
    if depths[0] < 0 or depths[-1] >= len(law.profile.loading):
        raise ValueError("saved schedule lies outside force law")
    return depths


@dataclass(frozen=True)
class ForceSamplingDefectDecomposition:
    saved_depths: tuple[int, ...]
    coarse_current_hold_work_numerator2: int
    fully_sampled_left_work_numerator2: int
    static_chord_work_numerator2: int
    state_sampling_defect_numerator2: int
    integrator_pairing_defect_numerator2: int
    total_static_defect_numerator2: int
    loading_nondecreasing: bool


def force_sampling_defect_decomposition(
    law: FiniteForceLaw,
    saved_depths: tuple[int, ...] | list[int],
) -> ForceSamplingDefectDecomposition:
    """Split static-minus-causal work into missed-state and left-pairing pieces."""
    depths = _schedule(law, saved_depths)
    start = depths[0]
    end = depths[-1]
    forces = law.profile.loading
    grid = law.deformation_counts
    nondecreasing = all(forces[k] <= forces[k + 1] for k in range(start, end))
    coarse2 = current_hold_work_over_explicit_saved_schedule(law, depths)
    full_left2 = sum(
        2 * forces[k] * (grid[k + 1] - grid[k])
        for k in range(start, end)
    )
    chord2 = sum(
        (forces[k] + forces[k + 1]) * (grid[k + 1] - grid[k])
        for k in range(start, end)
    )
    sampling = full_left2 - coarse2
    integrator = chord2 - full_left2
    total = chord2 - coarse2
    if total != sampling + integrator:
        raise AssertionError("force sampling defect decomposition failed exact additivity")
    if nondecreasing and (sampling < 0 or integrator < 0):
        raise AssertionError("hardening force produced a negative sampling/integrator defect")
    return ForceSamplingDefectDecomposition(
        saved_depths=depths,
        coarse_current_hold_work_numerator2=coarse2,
        fully_sampled_left_work_numerator2=full_left2,
        static_chord_work_numerator2=chord2,
        state_sampling_defect_numerator2=sampling,
        integrator_pairing_defect_numerator2=integrator,
        total_static_defect_numerator2=total,
        loading_nondecreasing=nondecreasing,
    )


def inserted_saved_state_work_gain_numerator2(
    law: FiniteForceLaw,
    left_depth: int,
    inserted_depth: int,
    right_depth: int,
) -> int:
    """Exact causal-work gain from replacing i->j by i->m->j."""
    for name, value in (
        ("left_depth", left_depth),
        ("inserted_depth", inserted_depth),
        ("right_depth", right_depth),
    ):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    if not 0 <= left_depth < inserted_depth < right_depth < len(law.profile.loading):
        raise ValueError("require 0 <= left < inserted < right within force law")
    forces = law.profile.loading
    grid = law.deformation_counts
    formula = 2 * (forces[inserted_depth] - forces[left_depth]) * (
        grid[right_depth] - grid[inserted_depth]
    )
    coarse = current_hold_work_over_explicit_saved_schedule(
        law, (left_depth, right_depth)
    )
    refined = current_hold_work_over_explicit_saved_schedule(
        law, (left_depth, inserted_depth, right_depth)
    )
    if refined - coarse != formula:
        raise AssertionError("inserted saved-state work gain formula failed")
    return formula
