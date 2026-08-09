"""Finite rank/index profile of radius-generated relation subgroups.

For a relation lattice ``Lambda`` and ambient matrix access sets ``Z_R(B)``, let

    Gamma_R = < Z_R(B) intersect Lambda >.

These subgroups are nested.  Their rational rank is nondecreasing.  Once full
rank is reached, the finite indices ``I_R=[Lambda:Gamma_R]`` form a divisibility
chain: ``I_(R+1) | I_R``.  The first full-rank radius can therefore precede the
first index-one (generator-complete) radius.

The exact profile records only strict changes of ``(rank,index)`` up to the
relation-generator radius.
"""

from __future__ import annotations

from dataclasses import dataclass

from .relation_generator_radius import (
    RelationGenerationLayer,
    exact_relation_generator_radius,
    relation_generation_layer,
)


Vector = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class RelationGenerationProfilePoint:
    radius: int
    coordinate_rank: int
    subgroup_index: int | None


@dataclass(frozen=True)
class RelationGenerationProfile:
    relation_rank: int
    first_nonzero_radius: int
    full_rank_radius: int
    generator_radius: int
    direct_basis_upper_bound: int
    points: tuple[RelationGenerationProfilePoint, ...]


def exact_relation_generation_profile(
    matrix: Matrix,
    relation_rows: tuple[Vector, ...],
    relation_basis: tuple[Vector, ...],
) -> RelationGenerationProfile:
    """Return the strict-change rank/index profile through generator completeness."""
    endpoint = exact_relation_generator_radius(matrix, relation_rows, relation_basis)
    rank = len(relation_basis)
    first_nonzero: int | None = None
    full_rank: int | None = None
    points: list[RelationGenerationProfilePoint] = []
    previous_state: tuple[int, int | None] | None = None
    previous_finite_index: int | None = None

    for radius in range(1, endpoint.generator_radius + 1):
        layer = relation_generation_layer(matrix, relation_rows, relation_basis, radius)
        if first_nonzero is None and layer.coordinate_rank > 0:
            first_nonzero = radius
        if full_rank is None and layer.coordinate_rank == rank:
            full_rank = radius
        if previous_state is not None and layer.coordinate_rank < previous_state[0]:
            raise AssertionError("generated relation subgroup rank must be nondecreasing")

        if layer.subgroup_index is not None:
            if layer.coordinate_rank != rank:
                raise AssertionError("finite subgroup index requires full rational rank")
            if previous_finite_index is not None:
                if previous_finite_index % layer.subgroup_index:
                    raise AssertionError("nested full-rank subgroup indices must form divisibility chain")
                if layer.subgroup_index > previous_finite_index:
                    raise AssertionError("nested subgroup index must not increase")
            previous_finite_index = layer.subgroup_index

        state = (layer.coordinate_rank, layer.subgroup_index)
        if state != previous_state and layer.coordinate_rank > 0:
            points.append(
                RelationGenerationProfilePoint(
                    radius=radius,
                    coordinate_rank=layer.coordinate_rank,
                    subgroup_index=layer.subgroup_index,
                )
            )
        previous_state = state

    if first_nonzero is None or first_nonzero != endpoint.first_nonzero_radius:
        raise AssertionError("profile disagrees with generator-radius first nonzero layer")
    if full_rank is None:
        raise AssertionError("generator completeness must pass through full rational rank")
    if not points or points[-1].subgroup_index != 1:
        raise AssertionError("profile must terminate at index-one generator completeness")

    return RelationGenerationProfile(
        relation_rank=rank,
        first_nonzero_radius=first_nonzero,
        full_rank_radius=full_rank,
        generator_radius=endpoint.generator_radius,
        direct_basis_upper_bound=endpoint.direct_basis_upper_bound,
        points=tuple(points),
    )


def finite_index_drop_count_bound(profile: RelationGenerationProfile) -> int:
    """Return a simple bound on strict finite-index drops after full rank.

    If the first finite index is ``I``, every strict proper-divisor drop is at
    most a factor one-half.  Hence the number of recorded finite-index levels is
    at most ``bit_length(I)``.  This is only a finite combinatorial bound, not a
    complexity claim for constructing the layers.
    """
    finite_points = tuple(point for point in profile.points if point.subgroup_index is not None)
    if not finite_points:
        raise ValueError("profile has no finite-index layer")
    initial = finite_points[0].subgroup_index
    if initial is None or initial <= 0:
        raise AssertionError("finite index must be positive")
    return initial.bit_length()
