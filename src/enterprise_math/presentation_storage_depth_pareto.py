"""Storage/execution-depth Pareto for exact literal-macro presentations.

Fix a finite exact action presentation with k named generator matrices.  A
literal d-macro presentation additionally stores the exact transition matrix for
every action word of length 1..d.  No new world law is introduced: every macro
is derivable by generator composition.

The number of stored literal macro rules is

    S(k,d) = sum_(i=1)^d k^i.

Any word of length h can then be decomposed into consecutive chunks of length at
most d and executed using

    ceil(h/d)

macro transitions.  Thus larger d trades storage for smaller execution depth.

This module deliberately studies the **literal macro-table representation
class**.  Algebraic relations, normal forms, circuits, DAG sharing and specialized
fast exponentiation may compress a particular action semigroup further.  The
point here is the exact project-level resource axis, not a universal lower bound
for every representation technology.

The module also separates reusable transition macros from terminal readout
tables: storing C B_w can answer a word directly but does not by itself preserve
the successor state needed for arbitrary continuation.

Memoization, transition monoids and time-memory tradeoffs are standard prior
mathematics/CS.  The project value is the explicit presentation-precision Pareto
bridge.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import ceil
from typing import Hashable, Mapping, Sequence


Action = Hashable
Scalar = int | Fraction
Matrix = tuple[tuple[Scalar, ...], ...]
Word = tuple[Action, ...]


def _positive_int(value: int, *, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def literal_macro_rule_count(action_count: int, macro_depth: int) -> int:
    k = _positive_int(action_count, name="action_count")
    d = _positive_int(macro_depth, name="macro_depth")
    return sum(k**length for length in range(1, d + 1))


def closed_literal_macro_rule_count(action_count: int, macro_depth: int) -> int:
    k = _positive_int(action_count, name="action_count")
    d = _positive_int(macro_depth, name="macro_depth")
    if k == 1:
        return d
    return k * (k**d - 1) // (k - 1)


def macro_execution_blocks(word_length: int, macro_depth: int) -> int:
    if isinstance(word_length, bool) or not isinstance(word_length, int) or word_length < 0:
        raise ValueError("word_length must be a nonnegative integer")
    d = _positive_int(macro_depth, name="macro_depth")
    if word_length == 0:
        return 0
    return ceil(word_length / d)


def literal_words(actions: Sequence[Action], max_length: int) -> tuple[Word, ...]:
    names = tuple(actions)
    if not names or len(set(names)) != len(names):
        raise ValueError("actions must be a nonempty distinct sequence")
    d = _positive_int(max_length, name="max_length")
    return tuple(
        word
        for length in range(1, d + 1)
        for word in product(names, repeat=length)
    )


def _validate_square_matrix(matrix: Sequence[Sequence[Scalar]]) -> Matrix:
    rows = tuple(tuple(value for value in row) for row in matrix)
    if not rows:
        raise ValueError("matrix must be nonempty")
    size = len(rows)
    if any(len(row) != size for row in rows):
        raise ValueError("matrix must be square")
    return rows


def identity_matrix(size: int) -> Matrix:
    n = _positive_int(size, name="size")
    return tuple(
        tuple(int(row == column) for column in range(n))
        for row in range(n)
    )


def matrix_multiply(left: Sequence[Sequence[Scalar]], right: Sequence[Sequence[Scalar]]) -> Matrix:
    a = _validate_square_matrix(left)
    b = _validate_square_matrix(right)
    if len(a) != len(b):
        raise ValueError("matrix dimensions must match")
    size = len(a)
    return tuple(
        tuple(
            sum(a[row][inner] * b[inner][column] for inner in range(size))
            for column in range(size)
        )
        for row in range(size)
    )


def word_transition_matrix(
    action_matrices: Mapping[Action, Sequence[Sequence[Scalar]]],
    word: Sequence[Action],
) -> Matrix:
    if not action_matrices:
        raise ValueError("action_matrices must be nonempty")
    matrices = {
        name: _validate_square_matrix(matrix)
        for name, matrix in action_matrices.items()
    }
    size = len(next(iter(matrices.values())))
    if any(len(matrix) != size for matrix in matrices.values()):
        raise ValueError("all action matrices must share one dimension")
    current = identity_matrix(size)
    for action in word:
        if action not in matrices:
            raise ValueError("word contains unknown action")
        # Column-state convention: first apply ``current``, then action matrix.
        current = matrix_multiply(matrices[action], current)
    return current


def precompute_literal_macro_table(
    action_matrices: Mapping[Action, Sequence[Sequence[Scalar]]],
    macro_depth: int,
) -> dict[Word, Matrix]:
    if not action_matrices:
        raise ValueError("action_matrices must be nonempty")
    names = tuple(action_matrices)
    d = _positive_int(macro_depth, name="macro_depth")
    return {
        word: word_transition_matrix(action_matrices, word)
        for word in literal_words(names, d)
    }


def chunk_word(word: Sequence[Action], macro_depth: int) -> tuple[Word, ...]:
    values = tuple(word)
    d = _positive_int(macro_depth, name="macro_depth")
    return tuple(
        values[start : start + d]
        for start in range(0, len(values), d)
    )


def execute_word_from_macro_table(
    action_matrices: Mapping[Action, Sequence[Sequence[Scalar]]],
    word: Sequence[Action],
    macro_depth: int,
) -> Matrix:
    matrices = dict(action_matrices)
    if not matrices:
        raise ValueError("action_matrices must be nonempty")
    size = len(_validate_square_matrix(next(iter(matrices.values()))))
    chunks = chunk_word(word, macro_depth)
    if not chunks:
        return identity_matrix(size)
    table = precompute_literal_macro_table(matrices, macro_depth)
    current = identity_matrix(size)
    for chunk in chunks:
        if chunk not in table:
            raise AssertionError("chunk missing from literal macro table")
        current = matrix_multiply(table[chunk], current)
    return current


def macro_execution_matches_literal(
    action_matrices: Mapping[Action, Sequence[Sequence[Scalar]]],
    word: Sequence[Action],
    macro_depth: int,
) -> bool:
    literal = word_transition_matrix(action_matrices, word)
    macro = execute_word_from_macro_table(action_matrices, word, macro_depth)
    if literal != macro:
        raise AssertionError("macro presentation changed exact word transition")
    return True


@dataclass(frozen=True)
class PresentationParetoPoint:
    action_count: int
    horizon: int
    macro_depth: int
    stored_macro_rules: int
    worst_case_execution_blocks: int
    state_dimension: int | None = None

    @property
    def stored_transition_scalars(self) -> int | None:
        if self.state_dimension is None:
            return None
        return self.stored_macro_rules * self.state_dimension**2


def presentation_pareto_point(
    action_count: int,
    horizon: int,
    macro_depth: int,
    *,
    state_dimension: int | None = None,
) -> PresentationParetoPoint:
    k = _positive_int(action_count, name="action_count")
    h = _positive_int(horizon, name="horizon")
    d = _positive_int(macro_depth, name="macro_depth")
    if d > h:
        raise ValueError("macro_depth need not exceed the declared horizon")
    if state_dimension is not None:
        _positive_int(state_dimension, name="state_dimension")
    return PresentationParetoPoint(
        action_count=k,
        horizon=h,
        macro_depth=d,
        stored_macro_rules=literal_macro_rule_count(k, d),
        worst_case_execution_blocks=macro_execution_blocks(h, d),
        state_dimension=state_dimension,
    )


def literal_macro_pareto_frontier(
    action_count: int,
    horizon: int,
    *,
    state_dimension: int | None = None,
) -> tuple[PresentationParetoPoint, ...]:
    """Return nondominated literal-macro depths for one declared horizon.

    Storage strictly increases with d.  A depth is dominated whenever increasing
    d did not reduce the worst-case chunk count relative to an earlier point.
    """
    k = _positive_int(action_count, name="action_count")
    h = _positive_int(horizon, name="horizon")
    points = tuple(
        presentation_pareto_point(
            k,
            h,
            depth,
            state_dimension=state_dimension,
        )
        for depth in range(1, h + 1)
    )
    frontier = []
    best_execution = None
    for point in points:
        if best_execution is None or point.worst_case_execution_blocks < best_execution:
            frontier.append(point)
            best_execution = point.worst_case_execution_blocks
    return tuple(frontier)


def full_terminal_readout_rule_count(action_count: int, horizon: int) -> int:
    """Literal terminal answer rows for every nonempty word through horizon."""
    return literal_macro_rule_count(action_count, horizon)


def terminal_readout_scalar_count(
    action_count: int,
    horizon: int,
    source_state_dimension: int,
    observation_dimension: int,
) -> int:
    k = _positive_int(action_count, name="action_count")
    h = _positive_int(horizon, name="horizon")
    b = _positive_int(source_state_dimension, name="source_state_dimension")
    c = _positive_int(observation_dimension, name="observation_dimension")
    return full_terminal_readout_rule_count(k, h) * b * c


def transition_macro_scalar_count(
    action_count: int,
    macro_depth: int,
    state_dimension: int,
) -> int:
    k = _positive_int(action_count, name="action_count")
    d = _positive_int(macro_depth, name="macro_depth")
    b = _positive_int(state_dimension, name="state_dimension")
    return literal_macro_rule_count(k, d) * b * b


def presentation_depth_table(
    action_count: int,
    horizon: int,
) -> tuple[tuple[int, int, int], ...]:
    """Return (macro_depth, stored_rules, execution_blocks) for every d<=h."""
    k = _positive_int(action_count, name="action_count")
    h = _positive_int(horizon, name="horizon")
    return tuple(
        (
            depth,
            literal_macro_rule_count(k, depth),
            macro_execution_blocks(h, depth),
        )
        for depth in range(1, h + 1)
    )
