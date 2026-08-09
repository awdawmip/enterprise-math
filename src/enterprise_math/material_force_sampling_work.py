"""Saved-state force sampling work versus the declared static material chord work.

A finite force-deformation law does not by itself determine how much work one
explicit world tick performs.  In the causal E001 impulse world the force is
sampled from the **current saved deformation** and held for the tick.  If that
tick jumps from represented depth i to a deeper depth j, its work differs from
the finite static/chord work carried by the tabulated material law.

For deformation coordinates x_i<...<x_j and loading force samples F_k:

    2 W_current = 2 F_i (x_j-x_i),

while the declared symmetric finite/chord work is

    2 W_chord = sum_{k=i+1}^j (F_{k-1}+F_k)(x_k-x_{k-1}).

If the loading branch is nondecreasing on the traversed interval then exactly

    W_current <= W_chord <= W_endpoint,

where ``W_endpoint=F_j(x_j-x_i)``.  The two non-negative defects are finite
sampling/integration-schedule resources, not material hysteresis.

The exact constant force that would reproduce the chord work over the whole jump
is the rational discrete-gradient/secant average

    F_exact = W_chord / (x_j-x_i)
            = chord_numerator2 / (2*(x_j-x_i)).

Using it requires endpoint information (or an implicit finite relation); the
current-causal world intentionally does not read the future endpoint when
choosing its force.  Discrete-gradient/trapezoidal energy accounting is established
numerical analysis.  E001 uses the identity to separate material work from
saved-state sampling effects.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .material_force_work import FiniteForceLaw


def _depth_pair(law: FiniteForceLaw, start_depth: int, end_depth: int) -> None:
    for name, value in (("start_depth", start_depth), ("end_depth", end_depth)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    if not 0 <= start_depth < end_depth < len(law.profile.loading):
        raise ValueError("require 0 <= start_depth < end_depth within the force law")


@dataclass(frozen=True)
class SavedForceSamplingWorkReport:
    start_depth: int
    end_depth: int
    deformation_span_counts: int
    start_force_count: int
    end_force_count: int
    current_hold_work_numerator2: int
    chord_work_numerator2: int
    endpoint_hold_work_numerator2: int
    current_sampling_defect_numerator2: int
    endpoint_sampling_defect_numerator2: int
    exact_average_force_numerator: int
    exact_average_force_denominator: int
    loading_nondecreasing_on_interval: bool
    current_hold_underestimates_chord: bool
    endpoint_hold_overestimates_chord: bool


def saved_force_sampling_work_report(
    law: FiniteForceLaw,
    start_depth: int,
    end_depth: int,
) -> SavedForceSamplingWorkReport:
    """Compare current-held, static chord, and endpoint-held loading work."""
    _depth_pair(law, start_depth, end_depth)
    grid = law.deformation_counts
    forces = law.profile.loading
    span = grid[end_depth] - grid[start_depth]
    start_force = forces[start_depth]
    end_force = forces[end_depth]
    current2 = 2 * start_force * span
    endpoint2 = 2 * end_force * span
    chord2 = 0
    for depth in range(start_depth + 1, end_depth + 1):
        width = grid[depth] - grid[depth - 1]
        chord2 += (forces[depth - 1] + forces[depth]) * width

    current_defect = chord2 - current2
    endpoint_defect = endpoint2 - chord2
    nondecreasing = all(
        forces[k - 1] <= forces[k]
        for k in range(start_depth + 1, end_depth + 1)
    )
    if nondecreasing and (current_defect < 0 or endpoint_defect < 0):
        raise AssertionError("monotone loading violated saved-force work ordering")

    average_num = chord2
    average_den = 2 * span
    common = gcd(abs(average_num), average_den)
    average_num //= common
    average_den //= common
    return SavedForceSamplingWorkReport(
        start_depth=start_depth,
        end_depth=end_depth,
        deformation_span_counts=span,
        start_force_count=start_force,
        end_force_count=end_force,
        current_hold_work_numerator2=current2,
        chord_work_numerator2=chord2,
        endpoint_hold_work_numerator2=endpoint2,
        current_sampling_defect_numerator2=current_defect,
        endpoint_sampling_defect_numerator2=endpoint_defect,
        exact_average_force_numerator=average_num,
        exact_average_force_denominator=average_den,
        loading_nondecreasing_on_interval=nondecreasing,
        current_hold_underestimates_chord=current_defect >= 0,
        endpoint_hold_overestimates_chord=endpoint_defect >= 0,
    )


def current_hold_work_over_explicit_saved_schedule(
    law: FiniteForceLaw,
    saved_depths: tuple[int, ...] | list[int],
) -> int:
    """Return doubled work for an explicitly sampled increasing-depth schedule.

    Every interval uses the force at its saved start.  No hidden material depth is
    inserted.  The result is a left-hold work coordinate on the declared schedule.
    """
    depths = tuple(saved_depths)
    if len(depths) < 2:
        raise ValueError("saved schedule must contain at least two depths")
    if any(
        isinstance(depth, bool) or not isinstance(depth, int)
        for depth in depths
    ):
        raise ValueError("saved depths must be integers")
    if any(right <= left for left, right in zip(depths, depths[1:])):
        raise ValueError("saved loading depths must be strictly increasing")
    if depths[0] < 0 or depths[-1] >= len(law.profile.loading):
        raise ValueError("saved schedule lies outside force law")
    total2 = 0
    for left, right in zip(depths, depths[1:]):
        width = law.deformation_counts[right] - law.deformation_counts[left]
        total2 += 2 * law.profile.loading[left] * width
    return total2
