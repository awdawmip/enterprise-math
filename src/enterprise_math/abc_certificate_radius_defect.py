"""Radius-dependent normalized Wronskian congruence defect for primitive abc.

For the normalized scalar certificate ``W/M`` the complete image is
``eta_min Z``.  At finite access radius ``R``, relation-compatible derivative
states generate a subgroup ``g_R Z``.  Once nonzero,

    total saturation index = g_R,
    intrinsic defect       = eta_min,
    access image index     = g_R / eta_min.

This scalar specialization makes the exact-sequence distinction between
intrinsic and access-induced certificate congruence visible in ordinary
integer arithmetic.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd

from .abc_block_value_lattice import block_value_lattice_invariants
from .matrix_access_word_norm import matrix_image_at_radius
from .relation_shared_prime_rank import derivative_coefficient_matrix


@dataclass(frozen=True)
class NormalizedWronskianRadiusDefect:
    abc: tuple[int, int, int]
    radius: int
    certificate_rank: int
    generated_normalized_image: int
    intrinsic_saturation_index: int
    access_image_index: int | None
    total_saturation_index: int | None


def normalized_wronskian_radius_defect(
    a: int, b: int, c: int, radius: int
) -> NormalizedWronskianRadiusDefect:
    """Return the scalar normalized-certificate rank/index state at one radius."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    invariants = block_value_lattice_invariants(a, b, c)
    M = invariants.residual_product
    eta_min = invariants.absorption_floor
    _primes, matrix = derivative_coefficient_matrix((a, b, c))

    generator = 0
    for t_a, t_b, t_c in matrix_image_at_radius(matrix, radius):
        if t_a + t_b != t_c:
            continue
        wronskian = a * t_b - b * t_a
        if wronskian % M:
            raise AssertionError("relation-compatible Wronskian violated residual divisibility")
        generator = gcd(generator, abs(wronskian // M))

    if generator == 0:
        return NormalizedWronskianRadiusDefect(
            abc=(a, b, c),
            radius=radius,
            certificate_rank=0,
            generated_normalized_image=0,
            intrinsic_saturation_index=eta_min,
            access_image_index=None,
            total_saturation_index=None,
        )
    if generator % eta_min:
        raise AssertionError("finite-radius certificate subgroup must lie in complete image")
    return NormalizedWronskianRadiusDefect(
        abc=(a, b, c),
        radius=radius,
        certificate_rank=1,
        generated_normalized_image=generator,
        intrinsic_saturation_index=eta_min,
        access_image_index=generator // eta_min,
        total_saturation_index=generator,
    )
