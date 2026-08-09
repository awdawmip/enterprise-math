"""Projective corner attainment and alignment defect for 1-2-1 abc triples.

For a support pattern ``(1,2,1)`` with additive equation

    A*x + B1*y + B2*z = C*w,

suppose the exact projective Wronskian operator norm is the ``(a,c)`` pair
capacity.  Equality in the dual L1/L-infinity bound forces, after choosing the
positive-W orientation,

    x = -R,   w = R.

Hence a projectively optimal integer witness at radius R must solve

    B1*y+B2*z = (A+C)R,  |y|,|z|<=R.

Writing ``g=gcd(B1,B2)`` gives the necessary congruence

    g | (A+C)R,

so every exact projective-attainment radius is a multiple of

    g / gcd(g,A+C).

For a general first witness with positive W, write

    x = -R + e,   w = R - d,

with ``0<=e,d<=2R``.  The projective capacity slack is then exactly

    c*A*e + a*C*d,

and the middle-block congruence becomes

    g | (A+C)R - A*e - C*d.

This exposes the discrete corner-alignment cost behind the projective factor
from Supplement 43.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd

from .abc_block_value_lattice import block_value_lattice_invariants
from .abc_one_two_one_mu import (
    _bounded_coprime_pair_solution,
    exact_one_two_one_mu,
    one_two_one_coefficients,
)
from .abc_projective_efficiency import projective_wronskian_efficiency


@dataclass(frozen=True)
class OneTwoOneProjectiveWitness:
    abc: tuple[int, int, int]
    radius: int
    coordinates: tuple[int, int, int, int]
    wronskian: int
    absorption_redundancy: int
    projective_ratio: Fraction


@dataclass(frozen=True)
class OneTwoOneCornerAlignment:
    abc: tuple[int, int, int]
    mu: int
    oriented_coordinates: tuple[int, int, int, int]
    outer_deficits: tuple[int, int]
    raw_capacity_slack: int
    congruence_modulus: int
    congruence_residue: int
    projective_alignment_factor: Fraction


def _require_ac_projective_pair(a: int, b: int, c: int) -> int:
    efficiency = projective_wronskian_efficiency(a, b, c)
    P_ab, P_ac, P_bc = efficiency.pair_capacities
    if P_ac != min(P_ab, P_ac, P_bc):
        raise ValueError("the (a,c) pair is not a projective capacity minimizer")
    return P_ac


def ac_projective_radius_modulus(a: int, b: int, c: int) -> int:
    """Return the divisibility step forced on exact (a,c)-corner attainment."""
    A, B1, B2, C = one_two_one_coefficients(a, b, c)
    _require_ac_projective_pair(a, b, c)
    middle_gcd = gcd(B1, B2)
    return middle_gcd // gcd(middle_gcd, A + C)


def ac_projective_witness_at_radius(
    a: int, b: int, c: int, radius: int
) -> OneTwoOneProjectiveWitness | None:
    """Return an integer witness attaining the exact projective corner at R."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius <= 0:
        raise ValueError("radius must be a positive integer")
    A, B1, B2, C = one_two_one_coefficients(a, b, c)
    capacity = _require_ac_projective_pair(a, b, c)
    middle_gcd = gcd(B1, B2)
    target_raw = (A + C) * radius
    if target_raw % middle_gcd:
        return None
    pair = _bounded_coprime_pair_solution(
        B1 // middle_gcd,
        B2 // middle_gcd,
        target_raw // middle_gcd,
        radius,
    )
    if pair is None:
        return None
    y, z = pair
    x = -radius
    w = radius
    derivative_a = A * x
    derivative_b = B1 * y + B2 * z
    derivative_c = C * w
    if derivative_a + derivative_b != derivative_c:
        raise AssertionError("projective corner witness escaped additivity")
    wronskian = a * derivative_b - b * derivative_a
    if wronskian != capacity * radius:
        raise AssertionError("projective corner witness failed exact capacity equality")
    invariants = block_value_lattice_invariants(a, b, c)
    M = invariants.residual_product
    if wronskian % M:
        raise AssertionError("projective corner Wronskian violated residual divisibility")
    eta = wronskian // M
    if eta <= 0:
        raise AssertionError("positive-W projective orientation must have positive eta")
    return OneTwoOneProjectiveWitness(
        abc=(a, b, c),
        radius=radius,
        coordinates=(x, y, z, w),
        wronskian=wronskian,
        absorption_redundancy=eta,
        projective_ratio=Fraction(radius, eta),
    )


def exact_ac_projective_attainment_radius(
    a: int, b: int, c: int, upper_bound: int
) -> OneTwoOneProjectiveWitness:
    """Return the first radius attaining the (a,c) projective optimum.

    Only multiples of the forced congruence modulus need to be tested.
    """
    step = ac_projective_radius_modulus(a, b, c)
    if upper_bound < step:
        raise ValueError("upper bound lies below forced projective modulus")
    for radius in range(step, upper_bound + 1, step):
        witness = ac_projective_witness_at_radius(a, b, c, radius)
        if witness is not None:
            return witness
    raise ValueError("no projective-attainment witness within supplied upper bound")


def first_witness_corner_alignment(
    a: int, b: int, c: int, mu_upper_bound: int
) -> OneTwoOneCornerAlignment:
    """Resolve the exact outer-corner deficit of the first nondegenerate witness."""
    A, B1, B2, C = one_two_one_coefficients(a, b, c)
    capacity = _require_ac_projective_pair(a, b, c)
    result = exact_one_two_one_mu(a, b, c, mu_upper_bound)
    R = result.mu
    x, y, z, w = result.witness.coordinates
    W = result.witness.wronskian
    if W < 0:
        x, y, z, w = (-x, -y, -z, -w)
        W = -W
    e = x + R
    d = R - w
    if not (0 <= e <= 2 * R and 0 <= d <= 2 * R):
        raise AssertionError("oriented witness failed outer-corner deficit bounds")
    slack = c * A * e + a * C * d
    if capacity * R - W != slack:
        raise AssertionError("outer-corner deficits failed projective slack identity")
    middle_gcd = gcd(B1, B2)
    residue = ((A + C) * R - A * e - C * d) % middle_gcd
    if residue != 0:
        raise AssertionError("actual witness failed middle-block congruence")
    alignment = Fraction(capacity * R, W)
    return OneTwoOneCornerAlignment(
        abc=(a, b, c),
        mu=R,
        oriented_coordinates=(x, y, z, w),
        outer_deficits=(e, d),
        raw_capacity_slack=slack,
        congruence_modulus=middle_gcd,
        congruence_residue=residue,
        projective_alignment_factor=alignment,
    )
