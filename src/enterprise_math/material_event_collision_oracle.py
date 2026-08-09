"""Event-driven material rebound oracle inside the precision-generated layer.

The collapse interaction scale ``d`` supplies only ``d-1`` positive-gap material
depths before primitive contact.  A force law independently supplies a finite
material depth and exact loading/return work prefixes.  This module composes those
resources without prescribing a post-collision velocity.

For incoming whole momentum p in the unit work/momentum comparison coordinate,
kinetic resource is ``p^2``.  Let

    K_spatial = d-1,
    K_material = len(profile)-1,
    K_rep = min(K_spatial,K_material).

Search loading work only through ``K_rep``:

* exact equality at K gives a represented turn before primitive contact;
* a strict work bracket gives ``TURN_UNDERRESOLVED`` -- the turning deformation
  lies inside one material cell and is not interpolated;
* if incoming work exceeds the deepest jointly represented work, the limiting
  resource is reported explicitly as spatial, material, or both.

At an exact turn the branch-aware ``material_turn_return_witness`` supplies
outgoing momentum and loading/return durations from the declared returning work.
Thus the precision-generated layer is capacity; the force-work geometry decides
whether that capacity is sufficient to turn the body.

This is an event-level engineering oracle.  A high-speed saved tick can still
skip the interaction layer completely under the active endpoint-only world; this
oracle applies only once a material interaction event has been declared.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_force_work import FiniteForceLaw, force_cycle_work_report
from .material_turn_return_witness import (
    EXACT_TURN_RETURN,
    MaterialTurnReturnWitness,
    material_turn_return_witness,
)

NO_POSITIVE_INTERACTION_LAYER = "NO_POSITIVE_INTERACTION_LAYER"
EXACT_MATERIAL_BOUNCE = "EXACT_MATERIAL_BOUNCE"
TURN_UNDERRESOLVED = "TURN_UNDERRESOLVED"
SPATIAL_LAYER_EXHAUSTED = "SPATIAL_LAYER_EXHAUSTED"
MATERIAL_DEPTH_EXHAUSTED = "MATERIAL_DEPTH_EXHAUSTED"
SPATIAL_AND_MATERIAL_EXHAUSTED = "SPATIAL_AND_MATERIAL_EXHAUSTED"


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


@dataclass(frozen=True)
class MaterialEventCollisionReport:
    collapse_factor: int
    incoming_momentum: int
    spatial_max_depth: int
    material_max_depth: int
    represented_max_depth: int
    incoming_work_resource_numerator2: int
    represented_loading_work_prefixes_numerator2: tuple[int, ...]
    status: str
    lower_turn_depth: int | None
    upper_turn_depth: int | None
    exact_turn_depth: int | None
    turn_return: MaterialTurnReturnWitness | None

    @property
    def outgoing_momentum(self) -> int | None:
        return None if self.turn_return is None else self.turn_return.outgoing_momentum


def material_event_collision_report(
    law: FiniteForceLaw,
    collapse_factor: int,
    incoming_momentum: int,
    mass_count: int = 1,
) -> MaterialEventCollisionReport:
    """Classify whether the finite interaction/material depth supports a full bounce."""
    _positive("collapse_factor", collapse_factor)
    _positive("incoming_momentum", incoming_momentum)
    _positive("mass_count", mass_count)
    spatial_max = collapse_factor - 1
    material_max = len(law.profile.loading) - 1
    represented_max = min(spatial_max, material_max)
    energy = incoming_momentum * incoming_momentum
    prefixes = tuple(
        force_cycle_work_report(law, depth).loading_work_numerator2
        for depth in range(represented_max + 1)
    )
    if represented_max == 0:
        return MaterialEventCollisionReport(
            collapse_factor=collapse_factor,
            incoming_momentum=incoming_momentum,
            spatial_max_depth=spatial_max,
            material_max_depth=material_max,
            represented_max_depth=represented_max,
            incoming_work_resource_numerator2=energy,
            represented_loading_work_prefixes_numerator2=prefixes,
            status=NO_POSITIVE_INTERACTION_LAYER,
            lower_turn_depth=None,
            upper_turn_depth=None,
            exact_turn_depth=None,
            turn_return=None,
        )

    for depth in range(1, represented_max + 1):
        work = prefixes[depth]
        if energy == work:
            witness = material_turn_return_witness(
                law, incoming_momentum, mass_count=mass_count
            )
            status = EXACT_MATERIAL_BOUNCE if witness.status == EXACT_TURN_RETURN else witness.status
            return MaterialEventCollisionReport(
                collapse_factor=collapse_factor,
                incoming_momentum=incoming_momentum,
                spatial_max_depth=spatial_max,
                material_max_depth=material_max,
                represented_max_depth=represented_max,
                incoming_work_resource_numerator2=energy,
                represented_loading_work_prefixes_numerator2=prefixes,
                status=status,
                lower_turn_depth=depth,
                upper_turn_depth=depth,
                exact_turn_depth=depth,
                turn_return=witness,
            )
        if energy < work:
            return MaterialEventCollisionReport(
                collapse_factor=collapse_factor,
                incoming_momentum=incoming_momentum,
                spatial_max_depth=spatial_max,
                material_max_depth=material_max,
                represented_max_depth=represented_max,
                incoming_work_resource_numerator2=energy,
                represented_loading_work_prefixes_numerator2=prefixes,
                status=TURN_UNDERRESOLVED,
                lower_turn_depth=depth - 1,
                upper_turn_depth=depth,
                exact_turn_depth=None,
                turn_return=None,
            )

    if spatial_max < material_max:
        status = SPATIAL_LAYER_EXHAUSTED
    elif material_max < spatial_max:
        status = MATERIAL_DEPTH_EXHAUSTED
    else:
        status = SPATIAL_AND_MATERIAL_EXHAUSTED
    return MaterialEventCollisionReport(
        collapse_factor=collapse_factor,
        incoming_momentum=incoming_momentum,
        spatial_max_depth=spatial_max,
        material_max_depth=material_max,
        represented_max_depth=represented_max,
        incoming_work_resource_numerator2=energy,
        represented_loading_work_prefixes_numerator2=prefixes,
        status=status,
        lower_turn_depth=represented_max,
        upper_turn_depth=None,
        exact_turn_depth=None,
        turn_return=None,
    )
