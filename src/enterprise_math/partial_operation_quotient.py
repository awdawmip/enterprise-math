"""Finite future-safe quotients for deterministic partial operation families.

This module is the research answer candidate for Foundation question
FQ-20260809-006.  It extends the existing total-operation P023 reference by
allowing each named deterministic operation to have a declared state-dependent
domain

    F_a : D_a -> X.

The generic mathematics is standard finite partial-transition-system /
behavioral-equivalence theory.  The Enterprise Math question is the minimal
interface needed so that action legality is not silently discarded by a
future-safe quotient.

Let ``q_t`` be the current finite partition.  One refinement step records,
for every generator ``a``, both whether the action is enabled and, when it is,
the next ``q_t`` class:

    q_(t+1)(x)
      = (q_t(x), ((enabled_a(x), next_class_a(x)) for a)).

Disabled actions use an explicit marker in the signature; they are not treated
as identity steps and no artificial world state is added to the semantic
domain.

At depth ``h``, the resulting partition is exactly equality of the original
observation after every *defined* operation word of length at most ``h``, with
undefinedness itself retained in the word signature.  Since every prefix is
also one of the enumerated words, this is equivalently equality of complete
prefix-legality behavior plus reached observations.

On a finite state set the refinement terminates.  The stable result is the
coarsest refinement of the initial observation for which every partial
operation descends while preserving its domain membership: states in one class
must agree on whether each action is enabled, and enabled targets must land in
one common quotient class.

If every operation is total, the construction reduces exactly to the canonical
``operation_quotient`` future refinement up to partition-label renaming.
More generally every partial family has an exact compiler reduction to that
same total theory: add one fresh absorbing state ``bottom``; send every disabled
transition to ``bottom``; and give ``bottom`` an observation label distinct from
every ordinary state observation.  On the original states, bounded future-word
partitions and the stable quotient are then exactly the genuine partial-family
partitions.  This lifted state is a verification/compiler device, not an
additional Enterprise Math physical/world state.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping
from dataclasses import dataclass

from .operation_quotient import operation_words

Vertex = Hashable
OperationName = Hashable
PartialOperation = Mapping[Vertex, Vertex]
Partition = Mapping[Vertex, Hashable]


def _domain(domain: Iterable[Vertex]) -> tuple[Vertex, ...]:
    states = tuple(domain)
    if not states:
        raise ValueError("domain must be nonempty")
    if len(states) != len(set(states)):
        raise ValueError("domain states must be distinct")
    return states


def _canonical_ids(
    states: tuple[Vertex, ...], labels: Mapping[Vertex, Hashable]
) -> dict[Vertex, int]:
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


def _partial_operations(
    states: tuple[Vertex, ...],
    operations: Mapping[OperationName, PartialOperation],
) -> tuple[tuple[OperationName, PartialOperation], ...]:
    if not operations:
        raise ValueError("operation family must be nonempty")
    state_set = set(states)
    result: list[tuple[OperationName, PartialOperation]] = []
    for name, operation in operations.items():
        operation_domain = set(operation)
        if not operation_domain <= state_set:
            raise ValueError("partial operation domain must lie inside the state domain")
        if any(target not in state_set for target in operation.values()):
            raise ValueError("partial operation targets must lie inside the state domain")
        result.append((name, operation))
    return tuple(result)


def totalize_partial_family(
    domain: Iterable[Vertex],
    operations: Mapping[OperationName, PartialOperation],
    observation: Partition,
    *,
    undefined_state: Vertex,
    undefined_observation: Hashable,
) -> tuple[
    tuple[Vertex, ...],
    dict[OperationName, dict[Vertex, Vertex]],
    dict[Vertex, Hashable],
]:
    """Compile partial operations to total ones with observable absorbing undefined.

    ``undefined_state`` must be fresh and ``undefined_observation`` must be
    distinct from every ordinary observation label.  The added state is a
    compiler/verification device: it is absorbing for every totalized action
    and represents the fact that a partial word has already become illegal.
    """
    states = _domain(domain)
    family = _partial_operations(states, operations)
    state_set = set(states)
    if set(observation) != state_set:
        raise ValueError("observation must label every state exactly once")
    if undefined_state in state_set:
        raise ValueError("undefined_state must be fresh")
    if undefined_observation in set(observation.values()):
        raise ValueError("undefined_observation must be distinguished")

    augmented = states + (undefined_state,)
    total_operations: dict[OperationName, dict[Vertex, Vertex]] = {}
    for name, operation in family:
        total = {
            state: operation[state] if state in operation else undefined_state
            for state in states
        }
        total[undefined_state] = undefined_state
        total_operations[name] = total

    total_observation = dict(observation)
    total_observation[undefined_state] = undefined_observation
    return augmented, total_operations, total_observation


def partition_refines(
    domain: Iterable[Vertex], finer: Partition, coarser: Partition
) -> bool:
    """Return whether every finer class lies inside one coarser class."""
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


def partitions_equivalent(
    domain: Iterable[Vertex], left: Partition, right: Partition
) -> bool:
    """Return equality of the induced equivalence relations, ignoring labels."""
    states = _domain(domain)
    return partition_refines(states, left, right) and partition_refines(
        states, right, left
    )


def partial_operation_descends(
    domain: Iterable[Vertex],
    operation: PartialOperation,
    partition: Partition,
) -> bool:
    """Whether one partial operation is well-defined on quotient classes.

    Quotient-class members must agree on operation definedness.  If enabled,
    their targets must lie in one quotient class.
    """
    states = _domain(domain)
    state_set = set(states)
    if not set(operation) <= state_set:
        raise ValueError("partial operation domain must lie inside the state domain")
    if any(target not in state_set for target in operation.values()):
        raise ValueError("partial operation targets must lie inside the state domain")
    if set(partition) != state_set:
        raise ValueError("partition must cover every state exactly once")

    class_behavior: dict[Hashable, tuple[bool, Hashable | None]] = {}
    for state in states:
        coarse = partition[state]
        enabled = state in operation
        behavior: tuple[bool, Hashable | None]
        if enabled:
            behavior = (True, partition[operation[state]])
        else:
            behavior = (False, None)
        if coarse in class_behavior and class_behavior[coarse] != behavior:
            return False
        class_behavior[coarse] = behavior
    return True


def partial_family_descends(
    domain: Iterable[Vertex],
    operations: Mapping[OperationName, PartialOperation],
    partition: Partition,
) -> bool:
    """Whether every declared partial operation descends with domain preserved."""
    states = _domain(domain)
    family = _partial_operations(states, operations)
    return all(
        partial_operation_descends(states, operation, partition)
        for _, operation in family
    )


def partial_family_refinement_step(
    domain: Iterable[Vertex],
    operations: Mapping[OperationName, PartialOperation],
    partition: Partition,
) -> dict[Vertex, int]:
    """Refine by current class plus every generator's enabled/target behavior."""
    states = _domain(domain)
    family = _partial_operations(states, operations)
    current = _canonical_ids(states, partition)

    signatures: dict[Vertex, Hashable] = {}
    for state in states:
        generator_signature: list[tuple[bool, int | None]] = []
        for _, operation in family:
            if state in operation:
                generator_signature.append((True, current[operation[state]]))
            else:
                generator_signature.append((False, None))
        signatures[state] = (current[state], tuple(generator_signature))
    return _canonical_ids(states, signatures)


