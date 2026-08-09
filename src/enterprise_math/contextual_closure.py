"""Finite contextual congruence closure for P018 multi-ary precision states.

Given a finite algebraic signature and an observation partition, repeatedly split
observation blocks by all elementary one-hole translations of the basic
operations.  The first stable partition is the greatest congruence contained in
the original observation equivalence, i.e. the canonical coarsest exact quotient
refinement supporting every operation in the signature.

The general congruence / syntactic-congruence machinery is classical universal
algebra.  This module pressure-tests the finite-precision interface used by P018.
"""

from __future__ import annotations

from collections.abc import Callable, Hashable, Iterable, Sequence
from dataclasses import dataclass
from itertools import product
from typing import Generic, TypeVar

from enterprise_math.predictive_closure import (
    block_map,
    candidate_is_observation_respecting,
    observation_partition,
    partition_refines,
)

State = TypeVar("State", bound=Hashable)
Output = TypeVar("Output", bound=Hashable)


@dataclass(frozen=True)
class FiniteOperation(Generic[State]):
    """One finitary basic operation on a finite state set."""

    name: str
    arity: int
    function: Callable[[tuple[State, ...]], State]

    def __post_init__(self) -> None:
        if not self.name:
            raise ValueError("operation name must be nonempty")
        if isinstance(self.arity, bool) or not isinstance(self.arity, int):
            raise ValueError("operation arity must be an integer")
        if self.arity < 0:
            raise ValueError("operation arity must be non-negative")

    def apply(self, args: tuple[State, ...]) -> State:
        if len(args) != self.arity:
            raise ValueError("argument tuple has wrong arity")
        return self.function(args)


def _states_tuple(states: Iterable[State]) -> tuple[State, ...]:
    materialized = tuple(states)
    if not materialized:
        raise ValueError("states must be nonempty")
    if len(set(materialized)) != len(materialized):
        raise ValueError("states must be distinct labels")
    return materialized


def _operations_tuple(
    operations: Sequence[FiniteOperation[State]],
) -> tuple[FiniteOperation[State], ...]:
    materialized = tuple(operations)
    names = [operation.name for operation in materialized]
    if len(names) != len(set(names)):
        raise ValueError("operation names must be unique")
    return materialized


def _check_operations(
    states: tuple[State, ...], operations: tuple[FiniteOperation[State], ...]
) -> None:
    domain = set(states)
    for operation in operations:
        for args in product(states, repeat=operation.arity):
            if operation.apply(tuple(args)) not in domain:
                raise ValueError(
                    f"operation {operation.name!r} must map the finite state set to itself"
                )


def _elementary_contexts(
    states: tuple[State, ...], operations: tuple[FiniteOperation[State], ...]
) -> tuple[Callable[[State], State], ...]:
    """All one-hole translations of the basic operations with fixed parameters."""
    contexts: list[Callable[[State], State]] = []
    for operation in operations:
        if operation.arity == 0:
            continue
        for coordinate in range(operation.arity):
            for parameters in product(states, repeat=operation.arity - 1):
                fixed = tuple(parameters)

                def context(
                    state: State,
                    *,
                    op: FiniteOperation[State] = operation,
                    slot: int = coordinate,
                    params: tuple[State, ...] = fixed,
                ) -> State:
                    args: list[State] = []
                    parameter_index = 0
                    for index in range(op.arity):
                        if index == slot:
                            args.append(state)
                        else:
                            args.append(params[parameter_index])
                            parameter_index += 1
                    return op.apply(tuple(args))

                contexts.append(context)
    return tuple(contexts)


def contextual_refine_once(
    states: Iterable[State],
    operations: Sequence[FiniteOperation[State]],
    partition: frozenset[frozenset[State]],
) -> frozenset[frozenset[State]]:
    """Apply one elementary-context refinement step to an equivalence partition."""
    materialized = _states_tuple(states)
    ops = _operations_tuple(operations)
    _check_operations(materialized, ops)
    state_to_block = block_map(partition)
    if set(state_to_block) != set(materialized):
        raise ValueError("partition must cover exactly the finite state set")
    contexts = _elementary_contexts(materialized, ops)

    blocks: dict[tuple[frozenset[State], ...], set[State]] = {}
    for state in materialized:
        signature = (state_to_block[state],) + tuple(
            state_to_block[context(state)] for context in contexts
        )
        blocks.setdefault(signature, set()).add(state)
    return frozenset(frozenset(block) for block in blocks.values())


def partition_is_signature_congruence(
    states: Iterable[State],
    operations: Sequence[FiniteOperation[State]],
    partition: frozenset[frozenset[State]],
) -> bool:
    """Whether the partition is compatible with every basic operation."""
    materialized = _states_tuple(states)
    try:
        return contextual_refine_once(materialized, operations, partition) == partition
    except ValueError:
        return False


