"""Minimum state-local task precision for rank-one A3 hidden guards.

Fix a parent partition, one current fine-state guard-score vector, and a declared
parent-level branch-effect language. For any partition refinement whose hidden
guard image remains rank one, the child image is q*Z*h for a finite integer
index q. The coarsest partition forcing divisibility by q is the canonical label
residue refinement.

Searching the finitely many canonical moduli up to the label-visibility bound is
therefore complete for minimum relation-rank task precision at the fixed state
and fixed parent-level effect language. The solver returns every minimum-rank
canonical partition (deduplicated), because different moduli can in principle
yield incomparable partitions with the same rank cost.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from dataclasses import dataclass

from .guard_branch_erasure import (
    BranchErasureReport,
    Pattern,
    rank_one_branch_erasure_report,
)
from .guard_image_lattice import (
    GuardFamily,
    guard_kernel_image_rank,
    guard_rank_one_step,
)
from .linear_relation_quotient import Partition
from .rank_one_guard_modulus import (
    rank_one_modulus_refinement,
    rank_one_modulus_visibility_bound,
)


@dataclass(frozen=True)
class RankOneTaskPrecisionCandidate:
    modulus: int
    partition: Partition
    relation_rank_gain: int
    child_hidden_rank: int
    child_step: tuple[int, ...] | None
    erasure_report: BranchErasureReport


@dataclass(frozen=True)
class RankOneTaskPrecisionResult:
    minimum_relation_rank_gain: int
    candidates: tuple[RankOneTaskPrecisionCandidate, ...]
    visibility_bound: int


def _constant_fiber_report(
    base_scores: tuple[int, ...],
    branch_effects: Mapping[Pattern, Hashable],
) -> BranchErasureReport:
    pattern = tuple(score >= 0 for score in base_scores)
    if pattern not in branch_effects:
        raise ValueError("branch_effects must define the current visible pattern")
    effect = branch_effects[pattern]
    try:
        hash(effect)
    except TypeError as error:
        raise ValueError("branch effects must be hashable") from error
    return BranchErasureReport(
        reachable_patterns=(pattern,),
        distinct_effects=(effect,),
        safe_to_erase=True,
    )


def minimum_rank_one_task_precision(
    guards: GuardFamily,
    parent_partition: Partition,
    base_scores: tuple[int, ...],
    branch_effects: Mapping[Pattern, Hashable],
) -> RankOneTaskPrecisionResult:
    """Return the complete minimum-rank safe refinement frontier for one state.

    `branch_effects` is interpreted in a fixed parent-level future language: a
    refined internal computation is safe when all branch patterns reachable in
    the refined child fiber induce the same declared parent-level effect.
    """
    parent_rank = guard_kernel_image_rank(guards, parent_partition)
    if parent_rank != 1:
        raise ValueError("parent guard-image lattice must have rank one")
    if not isinstance(base_scores, tuple) or len(base_scores) != len(guards):
        raise ValueError("base_scores must match the guard count")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for value in base_scores
    ):
        raise ValueError("base_scores entries must be integers")

    visibility_bound = rank_one_modulus_visibility_bound(
        guards, parent_partition
    )
    safe_by_partition: dict[Partition, RankOneTaskPrecisionCandidate] = {}

    for modulus in range(1, visibility_bound + 1):
        partition = rank_one_modulus_refinement(
            guards, parent_partition, modulus
        )
        child_rank = guard_kernel_image_rank(guards, partition)
        if child_rank == 0:
            child_step = None
            report = _constant_fiber_report(base_scores, branch_effects)
        elif child_rank == 1:
            child_step = guard_rank_one_step(guards, partition)
            report = rank_one_branch_erasure_report(
                base_scores, child_step, branch_effects
            )
        else:
            raise AssertionError("refinement of a rank-one hidden image cannot gain rank")

        if not report.safe_to_erase:
            continue
        candidate = RankOneTaskPrecisionCandidate(
            modulus=modulus,
            partition=partition,
            relation_rank_gain=len(partition) - len(parent_partition),
            child_hidden_rank=child_rank,
            child_step=child_step,
            erasure_report=report,
        )
        existing = safe_by_partition.get(partition)
        if existing is None or candidate.modulus < existing.modulus:
            safe_by_partition[partition] = candidate

    if not safe_by_partition:
        raise AssertionError("guard-visible label refinement must always make the fixed-state branch deterministic")

    minimum_gain = min(
        candidate.relation_rank_gain
        for candidate in safe_by_partition.values()
    )
    frontier = tuple(
        candidate
        for candidate in safe_by_partition.values()
        if candidate.relation_rank_gain == minimum_gain
    )
    return RankOneTaskPrecisionResult(
        minimum_relation_rank_gain=minimum_gain,
        candidates=frontier,
        visibility_bound=visibility_bound,
    )
