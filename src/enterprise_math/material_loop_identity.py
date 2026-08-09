"""Exact identity between the standard E001 hysteresis loop area and branch gap.

For the unit-step single-peak schedule

    0,1,...,n-1,n,n-1,...,1,0,

suppose loading/returning agree at deformation 0.  The realized material-state
polygon visits loading states at 0..n and returning states at n-1..0.  Its signed
shoelace twice-area is exactly

    A2 = 2 * sum_{k=1}^{n-1} (R_k - C_k).

The peak return value R_n is not visited by this actual history, and the depth-0
branch gap cancels in the closing vertical edge.  Thus, for this minimal cycle,
the realized repeated-depth branch-gap sum and the integer loop area carry the
same information.  More general schedules (holds, skipped depths, multiple
peaks) need not reduce to this identity.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_hysteresis import trace_deformation_schedule
from .material_loop_geometry import material_loop_geometry
from .material_response import MaterialCurveProfile


@dataclass(frozen=True)
class StandardLoopIdentity:
    """Exact comparison of shoelace twice-area and repeated-depth branch gap."""

    peak_depth: int
    schedule: tuple[int, ...]
    signed_twice_area: int
    repeated_depth_signed_gap: int
    reconstructed_twice_area: int


def standard_single_peak_schedule(peak_depth: int) -> tuple[int, ...]:
    if (
        isinstance(peak_depth, bool)
        or not isinstance(peak_depth, int)
        or peak_depth < 0
    ):
        raise ValueError("peak_depth must be a non-negative integer")
    if peak_depth == 0:
        return (0,)
    return tuple(range(peak_depth + 1)) + tuple(
        range(peak_depth - 1, -1, -1)
    )


def standard_loop_identity(
    profile: MaterialCurveProfile,
    peak_depth: int,
) -> StandardLoopIdentity:
    """Verify the exact signed-area / repeated-gap identity for one peak depth."""
    if peak_depth >= len(profile.loading):
        raise ValueError("peak_depth is not represented by material profile")
    if profile.loading[0] != profile.returning[0]:
        raise ValueError("standard closed-loop identity requires matching depth-0 branches")
    schedule = standard_single_peak_schedule(peak_depth)
    states = trace_deformation_schedule(profile, schedule)
    geometry = material_loop_geometry(states)
    if not geometry.closed or geometry.signed_twice_area is None:
        raise AssertionError("standard single-peak schedule failed to close")

    repeated_gap = sum(
        profile.returning[depth] - profile.loading[depth]
        for depth in range(1, peak_depth)
    )
    reconstructed = 2 * repeated_gap
    if geometry.signed_twice_area != reconstructed:
        raise AssertionError("standard loop area disagrees with repeated-depth gap identity")
    return StandardLoopIdentity(
        peak_depth=peak_depth,
        schedule=schedule,
        signed_twice_area=geometry.signed_twice_area,
        repeated_depth_signed_gap=repeated_gap,
        reconstructed_twice_area=reconstructed,
    )
