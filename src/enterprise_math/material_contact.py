"""Minimal geometry-to-material coupling for the E001 pressure test.

The current square-body contact certificate already exposes one intrinsic integer
quantity: the minimum relative unit translation needed to leave common-collapse
contact.  This module uses that quantity as a *candidate discrete deformation
index* and nothing more.

No normalization, interpolation, saturation, force, velocity, mass, or energy
mapping is inserted.  If a material curve does not explicitly contain that
index, the state is reported as unrepresented by raising ``ValueError``.
"""

from __future__ import annotations

from dataclasses import dataclass

from .collapse_contact import collapse_contact_profile
from .engineering_collision import Body2D, Pair
from .material_hysteresis import MaterialBranch, MaterialHistoryState, material_state
from .material_response import MaterialCurveProfile


@dataclass(frozen=True)
class ContactMaterialObservation2D:
    """One contact geometry observed through an explicit finite material branch."""

    pair: Pair
    deformation_steps: int
    minimum_axes: tuple[str, ...]
    shared_target_count: int
    material_state: MaterialHistoryState


def contact_deformation_steps(left: Body2D, right: Body2D) -> int | None:
    """Return minimum relative unit separation steps, or None when not in contact."""
    contact = collapse_contact_profile(left, right)
    return None if contact is None else contact.minimum_axis_separation_steps


def observe_contact_material(
    left: Body2D,
    right: Body2D,
    profile: MaterialCurveProfile,
    branch: MaterialBranch,
) -> ContactMaterialObservation2D | None:
    """Map exact contact depth to one declared material-curve index.

    Separate supports produce ``None``.  A contact whose integer depth exceeds
    the represented curve domain is rejected rather than silently clamped.
    """
    contact = collapse_contact_profile(left, right)
    if contact is None:
        return None
    depth = contact.minimum_axis_separation_steps
    if depth >= len(profile.loading):
        raise ValueError("contact deformation depth is not represented by material curve")
    state = material_state(profile, depth, branch)
    return ContactMaterialObservation2D(
        pair=contact.pair,
        deformation_steps=depth,
        minimum_axes=contact.minimum_axes,
        shared_target_count=contact.shared_target_count,
        material_state=state,
    )
