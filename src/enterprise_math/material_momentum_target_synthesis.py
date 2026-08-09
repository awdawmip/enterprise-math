"""Synthesize finite force curves from exact integer momentum targets by depth.

The square-slope family is only the linear special case of a broader exact work
construction.  On a unit deformation grid, suppose the desired exact loading
turning momentum magnitudes are

    P_0,...,P_K,

and desired full-return momentum magnitudes are

    Q_0,...,Q_K.

Under unit physical scales the corresponding doubled work prefixes must be

    S_k=P_k^2,    T_k=Q_k^2.

With zero initial force, the unique branch samples whose symmetric chord work has
those prefixes satisfy

    L_0=0,
    L_k=(P_k^2-P_{k-1}^2)-L_{k-1},

and the same recurrence for R/Q.  A target word is locally realizable as a
non-negative compression force law iff every derived sample is non-negative.
Thus cumulative/passive work targets can still fail local force realizability.

A simple sufficient condition is discrete convexity of the target work prefix:
if the increments ``P_k^2-P_{k-1}^2`` are nondecreasing, induction gives

    0 <= L_k <= P_k^2-P_{k-1}^2.

For a passive loading/return pair one additionally asks ``Q_k<=P_k`` at every
depth; this guarantees returned work never exceeds loading work, but does not by
itself guarantee non-negative local returning force.

This synthesis turns desired exact momentum behavior into a falsifiable finite
constitutive realizability problem instead of treating rebound as a direct
velocity rule.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_force_work import FiniteForceLaw, force_cycle_work_report, uniform_force_law
from .material_response import explicit_material_curve_profile


def _targets(name: str, values: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    targets = tuple(values)
    if not targets:
        raise ValueError(f"{name} targets must be nonempty")
    if targets[0] != 0:
        raise ValueError(f"{name} targets must start at zero")
    for value in targets:
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError(f"{name} targets must be non-negative integers")
    if any(right < left for left, right in zip(targets, targets[1:])):
        raise ValueError(f"{name} targets must be nondecreasing")
    return targets


def squared_target_increments(targets: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    values = _targets("momentum", targets)
    return tuple(
        values[k] * values[k] - values[k - 1] * values[k - 1]
        for k in range(1, len(values))
    )


def squared_work_increments_nondecreasing(targets: tuple[int, ...] | list[int]) -> bool:
    increments = squared_target_increments(targets)
    return all(left <= right for left, right in zip(increments, increments[1:]))


def force_samples_from_momentum_targets(
    targets: tuple[int, ...] | list[int],
) -> tuple[int, ...]:
    values = _targets("momentum", targets)
    forces = [0]
    for depth in range(1, len(values)):
        work_increment = values[depth] ** 2 - values[depth - 1] ** 2
        forces.append(work_increment - forces[-1])
    return tuple(forces)


@dataclass(frozen=True)
class MomentumTargetBranchRealizability:
    targets: tuple[int, ...]
    squared_work_increments: tuple[int, ...]
    force_samples: tuple[int, ...]
    nonnegative_force_realizable: bool
    first_negative_force_depth: int | None
    sufficient_convexity_condition: bool
    force_nondecreasing: bool


def momentum_target_branch_realizability(
    targets: tuple[int, ...] | list[int],
) -> MomentumTargetBranchRealizability:
    values = _targets("momentum", targets)
    increments = squared_target_increments(values)
    forces = force_samples_from_momentum_targets(values)
    first_negative = next((k for k, force in enumerate(forces) if force < 0), None)
    convex = squared_work_increments_nondecreasing(values)
    if convex and first_negative is not None:
        raise AssertionError("nondecreasing squared-work increments failed nonnegative-force sufficiency")
    return MomentumTargetBranchRealizability(
        targets=values,
        squared_work_increments=increments,
        force_samples=forces,
        nonnegative_force_realizable=first_negative is None,
        first_negative_force_depth=first_negative,
        sufficient_convexity_condition=convex,
        force_nondecreasing=all(a <= b for a, b in zip(forces, forces[1:])),
    )


@dataclass(frozen=True)
class MomentumTargetMaterialFamily:
    loading_targets: tuple[int, ...]
    returning_targets: tuple[int, ...]
    loading_realizability: MomentumTargetBranchRealizability
    returning_realizability: MomentumTargetBranchRealizability
    passive_work_targets: bool
    law: FiniteForceLaw


def momentum_target_material_family(
    loading_targets: tuple[int, ...] | list[int],
    returning_targets: tuple[int, ...] | list[int],
    require_passive: bool = True,
) -> MomentumTargetMaterialFamily:
    loading = _targets("loading momentum", loading_targets)
    returning = _targets("returning momentum", returning_targets)
    if len(loading) != len(returning):
        raise ValueError("loading and returning momentum targets must share one depth domain")
    load_report = momentum_target_branch_realizability(loading)
    return_report = momentum_target_branch_realizability(returning)
    if not load_report.nonnegative_force_realizable:
        raise ValueError("loading momentum targets require a negative local force")
    if not return_report.nonnegative_force_realizable:
        raise ValueError("returning momentum targets require a negative local force")
    passive = all(q <= p for p, q in zip(loading, returning))
    if require_passive and not passive:
        raise ValueError("returning momentum target exceeds loading target at some depth")
    amplitude = max(1, *load_report.force_samples, *return_report.force_samples)
    profile = explicit_material_curve_profile(
        load_report.force_samples,
        return_report.force_samples,
        amplitude,
    )
    law = uniform_force_law(profile)
    for depth, target in enumerate(loading):
        cycle = force_cycle_work_report(law, depth)
        if cycle.loading_work_numerator2 != target * target:
            raise AssertionError("synthesized loading force missed target square work")
        if cycle.returned_work_numerator2 != returning[depth] * returning[depth]:
            raise AssertionError("synthesized returning force missed target square work")
    return MomentumTargetMaterialFamily(
        loading_targets=loading,
        returning_targets=returning,
        loading_realizability=load_report,
        returning_realizability=return_report,
        passive_work_targets=passive,
        law=law,
    )
