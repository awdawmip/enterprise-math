"""Minimal rational linear predictive state for exact weighted terminal traces.

Start with an exact integer weighted quotient machine with b discrete branching
states, action matrices B_a and current observation rows C. Terminal weighted
word outputs are the rows

    C B_w.

Let

    W = span_Q { C B_w : all words w }.

W is finite-dimensional and invariant under right multiplication by every B_a.
Choose an integer row basis R of W, with r=rank_Q(W). Then for every action
there is a unique rational matrix T_a satisfying

    R B_a = T_a R,

and the current observation rows factor as

    C = H R.

For a discrete quotient source j, the predictive state is

    s_j = R e_j.

It evolves exactly by ``s -> T_a s`` and emits observations by ``H s``. Hence
every exact terminal weighted trace factors through an r-dimensional rational
predictive state.

The dimension r is minimal among **linear** predictive quotients over Q. Any
linear state map S through which every row C B_w factors must have row span
containing W, so rank(S)>=r.

This representation is intentionally weaker than the branching-operation state:
it need not retain enough information to execute the original relation/weighted
transition interface as a discrete quotient. It is the canonical representation
type for the declared linear terminal-trace language.

Finite-dimensional observability, weighted automata minimization and linear
systems realization are standard prior mathematics/CS. The project value is the
explicit semantic-precision route from reflected local machine to minimal linear
predictive state.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Callable, Hashable, Mapping, Sequence

from .bounded_local_law_reflection import (
    Action,
    Matrix,
    Observation,
    State,
    WeightedFamily,
    _states,
    _weighted_family,
    exact_weighted_quotient_matrices,
    matrix_word_apply,
    weighted_refinement_sequence,
)
from .relation_support_stable_refinement import (
    Partition,
    normalize_partition,
    partition_from_observation,
)
from .relation_terminal_count_trace_certificate import (
    independent_integer_rows,
    rational_matrix_rank,
    row_times_matrix,
)


RationalVector = tuple[Fraction, ...]
RationalMatrix = tuple[RationalVector, ...]


def quotient_observation_indicator_rows(
    partition: Sequence[Sequence[State] | frozenset[State]],
    observation: Callable[[State], Observation],
) -> tuple[tuple[int, ...], ...]:
    current = normalize_partition(partition)
    labels: list[Observation] = []
    block_labels: list[Observation] = []
    for block in current:
        values = {observation(state) for state in block}
        if len(values) != 1:
            raise ValueError("partition must refine current observation")
        label = next(iter(values))
        block_labels.append(label)
        if label not in labels:
            labels.append(label)
    return tuple(
        tuple(int(block_label == label) for block_label in block_labels)
        for label in labels
    )


@dataclass(frozen=True)
class LinearTraceClosureStep:
    horizon: int
    rank: int
    basis_rows: tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class LinearTraceClosureReport:
    quotient_state_count: int
    initial_observation_rank: int
    predictive_dimension: int
    stabilization_horizon: int
    theorem_horizon_bound: int
    basis_rows: tuple[tuple[int, ...], ...]
    steps: tuple[LinearTraceClosureStep, ...]


def weighted_quotient_trace_closure(
    action_matrices: Mapping[Action, Matrix],
    observation_rows: Sequence[Sequence[int]],
) -> LinearTraceClosureReport:
    if not action_matrices:
        raise ValueError("action_matrices must be nonempty")
    matrices = dict(action_matrices)
    first = next(iter(matrices.values()))
    size = len(first)
    if size <= 0 or any(len(row) != size for row in first):
        raise ValueError("action matrices must be nonempty and square")
    for matrix in matrices.values():
        if len(matrix) != size or any(len(row) != size for row in matrix):
            raise ValueError("all action matrices must share one square dimension")
    rows = tuple(tuple(row) for row in observation_rows)
    if not rows or any(len(row) != size for row in rows):
        raise ValueError("observation row width must equal quotient state count")

    basis = independent_integer_rows(rows)
    initial_rank = len(basis)
    if initial_rank <= 0:
        raise AssertionError("observation rows lost all rational rank")
    theorem_bound = size - initial_rank
    steps = [
        LinearTraceClosureStep(
            horizon=0,
            rank=initial_rank,
            basis_rows=basis,
        )
    ]
    horizon = 0
    action_order = tuple(
        matrix
        for _, matrix in sorted(matrices.items(), key=lambda item: repr(item[0]))
    )

    while True:
        generated = list(basis)
        generated.extend(
            row_times_matrix(row, matrix)
            for row in basis
            for matrix in action_order
        )
        nxt = independent_integer_rows(generated)
        if len(nxt) == len(basis):
            if horizon > theorem_bound:
                raise AssertionError("predictive row space stabilized after dimension bound")
            return LinearTraceClosureReport(
                quotient_state_count=size,
                initial_observation_rank=initial_rank,
                predictive_dimension=len(basis),
                stabilization_horizon=horizon,
                theorem_horizon_bound=theorem_bound,
                basis_rows=basis,
                steps=tuple(steps),
            )
        if len(nxt) <= len(basis):
            raise AssertionError("strict predictive closure step failed rank growth")
        basis = nxt
        horizon += 1
        if horizon > theorem_bound:
            raise AssertionError("predictive rank exceeded finite dimension bound")
        steps.append(
            LinearTraceClosureStep(
                horizon=horizon,
                rank=len(basis),
                basis_rows=basis,
            )
        )


def _row_coordinates_in_basis(
    vector: Sequence[int],
    basis_rows: Sequence[Sequence[int]],
) -> RationalVector:
    vector_values = tuple(vector)
    basis = tuple(tuple(row) for row in basis_rows)
    if not basis:
        raise ValueError("basis_rows must be nonempty")
    width = len(basis[0])
    if len(vector_values) != width or any(len(row) != width for row in basis):
        raise ValueError("basis/vector dimension mismatch")
    rank = rational_matrix_rank(basis)
    if rank != len(basis):
        raise ValueError("basis_rows must be rationally independent")
    if rational_matrix_rank((*basis, vector_values)) != rank:
        raise ValueError("vector does not lie in row span of basis")

    # Solve B^T c = vector^T. There are ``width`` equations in r unknowns and
    # the solution is unique because the basis rows are independent.
    variable_count = len(basis)
    work = [
        [Fraction(basis[column][equation]) for column in range(variable_count)]
        + [Fraction(vector_values[equation])]
        for equation in range(width)
    ]
    pivot_row = 0
    pivot_for_variable: dict[int, int] = {}
    for variable in range(variable_count):
        pivot = next(
            (
                row
                for row in range(pivot_row, len(work))
                if work[row][variable] != 0
            ),
            None,
        )
        if pivot is None:
            raise AssertionError("independent basis transpose lost a pivot")
        work[pivot_row], work[pivot] = work[pivot], work[pivot_row]
        pivot_value = work[pivot_row][variable]
        work[pivot_row] = [entry / pivot_value for entry in work[pivot_row]]
        for row in range(len(work)):
            if row == pivot_row:
                continue
            factor = work[row][variable]
            if factor == 0:
                continue
            work[row] = [
                left - factor * right
                for left, right in zip(work[row], work[pivot_row], strict=True)
            ]
        pivot_for_variable[variable] = pivot_row
        pivot_row += 1

    solution = tuple(
        work[pivot_for_variable[variable]][-1]
        for variable in range(variable_count)
    )
    reconstructed = tuple(
        sum(solution[index] * basis[index][column] for index in range(variable_count))
        for column in range(width)
    )
    if reconstructed != tuple(Fraction(value) for value in vector_values):
        raise AssertionError("row-coordinate solver reconstructed the wrong vector")
    return solution


def induced_predictive_action_matrices(
    basis_rows: Sequence[Sequence[int]],
    action_matrices: Mapping[Action, Matrix],
) -> dict[Action, RationalMatrix]:
    basis = tuple(tuple(row) for row in basis_rows)
    result: dict[Action, RationalMatrix] = {}
    for action, matrix in action_matrices.items():
        result[action] = tuple(
            _row_coordinates_in_basis(row_times_matrix(basis_row, matrix), basis)
            for basis_row in basis
        )
    return result


def observation_decoder_matrix(
    basis_rows: Sequence[Sequence[int]],
    observation_rows: Sequence[Sequence[int]],
) -> RationalMatrix:
    basis = tuple(tuple(row) for row in basis_rows)
    return tuple(
        _row_coordinates_in_basis(row, basis)
        for row in observation_rows
    )


def predictive_state_for_quotient_index(
    basis_rows: Sequence[Sequence[int]],
    quotient_index: int,
) -> RationalVector:
    basis = tuple(tuple(row) for row in basis_rows)
    if not basis:
        raise ValueError("basis_rows must be nonempty")
    width = len(basis[0])
    if not 0 <= quotient_index < width:
        raise ValueError("quotient_index outside basis width")
    return tuple(Fraction(row[quotient_index]) for row in basis)


def rational_matrix_times_vector(
    matrix: Sequence[Sequence[Fraction]],
    vector: Sequence[Fraction],
) -> RationalVector:
    rows = tuple(tuple(Fraction(value) for value in row) for row in matrix)
    values = tuple(Fraction(value) for value in vector)
    if not rows or any(len(row) != len(values) for row in rows):
        raise ValueError("matrix/vector dimension mismatch")
    return tuple(
        sum(row[index] * values[index] for index in range(len(values)))
        for row in rows
    )


def predictive_word_state(
    initial_state: Sequence[Fraction],
    word: Sequence[Action],
    predictive_actions: Mapping[Action, RationalMatrix],
) -> RationalVector:
    current = tuple(Fraction(value) for value in initial_state)
    for action in word:
        if action not in predictive_actions:
            raise ValueError("word contains unknown predictive action")
        current = rational_matrix_times_vector(predictive_actions[action], current)
    return current


def predictive_output(
    state: Sequence[Fraction],
    decoder: Sequence[Sequence[Fraction]],
) -> RationalVector:
    return rational_matrix_times_vector(decoder, state)


@dataclass(frozen=True)
class LinearPredictiveStateReport:
    raw_state_count: int
    branching_state_count: int
    predictive_dimension: int
    initial_observation_rank: int
    trace_stabilization_horizon: int
    trace_horizon_bound: int
    stable_partition: Partition
    quotient_action_matrices: dict[Action, Matrix]
    observation_rows: tuple[tuple[int, ...], ...]
    basis_rows: tuple[tuple[int, ...], ...]
    predictive_action_matrices: dict[Action, RationalMatrix]
    observation_decoder: RationalMatrix

    @property
    def linear_dimension_saved_vs_branching(self) -> int:
        return self.branching_state_count - self.predictive_dimension

    @property
    def unobservable_linear_dimension(self) -> int:
        return self.branching_state_count - self.predictive_dimension


def compile_linear_predictive_state(
    states: Sequence[State],
    family: WeightedFamily,
    observation: Callable[[State], Observation],
) -> LinearPredictiveStateReport:
    order = _states(states)
    weighted = _weighted_family(order, family)
    initial = partition_from_observation(order, observation)
    stable = weighted_refinement_sequence(initial, weighted)[-1]
    quotient_matrices = exact_weighted_quotient_matrices(stable, weighted)
    observation_rows = quotient_observation_indicator_rows(stable, observation)
    closure = weighted_quotient_trace_closure(quotient_matrices, observation_rows)
    basis = closure.basis_rows
    actions = induced_predictive_action_matrices(basis, quotient_matrices)
    decoder = observation_decoder_matrix(basis, observation_rows)
    return LinearPredictiveStateReport(
        raw_state_count=len(order),
        branching_state_count=len(stable),
        predictive_dimension=closure.predictive_dimension,
        initial_observation_rank=closure.initial_observation_rank,
        trace_stabilization_horizon=closure.stabilization_horizon,
        trace_horizon_bound=closure.theorem_horizon_bound,
        stable_partition=stable,
        quotient_action_matrices=quotient_matrices,
        observation_rows=observation_rows,
        basis_rows=basis,
        predictive_action_matrices=actions,
        observation_decoder=decoder,
    )


def predictive_state_for_raw_source(
    report: LinearPredictiveStateReport,
    source: State,
) -> RationalVector:
    block_index = next(
        (index for index, block in enumerate(report.stable_partition) if source in block),
        None,
    )
    if block_index is None:
        raise ValueError("source outside report stable partition")
    return predictive_state_for_quotient_index(report.basis_rows, block_index)


def predictive_trace_matches_exact_quotient(
    report: LinearPredictiveStateReport,
    source: State,
    word: Sequence[Action],
) -> bool:
    """Check both predictive-state intertwining and emitted terminal outputs."""
    source_block = next(
        (index for index, block in enumerate(report.stable_partition) if source in block),
        None,
    )
    if source_block is None:
        raise ValueError("source outside report stable partition")

    quotient_state = matrix_word_apply(
        report.quotient_action_matrices,
        source_block,
        word,
    )
    exact_basis_state = tuple(
        sum(
            Fraction(report.basis_rows[row][target]) * quotient_state[target]
            for target in range(report.branching_state_count)
        )
        for row in range(report.predictive_dimension)
    )
    predicted_state = predictive_word_state(
        predictive_state_for_quotient_index(report.basis_rows, source_block),
        word,
        report.predictive_action_matrices,
    )
    if exact_basis_state != predicted_state:
        raise AssertionError("predictive action failed exact quotient intertwining")

    exact_output = tuple(
        sum(
            Fraction(row[target]) * quotient_state[target]
            for target in range(report.branching_state_count)
        )
        for row in report.observation_rows
    )
    predicted_output = predictive_output(predicted_state, report.observation_decoder)
    if exact_output != predicted_output:
        raise AssertionError("predictive state emitted the wrong terminal output")
    return True


def predictive_partition_from_basis(
    report: LinearPredictiveStateReport,
) -> Partition:
    groups: dict[RationalVector, set[State]] = {}
    for block_index, block in enumerate(report.stable_partition):
        signature = predictive_state_for_quotient_index(report.basis_rows, block_index)
        for state in block:
            groups.setdefault(signature, set()).add(state)
    return normalize_partition(tuple(groups.values()))


def weighted_scalar_fan_fixture(
    count: int = 10,
) -> tuple[
    tuple[str, ...],
    dict[str, dict[tuple[str, str], int]],
    Callable[[str], str],
]:
    """Many discrete weighted branching states but a two-dimensional trace state."""
    if isinstance(count, bool) or not isinstance(count, int) or count < 2:
        raise ValueError("count must be an integer at least two")
    sources = tuple(f"x{index}" for index in range(1, count + 1))
    terminal = "z"
    states = (*sources, terminal)
    relation = {
        (source, terminal): index
        for index, source in enumerate(sources, start=1)
    }
    return states, {"a": relation}, lambda _state: "visible"
