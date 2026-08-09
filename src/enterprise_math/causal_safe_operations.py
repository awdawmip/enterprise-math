"""Operations that genuinely descend through a finite causal quotient.

A coarse state is not characterized only by which raw states it identifies.  It
also determines which future operations remain well-defined after that
identification.  For a finite quotient q:X->Q, an endomap F:X->X is safe iff

    q(x)=q(y) => q(F(x))=q(F(y)).

Safe endomaps contain identity and are closed under composition.  Thus every
quotient generates its own monoid of legal coarse operations; the induced map on
Q is uniquely determined.

This is the finite executable specialization of the general P023 congruence /
factorization criterion.  The project interpretation is important: a proposed
precision/collapse level is incomplete unless the future operation language that
must survive it is specified.

Safe-operation sets for two different quotients are not generally ordered by
partition refinement.  Finer state does not automatically mean a superset or
subset of safe operations; the operation/quotient pair is the causal object.
"""

from __future__ import annotations

from typing import Hashable

State = Hashable
ClassLabel = Hashable
Operation = dict[State, State]


def _validate_quotient(quotient: dict[State, ClassLabel]) -> tuple[State, ...]:
    if not isinstance(quotient, dict) or not quotient:
        raise ValueError("quotient must be a non-empty dict")
    states = tuple(quotient)
    for state, label in quotient.items():
        try:
            hash(state)
            hash(label)
        except TypeError as error:
            raise ValueError("states and class labels must be hashable") from error
    return states


def operation_is_safe(
    quotient: dict[State, ClassLabel],
    operation: Operation,
) -> bool:
    states = _validate_quotient(quotient)
    if set(operation) != set(states) or not set(operation.values()) <= set(states):
        raise ValueError("operation must be a total endomap on quotient states")
    for left in states:
        for right in states:
            if quotient[left] == quotient[right] and quotient[operation[left]] != quotient[operation[right]]:
                return False
    return True


def induced_operation(
    quotient: dict[State, ClassLabel],
    operation: Operation,
) -> dict[ClassLabel, ClassLabel]:
    """Unique coarse operation induced by a safe raw endomap."""
    if not operation_is_safe(quotient, operation):
        raise ValueError("operation does not descend through the quotient")
    result: dict[ClassLabel, ClassLabel] = {}
    for state, label in quotient.items():
        target_label = quotient[operation[state]]
        previous = result.get(label)
        if previous is not None and previous != target_label:
            raise AssertionError("safe operation failed representative independence")
        result[label] = target_label
    return result


def compose_operations(first: Operation, second: Operation) -> Operation:
    """Return `second after first`."""
    if set(first) != set(second):
        raise ValueError("operations must have the same state domain")
    states = set(first)
    if not set(first.values()) <= states or not set(second.values()) <= states:
        raise ValueError("operations must be endomaps")
    return {state: second[first[state]] for state in first}


def identity_operation(states: tuple[State, ...]) -> Operation:
    if not isinstance(states, tuple) or not states or len(set(states)) != len(states):
        raise ValueError("states must be a non-empty tuple of unique labels")
    return {state: state for state in states}


def safe_declared_operations(
    quotient: dict[State, ClassLabel],
    operations: dict[Hashable, Operation],
) -> tuple[Hashable, ...]:
    """Names of declared primitive operations that remain exact after collapse."""
    _validate_quotient(quotient)
    return tuple(
        name
        for name in sorted(operations, key=repr)
        if operation_is_safe(quotient, operations[name])
    )


def safe_composition_closure_check(
    quotient: dict[State, ClassLabel],
    first: Operation,
    second: Operation,
) -> bool:
    """Executable form of: safe F and G imply safe G∘F."""
    if not operation_is_safe(quotient, first):
        return False
    if not operation_is_safe(quotient, second):
        return False
    return operation_is_safe(quotient, compose_operations(first, second))


def partition_refines(
    finer: dict[State, ClassLabel],
    coarser: dict[State, ClassLabel],
) -> bool:
    if set(finer) != set(coarser):
        raise ValueError("partitions must cover the same states")
    states = tuple(finer)
    return all(
        finer[left] != finer[right] or coarser[left] == coarser[right]
        for left in states
        for right in states
    )
