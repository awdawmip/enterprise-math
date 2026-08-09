"""Deterministic one-step transport branching for P018.

The contextual-closure layer determines the persistent exact state distinctions.
This module asks a different question: if the decoder knows only the original
coarse input classes for one operation call, how many possible coarse output
classes remain inside the worst such input cell?

That maximum cardinality is the transport branching capacity ``B_E(mu)``.  It is
exactly the minimum reusable correction-token alphabet for a deterministic
one-message protocol that reports the exact coarse output.  This elementary
counting theorem is treated as a finite project coordinate, not as a new
communication-complexity model.
"""

from __future__ import annotations

from collections.abc import Callable, Hashable, Iterable, Sequence
from itertools import product
from typing import TypeVar

from enterprise_math.contextual_closure import (
    FiniteOperation,
    contextual_closure_partition,
)
from enterprise_math.predictive_closure import block_map

State = TypeVar("State", bound=Hashable)
Output = TypeVar("Output", bound=Hashable)


def _states_tuple(states: Iterable[State]) -> tuple[State, ...]:
    materialized = tuple(states)
    if not materialized:
        raise ValueError("states must be nonempty")
    if len(set(materialized)) != len(materialized):
        raise ValueError("states must be distinct labels")
    return materialized


def _operation_outputs_by_coarse_cell(
    states: tuple[State, ...],
    operation: FiniteOperation[State],
    observation: Callable[[State], Output],
) -> dict[tuple[Output, ...], set[Output]]:
    domain = set(states)
    cells: dict[tuple[Output, ...], set[Output]] = {}
    for args in product(states, repeat=operation.arity):
        result = operation.apply(tuple(args))
        if result not in domain:
            raise ValueError("operation must be an endomap on the finite state set")
        cell = tuple(observation(state) for state in args)
        cells.setdefault(cell, set()).add(observation(result))
    return cells


def transport_branching_profile(
    states: Iterable[State],
    operation: FiniteOperation[State],
    observation: Callable[[State], Output],
) -> dict[tuple[Output, ...], frozenset[Output]]:
    materialized = _states_tuple(states)
    return {
        cell: frozenset(outputs)
        for cell, outputs in _operation_outputs_by_coarse_cell(
            materialized, operation, observation
        ).items()
    }


def transport_branching_capacity(
    states: Iterable[State],
    operation: FiniteOperation[State],
    observation: Callable[[State], Output],
) -> int:
    """Maximum number of coarse outputs inside one coarse input cell."""
    profile = transport_branching_profile(states, operation, observation)
    return max((len(outputs) for outputs in profile.values()), default=1)


def transport_bit_cost(capacity: int) -> int:
    """Minimum fixed-length binary token size for ``capacity`` symbols."""
    if isinstance(capacity, bool) or not isinstance(capacity, int) or capacity < 1:
        raise ValueError("capacity must be a positive integer")
    return (capacity - 1).bit_length()


def canonical_transport_codebook(
    states: Iterable[State],
    operation: FiniteOperation[State],
    observation: Callable[[State], Output],
) -> dict[tuple[Output, ...], tuple[Output, ...]]:
    """One exact shared-token codebook achieving alphabet size ``B_E(mu)``.

    Token labels are local indices inside each coarse input cell and may be
    reused across cells because the decoder already knows the coarse input tuple.
    The ordering is the first occurrence order under the supplied finite-state
    enumeration, so no ordering on ``Output`` is required.
    """
    materialized = _states_tuple(states)
    domain = set(materialized)
    ordered: dict[tuple[Output, ...], list[Output]] = {}
    for args in product(materialized, repeat=operation.arity):
        result = operation.apply(tuple(args))
        if result not in domain:
            raise ValueError("operation must be an endomap on the finite state set")
        cell = tuple(observation(state) for state in args)
        output = observation(result)
        values = ordered.setdefault(cell, [])
        if output not in values:
            values.append(output)
    return {cell: tuple(values) for cell, values in ordered.items()}


def encode_transport_token(
    codebook: dict[tuple[Output, ...], tuple[Output, ...]],
    coarse_inputs: tuple[Output, ...],
    coarse_output: Output,
) -> int:
    if coarse_inputs not in codebook:
        raise ValueError("unknown coarse input cell")
    try:
        return codebook[coarse_inputs].index(coarse_output)
    except ValueError as exc:
        raise ValueError("coarse output is not realizable in this input cell") from exc


def decode_transport_token(
    codebook: dict[tuple[Output, ...], tuple[Output, ...]],
    coarse_inputs: tuple[Output, ...],
    token: int,
) -> Output:
    if coarse_inputs not in codebook:
        raise ValueError("unknown coarse input cell")
    if isinstance(token, bool) or not isinstance(token, int):
        raise ValueError("token must be an integer")
    values = codebook[coarse_inputs]
    if token < 0 or token >= len(values):
        raise ValueError("token is out of range for this coarse input cell")
    return values[token]


