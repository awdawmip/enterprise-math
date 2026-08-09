"""Reusable exact interface boundary for P018 transport models.

A transient one-step correction token and a self-contained state interface solve
different information problems.  This module audits the second model.

An interface map I : X -> Z is reusable for a declared operation language when:
1. the raw observation O factors through I, so I never identifies states that O
   distinguishes; and
2. the kernel partition of I is a congruence for every declared operation.

Any such kernel is a congruence inside ker(O), hence it must refine the canonical
contextual closure, which is the greatest congruence contained in ker(O).
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Callable, Hashable, Iterable, Sequence
from typing import TypeVar

from enterprise_math.contextual_closure import (
    FiniteOperation,
    contextual_closure_partition,
    partition_is_signature_congruence,
)
from enterprise_math.predictive_closure import partition_refines

State = TypeVar("State", bound=Hashable)
Observation = TypeVar("Observation", bound=Hashable)
Interface = TypeVar("Interface", bound=Hashable)

Partition = frozenset[frozenset[State]]


def _states_tuple(states: Iterable[State]) -> tuple[State, ...]:
    materialized = tuple(states)
    if not materialized:
        raise ValueError("states must be nonempty")
    if len(set(materialized)) != len(materialized):
        raise ValueError("states must be distinct labels")
    return materialized


def interface_partition(
    states: Iterable[State], interface: Callable[[State], Interface]
) -> Partition[State]:
    materialized = _states_tuple(states)
    blocks: dict[Interface, set[State]] = defaultdict(set)
    for state in materialized:
        blocks[interface(state)].add(state)
    return frozenset(frozenset(block) for block in blocks.values())


def observation_factors_through_interface(
    states: Iterable[State],
    observation: Callable[[State], Observation],
    interface: Callable[[State], Interface],
) -> bool:
    """Check ker(I) subseteq ker(O)."""
    partition = interface_partition(states, interface)
    for block in partition:
        outputs = {observation(state) for state in block}
        if len(outputs) != 1:
            return False
    return True


def reusable_exact_interface(
    states: Iterable[State],
    operations: Sequence[FiniteOperation[State]],
    observation: Callable[[State], Observation],
    interface: Callable[[State], Interface],
) -> bool:
    """Whether I is a self-contained exact state interface for the signature."""
    materialized = _states_tuple(states)
    partition = interface_partition(materialized, interface)
    return observation_factors_through_interface(
        materialized, observation, interface
    ) and partition_is_signature_congruence(materialized, tuple(operations), partition)


def reusable_interface_refines_contextual_closure(
    states: Iterable[State],
    operations: Sequence[FiniteOperation[State]],
    observation: Callable[[State], Observation],
    interface: Callable[[State], Interface],
) -> bool:
    """Audit the T175 access-model theorem for one candidate interface."""
    materialized = _states_tuple(states)
    if not reusable_exact_interface(materialized, operations, observation, interface):
        raise ValueError("candidate interface is not an exact reusable interface")
    candidate = interface_partition(materialized, interface)
    canonical = contextual_closure_partition(materialized, tuple(operations), observation)
    return partition_refines(candidate, canonical)


def reusable_interface_state_count(
    states: Iterable[State], interface: Callable[[State], Interface]
) -> int:
    return len(interface_partition(states, interface))


def canonical_reusable_state_count(
    states: Iterable[State],
    operations: Sequence[FiniteOperation[State]],
    observation: Callable[[State], Observation],
) -> int:
    materialized = _states_tuple(states)
    return len(contextual_closure_partition(materialized, tuple(operations), observation))
