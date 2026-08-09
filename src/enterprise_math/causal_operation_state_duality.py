"""How much of a finite state quotient is recoverable from its full safe monoid.

For an equivalence partition E on X, Safe(E) is the full monoid of endomaps that
preserve E.  Distinct equivalence relations have distinct full safe monoids,
except for the two extreme partitions: discrete equality and indiscrete total
collapse both admit every raw endomap.

Consequently, once a nonconstant current observation is fixed, every admissible
future-state partition refines its non-universal observation kernel; the
indiscrete extreme is excluded, and the full zero-cost operation envelope
uniquely determines the state partition.

This is a semantic reconstruction theorem.  A physically declared operation
language is usually only a subset of Safe(E), so a small observed operation set
need not determine E uniquely.
"""

from __future__ import annotations

from typing import Hashable, Mapping

from .causal_operation_language import Partition, generator_respects_partition

State = Hashable
Observation = Hashable


def _class_count(partition: Partition) -> int:
    return len(set(partition.values()))


def _same_partition(left: Partition, right: Partition) -> bool:
    if set(left) != set(right):
        return False
    states = tuple(left)
    return all(
        (left[a] == left[b]) == (right[a] == right[b])
        for a in states
        for b in states
    )


def _block_constant_map(
    states: tuple[State, ...],
    partition: Partition,
    class_targets: dict[int, State],
) -> dict[State, State]:
    return {state: class_targets[partition[state]] for state in states}


def _different_class_pair(states: tuple[State, ...], partition: Partition) -> tuple[State, State] | None:
    for left in states:
        for right in states:
            if partition[left] != partition[right]:
                return left, right
    return None


def _same_class_pair(states: tuple[State, ...], partition: Partition) -> tuple[State, State] | None:
    for index, left in enumerate(states):
        for right in states[index + 1 :]:
            if partition[left] == partition[right]:
                return left, right
    return None


def safe_monoid_separator(
    states: tuple[State, ...],
    left: Partition,
    right: Partition,
) -> tuple[str, dict[State, State]] | None:
    """Construct a map preserving exactly one of two distinct partitions.

    Returns `("left_only", f)` or `("right_only", f)`.  Returns None exactly for
    equal partitions or for the discrete/indiscrete extreme pair, whose full safe
    endomorphism monoids are both the set of all raw maps.
    """
    if set(left) != set(states) or set(right) != set(states):
        raise ValueError("partitions must cover the state set")
    if _same_partition(left, right):
        return None

    n = len(states)
    left_classes = _class_count(left)
    right_classes = _class_count(right)
    left_discrete = left_classes == n
    right_discrete = right_classes == n
    left_indiscrete = left_classes == 1
    right_indiscrete = right_classes == 1
    if (left_discrete and right_indiscrete) or (right_discrete and left_indiscrete):
        return None

    # If a pair is merged by left but split by right, a right-block-constant map
    # can preserve right while sending that pair to different left classes.
    for a in states:
        for b in states:
            if left[a] == left[b] and right[a] != right[b]:
                images = _different_class_pair(states, left)
                if images is not None:
                    u, v = images
                    targets = {class_id: u for class_id in set(right.values())}
                    targets[right[b]] = v
                    mapping = _block_constant_map(states, right, targets)
                    if generator_respects_partition(states, right, mapping) and not generator_respects_partition(states, left, mapping):
                        return "right_only", mapping

    # Symmetric case.
    for a in states:
        for b in states:
            if right[a] == right[b] and left[a] != left[b]:
                images = _different_class_pair(states, right)
                if images is not None:
                    u, v = images
                    targets = {class_id: u for class_id in set(left.values())}
                    targets[left[b]] = v
                    mapping = _block_constant_map(states, left, targets)
                    if generator_respects_partition(states, left, mapping) and not generator_respects_partition(states, right, mapping):
                        return "left_only", mapping

    # One partition may be indiscrete: all raw maps preserve it.  Unless the other
    # is discrete (the unique degeneracy above), choose any map that splits one of
    # the other's non-singleton blocks across two of its classes.
    if left_indiscrete and not right_discrete:
        pair = _same_class_pair(states, right)
        images = _different_class_pair(states, right)
        if pair is not None and images is not None:
            a, b = pair
            u, v = images
            mapping = {state: u for state in states}
            mapping[b] = v
            if not generator_respects_partition(states, right, mapping):
                return "left_only", mapping

    if right_indiscrete and not left_discrete:
        pair = _same_class_pair(states, left)
        images = _different_class_pair(states, left)
        if pair is not None and images is not None:
            a, b = pair
            u, v = images
            mapping = {state: u for state in states}
            mapping[b] = v
            if not generator_respects_partition(states, left, mapping):
                return "right_only", mapping

    raise AssertionError("distinct non-extreme equivalences must have different safe monoids")


def refines_observation_kernel(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    partition: Partition,
) -> bool:
    if set(observation) != set(states) or set(partition) != set(states):
        raise ValueError("observation and partition must cover the state set")
    return all(
        partition[a] != partition[b] or observation[a] == observation[b]
        for a in states
        for b in states
    )


def observation_removes_safe_monoid_degeneracy(
    states: tuple[State, ...],
    observation: Mapping[State, Observation],
    left: Partition,
    right: Partition,
) -> bool:
    """Finite theorem check for nonconstant O and O-refining partitions.

    If the partitions are distinct and both preserve current observation, a safe
    monoid separator must exist; the discrete/indiscrete degeneracy is impossible
    because a nonconstant observation forbids the indiscrete partition.
    """
    if len(set(observation.values())) < 2:
        raise ValueError("observation must be nonconstant")
    if not refines_observation_kernel(states, observation, left) or not refines_observation_kernel(states, observation, right):
        raise ValueError("partitions must refine the current observation kernel")
    if _same_partition(left, right):
        return True
    return safe_monoid_separator(states, left, right) is not None