def operation_is_observation_congruent(
    states: Iterable[State],
    operation: FiniteOperation[State],
    observation: Callable[[State], Output],
) -> bool:
    """Exact finite check of T169 for one operation."""
    return transport_branching_capacity(states, operation, observation) == 1


def compose_disjoint_operations(
    outer: FiniteOperation[State],
    inner: Sequence[FiniteOperation[State]],
) -> FiniteOperation[State]:
    """Compose an outer operation with disjoint-tuples inner operations."""
    inner_tuple = tuple(inner)
    if outer.arity != len(inner_tuple):
        raise ValueError("outer arity must equal number of inner operations")
    offsets: list[tuple[int, int]] = []
    start = 0
    for operation in inner_tuple:
        stop = start + operation.arity
        offsets.append((start, stop))
        start = stop

    def composite(args: tuple[State, ...]) -> State:
        if len(args) != start:
            raise ValueError("composite argument tuple has wrong arity")
        intermediate = tuple(
            operation.apply(tuple(args[left:right]))
            for operation, (left, right) in zip(inner_tuple, offsets)
        )
        return outer.apply(intermediate)

    return FiniteOperation(
        name=f"{outer.name}_composed",
        arity=start,
        function=composite,
    )


def composition_branching_bound(
    states: Iterable[State],
    outer: FiniteOperation[State],
    inner: Sequence[FiniteOperation[State]],
    observation: Callable[[State], Output],
) -> tuple[int, int]:
    """Return ``(actual, product_bound)`` for disjoint operation-tree composition."""
    materialized = _states_tuple(states)
    inner_tuple = tuple(inner)
    composite = compose_disjoint_operations(outer, inner_tuple)
    actual = transport_branching_capacity(materialized, composite, observation)
    bound = transport_branching_capacity(materialized, outer, observation)
    for operation in inner_tuple:
        bound *= transport_branching_capacity(materialized, operation, observation)
    if actual > bound:
        raise AssertionError("transport branching violated the product composition bound")
    return actual, bound


def contextual_detail_counts(
    states: Iterable[State],
    operations: Sequence[FiniteOperation[State]],
    observation: Callable[[State], Output],
) -> dict[Output, int]:
    """Number of exact contextual-state blocks inside each raw observation fiber."""
    materialized = _states_tuple(states)
    closure = contextual_closure_partition(materialized, tuple(operations), observation)
    counts: dict[Output, int] = {}
    for block in closure:
        output = observation(next(iter(block)))
        counts[output] = counts.get(output, 0) + 1
    return counts


def local_detail_transport_bound(
    states: Iterable[State],
    operations: Sequence[FiniteOperation[State]],
    operation: FiniteOperation[State],
    observation: Callable[[State], Output],
) -> dict[tuple[Output, ...], tuple[int, int]]:
    """For each coarse input cell return ``(actual_B_cell, product_detail_bound)``."""
    materialized = _states_tuple(states)
    counts = contextual_detail_counts(materialized, operations, observation)
    profile = transport_branching_profile(materialized, operation, observation)
    result: dict[tuple[Output, ...], tuple[int, int]] = {}
    for cell, outputs in profile.items():
        bound = 1
        for output in cell:
            bound *= counts[output]
        if len(outputs) > bound:
            raise AssertionError("transport branching exceeded contextual detail-product bound")
        result[cell] = (len(outputs), bound)
    return result


def radix_addition_transport_capacity(radix: int) -> int:
    """Exact Q_r addition transport capacity: the carry alphabet has size two."""
    if isinstance(radix, bool) or not isinstance(radix, int) or radix < 2:
        raise ValueError("radix must be an integer at least two")
    outputs = {(u + v) // radix for u in range(radix) for v in range(radix)}
    return len(outputs)


def radix_multiplication_worst_cell_outputs(radix: int) -> frozenset[int]:
    """A coarse input cell witnessing r^2 distinct Q_r multiplication outputs.

    Use coarse inputs ``a=1`` and ``b=2r``.  Up to the common constant ``2r^2``,
    the coarse product output is ``2r*u + v + floor(u*v/r)``.  The intervals for
    consecutive ``u`` are disjoint and the expression is strictly increasing in
    ``v``, so all ``r^2`` residue pairs produce distinct coarse outputs.
    """
    if isinstance(radix, bool) or not isinstance(radix, int) or radix < 2:
        raise ValueError("radix must be an integer at least two")
    a = 1
    b = 2 * radix
    outputs = {
        radix * a * b + a * v + b * u + (u * v) // radix
        for u in range(radix)
        for v in range(radix)
    }
    return frozenset(outputs)


def radix_multiplication_transport_capacity(radix: int) -> int:
    """Exact global Q_r multiplication transport capacity on natural numbers."""
    outputs = radix_multiplication_worst_cell_outputs(radix)
    expected = radix * radix
    if len(outputs) != expected:
        raise AssertionError("chosen multiplication witness cell is not injective")
    # Every coarse input cell contains only r^2 fine residue pairs, so r^2 is
    # simultaneously a universal upper bound and the witnessed lower bound.
    return expected
