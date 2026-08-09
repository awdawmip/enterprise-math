"""P022 checkpoint objectives as functionals of the P011 collision polynomial.

The generic identities ``K(-1)=-|image|``, ``deg K=max fiber size`` and
``leading coefficient=#max fibers`` belong to P011/A1 and are relayed there.
This module only applies those identities to the structured Barlow checkpoint
quotient and combines them with the P022 order-repair inverse.
"""

from __future__ import annotations

from .p022_barlow_collision_geometry import (
    CollisionCoefficients,
    collision_coefficients_from_selected_layers,
)
from .p022_barlow_collision_order_repair import (
    ordered_geometry_fiber_size_from_collision_coefficients,
)


def _require_coefficients(coefficients: CollisionCoefficients) -> None:
    if not isinstance(coefficients, tuple) or not coefficients:
        raise ValueError("collision coefficients must be a nonempty tuple")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in coefficients
    ):
        raise ValueError("collision coefficients must be non-negative integers")
    if coefficients[0] <= 0:
        raise ValueError("J1/domain size must be positive")


def collision_image_size(coefficients: CollisionCoefficients) -> int:
    """Recover ``|im O|=-K_O(-1)`` from complete P011 coefficients."""
    _require_coefficients(coefficients)
    image = sum(
        ((-1) ** (order + 1)) * coefficient
        for order, coefficient in enumerate(coefficients, start=1)
    )
    if image <= 0:
        raise ValueError("coefficients do not encode a positive finite image")
    return image


def collision_pair_ambiguity(coefficients: CollisionCoefficients) -> int:
    """P011 pair collision coefficient J2."""
    _require_coefficients(coefficients)
    return coefficients[1] if len(coefficients) >= 2 else 0


def collision_max_fiber_size(coefficients: CollisionCoefficients) -> int:
    """Return ``deg K``, equal to the largest represented microscopic fiber."""
    _require_coefficients(coefficients)
    for order in range(len(coefficients), 0, -1):
        if coefficients[order - 1]:
            return order
    raise AssertionError("positive J1 prevents an empty collision polynomial")


def collision_max_fiber_count(coefficients: CollisionCoefficients) -> int:
    """Leading coefficient: number of fibers attaining the maximum size."""
    maximum = collision_max_fiber_size(coefficients)
    return coefficients[maximum - 1]


def collision_objective_summary(
    coefficients: CollisionCoefficients,
) -> tuple[int, int, int, int, int]:
    """Return ``(image, J2, max_fiber, max_fiber_count, order_fiber)``."""
    return (
        collision_image_size(coefficients),
        collision_pair_ambiguity(coefficients),
        collision_max_fiber_size(coefficients),
        collision_max_fiber_count(coefficients),
        ordered_geometry_fiber_size_from_collision_coefficients(coefficients),
    )


def checkpoint_objective_summary(
    length: int, selected_layers: tuple[int, ...]
) -> tuple[int, int, int, int, int]:
    """Build the complete collision state then read the five P022 objectives."""
    coefficients = collision_coefficients_from_selected_layers(
        length, selected_layers
    )
    return collision_objective_summary(coefficients)
