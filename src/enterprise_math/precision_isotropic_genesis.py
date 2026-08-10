"""Label-independent isotropic divisor-grid genesis candidate.

For a squarefree support ``P`` with ``D=omega(P)`` and level ``a>=1``, the
scale ``lambda=P^a`` has equal prime exponents.  Its divisor Hasse graph is the
unlabeled grid ``{0,...,a}^D``.  Consequently all graph observables built only
from that grid, including the R004 threshold-record distance spectrum, depend
on ``D`` and ``a`` but not on which prime labels form ``P``.

This removes prime *labels* from the candidate geometry.  It does not explain
why the physical support rank should be three.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction

from enterprise_math.precision_divisor_geometry import (
    DivisorGridProfile,
    divisor_grid_profile,
    isotropic_genesis_sequence,
)
from enterprise_math.precision_grid_distance_spectrum import (
    grid_zero_overlap_pair_fraction,
)
from enterprise_math.precision_prime_axes import prime_axis_rank


@dataclass(frozen=True)
class IsotropicGenesisSignature:
    level: int
    dimension: int
    shape: tuple[int, ...]
    vertex_count: int
    edge_count: int
    diameter: int


def isotropic_genesis_signature(
    squarefree_support: int, level: int
) -> IsotropicGenesisSignature:
    if isinstance(level, bool) or not isinstance(level, int) or level < 0:
        raise ValueError("level must be a non-negative integer")
    scales = isotropic_genesis_sequence(squarefree_support, level)
    profile = divisor_grid_profile(scales[-1])
    return IsotropicGenesisSignature(
        level=level,
        dimension=profile.dimension,
        shape=profile.shape,
        vertex_count=profile.vertex_count,
        edge_count=profile.edge_count,
        diameter=profile.diameter,
    )


def same_rank_supports_same_unlabeled_geometry(
    first_support: int, second_support: int, level: int
) -> bool:
    first = isotropic_genesis_signature(first_support, level)
    second = isotropic_genesis_signature(second_support, level)
    if level == 0:
        return True
    return (
        first.dimension == second.dimension
        and first.shape == second.shape
        and first.vertex_count == second.vertex_count
        and first.edge_count == second.edge_count
        and first.diameter == second.diameter
    )


def isotropic_zero_overlap_fraction(
    squarefree_support: int, level: int, record_resolution: int
) -> Fraction:
    signature = isotropic_genesis_signature(squarefree_support, level)
    if signature.vertex_count <= 1:
        return Fraction(0, 1)
    return grid_zero_overlap_pair_fraction(signature.shape, record_resolution)


def isotropic_zero_overlap_sequence(
    squarefree_support: int, levels: int, record_resolution: int
) -> tuple[Fraction, ...]:
    if isinstance(levels, bool) or not isinstance(levels, int) or levels < 0:
        raise ValueError("levels must be a non-negative integer")
    return tuple(
        isotropic_zero_overlap_fraction(
            squarefree_support, level, record_resolution
        )
        for level in range(levels + 1)
    )


def genesis_rank_jump(squarefree_support: int) -> int:
    isotropic_genesis_sequence(squarefree_support, 1)
    return prime_axis_rank(squarefree_support)
