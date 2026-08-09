"""One-tick wall world combining collapse depth, material impulse and mass drift.

This E001 pressure-test composes already explicit finite layers:

    sampled wall clearance
      -> coarse interaction depth (only while approaching)
      -> loading-branch material response
      -> signed impulse quantization
      -> momentum update
      -> declared impulse/drift tick ordering
      -> sampled end state.

No rule says ``contact => rebound`` and no rule says ``REBOUND => reverse``.
Rebound is only a momentum-sign observation after the material impulse has been
applied.  A coarse interaction with zero/insufficient response can still
transmit, and a fine state that no longer belongs to the interaction layer can
legally make one long saved-state jump through the wall.

This module intentionally handles only positive-clearance start states.  A
primitive touch/overlap is returned as ``PRIMITIVE_CONTACT`` and delegated to
the terminal/contact comparator; no side normal is fabricated inside overlap.
Likewise, when the spatial layer requests a material depth not represented by
the profile, the result is explicitly ``MATERIAL_UNDERRESOLVED`` with no
invented after-state.

If a tick crosses the wall, the end-side normal is recomputed from the saved end
state.  The old-side normal is not reused to describe post-crossing approach or
separation.

The contact-local impulse remainder is merely carried through this one-tick
operator.  Its lifetime after separation (reset versus retained contact memory)
is a separate multi-tick world policy and is not silently chosen here.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_impulse_tick_order import (
    ImpulseDriftTickOutcome1D,
    ImpulseDriftTickState1D,
    TickOrder,
    material_impulse_drift_tick,
)
from .material_impulse_world_1d import momentum_contact_status
from .material_response import MaterialCurveProfile
from .scale_tunneling_1d import (
    BodyInterval1D,
    Wall1D,
    interval_wall_clearance,
    wall_jump_profile,
)

PRIMITIVE_CONTACT = "PRIMITIVE_CONTACT"
MATERIAL_UNDERRESOLVED = "MATERIAL_UNDERRESOLVED"
DRIFT = "DRIFT"
MATERIAL_INTERACTION = "MATERIAL_INTERACTION"
TRANSMIT = "TRANSMIT"

LEFT = "LEFT"
RIGHT = "RIGHT"


@dataclass(frozen=True)
class MaterialImpulseWallState1D:
    motion: ImpulseDriftTickState1D
    radius: int = 0

    def __post_init__(self) -> None:
        if isinstance(self.radius, bool) or not isinstance(self.radius, int) or self.radius < 0:
            raise ValueError("radius must be a non-negative integer")

    @property
    def center(self) -> int:
        return self.motion.motion.position


@dataclass(frozen=True)
class MaterialImpulseWallTick1D:
    kind: str
    wall: Wall1D
    collapse_factor: int
    start: MaterialImpulseWallState1D
    start_side: str | None
    outward_normal: int | None
    start_clearance: int
    macro_contact: bool
    approaching: bool
    layer_depth: int | None
    material_response_sample: int | None
    tick_order: TickOrder
    tick: ImpulseDriftTickOutcome1D | None
    after: MaterialImpulseWallState1D | None
    end_side: str | None
    end_outward_normal: int | None
    end_momentum_status: str | None
    end_clearance: int | None
    crossed_between_separated_sides: bool


def _positive_clearance_side(
    body: BodyInterval1D,
    wall: Wall1D,
) -> tuple[str, int] | None:
    if body.hi < wall.lo:
        return LEFT, -1
    if body.lo > wall.hi:
        return RIGHT, 1
    return None


def material_impulse_wall_tick(
    state: MaterialImpulseWallState1D,
    wall: Wall1D,
    collapse_factor: int,
    profile: MaterialCurveProfile,
    impulse_scale_magnitude: int,
    tick_order: TickOrder,
) -> MaterialImpulseWallTick1D:
    """Advance one sampled tick under the declared precision/material policy."""
    if (
        isinstance(collapse_factor, bool)
        or not isinstance(collapse_factor, int)
        or collapse_factor <= 0
    ):
        raise ValueError("collapse_factor must be a positive integer")
    if (
        isinstance(impulse_scale_magnitude, bool)
        or not isinstance(impulse_scale_magnitude, int)
        or impulse_scale_magnitude <= 0
    ):
        raise ValueError("impulse_scale_magnitude must be a positive integer")
    if not profile.loading or len(profile.loading) != len(profile.returning):
        raise ValueError("material profile must contain equal nonempty branches")

    start_body = BodyInterval1D(state.center, state.radius)
    gap = interval_wall_clearance(start_body, wall)
    side_normal = _positive_clearance_side(start_body, wall)
    if gap == 0 or side_normal is None:
        return MaterialImpulseWallTick1D(
            kind=PRIMITIVE_CONTACT,
            wall=wall,
            collapse_factor=collapse_factor,
            start=state,
            start_side=None,
            outward_normal=None,
            start_clearance=gap,
            macro_contact=True,
            approaching=False,
            layer_depth=None,
            material_response_sample=None,
            tick_order=tick_order,
            tick=None,
            after=None,
            end_side=None,
            end_outward_normal=None,
            end_momentum_status=None,
            end_clearance=None,
            crossed_between_separated_sides=False,
        )

    side, outward_normal = side_normal
    approaching = outward_normal * state.motion.motion.momentum < 0
    macro_contact = gap < collapse_factor
    depth: int | None = None
    sample: int | None = None
    response_for_tick = 0

    if macro_contact and approaching:
        depth = collapse_factor - gap
        if depth >= len(profile.loading):
            return MaterialImpulseWallTick1D(
                kind=MATERIAL_UNDERRESOLVED,
                wall=wall,
                collapse_factor=collapse_factor,
                start=state,
                start_side=side,
                outward_normal=outward_normal,
                start_clearance=gap,
                macro_contact=True,
                approaching=True,
                layer_depth=depth,
                material_response_sample=None,
                tick_order=tick_order,
                tick=None,
                after=None,
                end_side=None,
                end_outward_normal=None,
                end_momentum_status=None,
                end_clearance=None,
                crossed_between_separated_sides=False,
            )
        sample = profile.loading[depth]
        response_for_tick = sample

    tick = material_impulse_drift_tick(
        state.motion,
        outward_normal,
        response_for_tick,
        profile.amplitude,
        impulse_scale_magnitude,
        tick_order,
    )
    after = MaterialImpulseWallState1D(
        motion=tick.after,
        radius=state.radius,
    )
    end_body = BodyInterval1D(after.center, after.radius)
    end_gap = interval_wall_clearance(end_body, wall)
    end_side_normal = _positive_clearance_side(end_body, wall)
    if end_side_normal is None:
        end_side = None
        end_normal = None
        end_status = None
    else:
        end_side, end_normal = end_side_normal
        end_status = momentum_contact_status(
            after.motion.motion.momentum,
            end_normal,
        )
    jump = wall_jump_profile(wall, state.center, after.center, state.radius)

    if jump.crosses_between_separated_sides:
        kind = TRANSMIT
    elif sample is not None:
        kind = MATERIAL_INTERACTION
    else:
        kind = DRIFT

    return MaterialImpulseWallTick1D(
        kind=kind,
        wall=wall,
        collapse_factor=collapse_factor,
        start=state,
        start_side=side,
        outward_normal=outward_normal,
        start_clearance=gap,
        macro_contact=macro_contact,
        approaching=approaching,
        layer_depth=depth,
        material_response_sample=sample,
        tick_order=tick_order,
        tick=tick,
        after=after,
        end_side=end_side,
        end_outward_normal=end_normal,
        end_momentum_status=end_status,
        end_clearance=end_gap,
        crossed_between_separated_sides=jump.crosses_between_separated_sides,
    )
