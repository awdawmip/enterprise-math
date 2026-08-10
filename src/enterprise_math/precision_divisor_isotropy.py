"""Intrinsic anisotropy pressure test for the R004 divisor-grid candidate.

The test uses no Euclidean angle.  Two vertices at the same graph distance from
a center have different shortest-path multiplicities, so they cannot lie in the
same orbit of any center-fixing graph automorphism.  Hence the ordinary
Cartesian divisor grid is not sphere-transitive/distance-isotropic even when
all prime-exponent side lengths are equal.

Geodesic counting reuses the generic finite graph helper already present in the
R004 executable layer rather than introducing a parallel P022 geometry engine.
"""
from __future__ import annotations

from dataclasses import dataclass

from enterprise_math.precision_divisor_geometry import (
    divisor_grid_distance,
    divisor_grid_edges,
    divisor_grid_profile,
    divisor_grid_states,
)
from enterprise_math.precision_genesis import geodesic_count


@dataclass(frozen=True)
class DivisorGridIsotropyWitness:
    scale: int
    center: tuple[int, ...]
    first_target: tuple[int, ...]
    second_target: tuple[int, ...]
    common_distance: int
    first_geodesic_count: int
    second_geodesic_count: int


def intrinsic_radius_two_anisotropy_witness(
    scale: int,
) -> DivisorGridIsotropyWitness:
    profile = divisor_grid_profile(scale)
    if profile.dimension < 2:
        raise ValueError("anisotropy witness needs at least two exponent axes")
    if any(maximum < 4 for maximum in profile.maximum_exponents[:2]):
        raise ValueError("first two axes need exponent range at least 0..4")

    center = tuple(2 for _ in range(profile.dimension))
    if any(center[index] > maximum for index, maximum in enumerate(profile.maximum_exponents)):
        raise ValueError("all axes need an interior exponent coordinate 2")

    axial = list(center)
    axial[0] += 2
    split = list(center)
    split[0] += 1
    split[1] += 1
    axial_target = tuple(axial)
    split_target = tuple(split)

    axial_distance = divisor_grid_distance(center, axial_target, scale)
    split_distance = divisor_grid_distance(center, split_target, scale)
    if axial_distance != 2 or split_distance != 2:
        raise AssertionError("declared witness must lie on graph sphere radius two")

    vertices = divisor_grid_states(scale)
    edges = divisor_grid_edges(scale)
    axial_count = geodesic_count(vertices, edges, center, axial_target)
    split_count = geodesic_count(vertices, edges, center, split_target)
    if axial_count == split_count:
        raise AssertionError("radius-two witness must separate geodesic multiplicities")

    return DivisorGridIsotropyWitness(
        scale=scale,
        center=center,
        first_target=axial_target,
        second_target=split_target,
        common_distance=2,
        first_geodesic_count=axial_count,
        second_geodesic_count=split_count,
    )


def strong_sphere_transitivity_fails(scale: int) -> bool:
    witness = intrinsic_radius_two_anisotropy_witness(scale)
    return witness.first_geodesic_count != witness.second_geodesic_count
