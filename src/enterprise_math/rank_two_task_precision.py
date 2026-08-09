"""Complete state-local minimum task precision for rank-two A3 hidden guards.

Every partition refinement of a rank-two parent guard image has an exact child
image subgroup M <= Z^2 in parent hidden coordinates. That subgroup is generated
by a subset of the finite hidden-label differences. For each realizable M, the
canonical coset refinement is the coarsest partition with exact child image M.

Therefore minimum state-local task precision for a fixed parent-level branch
effect language can be found by enumerating distinct realizable subgroups rather
than all set partitions.
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
from .rank_two_guard_refinement import (
    SubgroupBasis,
    rank_two_canonical_sublattice_refinement,
    rank_two_realizable_image_subgroups,
)


@dataclass(frozen=True)
class RankTwoTaskPrecisionCandidate:
    subgroup: SubgroupBasis
    partition: Partition
    relation_rank_gain: int
    child_hidden_rank: int
    erasure_report: BranchErasureReport


@dataclass(frozen=True)
class RankTwoTaskPrecisionResult:
    minimum_relation_rank_gain: int
    candidates: tuple[RankTwoTaskPrecisionCandidate, ...]
    realizable_subgroup_count: int


def _constant_report(
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


def minimum_rank_two_task_precision(
    guards: GuardFamily,
    parent_partition: Partition,
    base_scores: tuple[int, ...],
    branch_effects: Mapping[Pattern, Hashable],
) -> RankTwoTaskPrecisionResult:
    """Return the complete minimum-rank safe refinement frontier for rank two.

    The declared branch effects remain in one fixed parent-level future
    language. Refinement is used only as internal precision to make that effect
    exact for the current state/fiber.
    """
    if guard_kernel_image_rank(guards, parent_partition) != 2:
        raise ValueError("parent guard-image lattice must have rank two")
    if not isinstance(base_scores, tuple) or len(base_scores) != len(guards):
        raise ValueError("base_scores must match the guard count")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for value in base_scores
    ):
        raise ValueError("base_scores entries must be integers")

    subgroups = rank_two_realizable_image_subgroups(guards, parent_partition)
    safe_candidates = []

    for subgroup in subgroups:
        partition = rank_two_canonical_sublattice_refinement(
            guards, parent_partition, subgroup
        )
        child_rank = guard_kernel_image_rank(guards, partition)
        if child_rank != len(subgroup):
            raise AssertionError("canonical realizable subgroup refinement must have exact target rank")

        if child_rank == 0:
            report = _constant_report(base_scores, branch_effects)
        elif child_rank == 1:
            step = guard_rank_one_step(guards, partition)
            report = rank_one_branch_erasure_report(
                base_scores, step, branch_effects
            )
        elif child_rank == 2:
            generators = guard_kernel_image_generators(guards, partition)
            report = rank_two_branch_erasure_report(
                base_scores, generators, branch_effects
            )
        else:
            raise AssertionError("rank-two parent refinement cannot have hidden rank above two")

        if report.safe_to_erase:
            safe_candidates.append(
                RankTwoTaskPrecisionCandidate(
                    subgroup=subgroup,
                    partition=partition,
                    relation_rank_gain=len(partition) - len(parent_partition),
                    child_hidden_rank=child_rank,
                    erasure_report=report,
                )
            )

    if not safe_candidates:
        raise AssertionError("zero hidden subgroup must make the fixed-state branch deterministic")
    minimum_gain = min(candidate.relation_rank_gain for candidate in safe_candidates)
    frontier = tuple(
        candidate
        for candidate in safe_candidates
        if candidate.relation_rank_gain == minimum_gain
    )
    return RankTwoTaskPrecisionResult(
        minimum_relation_rank_gain=minimum_gain,
        candidates=frontier,
        realizable_subgroup_count=len(subgroups),
    )
