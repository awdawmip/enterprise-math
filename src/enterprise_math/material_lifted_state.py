"""Exact scale-carrying integer rotation states for E001 material research.

A Pythagorean rotation lift does not need to lose information.  Retain an
explicit positive scale coordinate ``sigma`` and evolve

    (x,y;sigma) -> (a*x-b*y, b*x+a*y; c*sigma).

For an initial normalized amplitude A at scale 1, the exact invariant is

    x^2+y^2 = A^2 * sigma^2.

Only a later explicit projection to a coarser represented scale discards bounded
detail.  This separates exact integer rotation geometry from finite-resolution
material damping.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_oscillator import (
    PythagoreanRotation,
    integer_rotation_lift,
    signed_divmod_toward_zero,
)


@dataclass(frozen=True)
class LiftedRotationState2D:
    """Exact integer numerator coordinates with an explicit common scale."""

    x: int
    y: int
    scale: int
    step: int
    amplitude: int

    def __post_init__(self) -> None:
        for name, value in (("x", self.x), ("y", self.y)):
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError(f"{name} must be an integer")
        if isinstance(self.scale, bool) or not isinstance(self.scale, int) or self.scale <= 0:
            raise ValueError("scale must be a positive integer")
        if isinstance(self.step, bool) or not isinstance(self.step, int) or self.step < 0:
            raise ValueError("step must be a non-negative integer")
        if isinstance(self.amplitude, bool) or not isinstance(self.amplitude, int) or self.amplitude < 0:
            raise ValueError("amplitude must be a non-negative integer")
        if self.x * self.x + self.y * self.y != self.amplitude**2 * self.scale**2:
            raise ValueError("lifted state violates exact radius/scale invariant")


@dataclass(frozen=True)
class LiftedProjection2D:
    """Projection of one exact lifted state to a declared coarser scale."""

    source_scale: int
    target_scale: int
    ratio: int
    coordinates: tuple[int, int]
    details: tuple[int, int]


def initial_lifted_rotation_state(amplitude: int) -> LiftedRotationState2D:
    """Return the exact axis-aligned initial state ``(A,0;1)``."""
    if isinstance(amplitude, bool) or not isinstance(amplitude, int) or amplitude < 0:
        raise ValueError("amplitude must be a non-negative integer")
    return LiftedRotationState2D(amplitude, 0, 1, 0, amplitude)


def advance_lifted_rotation_state(
    state: LiftedRotationState2D,
    rotation: PythagoreanRotation,
) -> LiftedRotationState2D:
    """Apply one exact lift and multiply the explicit scale by ``c``."""
    raw_x, raw_y = integer_rotation_lift(state.x, state.y, rotation)
    next_scale = state.scale * rotation.c
    return LiftedRotationState2D(
        x=raw_x,
        y=raw_y,
        scale=next_scale,
        step=state.step + 1,
        amplitude=state.amplitude,
    )


def lifted_rotation_orbit(
    amplitude: int,
    rotation: PythagoreanRotation,
    steps: int,
) -> tuple[LiftedRotationState2D, ...]:
    """Return an exact no-loss scale-carrying rotation history."""
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 0:
        raise ValueError("steps must be a non-negative integer")
    state = initial_lifted_rotation_state(amplitude)
    states = [state]
    for _ in range(steps):
        state = advance_lifted_rotation_state(state, rotation)
        states.append(state)
    return tuple(states)


def project_lifted_state_toward_zero(
    state: LiftedRotationState2D,
    target_scale: int,
) -> LiftedProjection2D:
    """Project exact numerator coordinates to one divisor scale with signed details."""
    if isinstance(target_scale, bool) or not isinstance(target_scale, int) or target_scale <= 0:
        raise ValueError("target_scale must be a positive integer")
    if state.scale % target_scale != 0:
        raise ValueError("target_scale must divide the lifted state scale")
    ratio = state.scale // target_scale
    qx, dx = signed_divmod_toward_zero(state.x, ratio)
    qy, dy = signed_divmod_toward_zero(state.y, ratio)
    if state.x != ratio * qx + dx or state.y != ratio * qy + dy:
        raise AssertionError("lifted projection failed exact recomposition")
    return LiftedProjection2D(
        source_scale=state.scale,
        target_scale=target_scale,
        ratio=ratio,
        coordinates=(qx, qy),
        details=(dx, dy),
    )
