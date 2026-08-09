"""Finite labelled congruence code for square full-rank certificate lattices.

If a complete labelled certificate image has an integer basis matrix ``G``
with nonzero determinant, then

    C = G Z^q <= Z^q.

The adjugate identity ``adj(G) G = det(G) I`` gives the exact membership test

    y in C  <=>  adj(G) y == 0 mod |det(G)|.

Thus ``adj(G)y mod |det G|`` is a finite labelled quotient code whose kernel is
exactly the certificate lattice.  It need not be a minimal codomain, but it
preserves the exact target-membership kernel without requiring a full Smith
transformation matrix.
"""

from __future__ import annotations

from dataclasses import dataclass

from .certificate_image_index import certificate_basis_generators


Vector = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class AdjugateCertificateCode:
    generator_matrix: Matrix
    determinant: int
    modulus: int
    adjugate: Matrix


def _determinant(matrix: Matrix) -> int:
    n = len(matrix)
    if n == 0:
        return 1
    if any(len(row) != n for row in matrix):
        raise ValueError("determinant requires a square matrix")
    work = [list(row) for row in matrix]
    sign = 1
    previous = 1
    for k in range(n - 1):
        if work[k][k] == 0:
            pivot = next((r for r in range(k + 1, n) if work[r][k] != 0), None)
            if pivot is None:
                return 0
            work[k], work[pivot] = work[pivot], work[k]
            sign *= -1
        pivot_value = work[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                numerator = work[i][j] * pivot_value - work[i][k] * work[k][j]
                if numerator % previous:
                    raise AssertionError("Bareiss exact division failed")
                work[i][j] = numerator // previous
        previous = pivot_value
        for i in range(k + 1, n):
            work[i][k] = 0
    return sign * work[n - 1][n - 1]


def _minor(matrix: Matrix, remove_row: int, remove_column: int) -> Matrix:
    return tuple(
        tuple(value for j, value in enumerate(row) if j != remove_column)
        for i, row in enumerate(matrix)
        if i != remove_row
    )


def _adjugate(matrix: Matrix) -> Matrix:
    n = len(matrix)
    if n == 0:
        return ()
    if n == 1:
        return ((1,),)
    cofactors = tuple(
        tuple(
            ((-1) ** (i + j)) * _determinant(_minor(matrix, i, j))
            for j in range(n)
        )
        for i in range(n)
    )
    return tuple(
        tuple(cofactors[j][i] for j in range(n))
        for i in range(n)
    )


def square_lattice_congruence_code(generator_columns: tuple[Vector, ...]) -> AdjugateCertificateCode:
    """Build the exact adjugate code from a square integer lattice basis.

    ``generator_columns`` are the basis vectors of the labelled image lattice.
    """
    q = len(generator_columns)
    if q == 0:
        raise ValueError("square lattice code requires positive rank")
    if any(len(column) != q for column in generator_columns):
        raise ValueError("need exactly q labelled q-dimensional generator columns")
    matrix = tuple(
        tuple(generator_columns[column][row] for column in range(q))
        for row in range(q)
    )
    determinant = _determinant(matrix)
    if determinant == 0:
        raise ValueError("certificate generator matrix must have full rank")
    adjugate = _adjugate(matrix)

    # Exact identity audit.
    for i in range(q):
        for j in range(q):
            value = sum(adjugate[i][k] * matrix[k][j] for k in range(q))
            expected = determinant if i == j else 0
            if value != expected:
                raise AssertionError("adjugate identity failed")
    return AdjugateCertificateCode(
        generator_matrix=matrix,
        determinant=determinant,
        modulus=abs(determinant),
        adjugate=adjugate,
    )


def square_certificate_congruence_code(
    relation_basis: tuple[Vector, ...],
    certificate_rows: tuple[Vector, ...],
) -> AdjugateCertificateCode:
    """Build a finite labelled code when certificate dimension equals relation rank.

    Full rank of the resulting square matrix means the certificate map is
    injective on the declared relation lattice, so the images of the declared
    relation basis form an integer basis of the complete certificate image.
    """
    if len(certificate_rows) != len(relation_basis):
        raise ValueError("square certificate code requires output dimension = relation rank")
    columns = certificate_basis_generators(relation_basis, certificate_rows)
    return square_lattice_congruence_code(columns)


def certificate_target_code(code: AdjugateCertificateCode, target: Vector) -> Vector:
    """Return the finite labelled residue code of one integer certificate target."""
    q = len(code.generator_matrix)
    if len(target) != q:
        raise ValueError("target dimension must match certificate code")
    return tuple(
        sum(code.adjugate[i][j] * target[j] for j in range(q)) % code.modulus
        for i in range(q)
    )


def certificate_target_is_attainable(code: AdjugateCertificateCode, target: Vector) -> bool:
    """Return exact membership in the complete square certificate lattice."""
    return all(value == 0 for value in certificate_target_code(code, target))


def certificate_target_coordinates(code: AdjugateCertificateCode, target: Vector) -> Vector:
    """Recover integer lattice coordinates of an attainable target."""
    q = len(code.generator_matrix)
    if len(target) != q:
        raise ValueError("target dimension must match certificate code")
    numerators = tuple(
        sum(code.adjugate[i][j] * target[j] for j in range(q))
        for i in range(q)
    )
    det = code.determinant
    if any(value % det for value in numerators):
        raise ValueError("target is outside the certificate lattice")
    coordinates = tuple(value // det for value in numerators)
    reconstructed = tuple(
        sum(code.generator_matrix[row][column] * coordinates[column] for column in range(q))
        for row in range(q)
    )
    if reconstructed != target:
        raise AssertionError("adjugate coordinates failed target reconstruction")
    return coordinates
