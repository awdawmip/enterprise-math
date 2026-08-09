"""Exact finite invariants for E001 material-oscillator research.

This module does not introduce a new constitutive law.  It extracts exact
integer consequences from the existing Pythagorean projected oscillator and
material-curve transforms:

* an exact per-step collapse-loss certificate;
* a parameterized Pythagorean turn family and its finite resolution dead zone;
* explicit comparison between stepwise projection and one terminal projection;
* non-negative composition defects for staged hardening/softening transforms.

All state and certificates are integer-valued.  No real-valued sine, pi, true
division, force, impulse, or energy unit is assumed.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_oscillator import (
    TOWARD_ZERO,
    PythagoreanRotation,
    integer_rotation_lift,
    projected_rotation_orbit,
    projected_rotation_step,
    signed_project,
)
from .material_response import hardening_sample, softening_sample


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def _require_natural(name: str, value: int) -> None:
    _require_integer(name, value)
    if value < 0:
        raise ValueError(f"{name} must be non-negative")


def _require_positive(name: str, value: int) -> None:
    _require_integer(name, value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def parameter_rotation(m: int) -> PythagoreanRotation:
    """Return the exact integer turn `(m^2-1, 2m, m^2+1)` for `m>=2`."""
    _require_integer("m", m)
    if m < 2:
        raise ValueError("m must be at least 2")
    return PythagoreanRotation(m * m - 1, 2 * m, m * m + 1)


def toward_zero_loss_certificate(
    x: int, y: int, rotation: PythagoreanRotation
) -> int:
    """Return the exact numerator certifying one squared-radius loss.

    For a toward-zero projected step with details `r_x,r_y`, this proves

        c^2 (E_before-E_after)
          = 2c(|x'| |r_x| + |y'| |r_y|) + r_x^2 + r_y^2.

    The returned integer is both sides of that identity.
    """
    report = projected_rotation_step(x, y, rotation, TOWARD_ZERO)
    next_x, next_y = report.after
    detail_x, detail_y = report.details
    rhs = (
        2
        * rotation.c
        * (abs(next_x) * abs(detail_x) + abs(next_y) * abs(detail_y))
        + detail_x * detail_x
        + detail_y * detail_y
    )
    lhs = rotation.c * rotation.c * report.norm_sq_loss
    if lhs != rhs:
        raise AssertionError("toward-zero collapse loss identity failed")
    return rhs


def minimum_transverse_amplitude(rotation: PythagoreanRotation) -> int:
    """Smallest axis amplitude whose first projected turn has nonzero y-state."""
    return (rotation.c + rotation.b - 1) // rotation.b


def parameter_rotation_minimum_transverse_amplitude(m: int) -> int:
    """Closed form dead-zone boundary for :func:`parameter_rotation`.

    The exact value is `floor(m/2)+1`.  Equivalently a nonzero first transverse
    response at amplitude `A` requires `m < 2A`.
    """
    rotation = parameter_rotation(m)
    threshold = minimum_transverse_amplitude(rotation)
    expected = m // 2 + 1
    if threshold != expected:
        raise AssertionError("parameterized transverse threshold identity failed")
    return threshold


def axis_dead_zone_orbit(
    amplitude: int, rotation: PythagoreanRotation
) -> tuple[tuple[int, int], ...]:
    """Return the exact axis-only decay orbit below the transverse threshold.

    Below the threshold the y-coordinate can never become nonzero: x strictly
    decreases under toward-zero projection until `(0,0)` is reached.
    """
    _require_natural("amplitude", amplitude)
    threshold = minimum_transverse_amplitude(rotation)
    if amplitude >= threshold:
        raise ValueError("amplitude is not inside the transverse dead zone")

    state = (amplitude, 0)
    states = [state]
    for _ in range(amplitude + 1):
        if state == (0, 0):
            return tuple(states)
        following = projected_rotation_step(*state, rotation, TOWARD_ZERO).after
        if following[1] != 0:
            raise AssertionError("dead-zone orbit created transverse motion")
        if not 0 <= following[0] < state[0]:
            raise AssertionError("dead-zone axis state failed to decrease")
        state = following
        states.append(state)
    raise AssertionError("dead-zone orbit failed to reach zero in finite steps")


def exact_scaled_rotation_state(
    amplitude: int, rotation: PythagoreanRotation, steps: int
) -> tuple[int, int, int]:
    """Return the unprojected integer lift `(U,V,scale)` after finitely many turns."""
    _require_natural("amplitude", amplitude)
    _require_natural("steps", steps)
    x, y = amplitude, 0
    scale = 1
    for _ in range(steps):
        x, y = integer_rotation_lift(x, y, rotation)
        scale *= rotation.c
    expected = amplitude * amplitude * scale * scale
    if x * x + y * y != expected:
        raise AssertionError("scaled rotation state lost its exact norm identity")
    return x, y, scale


def terminal_projected_rotation_state(
    amplitude: int, rotation: PythagoreanRotation, steps: int
) -> tuple[int, int]:
    """Project only once after the exact finite lifted history."""
    x, y, scale = exact_scaled_rotation_state(amplitude, rotation, steps)
    return signed_project(x, scale, TOWARD_ZERO), signed_project(y, scale, TOWARD_ZERO)


@dataclass(frozen=True)
class ProjectionHistoryComparison:
    """Stepwise-vs-terminal projection result for the same exact lifted turns."""

    stepwise: tuple[int, int]
    terminal: tuple[int, int]
    defect: tuple[int, int]
    l1_defect: int


def projection_history_comparison(
    amplitude: int, rotation: PythagoreanRotation, steps: int
) -> ProjectionHistoryComparison:
    """Expose history dependence created solely by intermediate projections."""
    stepwise = projected_rotation_orbit(amplitude, rotation, steps, TOWARD_ZERO)[-1]
    terminal = terminal_projected_rotation_state(amplitude, rotation, steps)
    defect = (stepwise[0] - terminal[0], stepwise[1] - terminal[1])
    return ProjectionHistoryComparison(
        stepwise=stepwise,
        terminal=terminal,
        defect=defect,
        l1_defect=abs(defect[0]) + abs(defect[1]),
    )


def first_resolved_loading_lobe(
    amplitude: int,
    rotation: PythagoreanRotation,
) -> tuple[int, ...]:
    """Extract the first nondecreasing y-lobe until its first plateau/turn.

    This is a finite material-curve basis, not a claim that all material loading
    curves are sinusoidal.  A dead-zone amplitude returns `(0,)`.
    """
    _require_natural("amplitude", amplitude)
    if amplitude < minimum_transverse_amplitude(rotation):
        return (0,)

    state = (amplitude, 0)
    samples = [0]
    seen = {state}
    max_states = (2 * amplitude + 1) ** 2
    for _ in range(max_states):
        following = projected_rotation_step(*state, rotation, TOWARD_ZERO).after
        next_y = following[1]
        if next_y <= samples[-1]:
            return tuple(samples)
        samples.append(next_y)
        state = following
        if state in seen:
            raise AssertionError("nonzero projected cycle appeared before loading peak")
        seen.add(state)
    raise AssertionError("finite loading lobe failed to turn within bounded state space")


def hardening_composition_defect(
    sample: int, amplitude: int, outer_power: int, inner_power: int
) -> int:
    """Return `H_pq(s)-H_p(H_q(s))`, always a non-negative integer."""
    _require_positive("outer_power", outer_power)
    _require_positive("inner_power", inner_power)
    direct = hardening_sample(sample, amplitude, outer_power * inner_power)
    staged = hardening_sample(
        hardening_sample(sample, amplitude, inner_power),
        amplitude,
        outer_power,
    )
    defect = direct - staged
    if defect < 0:
        raise AssertionError("staged hardening exceeded direct product-order hardening")
    return defect


def softening_composition_defect(
    sample: int, amplitude: int, outer_power: int, inner_power: int
) -> int:
    """Return `G_pq(s)-G_p(G_q(s))`, always a non-negative integer."""
    _require_positive("outer_power", outer_power)
    _require_positive("inner_power", inner_power)
    direct = softening_sample(sample, amplitude, outer_power * inner_power)
    staged = softening_sample(
        softening_sample(sample, amplitude, inner_power),
        amplitude,
        outer_power,
    )
    defect = direct - staged
    if defect < 0:
        raise AssertionError("staged softening exceeded direct product-order softening")
    return defect
