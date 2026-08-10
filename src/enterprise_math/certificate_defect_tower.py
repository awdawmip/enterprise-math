"""Radius-dependent Smith signatures of certificate obstruction quotients.

For full certificate rank, ``C_R`` and the complete certificate image ``C``
have the same rational span.  Hence

    D_R = Sat(C) / C_R

is finite and its Smith invariant factors are exactly the defect signature of
the radius-generated labelled certificate lattice.  The terminal signature is
that of

    D_inf = Sat(C) / C.

The natural quotient maps ``D_R -> D_(R+1) -> D_inf`` come from the nested
certificate sublattices.  This module records the finite signatures; it does
not claim Smith theory or finite abelian group classification as new.
"""

from __future__ import annotations

from dataclasses import dataclass

from .certificate_image_index import (
    LatticeDefectSignature,
    certificate_basis_generators,
    lattice_defect_signature,
)
from .relation_generator_radius import (
    exact_relation_generator_radius,
    relation_generation_layer,
)


Vector = tuple[int, ...]
Matrix = tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class CertificateDefectTowerPoint:
    radius: int
    certificate_rank: int
    invariant_factors: tuple[int, ...] | None
    total_saturation_index: int | None
    access_image_index: int | None
    terminal: bool


@dataclass(frozen=True)
class CertificateDefectTower:
    full_certificate_rank: int
    terminal_signature: LatticeDefectSignature
    full_rank_radius: int
    certificate_complete_radius: int
    relation_generator_radius: int
    points: tuple[CertificateDefectTowerPoint, ...]


def _certificate_generators_from_coordinates(
    relation_coordinates: tuple[Vector, ...],
    certificate_basis: tuple[Vector, ...],
) -> tuple[Vector, ...]:
    relation_rank = len(certificate_basis)
    if relation_rank == 0:
        return ()
    output_dimension = len(certificate_basis[0])
    results: list[Vector] = []
    for coordinates in relation_coordinates:
        if len(coordinates) != relation_rank:
            raise ValueError("relation coordinates must match relation basis rank")
        results.append(
            tuple(
                sum(coordinates[i] * certificate_basis[i][j] for i in range(relation_rank))
                for j in range(output_dimension)
            )
        )
    return tuple(results)


def certificate_defect_signature_at_radius(
    matrix: Matrix,
    relation_rows: tuple[Vector, ...],
    relation_basis: tuple[Vector, ...],
    certificate_rows: tuple[Vector, ...],
    radius: int,
) -> tuple[LatticeDefectSignature, LatticeDefectSignature]:
    """Return current and terminal labelled certificate defect signatures."""
    certificate_basis = certificate_basis_generators(relation_basis, certificate_rows)
    terminal = lattice_defect_signature(certificate_basis)
    relation_layer = relation_generation_layer(matrix, relation_rows, relation_basis, radius)
    current_generators = _certificate_generators_from_coordinates(
        relation_layer.coordinate_generators,
        certificate_basis,
    )
    current = lattice_defect_signature(current_generators)
    return current, terminal


def exact_certificate_defect_tower(
    matrix: Matrix,
    relation_rows: tuple[Vector, ...],
    relation_basis: tuple[Vector, ...],
    certificate_rows: tuple[Vector, ...],
) -> CertificateDefectTower:
    """Return strict changes of the finite certificate obstruction quotient.

    Rank-deficient layers are recorded with no finite defect signature.  Once
    the complete certificate rank is reached, every point stores the Smith
    factors of ``Sat(C)/C_R`` and the relative access index ``[C:C_R]``.
    """
    certificate_basis = certificate_basis_generators(relation_basis, certificate_rows)
    terminal = lattice_defect_signature(certificate_basis)
    endpoint = exact_relation_generator_radius(matrix, relation_rows, relation_basis)
    full_rank = terminal.rank

    if full_rank == 0:
        return CertificateDefectTower(
            full_certificate_rank=0,
            terminal_signature=terminal,
            full_rank_radius=0,
            certificate_complete_radius=0,
            relation_generator_radius=endpoint.generator_radius,
            points=(),
        )

    full_rank_radius: int | None = None
    complete_radius: int | None = None
    points: list[CertificateDefectTowerPoint] = []
    previous_state: tuple[int, tuple[int, ...] | None] | None = None

    for radius in range(1, endpoint.generator_radius + 1):
        current, _terminal = certificate_defect_signature_at_radius(
            matrix,
            relation_rows,
            relation_basis,
            certificate_rows,
            radius,
        )
        if current.rank == full_rank and full_rank_radius is None:
            full_rank_radius = radius
        if current.rank == full_rank:
            if current.saturation_index % terminal.saturation_index:
                raise AssertionError("full-rank defect order must contain terminal defect order")
            access_index = current.saturation_index // terminal.saturation_index
            if access_index == 1 and complete_radius is None:
                complete_radius = radius
            signature: tuple[int, ...] | None = current.invariant_factors
            total_index: int | None = current.saturation_index
        else:
            access_index = None
            signature = None
            total_index = None

        state = (current.rank, signature)
        if state != previous_state and current.rank > 0:
            points.append(
                CertificateDefectTowerPoint(
                    radius=radius,
                    certificate_rank=current.rank,
                    invariant_factors=signature,
                    total_saturation_index=total_index,
                    access_image_index=access_index,
                    terminal=(
                        current.rank == full_rank
                        and current.invariant_factors == terminal.invariant_factors
                        and access_index == 1
                    ),
                )
            )
        previous_state = state

    if full_rank_radius is None or complete_radius is None:
        raise AssertionError("relation generator completeness must force terminal certificate image")
    if not points or not points[-1].terminal:
        raise AssertionError("defect tower must stabilize at terminal certificate quotient")
    return CertificateDefectTower(
        full_certificate_rank=full_rank,
        terminal_signature=terminal,
        full_rank_radius=full_rank_radius,
        certificate_complete_radius=complete_radius,
        relation_generator_radius=endpoint.generator_radius,
        points=tuple(points),
    )
