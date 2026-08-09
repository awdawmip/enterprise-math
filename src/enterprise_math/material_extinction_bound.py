"""Finite state-count bound for toward-zero Pythagorean projection extinction.

The bound now depends on the explicit source theorem in
``material_extinction_theorem``: a valid nontrivial Pythagorean rational
rotation has no nonzero periodic orbit under componentwise toward-zero
projection.

Squared radius is nonincreasing, so all visited represented states remain in the
finite integer Euclidean ball determined by the initial squared norm ``N0``.
With no nonzero state allowed to repeat, deterministic iteration must reach zero
within

    T_extinct <= |{(x,y) in Z^2 : x^2+y^2 <= N0}| - 1.

This is deliberately coarse but requires no floating constants or asymptotics.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import isqrt

from .material_extinction_theorem import certify_no_nonzero_periodic_orbit
from .material_oscillator import TOWARD_ZERO, PythagoreanRotation, projected_rotation_step


@dataclass(frozen=True)
class ExtinctionBoundReport:
    """Finite state-count bound and witnessed extinction time with theorem anchor."""

    initial_state: tuple[int, int]
    initial_norm_sq: int
    lattice_ball_state_count: int
    transition_upper_bound: int
    witnessed_extinction_time: int | None
    no_nonzero_cycle_certified: bool
    reduced_rotation_trace_denominator: int


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
    """Return the finite lattice-ball transition count used after theorem certification."""
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
    """Run the reference map to zero under the theorem-backed finite bound."""
    theorem = certify_no_nonzero_periodic_orbit(rotation)
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
                raise AssertionError(
                    "nonzero state repeated despite certified no-cycle theorem"
                )
            seen.add((x, y))
        if extinction is None:
            raise AssertionError("projected rotation exceeded finite lattice-ball extinction bound")
    return ExtinctionBoundReport(
        initial_state=initial_state,
        initial_norm_sq=norm_sq,
        lattice_ball_state_count=count,
        transition_upper_bound=bound,
        witnessed_extinction_time=extinction,
        no_nonzero_cycle_certified=theorem.no_nonzero_periodic_orbit,
        reduced_rotation_trace_denominator=(
            theorem.finite_order_obstruction.reduced_trace_denominator
        ),
    )
