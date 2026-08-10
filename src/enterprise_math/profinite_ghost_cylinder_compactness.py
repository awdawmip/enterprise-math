"""Executable finite-intersection surface for the profinite ghost witness.

For the fixed intersective polynomial F, let C_M be the profinite cylinder of
solutions modulo M.  Finite intersections satisfy

    C_(M_1) intersect ... intersect C_(M_k) = C_lcm(M_1,...,M_k).

The topological compactness theorem itself is not an algorithm over infinitely
many moduli.  This module locks the finite-intersection input to that theorem:
given any finite modulus family, construct one root modulo the lcm and verify that
its reductions solve every member of the family simultaneously.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import lcm
from typing import Sequence

from .nonlinear_profinite_ghost import (
    intersective_polynomial,
    polynomial_root_modulus,
)


def _moduli(values: Sequence[int]) -> tuple[int, ...]:
    moduli = tuple(values)
    if not moduli:
        raise ValueError("modulus family must be nonempty")
    for modulus in moduli:
        if isinstance(modulus, bool) or not isinstance(modulus, int):
            raise TypeError("moduli must be integers")
        if modulus <= 0:
            raise ValueError("moduli must be positive")
    return moduli


def modulus_family_lcm(moduli: Sequence[int]) -> int:
    values = _moduli(moduli)
    result = 1
    for modulus in values:
        result = lcm(result, modulus)
    return result


@dataclass(frozen=True)
class GhostFiniteCylinderIntersection:
    moduli: tuple[int, ...]
    lcm_modulus: int
    common_residue: int
    polynomial_value: int

    @property
    def solves_every_cylinder(self) -> bool:
        return all(self.polynomial_value % modulus == 0 for modulus in self.moduli)


def ghost_finite_cylinder_intersection(
    moduli: Sequence[int],
) -> GhostFiniteCylinderIntersection:
    values = _moduli(moduli)
    ceiling = modulus_family_lcm(values)
    residue = polynomial_root_modulus(ceiling)
    value = intersective_polynomial(residue)
    if value % ceiling:
        raise AssertionError("lcm residue did not solve the lcm cylinder")
    if any(value % modulus for modulus in values):
        raise AssertionError("lcm root failed one finite local cylinder")
    return GhostFiniteCylinderIntersection(
        moduli=values,
        lcm_modulus=ceiling,
        common_residue=residue,
        polynomial_value=value,
    )
