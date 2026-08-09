"""Midpoint-exact time sampling can still change material outcome.

The causal midpoint world removes the constant-force pre/post integration defect,
but it does not make different saved-state time cadences semantically identical.
This module gives an exact no-remainder family where the same physical total time
transmits under one coarse saved tick and reverses under explicit substeps because
the substeps visit a material layer that the coarse current-state sample never
sees.

Choose an even positive free-drift count ``s``, an integer substep count ``m>=4``,
and collapse factor d satisfying

    3*s/2 < d < (m-1)*s.

Use point geometry, unit count scales/mass, material amplitude 1, a constant
positive loading/returning sample 1 through depth ``3*s/2``, full-scale force
count ``s``, initial center ``-(d+s)``, and momentum count ``s``.

Coarse time
-----------
One tick of duration count m starts outside the interaction layer, samples zero
material force, and free-drifts exactly ``m*s`` cells.  Its final center

    (m-1)*s-d > 0

lies on the opposite separated side, so the saved transition transmits.

Fine time
---------
Run m ticks of duration count 1 with the same force law and total physical time.
The first two free ticks visit gaps ``d`` and ``d-s``.  The third tick starts at
material depth s; force impulse ``-s`` stalls momentum from s to 0.  Midpoint
drift moves inward exactly ``s/2`` cells.  The fourth tick samples the still-
represented material layer, changes momentum 0 -> -s, and midpoint-drifts outward
``s/2`` cells.  Lifted momentum has therefore reversed.

All divisions are exact because s is even and amplitude/physical scales are one.
The mismatch is not a projection or integrator defect.  It is a saved-state
material-support sampling effect.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_physical_impulse_world_1d import PhysicalLiftedMaterialScale1D
from .material_physical_midpoint_world_1d import (
    CROSSING_TRANSMIT,
    PhysicalMidpointMaterialState1D,
    PhysicalMidpointMaterialTransition1D,
    physical_midpoint_material_step_1d,
)
from .material_physical_projection import ForceImpulseCountScale, MomentumDriftCountScale
from .material_response import explicit_material_curve_profile
from .scale_tunneling_1d import Wall1D

COARSE_TRANSMIT = "COARSE_TRANSMIT"
FINE_REVERSE = "FINE_REVERSE"


def _scale(force_count: int, tick_duration: int) -> PhysicalLiftedMaterialScale1D:
    return PhysicalLiftedMaterialScale1D(
        full_scale_force_count=force_count,
        force_impulse=ForceImpulseCountScale(
            force_scale_factor=1,
            time_scale_factor=1,
            momentum_scale_factor=1,
            tick_duration_count=tick_duration,
            force_unit="F",
            time_unit="t",
            momentum_unit="p",
        ),
        momentum_drift=MomentumDriftCountScale(
            momentum_scale_factor=1,
            mass_scale_factor=1,
            time_scale_factor=1,
            position_scale_factor=1,
            tick_duration_count=tick_duration,
            mass_count=1,
            momentum_unit="p",
            mass_unit="m",
            time_unit="t",
            position_unit="x",
        ),
    )


@dataclass(frozen=True)
class MidpointTimeSamplingWitness:
    substep_count: int
    free_drift_count: int
    collapse_factor: int
    initial_center: int
    initial_momentum: int
    coarse_transition: PhysicalMidpointMaterialTransition1D
    fine_transitions: tuple[PhysicalMidpointMaterialTransition1D, ...]
    outcome_pair: tuple[str, str]
    first_fine_reversal_tick: int


def midpoint_time_sampling_witness(
    substep_count: int,
    free_drift_count: int,
    collapse_factor: int,
) -> MidpointTimeSamplingWitness:
    """Construct the exact coarse-transmit / fine-reverse midpoint family."""
    m = substep_count
    s = free_drift_count
    d = collapse_factor
    for name, value in (("substep_count", m), ("free_drift_count", s), ("collapse_factor", d)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    if m < 4:
        raise ValueError("substep_count must be at least 4")
    if s <= 0 or s % 2:
        raise ValueError("free_drift_count must be a positive even integer")
    if not 3 * s < 2 * d < 2 * (m - 1) * s:
        raise ValueError("require 3*s/2 < d < (m-1)*s")

    max_depth = 3 * s // 2
    profile = explicit_material_curve_profile(
        loading=(0,) + (1,) * max_depth,
        returning=(0,) + (1,) * max_depth,
        amplitude=1,
    )
    wall = Wall1D(0, 0)
    initial = PhysicalMidpointMaterialState1D(
        center_count=-(d + s),
        momentum_count=s,
    )
    coarse = physical_midpoint_material_step_1d(
        initial,
        wall,
        radius=0,
        collapse_factor=d,
        material_profile=profile,
        scale=_scale(s, m),
    )
    if coarse.kind != CROSSING_TRANSMIT:
        raise AssertionError("coarse midpoint witness did not transmit")

    current = initial
    transitions: list[PhysicalMidpointMaterialTransition1D] = []
    first_reversal = None
    fine_scale = _scale(s, 1)
    for tick in range(m):
        transition = physical_midpoint_material_step_1d(
            current,
            wall,
            radius=0,
            collapse_factor=d,
            material_profile=profile,
            scale=fine_scale,
        )
        transitions.append(transition)
        if transition.lifted_momentum_reversed and first_reversal is None:
            first_reversal = tick
        if transition.after is None:
            break
        current = transition.after
    if first_reversal is None:
        raise AssertionError("fine midpoint witness did not reverse")
    for transition in transitions:
        if transition.momentum_detail_after not in (None, 0):
            raise AssertionError("midpoint witness unexpectedly used momentum remainder")
        if transition.midpoint_position_detail_after not in (None, 0):
            raise AssertionError("midpoint witness unexpectedly used position remainder")

    return MidpointTimeSamplingWitness(
        substep_count=m,
        free_drift_count=s,
        collapse_factor=d,
        initial_center=initial.center_count,
        initial_momentum=initial.momentum_count,
        coarse_transition=coarse,
        fine_transitions=tuple(transitions),
        outcome_pair=(COARSE_TRANSMIT, FINE_REVERSE),
        first_fine_reversal_tick=first_reversal,
    )
