"""E001 material-response pressure tests built from integer-only oscillators.

This module deliberately keeps three intrinsic constructions separate:

1. an exact Pythagorean integer rotation lift followed by an explicit signed
   projection;
2. a second-order integer recurrence derived from the same rational rotation;
3. a root-basin digital quarter circle used as a static monotone curve basis.

Conventional real-valued sine is not used anywhere in this module.  External
``sin`` comparisons belong in experiments only.

The signed projection convention is explicit.  In particular, projection
*toward zero* has a useful exact safety property for the Pythagorean lift: the
projected squared radius never increases.  Ordinary floor division does not
have that property on negative coordinates and is retained only as a comparison
policy.
"""

from __future__ import annotations

from dataclasses import dataclass

from .core import integer_nth_root

TOWARD_ZERO = "TOWARD_ZERO"
FLOOR = "FLOOR"
ProjectionMode = str


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


@dataclass(frozen=True)
class PythagoreanRotation:
    """One exact integer lift of a rational circle rotation."""

    a: int
    b: int
    c: int

    def __post_init__(self) -> None:
        _require_natural("a", self.a)
        _require_positive("b", self.b)
        _require_positive("c", self.c)
        if self.a >= self.c or self.b >= self.c:
            raise ValueError("a and b must be strictly smaller than c")
        if self.a * self.a + self.b * self.b != self.c * self.c:
            raise ValueError("rotation coefficients must satisfy a^2+b^2=c^2")


