"""Exact finite compiler for preserving a specified p-adic linear target quotient.

This module is deliberately reference-grade.  It uses finite row-module enumeration so
its semantics are transparent and exact on small carriers.  Faster Smith-normal-form
backends can replace the enumeration without changing the public theorem surface.
"""

from __future__ import annotations

from itertools import combinations, product
from typing import Iterable, Sequence, Tuple

Matrix = Tuple[Tuple[int, ...], ...]


def _matrix(rows: Sequence[Sequence[int]], modulus: int, width: int | None = None) -> Matrix:
    out = tuple(tuple(int(v) % modulus for v in row) for row in rows)
    if out:
        w = len(out[0])
        if any(len(row) != w for row in out):
            raise ValueError("matrix rows must have equal width")
        if width is not None and w != width:
            raise ValueError("matrix width mismatch")
        return out
    if width is None:
        raise ValueError("empty matrix requires explicit width")
    return tuple()


def restrict_columns(matrix: Matrix, columns: Iterable[int]) -> Matrix:
    cols = tuple(columns)
    return tuple(tuple(row[j] for j in cols) for row in matrix)


def row_module_elements(matrix: Matrix, p: int, K: int, *, width: int | None = None,
                        max_combinations: int = 1_000_000) -> frozenset[Tuple[int, ...]]:
    if p < 2 or K < 1:
        raise ValueError("require p>=2 and K>=1")
    modulus = p ** K
    if matrix:
        w = len(matrix[0])
    elif width is not None:
        w = width
    else:
        raise ValueError("empty matrix requires width")
    count = modulus ** len(matrix)
    if count > max_combinations:
        raise ValueError("reference row-module enumeration limit exceeded")
    if not matrix:
        return frozenset({(0,) * w})
    values = set()
    for coeffs in product(range(modulus), repeat=len(matrix)):
        values.add(tuple(sum(coeffs[i] * matrix[i][j] for i in range(len(matrix))) % modulus
                         for j in range(w)))
    return frozenset(values)


def _stack(A: Matrix, B: Matrix) -> Matrix:
    return tuple(A) + tuple(B)


def target_defect_exponent(A: Matrix, B: Matrix, hidden: Iterable[int], p: int, K: int) -> int:
    """Return log_p |(Row(A_H)+Row(B_H))/Row(A_H)| exactly."""
    H = tuple(hidden)
    AH = restrict_columns(A, H)
    CH = restrict_columns(_stack(A, B), H)
    RA = row_module_elements(AH, p, K, width=len(H))
    RC = row_module_elements(CH, p, K, width=len(H))
    if len(RC) % len(RA):
        raise AssertionError("row-module inclusion invariant violated")
    ratio = len(RC) // len(RA)
    exponent = 0
    while ratio > 1:
        if ratio % p:
            raise AssertionError("defect quotient is not a p-group")
        ratio //= p
        exponent += 1
    return exponent


def target_safe(A: Matrix, B: Matrix, retained: Iterable[int], p: int, K: int) -> bool:
    d = len(A[0]) if A else len(B[0])
    retained_set = set(retained)
    hidden = tuple(i for i in range(d) if i not in retained_set)
    return target_defect_exponent(A, B, hidden, p, K) == 0


def target_signature(x: Sequence[int], A: Matrix, retained: Iterable[int], p: int, K: int):
    modulus = p ** K
    x = tuple(int(v) % modulus for v in x)
    observed = tuple(sum(row[j] * x[j] for j in range(len(x))) % modulus for row in A)
    kept = tuple(x[j] for j in sorted(set(retained)))
    return observed, kept


def target_value(x: Sequence[int], B: Matrix, p: int, K: int):
    modulus = p ** K
    x = tuple(int(v) % modulus for v in x)
    return tuple(sum(row[j] * x[j] for j in range(len(x))) % modulus for row in B)


def minimal_target_cuts(A: Matrix, B: Matrix, p: int, K: int) -> Tuple[Tuple[int, ...], ...]:
    """Inclusion-minimal hidden-coordinate sets with nonzero target defect."""
    d = len(A[0]) if A else len(B[0])
    cuts = []
    for size in range(1, d + 1):
        for H in combinations(range(d), size):
            if target_defect_exponent(A, B, H, p, K) == 0:
                continue
            if any(set(C).issubset(H) for C in cuts):
                continue
            cuts.append(H)
    return tuple(cuts)


def rank_mod_p(matrix: Matrix, p: int) -> int:
    if not matrix:
        return 0
    M = [[v % p for v in row] for row in matrix]
    rows_n = len(M)
    cols_n = len(M[0])
    rank = 0
    for col in range(cols_n):
        pivot = next((i for i in range(rank, rows_n) if M[i][col] % p), None)
        if pivot is None:
            continue
        M[rank], M[pivot] = M[pivot], M[rank]
        inv = pow(M[rank][col], -1, p)
        M[rank] = [(v * inv) % p for v in M[rank]]
        for i in range(rows_n):
            if i != rank and M[i][col] % p:
                factor = M[i][col] % p
                M[i] = [(M[i][j] - factor * M[rank][j]) % p for j in range(cols_n)]
        rank += 1
        if rank == rows_n:
            break
    return rank


def field_relative_cuts(A: Matrix, B: Matrix, p: int) -> Tuple[Tuple[int, ...], ...]:
    """K=1 closed form: A-circuits that are independent in stacked [A;B]."""
    d = len(A[0]) if A else len(B[0])
    C = _stack(A, B)
    out = []
    for size in range(1, d + 1):
        for H in combinations(range(d), size):
            AH = restrict_columns(A, H)
            CH = restrict_columns(C, H)
            if rank_mod_p(CH, p) != size:
                continue
            if rank_mod_p(AH, p) == size:
                continue
            if all(rank_mod_p(restrict_columns(A, tuple(j for j in H if j != e)), p) == size - 1
                   for e in H):
                out.append(H)
    return tuple(out)
