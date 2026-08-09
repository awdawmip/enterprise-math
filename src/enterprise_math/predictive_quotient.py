"""Finite predictive quotient compiler for Enterprise Math engineering probes.

Given a finite deterministic state set, a finite named action family, and a
finite observation language, this module computes the coarsest state partition
that preserves all observation futures through a declared horizon.  Repeating
refinement until no further split occurs gives the coarsest partition compatible
with arbitrary finite action words on the supplied finite system.

This is established finite-state partition-refinement / Moore-machine style
mathematics used as an executable P023 specialization.  The project-specific
purpose is to compile a task-relative precision state automatically and to
falsify hand-derived E002 quotient formulas against a generic finite oracle.
"""

from __future__ import annotations

from collections.abc import Callable, Hashable, Mapping, Sequence
from dataclasses import dataclass
from typing import Any

State = Hashable
Action = Callable[[State], State]
Observation = Callable[[State], Hashable]


def _validate_states(states: Sequence[State]) -> tuple[State, ...]:
    values = tuple(states)
    if not values:
        raise ValueError("state set must be nonempty")
    if len(set(values)) != len(values):
        raise ValueError("states must be distinct")
    return values


def _validate_actions(
    states: tuple[State, ...],
    actions: Mapping[str, Action],
) -> tuple[tuple[str, Action], ...]:
    if not actions:
        raise ValueError("at least one action is required")
    items = tuple(actions.items())
    names = [name for name, _ in items]
    if any(not isinstance(name, str) or not name for name in names):
        raise TypeError("action names must be nonempty strings")
    if len(set(names)) != len(names):
        raise ValueError("action names must be distinct")
    state_set = set(states)
    for name, action in items:
        if not callable(action):
            raise TypeError(f"action {name!r} must be callable")
        for state in states:
            target = action(state)
            if target not in state_set:
                raise ValueError(f"action {name!r} leaves the finite state set at {state!r}")
    return items


def _canonical_ids(signatures: Sequence[Hashable]) -> tuple[int, ...]:
    ids: dict[Hashable, int] = {}
    result: list[int] = []
    for signature in signatures:
        if signature not in ids:
            ids[signature] = len(ids)
        result.append(ids[signature])
    return tuple(result)


def partition_blocks(
    states: Sequence[State],
    partition: Sequence[int],
) -> tuple[tuple[State, ...], ...]:
    """Return blocks in canonical first-state order."""
    values = _validate_states(states)
    labels = tuple(partition)
    if len(labels) != len(values):
        raise ValueError("partition length must match state count")
    ordered: list[list[State]] = []
    index_by_label: dict[int, int] = {}
    for state, label in zip(values, labels):
        if isinstance(label, bool) or not isinstance(label, int) or label < 0:
            raise TypeError("partition labels must be nonnegative integers")
        if label not in index_by_label:
            index_by_label[label] = len(ordered)
            ordered.append([])
        ordered[index_by_label[label]].append(state)
    return tuple(tuple(block) for block in ordered)


def partition_block_count(partition: Sequence[int]) -> int:
    """Number of equivalence blocks represented by one partition label vector."""
    labels = tuple(partition)
    if not labels:
        return 0
    return len(set(labels))


def restricted_block_count(
    states: Sequence[State],
    partition: Sequence[int],
    subset: Sequence[State],
) -> int:
    """Number of partition blocks intersecting one declared initial-state subset."""
    values = _validate_states(states)
    labels = tuple(partition)
    if len(labels) != len(values):
        raise ValueError("partition length must match state count")
    state_to_label = dict(zip(values, labels))
    requested = tuple(subset)
    if len(set(requested)) != len(requested):
        raise ValueError("subset states must be distinct")
    if any(state not in state_to_label for state in requested):
        raise ValueError("subset must lie inside the finite state set")
    return len({state_to_label[state] for state in requested})


def observation_partition(
    states: Sequence[State],
    observe: Observation,
) -> tuple[int, ...]:
    """Coarsest partition preserving the current observation only."""
    values = _validate_states(states)
    if not callable(observe):
        raise TypeError("observe must be callable")
    return _canonical_ids(tuple(observe(state) for state in values))


def refine_predictive_partition(
    states: Sequence[State],
    actions: Mapping[str, Action],
    observe: Observation,
    previous: Sequence[int],
) -> tuple[int, ...]:
    """Add one action step of future observation responsibility."""
    values = _validate_states(states)
    items = _validate_actions(values, actions)
    labels = tuple(previous)
    if len(labels) != len(values):
        raise ValueError("previous partition length must match state count")
    index = {state: position for position, state in enumerate(values)}
    signatures = []
    for state in values:
        signatures.append(
            (
                observe(state),
                tuple(labels[index[action(state)]] for _name, action in items),
            )
        )
    return _canonical_ids(tuple(signatures))


