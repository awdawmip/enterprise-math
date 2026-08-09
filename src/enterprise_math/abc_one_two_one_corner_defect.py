"""Weighted modular corner obstruction for projective alignment in 1-2-1 abc.

In the positive-W orientation of an (a,c)-projective-capacity witness, write

    x = -R + e,   w = R - d,

with outer deficits ``0<=e,d<=2R``.  If

    A*x + B1*y+B2*z = C*w

and ``g=gcd(B1,B2)``, middle-block integrality forces

    A*e + C*d == (A+C)R (mod g).

The exact raw Wronskian capacity loss is

    c*A*e + a*C*d.

Therefore minimizing this weighted congruence defect gives a rigorous lower
bound on projective alignment loss at radius R, before any finer bounded
middle-block representability is checked.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd

from .abc_one_two_one_mu import _congruence_values_in_box, one_two_one_coefficients
from .abc_one_two_one_projective import first_witness_corner_alignment
from .abc_projective_efficiency import projective_wronskian_efficiency


@dataclass(frozen=True)
class ModularCornerDefect:
    abc: tuple[int, int, int]
    radius: int
    modulus: int
    outer_deficits: tuple[int, int]
    weighted_defect: int
    projective_capacity: int
    alignment_lower_bound: Fraction


def modular_corner_defect(
    a: int, b: int, c: int, radius: int
) -> ModularCornerDefect:
    """Minimize the exact outer weighted defect under the forced congruence."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius <= 0:
        raise ValueError("radius must be a positive integer")
    A, B1, B2, C = one_two_one_coefficients(a, b, c)
    efficiency = projective_wronskian_efficiency(a, b, c)
    P_ab, P_ac, P_bc = efficiency.pair_capacities
    if P_ac != min(P_ab, P_ac, P_bc):
        raise ValueError("the (a,c) pair must be a projective capacity minimizer")
    modulus = gcd(B1, B2)
    rhs = (A + C) * radius

    best: tuple[int, int, int] | None = None
    for d in range(0, 2 * radius + 1):
        for e in _congruence_values_in_box(A, rhs - C * d, modulus, 2 * radius):
            if not 0 <= e <= 2 * radius:
                continue
            defect = c * A * e + a * C * d
            candidate = (defect, e, d)
            if best is None or candidate < best:
                best = candidate
    if best is None:
        raise ValueError("no outer corner deficits satisfy the forced congruence")
    defect, e, d = best
    denominator = P_ac * radius - defect
    if denominator <= 0:
        # The congruence alone may be satisfiable only beyond the positive-W
        # corner capacity at a tiny radius; then it gives no finite positive
        # alignment lower bound for an actual positive-W witness.
        alignment = Fraction(1, 1)
    else:
        alignment = Fraction(P_ac * radius, denominator)
    return ModularCornerDefect(
        abc=(a, b, c),
        radius=radius,
        modulus=modulus,
        outer_deficits=(e, d),
        weighted_defect=defect,
        projective_capacity=P_ac,
        alignment_lower_bound=alignment,
    )


def first_witness_modular_alignment_is_sharp(
    a: int, b: int, c: int, mu_upper_bound: int
) -> bool:
    """Return whether the first witness attains the congruence-only defect floor."""
    actual = first_witness_corner_alignment(a, b, c, mu_upper_bound)
    lower = modular_corner_defect(a, b, c, actual.mu)
    if actual.raw_capacity_slack < lower.weighted_defect:
        raise AssertionError("actual witness beat forced modular corner defect")
    if actual.projective_alignment_factor < lower.alignment_lower_bound:
        raise AssertionError("actual alignment beat modular lower bound")
    return (
        actual.raw_capacity_slack == lower.weighted_defect
        and actual.outer_deficits == lower.outer_deficits
        and actual.projective_alignment_factor == lower.alignment_lower_bound
    )
