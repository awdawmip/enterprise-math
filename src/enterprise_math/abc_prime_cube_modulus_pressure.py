"""Projective threshold pressure on repeated prime-cube cyclotomic moduli.

Cube sum: activation forces multiplicity into Phi_6, hence its full repeated
prime-power modulus is at least ``7*T*rad(center)``.

Cube difference: activation gives ``m(radius)*m(Phi_3) >= T*center``.  For any
integer split H with 1<=H<=T*center, either ``m(radius)>=H`` or the repeated
Phi_3 modulus M satisfies ``H*M > 7*T*center``.

Inside the P018 size range, taking H=radius+1 kills the radius branch and forces
all threshold pressure into the cyclotomic congruence modulus.
"""

from __future__ import annotations

from dataclasses import dataclass

from .abc_prime_cube_centered import (
    prime_cube_difference_centered_state,
    prime_cube_sum_centered_state,
)
from .abc_prime_cube_cyclotomic_congruence import (
    prime_cube_cyclotomic_congruence_signature,
)
from .abc_support import multiplicity_residual, radical


@dataclass(frozen=True)
class CubeSumModulusPressure:
    left_prime: int
    right_prime: int
    threshold: int
    center: int
    center_radical: int
    quadratic_residual: int
    repeated_modulus: int
    lower_bound: int


@dataclass(frozen=True)
class CubeDifferenceModulusPressure:
    left_prime: int
    right_prime: int
    threshold: int
    split_horizon: int
    center: int
    radius: int
    radius_residual: int
    quadratic_residual: int
    branch: str
    repeated_modulus: int | None


def cube_sum_modulus_pressure(q: int, p: int, threshold: int) -> CubeSumModulusPressure:
    if isinstance(threshold, bool) or not isinstance(threshold, int) or threshold < 1:
        raise ValueError("threshold must be an integer >=1")
    state = prime_cube_sum_centered_state(q, p)
    if state.projective_atom_value < threshold:
        raise ValueError("cube-sum atom does not cross supplied threshold")
    signature = prime_cube_cyclotomic_congruence_signature(q, p, "sum")
    if not signature.constraints:
        raise AssertionError("activated cube sum must have repeated Phi_6 support")
    E = state.quadratic_factor
    residual = multiplicity_residual(E)
    lower = 7 * threshold * radical(state.center)
    if signature.repeated_modulus < lower:
        raise AssertionError("cube-sum repeated modulus lost threshold lower bound")
    return CubeSumModulusPressure(
        left_prime=q,
        right_prime=p,
        threshold=threshold,
        center=state.center,
        center_radical=radical(state.center),
        quadratic_residual=residual,
        repeated_modulus=signature.repeated_modulus,
        lower_bound=lower,
    )


def cube_difference_modulus_pressure(
    q: int, p: int, threshold: int, split_horizon: int
) -> CubeDifferenceModulusPressure:
    if isinstance(threshold, bool) or not isinstance(threshold, int) or threshold < 1:
        raise ValueError("threshold must be an integer >=1")
    if (
        isinstance(split_horizon, bool)
        or not isinstance(split_horizon, int)
        or split_horizon < 1
    ):
        raise ValueError("split_horizon must be a positive integer")
    state = prime_cube_difference_centered_state(q, p)
    if state.projective_atom_value < threshold:
        raise ValueError("cube-difference atom does not cross supplied threshold")
    B = state.center
    A = state.radius
    if split_horizon > threshold * B:
        raise ValueError("require split_horizon <= threshold*center")
    mA = multiplicity_residual(A)
    mD = multiplicity_residual(state.quadratic_factor)
    # Exact Stage-75 formula implies eps*g*mA*mD >= 6*T*B with eps*g<=6.
    if mA * mD < threshold * B:
        raise AssertionError("cube-difference threshold lost residual product pressure")
    if mA >= split_horizon:
        return CubeDifferenceModulusPressure(
            left_prime=q,
            right_prime=p,
            threshold=threshold,
            split_horizon=split_horizon,
            center=B,
            radius=A,
            radius_residual=mA,
            quadratic_residual=mD,
            branch="radius-residual",
            repeated_modulus=None,
        )

    signature = prime_cube_cyclotomic_congruence_signature(q, p, "difference")
    if not signature.constraints:
        raise AssertionError("quadratic branch must have repeated Phi_3 support")
    M = signature.repeated_modulus
    if split_horizon * M <= 7 * threshold * B:
        raise AssertionError("cube-difference cyclotomic modulus lost split lower bound")
    return CubeDifferenceModulusPressure(
        left_prime=q,
        right_prime=p,
        threshold=threshold,
        split_horizon=split_horizon,
        center=B,
        radius=A,
        radius_residual=mA,
        quadratic_residual=mD,
        branch="cyclotomic-modulus",
        repeated_modulus=M,
    )


def p018_cube_difference_modulus_pressure(q: int, p: int, threshold: int) -> CubeDifferenceModulusPressure:
    """Force the cyclotomic branch under the P018 ``q>radius^2`` size gate."""
    state = prime_cube_difference_centered_state(q, p)
    if q <= state.radius * state.radius:
        raise ValueError("centered prime pair lies outside P018 q>radius^2 range")
    result = cube_difference_modulus_pressure(
        q, p, threshold, state.radius + 1
    )
    if result.branch != "cyclotomic-modulus":
        raise AssertionError("P018 size gate should eliminate radius-residual branch")
    return result
