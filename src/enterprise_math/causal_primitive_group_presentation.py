"""Global translation rank from primitive inverse and local difference relations.

A reversible primitive move system supplies:

* primitive directions R;
* an inverse involution inv(r);
* compatibility adjacency.

For an adjacent pair u~v, a candidate primitive difference w=v-u is defined
purely relationally as the unique direction satisfying

    w ~ v   and   inv(w) ~ u.

When unique, impose the abelian relations

    e_r + e_inv(r) = 0,
    e_v - e_u - e_w = 0.

These define a causal translation presentation without an ambient coordinate
space.  A modular row-rank gives a rigorous lower bound on the rational relation
rank.  An optional exact integer realization can certify completeness: if all
causal relations vanish in a d-dimensional realization spanning rank d and the
modular relation rank is |R|-d, then the causal quotient has rational rank d
exactly.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from .causal_primitive_link_profile import Adjacency, Vector

Inverse = Callable[[Vector], Vector]
SparseRow = dict[int, int]


def unique_primitive_difference_target(
    adjacency: Adjacency,
    inverse: Inverse,
    left: Vector,
    right: Vector,
) -> Vector:
    if left not in adjacency or right not in adjacency[left]:
        raise ValueError("left and right must be primitive-adjacent")
    candidates = tuple(
        candidate
        for candidate in adjacency[right]
        if inverse(candidate) in adjacency[left]
    )
    if len(candidates) != 1:
        raise ValueError("adjacent pair does not determine one primitive difference target")
    return candidates[0]


def primitive_presentation_rows(
    adjacency: Adjacency,
    inverse: Inverse,
) -> tuple[SparseRow, ...]:
    vertices = tuple(adjacency)
    index = {vertex: position for position, vertex in enumerate(vertices)}
    if any(inverse(inverse(vertex)) != vertex for vertex in vertices):
        raise ValueError("inverse must be involutive")
    if any(inverse(vertex) not in adjacency for vertex in vertices):
        raise ValueError("inverse must stay inside primitive family")

    rows: list[SparseRow] = []
    seen_inverse = set()
    for vertex in vertices:
        pair = tuple(sorted((index[vertex], index[inverse(vertex)])))
        if pair in seen_inverse:
            continue
        seen_inverse.add(pair)
        rows.append({pair[0]: 1, pair[1]: 1})

    seen_edges = set()
    for left in vertices:
        for right in adjacency[left]:
            edge = tuple(sorted((index[left], index[right])))
            if edge in seen_edges:
                continue
            seen_edges.add(edge)
            target = unique_primitive_difference_target(adjacency, inverse, left, right)
            rows.append({index[right]: 1, index[left]: -1, index[target]: -1})
    return tuple(rows)


def sparse_rank_mod_prime(
    rows: tuple[SparseRow, ...],
    column_count: int,
    prime: int = 1_000_003,
) -> int:
    """Exact rank over F_p for sparse integer relation rows."""
    if prime <= 2:
        raise ValueError("prime modulus must exceed two")
    pivots: dict[int, dict[int, int]] = {}
    for source in rows:
        vector = {column: value % prime for column, value in source.items() if value % prime}
        while vector:
            column = min(vector)
            pivot = pivots.get(column)
            if pivot is None:
                inverse_pivot = pow(vector[column], prime - 2, prime)
                normalized = {
                    key: (value * inverse_pivot) % prime
                    for key, value in vector.items()
                    if (value * inverse_pivot) % prime
                }
                pivots[column] = normalized
                break
            factor = vector[column]
            for key, value in pivot.items():
                updated = (vector.get(key, 0) - factor * value) % prime
                if updated:
                    vector[key] = updated
                else:
                    vector.pop(key, None)
    if len(pivots) > column_count:
        raise AssertionError("row rank cannot exceed column count")
    return len(pivots)


def dense_coordinate_rank_mod_prime(
    vectors: tuple[Vector, ...],
    prime: int = 1_000_003,
) -> int:
    """Column-span rank of exact integer realization vectors over F_p."""
    if not vectors:
        return 0
    dimension = len(vectors[0])
    rows = tuple(
        {column: vectors[column][coordinate] for column in range(len(vectors)) if vectors[column][coordinate]}
        for coordinate in range(dimension)
    )
    return sparse_rank_mod_prime(rows, len(vectors), prime)


def presentation_relations_hold_in_realization(
    rows: tuple[SparseRow, ...],
    vectors: tuple[Vector, ...],
) -> bool:
    if not vectors:
        return False
    dimension = len(vectors[0])
    return all(
        all(
            sum(coefficient * vectors[column][coordinate] for column, coefficient in row.items()) == 0
            for coordinate in range(dimension)
        )
        for row in rows
    )


@dataclass(frozen=True)
class PresentationRankCertificate:
    primitive_count: int
    modular_relation_rank: int
    realization_span_rank: int
    certified_translation_rank: int | None
    relations_hold_in_realization: bool


def certify_translation_rank_with_realization(
    adjacency: Adjacency,
    inverse: Inverse,
    realization_vectors: tuple[Vector, ...],
    prime: int = 1_000_003,
) -> PresentationRankCertificate:
    vertices = tuple(adjacency)
    if tuple(realization_vectors) != vertices:
        raise ValueError("realization vectors must use the adjacency vertex order")
    rows = primitive_presentation_rows(adjacency, inverse)
    relation_rank = sparse_rank_mod_prime(rows, len(vertices), prime)
    span_rank = dense_coordinate_rank_mod_prime(vertices, prime)
    relations_hold = presentation_relations_hold_in_realization(rows, vertices)
    certified = None
    if relations_hold and relation_rank + span_rank == len(vertices):
        certified = span_rank
    return PresentationRankCertificate(
        primitive_count=len(vertices),
        modular_relation_rank=relation_rank,
        realization_span_rank=span_rank,
        certified_translation_rank=certified,
        relations_hold_in_realization=relations_hold,
    )
