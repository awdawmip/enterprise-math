"""State-local branch-erasure checks from A3 hidden guard lattices.

General future-compatible quotient semantics say that hidden branch identity may
be erased exactly when all fine branches reachable inside one coarse fiber have
the same coarse effect. This module supplies A3-specialized exact reachable-set
construction for hidden guard rank one and two.

The branch-effect table is explicit and finite: every Boolean guard pattern maps
to a hashable coarse effect (for example a descended affine-map tuple). Effects
of unreachable patterns are irrelevant and create no precision obligation.
"""

from __future__ import annotations

from collections.abc import Hashable, Mapping
from dataclasses import dataclass
from itertools import product

from .guard_image_lattice import IntMatrix
from .rank_two_guard_reachability import rank_two_threshold_pattern_reachable


Pattern = tuple[bool, ...]


@dataclass(frozen=True)
class BranchErasureReport:
    reachable_patterns: tuple[Pattern, ...]
    distinct_effects: tuple[Hashable, ...]
    safe_to_erase: bool


def _require_score_step(base_scores: tuple[int, ...], step: tuple[int, ...]) -> int:
    if not isinstance(base_scores, tuple) or not isinstance(step, tuple):
        raise ValueError("base_scores and step must be tuples")
    if not base_scores or len(base_scores) != len(step):
        raise ValueError("base_scores and step must have the same positive length")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for value in base_scores + step
    ):
        raise ValueError("base_scores and step entries must be integers")
    if not any(step):
        raise ValueError("rank-one step must be nonzero")
    return len(step)


def _require_complete_branch_table(
    branch_effects: Mapping[Pattern, Hashable], guard_count: int
) -> None:
    if not isinstance(branch_effects, Mapping):
        raise ValueError("branch_effects must be a mapping")
    expected = set(product((False, True), repeat=guard_count))
    if set(branch_effects) != expected:
        raise ValueError("branch_effects must define every Boolean guard pattern exactly once")
    for effect in branch_effects.values():
        try:
            hash(effect)
        except TypeError as error:
            raise ValueError("branch effects must be hashable") from error


def rank_one_reachable_patterns(
    base_scores: tuple[int, ...], step: tuple[int, ...]
) -> tuple[Pattern, ...]:
    """Enumerate all threshold patterns on the integer line g+t*h without 2^r search.

    Every nonconstant guard flips exactly once as t increases. The pattern at
    t -> -infinity is explicit, and processing the sorted integer switch points
    gives every reachable pattern. Therefore at most q+1 patterns occur, where
    q is the number of nonzero step coordinates.
    """
    guard_count = _require_score_step(base_scores, step)
    current = []
    switches: dict[int, list[tuple[int, bool]]] = {}

    for index, (base, delta) in enumerate(zip(base_scores, step)):
        if delta > 0:
            current.append(False)
            switch = -((-(-base)) // delta)  # ceil(-base/delta)
            # Written explicitly below to keep the integer threshold obvious.
            switch = -((base) // delta) if base % delta == 0 else -((base) // delta)
            # Python floor division makes the compact identity ceil(-base/d)=-(base//d).
            switch = -(base // delta)
            switches.setdefault(switch, []).append((index, True))
        elif delta < 0:
            current.append(True)
            switch = base // (-delta) + 1
            switches.setdefault(switch, []).append((index, False))
        else:
            current.append(base >= 0)

    patterns = [tuple(current)]
    for switch in sorted(switches):
        for index, value in switches[switch]:
            current[index] = value
        pattern = tuple(current)
        if pattern != patterns[-1]:
            patterns.append(pattern)

    if len(patterns) > 1 + sum(delta != 0 for delta in step):
        raise AssertionError("rank-one threshold sweep cannot exceed q+1 patterns")
    if any(len(pattern) != guard_count for pattern in patterns):
        raise AssertionError("reachable patterns must preserve guard count")
    return tuple(patterns)


def _distinct_effects(
    reachable_patterns: tuple[Pattern, ...],
    branch_effects: Mapping[Pattern, Hashable],
) -> tuple[Hashable, ...]:
    result = []
    seen = set()
    for pattern in reachable_patterns:
        effect = branch_effects[pattern]
        if effect not in seen:
            seen.add(effect)
            result.append(effect)
    return tuple(result)


def rank_one_branch_erasure_report(
    base_scores: tuple[int, ...],
    step: tuple[int, ...],
    branch_effects: Mapping[Pattern, Hashable],
) -> BranchErasureReport:
    """Exact coarse-effect erasure report for one rank-one hidden guard fiber."""
    guard_count = _require_score_step(base_scores, step)
    _require_complete_branch_table(branch_effects, guard_count)
    reachable = rank_one_reachable_patterns(base_scores, step)
    effects = _distinct_effects(reachable, branch_effects)
    return BranchErasureReport(
        reachable_patterns=reachable,
        distinct_effects=effects,
        safe_to_erase=len(effects) <= 1,
    )


def rank_two_branch_erasure_report(
    base_scores: tuple[int, ...],
    generators: IntMatrix,
    branch_effects: Mapping[Pattern, Hashable],
) -> BranchErasureReport:
    """Exact coarse-effect erasure report for one rank-two hidden guard fiber.

    The branch table is already an explicit 2^r-sized program input, so testing
    its keys does not add asymptotic expansion beyond that representation. Each
    reachability decision itself uses the exact rank-two integer solver.
    """
    if not isinstance(base_scores, tuple) or not base_scores:
        raise ValueError("base_scores must be a non-empty tuple")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for value in base_scores
    ):
        raise ValueError("base_scores entries must be integers")
    guard_count = len(base_scores)
    _require_complete_branch_table(branch_effects, guard_count)

    reachable = tuple(
        pattern
        for pattern in branch_effects
        if rank_two_threshold_pattern_reachable(base_scores, generators, pattern)
    )
    if not reachable:
        raise AssertionError("an affine rank-two guard lattice must realize at least one pattern")
    effects = _distinct_effects(reachable, branch_effects)
    return BranchErasureReport(
        reachable_patterns=reachable,
        distinct_effects=effects,
        safe_to_erase=len(effects) <= 1,
    )
