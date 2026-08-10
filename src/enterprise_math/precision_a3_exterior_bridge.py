"""Exact bridge: A3 weighted relation fields are rank-one exterior tokens.

For positive capacities m=(m_i) and integer totals c=(c_i), A3 defines

    Z_ij = m_j*c_i - m_i*c_j.

The fraction-free linear-lift compiler with one difference basis row m gives
2x2 determinant coordinates

    D_ij = det [[m_i,m_j],[c_i,c_j]] = m_i*c_j-m_j*c_i.

Hence Z_ij=-D_ij for i<j.  The A3 weighted closure law

    m_k Z_ij + m_i Z_jk + m_j Z_ki = 0

is exactly the coordinate identity m wedge (m wedge c)=0.  Equal A3 fields are
therefore the same integer-lattice quotient as equal rank-one exterior tokens;
the primitive field-preserving shift is the primitive capacity vector m/gcd(m).

Exterior algebra/minors are prior mathematics.  This module records the exact
cross-owner reduction between the existing A3 object and the R004 representation
compiler; it does not re-own A3.
"""
from __future__ import annotations

from enterprise_math.precision_integer_linear_lift_compiler import (
    determinant_relation_token,
)
from enterprise_math.relation_lattice import primitive_capacity_vector
from enterprise_math.weighted_relation_field import (
    weighted_relation_dimension,
    weighted_relation_field,
    weighted_relation_field_is_closed,
)


def _state(capacities: tuple[int, ...], totals: tuple[int, ...]) -> None:
    if not capacities or len(capacities) != len(totals):
        raise ValueError("capacities/totals must be nonempty and have equal width")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in capacities
    ):
        raise ValueError("capacities must be positive integers")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in totals):
        raise ValueError("totals must be integers")


def upper_pair_indices(width: int) -> tuple[tuple[int, int], ...]:
    if isinstance(width, bool) or not isinstance(width, int) or width <= 0:
        raise ValueError("width must be positive")
    return tuple((i, j) for i in range(width) for j in range(i + 1, width))


def a3_upper_relation_token(
    capacities: tuple[int, ...], totals: tuple[int, ...]
) -> tuple[int, ...]:
    _state(capacities, totals)
    field = weighted_relation_field(capacities, totals)
    return tuple(field[i][j] for i, j in upper_pair_indices(len(capacities)))


def exterior_upper_relation_token(
    capacities: tuple[int, ...], totals: tuple[int, ...]
) -> tuple[int, ...]:
    _state(capacities, totals)
    return determinant_relation_token(totals, (capacities,))


def a3_exterior_identity_holds(
    capacities: tuple[int, ...], totals: tuple[int, ...]
) -> bool:
    """Check Z_upper = - exterior determinant token."""
    a3 = a3_upper_relation_token(capacities, totals)
    exterior = exterior_upper_relation_token(capacities, totals)
    return a3 == tuple(-value for value in exterior)


def a3_closure_defects(
    capacities: tuple[int, ...], totals: tuple[int, ...]
) -> tuple[int, ...]:
    """Return all m_k Z_ij+m_i Z_jk+m_j Z_ki defects for i<j<k."""
    _state(capacities, totals)
    field = weighted_relation_field(capacities, totals)
    defects = []
    for i in range(len(capacities)):
        for j in range(i + 1, len(capacities)):
            for k in range(j + 1, len(capacities)):
                defects.append(
                    capacities[k] * field[i][j]
                    + capacities[i] * field[j][k]
                    + capacities[j] * field[k][i]
                )
    return tuple(defects)


def a3_closure_is_exterior_identity(
    capacities: tuple[int, ...], totals: tuple[int, ...]
) -> bool:
    _state(capacities, totals)
    field = weighted_relation_field(capacities, totals)
    return (
        a3_exterior_identity_holds(capacities, totals)
        and weighted_relation_field_is_closed(capacities, field)
        and all(defect == 0 for defect in a3_closure_defects(capacities, totals))
    )


def a3_exterior_quotient_codimension(capacities: tuple[int, ...]) -> int:
    """Rank-one shift span leaves ambient quotient dimension n-1."""
    if not capacities:
        raise ValueError("capacities must be nonempty")
    expected = len(capacities) - 1
    actual = weighted_relation_dimension(capacities)
    if actual != expected:
        raise AssertionError("A3 relation dimension must match rank-one quotient codimension")
    return actual


def field_preserving_primitive_direction(
    capacities: tuple[int, ...]
) -> tuple[int, ...]:
    """Primitive integer generator of the rank-one exterior kernel."""
    return primitive_capacity_vector(capacities)
