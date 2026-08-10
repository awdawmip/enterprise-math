"""Fraction-free integer linear-lift compilers for finite future partitions.

A future-safe partition on a finite subset X of Z^d may fail to be an additive
congruence modulo the original finite carrier while still be the restriction of
cosets of an ordinary rational linear subspace in the integer lift.

Let V_E be the Q-span of all differences x-y inside the same partition block.
The generic linear-lift gate succeeds exactly when no inter-block difference lies
in V_E.  If it succeeds, choose any independent integer difference basis B for
V_E.  A completely fraction-free token is obtained from all (rank(B)+1)-column
minors of the matrix formed by B with the state x appended.  Token equality is
equivalent to x-y lying in V_E, so the determinant token has exactly the desired
future fibers.

Codimension one is the smallest specialization: V_E has rank d-1 and its
annihilator has one primitive integer normal c_E, recovered by cofactors.  The
determinant token then reduces to the ordinary integer coordinate c_E·x.

Exterior determinants, rational spans and exact linear algebra are established
prior mathematics.  R004 uses them as a fail-closed compiler gate between
modular quotient states and richer A3/A4 relation/witness states.
"""
from __future__ import annotations

from collections.abc import Sequence
from itertools import combinations
from math import gcd

State = tuple[int, ...]
Partition = tuple[tuple[State, ...], ...]


def _states(states: Sequence[Sequence[int]]) -> tuple[State, ...]:
    points = tuple(tuple(point) for point in states)
    if not points:
        raise ValueError("state set must be nonempty")
    dimension = len(points[0])
    if dimension == 0:
        raise ValueError("states must have positive dimension")
    if any(len(point) != dimension for point in points):
        raise ValueError("states must have common dimension")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for point in points
        for value in point
    ):
        raise ValueError("state coordinates must be integers")
    if len(points) != len(set(points)):
        raise ValueError("states must be distinct")
    return points


def _partition(
    states: Sequence[Sequence[int]], blocks: Sequence[Sequence[Sequence[int]]]
) -> tuple[tuple[State, ...], ...]:
    points = _states(states)
    declared = set(points)
    normalized = []
    seen: set[State] = set()
    for block in blocks:
        row = tuple(tuple(point) for point in block)
        if not row:
            raise ValueError("partition blocks must be nonempty")
        if any(point not in declared for point in row):
            raise ValueError("partition contains undeclared state")
        if len(row) != len(set(row)) or seen & set(row):
            raise ValueError("partition blocks must be disjoint")
        seen.update(row)
        normalized.append(row)
    if seen != declared:
        raise ValueError("partition must cover every state exactly once")
    return tuple(normalized)


def determinant_bareiss(matrix: Sequence[Sequence[int]]) -> int:
    """Exact fraction-free determinant by Bareiss elimination."""
    rows = [list(row) for row in matrix]
    size = len(rows)
    if any(len(row) != size for row in rows):
        raise ValueError("determinant needs a square matrix")
    if size == 0:
        return 1
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for row in rows
        for value in row
    ):
        raise ValueError("matrix entries must be integers")
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        pivot_row = next(
            (row for row in range(pivot_index, size) if rows[row][pivot_index] != 0),
            None,
        )
        if pivot_row is None:
            return 0
        if pivot_row != pivot_index:
            rows[pivot_index], rows[pivot_row] = rows[pivot_row], rows[pivot_index]
            sign = -sign
        pivot = rows[pivot_index][pivot_index]
        for i in range(pivot_index + 1, size):
            for j in range(pivot_index + 1, size):
                numerator = rows[i][j] * pivot - rows[i][pivot_index] * rows[pivot_index][j]
                if previous != 1:
                    if numerator % previous:
                        raise AssertionError("Bareiss division must be exact")
                    numerator //= previous
                rows[i][j] = numerator
            rows[i][pivot_index] = 0
        previous = pivot
    return sign * rows[-1][-1]


