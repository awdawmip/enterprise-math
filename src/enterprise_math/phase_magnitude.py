"""Phase/magnitude separation for Enterprise Math P019.

Finite-precision magnitude collapse must not erase an exact integer sign/phase
channel.  This module makes that separation explicit for the Schwarzschild and
charged radial pressure tests.
"""

from __future__ import annotations

from .black_hole import horizon_observation
from .charged_black_hole import charged_horizon_observation, charged_residual


def integer_phase(value: int) -> int:
    """Return -1, 0, or +1 without quantizing away sign."""
    if not isinstance(value, int):
        raise TypeError("phase source must be an integer")
    return (value > 0) - (value < 0)


def phase_magnitude_pair(value: int, magnitude: int) -> tuple[int, int]:
    """Keep exact phase and a nonnegative finite-precision magnitude together."""
    if not isinstance(magnitude, int):
        raise TypeError("magnitude must be an integer")
    if magnitude < 0:
        raise ValueError("magnitude must be nonnegative")
    return integer_phase(value), magnitude


def schwarzschild_phase_magnitude(
    precision: int, radius: int, horizon: int
) -> tuple[int, int]:
    """Return (sign(n-h), q_lambda(n;h))."""
    if not isinstance(radius, int) or not isinstance(horizon, int):
        raise TypeError("radius and horizon must be integers")
    if radius <= 0 or horizon <= 0:
        raise ValueError("radius and horizon must be positive")
    magnitude = horizon_observation(precision, radius, horizon)
    return integer_phase(radius - horizon), magnitude


def charged_phase_magnitude(
    precision: int, radius: int, mass_coefficient: int, charge_square: int
) -> tuple[int, int]:
    """Return (sign(P(n)), g_lambda(n;a,b))."""
    residual = charged_residual(radius, mass_coefficient, charge_square)
    magnitude = charged_horizon_observation(
        precision, radius, mass_coefficient, charge_square
    )
    return integer_phase(residual), magnitude


def is_zero_phase_boundary(observation: tuple[int, int]) -> bool:
    """Return whether an observation lies on an exact zero-phase primal boundary."""
    phase, magnitude = observation
    return phase == 0 and magnitude == 0
