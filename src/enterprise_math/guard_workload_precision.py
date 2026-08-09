"""Common-safe task precision for finite A3 coarse-state workloads.

State-local minimum precision need not compose across states: different coarse
fibers can require different hidden subgroups to erase branch ambiguity. This
module finds one common partition refinement that is exact for every declared
base-score state under one fixed parent-level branch-effect language.

Rank-one workloads enumerate the complete finite family of canonical modulus
refinements. Rank-two workloads enumerate the complete finite family of
partition-realizable hidden subgroups. Completeness follows from the same
canonical replacement theorems used by the state-local solvers.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from dataclasses import dataclass

from .guard_branch_erasure import (
    BranchErasureReport,
    Pattern,
    rank_one_branch_erasure_report,
    rank_two_branch_erasure_report,
)
from .guard_image_lattice import (
    GuardFamily,
    guard_kernel_image_generators,
    guard_kernel_image_rank,
    guard_rank_one_step,
)
from .linear_relation_quotient import Partition
from .rank_one_guard_modulus import (
    rank_one_modulus_refinement,
    rank_one_modulus_visibility_bound,
)
from .rank_two_guard_refinement import (
    SubgroupBasis,
    rank_two_canonical_sublattice_refinement,
    rank_two_realizable_image_subgroups,
)


@dataclass(frozen=True)
class WorkloadPrecisionCandidate:
    partition: Partition
    relation_rank_gain: int
    child_hidden_rank: int
    workload_reports: tuple[BranchErasureReport, ...]
    modulus: int | None = None
    subgroup: SubgroupBasis | None = None


@dataclass(frozen=True)
class WorkloadPrecisionResult:
    minimum_relation_rank_gain: int
    candidates: tuple[WorkloadPrecisionCandidate, ...]
    workload_size: int
    search_state_count: int


def _require_workload(
    base_score_workload: tuple[tuple[int, ...], ...], guard_count: int
) -> None:
    if not isinstance(base_score_workload, tuple) or not base_score_workload:
        raise ValueError("base_score_workload must be a non-empty tuple")
    for scores in base_score_workload:
        if not isinstance(scores, tuple) or len(scores) != guard_count:
            raise ValueError("every workload score vector must match the guard count")
        if any(isinstance(value, bool) or not isinstance(value, int) for value in scores):
            raise ValueError("workload score entries must be integers")


def _visible_report(
    scores: tuple[int, ...], branch_effects: Mapping[Pattern, Hashable]
) -> BranchErasureReport:
    pattern = tuple(score >= 0 for score in scores)
    if pattern not in branch_effects:
        raise ValueError("branch_effects must define every workload-visible pattern")
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


def minimum_rank_one_workload_precision(
    guards: GuardFamily,
    parent_partition: Partition,
    base_score_workload: tuple[tuple[int, ...], ...],
    branch_effects: Mapping[Pattern, Hashable],
) -> WorkloadPrecisionResult:
    """Complete minimum-rank common refinement for a finite rank-one workload."""
    if guard_kernel_image_rank(guards, parent_partition) != 1:
        raise ValueError("parent guard-image lattice must have rank one")
    _require_workload(base_score_workload, len(guards))
    visibility_bound = rank_one_modulus_visibility_bound(guards, parent_partition)

    safe_by_partition: dict[Partition, WorkloadPrecisionCandidate] = {}
    for modulus in range(1, visibility_bound + 1):
        partition = rank_one_modulus_refinement(guards, parent_partition, modulus)
        child_rank = guard_kernel_image_rank(guards, partition)
        reports = []
        for scores in base_score_workload:
            if child_rank == 0:
                report = _visible_report(scores, branch_effects)
            elif child_rank == 1:
                report = rank_one_branch_erasure_report(
                    scores,
                    guard_rank_one_step(guards, partition),
                    branch_effects,
                )
            else:
                raise AssertionError("rank-one parent refinement cannot gain hidden rank")
            reports.append(report)
        if not all(report.safe_to_erase for report in reports):
            continue
        candidate = WorkloadPrecisionCandidate(
            partition=partition,
            relation_rank_gain=len(partition) - len(parent_partition),
            child_hidden_rank=child_rank,
            workload_reports=tuple(reports),
            modulus=modulus,
        )
        existing = safe_by_partition.get(partition)
        if existing is None or modulus < (existing.modulus or modulus + 1):
            safe_by_partition[partition] = candidate

    if not safe_by_partition:
        raise AssertionError("guard-visible refinement must be safe for every finite workload")
    minimum_gain = min(candidate.relation_rank_gain for candidate in safe_by_partition.values())
    frontier = tuple(
        candidate
        for candidate in safe_by_partition.values()
        if candidate.relation_rank_gain == minimum_gain
    )
    return WorkloadPrecisionResult(
        minimum_relation_rank_gain=minimum_gain,
        candidates=frontier,
        workload_size=len(base_score_workload),
        search_state_count=visibility_bound,
    )


def minimum_rank_two_workload_precision(
    guards: GuardFamily,
    parent_partition: Partition,
    base_score_workload: tuple[tuple[int, ...], ...],
    branch_effects: Mapping[Pattern, Hashable],
) -> WorkloadPrecisionResult:
    """Complete minimum-rank common refinement for a finite rank-two workload."""
    if guard_kernel_image_rank(guards, parent_partition) != 2:
        raise ValueError("parent guard-image lattice must have rank two")
    _require_workload(base_score_workload, len(guards))
    subgroups = rank_two_realizable_image_subgroups(guards, parent_partition)
    safe_candidates = []

    for subgroup in subgroups:
        partition = rank_two_canonical_sublattice_refinement(
            guards, parent_partition, subgroup
        )
        child_rank = guard_kernel_image_rank(guards, partition)
        reports = []
        for scores in base_score_workload:
            if child_rank == 0:
                report = _visible_report(scores, branch_effects)
            elif child_rank == 1:
                report = rank_one_branch_erasure_report(
                    scores,
                    guard_rank_one_step(guards, partition),
                    branch_effects,
                )
            elif child_rank == 2:
                report = rank_two_branch_erasure_report(
                    scores,
                    guard_kernel_image_generators(guards, partition),
                    branch_effects,
                )
            else:
                raise AssertionError("rank-two parent refinement cannot gain hidden rank")
            reports.append(report)
        if all(report.safe_to_erase for report in reports):
            safe_candidates.append(
                WorkloadPrecisionCandidate(
                    partition=partition,
                    relation_rank_gain=len(partition) - len(parent_partition),
                    child_hidden_rank=child_rank,
                    workload_reports=tuple(reports),
                    subgroup=subgroup,
                )
            )

    if not safe_candidates:
        raise AssertionError("zero hidden subgroup must be safe for every finite workload")
    minimum_gain = min(candidate.relation_rank_gain for candidate in safe_candidates)
    frontier = tuple(
        candidate
        for candidate in safe_candidates
        if candidate.relation_rank_gain == minimum_gain
    )
    return WorkloadPrecisionResult(
        minimum_relation_rank_gain=minimum_gain,
        candidates=frontier,
        workload_size=len(base_score_workload),
        search_state_count=len(subgroups),
    )
