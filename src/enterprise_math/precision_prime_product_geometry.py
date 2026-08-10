"""Prime-factor product-grid candidate for R004 precision genesis.

For ``lambda>1``, unique factorization gives pairwise-coprime prime-power side
lengths ``p^a`` whose product is ``lambda``.  Each side carries its canonical
ordered path refinement chain ``1,p,...,p^a``; taking the Cartesian product
therefore gives a finite grid with exactly ``lambda`` vertices and dimension
``omega(lambda)``.

All arithmetic decomposition statements are standard consequences of unique
factorization.  The graph construction is a project-level *candidate* for
turning scale-axis rank into spatial rank.  Identifying its dimension with
physical spatial dimension is not a proved Enterprise Math consequence.
"""
from __future__ import annotations

from dataclasses import dataclass

from enterprise_math.precision_prime_axes import (
    prime_axis_rank,
    prime_power_axis_scale_chains,
    prime_power_axis_sizes,
)
from enterprise_math.precision_product_geometry import (
    product_grid_diameter,
    product_grid_edge_count,
    product_grid_vertex_count,
)


@dataclass(frozen=True)
class PrimeProductGeometryProfile:
    scale: int
    dimension: int
    axis_sizes: tuple[int, ...]
    vertex_count: int
    edge_count: int
    diameter: int


def prime_product_geometry_profile(scale: int) -> PrimeProductGeometryProfile:
    if scale == 1:
        return PrimeProductGeometryProfile(
            scale=1,
            dimension=0,
            axis_sizes=(),
            vertex_count=1,
            edge_count=0,
            diameter=0,
        )
    chains = prime_power_axis_scale_chains(scale)
    sizes = prime_power_axis_sizes(scale)
    return PrimeProductGeometryProfile(
        scale=scale,
        dimension=prime_axis_rank(scale),
        axis_sizes=sizes,
        vertex_count=product_grid_vertex_count(chains),
        edge_count=product_grid_edge_count(chains),
        diameter=product_grid_diameter(chains),
    )


def prime_product_dimension_stable(coarse: int, fine: int) -> bool:
    coarse_profile = prime_product_geometry_profile(coarse)
    fine_profile = prime_product_geometry_profile(fine)
    if fine % coarse:
        raise ValueError("coarse scale must divide fine scale")
    return coarse_profile.dimension == fine_profile.dimension


def prime_product_genesis_profiles(
    scales: tuple[int, ...],
) -> tuple[PrimeProductGeometryProfile, ...]:
    if not scales:
        raise ValueError("scale sequence must be nonempty")
    if any(right % left for left, right in zip(scales, scales[1:])):
        raise ValueError("scales must form a divisibility refinement chain")
    return tuple(prime_product_geometry_profile(scale) for scale in scales)
