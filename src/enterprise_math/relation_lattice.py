"""Integer lattice invariants of P019 capacity-weighted relation fields.

For capacities m with gcd g, the weighted relation map c -> c wedge m has
nonzero Smith invariant g in each of its k-1 independent relation directions.
Equal relation fields differ by integer multiples of the primitive capacity
vector m/g, changing the grand total by M/g.
"""

from __future__ import annotations

from math import gcd

from .weighted_relation_field import weighted_relation_field


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
    """Universal Smith quantum of independent weighted relation coordinates."""
    return capacity_gcd(capacities)


def relation_translation_period(capacities: tuple[int, ...]) -> int:
    """Grand-total change produced by the primitive field-preserving shift."""
    divisor = capacity_gcd(capacities)
    return sum(capacities) // divisor


def relation_precision_duality(capacities: tuple[int, ...]) -> tuple[int, int, int]:
    """Return (relation quantum g, translation period tau, total capacity M)."""
    quantum = relation_quantum(capacities)
    period = relation_translation_period(capacities)
    total = sum(capacities)
    if quantum * period != total:
        raise AssertionError("relation quantum times translation period must equal total capacity")
    return quantum, period, total


def field_preserving_shift(
    capacities: tuple[int, ...], totals: tuple[int, ...], steps: int
) -> tuple[int, ...]:
    """Shift totals by steps*(m/g), preserving every weighted relation."""
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
    """Return t when right-left=t*(m/g), or None if fields/states do not match so."""
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
    """Check the necessary divisibility law g_fine | g_coarse."""
    fine = capacity_gcd(fine_capacities)
    coarse = capacity_gcd(coarse_capacities)
    return coarse % fine == 0
