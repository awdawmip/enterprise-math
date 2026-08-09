"""Finite operation-family closure for P023 composition-safe collapse.

Given a finite state space, a finite named family of deterministic endomaps, and
an initial observation partition, this module computes the coarsest refinement
on which every operation descends.  The refinement is exact and finite:

    q_{t+1}(x) = (q_t(x), (q_t(F_a(x)))_a).

At depth t, two states remain equivalent exactly when every operation word of
length at most t sends them to states with the same original observation.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping
from itertools import product

Vertex = Hashable
OperationName = Hashable
Operation = Mapping[Vertex, Vertex]
Partition = Mapping[Vertex, Hashable]


def _domain(domain: Iterable[Vertex]) -> tuple[Vertex, ...]:
    states = tuple(domain)
    if not states:
        raise ValueError("domain must be nonempty")
    if len(states) != len(set(states)):
        raise ValueError("domain states must be distinct")
    return states


def _canonical_ids(states: tuple[Vertex, ...], labels: Mapping[Vertex, Hashable]) -> dict[Vertex, int]:
    if set(labels) != set(states):
        raise ValueError("partition must label every state exactly once")
    ids: dict[Hashable, int] = {}
    result: dict[Vertex, int] = {}
    for state in states:
        label = labels[state]
        if label not in ids:
            ids[label] = len(ids)
        result[state] = ids[label]
    return result


def _operations(
    states: tuple[Vertex, ...], operations: Mapping[OperationName, Operation]
) -> tuple[tuple[OperationName, Operation], ...]:
    if not operations:
        raise ValueError("operation family must be nonempty")
    state_set = set(states)
    result: list[tuple[OperationName, Operation]] = []
    for name, operation in operations.items():
        if set(operation) != state_set:
            raise ValueError("every operation must be total on the domain")
        if any(operation[state] not in state_set for state in states):
            raise ValueError("every operation must map the domain into itself")
        result.append((name, operation))
    return tuple(result)


def refines(
    domain: Iterable[Vertex], finer: Partition, coarser: Partition
) -> bool:
    states = _domain(domain)
    if set(finer) != set(states) or set(coarser) != set(states):
        raise ValueError("partitions must label every state exactly once")
    seen: dict[Hashable, Hashable] = {}
    for state in states:
        fine = finer[state]
        coarse = coarser[state]
        if fine in seen and seen[fine] != coarse:
            return False
        seen[fine] = coarse
    return True


def operation_descends(
    domain: Iterable[Vertex], operation: Operation, partition: Partition
) -> bool:
    """Whether one deterministic operation is well-defined on partition classes."""
    states = _domain(domain)
    if set(operation) != set(states) or set(partition) != set(states):
        raise ValueError("operation and partition must cover the domain")
    seen: dict[Hashable, Hashable] = {}
    for state in states:
        coarse = partition[state]
        next_coarse = partition[operation[state]]
        if coarse in seen and seen[coarse] != next_coarse:
            return False
        seen[coarse] = next_coarse
    return True


def family_descends(
    domain: Iterable[Vertex],
    operations: Mapping[OperationName, Operation],
    partition: Partition,
) -> bool:
    states = _domain(domain)
    family = _operations(states, operations)
    return all(operation_descends(states, operation, partition) for _, operation in family)


def family_refinement_step(
    domain: Iterable[Vertex],
    operations: Mapping[OperationName, Operation],
    partition: Partition,
) -> dict[Vertex, int]:
    """Refine by current class plus every generator's next class."""
    states = _domain(domain)
    family = _operations(states, operations)
    current = _canonical_ids(states, partition)
    signatures = {
        state: (
            current[state],
            tuple(current[operation[state]] for _, operation in family),
        )
        for state in states
    }
    return _canonical_ids(states, signatures)


def family_future_partition_sequence(
    domain: Iterable[Vertex],
    operations: Mapping[OperationName, Operation],
    initial_partition: Partition,
) -> tuple[dict[Vertex, int], ...]:
    """Return all distinct stages through the first common-compatible partition."""
    states = _domain(domain)
    _operations(states, operations)
    current = _canonical_ids(states, initial_partition)
    stages = [current]
    while True:
        nxt = family_refinement_step(states, operations, current)
        if nxt == current:
            return tuple(stages)
        if not refines(states, nxt, current):
            raise AssertionError("family refinement must never merge existing classes")
        stages.append(nxt)
        current = nxt
        if len(stages) > len(states):
            raise AssertionError("finite family refinement exceeded the state bound")


def stable_family_partition(
    domain: Iterable[Vertex],
    operations: Mapping[OperationName, Operation],
    initial_partition: Partition,
) -> dict[Vertex, int]:
    """Coarsest refinement on which every supplied operation descends."""
    return dict(family_future_partition_sequence(domain, operations, initial_partition)[-1])


def apply_word(
    state: Vertex,
    operations: Mapping[OperationName, Operation],
    word: Iterable[OperationName],
) -> Vertex:
    """Apply an operation word from left to right."""
    current = state
    for name in word:
        if name not in operations:
            raise ValueError("word contains an operation outside the family")
        operation = operations[name]
        if current not in operation:
            raise ValueError("operation is not defined on the visited state")
        current = operation[current]
    return current


def operation_words(names: Iterable[OperationName], max_length: int) -> tuple[tuple[OperationName, ...], ...]:
    """Enumerate all operation words of length at most ``max_length``."""
    if max_length < 0:
        raise ValueError("max_length must be nonnegative")
    alphabet = tuple(names)
    if not alphabet:
        raise ValueError("operation alphabet must be nonempty")
    words: list[tuple[OperationName, ...]] = [()]
    for length in range(1, max_length + 1):
        words.extend(product(alphabet, repeat=length))
    return tuple(words)


def word_observation_signature(
    state: Vertex,
    operations: Mapping[OperationName, Operation],
    observation: Partition,
    max_length: int,
) -> tuple[Hashable, ...]:
    """Original observation after every operation word up to a bounded length."""
    words = operation_words(operations.keys(), max_length)
    result: list[Hashable] = []
    for word in words:
        reached = apply_word(state, operations, word)
        if reached not in observation:
            raise ValueError("observation must cover every reached state")
        result.append(observation[reached])
    return tuple(result)


def class_count(partition: Partition) -> int:
    return len(set(partition.values()))
