"""Typed defect-certificate composition reference rules.

Strong certificate kinds have their own exact composition laws.  Every MAY-capable
certificate may demote to a support relation; this file provides the total support
fallback and the p-adic row-defect short-exact-sequence size certificate.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, FrozenSet, Hashable, Iterable, Mapping, Sequence, Tuple

from .precision_structural_target_cut_compiler import row_module_elements

Relation = FrozenSet[Tuple[Hashable, Hashable]]
Matrix = Tuple[Tuple[int, ...], ...]


def compose_relations(left: Iterable[Tuple[Hashable, Hashable]],
                      right: Iterable[Tuple[Hashable, Hashable]]) -> Relation:
    by_source = defaultdict(set)
    for y, z in right:
        by_source[y].add(z)
    return frozenset((x, z) for x, y in left for z in by_source.get(y, ()))


def reverse_graph(mapping: Mapping[Hashable, Hashable]) -> Relation:
    """Relation from codomain back to every source point."""
    return frozenset((target, source) for source, target in mapping.items())


def coarsen_support_relation(relation: Iterable[Tuple[Hashable, Hashable]],
                            coarse_map: Mapping[Hashable, Hashable]) -> Relation:
    """Exact MAY support after further coarsening the source carrier."""
    return compose_relations(reverse_graph(coarse_map), relation)


def natural_matrix_product(A: Matrix, B: Matrix) -> Matrix:
    if not A or not B:
        return tuple()
    if len(A[0]) != len(B):
        raise ValueError("matrix shape mismatch")
    return tuple(
        tuple(sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0])))
        for i in range(len(A))
    )


def boolean_support(A: Matrix) -> Tuple[Tuple[bool, ...], ...]:
    return tuple(tuple(value != 0 for value in row) for row in A)


def boolean_matrix_product(A: Tuple[Tuple[bool, ...], ...],
                           B: Tuple[Tuple[bool, ...], ...]) -> Tuple[Tuple[bool, ...], ...]:
    if not A or not B:
        return tuple()
    if len(A[0]) != len(B):
        raise ValueError("matrix shape mismatch")
    return tuple(
        tuple(any(A[i][k] and B[k][j] for k in range(len(B))) for j in range(len(B[0])))
        for i in range(len(A))
    )


def count_support_composition_certificate(A: Matrix, B: Matrix) -> bool:
    """Nonzero-count erasure commutes with N-semiring matrix composition."""
    return boolean_support(natural_matrix_product(A, B)) == boolean_matrix_product(
        boolean_support(A), boolean_support(B)
    )


def _matrix_width(*matrices: Matrix) -> int:
    for M in matrices:
        if M:
            return len(M[0])
    raise ValueError("at least one matrix must have a row")


def _row_module(M: Matrix, p: int, K: int, width: int):
    return row_module_elements(M, p, K, width=width)


def _subgroup_sum(A, B, modulus: int):
    return frozenset(tuple((x + y) % modulus for x, y in zip(a, b)) for a in A for b in B)


def _p_exponent(size: int, p: int) -> int:
    if size < 1:
        raise ValueError("size must be positive")
    exponent = 0
    while size > 1:
        if size % p:
            raise ValueError("size is not a p-power")
        size //= p
        exponent += 1
    return exponent


def row_defect_exact_sequence(A_fine: Matrix, A_coarse: Matrix, B: Matrix, p: int, K: int) -> Dict[str, int]:
    """Return exact cardinality/mass data for a nested linear target-defect sequence.

    Let V=Row(A_fine), U=Row(A_coarse), W=Row(B), with U <= V.  Then
      0 -> (W cap V)/(W cap U) -> (U+W)/U -> (V+W)/V -> 0.
    """
    width = _matrix_width(A_fine, A_coarse, B)
    modulus = p ** K
    U = _row_module(A_coarse, p, K, width)
    V = _row_module(A_fine, p, K, width)
    W = _row_module(B, p, K, width)
    if not U.issubset(V):
        raise ValueError("coarse row module must be contained in fine row module")
    UplusW = _subgroup_sum(U, W, modulus)
    VplusW = _subgroup_sum(V, W, modulus)
    WcapU = W.intersection(U)
    WcapV = W.intersection(V)
    d_coarse = len(UplusW) // len(U)
    d_fine = len(VplusW) // len(V)
    incremental = len(WcapV) // len(WcapU)
    if d_coarse != d_fine * incremental:
        raise AssertionError("short exact sequence cardinality invariant violated")
    return {
        "fine_defect_size": d_fine,
        "coarse_defect_size": d_coarse,
        "incremental_defect_size": incremental,
        "fine_mass": _p_exponent(d_fine, p),
        "coarse_mass": _p_exponent(d_coarse, p),
        "incremental_mass": _p_exponent(incremental, p),
    }
