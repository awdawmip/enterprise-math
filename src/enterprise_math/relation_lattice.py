"""Integer lattice invariants of A3 capacity-weighted relation fields.

Semantic replay from the historical relation-quotient branch. For capacities
``m`` with gcd ``g``, the weighted relation map has the same common integer
quantum ``g`` in each independent relation direction. Equal relation fields
differ by integer multiples of the primitive capacity vector ``m/g``, changing
the grand total by ``sum(m)/g``.

The lower-generation criterion below is an Enterprise specialization of
standard integer-lattice / Smith-normal-form mathematics.  It does not define a
new R012 lattice family: it closes a missing converse inside the existing A3
relation-lattice owner.
"""

from __future__ import annotations

from math import gcd

from .weighted_relation_field import (
    WeightedField,
    weighted_relation_field,
    weighted_relation_field_is_closed,
)


def _require_capacities(capacities: tuple[int, ...]) -> None:
    if not isinstance(capacities, tuple) or not capacities:
        raise ValueError("capacities must be a non-empty tuple")
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value <= 0
        for value in capacities
    ):
        raise ValueError("capacities must be positive integers")


def capacity_gcd(capacities: tuple[int, ...]) -> int:
    """Greatest common divisor of current block capacities."""
    _require_capacities(capacities)
    result = 0
    for capacity in capacities:
        result = gcd(result, capacity)
    return result


def primitive_capacity_vector(capacities: tuple[int, ...]) -> tuple[int, ...]:
    """Capacities divided by their common relation quantum g."""
    divisor = capacity_gcd(capacities)
    return tuple(capacity // divisor for capacity in capacities)


def relation_quantum(capacities: tuple[int, ...]) -> int:
    """Universal integer quantum of weighted relation coordinates."""
    return capacity_gcd(capacities)


def relation_translation_period(capacities: tuple[int, ...]) -> int:
    """Grand-total change produced by the primitive field-preserving shift."""
    divisor = capacity_gcd(capacities)
    return sum(capacities) // divisor


def relation_precision_duality(capacities: tuple[int, ...]) -> tuple[int, int, int]:
    """Return ``(relation quantum g, translation period tau, total capacity M)``."""
    quantum = relation_quantum(capacities)
    period = relation_translation_period(capacities)
    total = sum(capacities)
    if quantum * period != total:
        raise AssertionError("relation quantum times translation period must equal total capacity")
    return quantum, period, total


def field_preserving_shift(
    capacities: tuple[int, ...], totals: tuple[int, ...], steps: int
) -> tuple[int, ...]:
    """Shift totals by ``steps*(m/g)``, preserving every weighted relation."""
    _require_capacities(capacities)
    if not isinstance(totals, tuple) or len(totals) != len(capacities):
        raise ValueError("totals must match capacities")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in totals):
        raise ValueError("totals must be integers")
    if isinstance(steps, bool) or not isinstance(steps, int):
        raise ValueError("steps must be an integer")
    primitive = primitive_capacity_vector(capacities)
    shifted = tuple(total + steps * step for total, step in zip(totals, primitive))
    if weighted_relation_field(capacities, shifted) != weighted_relation_field(capacities, totals):
        raise AssertionError("primitive capacity shift must preserve the weighted field")
    return shifted


def same_field_shift_multiple(
    capacities: tuple[int, ...], left: tuple[int, ...], right: tuple[int, ...]
) -> int | None:
    """Return ``t`` when ``right-left=t*(m/g)``, else ``None``."""
    _require_capacities(capacities)
    if not isinstance(left, tuple) or not isinstance(right, tuple):
        raise ValueError("left and right must be tuples")
    if len(left) != len(capacities) or len(right) != len(capacities):
        raise ValueError("states must match capacities")
    if any(
        isinstance(value, bool) or not isinstance(value, int)
        for value in left + right
    ):
        raise ValueError("state entries must be integers")
    if weighted_relation_field(capacities, left) != weighted_relation_field(capacities, right):
        return None
    primitive = primitive_capacity_vector(capacities)
    differences = tuple(r - l for l, r in zip(left, right))
    candidate = None
    for difference, step in zip(differences, primitive):
        if difference % step != 0:
            return None
        current = difference // step
        if candidate is None:
            candidate = current
        elif current != candidate:
            return None
    return 0 if candidate is None else candidate


