"""Stable-equivalence calculus for P023 safe-precision selectors.

For a finite deterministic operation family A, ``Safe_A`` is the coarsest
A-compatible refinement of the supplied finite partition.  A single sequential
pass of several selectors may depend on order and may fail common compatibility.
However, every selector is monotone, reductive and idempotent on the finite
partition poset.  Repeating any fixed selector word that contains the desired
operation requirements stabilizes to the common safe precision.

The implementation below treats selector words as tuples of nonempty operation
families.  The canonical stable target is the safe selector of their union.
"""

from __future__ import annotations

from collections.abc import Hashable, Iterable, Mapping, Sequence

from .operation_quotient import family_descends, stable_family_partition

Vertex = Hashable
Operation = Mapping[Vertex, Vertex]
OperationFamily = Mapping[Hashable, Operation]
Partition = Mapping[Vertex, Hashable]


def _states(domain: Iterable[Vertex]) -> tuple[Vertex, ...]:
    states = tuple(domain)
    if not states:
        raise ValueError("domain must be nonempty")
    if len(states) != len(set(states)):
        raise ValueError("domain states must be distinct")
    return states


def _canonical_partition(states: tuple[Vertex, ...], labels: Partition) -> dict[Vertex, int]:
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


def _validated_family(states: tuple[Vertex, ...], family: OperationFamily) -> dict[Hashable, dict[Vertex, Vertex]]:
    if not family:
        raise ValueError("selector operation family must be nonempty")
    state_set = set(states)
    result: dict[Hashable, dict[Vertex, Vertex]] = {}
    for name, operation in family.items():
        if set(operation) != state_set:
            raise ValueError("operation must be total on the domain")
        copied = {state: operation[state] for state in states}
        if any(value not in state_set for value in copied.values()):
            raise ValueError("operation must map the domain into itself")
        result[name] = copied
    return result


def selector_word_union(
    domain: Iterable[Vertex], selector_word: Sequence[OperationFamily]
) -> dict[tuple[int, Hashable], dict[Vertex, Vertex]]:
    """Return a collision-free named union of all operations occurring in a word."""
    states = _states(domain)
    if not selector_word:
        raise ValueError("selector word must be nonempty")
    union: dict[tuple[int, Hashable], dict[Vertex, Vertex]] = {}
    for index, family in enumerate(selector_word):
        validated = _validated_family(states, family)
        for name, operation in validated.items():
            union[(index, name)] = operation
    return union


def selector_word_once(
    domain: Iterable[Vertex],
    selector_word: Sequence[OperationFamily],
    partition: Partition,
) -> dict[Vertex, int]:
    """Apply the coarsest selector for each operation family once, in order."""
    states = _states(domain)
    if not selector_word:
        raise ValueError("selector word must be nonempty")
    current = _canonical_partition(states, partition)
    for family in selector_word:
        current = stable_family_partition(states, _validated_family(states, family), current)
    return current


def selector_word_sequence(
    domain: Iterable[Vertex],
    selector_word: Sequence[OperationFamily],
    partition: Partition,
) -> tuple[dict[Vertex, int], ...]:
    """Repeat one fixed selector word through its first stable partition."""
    states = _states(domain)
    union = selector_word_union(states, selector_word)
    current = _canonical_partition(states, partition)
    stages = [current]
    while True:
        nxt = selector_word_once(states, selector_word, current)
        if nxt == current:
            if not family_descends(states, union, current):
                raise AssertionError("stable selector word is not common-compatible")
            return tuple(stages)
        if len(set(nxt.values())) <= len(set(current.values())):
            raise AssertionError("strict selector-word progress must increase class count")
        stages.append(nxt)
        current = nxt
        if len(stages) > len(states):
            raise AssertionError("finite selector-word stabilization exceeded class bound")


def stable_selector_word(
    domain: Iterable[Vertex],
    selector_word: Sequence[OperationFamily],
    partition: Partition,
) -> dict[Vertex, int]:
    """Stable value of repeated application of one selector word."""
    return selector_word_sequence(domain, selector_word, partition)[-1]


def joint_safe_partition(
    domain: Iterable[Vertex],
    selector_word: Sequence[OperationFamily],
    partition: Partition,
) -> dict[Vertex, int]:
    """Coarsest refinement supporting every operation that occurs in the word."""
    states = _states(domain)
    union = selector_word_union(states, selector_word)
    return stable_family_partition(states, union, partition)


def selector_word_stable_equivalence_holds(
    domain: Iterable[Vertex],
    selector_word: Sequence[OperationFamily],
    partition: Partition,
) -> bool:
    """Audit that repeated selector-word action equals the joint safe selector."""
    states = _states(domain)
    left = stable_selector_word(states, selector_word, partition)
    right = joint_safe_partition(states, selector_word, partition)
    return all((left[x] == left[y]) == (right[x] == right[y]) for x in states for y in states)


def selector_word_fixed_iff_common_compatible(
    domain: Iterable[Vertex],
    selector_word: Sequence[OperationFamily],
    partition: Partition,
) -> bool:
    """Check the fixed-point characterization for one finite input partition."""
    states = _states(domain)
    current = _canonical_partition(states, partition)
    once = selector_word_once(states, selector_word, current)
    union = selector_word_union(states, selector_word)
    return (once == current) == family_descends(states, union, current)
