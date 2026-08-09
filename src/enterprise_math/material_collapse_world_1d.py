"""Automatic coarse-layer material rebound world for sampled 1D wall jumps.

This composes explicit E001 engineering policies while separating *contact state*
from *response trigger*:

1. positive sampled gap ``g`` belongs to the coarse interaction layer iff ``g<d``;
2. coarse-only layer depth is ``kappa=d-g``;
3. a response is triggered only when a proposal crosses the wall between
   separated sampled sides or moves closer to the wall while the controlling
   sampled gap lies in the layer;
4. same-side HOLD or retreat is accepted, even if the represented start state is
   still inside the coarse layer, so unloading can leave the interaction layer;
5. on trigger, the RETURNING branch sample at layer depth splits the incoming
   displacement budget by ``floor(B*r/A)`` and sends the returned budget opposite
   the proposal.

If a crossing proposal is resolved at the current factor it transmits directly.
Primitive endpoint contact ``g=0`` is rejected from this coarse-layer helper and
must use explicit terminal contact geometry instead.

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
NO_TRIGGER = "NO_TRIGGER"
CROSSING_CONTACT = "CROSSING_CONTACT"
APPROACH_CONTACT = "APPROACH_CONTACT"


@dataclass(frozen=True)
class CollapseMaterialWorldOutcome1D:
    """One finite after-state with material state derived from collapse depth."""

    kind: str
    trigger_reason: str
    start_center: int
    proposed_end_center: int
    after_center: int
    radius: int
    collapse_factor: int
    start_clearance: int
    end_clearance: int
    crosses_between_separated_sides: bool
    approaching_wall: bool
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
    approaching = end_gap < start_gap
    controlling_gap = min(start_gap, end_gap)
    layer_contact = controlling_gap < collapse_factor
    should_rebound = layer_contact and (crosses or approaching)

    if not should_rebound:
        return CollapseMaterialWorldOutcome1D(
            kind=TRANSMIT if crosses else ACCEPT,
            trigger_reason=NO_TRIGGER,
            start_center=start_center,
            proposed_end_center=proposed_end_center,
            after_center=proposed_end_center,
            radius=radius,
            collapse_factor=collapse_factor,
            start_clearance=start_gap,
            end_clearance=end_gap,
            crosses_between_separated_sides=crosses,
            approaching_wall=approaching,
            layer_material=None,
            rebound=None,
        )

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
        raise AssertionError("rebound trigger did not produce a coarse layer material state")

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
        trigger_reason=CROSSING_CONTACT if crosses else APPROACH_CONTACT,
        start_center=start_center,
        proposed_end_center=proposed_end_center,
        after_center=after,
        radius=radius,
        collapse_factor=collapse_factor,
        start_clearance=start_gap,
        end_clearance=end_gap,
        crosses_between_separated_sides=crosses,
        approaching_wall=approaching,
        layer_material=observation,
        rebound=rebound,
    )
