"""One-dimensional finite impulse material world where rebound is emergent.

This is an E001 engineering pressure test of a stronger material-world idea.  It
does **not** prescribe a returned velocity.  Instead, a saved material state
produces a finite force sample which, when nonzero, projects to signed impulse,
updates momentum, and then drifts position through an integer mass quotient.

For a body on one separated side of a wall:

1. positive gap ``g<d`` gives coarse material depth ``k=d-g``;
2. inward motion selects LOADING, outward motion selects RETURNING, while zero
   momentum preserves the stored branch;
3. a zero branch sample is explicit ``MATERIAL_ZERO_FORCE``: the material state
   is sampled but no impulse event is created and momentum/detail are unchanged;
4. a positive branch sample is projected to an outward signed impulse by
   ``material_impulse_coupling`` and is ``MATERIAL_KICK``;
5. momentum changes only under a nonzero kick;
6. one saved drift is ``trunc(momentum / mass_quanta)`` cells.

If accumulated material impulse changes the represented momentum from an
inward/stalled state into a nonzero outward state, rebound has emerged without a
``REBOUND -> reverse velocity`` rule.  The finite zero-momentum stall band is a
legal intermediate state and does not erase a later outward onset.

If a saved drift jumps from one separated side of the wall to the other, that
transmission is legal here; no hidden continuous path is reconstructed.  A saved
endpoint touching/overlapping the primitive wall is returned as explicit
TERMINAL_CONTACT for the terminal geometry layer.

Crucially, the current material force is selected only from the **current saved
state**.  A future post-drift endpoint cannot retroactively trigger force in the
current tick.

The declared maximum impulse-per-tick is still a calibration/policy boundary.
This module is therefore a finite world-engine experiment, not yet a complete
physical constitutive model.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_hysteresis import LOADING, RETURNING, MaterialBranch
from .material_impulse_coupling import (
    MaterialImpulseProjection,
    project_material_impulse,
    signed_toward_zero_divmod,
)
from .material_response import MaterialCurveProfile
from .scale_tunneling_1d import BodyInterval1D, Wall1D, interval_wall_clearance

FREE_DRIFT = "FREE_DRIFT"
MATERIAL_ZERO_FORCE = "MATERIAL_ZERO_FORCE"
MATERIAL_KICK = "MATERIAL_KICK"
CROSSING_TRANSMIT = "CROSSING_TRANSMIT"
TERMINAL_CONTACT = "TERMINAL_CONTACT"
MATERIAL_UNDERRESOLVED = "MATERIAL_UNDERRESOLVED"


@dataclass(frozen=True)
class MomentumMaterialState1D:
    center: int
    momentum_quanta: int
    branch: MaterialBranch = LOADING
    impulse_detail_numerator: int = 0

    def __post_init__(self) -> None:
        for name, value in (
            ("center", self.center),
            ("momentum_quanta", self.momentum_quanta),
            ("impulse_detail_numerator", self.impulse_detail_numerator),
        ):
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError(f"{name} must be an integer")
        if self.branch not in (LOADING, RETURNING):
            raise ValueError("branch must be LOADING or RETURNING")


@dataclass(frozen=True)
class ImpulseMaterialTransition1D:
    before: MomentumMaterialState1D
    after: MomentumMaterialState1D | None
    kind: str
    start_clearance: int
    end_clearance: int | None
    layer_depth: int | None
    response_sample: int | None
    impulse: MaterialImpulseProjection | None
    drift_cells: int | None
    start_side: int
    end_side: int | None
    momentum_reversed: bool


def _body_side(body: BodyInterval1D, wall: Wall1D) -> int:
    if body.hi < wall.lo:
        return -1
    if body.lo > wall.hi:
        return 1
    return 0


def _branch_from_motion(
    current_branch: MaterialBranch,
    momentum: int,
    outward_sign: int,
) -> MaterialBranch:
    if momentum == 0:
        return current_branch
    return RETURNING if momentum * outward_sign > 0 else LOADING


def _motion_reversed(before: int, after: int, start_side: int) -> bool:
    """Whether this tick first enters nonzero outward whole momentum.

    ``before`` may already be the finite zero-momentum stall state.  That stall
    must not hide a later material-driven outward onset, so the previous state is
    required only to be *not outward*, rather than strictly inward.
    """
    return before * start_side <= 0 and after * start_side > 0


def impulse_material_step_1d(
    state: MomentumMaterialState1D,
    wall: Wall1D,
    radius: int,
    collapse_factor: int,
    material_profile: MaterialCurveProfile,
    mass_quanta: int,
    max_impulse_per_tick: int,
    retain_impulse_detail: bool = True,
) -> ImpulseMaterialTransition1D:
    """Advance one saved tick using causal force/kick-then-drift finite dynamics."""
    for name, value in (
        ("radius", radius),
        ("collapse_factor", collapse_factor),
        ("mass_quanta", mass_quanta),
        ("max_impulse_per_tick", max_impulse_per_tick),
    ):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    if radius < 0:
        raise ValueError("radius must be non-negative")
    if collapse_factor <= 0:
        raise ValueError("collapse_factor must be positive")
    if mass_quanta <= 0:
        raise ValueError("mass_quanta must be positive")
    if max_impulse_per_tick < 0:
        raise ValueError("max_impulse_per_tick must be non-negative")
    if abs(state.impulse_detail_numerator) >= material_profile.amplitude:
        raise ValueError("state impulse detail lies outside the material amplitude cell")

    start_body = BodyInterval1D(state.center, radius)
    start_gap = interval_wall_clearance(start_body, wall)
    start_side = _body_side(start_body, wall)
    if start_gap == 0 or start_side == 0:
        return ImpulseMaterialTransition1D(
            before=state,
            after=None,
            kind=TERMINAL_CONTACT,
            start_clearance=0,
            end_clearance=None,
            layer_depth=None,
            response_sample=None,
            impulse=None,
            drift_cells=None,
            start_side=0,
            end_side=None,
            momentum_reversed=False,
        )

    depth = None
    sample = None
    impulse = None
    momentum_after_kick = state.momentum_quanta
    detail_after = state.impulse_detail_numerator
    branch = _branch_from_motion(state.branch, state.momentum_quanta, start_side)
    kind = FREE_DRIFT

    # Causal rule: only the current saved clearance decides current material force.
    if start_gap < collapse_factor:
        depth = collapse_factor - start_gap
        if depth >= len(material_profile.loading) or depth >= len(material_profile.returning):
            return ImpulseMaterialTransition1D(
                before=state,
                after=None,
                kind=MATERIAL_UNDERRESOLVED,
                start_clearance=start_gap,
                end_clearance=None,
                layer_depth=depth,
                response_sample=None,
                impulse=None,
                drift_cells=None,
                start_side=start_side,
                end_side=None,
                momentum_reversed=False,
            )
        samples = material_profile.loading if branch == LOADING else material_profile.returning
        sample = samples[depth]
        if sample == 0:
            # A represented material state with zero force is not a kick.  Keep
            # the state evidence (depth/sample) while leaving momentum and the
            # impulse-detail coordinate exactly unchanged.
            kind = MATERIAL_ZERO_FORCE
        else:
            impulse = project_material_impulse(
                sample,
                material_profile.amplitude,
                max_impulse_per_tick,
                start_side,
                state.impulse_detail_numerator,
                retain_impulse_detail,
            )
            momentum_after_kick += impulse.impulse_quanta
            detail_after = impulse.next_detail_numerator
            kind = MATERIAL_KICK

    drift, _mass_detail = signed_toward_zero_divmod(momentum_after_kick, mass_quanta)
    end_center = state.center + drift
    end_body = BodyInterval1D(end_center, radius)
    end_gap = interval_wall_clearance(end_body, wall)
    end_side = _body_side(end_body, wall)
    reversed_now = _motion_reversed(
        state.momentum_quanta,
        momentum_after_kick,
        start_side,
    )

    if end_gap == 0 or end_side == 0:
        return ImpulseMaterialTransition1D(
            before=state,
            after=None,
            kind=TERMINAL_CONTACT,
            start_clearance=start_gap,
            end_clearance=0,
            layer_depth=depth,
            response_sample=sample,
            impulse=impulse,
            drift_cells=drift,
            start_side=start_side,
            end_side=0,
            momentum_reversed=reversed_now,
        )

    if end_side != start_side:
        kind = CROSSING_TRANSMIT

    next_branch = _branch_from_motion(branch, momentum_after_kick, end_side)
    after = MomentumMaterialState1D(
        center=end_center,
        momentum_quanta=momentum_after_kick,
        branch=next_branch,
        impulse_detail_numerator=detail_after,
    )
    return ImpulseMaterialTransition1D(
        before=state,
        after=after,
        kind=kind,
        start_center if False else state.center,
        end_center if False else end_gap,
        depth,
        sample,
        impulse,
        drift,
        start_side,
        end_side,
        reversed_now,
    )


@dataclass(frozen=True)
class ImpulseMaterialHistory1D:
    initial: MomentumMaterialState1D
    transitions: tuple[ImpulseMaterialTransition1D, ...]
    final: MomentumMaterialState1D | None
    halted_kind: str | None
    first_reversal_tick: int | None


def run_impulse_material_world_1d(
    initial: MomentumMaterialState1D,
    wall: Wall1D,
    radius: int,
    collapse_factor: int,
    material_profile: MaterialCurveProfile,
    mass_quanta: int,
    max_impulse_per_tick: int,
    ticks: int,
    retain_impulse_detail: bool = True,
) -> ImpulseMaterialHistory1D:
    """Run a finite number of causal material force/kick/drift ticks."""
    if isinstance(ticks, bool) or not isinstance(ticks, int) or ticks < 0:
        raise ValueError("ticks must be a non-negative integer")
    current: MomentumMaterialState1D | None = initial
    transitions: list[ImpulseMaterialTransition1D] = []
    halted_kind = None
    first_reversal = None
    for tick in range(ticks):
        if current is None:
            break
        transition = impulse_material_step_1d(
            current,
            wall,
            radius,
            collapse_factor,
            material_profile,
            mass_quanta,
            max_impulse_per_tick,
            retain_impulse_detail,
        )
        transitions.append(transition)
        if transition.momentum_reversed and first_reversal is None:
            first_reversal = tick
        current = transition.after
        if current is None:
            halted_kind = transition.kind
            break
    return ImpulseMaterialHistory1D(
        initial=initial,
        transitions=tuple(transitions),
        final=current,
        halted_kind=halted_kind,
        first_reversal_tick=first_reversal,
    )
