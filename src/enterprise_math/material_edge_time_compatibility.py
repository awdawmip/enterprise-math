"""Factor finite endpoint dynamics into work closure and exact time compatibility.

An energy-consistent endpoint can fail a fixed-time world for two independent
reasons.  First the branch work may not leave a square momentum state.  Second,
even when the endpoint momentum is exact, midpoint kinematics may require a
rational duration different from the declared tick.

This unit-scale E001 comparator uses integer material deformation coordinates,
integer oriented momentum and integer mass count.  For loading ``i<j``:

    p_1^2 = p_0^2 - W2_L(i,j).

When the right side is a non-negative perfect square r^2, both ``p_1=+r`` and
``p_1=-r`` are retained when their midpoint average still points toward the
represented deeper endpoint.  The exact required duration is

    tau = 2*m*(x_j-x_i)/(p_0+p_1).

For returning ``j<i`` the material releases work:

    p_1^2 = p_0^2 + W2_R(j,i),

and the outward solution uses the positive square root.  Again midpoint
kinematics determines an exact rational duration.

Thus endpoint dynamics factor as

    constitutive work endpoint
      -> momentum state closure
      -> time-grid compatibility.

A missing unit-time endpoint need not mean material underresolution.  It may be a
perfectly represented constitutive/momentum state whose natural duration lies on
a different finite time grid.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, isqrt

from .material_edge_work_relation import branch_chord_work_between_depths_numerator2
from .material_force_work import FiniteForceLaw
from .material_hysteresis import LOADING, RETURNING

INWARD_AFTER = "INWARD_AFTER"
TURN_AT_ENDPOINT = "TURN_AT_ENDPOINT"
OUTWARD_AFTER = "OUTWARD_AFTER"


def _nonnegative(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


@dataclass(frozen=True, order=True)
class ExactDuration:
    numerator: int
    denominator: int

    def __post_init__(self) -> None:
        _positive("duration numerator", self.numerator)
        _positive("duration denominator", self.denominator)
        if gcd(self.numerator, self.denominator) != 1:
            raise ValueError("duration fraction must be reduced")


def _duration(numerator: int, denominator: int) -> ExactDuration:
    if numerator <= 0 or denominator <= 0:
        raise ValueError("duration numerator/denominator must be positive")
    common = gcd(numerator, denominator)
    return ExactDuration(numerator // common, denominator // common)


def _perfect_square_root(value: int) -> int | None:
    if value < 0:
        return None
    root = isqrt(value)
    return root if root * root == value else None


@dataclass(frozen=True, order=True)
class EndpointTimeCandidate:
    start_depth: int
    end_depth: int
    branch: str
    deformation_displacement: int
    momentum_before: int
    momentum_after: int
    branch_work_numerator2: int
    required_duration: ExactDuration
    motion_phase_after: str

    @property
    def momentum_closed(self) -> bool:
        return True


def loading_endpoint_time_candidates(
    law: FiniteForceLaw,
    start_depth: int,
    inward_momentum: int,
    mass_count: int = 1,
) -> tuple[EndpointTimeCandidate, ...]:
    """Return all exact loading endpoint/time pairs supported by integer momentum."""
    _nonnegative("start_depth", start_depth)
    _nonnegative("inward_momentum", inward_momentum)
    _positive("mass_count", mass_count)
    if start_depth >= len(law.profile.loading):
        raise ValueError("start_depth lies outside force law")
    grid = law.deformation_counts
    result: list[EndpointTimeCandidate] = []
    for end_depth in range(start_depth + 1, len(law.profile.loading)):
        dx = grid[end_depth] - grid[start_depth]
        work2 = branch_chord_work_between_depths_numerator2(
            law, start_depth, end_depth, LOADING
        )
        root = _perfect_square_root(inward_momentum * inward_momentum - work2)
        if root is None:
            continue
        signed_roots = (0,) if root == 0 else (root, -root)
        for after in signed_roots:
            denominator = inward_momentum + after
            if denominator <= 0:
                continue
            duration = _duration(2 * mass_count * dx, denominator)
            phase = (
                INWARD_AFTER if after > 0 else OUTWARD_AFTER if after < 0 else TURN_AT_ENDPOINT
            )
            result.append(
                EndpointTimeCandidate(
                    start_depth=start_depth,
                    end_depth=end_depth,
                    branch=LOADING,
                    deformation_displacement=dx,
                    momentum_before=inward_momentum,
                    momentum_after=after,
                    branch_work_numerator2=work2,
                    required_duration=duration,
                    motion_phase_after=phase,
                )
            )
    return tuple(sorted(result))


def returning_endpoint_time_candidates(
    law: FiniteForceLaw,
    start_depth: int,
    outward_momentum: int,
    mass_count: int = 1,
) -> tuple[EndpointTimeCandidate, ...]:
    """Return exact returning endpoint/time pairs supported by integer momentum."""
    _nonnegative("start_depth", start_depth)
    _nonnegative("outward_momentum", outward_momentum)
    _positive("mass_count", mass_count)
    if start_depth >= len(law.profile.returning):
        raise ValueError("start_depth lies outside force law")
    grid = law.deformation_counts
    result: list[EndpointTimeCandidate] = []
    for end_depth in range(start_depth - 1, -1, -1):
        dx = grid[start_depth] - grid[end_depth]
        work2 = branch_chord_work_between_depths_numerator2(
            law, end_depth, start_depth, RETURNING
        )
        root = _perfect_square_root(outward_momentum * outward_momentum + work2)
        if root is None:
            continue
        denominator = outward_momentum + root
        if denominator <= 0:
            continue
        result.append(
            EndpointTimeCandidate(
                start_depth=start_depth,
                end_depth=end_depth,
                branch=RETURNING,
                deformation_displacement=dx,
                momentum_before=outward_momentum,
                momentum_after=root,
                branch_work_numerator2=work2,
                required_duration=_duration(2 * mass_count * dx, denominator),
                motion_phase_after=OUTWARD_AFTER if root > 0 else TURN_AT_ENDPOINT,
            )
        )
    return tuple(sorted(result))


def candidates_at_declared_duration(
    candidates: tuple[EndpointTimeCandidate, ...] | list[EndpointTimeCandidate],
    duration_numerator: int,
    duration_denominator: int = 1,
) -> tuple[EndpointTimeCandidate, ...]:
    """Filter exact endpoint candidates to one declared rational time grid."""
    target = _duration(duration_numerator, duration_denominator)
    return tuple(candidate for candidate in candidates if candidate.required_duration == target)
