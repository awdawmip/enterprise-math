"""Generic block-value rank law for relation-conditioned arithmetic derivatives.

For pairwise-coprime positive integer blocks ``n_i``, prime-coordinate supports
are disjoint.  Each block derivative value lies in one image ideal ``A_i Z``.
Given integer additive relations ``L n = 0``, linearity of arithmetic
derivations imposes the same relations ``L t = 0`` on block derivative values.

After removing unit blocks (whose derivative value is always zero), the
compressed lattice is

    Lambda = diag(A_i) Z^m intersect ker_Z(L).

Since the diagonal image-generator matrix is invertible over Q, the rational
rank is exactly

    m - rank_Q(L).

Thus global relation-state dimension depends on the number of active blocks and
independent relation rows, not on the total number of prime coordinates inside
those blocks.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd

from .abc_unit_relation import raw_block_derivative_image_generator


@dataclass(frozen=True)
class RelationBlockSystem:
    blocks: tuple[int, ...]
    relation_rows: tuple[tuple[int, ...], ...]
    active_indices: tuple[int, ...]
    block_image_generators: tuple[int, ...]
    active_relation_rows: tuple[tuple[int, ...], ...]
    relation_rank: int
    compressed_rank: int


def _validate_integer_matrix(rows: tuple[tuple[int, ...], ...], width: int) -> None:
    for row in rows:
        if len(row) != width:
            raise ValueError("every relation row must match the block count")
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError("relation coefficients must be integers")


def rational_matrix_rank(rows: tuple[tuple[int, ...], ...]) -> int:
    """Return exact Q-rank by finite Gaussian elimination."""
    if not rows:
        return 0
    width = len(rows[0])
    _validate_integer_matrix(rows, width)
    matrix = [[Fraction(value) for value in row] for row in rows]
    rank = 0
    pivot_column = 0
    while rank < len(matrix) and pivot_column < width:
        pivot = next(
            (index for index in range(rank, len(matrix)) if matrix[index][pivot_column] != 0),
            None,
        )
        if pivot is None:
            pivot_column += 1
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        pivot_value = matrix[rank][pivot_column]
        matrix[rank] = [value / pivot_value for value in matrix[rank]]
        for index in range(len(matrix)):
            if index == rank:
                continue
            factor = matrix[index][pivot_column]
            if factor == 0:
                continue
            matrix[index] = [
                value - factor * pivot_entry
                for value, pivot_entry in zip(matrix[index], matrix[rank], strict=True)
            ]
        rank += 1
        pivot_column += 1
    return rank


def relation_block_system(
    blocks: tuple[int, ...], relation_rows: tuple[tuple[int, ...], ...]
) -> RelationBlockSystem:
    """Build and validate a pairwise-coprime integer relation block system."""
    if not blocks:
        raise ValueError("block system must be nonempty")
    for block in blocks:
        if isinstance(block, bool) or not isinstance(block, int) or block <= 0:
            raise ValueError("blocks must be positive integers")
    for i, left in enumerate(blocks):
        for right in blocks[i + 1 :]:
            if gcd(left, right) != 1:
                raise ValueError("blocks must be pairwise coprime for independent prime supports")

    _validate_integer_matrix(relation_rows, len(blocks))
    for row in relation_rows:
        if sum(coefficient * block for coefficient, block in zip(row, blocks, strict=True)) != 0:
            raise ValueError("every declared relation row must annihilate the integer blocks")

    generators = tuple(
        0 if block == 1 else raw_block_derivative_image_generator(block)
        for block in blocks
    )
    active_indices = tuple(index for index, generator in enumerate(generators) if generator > 0)
    active_rows = tuple(
        tuple(row[index] for index in active_indices)
        for row in relation_rows
    )
    relation_rank = rational_matrix_rank(active_rows) if active_rows else 0
    compressed_rank = len(active_indices) - relation_rank
    if compressed_rank < 0:
        raise AssertionError("relation rank exceeded active block count")

    return RelationBlockSystem(
        blocks=blocks,
        relation_rows=relation_rows,
        active_indices=active_indices,
        block_image_generators=generators,
        active_relation_rows=active_rows,
        relation_rank=relation_rank,
        compressed_rank=compressed_rank,
    )


def derivative_value_state_is_admissible(
    system: RelationBlockSystem, values: tuple[int, ...]
) -> bool:
    """Check exact membership in the compressed block-value relation lattice."""
    if len(values) != len(system.blocks):
        raise ValueError("derivative-value vector must match block count")
    for value in values:
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError("derivative values must be integers")
    for value, generator in zip(values, system.block_image_generators, strict=True):
        if generator == 0:
            if value != 0:
                return False
        elif value % generator:
            return False
    return all(
        sum(coefficient * value for coefficient, value in zip(row, values, strict=True)) == 0
        for row in system.relation_rows
    )


def certificate_rank_ceiling(
    system: RelationBlockSystem,
    certificate_rows: tuple[tuple[int, ...], ...],
) -> int:
    """Return the universal rational-rank ceiling for block-linear certificates.

    Any certificate image is a linear image of the compressed relation lattice,
    so its rank cannot exceed ``compressed_rank``.  The function validates the
    labelled certificate width and returns that theorem-level ceiling; actual
    image rank may be lower.
    """
    _validate_integer_matrix(certificate_rows, len(system.blocks))
    return system.compressed_rank
