"""Exact quadratic accounting for the E001 memory-2 oscillator candidate.

For the rational recurrence

    c*y_(n+2) = 2*a*y_(n+1) - c*y_n,

treat the pair ``(u,v)=(y_n,y_(n+1))``.  The fraction-free lift

    (u,v) -> (c*v, 2*a*v-c*u)

preserves the quadratic form ``Q(u,v)=c(u^2+v^2)-2*a*u*v`` up to the expected
scale factor ``c^2``.

After toward-zero projection ``2*a*v-c*u=c*w+delta``, the fixed-scale defect is
exactly

    Q(u,v)-Q(v,w) = delta*(w-u).

Unlike the componentwise Pythagorean rotation loss, this defect has no universal
sign.  Local increases and decreases can therefore balance on a nonzero finite
cycle.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_oscillator import PythagoreanRotation, signed_divmod_toward_zero


@dataclass(frozen=True)
class RecurrenceInvariantStep:
    """One exact quadratic-form accounting step of the projected recurrence."""

    before: tuple[int, int]
    raw_lift: tuple[int, int]
    after: tuple[int, int]
    detail: int
    quadratic_before: int
    quadratic_after: int
    quadratic_defect: int
    reconstructed_defect: int


def recurrence_quadratic(u: int, v: int, rotation: PythagoreanRotation) -> int:
    """Return Q(u,v)=c(u^2+v^2)-2*a*u*v."""
    for name, value in (("u", u), ("v", v)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    return rotation.c * (u * u + v * v) - 2 * rotation.a * u * v


def recurrence_invariant_step(
    u: int,
    v: int,
    rotation: PythagoreanRotation,
) -> RecurrenceInvariantStep:
    """Project one recurrence step and verify the exact signed defect identity."""
    q_before = recurrence_quadratic(u, v, rotation)
    raw_second = 2 * rotation.a * v - rotation.c * u
    raw_lift = (rotation.c * v, raw_second)
    raw_q = recurrence_quadratic(*raw_lift, rotation)
    if raw_q != rotation.c * rotation.c * q_before:
        raise AssertionError("fraction-free recurrence lift lost its quadratic invariant")

    w, detail = signed_divmod_toward_zero(raw_second, rotation.c)
    q_after = recurrence_quadratic(v, w, rotation)
    defect = q_before - q_after
    reconstructed = detail * (w - u)
    if defect != reconstructed:
        raise AssertionError("recurrence projection defect identity failed")

    return RecurrenceInvariantStep(
        before=(u, v),
        raw_lift=raw_lift,
        after=(v, w),
        detail=detail,
        quadratic_before=q_before,
        quadratic_after=q_after,
        quadratic_defect=defect,
        reconstructed_defect=reconstructed,
    )


def recurrence_quadratic_trace(
    initial_pair: tuple[int, int],
    rotation: PythagoreanRotation,
    steps: int,
) -> tuple[RecurrenceInvariantStep, ...]:
    """Trace signed local defects; their sum telescopes to endpoint Q difference."""
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 0:
        raise ValueError("steps must be a non-negative integer")
    u, v = initial_pair
    trace: list[RecurrenceInvariantStep] = []
    for _ in range(steps):
        report = recurrence_invariant_step(u, v, rotation)
        trace.append(report)
        u, v = report.after
    if trace:
        total = sum(report.quadratic_defect for report in trace)
        endpoint = trace[0].quadratic_before - trace[-1].quadratic_after
        if total != endpoint:
            raise AssertionError("recurrence quadratic defects failed to telescope")
    return tuple(trace)
