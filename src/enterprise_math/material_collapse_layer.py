"""Map E001 coarse positive-gap interaction-layer depth into material state.

This module is intentionally restricted to *coarse-only* contact where sampled
primitive wall clearances remain positive.  Primitive overlap ``g=0`` is not
assigned the synthetic depth ``d``; it must use explicit terminal overlap/contact
geometry instead.
"""

from __future__ import annotations

from dataclasses import dataclass

from .collapse_interaction_layer import collapse_layer_depth
from .material_hysteresis import MaterialBranch, MaterialHistoryState, RETURNING, material_state
from .material_response import MaterialCurveProfile
from .scale_tunneling_1d import BodyInterval1D, Wall1D, interval_wall_clearance

START = "START"
END = "END"
BOTH = "BOTH"
TriggerSample = str


@dataclass(frozen=True)
class CollapseLayerMaterialObservation1D:
    """One coarse-only wall-contact depth observed through a material branch."""

    collapse_factor: int
    start_clearance: int
    end_clearance: int
    controlling_clearance: int
    layer_depth: int
    trigger_sample: TriggerSample
    material_state: MaterialHistoryState


def sampled_wall_layer_material(
    wall: Wall1D,
    start_center: int,
    end_center: int,
    radius: int,
    collapse_factor: int,
    profile: MaterialCurveProfile,
    branch: MaterialBranch = RETURNING,
) -> CollapseLayerMaterialObservation1D | None:
    """Return coarse positive-gap material state, None if no sampled macro contact.

    Raises when either sampled endpoint has primitive contact/overlap because that
    case belongs to terminal contact geometry, not the coarse positive-gap layer.
    """
    start = BodyInterval1D(start_center, radius)
    end = BodyInterval1D(end_center, radius)
    start_gap = interval_wall_clearance(start, wall)
    end_gap = interval_wall_clearance(end, wall)
    if start_gap == 0 or end_gap == 0:
        raise ValueError(
            "primitive wall contact requires terminal overlap geometry, not coarse layer depth"
        )

    controlling = min(start_gap, end_gap)
    depth = collapse_layer_depth(controlling, collapse_factor)
    if depth is None:
        return None
    if depth >= len(profile.loading):
        raise ValueError("collapse-layer depth is not represented by material curve")

    if start_gap < end_gap:
        trigger = START
    elif end_gap < start_gap:
        trigger = END
    else:
        trigger = BOTH

    return CollapseLayerMaterialObservation1D(
        collapse_factor=collapse_factor,
        start_clearance=start_gap,
        end_clearance=end_gap,
        controlling_clearance=controlling,
        layer_depth=depth,
        trigger_sample=trigger,
        material_state=material_state(profile, depth, branch),
    )
