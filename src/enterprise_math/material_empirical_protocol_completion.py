"""Compare predictive state before and after completing measured protocol edges.

This E001 diagnostic sits on top of ``material_empirical_action_protocol``.  It
records a useful negative boundary for empirical-state identification:

    adding measurements is not monotone in predictive class count.

Replacing an ``UNDERRESOLVED`` action edge by a measured successor can reveal a
previously hidden future difference and split one stable class.  It can also
remove a conservative ``measured versus unknown`` distinction and merge classes.
Both effects can occur in the same protocol completion.

The comparison is deliberately strict about what counts as a completion:

* every previously measured state remains measured;
* its current observation is unchanged;
* the declared action alphabet is unchanged;
* every previously explicit measured transition is unchanged;
* only previously missing transitions may remain missing or become measured;
* new measured states may be added.

The resulting relation is about the finite declared empirical prediction
interface, not monotonicity of physical material degrees of freedom.  Generic
partition-refinement theory remains owned by A2/P023; this module is only an
E001 completion diagnostic.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations

from .material_empirical_action_protocol import (
    EmpiricalActionProtocolMachine,
    UNDERRESOLVED_STATE,
)

SAME = "SAME"
AFTER_REFINES = "AFTER_REFINES"
AFTER_COARSENS = "AFTER_COARSENS"
INCOMPARABLE = "INCOMPARABLE"
CompletionRelation = str

Pair = tuple[str, str]


@dataclass(frozen=True)
class ProtocolCompletionComparison:
    shared_state_ids: tuple[str, ...]
    before_shared_class_count: int
    after_shared_class_count: int
    relation: CompletionRelation
    newly_split_pairs: tuple[Pair, ...]
    newly_merged_pairs: tuple[Pair, ...]


def _validate_completion(
    before: EmpiricalActionProtocolMachine,
    after: EmpiricalActionProtocolMachine,
) -> tuple[str, ...]:
    if before.action_names != after.action_names:
        raise ValueError("protocol completion must preserve the declared action alphabet")

    before_ids = set(before.measured_state_ids)
    after_ids = set(after.measured_state_ids)
    if not before_ids.issubset(after_ids):
        raise ValueError("protocol completion must not remove measured states")

    before_missing = set(before.missing_transitions)
    for state_id in before.measured_state_ids:
        if before.current_observation[state_id] != after.current_observation[state_id]:
            raise ValueError("protocol completion must preserve existing observations")
        for action in before.action_names:
            if (state_id, action) in before_missing:
                continue
            before_target = before.operations[action][state_id]
            after_target = after.operations[action][state_id]
            if before_target == UNDERRESOLVED_STATE:
                raise AssertionError("explicit measured transition unexpectedly used sink")
            if after_target != before_target:
                raise ValueError("protocol completion must preserve measured transitions")

    return tuple(sorted(before_ids))


def _restricted_class_count(
    machine: EmpiricalActionProtocolMachine,
    state_ids: tuple[str, ...],
) -> int:
    return len({machine.stable_partition[state_id] for state_id in state_ids})


def compare_protocol_completion(
    before: EmpiricalActionProtocolMachine,
    after: EmpiricalActionProtocolMachine,
) -> ProtocolCompletionComparison:
    """Classify how added measurements change future equivalence on old states."""
    shared = _validate_completion(before, after)
    newly_split: list[Pair] = []
    newly_merged: list[Pair] = []
    for left, right in combinations(shared, 2):
        before_equal = before.stable_partition[left] == before.stable_partition[right]
        after_equal = after.stable_partition[left] == after.stable_partition[right]
        if before_equal and not after_equal:
            newly_split.append((left, right))
        elif not before_equal and after_equal:
            newly_merged.append((left, right))

    if newly_split and newly_merged:
        relation = INCOMPARABLE
    elif newly_split:
        relation = AFTER_REFINES
    elif newly_merged:
        relation = AFTER_COARSENS
    else:
        relation = SAME

    return ProtocolCompletionComparison(
        shared_state_ids=shared,
        before_shared_class_count=_restricted_class_count(before, shared),
        after_shared_class_count=_restricted_class_count(after, shared),
        relation=relation,
        newly_split_pairs=tuple(newly_split),
        newly_merged_pairs=tuple(newly_merged),
    )
