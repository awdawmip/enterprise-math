"""Certification precision requirements form a coordinatewise join lattice.

For an integer affine IMAGE task ``A:Z^n->Z^m``, uniform modular certification
of exact reachability depends on two resources:

* whether a free-cokernel separating experiment is required;
* the required p-adic depths ``a_p=v_p(E)`` of the torsion exponent E.

Package these as

    R(A) = (free_required ; (a_p)_p).

An experiment precision profile is complete exactly when it dominates this
requirement coordinatewise.

For several tasks sharing one experiment language, the least joint requirement is
the coordinatewise join:

* free flag = logical OR;
* each p-depth = maximum across tasks.

When every task has full row rank, no free-separation resource is needed and the
least single finite modulus certifying all tasks is

    lcm(E_1,...,E_k),

which is exactly primewise maximum depth.  If any task has a free cokernel and
targets are unrestricted, no finite family can satisfy the joint all-target
requirement; an unbounded separating resource or an independent target bound is
needed.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import lcm
from typing import Sequence

from .integer_affine_experiment_precision_profile import (
    INFINITE_DEPTH,
    ModularExperimentPrecisionProfile,
)
from .integer_affine_local_global import cokernel_torsion_exponent
from .integer_affine_prime_local_global import prime_power_depths_required_by_torsion
from .integer_future_smith_precision import integer_smith_precision_profile


Matrix = tuple[tuple[int, ...], ...]


def _matrix(values: Sequence[Sequence[int]]) -> Matrix:
    rows = tuple(tuple(row) for row in values)
    if not rows:
        raise ValueError("matrix must contain at least one row")
    width = len(rows[0])
    if width == 0 or any(len(row) != width for row in rows):
        raise ValueError("matrix rows must have one common positive width")
    for row in rows:
        for value in row:
            if isinstance(value, bool) or not isinstance(value, int):
                raise TypeError("matrix entries must be integers")
    return rows


@dataclass(frozen=True)
class AffineCertificationRequirement:
    free_separation_required: bool
    prime_depths: tuple[tuple[int, int], ...]
    torsion_exponent: int

    def required_depth_at(self, prime: int) -> int:
        for current, depth in self.prime_depths:
            if current == prime:
                return depth
        return 0


def affine_certification_requirement(
    matrix: Sequence[Sequence[int]],
) -> AffineCertificationRequirement:
    A = _matrix(matrix)
    profile = integer_smith_precision_profile(A)
    return AffineCertificationRequirement(
        free_separation_required=(len(A) - profile.rational_rank) > 0,
        prime_depths=prime_power_depths_required_by_torsion(A),
        torsion_exponent=cokernel_torsion_exponent(A),
    )


def experiment_profile_satisfies_requirement(
    profile: ModularExperimentPrecisionProfile,
    requirement: AffineCertificationRequirement,
) -> bool:
    if not isinstance(profile, ModularExperimentPrecisionProfile):
        raise TypeError("profile must be ModularExperimentPrecisionProfile")
    if not isinstance(requirement, AffineCertificationRequirement):
        raise TypeError("requirement must be AffineCertificationRequirement")
    if requirement.free_separation_required and not profile.free_integer_separating:
        return False
    for prime, required_depth in requirement.prime_depths:
        available = profile.depth_at(prime)
        if available == INFINITE_DEPTH:
            continue
        if not isinstance(available, int):
            raise AssertionError("experiment profile returned invalid prime depth")
        if available < required_depth:
            return False
    return True


def join_certification_requirements(
    requirements: Sequence[AffineCertificationRequirement],
) -> AffineCertificationRequirement:
    values = tuple(requirements)
    if not values:
        raise ValueError("at least one certification requirement is required")
    if any(not isinstance(value, AffineCertificationRequirement) for value in values):
        raise TypeError("requirements must be AffineCertificationRequirement values")

    primes = sorted({prime for value in values for prime, _ in value.prime_depths})
    joined_depths = tuple(
        (
            prime,
            max(value.required_depth_at(prime) for value in values),
        )
        for prime in primes
    )
    exponent = 1
    for prime, depth in joined_depths:
        exponent *= prime ** depth
    return AffineCertificationRequirement(
        free_separation_required=any(value.free_separation_required for value in values),
        prime_depths=joined_depths,
        torsion_exponent=exponent,
    )


def joint_affine_certification_requirement(
    matrices: Sequence[Sequence[Sequence[int]]],
) -> AffineCertificationRequirement:
    values = tuple(matrices)
    if not values:
        raise ValueError("at least one matrix is required")
    return join_certification_requirements(
        tuple(affine_certification_requirement(matrix) for matrix in values)
    )


def least_joint_finite_all_target_modulus(
    matrices: Sequence[Sequence[Sequence[int]]],
) -> int | None:
    """Least single finite modulus for all tasks, or None if any free part remains."""
    values = tuple(matrices)
    if not values:
        raise ValueError("at least one matrix is required")
    requirements = tuple(affine_certification_requirement(matrix) for matrix in values)
    joined = join_certification_requirements(requirements)
    if joined.free_separation_required:
        return None
    # Equivalent to lcm of individual torsion exponents; compute both ways as a
    # mechanical consistency check.
    direct = 1
    for requirement in requirements:
        direct = lcm(direct, requirement.torsion_exponent)
    if direct != joined.torsion_exponent:
        raise AssertionError("joint prime-depth join disagreed with lcm of exponents")
    return direct
