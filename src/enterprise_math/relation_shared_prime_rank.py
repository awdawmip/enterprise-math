"""Shared-prime generalization of the relation-conditioned block rank law.

For arbitrary positive integer blocks, prime-coordinate supports may overlap.
Let ``B`` be the block-by-prime arithmetic-derivative coefficient matrix

    B[i,p] = n_i * v_p(n_i) / p.

A fine prime-coordinate vector ``x`` produces block derivative values ``t=B*x``.
Declared integer block relations ``L*n=0`` impose ``L*B*x=0``.  The exact
compressed derivative-value state is therefore

    B(ker_Z(LB)) = im_Z(B) intersect ker_Z(L).

Over Q its rank is

    rank(B) - rank(LB).

Pairwise-coprime Stage 26 is the special case in which the active rows of ``B``
have disjoint supports and hence full row rank before relation constraints.
"""

from __future__ import annotations

from dataclasses import dataclass

from .abc_support import prime_factorization
from .relation_block_rank import rational_matrix_rank


@dataclass(frozen=True)
class SharedPrimeRelationSystem:
    blocks: tuple[int, ...]
    prime_coordinates: tuple[int, ...]
    derivative_matrix: tuple[tuple[int, ...], ...]
    relation_rows: tuple[tuple[int, ...], ...]
    relation_derivative_matrix: tuple[tuple[int, ...], ...]
    derivative_rank: int
    relation_derivative_rank: int
    compressed_rank: int


def _validate_relations(
    blocks: tuple[int, ...], rows: tuple[tuple[int, ...], ...]
) -> None:
    for row in rows:
        if len(row) != len(blocks):
            raise ValueError("relation rows must match block count")
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError("relation coefficients must be integers")
        if sum(value * block for value, block in zip(row, blocks, strict=True)) != 0:
            raise ValueError("every relation row must annihilate the integer blocks")


def derivative_coefficient_matrix(
    blocks: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[tuple[int, ...], ...]]:
    """Return sorted union-prime coordinates and exact raw derivative matrix."""
    if not blocks:
        raise ValueError("block family must be nonempty")
    for block in blocks:
        if isinstance(block, bool) or not isinstance(block, int) or block <= 0:
            raise ValueError("blocks must be positive integers")
    factors = tuple(dict(prime_factorization(block)) for block in blocks)
    primes = tuple(sorted(set().union(*(set(mapping) for mapping in factors))))
    rows = tuple(
        tuple(
            block * mapping.get(prime, 0) // prime
            if prime in mapping
            else 0
            for prime in primes
        )
        for block, mapping in zip(blocks, factors, strict=True)
    )
    return primes, rows


def _matrix_product(
    left: tuple[tuple[int, ...], ...],
    right: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    if not left:
        return ()
    if not right:
        return tuple(() for _ in left)
    inner = len(right)
    if any(len(row) != inner for row in left):
        raise ValueError("matrix dimensions do not match")
    width = len(right[0])
    if any(len(row) != width for row in right):
        raise ValueError("right matrix rows must have equal width")
    return tuple(
        tuple(
            sum(left_row[k] * right[k][j] for k in range(inner))
            for j in range(width)
        )
        for left_row in left
    )


def shared_prime_relation_system(
    blocks: tuple[int, ...], relation_rows: tuple[tuple[int, ...], ...]
) -> SharedPrimeRelationSystem:
    """Build the exact shared-prime derivative relation system and rank data."""
    _validate_relations(blocks, relation_rows)
    primes, derivative = derivative_coefficient_matrix(blocks)
    relation_derivative = _matrix_product(relation_rows, derivative)
    rank_b = rational_matrix_rank(derivative) if derivative else 0
    rank_lb = rational_matrix_rank(relation_derivative) if relation_derivative else 0
    compressed = rank_b - rank_lb
    if compressed < 0:
        raise AssertionError("relation-restricted derivative image acquired negative rank")
    return SharedPrimeRelationSystem(
        blocks=blocks,
        prime_coordinates=primes,
        derivative_matrix=derivative,
        relation_rows=relation_rows,
        relation_derivative_matrix=relation_derivative,
        derivative_rank=rank_b,
        relation_derivative_rank=rank_lb,
        compressed_rank=compressed,
    )


def derivative_values_from_fine_coordinates(
    system: SharedPrimeRelationSystem, coordinates: tuple[int, ...]
) -> tuple[int, ...]:
    """Evaluate the block derivative-value vector of a fine prime-coordinate state."""
    if len(coordinates) != len(system.prime_coordinates):
        raise ValueError("fine coordinate vector must match union-prime support")
    for value in coordinates:
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("fine coordinates must be integers")
    return tuple(
        sum(coefficient * value for coefficient, value in zip(row, coordinates, strict=True))
        for row in system.derivative_matrix
    )


def fine_coordinates_are_relation_adapted(
    system: SharedPrimeRelationSystem, coordinates: tuple[int, ...]
) -> bool:
    """Check the exact fine relation equations ``L*B*x=0``."""
    if len(coordinates) != len(system.prime_coordinates):
        raise ValueError("fine coordinate vector must match union-prime support")
    return all(
        sum(coefficient * value for coefficient, value in zip(row, coordinates, strict=True)) == 0
        for row in system.relation_derivative_matrix
    )


def individual_block_ideal_relation_membership(
    blocks: tuple[int, ...],
    relation_rows: tuple[tuple[int, ...], ...],
    derivative_values: tuple[int, ...],
) -> bool:
    """Naive separate-block test used only to expose the shared-prime failure boundary."""
    from math import gcd

    if len(derivative_values) != len(blocks):
        raise ValueError("derivative-value vector must match block count")
    _validate_relations(blocks, relation_rows)
    _primes, matrix = derivative_coefficient_matrix(blocks)
    for row, target in zip(matrix, derivative_values, strict=True):
        generator = 0
        for coefficient in row:
            generator = gcd(generator, abs(coefficient))
        if generator == 0:
            if target != 0:
                return False
        elif target % generator:
            return False
    return all(
        sum(coefficient * value for coefficient, value in zip(row, derivative_values, strict=True)) == 0
        for row in relation_rows
    )


def shared_prime_independence_counterexample() -> dict[str, object]:
    """Show separate block image ideals over-approximate the joint derivative image."""
    blocks = (2, 4, 6)
    relations = ((1, 1, -1),)
    system = shared_prime_relation_system(blocks, relations)
    false_state = (0, 4, 4)
    if not individual_block_ideal_relation_membership(blocks, relations, false_state):
        raise AssertionError("counterexample lost naive separate-ideal membership")
    # The first derivative value is x_2.  If it is zero, x_2=0, forcing the
    # second value 4*x_2 to be zero rather than four.  Hence false_state is not
    # in im_Z(B), even though every component lies in its separate block ideal.
    return {
        "blocks": blocks,
        "relations": relations,
        "prime_coordinates": system.prime_coordinates,
        "derivative_matrix": system.derivative_matrix,
        "relation_derivative_matrix": system.relation_derivative_matrix,
        "compressed_rank": system.compressed_rank,
        "false_separate_ideal_state": false_state,
    }
