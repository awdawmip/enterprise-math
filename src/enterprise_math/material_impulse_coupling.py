"""Finite material-sample to signed impulse projection with explicit remainder.

The older E001 kinematic comparator maps a material response directly to a
returned motion budget.  This module introduces a more physical intermediate
quantity: integer impulse quanta applied to momentum.

For response sample ``r`` on material amplitude ``A`` and a declared maximum
impulse-per-tick scale ``J``, one raw signed impulse numerator is

    u = sign * J * r.

Projection to whole momentum quanta is signed toward zero:

    u + eta = A*q + eta',      |eta'| < A,

where ``eta`` is an optional carried subquantum detail.  Retaining ``eta'`` makes
repeated subquantum material forces accumulate exactly in the finite numerator
state.  Dropping it deliberately creates a coarser actuation law.  Neither mode
turns a measured stress into impulse automatically: ``J`` is an explicit
calibration/policy boundary with its own physical units outside this module.
"""

from __future__ import annotations

from dataclasses import dataclass


def _require_nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def signed_toward_zero_divmod(value: int, divisor: int) -> tuple[int, int]:
    """Return q,r with value=divisor*q+r and |r|<divisor, truncating q to zero."""
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError("value must be an integer")
    _require_positive("divisor", divisor)
    if value >= 0:
        quotient = value // divisor
    else:
        quotient = -((-value) // divisor)
    remainder = value - divisor * quotient
    if abs(remainder) >= divisor:
        raise AssertionError("signed toward-zero remainder escaped divisor bound")
    return quotient, remainder


@dataclass(frozen=True)
class MaterialImpulseProjection:
    response_sample: int
    response_amplitude: int
    max_impulse_per_tick: int
    outward_sign: int
    incoming_detail_numerator: int
    raw_signed_impulse_numerator: int
    total_signed_impulse_numerator: int
    impulse_quanta: int
    projection_detail_numerator: int
    next_detail_numerator: int
    retain_detail: bool


def project_material_impulse(
    response_sample: int,
    response_amplitude: int,
    max_impulse_per_tick: int,
    outward_sign: int,
    incoming_detail_numerator: int = 0,
    retain_detail: bool = True,
) -> MaterialImpulseProjection:
    """Project one finite material response onto signed whole momentum quanta."""
    _require_nonnegative("response_sample", response_sample)
    _require_positive("response_amplitude", response_amplitude)
    _require_nonnegative("max_impulse_per_tick", max_impulse_per_tick)
    if response_sample > response_amplitude:
        raise ValueError("response_sample must not exceed response_amplitude")
    if outward_sign not in (-1, 1):
        raise ValueError("outward_sign must be -1 or +1")
    if isinstance(incoming_detail_numerator, bool) or not isinstance(
        incoming_detail_numerator, int
    ):
        raise ValueError("incoming_detail_numerator must be an integer")
    if abs(incoming_detail_numerator) >= response_amplitude:
        raise ValueError("incoming impulse detail must lie strictly inside one amplitude cell")

    carried = incoming_detail_numerator if retain_detail else 0
    raw = outward_sign * max_impulse_per_tick * response_sample
    total = carried + raw
    whole, detail = signed_toward_zero_divmod(total, response_amplitude)
    next_detail = detail if retain_detail else 0
    if total != response_amplitude * whole + detail:
        raise AssertionError("impulse projection lost exact numerator accounting")
    return MaterialImpulseProjection(
        response_sample=response_sample,
        response_amplitude=response_amplitude,
        max_impulse_per_tick=max_impulse_per_tick,
        outward_sign=outward_sign,
        incoming_detail_numerator=carried,
        raw_signed_impulse_numerator=raw,
        total_signed_impulse_numerator=total,
        impulse_quanta=whole,
        projection_detail_numerator=detail,
        next_detail_numerator=next_detail,
        retain_detail=retain_detail,
    )


def repeated_constant_impulse(
    ticks: int,
    response_sample: int,
    response_amplitude: int,
    max_impulse_per_tick: int,
    outward_sign: int,
    retain_detail: bool = True,
) -> tuple[int, int]:
    """Return cumulative whole impulse and final detail for a constant response."""
    _require_nonnegative("ticks", ticks)
    detail = 0
    total_impulse = 0
    for _ in range(ticks):
        report = project_material_impulse(
            response_sample,
            response_amplitude,
            max_impulse_per_tick,
            outward_sign,
            detail,
            retain_detail,
        )
        total_impulse += report.impulse_quanta
        detail = report.next_detail_numerator
    return total_impulse, detail