def partial_family_future_partition_sequence(
    domain: Iterable[Vertex],
    operations: Mapping[OperationName, PartialOperation],
    initial_partition: Partition,
) -> tuple[dict[Vertex, int], ...]:
    """Return all distinct partial-family future refinements through stability."""
    states = _domain(domain)
    _partial_operations(states, operations)
    current = _canonical_ids(states, initial_partition)
    stages = [current]

    while True:
        nxt = partial_family_refinement_step(states, operations, current)
        if nxt == current:
            if not partial_family_descends(states, operations, current):
                raise AssertionError("stable partial-family partition is not compatible")
            return tuple(stages)
        if not partition_refines(states, nxt, current):
            raise AssertionError("partial-family refinement must never merge existing classes")
        stages.append(nxt)
        current = nxt
        if len(stages) > len(states):
            raise AssertionError("finite partial-family refinement exceeded the state bound")


def stable_partial_family_partition(
    domain: Iterable[Vertex],
    operations: Mapping[OperationName, PartialOperation],
    initial_partition: Partition,
) -> dict[Vertex, int]:
    """Return the coarsest compatible refinement of the initial observation."""
    return dict(
        partial_family_future_partition_sequence(
            domain, operations, initial_partition
        )[-1]
    )


@dataclass(frozen=True)
class PartialWordResult:
    defined: bool
    state: Vertex | None
    defined_prefix_length: int


