"""Determinantal/Smith precision profile for integer future observation matrices.

The integer future-observability bridge separates hidden free rank from one
maximal-minor saturation index.  The full unimodular-equivalence invariant is
the determinantal-divisor / Smith profile.

For integer matrix ``O`` and ``Delta_0=1``, define

    Delta_k(O) = gcd of all k x k minors,

with ``Delta_k=0`` once ``k`` exceeds the rational rank.  For every
``1<=k<=r=rank_Q(O)``, standard Smith theory gives

    d_k = Delta_k / Delta_(k-1),

and

    d_1 | d_2 | ... | d_r.

The resulting precision profile is

    hidden_free_rank = n-r,
    smith_factors = (d_1,...,d_r).

Interpretation for a state observation map ``O:Z^n->Z^m``:

* zero rank directions correspond to future-hidden free state directions;
* nonunit Smith factors describe the non-unimodular embedding of the observable
  state image in the ambient integer observation coordinates;
* when ``r=n`` and every ``d_k=1`` (equivalently ``Delta_n=1``), an integer
  linear left decoder exists.

For a row-extension obtained by adding future observations, every existing
``k``-minor from the old matrix remains available in the new matrix.  Therefore
whenever ``Delta_k(old)`` is nonzero,

    Delta_k(new) divides Delta_k(old).

This gives an exact divisibility filtration of integer future precision.  Rank
can increase when a previously zero higher divisor becomes nonzero; after full
rank, future observations can still lower determinantal divisors and remove
coordinate torsion without changing state distinguishability.

These are standard Smith-normal-form/determinantal-divisor facts.  The project
value is using the complete profile as an integer precision coordinate for
future observation languages.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from math import gcd

from .integer_future_observability import integer_matrix_rank


Matrix = tuple[tuple[int, ...], ...]


def _matrix(values: Matrix) -> Matrix:
    matrix = tuple(tuple(row) for row in values)
    if not matrix:
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


def _bareiss_determinant(square: Matrix) -> int:
    size = len(square)
    if size == 0:
        return 1
    if any(len(row) != size for row in square):
        raise ValueError("determinant requires a square matrix")
    work = [list(row) for row in square]
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


def determinantal_divisor(matrix: Matrix, order: int) -> int:
    """Return ``Delta_order``; zero iff requested order exceeds rational rank."""
    normalized = _matrix(matrix)
    if isinstance(order, bool) or not isinstance(order, int):
        raise TypeError("order must be an integer")
    if order < 0:
        raise ValueError("order must be nonnegative")
    if order == 0:
        return 1
    row_count = len(normalized)
    column_count = len(normalized[0])
    if order > min(row_count, column_count):
        return 0
    common = 0
    for row_indices in combinations(range(row_count), order):
        for column_indices in combinations(range(column_count), order):
            square = tuple(
                tuple(normalized[row][column] for column in column_indices)
                for row in row_indices
            )
            determinant = abs(_bareiss_determinant(square))
            common = gcd(common, determinant)
            if common == 1:
                return 1
    return common


def determinantal_divisors(matrix: Matrix) -> tuple[int, ...]:
    """Return ``(Delta_1,...,Delta_n)`` through state-column dimension."""
    normalized = _matrix(matrix)
    dimension = len(normalized[0])
    return tuple(
        determinantal_divisor(normalized, order)
        for order in range(1, dimension + 1)
    )


def smith_invariant_factors_from_minors(matrix: Matrix) -> tuple[int, ...]:
    """Return nonzero Smith invariant factors using exact determinantal divisors."""
    normalized = _matrix(matrix)
    rank = integer_matrix_rank(normalized)
    previous = 1
    factors = []
    for order in range(1, rank + 1):
        current = determinantal_divisor(normalized, order)
        if current <= 0:
            raise AssertionError("positive-rank Smith divisor unexpectedly vanished")
        if current % previous != 0:
            raise AssertionError("determinantal divisors violated Smith divisibility")
        factor = current // previous
        if factors and factor % factors[-1] != 0:
            raise AssertionError("Smith invariant factors lost divisibility order")
        factors.append(factor)
        previous = current
    return tuple(factors)


@dataclass(frozen=True)
class IntegerSmithPrecisionProfile:
    state_dimension: int
    rational_rank: int
    hidden_free_rank: int
    determinantal_divisors: tuple[int, ...]
    smith_invariant_factors: tuple[int, ...]

    @property
    def full_rank(self) -> bool:
        return self.rational_rank == self.state_dimension

    @property
    def integer_unimodular(self) -> bool:
        return self.full_rank and all(
            factor == 1 for factor in self.smith_invariant_factors
        )

    @property
    def maximal_nonzero_determinantal_divisor(self) -> int:
        if self.rational_rank == 0:
            return 1
        return self.determinantal_divisors[self.rational_rank - 1]


def integer_smith_precision_profile(matrix: Matrix) -> IntegerSmithPrecisionProfile:
    normalized = _matrix(matrix)
    dimension = len(normalized[0])
    rank = integer_matrix_rank(normalized)
    divisors = determinantal_divisors(normalized)
    factors = smith_invariant_factors_from_minors(normalized)
    return IntegerSmithPrecisionProfile(
        state_dimension=dimension,
        rational_rank=rank,
        hidden_free_rank=dimension - rank,
        determinantal_divisors=divisors,
        smith_invariant_factors=factors,
    )


def row_extension_determinantal_refinement(
    earlier: Matrix,
    later: Matrix,
) -> tuple[bool, ...]:
    """Verify every nonzero old determinantal divisor is refined by divisibility."""
    first = _matrix(earlier)
    second = _matrix(later)
    if len(first[0]) != len(second[0]):
        raise ValueError("state dimensions must agree")
    if tuple(second[: len(first)]) != first:
        raise ValueError("later observation family must extend earlier rows by prefix")
    old = determinantal_divisors(first)
    new = determinantal_divisors(second)
    checks = []
    for old_value, new_value in zip(old, new, strict=True):
        if old_value == 0:
            checks.append(True)
            continue
        if new_value == 0 or old_value % new_value != 0:
            raise AssertionError("future row extension violated determinantal divisibility")
        checks.append(True)
    return tuple(checks)
