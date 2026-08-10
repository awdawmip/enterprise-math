"""Temporal retirement specializations for representable-matroid cut backends."""

from __future__ import annotations

from itertools import combinations
from typing import Iterable, Sequence, Tuple


def rank_mod_p(columns: Sequence[Sequence[int]], p: int) -> int:
    if not columns:
        return 0
    dim = len(columns[0])
    M = [[int(columns[j][i]) % p for j in range(len(columns))] for i in range(dim)]
    rank = 0
    for col in range(len(columns)):
        pivot = next((i for i in range(rank, dim) if M[i][col] % p), None)
        if pivot is None:
            continue
        M[rank], M[pivot] = M[pivot], M[rank]
        inv = pow(M[rank][col], -1, p)
        M[rank] = [(v * inv) % p for v in M[rank]]
        for i in range(dim):
            if i != rank and M[i][col] % p:
                factor = M[i][col] % p
                M[i] = [(M[i][j] - factor * M[rank][j]) % p for j in range(len(columns))]
        rank += 1
        if rank == dim:
            break
    return rank


def independent(columns: Sequence[Sequence[int]], subset: Iterable[int], p: int) -> bool:
    S = tuple(subset)
    return rank_mod_p(tuple(columns[i] for i in S), p) == len(S)


def extend_to_basis(columns: Sequence[Sequence[int]], seed: Iterable[int], p: int) -> frozenset[int]:
    E = range(len(columns))
    B = set(seed)
    if not independent(columns, B, p):
        raise ValueError("seed must be independent")
    for e in E:
        if e not in B and independent(columns, B | {e}, p):
            B.add(e)
    return frozenset(B)


def nested_cardinality_retirement(matrix_sequence: Sequence[Sequence[Sequence[int]]], p: int):
    """Return nested retained sets, assuming each prior hidden basis stays independent later."""
    if not matrix_sequence:
        return tuple()
    hidden = frozenset()
    retained_schedule = []
    E = frozenset(range(len(matrix_sequence[0])))
    for columns in matrix_sequence:
        if len(columns) != len(E):
            raise ValueError("ground set changed")
        if not independent(columns, hidden, p):
            raise ValueError("independent families are not nested along this sequence")
        hidden = extend_to_basis(columns, hidden, p)
        retained_schedule.append(E - hidden)
    return tuple(retained_schedule)


def all_bases(columns: Sequence[Sequence[int]], p: int) -> Tuple[frozenset[int], ...]:
    r = rank_mod_p(columns, p)
    E = range(len(columns))
    return tuple(frozenset(S) for S in combinations(E, r) if independent(columns, S, p))


def maximum_weight_bases(columns: Sequence[Sequence[int]], weights: Sequence[int], p: int):
    bases = all_bases(columns, p)
    best = max(sum(weights[i] for i in B) for B in bases)
    return tuple(B for B in bases if sum(weights[i] for i in B) == best)
