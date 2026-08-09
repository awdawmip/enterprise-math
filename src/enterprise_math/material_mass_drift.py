"""Exact integer mass drift with explicit saved-position remainder.

The first E001 impulse world advances position by ``trunc(p/m)`` cells each tick
and discards the mass-division remainder.  That is a legitimate coarse schedule,
but it is not forced by the finite state algebra.

This module isolates the second precision reservoir:

    rho_x + p = m*q + rho_x',      |rho_x'| < m.

``q`` is the saved integer-cell drift.  Retaining ``rho_x'`` lets sub-cell
position phase accumulate across ticks; dropping it deliberately projects back
to a coarser world after every drift.

For constant nonzero momentum with ``0<|p|<m`` and initial detail zero:

* retain-detail first moves one saved cell exactly at
  ``ceil(m/|p|)`` ticks;
* drop-detail never moves at all while that momentum stays fixed.

Thus a world can preserve subquantum material impulse while still freezing
sub-cell mass drift if it keeps the impulse remainder but discards this distinct
position remainder.  The two precision reservoirs must not be conflated.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_impulse_coupling import signed_toward_zero_divmod


@dataclass(frozen=True)
class MassDriftProjection1D:
    momentum_quanta: int
    mass_quanta: int
    incoming_position_detail: int
    total_drift_numerator: int
    drift_cells: int
    projection_detail: int
    next_position_detail: int
    retain_detail: bool


def project_mass_drift(
    momentum_quanta: int,
    mass_quanta: int,
    incoming_position_detail: int = 0,
    retain_detail: bool = True,
) -> MassDriftProjection1D:
    """Project one momentum tick into integer-cell motion with optional detail carry."""
    for name, value in (
        ("momentum_quanta", momentum_quanta),
        ("incoming_position_detail", incoming_position_detail),
    ):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    if isinstance(mass_quanta, bool) or not isinstance(mass_quanta, int) or mass_quanta <= 0:
        raise ValueError("mass_quanta must be a positive integer")
    if abs(incoming_position_detail) >= mass_quanta:
        raise ValueError("position detail must lie strictly inside one mass cell")

    carried = incoming_position_detail if retain_detail else 0
    total = carried + momentum_quanta
    drift, detail = signed_toward_zero_divmod(total, mass_quanta)
    next_detail = detail if retain_detail else 0
    if total != mass_quanta * drift + detail:
        raise AssertionError("mass drift projection lost exact numerator accounting")
    return MassDriftProjection1D(
        momentum_quanta=momentum_quanta,
        mass_quanta=mass_quanta,
        incoming_position_detail=carried,
        total_drift_numerator=total,
        drift_cells=drift,
        projection_detail=detail,
        next_position_detail=next_detail,
        retain_detail=retain_detail,
    )


def repeated_constant_mass_drift(
    ticks: int,
    momentum_quanta: int,
    mass_quanta: int,
    retain_detail: bool = True,
) -> tuple[int, int]:
    """Return total integer displacement and final position detail."""
    if isinstance(ticks, bool) or not isinstance(ticks, int) or ticks < 0:
        raise ValueError("ticks must be a non-negative integer")
    displacement = 0
    detail = 0
    for _ in range(ticks):
        report = project_mass_drift(
            momentum_quanta,
            mass_quanta,
            detail,
            retain_detail,
        )
        displacement += report.drift_cells
        detail = report.next_position_detail
    return displacement, detail


def first_retained_drift_tick(momentum_quanta: int, mass_quanta: int) -> int | None:
    """For |p|<m, return ceil(m/|p|); None for zero momentum."""
    if isinstance(momentum_quanta, bool) or not isinstance(momentum_quanta, int):
        raise ValueError("momentum_quanta must be an integer")
    if isinstance(mass_quanta, bool) or not isinstance(mass_quanta, int) or mass_quanta <= 0:
        raise ValueError("mass_quanta must be a positive integer")
    magnitude = abs(momentum_quanta)
    if magnitude == 0:
        return None
    if magnitude >= mass_quanta:
        return 1
    return (mass_quanta + magnitude - 1) // magnitude
