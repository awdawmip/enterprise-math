"""Causal constant-force midpoint variant of the physically-scaled material world.

The current saved deformation selects one material force sample.  That force is
declared constant for the whole saved tick.  Instead of the older
kick-then-post-drift update, this policy uses the exact finite constant-force
endpoint pairing

    Pi_1 = Pi_0 + J,
    2*Dx*Delta x = (Pi_0 + Pi_1) * drift_multiplier,

where ``Pi`` is the retained lifted momentum numerator and ``Dx`` is the physical
momentum-to-position divisor before the factor 2.  All arithmetic remains integer;
subcell position detail is retained explicitly.

This does not reconstruct a hidden continuous trajectory and does not inspect a
future material force.  It is a different one-tick law for the declared constant
current force.  At the lifted level it exactly satisfies

    Pi_1^2-Pi_0^2 = (Pi_1-Pi_0)(Pi_0+Pi_1),

and for a constant force/rate it is endpoint-invariant under explicit time
partition before spatial projection.  Midpoint/trapezoidal integration is prior
art; E001 uses it to separate material hysteresis from integrator scheduling.

Whole-cell geometry remains the collision/material-support observable.  Position
subcell detail is retained for future drift but is not a hidden contact path.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_hysteresis import LOADING, RETURNING, MaterialBranch
from .material_impulse_coupling import signed_toward_zero_divmod
from .material_physical_impulse_world_1d import PhysicalLiftedMaterialScale1D
from .material_response import MaterialCurveProfile
from .scale_tunneling_1d import BodyInterval1D, Wall1D, interval_wall_clearance

FREE_MIDPOINT_DRIFT = "FREE_MIDPOINT_DRIFT"
MATERIAL_MIDPOINT_FORCE = "MATERIAL_MIDPOINT_FORCE"
MATERIAL_ZERO_FORCE = "MATERIAL_ZERO_FORCE"
CROSSING_TRANSMIT = "CROSSING_TRANSMIT"
TERMINAL_CONTACT = "TERMINAL_CONTACT"
MATERIAL_UNDERRESOLVED = "MATERIAL_UNDERRESOLVED"


def _side(body: BodyInterval1D, wall: Wall1D) -> int:
    if body.hi < wall.lo:
        return -1
    if body.lo > wall.hi:
        return 1
    return 0


def _branch(current: MaterialBranch, lifted_momentum: int, outward_sign: int) -> MaterialBranch:
    if lifted_momentum == 0:
        return current
    return RETURNING if lifted_momentum * outward_sign > 0 else LOADING


@dataclass(frozen=True)
class PhysicalMidpointMaterialState1D:
    center_count: int
    momentum_count: int
    branch: MaterialBranch = LOADING
    momentum_detail_numerator: int = 0
    midpoint_position_detail_numerator: int = 0

    def __post_init__(self) -> None:
        for name, value in (
            ("center_count", self.center_count),
            ("momentum_count", self.momentum_count),
            ("momentum_detail_numerator", self.momentum_detail_numerator),
            ("midpoint_position_detail_numerator", self.midpoint_position_detail_numerator),
        ):
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError(f"{name} must be an integer")
        if self.branch not in (LOADING, RETURNING):
            raise ValueError("branch must be LOADING or RETURNING")


@dataclass(frozen=True)
class PhysicalMidpointMaterialTransition1D:
    before: PhysicalMidpointMaterialState1D
    after: PhysicalMidpointMaterialState1D | None
    kind: str
    start_clearance: int
    end_clearance: int | None
    layer_depth: int | None
    response_sample: int | None
    momentum_lift_before: int
    raw_impulse_numerator: int | None
    momentum_lift_after_raw: int | None
    momentum_lift_after_projection: int | None
    whole_momentum_after: int | None
    momentum_detail_after: int | None
    midpoint_position_numerator: int | None
    displacement_cells: int | None
    midpoint_position_detail_after: int | None
    lifted_square_change: int | None
    impulse_midpoint_work_numerator: int | None
    start_side: int
    end_side: int | None
    lifted_momentum_reversed: bool


def _halted(
    *,
    state: PhysicalMidpointMaterialState1D,
    kind: str,
    start_clearance: int,
    layer_depth: int | None,
    momentum_lift_before: int,
    start_side: int,
) -> PhysicalMidpointMaterialTransition1D:
    return PhysicalMidpointMaterialTransition1D(
        before=state,
        after=None,
        kind=kind,
        start_clearance=start_clearance,
        end_clearance=None,
        layer_depth=layer_depth,
        response_sample=None,
        momentum_lift_before=momentum_lift_before,
        raw_impulse_numerator=None,
        momentum_lift_after_raw=None,
        momentum_lift_after_projection=None,
        whole_momentum_after=None,
        momentum_detail_after=None,
        midpoint_position_numerator=None,
        displacement_cells=None,
        midpoint_position_detail_after=None,
        lifted_square_change=None,
        impulse_midpoint_work_numerator=None,
        start_side=start_side,
        end_side=None,
        lifted_momentum_reversed=False,
    )


def physical_midpoint_material_step_1d(
    state: PhysicalMidpointMaterialState1D,
    wall: Wall1D,
    radius: int,
    collapse_factor: int,
    material_profile: MaterialCurveProfile,
    scale: PhysicalLiftedMaterialScale1D,
    retain_momentum_detail: bool = True,
    retain_position_detail: bool = True,
) -> PhysicalMidpointMaterialTransition1D:
    """Advance one current-force, midpoint-drift saved tick."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    if isinstance(collapse_factor, bool) or not isinstance(collapse_factor, int) or collapse_factor <= 0:
        raise ValueError("collapse_factor must be a positive integer")
    if not material_profile.loading or len(material_profile.loading) != len(material_profile.returning):
        raise ValueError("material profile must contain equal nonempty branches")

    dp = scale.momentum_lift_divisor(material_profile.amplitude)
    base_dx = scale.position_lift_divisor(material_profile.amplitude)
    midpoint_dx = 2 * base_dx
    if abs(state.momentum_detail_numerator) >= dp:
        raise ValueError("momentum detail lies outside one lifted momentum cell")
    if abs(state.midpoint_position_detail_numerator) >= midpoint_dx:
        raise ValueError("midpoint position detail lies outside one projection cell")

    eta_p = state.momentum_detail_numerator if retain_momentum_detail else 0
    eta_x = state.midpoint_position_detail_numerator if retain_position_detail else 0
    pi0 = dp * state.momentum_count + eta_p

    body = BodyInterval1D(state.center_count, radius)
    gap = interval_wall_clearance(body, wall)
    start_side = _side(body, wall)
    if gap == 0 or start_side == 0:
        return _halted(
            state=state,
            kind=TERMINAL_CONTACT,
            start_clearance=0,
            layer_depth=None,
            momentum_lift_before=pi0,
            start_side=0,
        )

    branch = _branch(state.branch, pi0, start_side)
    depth = None
    sample = None
    raw_impulse = 0
    kind = FREE_MIDPOINT_DRIFT
    if gap < collapse_factor:
        depth = collapse_factor - gap
        if depth >= len(material_profile.loading):
            return _halted(
                state=state,
                kind=MATERIAL_UNDERRESOLVED,
                start_clearance=gap,
                layer_depth=depth,
                momentum_lift_before=pi0,
                start_side=start_side,
            )
        samples = material_profile.loading if branch == LOADING else material_profile.returning
        sample = samples[depth]
        if sample == 0:
            kind = MATERIAL_ZERO_FORCE
        else:
            fi = scale.force_impulse
            raw_impulse = (
                start_side
                * sample
                * scale.full_scale_force_count
                * fi.tick_duration_count
                * fi.momentum_scale_factor
            )
            kind = MATERIAL_MIDPOINT_FORCE

    pi1_raw = pi0 + raw_impulse
    whole1, eta1_raw = signed_toward_zero_divmod(pi1_raw, dp)
    eta1 = eta1_raw if retain_momentum_detail else 0
    pi1 = dp * whole1 + eta1

    md = scale.momentum_drift
    drift_multiplier = (
        md.mass_scale_factor
        * md.tick_duration_count
        * md.position_scale_factor
    )
    midpoint_numerator = (pi0 + pi1) * drift_multiplier
    total_position = eta_x + midpoint_numerator
    displacement, eta_x_raw = signed_toward_zero_divmod(total_position, midpoint_dx)
    eta_x1 = eta_x_raw if retain_position_detail else 0
    end_center = state.center_count + displacement
    end_body = BodyInterval1D(end_center, radius)
    end_gap = interval_wall_clearance(end_body, wall)
    end_side = _side(end_body, wall)

    square_change = pi1 * pi1 - pi0 * pi0
    midpoint_work = (pi1 - pi0) * (pi0 + pi1)
    if square_change != midpoint_work:
        raise AssertionError("midpoint lifted work failed exact square identity")
    reversal = pi0 * start_side < 0 and pi1 * start_side > 0

    if end_gap == 0 or end_side == 0:
        return PhysicalMidpointMaterialTransition1D(
            before=state,
            after=None,
            kind=TERMINAL_CONTACT,
            start_clearance=gap,
            end_clearance=0,
            layer_depth=depth,
            response_sample=sample,
            momentum_lift_before=pi0,
            raw_impulse_numerator=raw_impulse,
            momentum_lift_after_raw=pi1_raw,
            momentum_lift_after_projection=pi1,
            whole_momentum_after=whole1,
            momentum_detail_after=eta1,
            midpoint_position_numerator=midpoint_numerator,
            displacement_cells=displacement,
            midpoint_position_detail_after=eta_x1,
            lifted_square_change=square_change,
            impulse_midpoint_work_numerator=midpoint_work,
            start_side=start_side,
            end_side=0,
            lifted_momentum_reversed=reversal,
        )
    if end_side != start_side:
        kind = CROSSING_TRANSMIT
    next_branch = _branch(branch, pi1, end_side)
    after = PhysicalMidpointMaterialState1D(
        center_count=end_center,
        momentum_count=whole1,
        branch=next_branch,
        momentum_detail_numerator=eta1,
        midpoint_position_detail_numerator=eta_x1,
    )
    return PhysicalMidpointMaterialTransition1D(
        before=state,
        after=after,
        kind=kind,
        start_clearance=gap,
        end_clearance=end_gap,
        layer_depth=depth,
        response_sample=sample,
        momentum_lift_before=pi0,
        raw_impulse_numerator=raw_impulse,
        momentum_lift_after_raw=pi1_raw,
        momentum_lift_after_projection=pi1,
        whole_momentum_after=whole1,
        momentum_detail_after=eta1,
        midpoint_position_numerator=midpoint_numerator,
        displacement_cells=displacement,
        midpoint_position_detail_after=eta_x1,
        lifted_square_change=square_change,
        impulse_midpoint_work_numerator=midpoint_work,
        start_side=start_side,
        end_side=end_side,
        lifted_momentum_reversed=reversal,
    )
