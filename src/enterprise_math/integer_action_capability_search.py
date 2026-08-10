"""Exact branch-and-bound search for minimum future-action capability families.

For a fixed precision level (STATE_KERNEL or INTEGER_MODULE), the predicate

    P(S) := action subset S preserves the full declared future precision

is monotone upward.  That monotonicity, not context-local action redundancy, is
the safe search structure.

Before branching, every action that belongs to all preserving subsets is found
by the leave-one-out unavoidable-core theorem.  Those actions are preselected;
only optional actions enter the search tree.

The remaining exact search uses only theorem-safe prunes:

1. a selected set whose size is already no better than the best known solution
   cannot improve the optimum;
2. if ``selected union undecided`` does not preserve full precision, no extension
   below that node can preserve it;
3. if ``selected`` already preserves, every extension is larger and the branch
   closes immediately.

The search is exact but has no polynomial worst-case claim.  Generic capability
rank is not submodular, local redundancy is context-dependent, and minimal
preserving families can have unequal cardinalities.  The unavoidable core can
shrink the exact search substantially, but the optional synergy problem can
still be exponential.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence

from .integer_action_capability_basis import (
    INTEGER_MODULE,
    STATE_KERNEL,
    action_subset_preserves,
)
from .integer_action_capability_core import action_capability_unavoidable_core


@dataclass(frozen=True)
class MinimumActionCapabilitySearchReport:
    mode: str
    action_count: int
    unavoidable_core: tuple[int, ...]
    optional_actions: tuple[int, ...]
    minimum_cardinality: int
    minimum_subsets: tuple[tuple[int, ...], ...]
    visited_nodes: int
    oracle_calls: int
    cached_oracle_hits: int
    size_prunes: int
    impossible_extension_prunes: int
    preserving_node_prunes: int
    full_subset_count: int
    core_reduced_subset_count: int

    @property
    def core_removed_search_dimensions(self) -> int:
        return self.action_count - len(self.optional_actions)

    @property
    def oracle_avoided_full_original_enumeration(self) -> bool:
        return self.oracle_calls < self.full_subset_count


def _mode(value: str) -> str:
    if value not in (STATE_KERNEL, INTEGER_MODULE):
        raise ValueError("mode must be STATE_KERNEL or INTEGER_MODULE")
    return value


def minimum_action_capability_subsets(
    action_matrices: Sequence[Sequence[Sequence[int]]],
    observation_rows: Sequence[Sequence[int]],
    *,
    mode: str = INTEGER_MODULE,
) -> MinimumActionCapabilitySearchReport:
    """Return every minimum-cardinality full-precision action subset exactly."""
    actions = tuple(action_matrices)
    if not actions:
        raise ValueError("at least one action is required")
    selected_mode = _mode(mode)
    action_count = len(actions)
    all_indices = tuple(range(action_count))

    core_report = action_capability_unavoidable_core(
        actions,
        observation_rows,
        mode=selected_mode,
    )
    unavoidable_core = core_report.unavoidable_core
    optional_actions = core_report.optional_actions

    cache: dict[frozenset[int], bool] = {}
    oracle_calls = 0
    cached_hits = 0

    def preserves(indices: tuple[int, ...]) -> bool:
        nonlocal oracle_calls, cached_hits
        key = frozenset(indices)
        if key in cache:
            cached_hits += 1
            return cache[key]
        oracle_calls += 1
        value = action_subset_preserves(
            actions,
            observation_rows,
            tuple(sorted(key)),
            mode=selected_mode,
        )
        cache[key] = value
        return value

    if not preserves(all_indices):
        raise AssertionError("full action family failed to preserve its own precision")

    best_size = action_count + 1
    solutions: set[tuple[int, ...]] = set()
    visited_nodes = 0
    size_prunes = 0
    impossible_prunes = 0
    preserving_prunes = 0

    def search(selected: tuple[int, ...], undecided: tuple[int, ...]) -> None:
        nonlocal best_size, visited_nodes
        nonlocal size_prunes, impossible_prunes, preserving_prunes
        visited_nodes += 1

        if len(selected) > best_size:
            size_prunes += 1
            return

        if preserves(selected):
            preserving_prunes += 1
            if len(selected) < best_size:
                best_size = len(selected)
                solutions.clear()
            if len(selected) == best_size:
                solutions.add(tuple(sorted(selected)))
            return

        if len(selected) >= best_size:
            size_prunes += 1
            return

        maximal_extension = tuple((*selected, *undecided))
        if not preserves(maximal_extension):
            impossible_prunes += 1
            return

        if not undecided:
            return

        action = undecided[0]
        rest = undecided[1:]

        # Exclusion first tends to discover smaller preserving families early;
        # correctness is independent of branch order.
        search(selected, rest)
        search(tuple((*selected, action)), rest)

    search(unavoidable_core, optional_actions)
    if not solutions or best_size > action_count:
        raise AssertionError("minimum capability search lost the full-family solution")

    return MinimumActionCapabilitySearchReport(
        mode=selected_mode,
        action_count=action_count,
        unavoidable_core=unavoidable_core,
        optional_actions=optional_actions,
        minimum_cardinality=best_size,
        minimum_subsets=tuple(sorted(solutions)),
        visited_nodes=visited_nodes,
        oracle_calls=oracle_calls,
        cached_oracle_hits=cached_hits,
        size_prunes=size_prunes,
        impossible_extension_prunes=impossible_prunes,
        preserving_node_prunes=preserving_prunes,
        full_subset_count=1 << action_count,
        core_reduced_subset_count=1 << len(optional_actions),
    )
