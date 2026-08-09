"""Causal future distinguishability on integer linear state systems.

This module intentionally reverses the usual ontology.  The primitive data are
integer states, allowed future operations, and integer observations.  Linear
algebraic objects (row span, kernel, rank) are derived summaries of which state
differences can still affect any allowed finite future observation.

For X = Z^k, operation matrices B_a, and observation rows W, define the depth-t
future observation rows by pulling W backwards through every operation word of
length at most t.  Their common integer kernel is exactly the set of differences
that no future of depth <= t can observe.

Because the cumulative rational row span only grows inside Q^k, and equality of
a cumulative span makes it invariant under every declared operation, the closure
stabilizes after at most k strict rank increases even though X itself is infinite.
No floating point, limits, or continuous completion are used.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd


Vector = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]
RowFamily = tuple[Vector, ...]


@dataclass(frozen=True)
class CausalFutureClosure:
    state_dimension: int
    levels: tuple[RowFamily, ...]
    ranks: tuple[int, ...]
    stable_depth: int

    @property
    def causal_visible_rank(self) -> int:
        """Free rank of state directions distinguishable by some finite future."""
        return self.ranks[-1]

    @property
    def causal_invisible_rank(self) -> int:
        """Rank of the stable future-invisible subgroup."""
        return self.state_dimension - self.causal_visible_rank

    @property
    def stable_rows(self) -> RowFamily:
        return self.levels[-1]


def _require_matrix(matrix: Matrix, size: int | None = None) -> int:
    if not isinstance(matrix, tuple) or not matrix:
        raise ValueError("matrix must be a non-empty tuple")
    matrix_size = len(matrix)
    if size is not None and matrix_size != size:
        raise ValueError("matrix dimension mismatch")
    if any(not isinstance(row, tuple) or len(row) != matrix_size for row in matrix):
        raise ValueError("matrix must be square")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for row in matrix
        for value in row
    ):
        raise ValueError("matrix entries must be integers")
    return matrix_size


def _require_rows(rows: RowFamily, size: int | None = None) -> int:
    if not isinstance(rows, tuple) or not rows:
        raise ValueError("observations must be a non-empty tuple")
    width = len(rows[0])
    if width == 0:
        raise ValueError("observation rows must be non-empty")
    if size is not None and width != size:
        raise ValueError("observation dimension mismatch")
    if any(not isinstance(row, tuple) or len(row) != width for row in rows):
        raise ValueError("observation rows must have a common width")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for row in rows
        for value in row
    ):
        raise ValueError("observation entries must be integers")
    return width


def _primitive_row(row: Vector) -> Vector:
    divisor = 0
    for value in row:
        divisor = gcd(divisor, abs(value))
    if divisor == 0:
        return tuple(0 for _ in row)
    normalized = tuple(value // divisor for value in row)
    first = next(value for value in normalized if value != 0)
    if first < 0:
        normalized = tuple(-value for value in normalized)
    return normalized


def _normalize_rows(rows: RowFamily) -> RowFamily:
    seen = set()
    result = []
    for row in rows:
        normalized = _primitive_row(row)
        if not any(normalized):
            continue
        if normalized not in seen:
            seen.add(normalized)
            result.append(normalized)
    return tuple(result)


def _integer_rank(rows: RowFamily, width: int) -> int:
    """Exact rational rank via fraction-free integer elimination."""
    if not rows:
        return 0
    data = [list(row) for row in _normalize_rows(rows)]
    pivot_row = 0
    for column in range(width):
        pivot = next(
            (index for index in range(pivot_row, len(data)) if data[index][column]),
            None,
        )
        if pivot is None:
            continue
        data[pivot_row], data[pivot] = data[pivot], data[pivot_row]
        pivot_value = data[pivot_row][column]
        for row_index in range(pivot_row + 1, len(data)):
            entry = data[row_index][column]
            if entry == 0:
                continue
            divisor = gcd(abs(pivot_value), abs(entry))
            left_factor = pivot_value // divisor
            right_factor = entry // divisor
            data[row_index] = [
                left_factor * data[row_index][index]
                - right_factor * data[pivot_row][index]
                for index in range(width)
            ]
            normalized = _primitive_row(tuple(data[row_index]))
            data[row_index] = list(normalized)
        pivot_row += 1
        if pivot_row == len(data):
            break
    return pivot_row


def _row_times_matrix(row: Vector, matrix: Matrix) -> Vector:
    return tuple(
        sum(row[index] * matrix[index][column] for index in range(len(row)))
        for column in range(len(row))
    )


def causal_future_closure(
    operations: tuple[Matrix, ...],
    observations: RowFamily,
) -> CausalFutureClosure:
    """Compute the exact finite future-visible row closure on Z^k.

    `levels[t]` is a cumulative normalized row family whose common kernel equals
    the differences invisible to every declared operation word of length <= t.
    Stabilization occurs when the rational row rank stops increasing; at that
    point the current span is invariant under every declared operation, so no
    later word can add a new distinguishable direction.
    """
    size = _require_rows(observations)
    if not isinstance(operations, tuple):
        raise ValueError("operations must be a tuple")
    for matrix in operations:
        _require_matrix(matrix, size)

    current = _normalize_rows(observations)
    levels = [current]
    ranks = [_integer_rank(current, size)]

    # A strict step raises row rank by at least one, hence there can be at most
    # `size` strict steps.  We nevertheless terminate immediately on equality.
    for _ in range(size + 1):
        generated = list(current)
        for row in current:
            for matrix in operations:
                generated.append(_row_times_matrix(row, matrix))
        next_rows = _normalize_rows(tuple(generated))
        next_rank = _integer_rank(next_rows, size)
        if next_rank == ranks[-1]:
            return CausalFutureClosure(
                state_dimension=size,
                levels=tuple(levels),
                ranks=tuple(ranks),
                stable_depth=len(levels) - 1,
            )
        if next_rank < ranks[-1]:
            raise AssertionError("future-visible row rank cannot decrease")
        current = next_rows
        levels.append(current)
        ranks.append(next_rank)

    raise AssertionError("integer-linear future closure must stabilize within state rank")


def row_dot(row: Vector, vector: Vector) -> int:
    if len(row) != len(vector):
        raise ValueError("row and vector dimension mismatch")
    return sum(left * right for left, right in zip(row, vector))


def future_indistinguishable(
    left: Vector,
    right: Vector,
    closure: CausalFutureClosure,
) -> bool:
    """Whether no declared finite future observation distinguishes two states."""
    if len(left) != closure.state_dimension or len(right) != closure.state_dimension:
        raise ValueError("state dimension mismatch")
    difference = tuple(r - l for l, r in zip(left, right))
    return all(row_dot(row, difference) == 0 for row in closure.stable_rows)


def first_distinguishing_depth(
    left: Vector,
    right: Vector,
    closure: CausalFutureClosure,
) -> int | None:
    """Earliest future depth that distinguishes the states; None means never.

    This is a causal agreement-depth primitive.  If the answer is t, the states
    agree under every operation word of length < t and differ for at least one
    word of length <= t.  `None` denotes stable future equivalence.
    """
    if len(left) != closure.state_dimension or len(right) != closure.state_dimension:
        raise ValueError("state dimension mismatch")
    difference = tuple(r - l for l, r in zip(left, right))
    for depth, rows in enumerate(closure.levels):
        if any(row_dot(row, difference) != 0 for row in rows):
            return depth
    return None


def agreement_depth_ge(
    left: Vector,
    right: Vector,
    closure: CausalFutureClosure,
    depth: int,
) -> bool:
    """Whether two states agree under every future observation up to `depth`."""
    if isinstance(depth, bool) or not isinstance(depth, int) or depth < 0:
        raise ValueError("depth must be a non-negative integer")
    if len(left) != closure.state_dimension or len(right) != closure.state_dimension:
        raise ValueError("state dimension mismatch")
    effective = min(depth, closure.stable_depth)
    difference = tuple(r - l for l, r in zip(left, right))
    return all(row_dot(row, difference) == 0 for row in closure.levels[effective])
