"""Finite iteration dynamics of E001 material shape operators.

For p>1 on the finite amplitude chain 0..A:

* hardening H_p is reductive and strictly decreases every interior state, so
  repeated hardening reaches 0 in finitely many steps; its only fixed points
  are 0 and A;
* softening G_p is extensive.  Its positive fixed points form one terminal
  interval ``tau..A``.  Every positive state below ``tau`` iterates exactly to
  ``tau``; states at/above ``tau`` are already fixed.

These are finite integer dynamics, not physical aging laws unless a material
model explicitly chooses to iterate these operators over time/cycles.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_response import hardening_sample, softening_sample

HARDENING = "HARDENING"
SOFTENING = "SOFTENING"


@dataclass(frozen=True)
class MaterialIterationTrace:
    """Finite orbit of one repeatedly applied material shape operator."""

    operator: str
    amplitude: int
    power: int
    initial: int
    states: tuple[int, ...]
    stabilized_at: int
    strict_steps: int


def _validate(sample: int, amplitude: int, power: int) -> None:
    if isinstance(amplitude, bool) or not isinstance(amplitude, int) or amplitude <= 0:
        raise ValueError("amplitude must be a positive integer")
    if isinstance(sample, bool) or not isinstance(sample, int) or not 0 <= sample <= amplitude:
        raise ValueError("sample must be an integer in 0..amplitude")
    if isinstance(power, bool) or not isinstance(power, int) or power <= 1:
        raise ValueError("power must be an integer >1")


def hardening_fixed(sample: int, amplitude: int, power: int) -> bool:
    _validate(sample, amplitude, power)
    return hardening_sample(sample, amplitude, power) == sample


def softening_fixed(sample: int, amplitude: int, power: int) -> bool:
    _validate(sample, amplitude, power)
    return softening_sample(sample, amplitude, power) == sample


def softening_fixed_by_basin(sample: int, amplitude: int, power: int) -> bool:
    """Exact fixed-point criterion s*A^(p-1) < (s+1)^p."""
    _validate(sample, amplitude, power)
    return sample * amplitude ** (power - 1) < (sample + 1) ** power


def softening_positive_fixed_threshold(amplitude: int, power: int) -> int:
    """Return the smallest positive G_p fixed state ``tau``.

    The positive fixed predicate is upward closed for p>1.  For s>=1,
    ``(s+1)^p/s`` is nondecreasing: the adjacent inequality follows from
    ``(1+1/(s+1))^p >= 1+p/(s+1) >= 1+1/s``.  Hence one binary search locates
    the first positive fixed state without floating arithmetic.
    """
    _validate(0, amplitude, power)
    lo = 1
    hi = amplitude
    while lo < hi:
        mid = (lo + hi) // 2
        if softening_fixed_by_basin(mid, amplitude, power):
            hi = mid
        else:
            lo = mid + 1
    if not softening_fixed_by_basin(lo, amplitude, power):
        raise AssertionError("positive softening fixed threshold was not found")
    if lo > 1 and softening_fixed_by_basin(lo - 1, amplitude, power):
        raise AssertionError("softening threshold is not minimal")
    return lo


def softening_stabilized_state(sample: int, amplitude: int, power: int) -> int:
    """Closed-form eventual state of repeated G_p."""
    _validate(sample, amplitude, power)
    if sample == 0:
        return 0
    threshold = softening_positive_fixed_threshold(amplitude, power)
    return max(sample, threshold)


def iterate_hardening(sample: int, amplitude: int, power: int) -> MaterialIterationTrace:
    """Iterate H_p until its finite fixed point is reached."""
    _validate(sample, amplitude, power)
    states = [sample]
    current = sample
    while True:
        following = hardening_sample(current, amplitude, power)
        if following == current:
            break
        if not following < current:
            raise AssertionError("interior hardening failed strict reductivity")
        states.append(following)
        current = following
    if current not in (0, amplitude):
        raise AssertionError("hardening stabilized at an unexpected interior fixed point")
    return MaterialIterationTrace(
        operator=HARDENING,
        amplitude=amplitude,
        power=power,
        initial=sample,
        states=tuple(states),
        stabilized_at=current,
        strict_steps=len(states) - 1,
    )


def iterate_softening(sample: int, amplitude: int, power: int) -> MaterialIterationTrace:
    """Iterate G_p until its finite fixed plateau is reached."""
    _validate(sample, amplitude, power)
    expected_terminal = softening_stabilized_state(sample, amplitude, power)
    states = [sample]
    current = sample
    while True:
        following = softening_sample(current, amplitude, power)
        if following == current:
            break
        if not following > current:
            raise AssertionError("non-fixed softening failed strict extensivity")
        if following > expected_terminal:
            raise AssertionError("softening overshot its least reachable fixed plateau")
        states.append(following)
        current = following
        if len(states) > amplitude + 1:
            raise AssertionError("softening exceeded finite-chain stabilization bound")
    if not softening_fixed_by_basin(current, amplitude, power):
        raise AssertionError("softening fixed point disagrees with root-basin criterion")
    if current != expected_terminal:
        raise AssertionError("softening orbit disagrees with closed-form terminal state")
    return MaterialIterationTrace(
        operator=SOFTENING,
        amplitude=amplitude,
        power=power,
        initial=sample,
        states=tuple(states),
        stabilized_at=current,
        strict_steps=len(states) - 1,
    )
