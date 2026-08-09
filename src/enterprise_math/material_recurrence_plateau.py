"""Exact fixed-point band of the E001 MIN_QUADRATIC recurrence policy.

For the memory-2 recurrence policy implemented in ``material_recurrence_policy``,
a fixed state must satisfy ``(u,v)=(k,k)``.  At such a state the unprojected
next value is

    ((2*a-c)/c) * k.

The integer candidate ``w=k`` is one of the floor/ceil brackets exactly when

    2*(c-a)*|k| < c.

At ``w=k`` the quadratic defect ``delta*(w-u)`` is zero.  The other bracketing
candidate, when distinct, has negative defect, so the MIN_QUADRATIC policy
selects ``k``.  Therefore the complete fixed set is the diagonal band

    {(k,k): |k| <= floor((c-1)/(2*(c-a)))}.

Thus Q-nonincreasing projection can stabilize on a nonzero finite plateau band;
nonincrease is strictly weaker than the zero-extinction theorem of the
componentwise projected Pythagorean oscillator.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_oscillator import PythagoreanRotation
from .material_recurrence_policy import MIN_QUADRATIC, recurrence_policy_step


@dataclass(frozen=True)
class MinQuadraticPlateau:
    """Exact diagonal fixed-point band for one Pythagorean recurrence policy."""

    rotation: PythagoreanRotation
    radius: int
    fixed_points: tuple[tuple[int, int], ...]
    fixed_point_count: int


def min_quadratic_fixed_plateau_radius(rotation: PythagoreanRotation) -> int:
    """Return K=floor((c-1)/(2*(c-a)))."""
    denominator = 2 * (rotation.c - rotation.a)
    if denominator <= 0:
        raise ValueError("MIN_QUADRATIC plateau requires a<c")
    return (rotation.c - 1) // denominator


def min_quadratic_fixed_points(
    rotation: PythagoreanRotation,
) -> tuple[tuple[int, int], ...]:
    """Return the complete predicted fixed-point diagonal band."""
    radius = min_quadratic_fixed_plateau_radius(rotation)
    return tuple((k, k) for k in range(-radius, radius + 1))


def min_quadratic_is_fixed(
    u: int,
    v: int,
    rotation: PythagoreanRotation,
) -> bool:
    """Whether one concrete state is fixed under the implemented policy."""
    return recurrence_policy_step(u, v, rotation, MIN_QUADRATIC).after == (u, v)


def min_quadratic_fixed_point_theorem(
    u: int,
    v: int,
    rotation: PythagoreanRotation,
) -> bool:
    """Verify implemented fixedness against the closed-form diagonal criterion."""
    radius = min_quadratic_fixed_plateau_radius(rotation)
    predicted = u == v and abs(u) <= radius
    actual = min_quadratic_is_fixed(u, v, rotation)
    if actual != predicted:
        raise AssertionError("MIN_QUADRATIC fixed state disagrees with plateau theorem")
    return actual


def min_quadratic_plateau(rotation: PythagoreanRotation) -> MinQuadraticPlateau:
    """Return and verify the whole finite fixed-point band."""
    fixed = min_quadratic_fixed_points(rotation)
    for state in fixed:
        if not min_quadratic_is_fixed(*state, rotation):
            raise AssertionError("predicted plateau state is not fixed")
    return MinQuadraticPlateau(
        rotation=rotation,
        radius=min_quadratic_fixed_plateau_radius(rotation),
        fixed_points=fixed,
        fixed_point_count=len(fixed),
    )
