"""Finite operation/quotient duality helpers for A2.

This module is a bridge over the canonical P023 unary operation-family engine.
For a finite algebra, congruence compatibility with a finitary operation is
completely determined by its elementary unary translations: fix every input
except one, and vary the remaining coordinate.  Compiling all basic finitary
operations to those unary contexts lets ``stable_family_partition`` compute the
coarsest observation refinement that is a congruence for the whole algebra.

The generic congruence fact is classical universal algebra.  The Enterprise
Math use is to connect a declared causal operation language to the P023/P024
future-safe quotient machinery without creating a competing quotient theory.
"""

from __future__ import annotations

from bisect import bisect_right
from collections.abc import Hashable, Iterable, Mapping, Sequence
from itertools import product
from typing import TypeVar

from enterprise_math.operation_quotient import (
    family_descends,
    stable_family_partition,
)

State = TypeVar("State", bound=Hashable)
Label = TypeVar("Label", bound=Hashable)
OperationName = TypeVar("OperationName", bound=Hashable)

FinitaryOperation = Mapping[tuple[State, ...], State]
Partition = Mapping[State, Hashable]


def _domain(domain: Iterable[State]) -> tuple[State, ...]:
    states = tuple(domain)
    if not states:
        raise ValueError("domain must be nonempty")
    if len(states) != len(set(states)):
        raise ValueError("domain states must be distinct")
    return states


def _validated_operation(
    states: tuple[State, ...], operation: FinitaryOperation[State]
) -> int:
    if not operation:
        raise ValueError("finitary operation table must be nonempty")
    arities = {len(inputs) for inputs in operation}
    if len(arities) != 1:
        raise ValueError("all operation-table keys must have the same arity")
    arity = arities.pop()
    if arity < 1:
        raise ValueError("only positive-arity operations are supported")
    expected = set(product(states, repeat=arity))
    if set(operation) != expected:
        raise ValueError("operation table must be total on the finite domain")
    state_set = set(states)
    if any(output not in state_set for output in operation.values()):
        raise ValueError("operation outputs must stay inside the finite domain")
    return arity


def finitary_operation_descends(
    domain: Iterable[State],
    operation: FinitaryOperation[State],
    partition: Partition,
) -> bool:
    """Whether a total finite finitary operation descends through ``partition``."""
    states = _domain(domain)
    arity = _validated_operation(states, operation)
    if set(partition) != set(states):
        raise ValueError("partition must label every state exactly once")

    seen: dict[tuple[Hashable, ...], Hashable] = {}
    for inputs in product(states, repeat=arity):
        coarse_inputs = tuple(partition[state] for state in inputs)
        coarse_output = partition[operation[inputs]]
        if coarse_inputs in seen and seen[coarse_inputs] != coarse_output:
            return False
        seen[coarse_inputs] = coarse_output
    return True


def elementary_translations(
    domain: Iterable[State],
    operations: Mapping[OperationName, FinitaryOperation[State]],
) -> dict[tuple[OperationName, int, tuple[State, ...]], dict[State, State]]:
    """Compile basic finitary operations to all elementary unary translations.

    For an r-ary operation ``f``, coordinate ``i``, and fixed values for the
    other ``r-1`` coordinates, the resulting unary map is

        x -> f(a_0, ..., a_{i-1}, x, a_{i+1}, ..., a_{r-1}).

    A partition is a congruence for every supplied basic operation iff every
    compiled unary translation descends through it.
    """
    states = _domain(domain)
    if not operations:
        raise ValueError("operation family must be nonempty")

    compiled: dict[
        tuple[OperationName, int, tuple[State, ...]], dict[State, State]
    ] = {}
    for name, operation in operations.items():
        arity = _validated_operation(states, operation)
        for coordinate in range(arity):
            for parameters in product(states, repeat=arity - 1):
                unary: dict[State, State] = {}
                for varying in states:
                    parameter_index = 0
                    inputs: list[State] = []
                    for index in range(arity):
                        if index == coordinate:
                            inputs.append(varying)
                        else:
                            inputs.append(parameters[parameter_index])
                            parameter_index += 1
                    unary[varying] = operation[tuple(inputs)]
                compiled[(name, coordinate, tuple(parameters))] = unary
    return compiled


def finitary_family_descends(
    domain: Iterable[State],
    operations: Mapping[OperationName, FinitaryOperation[State]],
    partition: Partition,
) -> bool:
    """Direct congruence test for every basic finitary operation."""
    states = _domain(domain)
    if not operations:
        raise ValueError("operation family must be nonempty")
    return all(
        finitary_operation_descends(states, operation, partition)
        for operation in operations.values()
    )


def elementary_family_descends(
    domain: Iterable[State],
    operations: Mapping[OperationName, FinitaryOperation[State]],
    partition: Partition,
) -> bool:
    """Equivalent congruence test through compiled unary translations."""
    states = _domain(domain)
    translations = elementary_translations(states, operations)
    return family_descends(states, translations, partition)


def stable_finitary_observation_congruence(
    domain: Iterable[State],
    operations: Mapping[OperationName, FinitaryOperation[State]],
    observation: Partition,
) -> dict[State, int]:
    """Largest operation congruence contained in the observation kernel.

    In partition order this is the coarsest refinement of ``observation`` on
    which every supplied finitary operation descends.  It is computed by
    compiling the algebra to elementary unary translations and invoking the
    canonical finite P023 operation-family refinement engine.
    """
    states = _domain(domain)
    translations = elementary_translations(states, operations)
    return stable_family_partition(states, translations, observation)


def interval_level(boundaries: Sequence[int], amount: int) -> int:
    """Level of ``amount`` in a represented P008 interval prefix."""
    values = tuple(boundaries)
    if len(values) < 2:
        raise ValueError("boundaries must contain at least two values")
    if values[0] != 0:
        raise ValueError("represented P008 boundaries must start at zero")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in values
    ):
        raise ValueError("boundaries must be nonnegative integers")
    if any(left >= right for left, right in zip(values, values[1:])):
        raise ValueError("boundaries must be strictly increasing")
    if isinstance(amount, bool) or not isinstance(amount, int):
        raise ValueError("amount must be an integer")
    if amount < 0 or amount >= values[-1]:
        raise ValueError("amount must lie in the represented prefix")
    return bisect_right(values, amount) - 1


def interval_lattice_identity_holds(
    boundaries: Sequence[int], x: int, y: int
) -> bool:
    """Check the exact min/max quotient identities on a represented prefix."""
    qx = interval_level(boundaries, x)
    qy = interval_level(boundaries, y)
    return (
        interval_level(boundaries, min(x, y)) == min(qx, qy)
        and interval_level(boundaries, max(x, y)) == max(qx, qy)
    )
