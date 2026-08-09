"""Higher-rank relation-generator radius inside an ambient matrix access norm.

Let ``B`` define the ambient derivative-image access sets ``Z_R(B)`` and let
``Lambda`` be a declared relation subgroup.  Given an integer basis of Lambda,
map each radius-R relation-compatible state to its exact basis coordinates in
``Z^k``.  Those states generate Lambda iff their coordinate subgroup is all of
``Z^k``.

For rank k this is equivalent to rational rank k together with gcd one for all
k x k maximal minors of the coordinate generator matrix.  Rank one recovers
the ordinary gcd criterion used by P025 Stage 31.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations
from math import gcd

from .matrix_access_word_norm import matrix_access_radius, matrix_image_at_radius
from .relation_block_rank import rational_matrix_rank


Vector = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class RelationGenerationLayer:
    radius: int
    accessible_state_count: int
    coordinate_generators: tuple[Vector, ...]
    coordinate_rank: int
    subgroup_index: int | None
    complete: bool


@dataclass(frozen=True)
class RelationGeneratorRadiusResult:
    relation_basis: tuple[Vector, ...]
    first_nonzero_radius: int
    generator_radius: int
    direct_basis_upper_bound: int
    layer_at_generator_radius: RelationGenerationLayer


def _validate_basis(basis: tuple[Vector, ...]) -> tuple[int, int]:
    if not basis:
        raise ValueError("relation basis must be nonempty")
    ambient = len(basis[0])
    if ambient == 0:
        raise ValueError("basis vectors must be nonempty")
    for vector in basis:
        if len(vector) != ambient:
            raise ValueError("basis vectors must share ambient dimension")
        for value in vector:
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError("basis coordinates must be integers")
    if rational_matrix_rank(basis) != len(basis):
        raise ValueError("relation basis vectors must be Q-independent")
    return ambient, len(basis)


def _validate_relation_rows(rows: tuple[Vector, ...], ambient: int) -> None:
    for row in rows:
        if len(row) != ambient:
            raise ValueError("relation rows must match ambient state dimension")
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError("relation coefficients must be integers")


def _relation_ok(rows: tuple[Vector, ...], value: Vector) -> bool:
    return all(
        sum(coefficient * coordinate for coefficient, coordinate in zip(row, value, strict=True)) == 0
        for row in rows
    )


def _solve_square(matrix: list[list[Fraction]], rhs: list[Fraction]) -> list[Fraction]:
    n = len(matrix)
    augmented = [row[:] + [rhs[i]] for i, row in enumerate(matrix)]
    for column in range(n):
        pivot = next(
            (row for row in range(column, n) if augmented[row][column] != 0),
            None,
        )
        if pivot is None:
            raise ValueError("selected basis minor is singular")
        augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
        pivot_value = augmented[column][column]
        augmented[column] = [value / pivot_value for value in augmented[column]]
        for row in range(n):
            if row == column:
                continue
            factor = augmented[row][column]
            if factor == 0:
                continue
            augmented[row] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(augmented[row], augmented[column], strict=True)
            ]
    return [augmented[i][-1] for i in range(n)]


def basis_coordinates(basis: tuple[Vector, ...], value: Vector) -> Vector:
    """Return exact integer coordinates of ``value`` in the declared lattice basis."""
    ambient, rank = _validate_basis(basis)
    if len(value) != ambient:
        raise ValueError("value must match basis ambient dimension")

    # Basis vectors are columns.  Pick any nonsingular rank x rank row minor.
    chosen_rows: tuple[int, ...] | None = None
    for rows in combinations(range(ambient), rank):
        square = tuple(
            tuple(basis[column][row] for column in range(rank))
            for row in rows
        )
        if rational_matrix_rank(square) == rank:
            chosen_rows = rows
            break
    if chosen_rows is None:
        raise AssertionError("independent basis lost a nonsingular row minor")

    matrix = [
        [Fraction(basis[column][row]) for column in range(rank)]
        for row in chosen_rows
    ]
    rhs = [Fraction(value[row]) for row in chosen_rows]
    solution = _solve_square(matrix, rhs)
    if any(item.denominator != 1 for item in solution):
        raise ValueError("value lies in rational span but outside declared integer lattice")
    coordinates = tuple(int(item) for item in solution)
    reconstructed = tuple(
        sum(coordinates[column] * basis[column][row] for column in range(rank))
        for row in range(ambient)
    )
    if reconstructed != value:
        raise ValueError("value lies outside declared relation lattice")
    return coordinates


def _bareiss_determinant(rows: tuple[Vector, ...]) -> int:
    n = len(rows)
    if n == 0:
        return 1
    if any(len(row) != n for row in rows):
        raise ValueError("determinant requires a square matrix")
    matrix = [list(row) for row in rows]
    sign = 1
    previous = 1
    for k in range(n - 1):
        if matrix[k][k] == 0:
            pivot = next((r for r in range(k + 1, n) if matrix[r][k] != 0), None)
            if pivot is None:
                return 0
            matrix[k], matrix[pivot] = matrix[pivot], matrix[k]
            sign *= -1
        pivot_value = matrix[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = matrix[i][j] * pivot_value - matrix[i][k] * matrix[k][j]
                if numerator % previous:
                    raise AssertionError("Bareiss exact division failed")
                matrix[i][j] = numerator // previous
        previous = pivot_value
        for i in range(k + 1, n):
            matrix[i][k] = 0
    return sign * matrix[n - 1][n - 1]


def coordinate_subgroup_index(generators: tuple[Vector, ...], rank: int) -> int | None:
    """Return subgroup index in ``Z^rank``; None means infinite index."""
    if rank <= 0:
        raise ValueError("rank must be positive")
    nonzero = tuple(vector for vector in generators if any(vector))
    if not nonzero:
        return None
    if any(len(vector) != rank for vector in nonzero):
        raise ValueError("coordinate generators must match lattice rank")
    if rational_matrix_rank(nonzero) < rank:
        return None
    minor_gcd = 0
    for selected in combinations(nonzero, rank):
        determinant = abs(_bareiss_determinant(selected))
        minor_gcd = gcd(minor_gcd, determinant)
    if minor_gcd <= 0:
        raise AssertionError("full-rank coordinate generators lost maximal minor")
    return minor_gcd


def relation_generation_layer(
    matrix: Matrix,
    relation_rows: tuple[Vector, ...],
    relation_basis: tuple[Vector, ...],
    radius: int,
) -> RelationGenerationLayer:
    """Return subgroup generated by radius-R relation-compatible ambient states."""
    ambient, rank = _validate_basis(relation_basis)
    _validate_relation_rows(relation_rows, ambient)
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be non-negative")
    for vector in relation_basis:
        if not _relation_ok(relation_rows, vector):
            raise ValueError("declared relation basis must satisfy every relation row")

    accessible = tuple(
        sorted(
            value
            for value in matrix_image_at_radius(matrix, radius)
            if _relation_ok(relation_rows, value)
        )
    )
    coordinates = tuple(basis_coordinates(relation_basis, value) for value in accessible)
    coordinate_rank = rational_matrix_rank(coordinates) if coordinates else 0
    index = coordinate_subgroup_index(coordinates, rank)
    return RelationGenerationLayer(
        radius=radius,
        accessible_state_count=len(accessible),
        coordinate_generators=coordinates,
        coordinate_rank=coordinate_rank,
        subgroup_index=index,
        complete=index == 1,
    )


def exact_relation_generator_radius(
    matrix: Matrix,
    relation_rows: tuple[Vector, ...],
    relation_basis: tuple[Vector, ...],
) -> RelationGeneratorRadiusResult:
    """Return first radius whose accessible relation states generate the full lattice."""
    ambient, _rank = _validate_basis(relation_basis)
    _validate_relation_rows(relation_rows, ambient)
    basis_access = tuple(
        matrix_access_radius(matrix, vector, max_radius=_basis_search_bound(matrix, vector))
        for vector in relation_basis
    )
    upper = max(basis_access)
    first_nonzero: int | None = None
    for radius in range(1, upper + 1):
        layer = relation_generation_layer(matrix, relation_rows, relation_basis, radius)
        if first_nonzero is None and layer.coordinate_rank > 0:
            first_nonzero = radius
        if layer.complete:
            if first_nonzero is None:
                raise AssertionError("complete relation subgroup appeared before any nonzero state")
            return RelationGeneratorRadiusResult(
                relation_basis=relation_basis,
                first_nonzero_radius=first_nonzero,
                generator_radius=radius,
                direct_basis_upper_bound=upper,
                layer_at_generator_radius=layer,
            )
    raise AssertionError("direct access to a declared lattice basis must generate the full subgroup")


def _basis_search_bound(matrix: Matrix, target: Vector) -> int:
    """Construct a safe finite access bound by repeated one-step growth.

    This helper is deliberately conservative.  It searches until the target
    appears; declared relation bases used by the current exact oracle are small.
    """
    radius = 0
    while radius <= 10_000:
        if target in matrix_image_at_radius(matrix, radius):
            return radius
        radius += 1
    raise ValueError("declared relation basis target not reached within safety cap")
