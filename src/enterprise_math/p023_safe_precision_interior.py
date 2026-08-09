"""Stage-2 safe-precision selector for Enterprise Math P023.

This module keeps two levels distinct:

1. a finite equivalence relation is the actual coarse-state quotient;
2. a labeled partition is only one convenient representation of that relation.

For a finite family of deterministic operations, the relation step

    Phi(E) = E ∩ ⋂_a (F_a × F_a)^(-1)(E)

is monotone and reductive under relation inclusion.  Its fixed points are exactly
operation-compatible quotients.  Finite iteration therefore selects the largest
compatible relation contained in the initial observation relation, matching the
partition-refinement implementation already used by P023.

The module also records the special simplification for an idempotent operation:
`(q(x), q(T(x)))` is already the full coarsest T-compatible repair of q.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping

from .operation_quotient import operation_descends, stable_family_partition

Vertex = Hashable
OperationName = Hashable
Operation = Mapping[Vertex, Vertex]
Partition = Mapping[Vertex, Hashable]
Relation = frozenset[tuple[Vertex, Vertex]]


def _states(domain: Iterable[Vertex]) -> tuple[Vertex, ...]:
    states = tuple(domain)
    if not states:
        raise ValueError("domain must be nonempty")
    if len(states) != len(set(states)):
        raise ValueError("domain states must be distinct")
    return states


def _canonical_partition(states: tuple[Vertex, ...], labels: Mapping[Vertex, Hashable]) -> dict[Vertex, int]:
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


def partition_relation(domain: Iterable[Vertex], partition: Partition) -> Relation:
    """Return the equivalence relation represented by a finite partition."""
    states = _states(domain)
    labels = _canonical_partition(states, partition)
    return frozenset(
        (left, right)
        for left in states
        for right in states
        if labels[left] == labels[right]
    )


def is_equivalence_relation(domain: Iterable[Vertex], relation: Relation) -> bool:
    states = _states(domain)
    state_set = set(states)
    if any(left not in state_set or right not in state_set for left, right in relation):
        return False
    if any((state, state) not in relation for state in states):
        return False
    if any((right, left) not in relation for left, right in relation):
        return False
    for left in states:
        for middle in states:
            if (left, middle) not in relation:
                continue
            for right in states:
                if (middle, right) in relation and (left, right) not in relation:
                    return False
    return True


def relation_partition(domain: Iterable[Vertex], relation: Relation) -> dict[Vertex, int]:
    """Return canonical class IDs for an explicit finite equivalence relation."""
    states = _states(domain)
    if not is_equivalence_relation(states, relation):
        raise ValueError("relation must be an equivalence relation on the domain")
    result: dict[Vertex, int] = {}
    class_id = 0
    for state in states:
        if state in result:
            continue
        members = [other for other in states if (state, other) in relation]
        for member in members:
            result[member] = class_id
        class_id += 1
    return result


def relation_compatible(
    domain: Iterable[Vertex], operations: Mapping[OperationName, Operation], relation: Relation
) -> bool:
    """Whether every operation preserves relatedness."""
    states = _states(domain)
    if not is_equivalence_relation(states, relation):
        raise ValueError("relation must be an equivalence relation")
    state_set = set(states)
    if not operations:
        raise ValueError("operation family must be nonempty")
    for operation in operations.values():
        if set(operation) != state_set or any(operation[state] not in state_set for state in states):
            raise ValueError("operations must be total endomaps of the domain")
        for left, right in relation:
            if (operation[left], operation[right]) not in relation:
                return False
    return True


def safe_relation_step(
    domain: Iterable[Vertex], operations: Mapping[OperationName, Operation], relation: Relation
) -> Relation:
    """Apply Phi(E)=E intersect every operation preimage of E."""
    states = _states(domain)
    if not is_equivalence_relation(states, relation):
        raise ValueError("relation must be an equivalence relation")
    if not operations:
        raise ValueError("operation family must be nonempty")
    state_set = set(states)
    for operation in operations.values():
        if set(operation) != state_set or any(operation[state] not in state_set for state in states):
            raise ValueError("operations must be total endomaps of the domain")
    return frozenset(
        (left, right)
        for left, right in relation
        if all((operation[left], operation[right]) in relation for operation in operations.values())
    )


def safe_relation_sequence(
    domain: Iterable[Vertex], operations: Mapping[OperationName, Operation], initial: Relation
) -> tuple[Relation, ...]:
    """Iterate the reductive relation step through its first fixed point."""
    states = _states(domain)
    if not is_equivalence_relation(states, initial):
        raise ValueError("initial relation must be an equivalence relation")
    current = initial
    stages = [current]
    while True:
        nxt = safe_relation_step(states, operations, current)
        if not nxt.issubset(current):
            raise AssertionError("safe relation step must be reductive")
        if not is_equivalence_relation(states, nxt):
            raise AssertionError("safe relation step must preserve equivalence relations")
        if nxt == current:
            return tuple(stages)
        stages.append(nxt)
        current = nxt
        if len(stages) > len(states):
            raise AssertionError("finite relation refinement exceeded the class bound")


def safe_relation_selector(
    domain: Iterable[Vertex], operations: Mapping[OperationName, Operation], initial: Relation
) -> Relation:
    """Largest common-compatible equivalence relation contained in ``initial``."""
    return safe_relation_sequence(domain, operations, initial)[-1]


def safe_partition_selector(
    domain: Iterable[Vertex], operations: Mapping[OperationName, Operation], initial: Partition
) -> dict[Vertex, int]:
    """Relation-level selector expressed again as canonical partition labels."""
    states = _states(domain)
    relation = safe_relation_selector(states, operations, partition_relation(states, initial))
    result = relation_partition(states, relation)
    expected = stable_family_partition(states, operations, initial)
    if partition_relation(states, result) != partition_relation(states, expected):
        raise AssertionError("relation selector disagrees with P023 partition refinement")
    return result


def is_idempotent(domain: Iterable[Vertex], operation: Operation) -> bool:
    states = _states(domain)
    state_set = set(states)
    if set(operation) != state_set or any(operation[state] not in state_set for state in states):
        raise ValueError("operation must be a total endomap")
    return all(operation[operation[state]] == operation[state] for state in states)


def idempotent_safe_repair(
    domain: Iterable[Vertex], operation: Operation, coarse: Partition
) -> dict[Vertex, int]:
    """Full coarsest repair `(q,q∘T)` for one idempotent operation."""
    states = _states(domain)
    if not is_idempotent(states, operation):
        raise ValueError("operation must be idempotent")
    current = _canonical_partition(states, coarse)
    signatures = {
        state: (current[state], current[operation[state]])
        for state in states
    }
    repaired = _canonical_partition(states, signatures)
    if not operation_descends(states, operation, repaired):
        raise AssertionError("idempotent one-step repair must already be fully compatible")
    expected = stable_family_partition(states, {"T": operation}, current)
    if partition_relation(states, repaired) != partition_relation(states, expected):
        raise AssertionError("idempotent one-step repair is not the coarsest full repair")
    return repaired


def sequential_single_operation_pass(
    domain: Iterable[Vertex],
    operations: tuple[Operation, ...],
    initial: Partition,
) -> dict[Vertex, int]:
    """Apply each single-operation safe selector once, in the supplied order.

    This is deliberately *not* the canonical family selector.  It exists to
    expose the Stage-2 no-go: one pass can break compatibility with an operation
    processed earlier, so simultaneous/iterated family closure is essential.
    """
    states = _states(domain)
    current = _canonical_partition(states, initial)
    for index, operation in enumerate(operations):
        current = stable_family_partition(states, {index: operation}, current)
    return current