def finite_horizon_partition(
    states: Sequence[State],
    actions: Mapping[str, Action],
    observe: Observation,
    horizon: int,
) -> tuple[int, ...]:
    """Coarsest partition preserving all observation futures through ``horizon``.

    Horizon zero preserves only the current observation.  Each additional
    refinement adds every one-step action followed by the already-preserved
    shorter future language.
    """
    if isinstance(horizon, bool) or not isinstance(horizon, int):
        raise TypeError("horizon must be an integer")
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    values = _validate_states(states)
    _validate_actions(values, actions)
    partition = observation_partition(values, observe)
    for _ in range(horizon):
        partition = refine_predictive_partition(values, actions, observe, partition)
    return partition


def predictive_block_profile(
    states: Sequence[State],
    actions: Mapping[str, Action],
    observe: Observation,
    max_horizon: int,
    subset: Sequence[State] | None = None,
) -> tuple[int, ...]:
    """Block counts from horizon zero through ``max_horizon``."""
    if isinstance(max_horizon, bool) or not isinstance(max_horizon, int):
        raise TypeError("max_horizon must be an integer")
    if max_horizon < 0:
        raise ValueError("max_horizon must be nonnegative")
    values = _validate_states(states)
    _validate_actions(values, actions)
    partition = observation_partition(values, observe)
    counts: list[int] = []
    for horizon in range(max_horizon + 1):
        if subset is None:
            counts.append(partition_block_count(partition))
        else:
            counts.append(restricted_block_count(values, partition, subset))
        if horizon != max_horizon:
            partition = refine_predictive_partition(values, actions, observe, partition)
    return tuple(counts)


@dataclass(frozen=True)
class StablePredictiveQuotient:
    """Finite fixed point of predictive partition refinement."""

    partition: tuple[int, ...]
    stabilization_depth: int
    block_count: int


def stable_predictive_partition(
    states: Sequence[State],
    actions: Mapping[str, Action],
    observe: Observation,
) -> StablePredictiveQuotient:
    """Compute the coarsest partition preserving all finite action-word futures."""
    values = _validate_states(states)
    _validate_actions(values, actions)
    partition = observation_partition(values, observe)
    depth = 0
    while True:
        refined = refine_predictive_partition(values, actions, observe, partition)
        if partition_blocks(values, refined) == partition_blocks(values, partition):
            return StablePredictiveQuotient(
                partition=partition,
                stabilization_depth=depth,
                block_count=partition_block_count(partition),
            )
        if partition_block_count(refined) <= partition_block_count(partition):
            raise AssertionError("strict predictive refinement failed to split a block")
        partition = refined
        depth += 1
        if depth >= len(values):
            raise AssertionError("finite partition refinement exceeded state-count bound")


def distinguishing_horizon(
    states: Sequence[State],
    actions: Mapping[str, Action],
    observe: Observation,
    left: State,
    right: State,
) -> int | None:
    """First finite horizon that distinguishes two states, or ``None`` if never."""
    values = _validate_states(states)
    if left not in values or right not in values:
        raise ValueError("both states must belong to the finite state set")
    _validate_actions(values, actions)
    index = {state: position for position, state in enumerate(values)}
    partition = observation_partition(values, observe)
    horizon = 0
    while True:
        if partition[index[left]] != partition[index[right]]:
            return horizon
        refined = refine_predictive_partition(values, actions, observe, partition)
        if partition_blocks(values, refined) == partition_blocks(values, partition):
            return None
        partition = refined
        horizon += 1


def quotient_transition_table(
    states: Sequence[State],
    actions: Mapping[str, Action],
    partition: Sequence[int],
) -> dict[tuple[int, str], int]:
    """Build the deterministic quotient transition table, rejecting unsafe partitions."""
    values = _validate_states(states)
    items = _validate_actions(values, actions)
    labels = tuple(partition)
    if len(labels) != len(values):
        raise ValueError("partition length must match state count")
    index = {state: position for position, state in enumerate(values)}
    table: dict[tuple[int, str], int] = {}
    for state, source_label in zip(values, labels):
        for name, action in items:
            target_label = labels[index[action(state)]]
            key = (source_label, name)
            previous = table.setdefault(key, target_label)
            if previous != target_label:
                raise ValueError("partition is not compatible with the action family")
    return table


def quotient_observation_table(
    states: Sequence[State],
    observe: Observation,
    partition: Sequence[int],
) -> dict[int, Any]:
    """Build block observations, rejecting partitions that merge observable outputs."""
    values = _validate_states(states)
    labels = tuple(partition)
    if len(labels) != len(values):
        raise ValueError("partition length must match state count")
    table: dict[int, Any] = {}
    for state, label in zip(values, labels):
        output = observe(state)
        if label in table and table[label] != output:
            raise ValueError("partition merges distinct current observations")
        table[label] = output
    return table
