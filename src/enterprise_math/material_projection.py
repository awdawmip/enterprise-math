"""Exact integer accounting of oscillator projection loss.

For one Pythagorean lifted rotation, write each raw lifted coordinate as

    u_i = c*q_i + delta_i.

Because the lift obeys ``sum u_i^2 = c^2 * R_before^2``, the fixed-resolution
projected state ``q`` satisfies the exact identity

    c^2 * (R_before^2 - R_after^2)
      = 2*c*sum(q_i*delta_i) + sum(delta_i^2).

Summing these local identities telescopes exactly to the initial/final squared
radius difference.  The module treats that quantity as projection/detail
accounting only; it is not automatically physical energy or dissipation.
"""

from __future__ import annotations

from dataclasses import dataclass

from .material_oscillator import (
    TOWARD_ZERO,
    PythagoreanRotation,
    ProjectedRotationStep,
    projected_rotation_step,
)


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


@dataclass(frozen=True)
class ProjectionLossTrace:
    """Telescoped finite-detail accounting across a projected rotation history."""

    initial_state: tuple[int, int]
    final_state: tuple[int, int]
    initial_norm_sq: int
    final_norm_sq: int
    norm_sq_loss: int
    scaled_norm_sq_loss: int
    local_scaled_losses: tuple[int, ...]
    local_cross_terms: tuple[int, ...]
    local_detail_square_terms: tuple[int, ...]


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


def trace_toward_zero_projection_loss(
    initial_state: tuple[int, int],
    rotation: PythagoreanRotation,
    steps: int,
) -> ProjectionLossTrace:
    """Accumulate exact local detail losses and verify the global telescope."""
    if isinstance(steps, bool) or not isinstance(steps, int) or steps < 0:
        raise ValueError("steps must be a non-negative integer")
    x, y = initial_state
    if isinstance(x, bool) or not isinstance(x, int):
        raise ValueError("initial x must be an integer")
    if isinstance(y, bool) or not isinstance(y, int):
        raise ValueError("initial y must be an integer")

    initial_norm = x * x + y * y
    local_losses: list[int] = []
    cross_terms: list[int] = []
    detail_terms: list[int] = []

    for _ in range(steps):
        report = projected_rotation_step(x, y, rotation, TOWARD_ZERO)
        identity = rotation_projection_loss_identity(report, rotation)
        if not identity.nonnegative_from_sign_alignment:
            raise AssertionError("toward-zero trace lost sign alignment")
        local_losses.append(identity.scaled_norm_sq_loss)
        cross_terms.append(identity.quotient_detail_cross_term)
        detail_terms.append(identity.detail_square_term)
        x, y = report.after

    final_norm = x * x + y * y
    norm_loss = initial_norm - final_norm
    scaled_loss = rotation.c * rotation.c * norm_loss
    if sum(local_losses) != scaled_loss:
        raise AssertionError("local projection losses failed to telescope")
    if sum(cross_terms) + sum(detail_terms) != scaled_loss:
        raise AssertionError("detail decomposition failed to telescope")

    return ProjectionLossTrace(
        initial_state=initial_state,
        final_state=(x, y),
        initial_norm_sq=initial_norm,
        final_norm_sq=final_norm,
        norm_sq_loss=norm_loss,
        scaled_norm_sq_loss=scaled_loss,
        local_scaled_losses=tuple(local_losses),
        local_cross_terms=tuple(cross_terms),
        local_detail_square_terms=tuple(detail_terms),
    )
