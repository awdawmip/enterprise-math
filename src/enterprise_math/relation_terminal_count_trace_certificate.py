"""Finite exact certificate for infinite natural terminal path-count traces.

For a finite relation family, exact terminal path-count traces are linear over
integer adjacency matrices.  Let C be the observation-class indicator rows and
A_a the target-row/source-column adjacency matrices.  Literal word observations
are the integer rows

    C A_w.

Their rational row spaces satisfy

    W_(h+1) = W_h + sum_a W_h A_a.

If one step has no rational rank growth, W_h is action-invariant and no longer
word can create a new exact trace direction.  Starting from c_0 independent
observation rows in state dimension n, the exact row space therefore stabilizes
by horizon at most

    n - c_0.

Equality of all infinite exact natural terminal traces between two source states
is exactly equality of their coordinates under a rational basis of this final
row space.

If h_* is the actual stabilization horizon and Delta is the maximum raw
outdegree, every literal path-count coefficient needed through h_* is bounded by
max(1, Delta**h_*).  Hence any modulus larger than this bound reflects every
necessary exact coefficient.  The mod-M terminal trace partition through h_*
then equals the **infinite** exact-N trace partition.

This gives a finite two-resource certificate for an infinite terminal trace
language:

* finite word depth h_* from rational observability closure;
* finite coefficient modulus M > Delta**h_*.

The theorem is deliberately distinct from exact count-branching state, whose
coefficient cutoff is only Delta+1 and is horizon-independent.

Weighted automata equivalence, finite-dimensional observability and rational row
space closure are standard prior mathematics/CS.  The project value is the exact
resource decomposition between structural branching state and flattened path
traces.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Callable, Hashable, Mapping, Sequence

from .admissible_support import Relation
from .relation_branching_count_cutoff import relation_max_outdegree
from .relation_branching_semiring import modular_semiring
from .relation_branching_vs_trace_cutoff import (
    modular_terminal_trace_partition,
    natural_terminal_trace_partition,
)
from .relation_support_stable_refinement import Partition, normalize_partition


State = Hashable
Action = Hashable
Observation = Hashable
Vector = tuple[int, ...]
Matrix = tuple[Vector, ...]


def _states(values: Sequence[State]) -> tuple[State, ...]:
    result = tuple(values)
    if not result or len(set(result)) != len(result):
        raise ValueError("states must be a nonempty distinct sequence")
    return result


def _family(
    states: tuple[State, ...],
    relations: Mapping[Action, Relation],
) -> dict[Action, Relation]:
    if not relations:
        raise ValueError("relation family must be nonempty")
    state_set = set(states)
    result: dict[Action, Relation] = {}
    for name, relation in relations.items():
        if not isinstance(relation, frozenset):
            raise TypeError("every relation must be a frozenset of ordered pairs")
        if any(source not in state_set or target not in state_set for source, target in relation):
            raise ValueError("relation contains state outside declared state set")
        result[name] = relation
    return result


def relation_adjacency_matrix(
    states: Sequence[State],
    relation: Relation,
) -> Matrix:
    order = _states(states)
    index = {state: position for position, state in enumerate(order)}
    if not isinstance(relation, frozenset):
        raise TypeError("relation must be a frozenset")
    if any(source not in index or target not in index for source, target in relation):
        raise ValueError("relation contains state outside declared state set")
    size = len(order)
    work = [[0 for _ in range(size)] for _ in range(size)]
    for source, target in relation:
        work[index[target]][index[source]] = 1
    return tuple(tuple(row) for row in work)


def observation_indicator_rows(
    states: Sequence[State],
    observation: Callable[[State], Observation],
) -> Matrix:
    order = _states(states)
    labels: list[Observation] = []
    seen: set[Observation] = set()
    for state in order:
        label = observation(state)
        hash(label)
        if label not in seen:
            seen.add(label)
            labels.append(label)
    return tuple(
        tuple(int(observation(state) == label) for state in order)
        for label in labels
    )


def row_times_matrix(row: Vector, matrix: Matrix) -> Vector:
    if len(row) != len(matrix):
        raise ValueError("row/matrix dimension mismatch")
    if any(len(matrix_row) != len(row) for matrix_row in matrix):
        raise ValueError("action matrix must be square")
    return tuple(
        sum(row[inner] * matrix[inner][column] for inner in range(len(row)))
        for column in range(len(row))
    )


def rational_matrix_rank(rows: Sequence[Sequence[int]]) -> int:
    values = tuple(tuple(row) for row in rows)
    if not values:
        return 0
    width = len(values[0])
    if width == 0 or any(len(row) != width for row in values):
        raise ValueError("rows must have one common positive width")
    work = [[Fraction(value) for value in row] for row in values]
    rank = 0
    for column in range(width):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column] != 0),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][column]
        work[rank] = [value / pivot_value for value in work[rank]]
        for row in range(len(work)):
            if row == rank:
                continue
            factor = work[row][column]
            if factor == 0:
                continue
            work[row] = [
                left - factor * right
                for left, right in zip(work[row], work[rank], strict=True)
            ]
        rank += 1
        if rank == len(work):
            break
    return rank


def independent_integer_rows(rows: Sequence[Sequence[int]]) -> Matrix:
    """Select original integer rows forming a Q-basis of the supplied row span."""
    selected: list[Vector] = []
    current_rank = 0
    for row in rows:
        vector = tuple(row)
        if not vector:
            raise ValueError("row must be nonempty")
        candidate = tuple((*selected, vector))
        rank = rational_matrix_rank(candidate)
        if rank > current_rank:
            selected.append(vector)
            current_rank = rank
    return tuple(selected)


@dataclass(frozen=True)
class RationalTraceClosureStep:
    horizon: int
    rank: int
    basis_rows: Matrix


@dataclass(frozen=True)
class RationalTraceClosureReport:
    state_count: int
    initial_observation_rank: int
    theorem_horizon_bound: int
    stabilization_horizon: int
    final_basis_rows: Matrix
    steps: tuple[RationalTraceClosureStep, ...]


def rational_terminal_trace_closure_report(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
) -> RationalTraceClosureReport:
    order = _states(states)
    family = _family(order, relations)
    actions = tuple(
        relation_adjacency_matrix(order, family[name])
        for name in sorted(family, key=repr)
    )
    basis = independent_integer_rows(observation_indicator_rows(order, observation))
    initial_rank = len(basis)
    if initial_rank <= 0:
        raise AssertionError("nonempty state set lost all observation indicator rows")
    theorem_bound = len(order) - initial_rank
    steps = [
        RationalTraceClosureStep(
            horizon=0,
            rank=initial_rank,
            basis_rows=basis,
        )
    ]
    current_horizon = 0

    while True:
        previous = basis
        generated = list(previous)
        generated.extend(
            row_times_matrix(row, action)
            for row in previous
            for action in actions
        )
        basis = independent_integer_rows(generated)
        next_rank = len(basis)
        if next_rank == len(previous):
            if current_horizon > theorem_bound:
                raise AssertionError("trace row space stabilized after theorem bound")
            return RationalTraceClosureReport(
                state_count=len(order),
                initial_observation_rank=initial_rank,
                theorem_horizon_bound=theorem_bound,
                stabilization_horizon=current_horizon,
                final_basis_rows=previous,
                steps=tuple(steps),
            )
        if next_rank <= len(previous):
            raise AssertionError("strict trace closure step failed rank growth")
        current_horizon += 1
        if current_horizon > theorem_bound:
            raise AssertionError("trace row-space rank exceeded finite horizon bound")
        steps.append(
            RationalTraceClosureStep(
                horizon=current_horizon,
                rank=next_rank,
                basis_rows=basis,
            )
        )


def partition_from_row_basis(
    states: Sequence[State],
    basis_rows: Sequence[Sequence[int]],
) -> Partition:
    order = _states(states)
    basis = tuple(tuple(row) for row in basis_rows)
    if not basis:
        raise ValueError("basis_rows must be nonempty")
    if any(len(row) != len(order) for row in basis):
        raise ValueError("basis row width must equal state count")
    groups: dict[tuple[int, ...], set[State]] = {}
    for index, state in enumerate(order):
        signature = tuple(row[index] for row in basis)
        groups.setdefault(signature, set()).add(state)
    return normalize_partition(tuple(groups.values()))


def exact_infinite_terminal_trace_partition(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
) -> Partition:
    report = rational_terminal_trace_closure_report(states, relations, observation)
    return partition_from_row_basis(states, report.final_basis_rows)


def finite_trace_certificate_modulus(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
) -> int:
    """Guaranteed modulus using the actual rational stabilization horizon."""
    report = rational_terminal_trace_closure_report(states, relations, observation)
    delta = relation_max_outdegree(states, relations)
    bound = max(1, delta ** report.stabilization_horizon)
    return max(2, bound + 1)


def universal_state_count_trace_modulus_bound(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
) -> int:
    """Uniform bound using only Delta and n-c_0, not actual closure horizon."""
    order = _states(states)
    initial_rank = len(independent_integer_rows(observation_indicator_rows(order, observation)))
    delta = relation_max_outdegree(order, relations)
    horizon_bound = len(order) - initial_rank
    return max(2, max(1, delta**horizon_bound) + 1)


@dataclass(frozen=True)
class TerminalTraceFiniteCertificateReport:
    state_count: int
    maximum_outdegree: int
    initial_observation_rank: int
    theorem_horizon_bound: int
    stabilization_horizon: int
    actual_horizon_modulus: int
    universal_state_count_modulus_bound: int
    exact_infinite_partition: Partition
    exact_finite_horizon_partition: Partition
    modular_certificate_partition: Partition

    @property
    def finite_horizon_is_exact(self) -> bool:
        return self.exact_finite_horizon_partition == self.exact_infinite_partition

    @property
    def modular_certificate_is_exact(self) -> bool:
        return self.modular_certificate_partition == self.exact_infinite_partition


def terminal_trace_finite_certificate_report(
    states: Sequence[State],
    relations: Mapping[Action, Relation],
    observation: Callable[[State], Observation],
) -> TerminalTraceFiniteCertificateReport:
    order = _states(states)
    closure = rational_terminal_trace_closure_report(order, relations, observation)
    delta = relation_max_outdegree(order, relations)
    modulus = finite_trace_certificate_modulus(order, relations, observation)
    exact_infinite = partition_from_row_basis(order, closure.final_basis_rows)
    exact_finite = natural_terminal_trace_partition(
        order,
        relations,
        observation,
        closure.stabilization_horizon,
    )
    modular = modular_terminal_trace_partition(
        order,
        relations,
        observation,
        closure.stabilization_horizon,
        modulus,
    )
    if exact_finite != exact_infinite:
        raise AssertionError("rational closure horizon failed to determine infinite exact trace partition")
    if modular != exact_infinite:
        raise AssertionError("finite modulus at closure horizon failed exact trace certificate")
    return TerminalTraceFiniteCertificateReport(
        state_count=len(order),
        maximum_outdegree=delta,
        initial_observation_rank=closure.initial_observation_rank,
        theorem_horizon_bound=closure.theorem_horizon_bound,
        stabilization_horizon=closure.stabilization_horizon,
        actual_horizon_modulus=modulus,
        universal_state_count_modulus_bound=universal_state_count_trace_modulus_bound(
            order,
            relations,
            observation,
        ),
        exact_infinite_partition=exact_infinite,
        exact_finite_horizon_partition=exact_finite,
        modular_certificate_partition=modular,
    )
