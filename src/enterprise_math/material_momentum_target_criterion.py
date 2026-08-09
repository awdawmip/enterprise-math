"""Exact local-force realizability criterion for integer momentum target words.

Let a nondecreasing integer momentum target word start at zero:

    P_0=0, P_1,...,P_K.

The exact doubled work prefix required at depth k is ``S_k=P_k^2``.  Put

    Delta_k=S_k-S_{k-1}.

On a unit deformation grid with F_0=0, symmetric chord work forces the unique
local force recurrence

    F_k = Delta_k - F_{k-1}.

Therefore

    F_k = Delta_k-Delta_{k-1}+...+(-1)^(k-1) Delta_1.

A target word is realizable by a non-negative local compression-force law iff all
of these alternating prefix quantities are non-negative.  This is necessary and
sufficient, not merely a convenient sufficient condition.

The synthesized force is itself nondecreasing exactly when every local margin

    Delta_k - 2*F_{k-1}

is non-negative.  Thus target-work convexity and force hardening are related but
not identical finite constraints.

For a loading/return pair, cumulative work passivity ``Q_k<=P_k`` is independent
of local realizability: both loading and returning target words must separately
pass the alternating-force criterion.  Pointwise local return force may exceed
local loading force at some depths while cumulative returned work remains below
loading work.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_momentum_target_synthesis import (
    force_samples_from_momentum_targets,
    squared_target_increments,
)


def _targets(values: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    targets = tuple(values)
    if not targets or targets[0] != 0:
        raise ValueError("momentum targets must be nonempty and start at zero")
    for value in targets:
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("momentum targets must be non-negative integers")
    if any(right < left for left, right in zip(targets, targets[1:])):
        raise ValueError("momentum targets must be nondecreasing")
    return targets


def alternating_force_from_increments(increments: tuple[int, ...] | list[int]) -> tuple[int, ...]:
    """Return F_0,...,F_K from work increments Delta_1,...,Delta_K."""
    values = tuple(increments)
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError("work increments must be non-negative integers")
    forces = [0]
    for delta in values:
        forces.append(delta - forces[-1])
    return tuple(forces)


@dataclass(frozen=True)
class MomentumTargetExactCriterion:
    targets: tuple[int, ...]
    squared_work_increments: tuple[int, ...]
    alternating_force_samples: tuple[int, ...]
    recurrence_force_samples: tuple[int, ...]
    nonnegative_force_realizable: bool
    first_negative_force_depth: int | None
    hardening_margins: tuple[int, ...]
    force_nondecreasing: bool


def momentum_target_exact_criterion(
    targets: tuple[int, ...] | list[int],
) -> MomentumTargetExactCriterion:
    values = _targets(targets)
    increments = squared_target_increments(values)
    alternating = alternating_force_from_increments(increments)
    recurrence = force_samples_from_momentum_targets(values)
    if alternating != recurrence:
        raise AssertionError("alternating force criterion disagrees with synthesis recurrence")
    negative = next((k for k, force in enumerate(alternating) if force < 0), None)
    margins = tuple(
        increments[k - 1] - 2 * alternating[k - 1]
        for k in range(1, len(alternating))
    )
    nondecreasing = all(margin >= 0 for margin in margins)
    if nondecreasing != all(a <= b for a, b in zip(alternating, alternating[1:])):
        raise AssertionError("hardening margin criterion disagrees with force samples")
    return MomentumTargetExactCriterion(
        targets=values,
        squared_work_increments=increments,
        alternating_force_samples=alternating,
        recurrence_force_samples=recurrence,
        nonnegative_force_realizable=negative is None,
        first_negative_force_depth=negative,
        hardening_margins=margins,
        force_nondecreasing=nondecreasing,
    )


@dataclass(frozen=True)
class MomentumTargetPairCriterion:
    loading: MomentumTargetExactCriterion
    returning: MomentumTargetExactCriterion
    cumulative_work_passive: bool
    locally_realizable: bool
    pointwise_return_force_below_loading: bool | None


def momentum_target_pair_criterion(
    loading_targets: tuple[int, ...] | list[int],
    returning_targets: tuple[int, ...] | list[int],
) -> MomentumTargetPairCriterion:
    loading = momentum_target_exact_criterion(loading_targets)
    returning = momentum_target_exact_criterion(returning_targets)
    if len(loading.targets) != len(returning.targets):
        raise ValueError("loading and returning targets must share one depth domain")
    passive = all(q <= p for p, q in zip(loading.targets, returning.targets))
    locally_realizable = (
        loading.nonnegative_force_realizable and returning.nonnegative_force_realizable
    )
    pointwise = None
    if locally_realizable:
        pointwise = all(
            r <= l
            for l, r in zip(
                loading.alternating_force_samples,
                returning.alternating_force_samples,
            )
        )
    return MomentumTargetPairCriterion(
        loading=loading,
        returning=returning,
        cumulative_work_passive=passive,
        locally_realizable=locally_realizable,
        pointwise_return_force_below_loading=pointwise,
    )
