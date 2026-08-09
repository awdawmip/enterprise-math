"""E001.8 exact sampled-trajectory spatial contact-extinction threshold.

For a constant relative lattice trajectory

    q(n) = q0 + n*v,  n in N,

define its minimum sampled Chebyshev center separation

    D_* = min_n ||q(n)||_infinity.

For E001 square supports with radius sum ``R``, the minimum primitive sampled
clearance is

    g_* = max(0, D_* - R).

Under the active macro-collapse contact law, the trajectory has at least one
sampled macro-contact tick at spatial factor ``d`` exactly when ``g_* < d``.
Thus a positive ``g_*`` has finest still-contact factor ``g_*+1`` and first
fully resolved sampled-noncontact factor ``g_*``.  If ``g_*=0``, sampled
primitive contact persists at terminal factor 1.

``D_*`` is computed without scanning time or spatial factors: the integer tick-
window solver is monotone in the allowed half-width, so binary search finds the
smallest half-width with a nonempty sampled-contact tick window.

This threshold concerns sampled static supports only.  Primitive transition
witnesses can remain active after sampled-static contact has extinguished.
"""

from __future__ import annotations

from dataclasses import dataclass
from collections.abc import Sequence

from .collision_tick_window import static_contact_tick_window


@dataclass(frozen=True)
class SampledTrajectoryContactThreshold:
    """Exact spatial-collapse threshold of one constant relative lattice path."""

    start: tuple[int, ...]
    step: tuple[int, ...]
    radius_sum: int
    minimum_center_separation: int
    minimum_primitive_clearance: int
    finest_sampled_contact_factor: int | None
    first_resolving_factor: int | None


def _validate_vectors(start: Sequence[int], step: Sequence[int]) -> tuple[tuple[int, ...], tuple[int, ...]]:
    if len(start) == 0 or len(start) != len(step):
        raise ValueError("start and step must have the same positive dimension")
    values = (*start, *step)
    if any(isinstance(value, bool) or not isinstance(value, int) for value in values):
        raise ValueError("relative coordinates and steps must be integers")
    return tuple(start), tuple(step)


def minimum_sampled_chebyshev_separation(
    start: Sequence[int],
    step: Sequence[int],
) -> int:
    """Return ``min_{n>=0} ||start+n*step||_infinity`` exactly.

    Feasibility of half-width ``H`` is tested by asking whether an integer tick
    exists with every coordinate in ``[-H,H]``.  The initial state gives the
    finite upper bound ``||start||_infinity``.
    """
    start_tuple, step_tuple = _validate_vectors(start, step)
    upper = max(abs(value) for value in start_tuple)
    lower = 0
    while lower < upper:
        middle = (lower + upper) // 2
        # R=0 and d=H+1 gives contact half-width exactly H.
        window = static_contact_tick_window(
            start_tuple,
            step_tuple,
            radius_sum=0,
            collapse_factor=middle + 1,
        )
        if window is None:
            lower = middle + 1
        else:
            upper = middle
    return lower


def sampled_trajectory_contact_threshold(
    start: Sequence[int],
    step: Sequence[int],
    radius_sum: int,
) -> SampledTrajectoryContactThreshold:
    """Return the exact sampled-static spatial extinction threshold for one path."""
    start_tuple, step_tuple = _validate_vectors(start, step)
    if isinstance(radius_sum, bool) or not isinstance(radius_sum, int) or radius_sum < 0:
        raise ValueError("radius_sum must be a non-negative integer")

    minimum_center = minimum_sampled_chebyshev_separation(start_tuple, step_tuple)
    clearance = max(0, minimum_center - radius_sum)
    if clearance == 0:
        finest_contact = None
        resolving = None
    else:
        finest_contact = clearance + 1
        resolving = clearance
    return SampledTrajectoryContactThreshold(
        start=start_tuple,
        step=step_tuple,
        radius_sum=radius_sum,
        minimum_center_separation=minimum_center,
        minimum_primitive_clearance=clearance,
        finest_sampled_contact_factor=finest_contact,
        first_resolving_factor=resolving,
    )


def sampled_contact_exists_at_factor(
    threshold: SampledTrajectoryContactThreshold,
    collapse_factor: int,
) -> bool:
    """Whether the trajectory has at least one sampled macro-contact tick at ``d``."""
    if (
        isinstance(collapse_factor, bool)
        or not isinstance(collapse_factor, int)
        or collapse_factor <= 0
    ):
        raise ValueError("collapse_factor must be a positive integer")
    return threshold.minimum_primitive_clearance < collapse_factor
