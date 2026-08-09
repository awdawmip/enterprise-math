"""Finite state-count bound for toward-zero Pythagorean projection extinction.

For the nontrivial componentwise projected Pythagorean oscillator, squared radius
is nonincreasing and every non-exact step decreases it.  The separate extinction
theorem rules out nonzero periodic orbits.  Consequently no nonzero state can
repeat before the orbit reaches zero.

All visited states lie in the finite integer Euclidean ball determined by the
initial squared norm N0, giving the exact finite upper bound

    T_extinct <= |{(x,y) in Z^2 : x^2+y^2 <= N0}| - 1.

This is deliberately coarse but requires no floating constants or asymptotics.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt

from .material_oscillator import TOWARD_ZERO, PythagoreanRotation, projected_rotation_step


@dataclass(frozen=True)
class ExtinctionBoundReport:
    """Finite state-count bound and optional witnessed extinction time."""

    initial_state: tuple[int, int]
    initial_norm_sq: int
    lattice_ball_state_count: int
    transition_upper_bound: int
    witnessed_extinction_time: int | None


def integer_euclidean_ball_count_from_norm_sq(norm_sq: int) -> int:
    """Count integer pairs with x^2+y^2<=norm_sq using integer arithmetic only."""
    if isinstance(norm_sq, bool) or not isinstance(norm_sq, int) or norm_sq < 0:
        raise ValueError("norm_sq must be a non-negative integer")
    radius = isqrt(norm_sq)
    total = 0
    for x in range(-radius, radius + 1):
        y_max = isqrt(norm_sq - x * x)
        total += 2 * y_max + 1
    return total


def projected_rotation_extinction_upper_bound(initial_state: tuple[int, int]) -> int:
    """Return the finite non-repetition state-count upper bound on transitions."""
    x, y = initial_state
    for name, value in (("x", x), ("y", y)):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    norm_sq = x * x + y * y
    return integer_euclidean_ball_count_from_norm_sq(norm_sq) - 1


def witness_extinction_within_bound(
    initial_state: tuple[int, int],
    rotation: PythagoreanRotation,
) -> ExtinctionBoundReport:
    """Run the reference map until zero, asserting the finite state-count bound."""
    x, y = initial_state
    norm_sq = x * x + y * y
    count = integer_euclidean_ball_count_from_norm_sq(norm_sq)
    bound = count - 1
    if (x, y) == (0, 0):
        extinction = 0
    else:
        seen = {(x, y)}
        extinction = None
        for step in range(1, bound + 1):
            x, y = projected_rotation_step(x, y, rotation, TOWARD_ZERO).after
            if (x, y) == (0, 0):
                extinction = step
                break
            if (x, y) in seen:
                raise AssertionError("nonzero projected rotation state repeated before extinction")
            seen.add((x, y))
        if extinction is None:
            raise AssertionError("projected rotation exceeded finite lattice-ball extinction bound")
    return ExtinctionBoundReport(
        initial_state=initial_state,
        initial_norm_sq=norm_sq,
        lattice_ball_state_count=count,
        transition_upper_bound=bound,
        witnessed_extinction_time=extinction,
    )
