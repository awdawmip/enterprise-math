"""Alternative projection policy for the E001 memory-2 recurrence.

Toward-zero projection can pump the recurrence quadratic observable because
``Q_before-Q_after=delta*(w-u)`` has no fixed sign.  For nonintegral raw/c there
are exactly two bracketing integer quotients: floor and ceil.  Their details have
opposite signs, and the previous memory coordinate ``u`` cannot lie strictly
between two consecutive integers.  Therefore at least one bracketing candidate
has nonnegative quadratic defect.

The ``MIN_QUADRATIC`` policy chooses the candidate with smallest next Q (largest
nonnegative defect).  It guarantees Q never increases, but it can stabilize at
nonzero quantized plateaus; nonincrease is not the same as extinction.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_oscillator import PythagoreanRotation, signed_divmod_toward_zero
from .material_recurrence_invariant import recurrence_quadratic

MIN_QUADRATIC = "MIN_QUADRATIC"
TOWARD_ZERO = "TOWARD_ZERO"


@dataclass(frozen=True)
class RecurrenceProjectionCandidate:
    """One integer quotient candidate and its exact quadratic defect."""

    next_value: int
    detail: int
    quadratic_after: int
    quadratic_defect: int


@dataclass(frozen=True)
class RecurrencePolicyStep:
    """One memory-2 recurrence update under an explicit projection policy."""

    before: tuple[int, int]
    raw_second: int
    floor_candidate: RecurrenceProjectionCandidate
    ceil_candidate: RecurrenceProjectionCandidate
    selected: RecurrenceProjectionCandidate
    after: tuple[int, int]
    policy: str


def _candidate(
    u: int,
    v: int,
    raw_second: int,
    w: int,
    rotation: PythagoreanRotation,
) -> RecurrenceProjectionCandidate:
    detail = raw_second - rotation.c * w
    q_before = recurrence_quadratic(u, v, rotation)
    q_after = recurrence_quadratic(v, w, rotation)
    defect = q_before - q_after
    if defect != detail * (w - u):
        raise AssertionError("candidate quadratic defect identity failed")
    return RecurrenceProjectionCandidate(
        next_value=w,
        detail=detail,
        quadratic_after=q_after,
        quadratic_defect=defect,
    )


def recurrence_policy_step(
    u: int,
    v: int,
    rotation: PythagoreanRotation,
    policy: str = MIN_QUADRATIC,
) -> RecurrencePolicyStep:
    """Evaluate floor/ceil candidates and select one declared projection policy."""
    for name, value in (("u", u), ("v", v)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    raw = 2 * rotation.a * v - rotation.c * u
    floor_w = raw // rotation.c
    floor_candidate = _candidate(u, v, raw, floor_w, rotation)
    if raw % rotation.c == 0:
        ceil_w = floor_w
    else:
        ceil_w = floor_w + 1
    ceil_candidate = _candidate(u, v, raw, ceil_w, rotation)

    if policy == TOWARD_ZERO:
        toward_w, _detail = signed_divmod_toward_zero(raw, rotation.c)
        selected = floor_candidate if toward_w == floor_w else ceil_candidate
    elif policy == MIN_QUADRATIC:
        candidates = (floor_candidate, ceil_candidate)
        selected = min(
            candidates,
            key=lambda item: (
                item.quadratic_after,
                abs(item.detail),
                abs(item.next_value),
                item.next_value,
            ),
        )
        if selected.quadratic_defect < 0:
            raise AssertionError("bracketing projection failed to provide nonincreasing Q")
    else:
        raise ValueError("unknown recurrence projection policy")

    return RecurrencePolicyStep(
        before=(u, v),
        raw_second=raw,
        floor_candidate=floor_candidate,
        ceil_candidate=ceil_candidate,
        selected=selected,
        after=(v, selected.next_value),
        policy=policy,
    )


def recurrence_policy_orbit(
    initial_pair: tuple[int, int],
    rotation: PythagoreanRotation,
    policy: str,
    max_steps: int,
) -> tuple[tuple[int, int], ...]:
    """Run until the first repeated memory state or max_steps, retaining that repeat."""
    if isinstance(max_steps, bool) or not isinstance(max_steps, int) or max_steps < 0:
        raise ValueError("max_steps must be a non-negative integer")
    state = initial_pair
    states = [state]
    seen = {state}
    for _ in range(max_steps):
        state = recurrence_policy_step(*state, rotation, policy).after
        states.append(state)
        if state in seen:
            break
        seen.add(state)
    return tuple(states)