def integer_matrix_rank(matrix: Sequence[Sequence[int]]) -> int:
    """Rank over Q via fraction-free elimination."""
    rows = [list(row) for row in matrix]
    if not rows:
        return 0
    width = len(rows[0])
    if any(len(row) != width for row in rows):
        raise ValueError("matrix rows must have common width")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for row in rows
        for value in row
    ):
        raise ValueError("matrix entries must be integers")

    rank = 0
    column = 0
    while rank < len(rows) and column < width:
        pivot_row = next(
            (index for index in range(rank, len(rows)) if rows[index][column] != 0),
            None,
        )
        if pivot_row is None:
            column += 1
            continue
        rows[rank], rows[pivot_row] = rows[pivot_row], rows[rank]
        pivot = rows[rank][column]
        for index in range(len(rows)):
            if index == rank or rows[index][column] == 0:
                continue
            factor = rows[index][column]
            rows[index] = [
                pivot * value - factor * pivot_value
                for value, pivot_value in zip(rows[index], rows[rank])
            ]
            common = 0
            for value in rows[index]:
                common = gcd(common, abs(value))
            if common > 1:
                rows[index] = [value // common for value in rows[index]]
        rank += 1
        column += 1
    return rank


def intra_class_differences(
    states: Sequence[Sequence[int]], blocks: Sequence[Sequence[Sequence[int]]]
) -> tuple[State, ...]:
    points = _states(states)
    partition = _partition(points, blocks)
    output: list[State] = []
    for block in partition:
        base = block[0]
        for point in block[1:]:
            output.append(tuple(value - origin for value, origin in zip(point, base)))
    return tuple(output)


def _independent_rows(rows: Sequence[State], target_rank: int) -> tuple[State, ...]:
    if target_rank == 0:
        return ()
    selected: list[State] = []
    current_rank = 0
    for row in rows:
        candidate = (*selected, row)
        candidate_rank = integer_matrix_rank(candidate)
        if candidate_rank > current_rank:
            selected.append(row)
            current_rank = candidate_rank
            if current_rank == target_rank:
                break
    if current_rank != target_rank:
        raise ValueError("could not select required independent rows")
    return tuple(selected)


def linear_lift_difference_basis(
    states: Sequence[Sequence[int]], blocks: Sequence[Sequence[Sequence[int]]]
) -> tuple[State, ...]:
    points = _states(states)
    partition = _partition(points, blocks)
    differences = intra_class_differences(points, partition)
    rank = integer_matrix_rank(differences)
    return _independent_rows(differences, rank)


def _difference(left: State, right: State) -> State:
    return tuple(a - b for a, b in zip(left, right))


def linear_lift_span_gate_holds(
    states: Sequence[Sequence[int]], blocks: Sequence[Sequence[Sequence[int]]]
) -> bool:
    """Exact criterion for fibers of a rational-linear quotient restricted to X.

    V is generated by intra-class differences.  The gate holds iff no
    inter-class difference already lies in V.
    """
    points = _states(states)
    partition = _partition(points, blocks)
    if len(partition) == 1:
        return True
    basis = linear_lift_difference_basis(points, partition)
    rank = len(basis)
    if rank == len(points[0]):
        return False
    class_index = {
        point: index for index, block in enumerate(partition) for point in block
    }
    for left_index, left in enumerate(points):
        for right in points[left_index + 1 :]:
            if class_index[left] == class_index[right]:
                continue
            if integer_matrix_rank((*basis, _difference(left, right))) == rank:
                return False
    return True


def determinant_relation_token(
    state: Sequence[int],
    basis: Sequence[Sequence[int]],
) -> tuple[int, ...]:
    """Exterior/determinant token for the quotient by span_Q(basis).

    For rank k<d, coordinates are all (k+1)x(k+1) minors of [basis; state].
    Equality of tokens is equivalent to the state difference lying in the
    rational row span of the basis.
    """
    rows = tuple(tuple(row) for row in basis)
    point = tuple(state)
    if not point:
        raise ValueError("state must have positive dimension")
    dimension = len(point)
    if any(len(row) != dimension for row in rows):
        raise ValueError("basis rows and state must have common width")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for row in (*rows, point)
        for value in row
    ):
        raise ValueError("basis/state entries must be integers")
    rank = integer_matrix_rank(rows)
    if rank != len(rows):
        raise ValueError("basis rows must be independent")
    if rank >= dimension:
        return ()
    output = []
    for columns in combinations(range(dimension), rank + 1):
        square = tuple(
            tuple(row[column] for column in columns)
            for row in (*rows, point)
        )
        output.append(determinant_bareiss(square))
    return tuple(output)


