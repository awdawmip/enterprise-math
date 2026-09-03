"""Exact recurrent Weighted-BRC port-collapse signatures.

Foundation extraction of main-backed PRs #1152/#1153.  A stable hidden block is
Schur-eliminated to an exact positive-rational port matrix.  The minimal default
signature stores visible dynamics plus the optional exact hidden loop-zeta
constant needed for absolute global-zeta observers.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Sequence

from .brc_weighted_recurrent import RationalMatrix, RationalMatrixInput, finite_recurrent_mass_analysis


def _determinant(matrix: Sequence[Sequence[Fraction | int]]) -> Fraction:
    n = len(matrix)
    if n == 0:
        return Fraction(1, 1)
    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be square")
    work = [[Fraction(value) for value in row] for row in matrix]
    out = Fraction(1, 1)
    sign = 1
    for col in range(n):
        pivot = next((row for row in range(col, n) if work[row][col] != 0), None)
        if pivot is None:
            return Fraction(0, 1)
        if pivot != col:
            work[col], work[pivot] = work[pivot], work[col]
            sign *= -1
        pivot_value = work[col][col]
        out *= pivot_value
        for row in range(col + 1, n):
            factor = work[row][col] / pivot_value
            for j in range(col, n):
                work[row][j] -= factor * work[col][j]
    return sign * out


def _multiply(left: RationalMatrix, right: RationalMatrix) -> RationalMatrix:
    if not left or not right:
        return ()
    if len(left[0]) != len(right):
        raise ValueError("matrix dimension mismatch")
    return tuple(
        tuple(
            sum((left[i][k] * right[k][j] for k in range(len(right))), Fraction(0, 1))
            for j in range(len(right[0]))
        )
        for i in range(len(left))
    )


def _submatrix(matrix: RationalMatrix, rows: Sequence[int], cols: Sequence[int]) -> RationalMatrix:
    return tuple(tuple(matrix[i][j] for j in cols) for i in rows)


@dataclass(frozen=True)
class RecurrentPortSignature:
    """Minimal exact port signature for current positive-rational observers."""

    boundary_indices: tuple[int, ...]
    effective_matrix: RationalMatrix
    hidden_loop_zeta: Fraction

    @property
    def port_count(self) -> int:
        return len(self.boundary_indices)


def recurrent_port_signature(
    matrix: RationalMatrixInput,
    internal_indices: Sequence[int],
) -> RecurrentPortSignature:
    """Schur-eliminate a stable hidden block and return ``(W_eff,Z_int)``.

    The dynamic signature is ``W_eff`` alone. ``hidden_loop_zeta`` is retained
    only for observers asking for absolute full global zeta/Gamma.
    """
    full = tuple(tuple(Fraction(value) for value in row) for row in matrix)
    n = len(full)
    if n == 0 or any(len(row) != n for row in full):
        raise ValueError("matrix must be nonempty and square")
    if any(value < 0 for row in full for value in row):
        raise ValueError("matrix entries must be non-negative")
    internal = tuple(sorted(internal_indices))
    if not internal or len(internal) >= n or len(set(internal)) != len(internal):
        raise ValueError("internal_indices must be a nonempty proper state subset")
    if any(isinstance(i, bool) or not isinstance(i, int) or i < 0 or i >= n for i in internal):
        raise ValueError("internal state index out of range")
    internal_set = set(internal)
    boundary = tuple(i for i in range(n) if i not in internal_set)

    a = _submatrix(full, internal, internal)
    x = _submatrix(full, internal, boundary)
    y = _submatrix(full, boundary, internal)
    b = _submatrix(full, boundary, boundary)
    hidden = finite_recurrent_mass_analysis(a)
    if not hidden.stable or hidden.star is None:
        raise ValueError("hidden/internal block must be stable")
    excursion = _multiply(_multiply(y, hidden.star), x)
    effective = tuple(
        tuple(b[i][j] + excursion[i][j] for j in range(len(boundary)))
        for i in range(len(boundary))
    )
    hidden_zeta = _determinant(hidden.star)
    if hidden_zeta < 1:
        raise AssertionError("positive hidden loop zeta must be >=1")
    return RecurrentPortSignature(boundary, effective, hidden_zeta)


def recurrent_port_dynamic_equivalent(
    left: RecurrentPortSignature,
    right: RecurrentPortSignature,
) -> bool:
    """Exact same-labeled-port dynamic contextual equivalence predicate."""
    return left.port_count == right.port_count and left.effective_matrix == right.effective_matrix


def recurrent_port_zeta_equivalent(
    left: RecurrentPortSignature,
    right: RecurrentPortSignature,
) -> bool:
    """Dynamic equivalence plus equality of absolute hidden loop-zeta constant."""
    return recurrent_port_dynamic_equivalent(left, right) and left.hidden_loop_zeta == right.hidden_loop_zeta


def recurrent_port_context_matrix(
    signature: RecurrentPortSignature,
    port_update: RationalMatrixInput,
    port_to_external: RationalMatrixInput,
    external_to_port: RationalMatrixInput,
    external_matrix: RationalMatrixInput,
) -> RationalMatrix:
    """Build the exact visible reduced composite for an allowed port context."""
    w = signature.effective_matrix
    p = signature.port_count
    c = tuple(tuple(Fraction(value) for value in row) for row in port_update)
    u = tuple(tuple(Fraction(value) for value in row) for row in port_to_external)
    v = tuple(tuple(Fraction(value) for value in row) for row in external_to_port)
    r = tuple(tuple(Fraction(value) for value in row) for row in external_matrix)
    e = len(r)
    if any(value < 0 for matrix in (c, u, v, r) for row in matrix for value in row):
        raise ValueError("context matrices must be non-negative")
    if len(c) != p or any(len(row) != p for row in c):
        raise ValueError("port_update must be port_count square")
    if len(u) != p or any(len(row) != e for row in u):
        raise ValueError("port_to_external shape mismatch")
    if len(v) != e or any(len(row) != p for row in v):
        raise ValueError("external_to_port shape mismatch")
    if any(len(row) != e for row in r):
        raise ValueError("external_matrix must be square")
    out = [[Fraction(0, 1) for _ in range(p + e)] for _ in range(p + e)]
    for i in range(p):
        for j in range(p):
            out[i][j] = w[i][j] + c[i][j]
        for j in range(e):
            out[i][p + j] = u[i][j]
    for i in range(e):
        for j in range(p):
            out[p + i][j] = v[i][j]
        for j in range(e):
            out[p + i][p + j] = r[i][j]
    return tuple(tuple(row) for row in out)
