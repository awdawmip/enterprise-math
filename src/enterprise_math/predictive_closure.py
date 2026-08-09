"""Canonical finite predictive closure of a deterministic observation partition.

For a finite deterministic endomap F : X -> X and observation O : X -> Y,
define the horizon-n signature of x by

    (O(x), O(F x), ..., O(F^n x)).

Equal signatures give a descending sequence of equivalence relations.  Once two
successive partitions agree, the sequence is permanently stable; the stable
relation is the largest F-compatible equivalence contained in ker(O).  Its
quotient is therefore the coarsest exact dynamically closed refinement of the
original observation partition.

This is classical finite-state / automata-style behavioral refinement.  The
module exists to pressure-test its exact Enterprise Math finite-precision role.
"""

from __future__ import annotations

from collections.abc import Callable, Hashable, Iterable
from typing import TypeVar

State = TypeVar("State", bound=Hashable)
Output = TypeVar("Output", bound=Hashable)


def _states_tuple(states: Iterable[State]) -> tuple[State, ...]:
    materialized = tuple(states)
    if not materialized:
        raise ValueError("states must be nonempty")
    if len(set(materialized)) != len(materialized):
        raise ValueError("states must be distinct labels")
    return materialized


def _check_endomap(states: tuple[State, ...], operation: Callable[[State], State]) -> None:
    domain = set(states)
    for state in states:
        if operation(state) not in domain:
            raise ValueError("operation must map the finite state set to itself")


def trace_signature(
    operation: Callable[[State], State],
    observation: Callable[[State], Output],
    state: State,
    horizon: int,
) -> tuple[Output, ...]:
    """Observable future trace through time ``0..horizon`` inclusive."""
    if isinstance(horizon, bool) or not isinstance(horizon, int) or horizon < 0:
        raise ValueError("horizon must be a non-negative integer")
    current = state
    signature: list[Output] = []
    for _ in range(horizon + 1):
        signature.append(observation(current))
        current = operation(current)
    return tuple(signature)


def horizon_partition(
    states: Iterable[State],
    operation: Callable[[State], State],
    observation: Callable[[State], Output],
    horizon: int,
) -> frozenset[frozenset[State]]:
    """Partition states by equality of observable traces through ``horizon``."""
    materialized = _states_tuple(states)
    _check_endomap(materialized, operation)
    blocks: dict[tuple[Output, ...], set[State]] = {}
    for state in materialized:
        signature = trace_signature(operation, observation, state, horizon)
        blocks.setdefault(signature, set()).add(state)
    return frozenset(frozenset(block) for block in blocks.values())


def observation_partition(
    states: Iterable[State], observation: Callable[[State], Output]
) -> frozenset[frozenset[State]]:
    """The original precision/observation partition ``ker(O)``."""
    materialized = _states_tuple(states)
    blocks: dict[Output, set[State]] = {}
    for state in materialized:
        blocks.setdefault(observation(state), set()).add(state)
    return frozenset(frozenset(block) for block in blocks.values())


def block_map(partition: frozenset[frozenset[State]]) -> dict[State, frozenset[State]]:
    """Map each state label to its unique block."""
    result: dict[State, frozenset[State]] = {}
    for block in partition:
        if not block:
            raise ValueError("partition blocks must be nonempty")
        for state in block:
            if state in result:
                raise ValueError("partition blocks must be disjoint")
            result[state] = block
    return result


def partition_refines(
    finer: frozenset[frozenset[State]],
    coarser: frozenset[frozenset[State]],
) -> bool:
    """Whether every finer block is contained in one coarser block."""
    coarse_of = block_map(coarser)
    for block in finer:
        representative = next(iter(block))
        target = coarse_of.get(representative)
        if target is None or not block <= target:
            return False
    return True


def partition_is_forward_compatible(
    partition: frozenset[frozenset[State]],
    operation: Callable[[State], State],
) -> bool:
    """Whether block equivalence is a congruence for one deterministic endomap."""
    state_to_block = block_map(partition)
    for block in partition:
        target_blocks = {
            state_to_block.get(operation(state))
            for state in block
        }
        if None in target_blocks or len(target_blocks) != 1:
            return False
    return True


def first_stable_horizon(
    states: Iterable[State],
    operation: Callable[[State], State],
    observation: Callable[[State], Output],
) -> tuple[int, frozenset[frozenset[State]]]:
    """First horizon where one more observable step no longer refines the partition.

    For ``N`` finite states and ``c0`` initial observation blocks, stabilization
    must occur by horizon ``N-c0``: every strict refinement adds at least one
    block, and equality is itself forward compatible.
    """
    materialized = _states_tuple(states)
    _check_endomap(materialized, operation)
    current = horizon_partition(materialized, operation, observation, 0)
    bound = len(materialized) - len(current)
    for horizon in range(bound + 1):
        following = horizon_partition(
            materialized, operation, observation, horizon + 1
        )
        if following == current:
            return horizon, current
        if not partition_refines(following, current):
            raise AssertionError("future-trace partition failed to refine monotonically")
        current = following
    raise AssertionError("finite predictive refinement exceeded N-c0 bound")


def predictive_closure_partition(
    states: Iterable[State],
    operation: Callable[[State], State],
    observation: Callable[[State], Output],
) -> frozenset[frozenset[State]]:
    """The coarsest forward-compatible refinement of the observation partition."""
    return first_stable_horizon(states, operation, observation)[1]


def candidate_is_observation_respecting(
    partition: frozenset[frozenset[State]],
    observation: Callable[[State], Output],
) -> bool:
    """Whether every candidate block lies in one original observation fiber."""
    for block in partition:
        outputs = {observation(state) for state in block}
        if len(outputs) != 1:
            return False
    return True


def candidate_refines_predictive_closure(
    states: Iterable[State],
    operation: Callable[[State], State],
    observation: Callable[[State], Output],
    candidate: frozenset[frozenset[State]],
) -> bool:
    """Executable maximality check for an exact dynamically closed candidate.

    If ``candidate`` respects the original observation and is forward compatible,
    it must refine the canonical predictive closure.  Invalid candidates return
    ``False`` rather than asserting the theorem's premise.
    """
    materialized = _states_tuple(states)
    if set(block_map(candidate)) != set(materialized):
        return False
    if not candidate_is_observation_respecting(candidate, observation):
        return False
    if not partition_is_forward_compatible(candidate, operation):
        return False
    closure = predictive_closure_partition(materialized, operation, observation)
    return partition_refines(candidate, closure)


def quotient_transition(
    partition: frozenset[frozenset[State]],
    operation: Callable[[State], State],
) -> dict[frozenset[State], frozenset[State]]:
    """Descended deterministic dynamics on a forward-compatible partition."""
    if not partition_is_forward_compatible(partition, operation):
        raise ValueError("partition is not forward compatible")
    state_to_block = block_map(partition)
    result: dict[frozenset[State], frozenset[State]] = {}
    for block in partition:
        representative = next(iter(block))
        target = state_to_block.get(operation(representative))
        if target is None:
            raise ValueError("operation leaves the partition domain")
        result[block] = target
    return result


def quotient_observation(
    partition: frozenset[frozenset[State]],
    observation: Callable[[State], Output],
) -> dict[frozenset[State], Output]:
    """Well-defined original output on any observation-respecting refinement."""
    if not candidate_is_observation_respecting(partition, observation):
        raise ValueError("partition does not refine the observation kernel")
    return {
        block: observation(next(iter(block)))
        for block in partition
    }
