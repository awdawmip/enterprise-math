"""Finite iteration dynamics of E001 material shape operators.

For p>1 on the finite amplitude chain 0..A:

* hardening H_p is reductive and strictly decreases every interior state, so
  repeated hardening reaches 0 in finitely many steps; its only fixed points
  are 0 and A;
* softening G_p is extensive, so repeated softening reaches a fixed plateau in
  finitely many steps.  Interior fixed plateaus can exist.

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
    states = [sample]
    current = sample
    while True:
        following = softening_sample(current, amplitude, power)
        if following == current:
            break
        if not following > current:
            raise AssertionError("non-fixed softening failed strict extensivity")
        states.append(following)
        current = following
        if len(states) > amplitude + 1:
            raise AssertionError("softening exceeded finite-chain stabilization bound")
    if not softening_fixed_by_basin(current, amplitude, power):
        raise AssertionError("softening fixed point disagrees with root-basin criterion")
    return MaterialIterationTrace(
        operator=SOFTENING,
        amplitude=amplitude,
        power=power,
        initial=sample,
        states=tuple(states),
        stabilized_at=current,
        strict_steps=len(states) - 1,
    )
