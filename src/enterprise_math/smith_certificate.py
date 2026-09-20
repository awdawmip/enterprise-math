"""Witness-preserving Smith normal form certificate verification.

This candidate subtool extends the existing Enterprise exact integer/cokernel
surfaces.  It does not compute a Smith normal form.  It verifies a proposed
integer certificate

    U * A * V = S

with exact unimodular transition witnesses and canonical Smith diagonal laws.
Returning U and V preserves coordinate/provenance transport that invariant factors
alone erase.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from .discrete_laplacian_chip_firing import determinant

IntMatrix = tuple[tuple[int, ...], ...]


def _matrix(rows: Iterable[Iterable[int]], *, name: str) -> IntMatrix:
    result = tuple(tuple(row) for row in rows)
    if not result:
        raise ValueError(f"{name} must be nonempty")
    width = len(result[0])
    if width == 0 or any(len(row) != width for row in result):
        raise ValueError(f"{name} must be a nonempty rectangular matrix")
    for row in result:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError(f"{name} entries must be integers")
    return result


def _shape(matrix: IntMatrix) -> tuple[int, int]:
    return len(matrix), len(matrix[0])


def _matmul(left: IntMatrix, right: IntMatrix) -> IntMatrix:
    lm, lk = _shape(left)
    rk, rn = _shape(right)
    if lk != rk:
        raise ValueError("matrix dimensions do not compose")
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(lk)) for j in range(rn))
        for i in range(lm)
    )


def _identity(n: int) -> IntMatrix:
    return tuple(tuple(1 if i == j else 0 for j in range(n)) for i in range(n))


def _is_diagonal(matrix: IntMatrix) -> bool:
    m, n = _shape(matrix)
    return all(matrix[i][j] == 0 for i in range(m) for j in range(n) if i != j)


def _diagonal(matrix: IntMatrix) -> tuple[int, ...]:
    m, n = _shape(matrix)
    return tuple(matrix[i][i] for i in range(min(m, n)))


@dataclass(frozen=True, slots=True)
class SmithCertificateSummary:
    rank: int
    free_rank: int
    invariant_factors: tuple[int, ...]
    torsion_order: int
    u_determinant: int
    v_determinant: int


def verify_smith_certificate(
    original: Sequence[Sequence[int]],
    smith: Sequence[Sequence[int]],
    left_transform: Sequence[Sequence[int]],
    right_transform: Sequence[Sequence[int]],
) -> SmithCertificateSummary:
    """Verify a full integer Smith certificate and return exact cokernel data.

    The matrix A is interpreted as Z^n -> Z^m, so coker(A) has free rank m-rank.
    Invariant factors equal to 1 are omitted from the torsion decomposition but
    still count toward rank.
    """

    a = _matrix(original, name="original")
    s = _matrix(smith, name="smith")
    u = _matrix(left_transform, name="left_transform")
    v = _matrix(right_transform, name="right_transform")
    m, n = _shape(a)

    if _shape(s) != (m, n):
        raise ValueError("smith shape must equal original shape")
    if _shape(u) != (m, m):
        raise ValueError("left transform must be m x m")
    if _shape(v) != (n, n):
        raise ValueError("right transform must be n x n")

    det_u = determinant(u)
    det_v = determinant(v)
    if abs(det_u) != 1 or abs(det_v) != 1:
        raise ValueError("transition matrices must be unimodular")

    if _matmul(_matmul(u, a), v) != s:
        raise ValueError("U*A*V does not equal the proposed Smith matrix")
    if not _is_diagonal(s):
        raise ValueError("Smith matrix must be diagonal")

    diag = _diagonal(s)
    seen_zero = False
    nonzero: list[int] = []
    for value in diag:
        if value == 0:
            seen_zero = True
            continue
        if seen_zero:
            raise ValueError("nonzero Smith diagonal cannot follow zero")
        if value < 0:
            raise ValueError("nonzero Smith diagonal entries must be positive")
        nonzero.append(value)

    for left, right in zip(nonzero, nonzero[1:]):
        if right % left != 0:
            raise ValueError("Smith diagonal must satisfy d_i | d_(i+1)")

    rank = len(nonzero)
    free_rank = m - rank
    invariants = tuple(d for d in nonzero if d > 1)
    torsion_order = 1
    for d in invariants:
        torsion_order *= d

    return SmithCertificateSummary(
        rank=rank,
        free_rank=free_rank,
        invariant_factors=invariants,
        torsion_order=torsion_order,
        u_determinant=det_u,
        v_determinant=det_v,
    )
