"""Physically-scaled lifted 1D material impulse world.

This E001 experiment removes two accidental normalizations from the compact
impulse world:

* material response amplitude is not the physical force/time projection divisor;
* retained sub-whole momentum can participate immediately in the position drift.

The world still uses **whole position cells** for interaction geometry.  Position
subcell detail is retained for future drift but is not retroactively interpreted
as hidden continuous contact.  Refining the spatial geometry observable is a
separate declared dynamics/precision change.

Material response -> lifted momentum
-----------------------------------
A material branch sample ``r/A`` scales one declared full-scale force count
``Fmax``.  With force scale ``F_s``, time scale ``T_s``, momentum count scale
``P_s``, and tick duration count ``tau``, the exact signed momentum-count
increment is represented by the numerator

    dPi_num = sign * r * Fmax * tau * P_s

on fixed divisor

    Dp = A * F_s * T_s.

The state stores

    Pi = Dp*p_count + eta_p,      |eta_p|<Dp.

No whole-force quotient is required unless some declared future operation needs
whole force counts.

Lifted momentum -> lifted position
----------------------------------
For mass ``m_count/M_s`` and position count scale ``X_s``, the exact position
increment from lifted momentum Pi is represented by

    dx_num = Pi * M_s * tau * X_s

on divisor

    Dx = Dp * P_s * m_count * T_s.

A carried position numerator ``eta_x`` preserves subcell drift detail.  Whole
position cells are the geometry observable at this world precision.

Reversal is defined on the lifted momentum sign, not on the coarse whole-momentum
count.  Consequently the previous whole-count ZERO/stall band becomes only an
observation alias band when this lifted drift policy is used.

All unit tags are provenance; callers remain responsible for a compatible unit
system.  This is still an engineering pressure test, not a complete constitutive
or continuum mechanics model.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_hysteresis import LOADING, RETURNING, MaterialBranch
from .material_impulse_coupling import signed_toward_zero_divmod
from .material_physical_projection import ForceImpulseCountScale, MomentumDriftCountScale
from .material_response import MaterialCurveProfile
from .scale_tunneling_1d import BodyInterval1D, Wall1D, interval_wall_clearance

FREE_LIFTED_DRIFT = "FREE_LIFTED_DRIFT"
MATERIAL_FORCE_LIFT = "MATERIAL_FORCE_LIFT"
MATERIAL_ZERO_FORCE = "MATERIAL_ZERO_FORCE"
CROSSING_TRANSMIT = "CROSSING_TRANSMIT"
TERMINAL_CONTACT = "TERMINAL_CONTACT"
MATERIAL_UNDERRESOLVED = "MATERIAL_UNDERRESOLVED"


def _body_side(body: BodyInterval1D, wall: Wall1D) -> int:
    if body.hi < wall.lo:
        return -1
    if body.lo > wall.hi:
        return 1
    return 0


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


@dataclass(frozen=True)
class PhysicalLiftedMaterialScale1D:
    full_scale_force_count: int
    force_impulse: ForceImpulseCountScale
    momentum_drift: MomentumDriftCountScale

    def __post_init__(self) -> None:
        if (
            isinstance(self.full_scale_force_count, bool)
            or not isinstance(self.full_scale_force_count, int)
            or self.full_scale_force_count < 0
        ):
            raise ValueError("full_scale_force_count must be a non-negative integer")
        if self.force_impulse.momentum_scale_factor != self.momentum_drift.momentum_scale_factor:
            raise ValueError("force and drift layers must share one momentum count scale")
        if self.force_impulse.time_scale_factor != self.momentum_drift.time_scale_factor:
            raise ValueError("force and drift layers must share one time count scale")
        if self.force_impulse.tick_duration_count != self.momentum_drift.tick_duration_count:
            raise ValueError("force and drift layers must share one tick duration count")

    def momentum_lift_divisor(self, response_amplitude: int) -> int:
        if isinstance(response_amplitude, bool) or not isinstance(response_amplitude, int) or response_amplitude <= 0:
            raise ValueError("response_amplitude must be a positive integer")
        return response_amplitude * self.force_impulse.projection_divisor

    def position_lift_divisor(self, response_amplitude: int) -> int:
        dp = self.momentum_lift_divisor(response_amplitude)
        return dp * self.momentum_drift.projection_divisor


@dataclass(frozen=True)
class PhysicalLiftedMaterialState1D:
    center_count: int
    momentum_count: int
    branch: MaterialBranch = LOADING
    momentum_detail_numerator: int = 0
    position_detail_numerator: int = 0

    def __post_init__(self) -> None:
        for name, value in (
            ("center_count", self.center_count),
            ("momentum_count", self.momentum_count),
            ("momentum_detail_numerator", self.momentum_detail_numerator),
            ("position_detail_numerator", self.position_detail_numerator),
        ):
            _require_integer(name, value)
        if self.branch not in (LOADING, RETURNING):
            raise ValueError("branch must be LOADING or RETURNING")


@dataclass(frozen=True)
class PhysicalLiftedMaterialTransition1D:
    before: PhysicalLiftedMaterialState1D
    after: PhysicalLiftedMaterialState1D | None
    kind: str
    start_clearance: int
    end_clearance: int | None
    layer_depth: int | None
    response_sample: int | None
    momentum_lift_before: int
    momentum_lift_after_force: int | None
    raw_material_impulse_numerator: int | None
    whole_momentum_increment: int | None
    momentum_detail_after: int | None
    raw_position_numerator: int | None
    displacement_cells: int | None
    position_detail_after: int | None
    start_side: int
    end_side: int | None
    lifted_momentum_reversed: bool
    whole_momentum_reversed: bool


def _branch_from_lifted_motion(
    current_branch: MaterialBranch,
    lifted_momentum: int,
    outward_sign: int,
) -> MaterialBranch:
    if lifted_momentum == 0:
        return current_branch
    return RETURNING if lifted_momentum * outward_sign > 0 else LOADING


def _lifted_reversed(before: int, after: int, side: int) -> bool:
    return before * side < 0 and after * side > 0


def _whole_reversed(before: int, after: int, side: int) -> bool:
    return before * side < 0 and after * side > 0


def physical_lifted_material_step_1d(
    state: PhysicalLiftedMaterialState1D,
    wall: Wall1D,
    radius: int,
    collapse_factor: int,
    material_profile: MaterialCurveProfile,
    scale: PhysicalLiftedMaterialScale1D,
    retain_momentum_detail: bool = True,
    retain_position_detail: bool = True,
) -> PhysicalLiftedMaterialTransition1D:
    """Advance one causal saved-state tick through full response/momentum/position lifts."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    if isinstance(collapse_factor, bool) or not isinstance(collapse_factor, int) or collapse_factor <= 0:
        raise ValueError("collapse_factor must be a positive integer")
    if not material_profile.loading or len(material_profile.loading) != len(material_profile.returning):
        raise ValueError("material profile must contain equal nonempty branches")

    dp = scale.momentum_lift_divisor(material_profile.amplitude)
    dx_divisor = scale.position_lift_divisor(material_profile.amplitude)
    if abs(state.momentum_detail_numerator) >= dp:
        raise ValueError("momentum detail lies outside one lifted momentum cell")
    if abs(state.position_detail_numerator) >= dx_divisor:
        raise ValueError("position detail lies outside one lifted position cell")

    momentum_detail_before = state.momentum_detail_numerator if retain_momentum_detail else 0
    position_detail_before = state.position_detail_numerator if retain_position_detail else 0
    pi_before = dp * state.momentum_count + momentum_detail_before

    start_body = BodyInterval1D(state.center_count, radius)
    start_gap = interval_wall_clearance(start_body, wall)
    start_side = _body_side(start_body, wall)
    if start_gap == 0 or start_side == 0:
        return PhysicalLiftedMaterialTransition1D(
            before=state,
            after=None,
            kind=TERMINAL_CONTACT,
            start_clearance=0,
            end_clearance=None,
            layer_depth=None,
            response_sample=None,
            momentum_lift_before=pi_before,
            momentum_lift_after_force=None,
            raw_material_impulse_numerator=None,
            whole_momentum_increment=None,
            momentum_detail_after=None,
            raw_position_numerator=None,
            displacement_cells=None,
            position_detail_after=None,
            start_side=0,
            end_side=None,
            lifted_momentum_reversed=False,
            whole_momentum_reversed=False,
        )

    branch = _branch_from_lifted_motion(state.branch, pi_before, start_side)
    depth = None
    sample = None
    raw_impulse = 0
    kind = FREE_LIFTED_DRIFT

    if start_gap < collapse_factor:
        depth = collapse_factor - start_gap
        if depth >= len(material_profile.loading):
            return PhysicalLiftedMaterialTransition1D(
                before=state,
                after=None,
                kind=MATERIAL_UNDERRESOLVED,
                start_clearance=start_gap,
                end_clearance=None,
                layer_depth=depth,
                response_sample=None,
                momentum_lift_before=pi_before,
                momentum_lift_after_force=None,
                raw_material_impulse_numerator=None,
                whole_momentum_increment=None,
                momentum_detail_after=None,
                raw_position_numerator=None,
                displacement_cells=None,
                position_detail_after=None,
                start_side=start_side,
                end_side=None,
                lifted_momentum_reversed=False,
                whole_momentum_reversed=False,
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
            kind = MATERIAL_FORCE_LIFT

    pi_after = pi_before + raw_impulse
    whole_momentum_after, momentum_detail_after_raw = signed_toward_zero_divmod(pi_after, dp)
    momentum_detail_after = momentum_detail_after_raw if retain_momentum_detail else 0
    # If detail is deliberately dropped, the future drift consumes the resulting
    # coarse lifted state rather than the original hidden numerator.
    pi_for_drift = dp * whole_momentum_after + momentum_detail_after

    md = scale.momentum_drift
    raw_position = (
        pi_for_drift
        * md.mass_scale_factor
        * md.tick_duration_count
        * md.position_scale_factor
    )
    total_position = position_detail_before + raw_position
    displacement, position_detail_raw = signed_toward_zero_divmod(
        total_position,
        dx_divisor,
    )
    position_detail_after = position_detail_raw if retain_position_detail else 0
    end_center = state.center_count + displacement
    end_body = BodyInterval1D(end_center, radius)
    end_gap = interval_wall_clearance(end_body, wall)
    end_side = _body_side(end_body, wall)

    lifted_reversal = _lifted_reversed(pi_before, pi_after, start_side)
    whole_reversal = _whole_reversed(
        state.momentum_count,
        whole_momentum_after,
        start_side,
    )
    if end_gap == 0 or end_side == 0:
        return PhysicalLiftedMaterialTransition1D(
            before=state,
            after=None,
            kind=TERMINAL_CONTACT,
            start_clearance=start_gap,
            end_clearance=0,
            layer_depth=depth,
            response_sample=sample,
            momentum_lift_before=pi_before,
            momentum_lift_after_force=pi_after,
            raw_material_impulse_numerator=raw_impulse,
            whole_momentum_increment=whole_momentum_after - state.momentum_count,
            momentum_detail_after=momentum_detail_after,
            raw_position_numerator=raw_position,
            displacement_cells=displacement,
            position_detail_after=position_detail_after,
            start_side=start_side,
            end_side=0,
            lifted_momentum_reversed=lifted_reversal,
            whole_momentum_reversed=whole_reversal,
        )
    if end_side != start_side:
        kind = CROSSING_TRANSMIT

    next_branch = _branch_from_lifted_motion(branch, pi_after, end_side)
    after = PhysicalLiftedMaterialState1D(
        center_count=end_center,
        momentum_count=whole_momentum_after,
        branch=next_branch,
        momentum_detail_numerator=momentum_detail_after,
        position_detail_numerator=position_detail_after,
    )
    return PhysicalLiftedMaterialTransition1D(
        before=state,
        after=after,
        kind=kind,
        start_clearance=start_gap,
        end_clearance=end_gap,
        layer_depth=depth,
        response_sample=sample,
        momentum_lift_before=pi_before,
        momentum_lift_after_force=pi_after,
        raw_material_impulse_numerator=raw_impulse,
        whole_momentum_increment=whole_momentum_after - state.momentum_count,
        momentum_detail_after=momentum_detail_after,
        raw_position_numerator=raw_position,
        displacement_cells=displacement,
        position_detail_after=position_detail_after,
        start_side=start_side,
        end_side=end_side,
        lifted_momentum_reversed=lifted_reversal,
        whole_momentum_reversed=whole_reversal,
    )
