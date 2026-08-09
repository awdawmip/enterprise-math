"""Support-dimension boundary for P025 witness precision.

When the prime-labelled witness space has exactly two coordinates, the additive
witness lattice has rank one.  If the Wronskian flag is non-degenerate, the
degeneracy sublattice intersects that rank-one lattice only at zero.  Hence the
ordinary additive first radius and the restricted/non-degenerate first radius
coincide exactly.

This is elementary integer linear algebra.  P025 uses it only to locate the
minimum support dimension at which an independent degeneracy overhead can
appear.
"""

from __future__ import annotations

from math import gcd

from .abc_support import abc_support_state
from .abc_witness_precision import (
    additive_relation_vector,
    witness_coordinates,
    wronskian_relation_vector,
)


def two_coordinate_witness_radius(a: int, b: int, c: int) -> dict[str, object]:
    """Return the exact witness radius when ``supp(abc)`` has size two.

    Let ``alpha=(alpha_0,alpha_1)`` be the primitive additive normal and
    ``beta`` a degeneracy normal.  Non-degeneracy of the flag is equivalent to

        det(alpha,beta) != 0.

    The primitive generator of ``ker_Z(alpha)`` is

        (alpha_1/g, -alpha_0/g),

    where ``g=gcd(|alpha_0|,|alpha_1|)``.  Because ``beta`` is not proportional
    to ``alpha``, this generator is automatically non-degenerate.  Therefore

        rho = mu = U2 = max(|alpha_0|,|alpha_1|)/g.
    """
    abc_support_state(a, b, c)
    coordinates = witness_coordinates(a, b, c)
    if len(coordinates) != 2:
        raise ValueError("the prime-labelled witness support must have size exactly two")

    alpha = additive_relation_vector(a, b, c)
    beta = wronskian_relation_vector(a, b, c)
    determinant = alpha[0] * beta[1] - alpha[1] * beta[0]
    if determinant == 0:
        raise ValueError("the two-coordinate witness flag is degenerate")

    content = gcd(abs(alpha[0]), abs(alpha[1]))
    if content == 0:
        raise AssertionError("primitive additive normal cannot vanish identically")
    generator = (alpha[1] // content, -alpha[0] // content)
    radius = max(abs(generator[0]), abs(generator[1]))
    if radius <= 0:
        raise AssertionError("primitive rank-one kernel generator must be nonzero")

    beta_value = beta[0] * generator[0] + beta[1] * generator[1]
    if beta_value == 0:
        raise AssertionError("nonzero row determinant must make the kernel generator non-degenerate")

    return {
        "triple": (a, b, c),
        "coordinates": coordinates,
        "alpha": alpha,
        "beta": beta,
        "row_determinant": determinant,
        "primitive_generator": generator,
        "rho": radius,
        "mu": radius,
        "U2": radius,
        "nondegeneracy_overhead_over_rho": 0,
    }
