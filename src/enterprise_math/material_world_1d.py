"""One explicit 1D sampled wall world coupling E001 material response to after-state.

This is a deliberately small engineering world law, not a claim about physical
mechanics.  It keeps the active E001 sampled-jump semantics:

* only represented pre/post body states are inspected;
* no hidden intermediate path is reconstructed;
* a positive primitive wall clearance ``g`` collapses to macro contact at
  spatial factor ``d`` exactly when ``g<d``;
* if neither sampled endpoint is in macro contact, the proposed end state is
  accepted directly (including a separated-side wall transmission);
* if sampled macro contact is present, the forward proposal is rejected and a
  declared material return ratio converts the incoming integer displacement
  budget into an opposite-direction rebound from the represented start state.

The rebound ratio is supplied by ``material_kinematic_coupling``.  No mass,
force, impulse, energy, continuous trajectory, or hidden collision point is used.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_hysteresis import MaterialHistoryState
from .material_kinematic_coupling import ReboundBudget, rebound_budget_from_material_state
from .scale_tunneling_1d import BodyInterval1D, Wall1D, interval_wall_clearance

ACCEPT = "ACCEPT"
TRANSMIT = "TRANSMIT"
REBOUND = "REBOUND"
WorldOutcomeKind = str


@dataclass(frozen=True)
class MaterialWallOutcome1D:
    """One exact finite after-state under the declared sampled-wall policy."""

    kind: WorldOutcomeKind
    start_center: int
    proposed_end_center: int
    after_center: int
    radius: int
    collapse_factor: int
    start_clearance: int
    proposed_end_clearance: int
    start_macro_contact: bool
    proposed_end_macro_contact: bool
    crosses_between_separated_sides: bool
    incoming_direction: int
    incoming_budget: int
    rebound: ReboundBudget | None


def _require_positive_factor(collapse_factor: int) -> None:
    if (
        isinstance(collapse_factor, bool)
        or not isinstance(collapse_factor, int)
        or collapse_factor <= 0
    ):
        raise ValueError("collapse_factor must be a positive integer")


def _separated_side_crossing(
    start: BodyInterval1D,
    end: BodyInterval1D,
    wall: Wall1D,
) -> bool:
    return (
        start.hi < wall.lo and end.lo > wall.hi
    ) or (
        start.lo > wall.hi and end.hi < wall.lo
    )


def material_wall_step(
    wall: Wall1D,
    start_center: int,
    proposed_end_center: int,
    radius: int,
    collapse_factor: int,
    material_state: MaterialHistoryState,
    material_amplitude: int,
) -> MaterialWallOutcome1D:
    """Evaluate one sampled proposal under the explicit rebound/transmit law."""
    _require_positive_factor(collapse_factor)
    start = BodyInterval1D(start_center, radius)
    end = BodyInterval1D(proposed_end_center, radius)
    start_gap = interval_wall_clearance(start, wall)
    end_gap = interval_wall_clearance(end, wall)
    if start_gap == 0:
        raise ValueError("material wall step requires a primitively separated start state")

    delta = proposed_end_center - start_center
    direction = 0 if delta == 0 else 1 if delta > 0 else -1
    incoming_budget = abs(delta)
    start_macro = start_gap < collapse_factor
    end_macro = end_gap < collapse_factor
    crosses = _separated_side_crossing(start, end, wall)

    if not start_macro and not end_macro:
        kind = TRANSMIT if crosses else ACCEPT
        return MaterialWallOutcome1D(
            kind=kind,
            start_center=start_center,
            proposed_end_center=proposed_end_center,
            after_center=proposed_end_center,
            radius=radius,
            collapse_factor=collapse_factor,
            start_clearance=start_gap,
            proposed_end_clearance=end_gap,
            start_macro_contact=False,
            proposed_end_macro_contact=False,
            crosses_between_separated_sides=crosses,
            incoming_direction=direction,
            incoming_budget=incoming_budget,
            rebound=None,
        )

    rebound = rebound_budget_from_material_state(
        incoming_budget,
        material_state,
        material_amplitude,
    )
    after = start_center - direction * rebound.returned_budget
    return MaterialWallOutcome1D(
        kind=REBOUND,
        start_center=start_center,
        proposed_end_center=proposed_end_center,
        after_center=after,
        radius=radius,
        collapse_factor=collapse_factor,
        start_clearance=start_gap,
        proposed_end_clearance=end_gap,
        start_macro_contact=start_macro,
        proposed_end_macro_contact=end_macro,
        crosses_between_separated_sides=crosses,
        incoming_direction=direction,
        incoming_budget=incoming_budget,
        rebound=rebound,
    )
