"""Module/rank specialization of the R004 structural obstruction compiler.

State is a finite free Z/p^K-module, current observation is linear, and future
instructions reset individual coordinates.  Under primitive-column assumptions,
minimal carrier cuts are the circuits of the column matroid reduced mod p.
"""

from __future__ import annotations

from itertools import combinations
from typing import FrozenSet, Iterable, Sequence, Tuple


def matrix_vector_mod(matrix: Sequence[Sequence[int]], vector: Sequence[int], modulus: int) -> Tuple[int, ...]:
    if modulus <= 0:
        raise ValueError("modulus must be positive")
    return tuple(sum(a * x for a, x in zip(row, vector)) % modulus for row in matrix)


def rank_mod_prime(matrix: Sequence[Sequence[int]], p: int, columns: Iterable[int] | None = None) -> int:
    if p <= 1:
        raise ValueError("p must be prime-sized (>1)")
    if not matrix:
        return 0
    d = len(matrix[0])
    cols = tuple(range(d)) if columns is None else tuple(sorted(columns))
    M = [[row[j] % p for j in cols] for row in matrix]
    rows = len(M)
    cols_n = len(cols)
    rank = 0
    col = 0
    while rank < rows and col < cols_n:
        pivot = next((i for i in range(rank, rows) if M[i][col] % p), None)
        if pivot is None:
            col += 1
            continue
        M[rank], M[pivot] = M[pivot], M[rank]
        inv = pow(M[rank][col], -1, p)
        M[rank] = [(v * inv) % p for v in M[rank]]
        for i in range(rows):
            if i != rank and M[i][col] % p:
                f = M[i][col] % p
                M[i] = [(M[i][j] - f * M[rank][j]) % p for j in range(cols_n)]
        rank += 1
        col += 1
    return rank


def primitive_columns_mod_p(matrix: Sequence[Sequence[int]], p: int) -> bool:
    if not matrix:
        return True
    d = len(matrix[0])
    return all(any(row[j] % p != 0 for row in matrix) for j in range(d))


def retained_module_signature(
    state: Sequence[int],
    matrix: Sequence[Sequence[int]],
    p: int,
    exponent: int,
    retained: Iterable[int],
) -> Tuple[Tuple[int, ...], Tuple[int, ...]]:
    if exponent < 1:
        raise ValueError("exponent must be >= 1")
    if not primitive_columns_mod_p(matrix, p):
        raise ValueError("every observation column must be primitive mod p")
    modulus = p ** exponent
    kept = tuple(sorted(retained))
    return matrix_vector_mod(matrix, state, modulus), tuple(state[i] % modulus for i in kept)


def _subsets(d: int):
    for r in range(d + 1):
        for c in combinations(range(d), r):
            yield frozenset(c)


def column_circuits_mod_p(matrix: Sequence[Sequence[int]], p: int) -> Tuple[FrozenSet[int], ...]:
    if not matrix:
        return tuple()
    d = len(matrix[0])
    dependent = []
    for support in _subsets(d):
        if support and rank_mod_prime(matrix, p, support) < len(support):
            dependent.append(support)
    circuits = [s for s in dependent if not any(t < s for t in dependent)]
    return tuple(sorted(circuits, key=lambda s: (len(s), tuple(sorted(s)))))


def column_bases_mod_p(matrix: Sequence[Sequence[int]], p: int) -> Tuple[FrozenSet[int], ...]:
    if not matrix:
        return (frozenset(),)
    d = len(matrix[0])
    full_rank = rank_mod_prime(matrix, p)
    bases = [
        support
        for support in _subsets(d)
        if len(support) == full_rank and rank_mod_prime(matrix, p, support) == full_rank
    ]
    return tuple(sorted(bases, key=lambda s: tuple(sorted(s))))


def minimal_reset_carrier_bases(matrix: Sequence[Sequence[int]], p: int) -> Tuple[FrozenSet[int], ...]:
    if not matrix:
        return (frozenset(),)
    d = len(matrix[0])
    ground = frozenset(range(d))
    return tuple(sorted((ground - b for b in column_bases_mod_p(matrix, p)), key=lambda s: tuple(sorted(s))))


def minimal_reset_basis_size(matrix: Sequence[Sequence[int]], p: int) -> int:
    if not matrix:
        return 0
    return len(matrix[0]) - rank_mod_prime(matrix, p)


def hidden_map_is_injective(matrix: Sequence[Sequence[int]], p: int, hidden: Iterable[int]) -> bool:
    hidden = tuple(sorted(hidden))
    return rank_mod_prime(matrix, p, hidden) == len(hidden)