def apply_partial_word(
    state: Vertex,
    operations: Mapping[OperationName, PartialOperation],
    word: Iterable[OperationName],
) -> PartialWordResult:
    """Apply one named word until completion or the first disabled prefix."""
    if not operations:
        raise ValueError("operation family must be nonempty")
    current = state
    prefix_length = 0
    for name in word:
        if name not in operations:
            raise ValueError("word contains an operation outside the family")
        operation = operations[name]
        if current not in operation:
            return PartialWordResult(
                defined=False,
                state=None,
                defined_prefix_length=prefix_length,
            )
        current = operation[current]
        prefix_length += 1
    return PartialWordResult(
        defined=True,
        state=current,
        defined_prefix_length=prefix_length,
    )


def partial_word_observation_signature(
    state: Vertex,
    operations: Mapping[OperationName, PartialOperation],
    observation: Partition,
    max_length: int,
) -> tuple[tuple[bool, Hashable | None], ...]:
    """Observation/undefined signature for every named word through one horizon."""
    if max_length < 0:
        raise ValueError("max_length must be nonnegative")
    names = tuple(operations)
    if not names:
        raise ValueError("operation family must be nonempty")
    words = operation_words(names, max_length)
    result: list[tuple[bool, Hashable | None]] = []
    for word in words:
        outcome = apply_partial_word(state, operations, word)
        if not outcome.defined:
            result.append((False, None))
            continue
        if outcome.state not in observation:
            raise ValueError("observation must cover every reached state")
        result.append((True, observation[outcome.state]))
    return tuple(result)


def partial_family_horizon_partition(
    domain: Iterable[Vertex],
    operations: Mapping[OperationName, PartialOperation],
    observation: Partition,
    max_length: int,
) -> dict[Vertex, int]:
    """Partition states by exact legality-sensitive word signatures through ``h``."""
    states = _domain(domain)
    _partial_operations(states, operations)
    if set(observation) != set(states):
        raise ValueError("observation must label every state exactly once")
    signatures = {
        state: partial_word_observation_signature(
            state, operations, observation, max_length
        )
        for state in states
    }
    return _canonical_ids(states, signatures)


def stable_partial_family_is_coarsest_compatible(
    domain: Iterable[Vertex],
    operations: Mapping[OperationName, PartialOperation],
    initial_partition: Partition,
    candidate_partition: Partition,
) -> bool:
    """Check the universal minimality condition against one candidate refinement.

    Returns true exactly when every candidate that both refines the initial
    observation and makes the partial family descend also refines the computed
    stable partition.  Candidates outside those hypotheses make the implication
    vacuously true.
    """
    states = _domain(domain)
    stable = stable_partial_family_partition(
        states, operations, initial_partition
    )
    if not partition_refines(states, candidate_partition, initial_partition):
        return True
    if not partial_family_descends(states, operations, candidate_partition):
        return True
    return partition_refines(states, candidate_partition, stable)