def linear_lift_partition_is_exact(
    states: Sequence[Sequence[int]], blocks: Sequence[Sequence[Sequence[int]]]
) -> bool:
    points = _states(states)
    partition = _partition(points, blocks)
    if len(partition) == 1:
        return True
    if not linear_lift_span_gate_holds(points, partition):
        return False
    basis = linear_lift_difference_basis(points, partition)
    token_to_class: dict[tuple[int, ...], int] = {}
    class_index = {
        point: index for index, block in enumerate(partition) for point in block
    }
    for point in points:
        token = determinant_relation_token(point, basis)
        index = class_index[point]
        if token in token_to_class and token_to_class[token] != index:
            return False
        token_to_class[token] = index
    for block in partition:
        if len({determinant_relation_token(point, basis) for point in block}) != 1:
            return False
    return True


def compile_linear_lift_state(
    state: Sequence[int],
    states: Sequence[Sequence[int]],
    blocks: Sequence[Sequence[Sequence[int]]],
) -> tuple[int, ...]:
    points = _states(states)
    point = tuple(state)
    if point not in set(points):
        raise ValueError("state outside declared finite carrier")
    partition = _partition(points, blocks)
    if len(partition) == 1:
        return ()
    if not linear_lift_partition_is_exact(points, partition):
        raise ValueError("partition is not an integer linear-lift quotient on this carrier")
    basis = linear_lift_difference_basis(points, partition)
    return determinant_relation_token(point, basis)


def primitive_codimension_one_normal(
    states: Sequence[Sequence[int]], blocks: Sequence[Sequence[Sequence[int]]]
) -> State:
    """Return the unique primitive integer normal when intra-class rank is d-1."""
    points = _states(states)
    dimension = len(points[0])
    differences = intra_class_differences(points, blocks)
    rank = integer_matrix_rank(differences)
    if rank != dimension - 1:
        raise ValueError("intra-class difference span must have codimension one")
    if dimension == 1:
        normal = (1,)
    else:
        basis = _independent_rows(differences, dimension - 1)
        coordinates = []
        for column in range(dimension):
            minor = tuple(
                tuple(value for index, value in enumerate(row) if index != column)
                for row in basis
            )
            coordinates.append(((-1) ** column) * determinant_bareiss(minor))
        normal = tuple(coordinates)
    common = 0
    for value in normal:
        common = gcd(common, abs(value))
    if common == 0:
        raise AssertionError("codimension-one span must have a nonzero normal")
    primitive = tuple(value // common for value in normal)
    first_nonzero = next(value for value in primitive if value != 0)
    if first_nonzero < 0:
        primitive = tuple(-value for value in primitive)
    return primitive


def linear_coordinate(state: Sequence[int], normal: Sequence[int]) -> int:
    point = tuple(state)
    coefficients = tuple(normal)
    if len(point) != len(coefficients):
        raise ValueError("state and normal widths must match")
    return sum(value * coefficient for value, coefficient in zip(point, coefficients))


def codimension_one_linear_lift_holds(
    states: Sequence[Sequence[int]], blocks: Sequence[Sequence[Sequence[int]]]
) -> bool:
    points = _states(states)
    partition = _partition(points, blocks)
    try:
        normal = primitive_codimension_one_normal(points, partition)
    except ValueError:
        return False
    class_index = {
        point: index for index, block in enumerate(partition) for point in block
    }
    values: dict[int, int] = {}
    for point in points:
        coordinate = linear_coordinate(point, normal)
        index = class_index[point]
        if coordinate in values and values[coordinate] != index:
            return False
        values[coordinate] = index
    for block in partition:
        if len({linear_coordinate(point, normal) for point in block}) != 1:
            return False
    return True


def compile_codimension_one_linear_lift(
    state: Sequence[int],
    states: Sequence[Sequence[int]],
    blocks: Sequence[Sequence[Sequence[int]]],
) -> int:
    points = _states(states)
    point = tuple(state)
    if point not in set(points):
        raise ValueError("state outside declared finite carrier")
    partition = _partition(points, blocks)
    if not codimension_one_linear_lift_holds(points, partition):
        raise ValueError("partition is not a codimension-one integer-linear lift")
    normal = primitive_codimension_one_normal(points, partition)
    return linear_coordinate(point, normal)
