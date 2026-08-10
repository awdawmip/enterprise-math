"""Boolean-semimodule closure for finite relation-valued support futures.

A finite relation on state set X becomes a Boolean-linear map on support column
vectors.  With state order fixed, use Boolean matrix

    A[target, source] = 1  iff  source R target.

A target-observation class is an indicator row ``c``.  For one action word ``w``
its reachability predicate on initial states is exactly the Boolean row

    c A_w,

with OR as addition and AND as multiplication.  Thus the reachable-support
future language has the same closure shape as the integer P023 action module,
but over the Boolean semiring:

    L_(h+1) = join_closure(L_h union { r A_a : r in L_h }).

Because right multiplication preserves Boolean joins, it suffices to propagate
the unique join-irreducible generators of the finite join-semilattice ``L_h``.
If one closure step adds nothing, the semimodule is action-invariant and no
longer relation word can refine the support-observation kernel.

The Boolean row universe has only ``2^|X|`` elements, so strict closure steps are
finite.  This removes literal word explosion, though the Boolean semimodule
itself can still be exponential in the number of raw states.

The compiler preserves support semantics only.  Path multiplicity, branch
identity and per-branch definedness remain outside this Boolean semimodule, as in
its parent A4 powerset compiler.

Boolean matrices, subset construction, finite join-semilattices and
join-irreducibles are standard prior mathematics/automata theory.  The project
value is the explicit A4/P023 semiring boundary and exact online stop criterion.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Hashable, Iterable, Mapping, Sequence

from .admissible_support import Relation


State = Hashable
Observation = Hashable
Action = Hashable
BoolRow = tuple[int, ...]
BoolMatrix = tuple[BoolRow, ...]


def _state_order(states: Sequence[State]) -> tuple[State, ...]:
    result = tuple(states)
    if not result:
        raise ValueError("state order must be nonempty")
    if len(set(result)) != len(result):
        raise ValueError("state order must contain distinct states")
    return result


def _bit(value: int) -> int:
    if isinstance(value, bool):
        return int(value)
    if not isinstance(value, int) or value not in (0, 1):
        raise ValueError("Boolean entries must be 0/1")
    return value


def _row(values: Sequence[int], dimension: int | None = None) -> BoolRow:
    result = tuple(_bit(value) for value in values)
    if dimension is not None and len(result) != dimension:
        raise ValueError("Boolean row dimension mismatch")
    if not result:
        raise ValueError("Boolean row must be nonempty")
    return result


def _matrix(values: Sequence[Sequence[int]], dimension: int) -> BoolMatrix:
    rows = tuple(_row(row, dimension) for row in values)
    if len(rows) != dimension:
        raise ValueError("Boolean action matrix must be square")
    return rows


def relation_boolean_matrix(
    states: Sequence[State],
    relation: Relation,
) -> BoolMatrix:
    order = _state_order(states)
    if not isinstance(relation, frozenset):
        raise TypeError("relation must be a frozenset")
    index = {state: position for position, state in enumerate(order)}
    rows = [[0] * len(order) for _ in order]
    for source, target in relation:
        if source not in index or target not in index:
            raise ValueError("relation contains state outside declared order")
        rows[index[target]][index[source]] = 1
    return tuple(tuple(row) for row in rows)


def relation_family_boolean_matrices(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
) -> tuple[tuple[Action, BoolMatrix], ...]:
    order = _state_order(states)
    if not relations:
        raise ValueError("relation family must be nonempty")
    return tuple(
        (action, relation_boolean_matrix(order, relation))
        for action, relation in relations.items()
    )


def observation_boolean_rows(
    states: Sequence[State],
    observation: Callable[[State], Observation],
) -> tuple[tuple[Observation, BoolRow], ...]:
    order = _state_order(states)
    labels: list[Observation] = []
    for state in order:
        label = observation(state)
        if label not in labels:
            labels.append(label)
    return tuple(
        (
            label,
            tuple(int(observation(state) == label) for state in order),
        )
        for label in labels
    )


def boolean_row_action(row: Sequence[int], matrix: Sequence[Sequence[int]]) -> BoolRow:
    source = _row(row)
    action = _matrix(matrix, len(source))
    return tuple(
        int(
            any(
                source[inner] and action[inner][column]
                for inner in range(len(source))
            )
        )
        for column in range(len(source))
    )


def boolean_join(left: Sequence[int], right: Sequence[int]) -> BoolRow:
    left_row = _row(left)
    right_row = _row(right, len(left_row))
    return tuple(int(a or b) for a, b in zip(left_row, right_row, strict=True))


def boolean_join_closure(rows: Iterable[Sequence[int]]) -> frozenset[BoolRow]:
    generators = tuple(tuple(row) for row in rows)
    if not generators:
        raise ValueError("at least one Boolean generator row is required")
    dimension = len(generators[0])
    normalized = tuple(_row(row, dimension) for row in generators)
    zero = (0,) * dimension
    closure = {zero}
    for generator in normalized:
        closure.update(
            boolean_join(existing, generator)
            for existing in tuple(closure)
        )
    return frozenset(closure)


def boolean_join_irreducibles(
    semimodule: Iterable[Sequence[int]],
) -> tuple[BoolRow, ...]:
    values = tuple(tuple(row) for row in semimodule)
    if not values:
        raise ValueError("semimodule must be nonempty")
    dimension = len(values[0])
    closure = frozenset(_row(row, dimension) for row in values)
    zero = (0,) * dimension
    if zero not in closure:
        raise ValueError("Boolean semimodule must contain the zero row")
    for left in closure:
        for right in closure:
            if boolean_join(left, right) not in closure:
                raise ValueError("Boolean semimodule must be join-closed")

    def strict_subset(left: BoolRow, right: BoolRow) -> bool:
        return left != right and all(a <= b for a, b in zip(left, right, strict=True))

    irreducibles = []
    for candidate in closure:
        if candidate == zero:
            continue
        reducible = any(
            strict_subset(left, candidate)
            and strict_subset(right, candidate)
            and boolean_join(left, right) == candidate
            for left in closure
            for right in closure
        )
        if not reducible:
            irreducibles.append(candidate)
    return tuple(sorted(irreducibles))


def boolean_semimodule_closure_step(
    semimodule: Iterable[Sequence[int]],
    action_matrices: Sequence[Sequence[Sequence[int]]],
) -> frozenset[BoolRow]:
    values = tuple(tuple(row) for row in semimodule)
    if not values:
        raise ValueError("semimodule must be nonempty")
    dimension = len(values[0])
    current = frozenset(_row(row, dimension) for row in values)
    actions = tuple(_matrix(matrix, dimension) for matrix in action_matrices)
    if not actions:
        raise ValueError("at least one Boolean action is required")
    basis = boolean_join_irreducibles(current)
    generated = tuple(current) + tuple(
        boolean_row_action(row, action)
        for row in basis
        for action in actions
    )
    return boolean_join_closure(generated)


def boolean_semimodule_state_partition(
    states: Sequence[State],
    semimodule: Iterable[Sequence[int]],
) -> frozenset[frozenset[State]]:
    order = _state_order(states)
    values = tuple(tuple(row) for row in semimodule)
    if not values:
        raise ValueError("semimodule must be nonempty")
    dimension = len(order)
    closure = frozenset(_row(row, dimension) for row in values)
    basis = boolean_join_irreducibles(closure)
    groups: dict[tuple[int, ...], set[State]] = {}
    for column, state in enumerate(order):
        signature = tuple(row[column] for row in basis)
        groups.setdefault(signature, set()).add(state)
    return frozenset(frozenset(group) for group in groups.values())


@dataclass(frozen=True)
class BooleanFutureSemimoduleStep:
    horizon: int
    semimodule: frozenset[BoolRow]
    join_irreducibles: tuple[BoolRow, ...]
    state_partition: frozenset[frozenset[State]]


@dataclass(frozen=True)
class BooleanFutureSemimoduleReport:
    state_count: int
    action_count: int
    exact_stabilization_horizon: int
    final_semimodule: frozenset[BoolRow]
    final_join_irreducibles: tuple[BoolRow, ...]
    steps: tuple[BooleanFutureSemimoduleStep, ...]
    finite_row_universe_size: int


def relation_boolean_future_semimodule_report(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
) -> BooleanFutureSemimoduleReport:
    order = _state_order(states)
    action_pairs = relation_family_boolean_matrices(order, relations)
    actions = tuple(matrix for _, matrix in action_pairs)
    observation_pairs = observation_boolean_rows(order, observation)
    current = boolean_join_closure(row for _, row in observation_pairs)
    steps: list[BooleanFutureSemimoduleStep] = []

    def record(horizon: int, value: frozenset[BoolRow]) -> None:
        steps.append(
            BooleanFutureSemimoduleStep(
                horizon=horizon,
                semimodule=value,
                join_irreducibles=boolean_join_irreducibles(value),
                state_partition=boolean_semimodule_state_partition(order, value),
            )
        )

    horizon = 0
    record(horizon, current)
    row_universe_size = 1 << len(order)
    while True:
        nxt = boolean_semimodule_closure_step(current, actions)
        record(horizon + 1, nxt)
        if nxt == current:
            return BooleanFutureSemimoduleReport(
                state_count=len(order),
                action_count=len(actions),
                exact_stabilization_horizon=horizon,
                final_semimodule=current,
                final_join_irreducibles=boolean_join_irreducibles(current),
                steps=tuple(steps),
                finite_row_universe_size=row_universe_size,
            )
        if len(nxt) <= len(current):
            raise AssertionError("strict Boolean semimodule refinement did not grow")
        if len(nxt) > row_universe_size:
            raise AssertionError("Boolean row semimodule exceeded finite universe")
        horizon += 1
        current = nxt
