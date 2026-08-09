"""Invert the P011 collision polynomial to unordered Barlow checkpoint geometry.

P011 proves that collision coefficients J_k determine the complete fiber-size
profile by finite binomial inversion.  The P022 Barlow fiber-convolution theorem
then recovers the observed segment-length multiset and unobserved tail length.

Thus, inside this selected-layer specialization, the complete collision
polynomial is an exact encoding of the checkpoint geometry up to segment order.
"""

from __future__ import annotations

from math import comb

from .p022_barlow_fiber_convolution import (
    FiberProfile,
    profile_collision_count,
    profile_from_selected_layers,
    recover_selected_geometry_from_profile,
)

CollisionCoefficients = tuple[int, ...]


def _require_coefficients(coefficients: CollisionCoefficients) -> None:
    if not isinstance(coefficients, tuple) or not coefficients:
        raise ValueError("collision coefficients must be a nonempty tuple")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in coefficients
    ):
        raise ValueError("collision coefficients must be non-negative integers")
    if coefficients[0] <= 0:
        raise ValueError("J1 must be the positive microscopic domain size")


def fiber_profile_from_collision_coefficients(
    coefficients: CollisionCoefficients,
) -> FiberProfile:
    """P011 binomial inversion ``(J_1,...,J_M) -> (fiber size profile)``."""
    _require_coefficients(coefficients)
    maximum = len(coefficients)
    output = []
    for fiber_size in range(1, maximum + 1):
        multiplicity = sum(
            ((-1) ** (order - fiber_size))
            * comb(order, fiber_size)
            * coefficients[order - 1]
            for order in range(fiber_size, maximum + 1)
        )
        if multiplicity < 0:
            raise ValueError("coefficients do not encode a finite fiber profile")
        if multiplicity:
            output.append((fiber_size, multiplicity))
    profile = tuple(output)
    if sum(size * count for size, count in profile) != coefficients[0]:
        raise ValueError("inverted profile does not reconstruct J1/domain size")
    return profile


def collision_coefficients_from_profile(profile: FiberProfile) -> CollisionCoefficients:
    """Complete nonzero-degree P011 coefficient vector of one finite profile."""
    if not profile:
        raise ValueError("profile must be nonempty")
    maximum = max(size for size, _ in profile)
    return tuple(
        profile_collision_count(profile, order)
        for order in range(1, maximum + 1)
    )


def collision_coefficients_from_selected_layers(
    length: int, selected_layers: tuple[int, ...]
) -> CollisionCoefficients:
    """P011 polynomial coefficients for one Barlow selected-layer quotient."""
    return collision_coefficients_from_profile(
        profile_from_selected_layers(length, selected_layers)
    )


def recover_checkpoint_geometry_from_collision_coefficients(
    coefficients: CollisionCoefficients,
) -> tuple[tuple[int, ...], int]:
    """Recover ``(segment-length multiset, hidden-tail length)`` exactly."""
    profile = fiber_profile_from_collision_coefficients(coefficients)
    return recover_selected_geometry_from_profile(profile)
