"""Exact integer future-observability diagnostics.

For an integer state ``x in Z^n``, collect every declared linear future
observation row through one horizon into an integer matrix

    O : Z^n -> Z^m.

Two states are future-equivalent for this declared linear language exactly when

    O(x-y)=0.

Thus the hidden free rank is

    n - rank_Q(O).

A second integer-lattice question is independent of hidden-state rank.  Let ``r``
be the rational rank of ``O``.  The gcd of all nonzero ``r x r`` minors is the
saturation index of the observation row lattice inside its rational row space.
When ``r=n`` the state is already uniquely determined by the full observation
vector, but an index greater than one means the observation rows are not a
unimodular integer coordinate system: exact reconstruction by integer linear
combinations of the observed coordinates is impossible without an additional
integer-coordinate transformation / rational denominator.

Hence future precision has two independent linear integer coordinates:

* ``hidden_rank = n-rank_Q(O)``;
* ``observation_saturation_index``.

Adding future observations never enlarges the kernel.  Once full column rank has
been reached, adding rows can still reduce the maximal-minor gcd, so a future
language can improve integer coordinate quality even after states are already
uniquely distinguishable.

For one linear transition ``A`` and observation matrix ``C``, the ordinary
finite-horizon observability matrix is

    [ C ; C A ; ... ; C A^h ].

This module uses that standard construction only as an integer exact compiler;
no continuum/control-theory ontology is asserted.

The TTL age queue gives a sharp unimodular example: the state is the age
histogram, ``A`` shifts every surviving bucket one step older while dropping the
oldest, and ``C=(1,...,1)`` observes only total queue.  At horizon ``D-1`` the
observability matrix is full-rank with saturation index 1, matching the exact
integer-difference reconstruction already derived in E001.

A contrasting future-policy ledger example can be injective with saturation
index 2: three pair-partitions of four compartments uniquely determine the
ledger but not through a unimodular component-sum coordinate basis.

Rank, Smith/minor divisors, integer observability and lattice saturation are
standard prior mathematics.  This module only packages the exact A2/P023
precision diagnostics.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations, product
from math import gcd
from typing import Iterable, Sequence


Vector = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]


def _integer_matrix(values: Iterable[Sequence[int]], *, allow_empty: bool = False) -> Matrix:
    matrix = tuple(tuple(row) for row in values)
    if not matrix:
        if allow_empty:
            return ()
        raise ValueError("matrix must contain at least one row")
    width = len(matrix[0])
    if width == 0:
        raise ValueError("matrix rows must be nonempty")
    if any(len(row) != width for row in matrix):
        raise ValueError("matrix rows must have equal width")
    for row in matrix:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError("matrix entries must be integers")
    return matrix


def _integer_vector(values: Sequence[int], width: int) -> Vector:
    vector = tuple(values)
    if len(vector) != width:
        raise ValueError("vector width mismatch")
    for value in vector:
        if isinstance(value, bool) or not isinstance(value, int):
            raise TypeError("vector entries must be integers")
    return vector


def apply_integer_matrix(matrix: Matrix, vector: Sequence[int]) -> Vector:
    normalized = _integer_matrix(matrix)
    values = _integer_vector(vector, len(normalized[0]))
    return tuple(
        sum(coefficient * value for coefficient, value in zip(row, values, strict=True))
        for row in normalized
    )


def integer_matrix_product(left: Matrix, right: Matrix) -> Matrix:
    a = _integer_matrix(left)
    b = _integer_matrix(right)
    if len(a[0]) != len(b):
        raise ValueError("matrix product dimension mismatch")
    return tuple(
        tuple(
            sum(a[row][inner] * b[inner][column] for inner in range(len(b)))
            for column in range(len(b[0]))
        )
        for row in range(len(a))
    )


def integer_identity(size: int) -> Matrix:
    if isinstance(size, bool) or not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size <= 0:
        raise ValueError("size must be positive")
    return tuple(
        tuple(int(row == column) for column in range(size))
        for row in range(size)
    )


def integer_matrix_power(matrix: Matrix, exponent: int) -> Matrix:
    normalized = _integer_matrix(matrix)
    if len(normalized) != len(normalized[0]):
        raise ValueError("matrix power requires a square matrix")
    if isinstance(exponent, bool) or not isinstance(exponent, int):
        raise TypeError("exponent must be an integer")
    if exponent < 0:
        raise ValueError("exponent must be nonnegative")
    result = integer_identity(len(normalized))
    base = normalized
    power = exponent
    while power:
        if power & 1:
            result = integer_matrix_product(result, base)
        power //= 2
        if power:
            base = integer_matrix_product(base, base)
    return result


def integer_matrix_rank(matrix: Matrix) -> int:
    normalized = _integer_matrix(matrix, allow_empty=True)
    if not normalized:
        return 0
    work = [[Fraction(value) for value in row] for row in normalized]
    width = len(work[0])
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


def _bareiss_determinant(square: Matrix) -> int:
    matrix = _integer_matrix(square, allow_empty=True)
    size = len(matrix)
    if size == 0:
        return 1
    if any(len(row) != size for row in matrix):
        raise ValueError("determinant requires a square matrix")
    work = [list(row) for row in matrix]
    sign = 1
    previous = 1
    for pivot_index in range(size - 1):
        if work[pivot_index][pivot_index] == 0:
            replacement = next(
                (
                    row
                    for row in range(pivot_index + 1, size)
                    if work[row][pivot_index] != 0
                ),
                None,
            )
            if replacement is None:
                return 0
            work[pivot_index], work[replacement] = work[replacement], work[pivot_index]
            sign *= -1
        pivot = work[pivot_index][pivot_index]
        for row in range(pivot_index + 1, size):
            for column in range(pivot_index + 1, size):
                numerator = (
                    work[row][column] * pivot
                    - work[row][pivot_index] * work[pivot_index][column]
                )
                if numerator % previous != 0:
                    raise AssertionError("Bareiss division lost exactness")
                work[row][column] = numerator // previous
            work[row][pivot_index] = 0
        previous = pivot
    return sign * work[-1][-1]


def maximal_minor_gcd(matrix: Matrix) -> int:
    """Gcd of all nonzero maximal-rank minors; row-lattice saturation index."""
    normalized = _integer_matrix(matrix, allow_empty=True)
    if not normalized:
        return 1
    rank = integer_matrix_rank(normalized)
    if rank == 0:
        return 1
    row_count = len(normalized)
    column_count = len(normalized[0])
    common = 0
    for row_indices in combinations(range(row_count), rank):
        for column_indices in combinations(range(column_count), rank):
            square = tuple(
                tuple(normalized[row][column] for column in column_indices)
                for row in row_indices
            )
            determinant = abs(_bareiss_determinant(square))
            if determinant:
                common = gcd(common, determinant)
                if common == 1:
                    return 1
    if common == 0:
        raise AssertionError("rank-positive matrix had no nonzero maximal minor")
    return common


def independent_observation_rows(matrix: Matrix) -> Matrix:
    """Select original rows with the same rational row space and equality kernel."""
    normalized = _integer_matrix(matrix)
    selected: list[Vector] = []
    current_rank = 0
    for row in normalized:
        candidate = tuple((*selected, row))
        candidate_rank = integer_matrix_rank(candidate)
        if candidate_rank > current_rank:
            selected.append(row)
            current_rank = candidate_rank
    return tuple(selected)


def linear_future_equivalent(matrix: Matrix, left: Sequence[int], right: Sequence[int]) -> bool:
    normalized = _integer_matrix(matrix)
    a = _integer_vector(left, len(normalized[0]))
    b = _integer_vector(right, len(normalized[0]))
    difference = tuple(x - y for x, y in zip(a, b, strict=True))
    return not any(apply_integer_matrix(normalized, difference))


@dataclass(frozen=True)
class IntegerFutureObservabilityReport:
    state_dimension: int
    observation_row_count: int
    rational_rank: int
    hidden_free_rank: int
    row_lattice_saturation_index: int

    @property
    def injective_on_integer_state(self) -> bool:
        return self.rational_rank == self.state_dimension

    @property
    def integer_linear_decoder_exists(self) -> bool:
        """Full-rank criterion for an integer left inverse of the observation matrix."""
        return (
            self.injective_on_integer_state
            and self.row_lattice_saturation_index == 1
        )

    @property
    def injective_but_nonunimodular(self) -> bool:
        return (
            self.injective_on_integer_state
            and self.row_lattice_saturation_index > 1
        )


def integer_future_observability_report(matrix: Matrix) -> IntegerFutureObservabilityReport:
    normalized = _integer_matrix(matrix)
    dimension = len(normalized[0])
    rank = integer_matrix_rank(normalized)
    return IntegerFutureObservabilityReport(
        state_dimension=dimension,
        observation_row_count=len(normalized),
        rational_rank=rank,
        hidden_free_rank=dimension - rank,
        row_lattice_saturation_index=maximal_minor_gcd(normalized),
    )


def finite_horizon_observability_matrix(
    transition: Matrix,
    observation_rows: Matrix,
    horizon: int,
) -> Matrix:
    """Return stacked ``C A^t`` rows for ``t=0..h``."""
    a = _integer_matrix(transition)
    c = _integer_matrix(observation_rows)
    if len(a) != len(a[0]):
        raise ValueError("transition must be square")
    if len(c[0]) != len(a):
        raise ValueError("observation width must equal state dimension")
    if isinstance(horizon, bool) or not isinstance(horizon, int):
        raise TypeError("horizon must be an integer")
    if horizon < 0:
        raise ValueError("horizon must be nonnegative")
    rows: list[Vector] = []
    for exponent in range(horizon + 1):
        power = integer_matrix_power(a, exponent)
        block = integer_matrix_product(c, power)
        rows.extend(block)
    return tuple(rows)


def horizon_observability_reports(
    transition: Matrix,
    observation_rows: Matrix,
    maximum_horizon: int,
) -> tuple[IntegerFutureObservabilityReport, ...]:
    if isinstance(maximum_horizon, bool) or not isinstance(maximum_horizon, int):
        raise TypeError("maximum_horizon must be an integer")
    if maximum_horizon < 0:
        raise ValueError("maximum_horizon must be nonnegative")
    return tuple(
        integer_future_observability_report(
            finite_horizon_observability_matrix(
                transition,
                observation_rows,
                horizon,
            )
        )
        for horizon in range(maximum_horizon + 1)
    )


def full_rank_refinement_index_divides(
    earlier: Matrix,
    later: Matrix,
) -> bool:
    """Check the exact divisibility law when ``later`` extends a full-rank row family.

    If every earlier row is present in the same order at the start of ``later``
    and both matrices have full column rank, the later maximal-minor gcd divides
    the earlier one because the gcd is taken over a superset of maximal minors.
    """
    first = _integer_matrix(earlier)
    second = _integer_matrix(later)
    if len(first[0]) != len(second[0]):
        raise ValueError("observation dimensions must agree")
    if tuple(second[: len(first)]) != first:
        raise ValueError("later observation family must extend earlier rows by prefix")
    dimension = len(first[0])
    if integer_matrix_rank(first) != dimension or integer_matrix_rank(second) != dimension:
        raise ValueError("both observation families must already have full column rank")
    old_index = maximal_minor_gcd(first)
    new_index = maximal_minor_gcd(second)
    if old_index % new_index != 0:
        raise AssertionError("added observations violated maximal-minor gcd divisibility")
    return True