def first_stable_context_depth(
    states: Iterable[State],
    operations: Sequence[FiniteOperation[State]],
    observation: Callable[[State], Output],
) -> tuple[int, frozenset[frozenset[State]]]:
    """First fixed point of elementary-context refinement.

    If ``N`` is the number of fine states and ``c0`` the number of original
    observation blocks, each strict refinement adds at least one block, so the
    first fixed point occurs by depth ``N-c0``.
    """
    materialized = _states_tuple(states)
    ops = _operations_tuple(operations)
    _check_operations(materialized, ops)
    current = observation_partition(materialized, observation)
    bound = len(materialized) - len(current)
    for depth in range(bound + 1):
        following = contextual_refine_once(materialized, ops, current)
        if following == current:
            return depth, current
        if not partition_refines(following, current):
            raise AssertionError("context refinement failed to refine monotonically")
        current = following
    raise AssertionError("finite contextual closure exceeded N-c0 bound")


def contextual_closure_partition(
    states: Iterable[State],
    operations: Sequence[FiniteOperation[State]],
    observation: Callable[[State], Output],
) -> frozenset[frozenset[State]]:
    """Greatest operation congruence contained in the observation equivalence."""
    return first_stable_context_depth(states, operations, observation)[1]


def candidate_refines_contextual_closure(
    states: Iterable[State],
    operations: Sequence[FiniteOperation[State]],
    observation: Callable[[State], Output],
    candidate: frozenset[frozenset[State]],
) -> bool:
    """Executable maximality test for a proposed exact quotient refinement."""
    materialized = _states_tuple(states)
    if set(block_map(candidate)) != set(materialized):
        return False
    if not candidate_is_observation_respecting(candidate, observation):
        return False
    if not partition_is_signature_congruence(materialized, operations, candidate):
        return False
    closure = contextual_closure_partition(materialized, operations, observation)
    return partition_refines(candidate, closure)


def quotient_operation_tables(
    states: Iterable[State],
    operations: Sequence[FiniteOperation[State]],
    partition: frozenset[frozenset[State]],
) -> dict[
    str,
    dict[tuple[frozenset[State], ...], frozenset[State]],
]:
    """Exact descended operation tables on a congruent quotient partition."""
    materialized = _states_tuple(states)
    ops = _operations_tuple(operations)
    if not partition_is_signature_congruence(materialized, ops, partition):
        raise ValueError("partition is not a congruence for the operation signature")
    state_to_block = block_map(partition)
    tables: dict[
        str,
        dict[tuple[frozenset[State], ...], frozenset[State]],
    ] = {}
    for operation in ops:
        table: dict[tuple[frozenset[State], ...], frozenset[State]] = {}
        blocks = tuple(partition)
        for block_args in product(blocks, repeat=operation.arity):
            representatives = tuple(next(iter(block)) for block in block_args)
            result_state = operation.apply(representatives)
            table[tuple(block_args)] = state_to_block[result_state]
        tables[operation.name] = table
    return tables


def partition_meet(
    states: Iterable[State],
    partitions: Sequence[frozenset[frozenset[State]]],
) -> frozenset[frozenset[State]]:
    """Intersection/meet of equivalence partitions on one finite state set."""
    materialized = _states_tuple(states)
    if not partitions:
        return frozenset({frozenset(materialized)})
    maps = [block_map(partition) for partition in partitions]
    if any(set(mapping) != set(materialized) for mapping in maps):
        raise ValueError("every partition must cover exactly the finite state set")
    grouped: dict[tuple[frozenset[State], ...], set[State]] = {}
    for state in materialized:
        signature = tuple(mapping[state] for mapping in maps)
        grouped.setdefault(signature, set()).add(state)
    return frozenset(frozenset(block) for block in grouped.values())


def minimal_uniform_detail_size(
    states: Iterable[State],
    operations: Sequence[FiniteOperation[State]],
    observation: Callable[[State], Output],
) -> int:
    """Minimum uniform detail-alphabet size for a pair ``(O(x), detail(x))``.

    Within each original observation fiber, distinct contextual-closure blocks
    must receive distinct detail labels.  Labels may be reused across different
    observation fibers, so the optimum is the largest number of closure blocks
    occurring inside any one observation fiber.
    """
    materialized = _states_tuple(states)
    closure = contextual_closure_partition(materialized, operations, observation)
    counts: dict[Output, int] = {}
    for block in closure:
        output = observation(next(iter(block)))
        counts[output] = counts.get(output, 0) + 1
    return max(counts.values(), default=0)


def floor_quotient_addition_separator(radix: int, x: int, y: int) -> int:
    """Return an additive context separating two distinct states in one Q_r fiber.

    For ``x < y`` with ``x//r == y//r``, the context ``z -> z+t`` with
    ``t = r-1-(x mod r)`` keeps ``x`` in its original quotient cell and moves
    ``y`` into the next cell.  Thus exact addition forces all ``r`` residues to
    remain distinguishable inside every full quotient fiber.
    """
    if isinstance(radix, bool) or not isinstance(radix, int) or radix < 2:
        raise ValueError("radix must be an integer at least two")
    if isinstance(x, bool) or isinstance(y, bool) or not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("states must be integers")
    if x < 0 or y < 0 or x >= y:
        raise ValueError("require natural states with x < y")
    if x // radix != y // radix:
        raise ValueError("states must lie in the same quotient fiber")
    return radix - 1 - (x % radix)
