"""Unmodified four-function excerpt for actual T12 executable reuse.

Source: awdawmip/enterprise-math@88251de1923cc4cea75691d3d3809d1990b14c03
scripts/tool_discovery_tropical_residuation_idempotent_closure_check.py
Full source Git blob: dfa5b863999c81648c4deaf963bb344505f8119a.
Only envelope, identity_matrix, matrix_envelope, floyd_warshall_star are retained.
The source's 40-check main suite is NOT copied or claimed to have been run.
"""
from __future__ import annotations
Weight = int | None
Matrix = list[list[Weight]]


def envelope(a: Weight, b: Weight, kind: str) -> Weight:
    if a is None:
        return b
    if b is None:
        return a
    if kind == "min":
        return min(a, b)
    if kind == "max":
        return max(a, b)
    raise ValueError(kind)


def identity_matrix(n: int) -> Matrix:
    return [[0 if i == j else None for j in range(n)] for i in range(n)]


def matrix_envelope(A: Matrix, B: Matrix, kind: str) -> Matrix:
    return [
        [envelope(A[i][j], B[i][j], kind) for j in range(len(A[0]))]
        for i in range(len(A))
    ]


def floyd_warshall_star(A: Matrix, kind: str) -> Matrix:
    """All-pairs closure over simple-path representatives."""
    n = len(A)
    D = matrix_envelope(identity_matrix(n), [row[:] for row in A], kind)
    for k in range(n):
        for i in range(n):
            if D[i][k] is None:
                continue
            for j in range(n):
                if D[k][j] is None:
                    continue
                candidate = D[i][k] + D[k][j]
                D[i][j] = envelope(D[i][j], candidate, kind)
    return D
