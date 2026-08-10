"""Matrix relation-rank compiler for structured coupled future languages.

Let X=(Z/p^K Z)^d and let an integer rxd matrix A define the relation vector
R_A(x)=A x mod p^K.  If A has full row rank modulo p, one r x r minor is a
p-adic unit and R_A is surjective onto (Z/p^K Z)^r.

When the declared observable is the full vector of capped p-adic valuations of
the relation coordinates, componentwise state translations induce relation
translations R_A(a).  By product-signature factorization, correlated induced
actions may be projected to the r relation axes and each axis compiled by the
one-dimensional p-adic translation trie.

Thus future-safe state complexity is controlled by the observable relation rank,
not automatically by ambient state dimension.  Under full translations the
exact class count is p^(K*r), compared with p^(K*d) exact ambient states; the
integer exponent codimension is K*(d-r).

Matrix rank, invertible minors over Z/p^K Z and linear relation coordinates are
prior algebra.  This is an R004 consumer of A3/P023/P024 interfaces.
"""
from __future__ import annotations

from collections.abc import Sequence
from itertools import product
from math import prod

from enterprise_math.precision_translation_trie_compiler import (
    TrieToken,
    compile_translation_trie_state,
    translation_trie_class_count,
)
from enterprise_math.precision_valuation_repair import capped_p_valuation

Matrix = tuple[tuple[int, ...], ...]
State = tuple[int, ...]
RelationToken = tuple[TrieToken, ...]


def _prime(prime: int) -> None:
    if isinstance(prime, bool) or not isinstance(prime, int) or prime < 2:
        raise ValueError("prime must be prime")
    divisor = 2
    while divisor * divisor <= prime:
        if prime % divisor == 0:
            raise ValueError("prime must be prime")
        divisor += 1


def _cap(cap: int) -> None:
    if isinstance(cap, bool) or not isinstance(cap, int) or cap <= 0:
        raise ValueError("cap must be positive")


def _matrix(matrix: Sequence[Sequence[int]]) -> Matrix:
    rows = tuple(tuple(row) for row in matrix)
    if not rows or not rows[0]:
        raise ValueError("relation matrix must be nonempty")
    width = len(rows[0])
    if any(len(row) != width for row in rows):
        raise ValueError("relation matrix rows must have common width")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for row in rows
        for value in row
    ):
        raise ValueError("relation matrix entries must be integers")
    return rows


def matrix_rank_mod_prime(matrix: Sequence[Sequence[int]], prime: int) -> int:
    """Exact row-reduction rank over F_p using modular inverses."""
    _prime(prime)
    rows = [list(value % prime for value in row) for row in _matrix(matrix)]
    row_count = len(rows)
    column_count = len(rows[0])
    rank = 0
    for column in range(column_count):
        pivot = next(
            (index for index in range(rank, row_count) if rows[index][column] % prime),
            None,
        )
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        inverse = pow(rows[rank][column], -1, prime)
        rows[rank] = [(value * inverse) % prime for value in rows[rank]]
        for index in range(row_count):
            if index == rank:
                continue
            factor = rows[index][column] % prime
            if factor:
                rows[index] = [
                    (value - factor * pivot_value) % prime
                    for value, pivot_value in zip(rows[index], rows[rank])
                ]
        rank += 1
        if rank == row_count:
            break
    return rank


def relation_matrix_is_surjective(
    matrix: Sequence[Sequence[int]], prime: int
) -> bool:
    rows = _matrix(matrix)
    if len(rows) > len(rows[0]):
        return False
    return matrix_rank_mod_prime(rows, prime) == len(rows)


def relation_vector(
    state: Sequence[int], matrix: Sequence[Sequence[int]], prime: int, cap: int
) -> tuple[int, ...]:
    _prime(prime)
    _cap(cap)
    rows = _matrix(matrix)
    point = tuple(state)
    if len(point) != len(rows[0]):
        raise ValueError("state width must match relation matrix")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in point):
        raise ValueError("state entries must be integers")
    modulus = prime**cap
    return tuple(
        sum(coefficient * value for coefficient, value in zip(row, point)) % modulus
        for row in rows
    )


def induced_relation_actions(
    actions: Sequence[Sequence[int]],
    matrix: Sequence[Sequence[int]],
    prime: int,
    cap: int,
) -> tuple[tuple[int, ...], ...]:
    rows = _matrix(matrix)
    language = tuple(actions)
    if not language:
        raise ValueError("action language must be nonempty")
    return tuple(sorted({relation_vector(action, rows, prime, cap) for action in language}))


