"""E001 specialization of the P008 adjoint pattern for material curve operators.

The floor hardening transform

    H_p(s;A)=floor(s^p/A^(p-1))

is *not* the left adjoint of the root softening transform

    G_p(t;A)=floor_root(t*A^(p-1), p).

The exact left adjoint is the ceiling-scaled power

    K_p(s;A)=ceil(s^p/A^(p-1)).

Then on the finite chain ``0..A``:

    K_p(s;A) <= t  iff  s <= G_p(t;A).

Moreover K differs from H by exactly one remainder-boundary bit.  This module is
an application/corollary of the general P008 order-adjoint theory, not a new
mother theorem.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_response import hardening_sample, softening_sample


def _validate(sample: int, amplitude: int, power: int) -> None:
    if isinstance(amplitude, bool) or not isinstance(amplitude, int) or amplitude <= 0:
        raise ValueError("amplitude must be a positive integer")
    if isinstance(sample, bool) or not isinstance(sample, int) or not 0 <= sample <= amplitude:
        raise ValueError("sample must be an integer in 0..amplitude")
    if isinstance(power, bool) or not isinstance(power, int) or power <= 0:
        raise ValueError("power must be a positive integer")


def ceil_hardening_sample(sample: int, amplitude: int, power: int) -> int:
    """Return K_p(s;A)=ceil(s^p/A^(p-1)) using integer arithmetic only."""
    _validate(sample, amplitude, power)
    denominator = amplitude ** (power - 1)
    numerator = sample**power
    return (numerator + denominator - 1) // denominator


@dataclass(frozen=True)
class MaterialAdjointRepair:
    """One floor-to-ceiling repair and adjoint image diagnostic."""

    sample: int
    amplitude: int
    power: int
    floor_hardening: int
    ceil_hardening: int
    remainder: int
    boundary_bit: int
    softening_after_ceil: int
    softening_after_floor: int


def material_adjoint_repair(
    sample: int,
    amplitude: int,
    power: int,
) -> MaterialAdjointRepair:
    """Expose the one-bit repair that turns floor hardening into the adjoint map."""
    _validate(sample, amplitude, power)
    denominator = amplitude ** (power - 1)
    numerator = sample**power
    floor_value = hardening_sample(sample, amplitude, power)
    ceil_value = ceil_hardening_sample(sample, amplitude, power)
    remainder = numerator % denominator
    bit = int(remainder != 0)
    if ceil_value != floor_value + bit:
        raise AssertionError("ceil hardening did not equal floor hardening plus boundary bit")
    return MaterialAdjointRepair(
        sample=sample,
        amplitude=amplitude,
        power=power,
        floor_hardening=floor_value,
        ceil_hardening=ceil_value,
        remainder=remainder,
        boundary_bit=bit,
        softening_after_ceil=softening_sample(ceil_value, amplitude, power),
        softening_after_floor=softening_sample(floor_value, amplitude, power),
    )


def material_adjoint_law(
    sample: int,
    target: int,
    amplitude: int,
    power: int,
) -> bool:
    """Evaluate both sides of K_p(s)<=t iff s<=G_p(t) and verify equality."""
    _validate(sample, amplitude, power)
    _validate(target, amplitude, power)
    left = ceil_hardening_sample(sample, amplitude, power) <= target
    right = sample <= softening_sample(target, amplitude, power)
    if left != right:
        raise AssertionError("scaled power/root adjunction law failed")
    return left
