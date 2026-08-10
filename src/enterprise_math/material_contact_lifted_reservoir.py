"""Lifted contact-local material reservoir state and exact body-observation fibers.

This bridge reconnects the E001 material-impulse remainder law to the contact
network incidence algebra.

For ``E`` named contact channels, fix positive impulse amplitude ``A`` and one
nonnegative cumulative raw numerator per channel.  Coordinatewise Euclidean
division gives the exact lifted state

    N = A*j + delta,          0 <= delta_e < A,

where ``j`` is the delivered integer contact-impulse count and ``delta`` is the
contact-local subquantum remainder.  The body momentum layer sees only

    B*j.

Therefore the body-observation fiber has two independent sources of hidden
contact state:

1. local quantization detail ``delta`` inside each delivered-allocation cell;
2. topological allocation directions ``ker_Z B`` between delivered vectors.

The full lifted contact numerator is globally recoverable from body delta for
all nonnegative states iff

    A = 1  and  ker_Z B = 0,

and for graph incidence the second condition is exactly that the contact graph
is a forest.

The local remainder is not merely bookkeeping when the declared future language
can address named contacts.  Repeatedly adding one raw numerator unit to contact
``e`` causes its next delivered quantum after exactly

    A-delta_e          if delta_e>0,
    A                  if delta_e=0.

Thus the vector of first local-carry distances is a bijective encoding of the
remainder vector.  A named-contact future language can therefore recover all
contact-local remainders even when current body momentum cannot see them.

Pooling remainders across channels changes the semantics.  Since each local
remainder is individually subquantum, pooling can fabricate
``floor(sum(delta)/A)`` already-delivered quanta with no causal contact identity.
The reference example ``A=10, delta=(6,6)`` creates one such spurious pooled
quantum although neither contact has delivered anything.

Euclidean division, incidence kernels and graph cycle rank are standard prior
mathematics.  The project contribution is this exact E001 material/contact
precision interface.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Sequence

from .contact_cycle_witness_repair import (
    apply_integer_matrix,
    fundamental_cycle_lattice,
)


Vector = tuple[int, ...]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _require_positive_int(name: str, value: int) -> None:
    _require_int(name, value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def _nonnegative_vector(
    values: Sequence[int] | Iterable[int],
    length: int,
    *,
    name: str,
) -> Vector:
    result = tuple(values)
    if len(result) != length:
        raise ValueError(f"{name} must have length {length}")
    for value in result:
        _require_int(name, value)
        if value < 0:
            raise ValueError(f"{name} entries must be nonnegative")
    return result


def _incidence(
    incidence: Sequence[Sequence[int]],
) -> tuple[tuple[int, ...], ...]:
    rows = tuple(tuple(row) for row in incidence)
    fundamental_cycle_lattice(rows)
    return rows


@dataclass(frozen=True)
class LiftedContactReservoirState:
    amplitude: int
    raw_numerators: Vector
    delivered_impulse_quanta: Vector
    contact_remainders: Vector
    body_delta: Vector

    @property
    def contact_count(self) -> int:
        return len(self.raw_numerators)


def lifted_contact_reservoir_state(
    incidence: Sequence[Sequence[int]],
    raw_numerators: Sequence[int],
    amplitude: int,
) -> LiftedContactReservoirState:
    """Split exact named-contact raw numerators into delivered quanta/remainders."""
    matrix = _incidence(incidence)
    _require_positive_int("amplitude", amplitude)
    contact_count = len(matrix[0])
    raw = _nonnegative_vector(
        raw_numerators,
        contact_count,
        name="raw_numerators",
    )
    delivered = tuple(value // amplitude for value in raw)
    remainders = tuple(value % amplitude for value in raw)
    if raw != tuple(
        amplitude * quotient + remainder
        for quotient, remainder in zip(
            delivered,
            remainders,
            strict=True,
        )
    ):
        raise AssertionError("lifted contact Euclidean reconstruction failed")
    return LiftedContactReservoirState(
        amplitude=amplitude,
        raw_numerators=raw,
        delivered_impulse_quanta=delivered,
        contact_remainders=remainders,
        body_delta=apply_integer_matrix(matrix, delivered),
    )


def same_body_delta_from_lifted_contacts(
    incidence: Sequence[Sequence[int]],
    left_raw_numerators: Sequence[int],
    right_raw_numerators: Sequence[int],
    amplitude: int,
) -> bool:
    """Exact fiber criterion for two lifted contact numerator states."""
    matrix = _incidence(incidence)
    left = lifted_contact_reservoir_state(
        matrix,
        left_raw_numerators,
        amplitude,
    )
    right = lifted_contact_reservoir_state(
        matrix,
        right_raw_numerators,
        amplitude,
    )
    delivered_difference = tuple(
        right_value - left_value
        for left_value, right_value in zip(
            left.delivered_impulse_quanta,
            right.delivered_impulse_quanta,
            strict=True,
        )
    )
    kernel_test = not any(
        apply_integer_matrix(matrix, delivered_difference)
    )
    observed = left.body_delta == right.body_delta
    if observed != kernel_test:
        raise AssertionError("lifted body equivalence disagreed with incidence kernel")
    return observed


def local_first_delivery_distance(
    remainder: int,
    amplitude: int,
) -> int:
    """Unit raw additions until this named channel next delivers one quantum."""
    _require_positive_int("amplitude", amplitude)
    _require_int("remainder", remainder)
    if not 0 <= remainder < amplitude:
        raise ValueError("remainder must lie in 0..amplitude-1")
    return amplitude if remainder == 0 else amplitude - remainder


def remainder_from_first_delivery_distance(
    distance: int,
    amplitude: int,
) -> int:
    """Inverse of ``local_first_delivery_distance``."""
    _require_positive_int("amplitude", amplitude)
    _require_int("distance", distance)
    if not 1 <= distance <= amplitude:
        raise ValueError("distance must lie in 1..amplitude")
    return 0 if distance == amplitude else amplitude - distance


def named_local_carry_signature(
    raw_numerators: Sequence[int],
    amplitude: int,
) -> Vector:
    """Future signature of first delivered events under named unit raw actions."""
    _require_positive_int("amplitude", amplitude)
    raw = tuple(raw_numerators)
    for value in raw:
        _require_int("raw_numerator", value)
        if value < 0:
            raise ValueError("raw numerators must be nonnegative")
    return tuple(
        local_first_delivery_distance(
            value % amplitude,
            amplitude,
        )
        for value in raw
    )


def remainder_vector_from_carry_signature(
    signature: Sequence[int],
    amplitude: int,
) -> Vector:
    _require_positive_int("amplitude", amplitude)
    return tuple(
        remainder_from_first_delivery_distance(
            distance,
            amplitude,
        )
        for distance in signature
    )


@dataclass(frozen=True)
class ContactLiftedAmbiguityReport:
    amplitude: int
    contact_count: int
    cycle_rank: int
    remainder_states_per_delivered_allocation: int
    delivered_allocation_identifiable_from_body_delta: bool
    subquantum_detail_present: bool
    lifted_state_globally_identifiable_from_body_delta: bool


def contact_lifted_ambiguity_report(
    incidence: Sequence[Sequence[int]],
    amplitude: int,
) -> ContactLiftedAmbiguityReport:
    """Topology × quantization classification of hidden contact state."""
    matrix = _incidence(incidence)
    _require_positive_int("amplitude", amplitude)
    contact_count = len(matrix[0])
    cycle_rank = fundamental_cycle_lattice(matrix).cycle_rank
    delivered_identifiable = cycle_rank == 0
    subquantum_present = amplitude > 1
    globally_identifiable = delivered_identifiable and not subquantum_present
    return ContactLiftedAmbiguityReport(
        amplitude=amplitude,
        contact_count=contact_count,
        cycle_rank=cycle_rank,
        remainder_states_per_delivered_allocation=amplitude ** contact_count,
        delivered_allocation_identifiable_from_body_delta=delivered_identifiable,
        subquantum_detail_present=subquantum_present,
        lifted_state_globally_identifiable_from_body_delta=globally_identifiable,
    )


@dataclass(frozen=True)
class PooledRemainderComparator:
    amplitude: int
    local_remainders: Vector
    pooled_total: int
    pooled_delivered_quanta: int
    pooled_remainder: int

    @property
    def creates_spurious_delivered_quantum(self) -> bool:
        return self.pooled_delivered_quanta > 0


def pooled_remainder_comparator(
    remainders: Sequence[int],
    amplitude: int,
) -> PooledRemainderComparator:
    """Comparator showing what is fabricated by erasing contact identity."""
    _require_positive_int("amplitude", amplitude)
    values = tuple(remainders)
    if not values:
        raise ValueError("at least one contact remainder is required")
    for remainder in values:
        _require_int("remainder", remainder)
        if not 0 <= remainder < amplitude:
            raise ValueError("every local remainder must lie in 0..amplitude-1")
    total = sum(values)
    return PooledRemainderComparator(
        amplitude=amplitude,
        local_remainders=values,
        pooled_total=total,
        pooled_delivered_quanta=total // amplitude,
        pooled_remainder=total % amplitude,
    )