def relation_axis_action_language(
    actions: Sequence[Sequence[int]],
    matrix: Sequence[Sequence[int]],
    prime: int,
    cap: int,
    relation_axis: int,
) -> tuple[int, ...]:
    rows = _matrix(matrix)
    if (
        isinstance(relation_axis, bool)
        or not isinstance(relation_axis, int)
        or not 0 <= relation_axis < len(rows)
    ):
        raise ValueError("relation_axis outside relation matrix")
    induced = induced_relation_actions(actions, rows, prime, cap)
    return tuple(sorted({action[relation_axis] for action in induced}))


def compile_relation_rank_state(
    state: Sequence[int],
    actions: Sequence[Sequence[int]],
    matrix: Sequence[Sequence[int]],
    prime: int,
    cap: int,
) -> RelationToken:
    rows = _matrix(matrix)
    relation = relation_vector(state, rows, prime, cap)
    return tuple(
        compile_translation_trie_state(
            relation[axis],
            relation_axis_action_language(actions, rows, prime, cap, axis),
            prime,
            cap,
        )
        for axis in range(len(rows))
    )


def relation_rank_class_count(
    actions: Sequence[Sequence[int]],
    matrix: Sequence[Sequence[int]],
    prime: int,
    cap: int,
) -> int:
    rows = _matrix(matrix)
    if not relation_matrix_is_surjective(rows, prime):
        raise ValueError("exact class-count formula requires full row rank mod p")
    return prod(
        translation_trie_class_count(
            relation_axis_action_language(actions, rows, prime, cap, axis),
            prime,
            cap,
        )
        for axis in range(len(rows))
    )


def relation_rank_future_signature(
    state: Sequence[int],
    actions: Sequence[Sequence[int]],
    matrix: Sequence[Sequence[int]],
    prime: int,
    cap: int,
) -> tuple[tuple[int, ...], ...]:
    """Literal future signature over the original joint action language.

    Multiple joint actions are deliberately not deduplicated here even if they
    induce the same relation translation.  Duplicate coordinates do not change
    the kernel, but retaining them makes the regression oracle independent of
    the compiler's induced-action compression.
    """
    rows = _matrix(matrix)
    language = tuple(actions)
    if not language:
        raise ValueError("action language must be nonempty")
    relation = relation_vector(state, rows, prime, cap)
    modulus = prime**cap
    output = []
    for action in language:
        move = relation_vector(action, rows, prime, cap)
        output.append(
            tuple(
                capped_p_valuation((value + delta) % modulus, prime, cap)
                for value, delta in zip(relation, move)
            )
        )
    return tuple(output)


def relation_rank_partition_is_exact(
    actions: Sequence[Sequence[int]],
    matrix: Sequence[Sequence[int]],
    prime: int,
    cap: int,
) -> bool:
    rows = _matrix(matrix)
    if not relation_matrix_is_surjective(rows, prime):
        raise ValueError("oracle currently requires full row rank mod p")
    modulus = prime**cap
    width = len(rows[0])
    token_groups: dict[RelationToken, set[State]] = {}
    signature_groups: dict[tuple[tuple[int, ...], ...], set[State]] = {}
    for state in product(range(modulus), repeat=width):
        token_groups.setdefault(
            compile_relation_rank_state(state, actions, rows, prime, cap), set()
        ).add(state)
        signature_groups.setdefault(
            relation_rank_future_signature(state, actions, rows, prime, cap), set()
        ).add(state)
    return {frozenset(group) for group in token_groups.values()} == {
        frozenset(group) for group in signature_groups.values()
    }


def full_translation_relation_class_count(
    matrix: Sequence[Sequence[int]], prime: int, cap: int
) -> int:
    rows = _matrix(matrix)
    _cap(cap)
    if not relation_matrix_is_surjective(rows, prime):
        raise ValueError("full-translation formula requires full row rank mod p")
    return prime ** (cap * len(rows))


def representation_exponent_codimension(
    ambient_dimension: int, relation_rank: int, cap: int
) -> int:
    """Integer p-exponent removed when p^(Kd) safe state reduces to p^(Kr)."""
    for value, name in (
        (ambient_dimension, "ambient_dimension"),
        (relation_rank, "relation_rank"),
        (cap, "cap"),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError(f"{name} must be a non-negative integer")
    if cap == 0:
        raise ValueError("cap must be positive")
    if relation_rank > ambient_dimension:
        raise ValueError("relation_rank cannot exceed ambient_dimension")
    return cap * (ambient_dimension - relation_rank)
