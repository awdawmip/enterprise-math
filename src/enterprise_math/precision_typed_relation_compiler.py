"""Typed finite relation/witness compiler by commutative-monoid block aggregation.

This module is an R004 specialization at the P023/A4 boundary. Generic
weighted/balanced partition refinement and weighted bisimulation are established
prior mathematics. The project-local purpose is to make typed future semantics
explicit and to expose the composition boundary between total-operation
congruences and partition-dependent relation/witness aggregation.

For a channel c with values in a declared commutative monoid (M, combine, zero)
and a current partition P, define

    sigma_c,P(x, B) = combine_{y in B} w_c(x,y).

A partition is stable when equivalent source states have identical aggregate
vectors into every current target block for every declared channel. Repeated
signature refinement terminates at the unique coarsest stable refinement.

Important specializations supplied here:
- Boolean OR: MAY support;
- natural-number addition: witness multiplicity;
- finite-set union: witness label/class set.

Commutativity/associativity/identity laws of user-supplied monoids are semantic
preconditions. The executable layer validates finite carrier/partition shape
and hashability of aggregate values, but does not attempt to prove monoid laws.
"""

from __future__ import annotations

from collections.abc import Callable, Hashable, Iterable, Sequence
from dataclasses import dataclass
from typing import Any


State = Hashable
Partition = tuple[tuple[State, ...], ...]


@dataclass(frozen=True)
class RelationChannel:
    """One typed relation channel valued in a declared commutative monoid."""

    name: str
    zero: Hashable
    combine: Callable[[Any, Any], Any]
    edge_value: Callable[[State, State], Any]


@dataclass(frozen=True)
class StableRefinementResult:
    """Terminal partition plus exact finite refinement history."""

    partition: Partition
    strict_rounds: int
    class_counts: tuple[int, ...]


def _normalize_states(states: Iterable[State]) -> tuple[State, ...]:
    points = tuple(states)
    if not points:
        raise ValueError("state carrier must be nonempty")
    try:
        declared = set(points)
    except TypeError as exc:
        raise ValueError("states must be hashable") from exc
    if len(points) != len(declared):
        raise ValueError("states must be distinct")
    return points


def normalize_partition(states: Iterable[State], blocks: Iterable[Iterable[State]]) -> Partition:
    """Validate and normalize a partition using declared carrier order."""

    points = _normalize_states(states)
    order = {state: index for index, state in enumerate(points)}
    declared = set(points)
    seen: set[State] = set()
    normalized: list[tuple[State, ...]] = []

    for block in blocks:
        row = tuple(block)
        if not row:
            raise ValueError("partition blocks must be nonempty")
        try:
            row_set = set(row)
        except TypeError as exc:
            raise ValueError("partition states must be hashable") from exc
        if len(row) != len(row_set):
            raise ValueError("partition block contains duplicates")
        if not row_set.issubset(declared):
            raise ValueError("partition contains undeclared state")
        if seen & row_set:
            raise ValueError("partition blocks must be disjoint")
        seen.update(row_set)
        normalized.append(tuple(sorted(row, key=order.__getitem__)))

    if seen != declared:
        raise ValueError("partition must cover every state exactly once")
    normalized.sort(key=lambda block: order[block[0]])
    return tuple(normalized)


def partition_refines(states: Iterable[State], finer: Partition, coarser: Partition) -> bool:
    """Return whether every finer block lies inside one coarser block."""

    points = _normalize_states(states)
    fine = normalize_partition(points, finer)
    coarse = normalize_partition(points, coarser)
    coarse_index = {
        state: block_index
        for block_index, block in enumerate(coarse)
        for state in block
    }
    return all(len({coarse_index[state] for state in block}) == 1 for block in fine)


def common_refinement(states: Iterable[State], partitions: Sequence[Partition]) -> Partition:
    """Raw common refinement (intersection of equality kernels)."""

    points = _normalize_states(states)
    if not partitions:
        return (points,)
    normalized = tuple(normalize_partition(points, partition) for partition in partitions)
    labels: list[dict[State, int]] = []
    for partition in normalized:
        labels.append(
            {
                state: block_index
                for block_index, block in enumerate(partition)
                for state in block
            }
        )

    groups: dict[tuple[int, ...], list[State]] = {}
    for state in points:
        key = tuple(label[state] for label in labels)
        groups.setdefault(key, []).append(state)
    return normalize_partition(points, tuple(tuple(group) for group in groups.values()))


def _require_channels(channels: Sequence[RelationChannel]) -> tuple[RelationChannel, ...]:
    declared = tuple(channels)
    if not declared:
        raise ValueError("at least one relation channel is required")
    names = [channel.name for channel in declared]
    if any(not isinstance(name, str) or not name for name in names):
        raise ValueError("channel names must be nonempty strings")
    if len(set(names)) != len(names):
        raise ValueError("channel names must be distinct")
    for channel in declared:
        if not callable(channel.combine) or not callable(channel.edge_value):
            raise ValueError("channel combine and edge_value must be callable")
        try:
            hash(channel.zero)
        except TypeError as exc:
            raise ValueError("channel zero must be hashable") from exc
    return declared


