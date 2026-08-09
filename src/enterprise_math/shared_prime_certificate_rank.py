"""Certificate precision-rank gain after shared-prime block coupling.

For arbitrary overlapping integer blocks, prime coordinates map to block
derivative values through the matrix ``B``.  Declared block relations give
``L*B*x=0`` and block-linear certificate rows give ``H*B*x``.

The independent certificate dimension on the relation-adapted compressed state is

    rank([L*B; H*B]) - rank(L*B),

not ``rank([L;H])-rank(L)`` unless the block map has the independent-row property
of the pairwise-coprime setting.
"""

from __future__ import annotations

from dataclasses import dataclass

from .relation_block_rank import rational_matrix_rank
from .relation_shared_prime_rank import (
    SharedPrimeRelationSystem,
    shared_prime_relation_system,
)


@dataclass(frozen=True)
class SharedPrimeCertificateRankGain:
    derivative_rank: int
    relation_derivative_rank: int
    compressed_rank: int
    certificate_row_count: int
    certificate_derivative_rows: tuple[tuple[int, ...], ...]
    augmented_derivative_rank: int
    rank_gain: int
    residual_kernel_rank: int
    relation_redundant: bool
    compressed_state_complete: bool


def _validate_certificate_rows(
    system: SharedPrimeRelationSystem,
    rows: tuple[tuple[int, ...], ...],
) -> None:
    for row in rows:
        if len(row) != len(system.blocks):
            raise ValueError("certificate rows must match block count")
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError("certificate coefficients must be integers")


def _multiply_rows_by_derivative_matrix(
    rows: tuple[tuple[int, ...], ...],
    derivative_matrix: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    if not rows:
        return ()
    if not derivative_matrix:
        return tuple(() for _ in rows)
    width = len(derivative_matrix[0])
    return tuple(
        tuple(
            sum(row[i] * derivative_matrix[i][j] for i in range(len(derivative_matrix)))
            for j in range(width)
        )
        for row in rows
    )


def shared_prime_certificate_rank_gain(
    system: SharedPrimeRelationSystem,
    certificate_rows: tuple[tuple[int, ...], ...],
) -> SharedPrimeCertificateRankGain:
    """Return exact certificate rank gain after prime-to-block coupling."""
    _validate_certificate_rows(system, certificate_rows)
    hb = _multiply_rows_by_derivative_matrix(
        certificate_rows,
        system.derivative_matrix,
    )
    augmented = system.relation_derivative_matrix + hb
    augmented_rank = rational_matrix_rank(augmented) if augmented else 0
    gain = augmented_rank - system.relation_derivative_rank
    if not 0 <= gain <= system.compressed_rank:
        raise AssertionError("shared-prime certificate gain escaped compressed rank")
    residual = system.compressed_rank - gain
    return SharedPrimeCertificateRankGain(
        derivative_rank=system.derivative_rank,
        relation_derivative_rank=system.relation_derivative_rank,
        compressed_rank=system.compressed_rank,
        certificate_row_count=len(certificate_rows),
        certificate_derivative_rows=hb,
        augmented_derivative_rank=augmented_rank,
        rank_gain=gain,
        residual_kernel_rank=residual,
        relation_redundant=gain == 0,
        compressed_state_complete=gain == system.compressed_rank,
    )


def build_shared_prime_certificate_rank_gain(
    blocks: tuple[int, ...],
    relation_rows: tuple[tuple[int, ...], ...],
    certificate_rows: tuple[tuple[int, ...], ...],
) -> SharedPrimeCertificateRankGain:
    """Convenience constructor from raw block/relation data."""
    system = shared_prime_relation_system(blocks, relation_rows)
    return shared_prime_certificate_rank_gain(system, certificate_rows)