def signed_divmod_toward_zero(value: int, divisor: int) -> tuple[int, int]:
    """Return exact signed quotient/detail with quotient truncated toward zero.

    The result obeys ``value = divisor*quotient + detail`` and
    ``abs(detail) < divisor``.  Nonzero detail has the same sign as ``value``.
    """
    _require_integer("value", value)
    _require_positive("divisor", divisor)
    if value == 0:
        return 0, 0
    sign = 1 if value > 0 else -1
    quotient = sign * (abs(value) // divisor)
    detail = value - divisor * quotient
    if abs(detail) >= divisor:
        raise AssertionError("toward-zero detail escaped its bounded fiber")
    if detail and ((detail > 0) != (value > 0)):
        raise AssertionError("toward-zero detail changed sign")
    return quotient, detail


def signed_project(value: int, divisor: int, mode: ProjectionMode = TOWARD_ZERO) -> int:
    """Project one signed integer by an explicit finite-resolution convention."""
    _require_integer("value", value)
    _require_positive("divisor", divisor)
    if mode == TOWARD_ZERO:
        return signed_divmod_toward_zero(value, divisor)[0]
    if mode == FLOOR:
        return value // divisor
    raise ValueError("unknown signed projection mode")


def integer_rotation_lift(
    x: int, y: int, rotation: PythagoreanRotation
) -> tuple[int, int]:
    """Apply the exact fraction-free rotation lift."""
    _require_integer("x", x)
    _require_integer("y", y)
    return (
        rotation.a * x - rotation.b * y,
        rotation.b * x + rotation.a * y,
    )


@dataclass(frozen=True)
class ProjectedRotationStep:
    """Exact diagnostics for one lifted-then-projected oscillator step."""

    before: tuple[int, int]
    raw_lift: tuple[int, int]
    after: tuple[int, int]
    details: tuple[int, int]
    norm_sq_before: int
    norm_sq_after: int
    norm_sq_loss: int


def projected_rotation_step(
    x: int,
    y: int,
    rotation: PythagoreanRotation,
    mode: ProjectionMode = TOWARD_ZERO,
) -> ProjectedRotationStep:
    """Apply one fixed-resolution step and expose all projection defects."""
    raw_x, raw_y = integer_rotation_lift(x, y, rotation)
    before_norm = x * x + y * y
    raw_norm = raw_x * raw_x + raw_y * raw_y
    expected_raw_norm = rotation.c * rotation.c * before_norm
    if raw_norm != expected_raw_norm:
        raise AssertionError("Pythagorean lift lost its exact norm identity")

    if mode == TOWARD_ZERO:
        next_x, detail_x = signed_divmod_toward_zero(raw_x, rotation.c)
        next_y, detail_y = signed_divmod_toward_zero(raw_y, rotation.c)
    elif mode == FLOOR:
        next_x = raw_x // rotation.c
        next_y = raw_y // rotation.c
        detail_x = raw_x - rotation.c * next_x
        detail_y = raw_y - rotation.c * next_y
    else:
        raise ValueError("unknown signed projection mode")

    after_norm = next_x * next_x + next_y * next_y
    loss = before_norm - after_norm
    if mode == TOWARD_ZERO and loss < 0:
        raise AssertionError("toward-zero projection increased squared radius")

    return ProjectedRotationStep(
        before=(x, y),
        raw_lift=(raw_x, raw_y),
        after=(next_x, next_y),
        details=(detail_x, detail_y),
        norm_sq_before=before_norm,
        norm_sq_after=after_norm,
        norm_sq_loss=loss,
    )


def projected_rotation_orbit(
    amplitude: int,
    rotation: PythagoreanRotation,
    steps: int,
    mode: ProjectionMode = TOWARD_ZERO,
) -> tuple[tuple[int, int], ...]:
    """Return the initial state and ``steps`` projected oscillator states."""
    _require_natural("amplitude", amplitude)
    _require_natural("steps", steps)
    state = (amplitude, 0)
    orbit = [state]
    for _ in range(steps):
        state = projected_rotation_step(*state, rotation, mode).after
        orbit.append(state)
    return tuple(orbit)


def projected_rotation_first_repeat(
    amplitude: int,
    rotation: PythagoreanRotation,
    max_steps: int,
    mode: ProjectionMode = TOWARD_ZERO,
) -> tuple[int, int, tuple[tuple[int, int], ...]] | None:
    """Return ``(first_index, repeat_index, states)`` for the first repeated state."""
    _require_natural("amplitude", amplitude)
    _require_positive("max_steps", max_steps)
    seen: dict[tuple[int, int], int] = {}
    states: list[tuple[int, int]] = []
    state = (amplitude, 0)
    for index in range(max_steps + 1):
        if state in seen:
            return seen[state], index, tuple(states)
        seen[state] = index
        states.append(state)
        state = projected_rotation_step(*state, rotation, mode).after
    return None


def recurrence_sine_samples(
    amplitude: int,
    rotation: PythagoreanRotation,
    sample_count: int,
    mode: ProjectionMode = TOWARD_ZERO,
) -> tuple[int, ...]:
    """Return a memory-2 integer sine-like recurrence on one amplitude axis.

    The unprojected rational relation is

        c*y_(n+2) = 2*a*y_(n+1) - c*y_n.

    Every step explicitly projects the right-hand numerator by ``c``.
    """
    _require_natural("amplitude", amplitude)
    _require_positive("sample_count", sample_count)
    if sample_count == 1:
        return (0,)
    previous = 0
    current = signed_project(rotation.b * amplitude, rotation.c, mode)
    samples = [previous, current]
    while len(samples) < sample_count:
        numerator = 2 * rotation.a * current - rotation.c * previous
        following = signed_project(numerator, rotation.c, mode)
        samples.append(following)
        previous, current = current, following
    return tuple(samples)


def recurrence_first_repeat(
    amplitude: int,
    rotation: PythagoreanRotation,
    max_steps: int,
    mode: ProjectionMode = TOWARD_ZERO,
) -> tuple[int, int] | None:
    """Detect the first repeated memory-2 recurrence state."""
    _require_natural("amplitude", amplitude)
    _require_positive("max_steps", max_steps)
    previous = 0
    current = signed_project(rotation.b * amplitude, rotation.c, mode)
    seen: dict[tuple[int, int], int] = {}
    for index in range(max_steps + 1):
        pair = (previous, current)
        if pair in seen:
            return seen[pair], index
        seen[pair] = index
        numerator = 2 * rotation.a * current - rotation.c * previous
        following = signed_project(numerator, rotation.c, mode)
        previous, current = current, following
    return None


def digital_circle_quarter(amplitude: int) -> tuple[tuple[int, int], ...]:
    """Return an intrinsic root-basin quarter circle with integer x-phase.

    For x=A,A-1,...,0 use the largest integer y satisfying x^2+y^2<=A^2.
    The result is a monotone static curve basis; it is not an equal-angle clock.
    """
    _require_natural("amplitude", amplitude)
    radius_sq = amplitude * amplitude
    points = []
    for x in range(amplitude, -1, -1):
        y = integer_nth_root(radius_sq - x * x, 2)
        points.append((x, y))
    return tuple(points)


def digital_circle_radial_defect(amplitude: int, point: tuple[int, int]) -> int:
    """Return ``A^2-x^2-y^2`` for one point of the inward digital quarter circle."""
    _require_natural("amplitude", amplitude)
    x, y = point
    _require_natural("x", x)
    _require_natural("y", y)
    defect = amplitude * amplitude - x * x - y * y
    if defect < 0:
        raise ValueError("point lies outside the radius-A integer disk")
    return defect