def block_aggregate(channel: RelationChannel, source: State, block: Sequence[State]) -> Hashable:
    """Aggregate one source's channel values into one current target block."""

    value: Any = channel.zero
    for target in block:
        value = channel.combine(value, channel.edge_value(source, target))
    try:
        hash(value)
    except TypeError as exc:
        raise ValueError("channel aggregates must be hashable") from exc
    return value


def relation_signature(
    state: State,
    partition: Partition,
    channels: Sequence[RelationChannel],
) -> tuple[Hashable, ...]:
    """Complete typed block-aggregate signature at the current partition."""

    declared = _require_channels(channels)
    return tuple(
        block_aggregate(channel, state, block)
        for channel in declared
        for block in partition
    )


def refine_relation_partition_once(
    states: Iterable[State],
    partition: Partition,
    channels: Sequence[RelationChannel],
) -> Partition:
    """Split source blocks by their complete current target-block signatures."""

    points = _normalize_states(states)
    current = normalize_partition(points, partition)
    declared = _require_channels(channels)
    refined: list[tuple[State, ...]] = []

    for block in current:
        groups: dict[tuple[Hashable, ...], list[State]] = {}
        for state in block:
            signature = relation_signature(state, current, declared)
            groups.setdefault(signature, []).append(state)
        refined.extend(tuple(group) for group in groups.values())

    return normalize_partition(points, tuple(refined))


def relation_partition_is_stable(
    states: Iterable[State],
    partition: Partition,
    channels: Sequence[RelationChannel],
) -> bool:
    points = _normalize_states(states)
    current = normalize_partition(points, partition)
    return refine_relation_partition_once(points, current, channels) == current


def coarsest_relation_stable_refinement(
    states: Iterable[State],
    initial_partition: Partition,
    channels: Sequence[RelationChannel],
) -> StableRefinementResult:
    """Return the unique coarsest stable refinement of the initial partition.

    The proof of coarseness is the standard finite refinement induction:
    every stable refinement Q of P_n also refines P_(n+1), because every P_n
    target block is a union of Q-blocks and commutative-monoid aggregation
    respects such unions.
    """

    points = _normalize_states(states)
    declared = _require_channels(channels)
    current = normalize_partition(points, initial_partition)
    counts = [len(current)]
    strict_rounds = 0

    while True:
        refined = refine_relation_partition_once(points, current, declared)
        if refined == current:
            break
        if len(refined) <= len(current):
            raise AssertionError("a strict refinement must increase class count")
        strict_rounds += 1
        current = refined
        counts.append(len(current))
        if strict_rounds > len(points) - counts[0]:
            raise AssertionError("finite strict-refinement bound violated")

    return StableRefinementResult(
        partition=current,
        strict_rounds=strict_rounds,
        class_counts=tuple(counts),
    )


def stabilized_common_refinement(
    states: Iterable[State],
    partitions: Sequence[Partition],
    channels: Sequence[RelationChannel],
) -> StableRefinementResult:
    """Meet stable requirements by stabilizing their raw common refinement."""

    points = _normalize_states(states)
    raw = common_refinement(points, partitions)
    return coarsest_relation_stable_refinement(points, raw, channels)


def may_channel(name: str, edges: Iterable[tuple[State, State]]) -> RelationChannel:
    edge_set = frozenset(edges)
    return RelationChannel(
        name=name,
        zero=False,
        combine=lambda left, right: bool(left or right),
        edge_value=lambda source, target: (source, target) in edge_set,
    )


def count_channel(
    name: str,
    witnesses: Iterable[tuple[State, State, Hashable]],
) -> RelationChannel:
    counts: dict[tuple[State, State], int] = {}
    for source, target, _label in witnesses:
        counts[(source, target)] = counts.get((source, target), 0) + 1
    return RelationChannel(
        name=name,
        zero=0,
        combine=lambda left, right: left + right,
        edge_value=lambda source, target: counts.get((source, target), 0),
    )


def label_set_channel(
    name: str,
    witnesses: Iterable[tuple[State, State, Hashable]],
) -> RelationChannel:
    mutable: dict[tuple[State, State], set[Hashable]] = {}
    for source, target, label in witnesses:
        try:
            hash(label)
        except TypeError as exc:
            raise ValueError("witness labels must be hashable") from exc
        mutable.setdefault((source, target), set()).add(label)
    labels = {key: frozenset(values) for key, values in mutable.items()}
    return RelationChannel(
        name=name,
        zero=frozenset(),
        combine=lambda left, right: left | right,
        edge_value=lambda source, target: labels.get((source, target), frozenset()),
    )
