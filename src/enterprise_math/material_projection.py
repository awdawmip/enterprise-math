"""Exact integer accounting of oscillator projection loss.

For one Pythagorean lifted rotation, write each raw lifted coordinate as

    u_i = c*q_i + delta_i.

Because the lift obeys ``sum u_i^2 = c^2 * R_before^2``, the fixed-resolution
projected state ``q`` satisfies the exact identity

    c^2 * (R_before^2 - R_after^2)
      = 2*c*sum(q_i*delta_i) + sum(delta_i^2).

This module treats that quantity as projection/detail accounting only.  It is
not automatically physical energy or dissipation.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_oscillator import PythagoreanRotation, ProjectedRotationStep


@dataclass(frozen=True)
class ProjectionLossIdentity:
    """Exact decomposition of one squared-radius change into finite details."""

    scaled_norm_sq_loss: int
    quotient_detail_cross_term: int
    detail_square_term: int
    reconstructed_scaled_loss: int
    coordinate_products: tuple[int, int]

    @property
    def nonnegative_from_sign_alignment(self) -> bool:
        """Whether q_i*delta_i>=0 coordinatewise, sufficient for nonnegative loss."""
        return all(product >= 0 for product in self.coordinate_products)


def rotation_projection_loss_identity(
    report: ProjectedRotationStep,
    rotation: PythagoreanRotation,
) -> ProjectionLossIdentity:
    """Return and verify the exact finite-detail norm-loss decomposition."""
    qx, qy = report.after
    dx, dy = report.details
    c = rotation.c

    if report.raw_lift != (c * qx + dx, c * qy + dy):
        raise ValueError("report details do not recompose the raw lift at this scale")

    products = (qx * dx, qy * dy)
    cross = 2 * c * sum(products)
    detail_sq = dx * dx + dy * dy
    reconstructed = cross + detail_sq
    scaled_loss = c * c * report.norm_sq_loss
    if scaled_loss != reconstructed:
        raise AssertionError("projection detail identity failed")

    return ProjectionLossIdentity(
        scaled_norm_sq_loss=scaled_loss,
        quotient_detail_cross_term=cross,
        detail_square_term=detail_sq,
        reconstructed_scaled_loss=reconstructed,
        coordinate_products=products,
    )
