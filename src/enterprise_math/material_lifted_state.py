"""Exact scale-carrying integer rotation states for E001 material research.

A Pythagorean rotation lift does not need to lose information.  Retain an
explicit positive scale coordinate ``sigma`` and evolve

    (x,y;sigma) -> (a*x-b*y, b*x+a*y; c*sigma).

For an arbitrary integer initial state with squared norm ``N0``, the exact
invariant is

    x^2+y^2 = N0 * sigma^2.

No integer-radius assumption is needed.  An axis-aligned amplitude state
``(A,0;1)`` is just a convenient material-quarter-wave specialization.

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
    base_norm_sq: int

    def __post_init__(self) -> None:
        for name, value in (("x", self.x), ("y", self.y)):
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError(f"{name} must be an integer")
        if isinstance(self.scale, bool) or not isinstance(self.scale, int) or self.scale <= 0:
            raise ValueError("scale must be a positive integer")
        if isinstance(self.step, bool) or not isinstance(self.step, int) or self.step < 0:
            raise ValueError("step must be a non-negative integer")
        if (
            isinstance(self.base_norm_sq, bool)
            or not isinstance(self.base_norm_sq, int)
            or self.base_norm_sq < 0
        ):
            raise ValueError("base_norm_sq must be a non-negative integer")
        if self.x * self.x + self.y * self.y != self.base_norm_sq * self.scale**2:
            raise ValueError("lifted state violates exact norm/scale invariant")


@dataclass(frozen=True)
class LiftedProjection2D:
    """Projection of one exact lifted state to a declared coarser scale."""

    source_scale: int
    target_scale: int
    ratio: int
    coordinates: tuple[int, int]
    details: tuple[int, int]


def initial_lifted_rotation_state(x: int, y: int) -> LiftedRotationState2D:
    """Return one exact arbitrary integer initial state at scale 1."""
    for name, value in (("x", x), ("y", y)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    return LiftedRotationState2D(
        x=x,
        y=y,
        scale=1,
        step=0,
        base_norm_sq=x * x + y * y,
    )


def initial_axis_lifted_rotation_state(amplitude: int) -> LiftedRotationState2D:
    """Return the material-specialized axis state ``(A,0;1)``."""
    if isinstance(amplitude, bool) or not isinstance(amplitude, int) or amplitude < 0:
        raise ValueError("amplitude must be a non-negative integer")
    return initial_lifted_rotation_state(amplitude, 0)


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
        base_norm_sq=state.base_norm_sq,
    )


def lifted_rotation_orbit(
    initial_state: tuple[int, int],
    rotation: PythagoreanRotation,
    steps: int,
) -> tuple[LiftedRotationState2D, ...]:
    """Return an exact no-loss scale-carrying rotation history."""
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 0:
        raise ValueError("steps must be a non-negative integer")
    state = initial_lifted_rotation_state(*initial_state)
    states = [state]
    for _ in range(steps):
        state = advance_lifted_rotation_state(state, rotation)
        states.append(state)
    return tuple(states)


def axis_lifted_rotation_orbit(
    amplitude: int,
    rotation: PythagoreanRotation,
    steps: int,
) -> tuple[LiftedRotationState2D, ...]:
    """Convenience wrapper for the axis-aligned material start ``(A,0)``."""
    if isinstance(amplitude, bool) or not isinstance(amplitude, int) or amplitude < 0:
        raise ValueError("amplitude must be a non-negative integer")
    return lifted_rotation_orbit((amplitude, 0), rotation, steps)


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
