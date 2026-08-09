"""Automatic coarse-layer material rebound world for sampled 1D wall jumps.

This composes three already-declared E001 engineering policies:

1. positive sampled gap ``g`` enters macro contact iff ``g<d``;
2. coarse-only interaction-layer depth is ``kappa=d-g``;
3. the RETURNING branch sample at that depth splits the incoming displacement
   budget by ``floor(B*r/A)`` and sends the returned budget opposite the proposal.

If both sampled gaps are resolved at the current factor, the proposed state is
accepted directly, including legal wall transmission.  Primitive endpoint
contact ``g=0`` is rejected from this coarse-layer helper and must use explicit
terminal contact geometry instead.

This is a fully explicit toy world law, not a physical constitutive model.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_collapse_layer import CollapseLayerMaterialObservation1D, sampled_wall_layer_material
from .material_hysteresis import RETURNING
from .material_kinematic_coupling import ReboundBudget, rebound_budget_from_material_state
from .material_response import MaterialCurveProfile
from .scale_tunneling_1d import BodyInterval1D, Wall1D, interval_wall_clearance

TRANSMIT = "TRANSMIT"
ACCEPT = "ACCEPT"
REBOUND = "REBOUND"


@dataclass(frozen=True)
class CollapseMaterialWorldOutcome1D:
    """One finite after-state with the material state derived from collapse depth."""

    kind: str
    start_center: int
    proposed_end_center: int
    after_center: int
    radius: int
    collapse_factor: int
    start_clearance: int
    end_clearance: int
    crosses_between_separated_sides: bool
    layer_material: CollapseLayerMaterialObservation1D | None
    rebound: ReboundBudget | None


def _crosses(start: BodyInterval1D, end: BodyInterval1D, wall: Wall1D) -> bool:
    return (
        start.hi < wall.lo and end.lo > wall.hi
    ) or (
        start.lo > wall.hi and end.hi < wall.lo
    )


def collapse_material_wall_step(
    wall: Wall1D,
    start_center: int,
    proposed_end_center: int,
    radius: int,
    collapse_factor: int,
    material_profile: MaterialCurveProfile,
) -> CollapseMaterialWorldOutcome1D:
    """Evaluate one positive-gap sampled proposal end to end."""
    start = BodyInterval1D(start_center, radius)
    end = BodyInterval1D(proposed_end_center, radius)
    start_gap = interval_wall_clearance(start, wall)
    end_gap = interval_wall_clearance(end, wall)
    if start_gap == 0 or end_gap == 0:
        raise ValueError(
            "coarse collapse-material world requires positive primitive gaps at both sampled endpoints"
        )

    crosses = _crosses(start, end, wall)
    observation = sampled_wall_layer_material(
        wall,
        start_center,
        proposed_end_center,
        radius,
        collapse_factor,
        material_profile,
        RETURNING,
    )
    if observation is None:
        return CollapseMaterialWorldOutcome1D(
            kind=TRANSMIT if crosses else ACCEPT,
            start_center=start_center,
            proposed_end_center=proposed_end_center,
            after_center=proposed_end_center,
            radius=radius,
            collapse_factor=collapse_factor,
            start_clearance=start_gap,
            end_clearance=end_gap,
            crosses_between_separated_sides=crosses,
            layer_material=None,
            rebound=None,
        )

    delta = proposed_end_center - start_center
    direction = 0 if delta == 0 else 1 if delta > 0 else -1
    incoming_budget = abs(delta)
    rebound = rebound_budget_from_material_state(
        incoming_budget,
        observation.material_state,
        material_profile.amplitude,
    )
    after = start_center - direction * rebound.returned_budget
    return CollapseMaterialWorldOutcome1D(
        kind=REBOUND,
        start_center=start_center,
        proposed_end_center=proposed_end_center,
        after_center=after,
        radius=radius,
        collapse_factor=collapse_factor,
        start_clearance=start_gap,
        end_clearance=end_gap,
        crosses_between_separated_sides=crosses,
        layer_material=observation,
        rebound=rebound,
    )
