"""Exact coarse-time transmit / fine-time reverse family in the causal impulse world.

Time refinement is an explicit dynamics change in E001, not a hidden collision
sweep.  This module gives an infinite family where changing only the saved-state
time cadence changes the material outcome even though every relevant division is
exact and no projection remainder is responsible.

Choose integers

    m >= 4,     q >= 1,     q < d < (m-1)q.

Use a point wall at 0, point body initially at center ``-(d+q)``, inward momentum
``p=m*q``, and a material profile of amplitude 1 whose positive depths through q
all return sample 1.

Coarse full interval
--------------------
Use mass divisor 1.  The current saved state is outside the interaction layer, so
no force is sampled.  One drift of ``m*q`` cells lands at

    (m-1)q-d > 0,

on the opposite separated side: CROSSING_TRANSMIT.

Explicit m-substep interval
---------------------------
Scale the drift divisor to ``m`` and the full force/impulse capacity by the same
time partition.  The substep momentum remains ``m*q`` before force, hence every
free drift is exactly q cells.  Saved positions reach

    -(d+q) -> -d -> -(d-q).

The third saved state has gap ``d-q<d`` and layer depth q.  Set each substep
maximum impulse capacity to ``m*q``; at full response the first material kick is
exactly ``-p`` and stalls momentum at zero, while the next identical kick makes
momentum ``-p`` and the body drifts outward by q cells.  Thus the refined world
records true momentum reversal.

All force and drift quotients in this construction divide exactly.  Therefore
the mismatch

    coarse-time TRANSMIT != fine-time REVERSE

is caused by explicit saved-state sampling of material support, not by dropped
integer detail.  No hidden intermediate states are inserted into the coarse
world.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_impulse_world_1d import (
    CROSSING_TRANSMIT,
    ImpulseMaterialHistory1D,
    MomentumMaterialState1D,
    run_impulse_material_world_1d,
)
from .material_response import MaterialCurveProfile, explicit_material_curve_profile
from .scale_tunneling_1d import Wall1D

COARSE_TRANSMIT = "COARSE_TRANSMIT"
FINE_REVERSE = "FINE_REVERSE"


@dataclass(frozen=True)
class TimeSamplingDivergenceWitness1D:
    substeps: int
    free_drift_cells_per_substep: int
    collapse_factor: int
    initial_center: int
    initial_momentum: int
    full_interval_mass_divisor: int
    refined_mass_divisor: int
    full_interval_impulse_capacity: int
    refined_impulse_capacity: int
    profile: MaterialCurveProfile
    coarse_history: ImpulseMaterialHistory1D
    refined_history: ImpulseMaterialHistory1D
    outcome_pair: tuple[str, str]


def time_sampling_divergence_witness(
    substeps: int,
    free_drift_cells_per_substep: int,
    collapse_factor: int,
) -> TimeSamplingDivergenceWitness1D:
    """Construct one exact no-remainder time-cadence divergence witness."""
    m = substeps
    q = free_drift_cells_per_substep
    d = collapse_factor
    for name, value in (("substeps", m), ("free_drift_cells_per_substep", q), ("collapse_factor", d)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    if m < 4:
        raise ValueError("substeps must be at least 4")
    if q <= 0:
        raise ValueError("free_drift_cells_per_substep must be positive")
    if not q < d < (m - 1) * q:
        raise ValueError("collapse_factor must satisfy q < d < (m-1)q")

    momentum = m * q
    initial_center = -(d + q)
    profile = explicit_material_curve_profile(
        loading=(0,) + (1,) * q,
        returning=(0,) + (1,) * q,
        amplitude=1,
    )
    initial = MomentumMaterialState1D(initial_center, momentum)
    wall = Wall1D(0, 0)

    # A full interval with constant full-response force would have capacity m
    # times the refined per-substep capacity.  It is not sampled in the coarse
    # trajectory because the current saved state lies outside the layer.
    refined_capacity = momentum
    full_capacity = m * refined_capacity
    coarse = run_impulse_material_world_1d(
        initial,
        wall,
        radius=0,
        collapse_factor=d,
        material_profile=profile,
        mass_quanta=1,
        max_impulse_per_tick=full_capacity,
        ticks=1,
        retain_impulse_detail=True,
    )
    refined = run_impulse_material_world_1d(
        initial,
        wall,
        radius=0,
        collapse_factor=d,
        material_profile=profile,
        mass_quanta=m,
        max_impulse_per_tick=refined_capacity,
        ticks=m,
        retain_impulse_detail=True,
    )

    if not coarse.transitions or coarse.transitions[0].kind != CROSSING_TRANSMIT:
        raise AssertionError("coarse-time witness did not transmit")
    if refined.first_reversal_tick is None:
        raise AssertionError("fine-time witness did not reverse")
    # The construction is intentionally remainder-free at all nonzero material
    # kicks: A=1 and p is divisible by m.
    for transition in refined.transitions:
        if transition.impulse is not None and transition.impulse.next_detail_numerator != 0:
            raise AssertionError("fine-time witness unexpectedly used impulse remainder")
        if transition.drift_cells is not None and transition.after is not None:
            momentum_after = transition.after.momentum_quanta
            if momentum_after % m != 0:
                raise AssertionError("fine-time witness unexpectedly used drift quotient remainder")

    return TimeSamplingDivergenceWitness1D(
        substeps=m,
        free_drift_cells_per_substep=q,
        collapse_factor=d,
        initial_center=initial_center,
        initial_momentum=momentum,
        full_interval_mass_divisor=1,
        refined_mass_divisor=m,
        full_interval_impulse_capacity=full_capacity,
        refined_impulse_capacity=refined_capacity,
        profile=profile,
        coarse_history=coarse,
        refined_history=refined,
        outcome_pair=(COARSE_TRANSMIT, FINE_REVERSE),
    )
