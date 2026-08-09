"""Geometry-driven deformation history for the stacked E001 material line.

For the current square-body pressure test:

* separate supports map to deformation index 0;
* common-collapse contact maps to the exact minimum relative unit separation
  steps retained by ``collapse_contact_profile``.

A sequence of represented geometry states therefore induces a finite deformation
schedule without normalization or interpolation.  The existing material
hysteresis state machine then selects LOADING when depth increases and RETURNING
when depth decreases.

This closes only ``geometry history -> material history``.  It still does not
map material response samples back into force, velocity, or position updates.
"""

from __future__ import annotations

from dataclasses import dataclass

from .engineering_collision import Body2D, Pair
from .material_contact import contact_deformation_steps
from .material_hysteresis import (
    LOADING,
    MaterialBranch,
    MaterialHistoryState,
    trace_deformation_schedule,
)
from .material_response import MaterialCurveProfile

BodyPairState2D = tuple[Body2D, Body2D]


@dataclass(frozen=True)
class ContactMaterialHistory2D:
    """One finite geometry/deformation/material-history trace."""

    pair: Pair
    deformation_schedule: tuple[int, ...]
    material_states: tuple[MaterialHistoryState, ...]
    peak_deformation: int
    contact_state_count: int
    separate_state_count: int


def contact_deformation_schedule(
    pair_states: tuple[BodyPairState2D, ...] | list[BodyPairState2D],
) -> tuple[Pair, tuple[int, ...]]:
    """Convert represented body-pair states into exact integer deformation depths."""
    states = tuple(pair_states)
    if not states:
        raise ValueError("body-pair history must be nonempty")

    first_left, first_right = states[0]
    if first_left.body_id == first_right.body_id:
        raise ValueError("history pair must contain distinct body ids")
    pair = tuple(sorted((first_left.body_id, first_right.body_id)))

    depths: list[int] = []
    for left, right in states:
        if tuple(sorted((left.body_id, right.body_id))) != pair:
            raise ValueError("body-pair identity changed inside contact history")
        depth = contact_deformation_steps(left, right)
        depths.append(0 if depth is None else depth)
    return pair, tuple(depths)


def trace_contact_material_history(
    pair_states: tuple[BodyPairState2D, ...] | list[BodyPairState2D],
    profile: MaterialCurveProfile,
    initial_branch: MaterialBranch = LOADING,
) -> ContactMaterialHistory2D:
    """Trace material loading/returning directly from represented contact depths."""
    pair, schedule = contact_deformation_schedule(pair_states)
    if max(schedule) >= len(profile.loading):
        raise ValueError("contact history exceeds represented material deformation domain")
    material_states = trace_deformation_schedule(
        profile, schedule, initial_branch
    )
    contact_count = sum(depth > 0 for depth in schedule)
    return ContactMaterialHistory2D(
        pair=pair,
        deformation_schedule=schedule,
        material_states=material_states,
        peak_deformation=max(schedule),
        contact_state_count=contact_count,
        separate_state_count=len(schedule) - contact_count,
    )
