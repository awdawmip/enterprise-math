"""Automatic coarse-layer material response world for sampled 1D wall jumps.

This composes explicit E001 engineering policies while separating *contact state*
from *response trigger*, *material representability*, and *nonzero kinematic
return*:

1. positive sampled gap ``g`` belongs to the coarse interaction layer iff ``g<d``;
2. coarse-only layer depth is ``kappa=d-g``;
3. a response is triggered only when a proposal crosses the wall between
   separated sampled sides or moves closer to the wall while the controlling
   sampled gap lies in the layer;
4. same-side HOLD or retreat is accepted, even if the represented start state is
   still inside a coarse layer, so unloading can leave that layer;
5. if a triggered coarse layer asks for deformation depth beyond the finite
   material profile, the result is explicit ``MATERIAL_UNDERRESOLVED`` rather
   than clamping/saturating to the deepest represented material state;
6. a represented triggered layer evaluates the RETURNING branch and maps that
   finite response sample into an opposite-direction returned budget;
7. only a strictly positive returned budget is called ``REBOUND``.  A represented
   interaction whose returned budget quantizes to zero is ``ZERO_RETURN`` and
   remains at the represented start under the current explicit blocking policy.

If a crossing proposal is resolved at the current factor it transmits directly.
Primitive endpoint contact ``g=0`` remains outside this coarse positive-gap helper
and must use explicit terminal contact geometry instead.

This is a fully explicit toy world law, not a physical constitutive model.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_collapse_layer import (
    CollapseLayerMaterialObservation1D,
    sampled_wall_layer_material,
)
from .material_hysteresis import RETURNING
from .material_kinematic_coupling import ReboundBudget, rebound_budget_from_material_state
from .material_precision_compatibility import (
    MATERIAL_UNDERRESOLVED,
    REPRESENTED_CONTACT,
    RESOLVED,
    spatial_material_compatibility,
)
from .material_response import MaterialCurveProfile
from .scale_tunneling_1d import BodyInterval1D, Wall1D, interval_wall_clearance

TRANSMIT = "TRANSMIT"
ACCEPT = "ACCEPT"
REBOUND = "REBOUND"
ZERO_RETURN = "ZERO_RETURN"
UNDERRESOLVED = MATERIAL_UNDERRESOLVED
NO_TRIGGER = "NO_TRIGGER"
CROSSING_CONTACT = "CROSSING_CONTACT"
APPROACH_CONTACT = "APPROACH_CONTACT"


@dataclass(frozen=True)
class CollapseMaterialWorldOutcome1D:
    """One finite after-state or explicit material-precision incompatibility."""

    kind: str
    trigger_reason: str
    start_center: int
    proposed_end_center: int
    after_center: int | None
    radius: int
    collapse_factor: int
    start_clearance: int
    end_clearance: int
    crosses_between_separated_sides: bool
    approaching_wall: bool
    material_precision_status: str
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
    """Evaluate one positive-gap sampled proposal end to end.

    Material underresolution is only blocking when the proposal actually needs a
    material response.  HOLD/retreat may leave an underresolved coarse layer
    without synthesizing a response because no loading/crossing response is
    being requested on that step.
    """
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
    compatibility = spatial_material_compatibility(
        controlling_gap,
        collapse_factor,
        material_profile,
    )
    layer_contact = compatibility.status != RESOLVED
    should_respond = layer_contact and (crosses or approaching)

    if not should_respond:
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
            material_precision_status=compatibility.status,
            layer_material=None,
            rebound=None,
        )

    trigger_reason = CROSSING_CONTACT if crosses else APPROACH_CONTACT
    if compatibility.status == MATERIAL_UNDERRESOLVED:
        return CollapseMaterialWorldOutcome1D(
            kind=UNDERRESOLVED,
            trigger_reason=trigger_reason,
            start_center=start_center,
            proposed_end_center=proposed_end_center,
            after_center=None,
            radius=radius,
            collapse_factor=collapse_factor,
            start_clearance=start_gap,
            end_clearance=end_gap,
            crosses_between_separated_sides=crosses,
            approaching_wall=approaching,
            material_precision_status=compatibility.status,
            layer_material=None,
            rebound=None,
        )
    if compatibility.status != REPRESENTED_CONTACT:
        raise AssertionError("triggered coarse contact escaped material precision classification")

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
        raise AssertionError("represented response trigger lost its coarse layer material state")

    delta = proposed_end_center - start_center
    direction = 0 if delta == 0 else 1 if delta > 0 else -1
    incoming_budget = abs(delta)
    rebound = rebound_budget_from_material_state(
        incoming_budget,
        observation.material_state,
        material_profile.amplitude,
    )
    after = start_center - direction * rebound.returned_budget
    kind = REBOUND if rebound.returned_budget > 0 else ZERO_RETURN
    return CollapseMaterialWorldOutcome1D(
        kind=kind,
        trigger_reason=trigger_reason,
        start_center=start_center,
        proposed_end_center=proposed_end_center,
        after_center=after,
        radius=radius,
        collapse_factor=collapse_factor,
        start_clearance=start_gap,
        end_clearance=end_gap,
        crosses_between_separated_sides=crosses,
        approaching_wall=approaching,
        material_precision_status=compatibility.status,
        layer_material=observation,
        rebound=rebound,
    )