def coarsening_quantum_divides(
    fine_capacities: tuple[int, ...], coarse_capacities: tuple[int, ...]
) -> bool:
    """Check the necessary divisibility law ``g_fine | g_coarse``."""
    fine = capacity_gcd(fine_capacities)
    coarse = capacity_gcd(coarse_capacities)
    return coarse % fine == 0


def _extended_gcd(left: int, right: int) -> tuple[int, int, int]:
    """Return ``(g,s,t)`` with ``s*left+t*right=g=gcd(left,right)``."""
    old_r, r = left, right
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t
    return old_r, old_s, old_t


def _primitive_bezout_coefficients(primitive: tuple[int, ...]) -> tuple[int, ...]:
    """Return coefficients ``b`` with ``sum b_i*primitive_i = 1``."""
    if not primitive:
        raise ValueError("primitive capacity vector must be nonempty")
    coefficients = [1]
    common = primitive[0]
    for value in primitive[1:]:
        common, scale_existing, scale_new = _extended_gcd(common, value)
        coefficients = [scale_existing * coefficient for coefficient in coefficients]
        coefficients.append(scale_new)
    if common != 1:
        raise AssertionError("primitive capacity vector must have gcd one")
    result = tuple(coefficients)
    if sum(coefficient * value for coefficient, value in zip(result, primitive)) != 1:
        raise AssertionError("Bezout coefficients must certify primitivity")
    return result


def relation_field_is_lower_generated(
    capacities: tuple[int, ...], field: WeightedField
) -> bool:
    """Whether one closed integer field is generated by integer block totals.

    If ``m=g*v`` with primitive ``v``, weighted closure gives the saturated
    lattice ``C_m = im L_v``.  The actual lower-generated lattice is
    ``G_m = im L_m = g*C_m``.  Therefore a closed field is lower-generated
    exactly when every relation coordinate is divisible by the already
    canonical relation quantum ``g``.

    This criterion is the executable A3-owner specialization of standard
    integer-lattice / Smith-normal-form mathematics.
    """
    _require_capacities(capacities)
    if not weighted_relation_field_is_closed(capacities, field):
        return False
    quantum = relation_quantum(capacities)
    return all(value % quantum == 0 for row in field for value in row)


def lower_generation_witness(
    capacities: tuple[int, ...], field: WeightedField
) -> tuple[int, ...]:
    """Construct integer totals generating a lower-generated closed field.

    Raises ``ValueError`` if the field is not weighted-closed or if it lies in
    the saturated closure lattice but outside the lower-generated sublattice.
    The construction uses a Bezout certificate for the primitive capacity
    vector and proves the returned witness by replaying ``weighted_relation_field``.
    """
    _require_capacities(capacities)
    if not weighted_relation_field_is_closed(capacities, field):
        raise ValueError("weighted relation field is not closed")
    quantum = relation_quantum(capacities)
    if any(value % quantum != 0 for row in field for value in row):
        raise ValueError("closed field is not divisible by the relation quantum")

    primitive = primitive_capacity_vector(capacities)
    bezout = _primitive_bezout_coefficients(primitive)
    normalized = tuple(
        tuple(value // quantum for value in row)
        for row in field
    )
    totals = tuple(
        sum(coefficient * normalized[i][k] for k, coefficient in enumerate(bezout))
        for i in range(len(capacities))
    )
    if weighted_relation_field(capacities, totals) != field:
        raise AssertionError("constructed lower-generation witness must reproduce the field")
    return totals


def relation_lattice_quotient_invariant_factors(
    capacities: tuple[int, ...],
) -> tuple[int, ...]:
    """Invariant factors for ``C_m / G_m ≅ (Z/gZ)^(n-1)``.

    The returned tuple contains ``g`` exactly ``n-1`` times.  For ``g=1`` these
    are trivial cyclic factors.  This is owner-local metadata, not a separate
    quotient implementation.
    """
    quantum = relation_quantum(capacities)
    return (quantum,) * (len(capacities) - 1)


def relation_lattice_index(capacities: tuple[int, ...]) -> int:
    """Return ``[C_m:G_m]=g^(n-1)`` for the A3 relation lattice."""
    quantum = relation_quantum(capacities)
    return quantum ** (len(capacities) - 1)
