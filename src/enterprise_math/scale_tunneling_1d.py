"""E001.10 arbitrary finite jump through a 1D wall under scale-collapse contact.

This module follows the active world-engine decision: a long finite transition
is not automatically decomposed into hidden intermediate states.  If the engine
stores only the proposed pre/post states and has not declared an additional
transition incidence, a jump may legally move from one separated side of a wall
to the other.

All geometry is integer and interval based.

A wall occupies the closed primitive-cell interval ``[wall_lo, wall_hi]`` with
cell thickness

    T = wall_hi - wall_lo + 1.

A moving body of integer radius ``r`` occupies ``[x-r,x+r]`` and has primitive
cell diameter

    D = 2*r + 1.

For a left-to-right jump with positive pre/post clearances ``g_pre,g_post>=1``:

    displacement
      = T + D + (g_pre-1) + (g_post-1).

Consequently the minimum center displacement that can jump from one separated
side to the other while retaining one primitive cell of clearance on both ends
is exactly

    s_min = T + D.

For a genuine separated-side jump, let ``g_* = min(g_pre,g_post)``.  Under the
active sampled gap-collapse rule (and with no extra transition incidence),
coarse collision/rebound opportunity exists exactly for ``d>g_*``; refinement
to ``d<=g_*`` permits sampled-state transmission.  This is a world-engine toy
model, not a claim about real quantum tunneling or physical walls.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, order=True)
class Wall1D:
    lo: int
    hi: int

    def __post_init__(self) -> None:
        if any(isinstance(value, bool) or not isinstance(value, int) for value in (self.lo, self.hi)):
            raise ValueError("wall endpoints must be integers")
        if self.lo > self.hi:
            raise ValueError("wall lo must not exceed hi")

    @property
    def thickness_cells(self) -> int:
        return self.hi - self.lo + 1


@dataclass(frozen=True, order=True)
class BodyInterval1D:
    center: int
    radius: int = 0

    def __post_init__(self) -> None:
        if isinstance(self.center, bool) or not isinstance(self.center, int):
            raise ValueError("body center must be an integer")
        if isinstance(self.radius, bool) or not isinstance(self.radius, int) or self.radius < 0:
            raise ValueError("body radius must be a non-negative integer")

    @property
    def lo(self) -> int:
        return self.center - self.radius

    @property
    def hi(self) -> int:
        return self.center + self.radius

    @property
    def diameter_cells(self) -> int:
        return 2 * self.radius + 1


@dataclass(frozen=True)
class WallJumpProfile1D:
    """Exact sampled-state geometry of one arbitrary integer body jump."""

    wall: Wall1D
    radius: int
    start_center: int
    end_center: int
    displacement: int
    direction: str | None
    crosses_between_separated_sides: bool
    start_clearance: int
    end_clearance: int
    minimum_sampled_clearance: int
    effective_minimum_crossing_displacement: int
    finest_coarse_collision_factor: int | None
    first_transmission_factor: int | None


def interval_wall_clearance(body: BodyInterval1D, wall: Wall1D) -> int:
    """Primitive non-negative interval clearance; zero means touch/overlap."""
    if body.hi < wall.lo:
        return wall.lo - body.hi
    if wall.hi < body.lo:
        return body.lo - wall.hi
    return 0


def minimum_positive_clearance_crossing_displacement(
    wall: Wall1D,
    radius: int,
) -> int:
    """Return exact ``T + D`` minimum displacement for one-cell gaps at both ends."""
    body = BodyInterval1D(0, radius)
    return wall.thickness_cells + body.diameter_cells


def wall_jump_profile(
    wall: Wall1D,
    start_center: int,
    end_center: int,
    radius: int = 0,
) -> WallJumpProfile1D:
    """Classify one arbitrary sampled jump relative to a finite wall interval."""
    start = BodyInterval1D(start_center, radius)
    end = BodyInterval1D(end_center, radius)
    start_gap = interval_wall_clearance(start, wall)
    end_gap = interval_wall_clearance(end, wall)

    left_to_right = start.hi < wall.lo and end.lo > wall.hi
    right_to_left = start.lo > wall.hi and end.hi < wall.lo
    crosses = left_to_right or right_to_left
    direction = "LEFT_TO_RIGHT" if left_to_right else "RIGHT_TO_LEFT" if right_to_left else None
    displacement = abs(end_center - start_center)
    minimum_crossing = minimum_positive_clearance_crossing_displacement(wall, radius)

    if crosses:
        if start_gap <= 0 or end_gap <= 0:
            raise AssertionError("separated-side crossing lost positive endpoint clearance")
        minimum_gap = min(start_gap, end_gap)
        expected_displacement = (
            minimum_crossing + (start_gap - 1) + (end_gap - 1)
        )
        if displacement != expected_displacement:
            raise AssertionError("wall jump displacement disagrees with exact interval identity")
        finest_collision = minimum_gap + 1
        first_transmission = minimum_gap
    else:
        minimum_gap = min(start_gap, end_gap)
        finest_collision = None
        first_transmission = None

    return WallJumpProfile1D(
        wall=wall,
        radius=radius,
        start_center=start_center,
        end_center=end_center,
        displacement=displacement,
        direction=direction,
        crosses_between_separated_sides=crosses,
        start_clearance=start_gap,
        end_clearance=end_gap,
        minimum_sampled_clearance=minimum_gap,
        effective_minimum_crossing_displacement=minimum_crossing,
        finest_coarse_collision_factor=finest_collision,
        first_transmission_factor=first_transmission,
    )


def sampled_wall_collision_at_factor(
    profile: WallJumpProfile1D,
    collapse_factor: int,
) -> bool:
    """Sampled-state collapse collision for a separated-side jump at spatial factor ``d``."""
    if (
        isinstance(collapse_factor, bool)
        or not isinstance(collapse_factor, int)
        or collapse_factor <= 0
    ):
        raise ValueError("collapse_factor must be a positive integer")
    if not profile.crosses_between_separated_sides:
        raise ValueError("sampled tunneling threshold requires a separated-side crossing")
    return profile.minimum_sampled_clearance < collapse_factor


def sampled_wall_transmission_at_factor(
    profile: WallJumpProfile1D,
    collapse_factor: int,
) -> bool:
    """Whether this sampled jump is contact-free at both endpoints at factor ``d``."""
    return not sampled_wall_collision_at_factor(profile, collapse_factor)
