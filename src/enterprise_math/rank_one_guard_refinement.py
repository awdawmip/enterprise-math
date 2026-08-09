"""Rank-one hidden-guard refinement as an integer residue/step refinement.

If a partition refinement keeps hidden guard-image rank one, the child image is
a subgroup of the parent rank-one lattice. With canonical steps this has the
form

    L_parent = Z*h,
    L_child  = q*Z*h,

for an integer index q>=1. A child coarse fiber therefore restricts the parent
arithmetic-line parameter to one residue class modulo q. This can remove branch
patterns without making the guard family fully visible.
"""

from __future__ import annotations

from dataclasses import dataclass

from .guard_branch_erasure import BranchErasureReport, Pattern, rank_one_reachable_patterns
from .guard_image_lattice import (
    GuardFamily,
    guard_kernel_image_rank,
    guard_rank_one_step,
)
from .linear_relation_quotient import Partition
from .relation_precision_profile import partition_refines


@dataclass(frozen=True)
class RankOneGuardRefinement:
    parent_step: tuple[int, ...]
    child_step: tuple[int, ...] | None
    image_index: int | None
    child_hidden_rank: int


def rank_one_step_index(
    parent_step: tuple[int, ...], child_step: tuple[int, ...]
) -> int:
    """Return q when Z*child_step is the subgroup q*(Z*parent_step)."""
    if not isinstance(parent_step, tuple) or not isinstance(child_step, tuple):
        raise ValueError("steps must be tuples")
    if not parent_step or len(parent_step) != len(child_step):
        raise ValueError("steps must have the same positive dimension")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for value in parent_step + child_step
    ):
        raise ValueError("step entries must be integers")
    if not any(parent_step) or not any(child_step):
        raise ValueError("steps must be nonzero")

    pivot = next(index for index, value in enumerate(parent_step) if value != 0)
    if child_step[pivot] % parent_step[pivot] != 0:
        raise ValueError("child rank-one lattice is not a subgroup of the parent lattice")
    quotient = child_step[pivot] // parent_step[pivot]
    if quotient <= 0:
        raise ValueError("canonical child step must be a positive multiple of parent step")
    if tuple(quotient * value for value in parent_step) != child_step:
        raise ValueError("child rank-one lattice is not a subgroup of the parent lattice")
    return quotient


def analyze_rank_one_guard_refinement(
    guards: GuardFamily,
    parent_partition: Partition,
    child_partition: Partition,
) -> RankOneGuardRefinement:
    """Analyze how a partition refinement changes a rank-one guard-image lattice."""
    if not partition_refines(child_partition, parent_partition):
        raise ValueError("child_partition must refine parent_partition")
    parent_rank = guard_kernel_image_rank(guards, parent_partition)
    if parent_rank != 1:
        raise ValueError("parent guard-image lattice must have rank one")
    parent_step = guard_rank_one_step(guards, parent_partition)
    child_rank = guard_kernel_image_rank(guards, child_partition)
    if child_rank == 0:
        return RankOneGuardRefinement(
            parent_step=parent_step,
            child_step=None,
            image_index=None,
            child_hidden_rank=0,
        )
    if child_rank != 1:
        raise AssertionError("a subgroup of a rank-one guard image cannot increase rank")
    child_step = guard_rank_one_step(guards, child_partition)
    index = rank_one_step_index(parent_step, child_step)
    return RankOneGuardRefinement(
        parent_step=parent_step,
        child_step=child_step,
        image_index=index,
        child_hidden_rank=1,
    )


def rank_one_residue_reachable_patterns(
    parent_base_scores: tuple[int, ...],
    parent_step: tuple[int, ...],
    modulus: int,
    residue: int,
) -> tuple[Pattern, ...]:
    """Reachable patterns after restricting parent parameter t to one residue mod q."""
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus <= 0:
        raise ValueError("modulus must be a positive integer")
    if isinstance(residue, bool) or not isinstance(residue, int):
        raise ValueError("residue must be an integer")
    canonical_residue = residue % modulus
    shifted_base = tuple(
        base + canonical_residue * step
        for base, step in zip(parent_base_scores, parent_step)
    )
    child_step = tuple(modulus * step for step in parent_step)
    return rank_one_reachable_patterns(shifted_base, child_step)


def rank_one_residue_branch_erasure_report(
    parent_base_scores: tuple[int, ...],
    parent_step: tuple[int, ...],
    modulus: int,
    residue: int,
    branch_effects: dict[Pattern, object],
) -> BranchErasureReport:
    """Exact branch-erasure report for one rank-one residue-refined child fiber."""
    reachable = rank_one_residue_reachable_patterns(
        parent_base_scores, parent_step, modulus, residue
    )
    missing = [pattern for pattern in reachable if pattern not in branch_effects]
    if missing:
        raise ValueError("branch_effects must define every reachable pattern")
    effects = []
    seen = set()
    for pattern in reachable:
        effect = branch_effects[pattern]
        try:
            hash(effect)
        except TypeError as error:
            raise ValueError("branch effects must be hashable") from error
        if effect not in seen:
            seen.add(effect)
            effects.append(effect)
    return BranchErasureReport(
        reachable_patterns=reachable,
        distinct_effects=tuple(effects),
        safe_to_erase=len(effects) <= 1,
    )
