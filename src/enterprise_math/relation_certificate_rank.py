"""Exact certificate rank gain over a relation-conditioned block system.

Let ``L`` be the active relation matrix and ``H`` a family of block-linear
certificate rows.  On the rational relation state ``ker(L)``, the independent
certificate dimension is

    rank([L; H]) - rank(L).

This is the rank of ``H`` restricted to ``ker(L)``.  It measures how many new
exact block-value distinctions the certificate family adds beyond the declared
relations, independently of how many output coordinates are reported.
"""

from __future__ import annotations

from dataclasses import dataclass

from .relation_block_rank import (
    RelationBlockSystem,
    rational_matrix_rank,
)


@dataclass(frozen=True)
class CertificateRankGain:
    relation_rank: int
    compressed_rank: int
    certificate_row_count: int
    augmented_rank: int
    rank_gain: int
    residual_kernel_rank: int
    relation_redundant: bool
    block_value_complete: bool


def _validate_rows(rows: tuple[tuple[int, ...], ...], width: int) -> None:
    for row in rows:
        if len(row) != width:
            raise ValueError("certificate rows must match the original block count")
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise ValueError("certificate coefficients must be integers")


def certificate_rank_gain(
    system: RelationBlockSystem,
    certificate_rows: tuple[tuple[int, ...], ...],
) -> CertificateRankGain:
    """Return the exact rational precision-rank gain of a certificate family."""
    _validate_rows(certificate_rows, len(system.blocks))
    active_certificates = tuple(
        tuple(row[index] for index in system.active_indices)
        for row in certificate_rows
    )
    augmented = system.active_relation_rows + active_certificates
    augmented_rank = rational_matrix_rank(augmented) if augmented else 0
    gain = augmented_rank - system.relation_rank
    if not 0 <= gain <= system.compressed_rank:
        raise AssertionError("certificate rank gain escaped relation-kernel dimension")
    residual = system.compressed_rank - gain
    return CertificateRankGain(
        relation_rank=system.relation_rank,
        compressed_rank=system.compressed_rank,
        certificate_row_count=len(certificate_rows),
        augmented_rank=augmented_rank,
        rank_gain=gain,
        residual_kernel_rank=residual,
        relation_redundant=gain == 0,
        block_value_complete=gain == system.compressed_rank,
    )


def exact_certificate_equivalence_rank(
    system: RelationBlockSystem,
    certificate_rows: tuple[tuple[int, ...], ...],
) -> int:
    """Return the rank of the residual relation-state fiber after exact certificates."""
    return certificate_rank_gain(system, certificate_rows).residual_kernel_rank


def abc_wronskian_row(a: int, b: int, c: int) -> tuple[int, int, int]:
    """Return the block-value Wronskian row ``(-b,a,0)`` for ``a+b=c``."""
    if a + b != c:
        raise ValueError("require a+b=c")
    return (-b, a, 0)
