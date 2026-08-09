"""E001.7 exact integer tick windows for constant relative lattice motion.

The 1D phase-independent no-skip bound does not generalize by replacing the
step with a vector norm.  In multiple coordinates, each coordinate may enter
the macro-contact band at different integer ticks.

For a constant relative lattice trajectory

    q(n) = q0 + n*v,  n in N,

and E001 square contact half-width ``H=R+d-1``, static macro contact at tick ``n``
requires every coordinate of ``q(n)`` to lie in ``[-H,H]``.  Each coordinate
gives an exact integer interval of admissible ticks.  Their intersection is the
complete static-contact tick window.

This is discrete arithmetic only.  It deliberately does not infer collision
from continuous line-segment crossings between sampled lattice states.  If the
primitive geometry wants such crossings to be interaction events, A5/P022 must
represent the corresponding transition incidence explicitly.
"""

from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Sequence

from .collision_phase_diagram import contact_half_width_1d


@dataclass(frozen=True)
class ContactTickWindow:
    """Inclusive non-negative integer ticks at which static macro contact holds."""

    first_tick: int
    last_tick: int | None

    def contains(self, tick: int) -> bool:
        if isinstance(tick, bool) or not isinstance(tick, int) or tick < 0:
            return False
        if tick < self.first_tick:
            return False
        return self.last_tick is None or tick <= self.last_tick


def _ceil_div(numerator: int, denominator: int) -> int:
    if denominator == 0:
        raise ZeroDivisionError("ceil division denominator must be nonzero")
    return -((-numerator) // denominator)


def _coordinate_tick_window(
    start: int,
    step: int,
    half_width: int,
) -> tuple[int, int] | None:
    """All integer ticks n in Z with ``|start+n*step|<=half_width``."""
    if step == 0:
        if abs(start) <= half_width:
            # Use a very wide symbolic interval; the public solver handles the
            # unbounded non-negative end explicitly.
            return (-(10**30), 10**30)
        return None

    if step > 0:
        lower = _ceil_div(-half_width - start, step)
        upper = (half_width - start) // step
    else:
        lower = _ceil_div(half_width - start, step)
        upper = (-half_width - start) // step
    if lower > upper:
        return None
    return lower, upper


def static_contact_tick_window(
    start: Sequence[int],
    step: Sequence[int],
    radius_sum: int,
    collapse_factor: int,
) -> ContactTickWindow | None:
    """Return the exact non-negative integer tick window for square macro contact.

    ``start`` and ``step`` are the signed relative center coordinate and its
    constant per-tick update.  Any finite dimension is supported because square
    / L-infinity contact is coordinatewise.
    """
    if len(start) == 0 or len(start) != len(step):
        raise ValueError("start and step must have the same positive dimension")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in (*start, *step)):
        raise ValueError("relative coordinates and steps must be integers")

    half_width = contact_half_width_1d(radius_sum, collapse_factor)
    lower = 0
    upper: int | None = None
    all_stationary = True

    for coordinate, velocity in zip(start, step, strict=True):
        if velocity == 0:
            if abs(coordinate) > half_width:
                return None
            continue
        all_stationary = False
        window = _coordinate_tick_window(coordinate, velocity, half_width)
        if window is None:
            return None
        coordinate_lower, coordinate_upper = window
        lower = max(lower, coordinate_lower)
        upper = coordinate_upper if upper is None else min(upper, coordinate_upper)
        if upper < lower:
            return None

    if all_stationary:
        return ContactTickWindow(first_tick=0, last_tick=None)
    if upper is None or upper < 0:
        return None
    lower = max(0, lower)
    if lower > upper:
        return None
    return ContactTickWindow(first_tick=lower, last_tick=upper)


def first_static_contact_tick(
    start: Sequence[int],
    step: Sequence[int],
    radius_sum: int,
    collapse_factor: int,
) -> int | None:
    """Return the first non-negative sampled contact tick, if one exists."""
    window = static_contact_tick_window(start, step, radius_sum, collapse_factor)
    return None if window is None else window.first_tick
