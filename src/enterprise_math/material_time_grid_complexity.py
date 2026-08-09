"""Exact time-grid denominator cost for momentum-target material endpoints.

A material branch can be exact in work and momentum yet still require rational
saved-tick durations.  For an exact loading turn from deformation coordinate
``x_0`` to ``x_k`` with inward momentum target ``P_k>0`` and zero momentum at the
turn, midpoint kinematics requires

    tau_k = 2*m*(x_k-x_0) / P_k.

For a returning branch starting from rest at depth k and ending at zero
deformation with outward momentum target ``Q_k>0``, the same formula holds with
``Q_k``.

After reducing each duration, one base time grid ``1/T`` can represent every
listed endpoint duration exactly iff T is divisible by every reduced denominator.
The minimal such denominator is therefore their least common multiple.

A positive deformation with zero target momentum has no finite positive duration
under this rest-to-rest midpoint endpoint language and is reported explicitly
rather than assigned an infinite or fabricated time.

For the square-slope family ``P_k=b*k`` on a unit grid, every nonzero loading
turn has the same duration ``2*m/b``.  With unit mass the entire branch therefore
needs only the single denominator ``b/gcd(b,2)`` independent of depth.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, lcm

from .material_edge_time_compatibility import ExactDuration


def _positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _targets(values: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    targets = tuple(values)
    if not targets or targets[0] != 0:
        raise ValueError("momentum targets must be nonempty and start at zero")
    for value in targets:
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("momentum targets must be non-negative integers")
    return targets


def _grid(values: tuple[int, ...] | list[int], length: int) -> tuple[int, ...]:
    grid = tuple(values)
    if len(grid) != length:
        raise ValueError("deformation grid must match target length")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in grid):
        raise ValueError("deformation coordinates must be integers")
    if any(right <= left for left, right in zip(grid, grid[1:])):
        raise ValueError("deformation grid must be strictly increasing")
    return grid


def _duration(numerator: int, denominator: int) -> ExactDuration:
    common = gcd(numerator, denominator)
    return ExactDuration(numerator // common, denominator // common)


@dataclass(frozen=True, order=True)
class DepthTimeRequirement:
    depth: int
    deformation_span: int
    momentum_target: int
    exact_duration: ExactDuration | None
    finite_dynamic_endpoint: bool


@dataclass(frozen=True)
class MaterialTimeGridComplexity:
    requirements: tuple[DepthTimeRequirement, ...]
    finite_depths: tuple[int, ...]
    no_finite_duration_depths: tuple[int, ...]
    minimal_time_grid_denominator: int
    distinct_exact_durations: tuple[ExactDuration, ...]


def material_time_grid_complexity(
    momentum_targets: tuple[int, ...] | list[int],
    deformation_counts: tuple[int, ...] | list[int] | None = None,
    mass_count: int = 1,
) -> MaterialTimeGridComplexity:
    """Return exact rest/turn endpoint duration requirements for one target branch."""
    targets = _targets(momentum_targets)
    _positive("mass_count", mass_count)
    grid = _grid(
        tuple(range(len(targets))) if deformation_counts is None else deformation_counts,
        len(targets),
    )
    origin = grid[0]
    reports: list[DepthTimeRequirement] = []
    denominators: list[int] = []
    finite: list[int] = []
    missing: list[int] = []
    durations: set[ExactDuration] = set()
    for depth in range(1, len(targets)):
        span = grid[depth] - origin
        target = targets[depth]
        if target == 0:
            reports.append(
                DepthTimeRequirement(depth, span, target, None, False)
            )
            missing.append(depth)
            continue
        duration = _duration(2 * mass_count * span, target)
        reports.append(
            DepthTimeRequirement(depth, span, target, duration, True)
        )
        finite.append(depth)
        denominators.append(duration.denominator)
        durations.add(duration)
    denominator = 1
    for value in denominators:
        denominator = lcm(denominator, value)
    return MaterialTimeGridComplexity(
        requirements=tuple(reports),
        finite_depths=tuple(finite),
        no_finite_duration_depths=tuple(missing),
        minimal_time_grid_denominator=denominator,
        distinct_exact_durations=tuple(sorted(durations)),
    )


def square_slope_time_grid_denominator(
    momentum_root: int,
    mass_count: int = 1,
) -> int:
    """Minimal denominator for P_k=root*k on a unit grid."""
    _positive("momentum_root", momentum_root)
    _positive("mass_count", mass_count)
    # tau = 2*m/root for every positive depth.
    return momentum_root // gcd(2 * mass_count, momentum_root)
