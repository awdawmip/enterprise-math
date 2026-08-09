"""Finite precision threshold for projected rotation sign itineraries.

Let ``M=[[a,-b],[b,a]]`` with ``a^2+b^2=c^2``.  For an axis initial state
``(A,0)``, let ``U_k=M^k(1,0)`` be the exact unit-amplitude lifted numerator and
let ``z_k`` be the sequential toward-zero projected state at fixed scale 1.
Define the integer discrepancy

    E_k = c^k z_k - A U_k.

If the step-k projection details are delta_(k+1), then exactly

    E_(k+1) = M E_k - c^k delta_(k+1).

Because each detail coordinate has absolute value < c, a conservative L1 bound
``B_k`` obeys

    B_0=0,
    B_(k+1)=(a+b)B_k + 2(c-1)c^k.

Thus ``A*|u_k|>B_k`` certifies that projected and exact lifted x coordinates
have the same sign at step k.  Analogous statements hold for y.  This gives a
finite amplitude threshold for any finite sign itinerary, without a limit or
hidden real angle.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_oscillator import (
    TOWARD_ZERO,
    PythagoreanRotation,
    integer_rotation_lift,
    projected_rotation_step,
)


@dataclass(frozen=True)
class PhaseSignStabilityStep:
    """Exact lifted coordinate and conservative projected-discrepancy bound."""

    step: int
    unit_exact: tuple[int, int]
    scale: int
    l1_discrepancy_bound: int
    minimum_amplitude_for_x_sign: int | None
    minimum_amplitude_for_y_sign: int | None


def _minimum_amplitude_for_sign(coordinate: int, bound: int) -> int | None:
    if coordinate == 0:
        return None
    return bound // abs(coordinate) + 1


def phase_sign_stability_profile(
    rotation: PythagoreanRotation,
    horizon: int,
) -> tuple[PhaseSignStabilityStep, ...]:
    """Return exact unit lift and conservative sign-stability thresholds to horizon."""
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 0:
        raise ValueError("horizon must be a non-negative integer")

    ux, uy = 1, 0
    scale = 1
    bound = 0
    result: list[PhaseSignStabilityStep] = []
    for step in range(horizon + 1):
        result.append(
            PhaseSignStabilityStep(
                step=step,
                unit_exact=(ux, uy),
                scale=scale,
                l1_discrepancy_bound=bound,
                minimum_amplitude_for_x_sign=_minimum_amplitude_for_sign(ux, bound),
                minimum_amplitude_for_y_sign=_minimum_amplitude_for_sign(uy, bound),
            )
        )
        ux, uy = integer_rotation_lift(ux, uy, rotation)
        bound = (
            (rotation.a + rotation.b) * bound
            + 2 * (rotation.c - 1) * scale
        )
        scale *= rotation.c
    return tuple(result)


def x_sign_itinerary_amplitude_bound(
    rotation: PythagoreanRotation,
    horizon: int,
) -> int:
    """Sufficient amplitude for every nonzero exact x sign through ``horizon``."""
    profile = phase_sign_stability_profile(rotation, horizon)
    thresholds = [
        step.minimum_amplitude_for_x_sign
        for step in profile
        if step.minimum_amplitude_for_x_sign is not None
    ]
    return max(thresholds, default=0)


def exact_first_nonpositive_x_step(
    rotation: PythagoreanRotation,
    max_steps: int,
) -> int | None:
    """First step where the exact lifted unit x-coordinate is <=0."""
    if isinstance(max_steps, bool) or not isinstance(max_steps, int) or max_steps < 0:
        raise ValueError("max_steps must be a non-negative integer")
    x, y = 1, 0
    for step in range(max_steps + 1):
        if x <= 0:
            return step
        x, y = integer_rotation_lift(x, y, rotation)
    return None


def projected_first_nonpositive_x_step(
    amplitude: int,
    rotation: PythagoreanRotation,
    max_steps: int,
) -> int | None:
    """First represented step where sequential projected x<=0."""
    if isinstance(amplitude, bool) or not isinstance(amplitude, int) or amplitude < 0:
        raise ValueError("amplitude must be a non-negative integer")
    if isinstance(max_steps, bool) or not isinstance(max_steps, int) or max_steps < 0:
        raise ValueError("max_steps must be a non-negative integer")
    x, y = amplitude, 0
    for step in range(max_steps + 1):
        if x <= 0:
            return step
        x, y = projected_rotation_step(x, y, rotation, TOWARD_ZERO).after
    return None


def x_sign_certificate_holds(
    amplitude: int,
    rotation: PythagoreanRotation,
    horizon: int,
) -> bool:
    """Verify projected x sign against exact lifted sign when certified by B_k."""
    if isinstance(amplitude, bool) or not isinstance(amplitude, int) or amplitude < 0:
        raise ValueError("amplitude must be a non-negative integer")
    profile = phase_sign_stability_profile(rotation, horizon)
    projected_x, projected_y = amplitude, 0
    for index, info in enumerate(profile):
        exact_x = info.unit_exact[0]
        threshold = info.minimum_amplitude_for_x_sign
        if threshold is not None and amplitude >= threshold:
            if (projected_x > 0) != (exact_x > 0):
                return False
            if (projected_x < 0) != (exact_x < 0):
                return False
        if index < horizon:
            projected_x, projected_y = projected_rotation_step(
                projected_x, projected_y, rotation, TOWARD_ZERO
            ).after
    return True
