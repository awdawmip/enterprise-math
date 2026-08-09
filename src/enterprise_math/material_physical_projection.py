"""Exact count-scale calibration for force->momentum and momentum->position.

The normalized E001 impulse world uses compact engineering parameters such as a
maximum impulse-per-tick and an integer mass divisor.  Those are useful for
finite-precision mathematics but must not be mistaken for a physical unit
calibration.  This module separates the count scales explicitly.

Force/impulse projection
------------------------
If

    F = f / F_s,
    dt = tau / T_s,
    p = p_count / P_s,

in a caller-declared compatible force, time, and momentum unit system, then the
exact momentum-count increment is

    Delta p_count = f * tau * P_s / (F_s*T_s).

The fixed projection divisor is ``D_p=F_s*T_s``.  Retaining its signed remainder
makes repeated force samples exact in the lifted numerator coordinate.

Momentum/drift projection
-------------------------
If additionally

    m = m_count / M_s,
    x = x_count / X_s,

then one constant-momentum tick gives the exact position-count increment

    Delta x_count
      = p_count * M_s * tau * X_s
        / (P_s * m_count * T_s).

For a fixed body mass and tick duration this again has a fixed integer divisor,
so a spatial subcell remainder may be retained or deliberately dropped.

Unit strings below are opaque provenance tags; this module does not implement a
dimensional-algebra engine.  A caller is responsible for choosing mutually
compatible physical units before interpreting the counts physically.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_impulse_coupling import signed_toward_zero_divmod


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_unit(name: str, value: str) -> None:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{name} must be a nonempty string")


@dataclass(frozen=True)
class ForceImpulseCountScale:
    force_scale_factor: int
    time_scale_factor: int
    momentum_scale_factor: int
    tick_duration_count: int
    force_unit: str
    time_unit: str
    momentum_unit: str

    def __post_init__(self) -> None:
        _require_positive("force_scale_factor", self.force_scale_factor)
        _require_positive("time_scale_factor", self.time_scale_factor)
        _require_positive("momentum_scale_factor", self.momentum_scale_factor)
        _require_nonnegative("tick_duration_count", self.tick_duration_count)
        _require_unit("force_unit", self.force_unit)
        _require_unit("time_unit", self.time_unit)
        _require_unit("momentum_unit", self.momentum_unit)

    @property
    def projection_divisor(self) -> int:
        return self.force_scale_factor * self.time_scale_factor


@dataclass(frozen=True)
class ForceImpulseCountProjection:
    force_count: int
    direction_sign: int
    raw_momentum_count_numerator: int
    incoming_detail_numerator: int
    total_momentum_count_numerator: int
    momentum_count_increment: int
    projection_detail_numerator: int
    next_detail_numerator: int
    retain_detail: bool


def project_force_count_to_momentum(
    force_count: int,
    direction_sign: int,
    scale: ForceImpulseCountScale,
    incoming_detail_numerator: int = 0,
    retain_detail: bool = True,
) -> ForceImpulseCountProjection:
    """Project one force count over one declared tick into momentum counts."""
    _require_nonnegative("force_count", force_count)
    if direction_sign not in (-1, 1):
        raise ValueError("direction_sign must be -1 or +1")
    if isinstance(incoming_detail_numerator, bool) or not isinstance(
        incoming_detail_numerator, int
    ):
        raise ValueError("incoming_detail_numerator must be an integer")
    divisor = scale.projection_divisor
    if abs(incoming_detail_numerator) >= divisor:
        raise ValueError("incoming impulse detail must lie inside one projection cell")
    carried = incoming_detail_numerator if retain_detail else 0
    raw = (
        direction_sign
        * force_count
        * scale.tick_duration_count
        * scale.momentum_scale_factor
    )
    total = carried + raw
    whole, detail = signed_toward_zero_divmod(total, divisor)
    if total != divisor * whole + detail:
        raise AssertionError("force-to-momentum projection lost exact numerator accounting")
    return ForceImpulseCountProjection(
        force_count=force_count,
        direction_sign=direction_sign,
        raw_momentum_count_numerator=raw,
        incoming_detail_numerator=carried,
        total_momentum_count_numerator=total,
        momentum_count_increment=whole,
        projection_detail_numerator=detail,
        next_detail_numerator=detail if retain_detail else 0,
        retain_detail=retain_detail,
    )


@dataclass(frozen=True)
class MomentumDriftCountScale:
    momentum_scale_factor: int
    mass_scale_factor: int
    time_scale_factor: int
    position_scale_factor: int
    tick_duration_count: int
    mass_count: int
    momentum_unit: str
    mass_unit: str
    time_unit: str
    position_unit: str

    def __post_init__(self) -> None:
        for name, value in (
            ("momentum_scale_factor", self.momentum_scale_factor),
            ("mass_scale_factor", self.mass_scale_factor),
            ("time_scale_factor", self.time_scale_factor),
            ("position_scale_factor", self.position_scale_factor),
            ("mass_count", self.mass_count),
        ):
            _require_positive(name, value)
        _require_nonnegative("tick_duration_count", self.tick_duration_count)
        _require_unit("momentum_unit", self.momentum_unit)
        _require_unit("mass_unit", self.mass_unit)
        _require_unit("time_unit", self.time_unit)
        _require_unit("position_unit", self.position_unit)

    @property
    def projection_divisor(self) -> int:
        return (
            self.momentum_scale_factor
            * self.mass_count
            * self.time_scale_factor
        )


@dataclass(frozen=True)
class MomentumDriftCountProjection:
    momentum_count: int
    raw_position_count_numerator: int
    incoming_detail_numerator: int
    total_position_count_numerator: int
    displacement_cells: int
    projection_detail_numerator: int
    next_detail_numerator: int
    retain_detail: bool


def project_momentum_count_to_position(
    momentum_count: int,
    scale: MomentumDriftCountScale,
    incoming_detail_numerator: int = 0,
    retain_detail: bool = True,
) -> MomentumDriftCountProjection:
    """Project one momentum count over one tick into signed position cells."""
    if isinstance(momentum_count, bool) or not isinstance(momentum_count, int):
        raise ValueError("momentum_count must be an integer")
    if isinstance(incoming_detail_numerator, bool) or not isinstance(
        incoming_detail_numerator, int
    ):
        raise ValueError("incoming_detail_numerator must be an integer")
    divisor = scale.projection_divisor
    if abs(incoming_detail_numerator) >= divisor:
        raise ValueError("incoming drift detail must lie inside one projection cell")
    carried = incoming_detail_numerator if retain_detail else 0
    raw = (
        momentum_count
        * scale.mass_scale_factor
        * scale.tick_duration_count
        * scale.position_scale_factor
    )
    total = carried + raw
    whole, detail = signed_toward_zero_divmod(total, divisor)
    if total != divisor * whole + detail:
        raise AssertionError("momentum-to-position projection lost exact numerator accounting")
    return MomentumDriftCountProjection(
        momentum_count=momentum_count,
        raw_position_count_numerator=raw,
        incoming_detail_numerator=carried,
        total_position_count_numerator=total,
        displacement_cells=whole,
        projection_detail_numerator=detail,
        next_detail_numerator=detail if retain_detail else 0,
        retain_detail=retain_detail,
    )
