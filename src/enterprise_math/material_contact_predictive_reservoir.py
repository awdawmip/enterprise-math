"""Exact predictive quotient for named contact-local raw numerator actions.

The lifted material/contact state stores nonnegative contact raw numerators

    N = A*j + delta,      0 <= delta_e < A,

while the present body observation sees only ``b=Bj``.  Exact state equality is
strictly finer than future equivalence for a declared local action language.

Declare one primitive future action ``U_e`` for every named contact: add one raw
numerator unit to that contact.  Observe the body delta after every future word.
Then the exact predictive state is

    (b, delta) = (B*j, N mod A).

The hidden cycle component of delivered allocation ``j`` is irrelevant for this
language.  One projected local action closes on ``(b,delta)``:

* if ``delta_e < A-1``, increment only ``delta_e``;
* if ``delta_e = A-1``, reset it to zero and update ``b -> b+B e``.

Thus all named local future body outputs factor through ``(b,delta)`` even on a
cyclic contact graph.

The quotient is also exact/minimal for this language.  If two states have the
same body delta but different remainder vectors, choose a contact where the
remainders differ and repeatedly apply its named unit action.  The state with
the shorter next-carry distance delivers a nonzero incidence column before the
other.  A separating word always has length at most ``A-1``.  Therefore infinite
future equivalence is exactly equality of ``(b,delta)``.

At bounded horizon ``h``, one contact remainder is observed only through its
truncated first-carry distance.  There are exactly

    min(A, h+1)

predictive remainder classes per named contact, and therefore exactly

    min(A, h+1)^E

remainder signatures inside one fixed body-delta class when all ``E`` contacts
are independently addressable.  Horizon ``A-1`` is sufficient to recover the
entire remainder vector.

If a later material law also reads cumulative contact witness ``Cj`` (damage,
fatigue, delivered-count history, etc.), this quotient must be refined by the
cycle-witness repair from the parent bridge.  The result therefore cleanly
separates predictive sufficiency from exact lifted-state reconstruction.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Iterable, Sequence

from .contact_cycle_witness_repair import apply_integer_matrix
from .material_contact_lifted_reservoir import (
    LiftedContactReservoirState,
    lifted_contact_reservoir_state,
    local_first_delivery_distance,
)


Vector = tuple[int, ...]


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _require_nonnegative_int(name: str, value: int) -> None:
    _require_int(name, value)
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")


def _require_positive_int(name: str, value: int) -> None:
    _require_int(name, value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def _incidence(incidence: Sequence[Sequence[int]]) -> tuple[tuple[int, ...], ...]:
    rows = tuple(tuple(row) for row in incidence)
    if not rows or not rows[0]:
        raise ValueError("incidence must be nonempty")
    width = len(rows[0])
    if any(len(row) != width for row in rows):
        raise ValueError("incidence rows must have equal length")
    for edge in range(width):
        column = tuple(row[edge] for row in rows)
        if column.count(-1) != 1 or column.count(1) != 1 or any(
            value not in (-1, 0, 1) for value in column
        ):
            raise ValueError(
                "each incidence column must contain exactly one -1 and one +1"
            )
    return rows


@dataclass(frozen=True)
class PredictiveContactReservoirState:
    amplitude: int
    body_delta: Vector
    contact_remainders: Vector

    @property
    def contact_count(self) -> int:
        return len(self.contact_remainders)


def predictive_contact_reservoir_state(
    incidence: Sequence[Sequence[int]],
    raw_numerators: Sequence[int],
    amplitude: int,
) -> PredictiveContactReservoirState:
    """Project full lifted state to the exact named-local predictive quotient."""
    lifted = lifted_contact_reservoir_state(
        incidence,
        raw_numerators,
        amplitude,
    )
    return PredictiveContactReservoirState(
        amplitude=amplitude,
        body_delta=lifted.body_delta,
        contact_remainders=lifted.contact_remainders,
    )


def apply_named_unit_action_to_lifted_state(
    incidence: Sequence[Sequence[int]],
    state: LiftedContactReservoirState,
    contact: int,
) -> LiftedContactReservoirState:
    """Direct full-state action: add one raw numerator unit to one named contact."""
    matrix = _incidence(incidence)
    if not isinstance(state, LiftedContactReservoirState):
        raise TypeError("state must be LiftedContactReservoirState")
    if state.contact_count != len(matrix[0]):
        raise ValueError("state contact count does not match incidence")
    _require_int("contact", contact)
    if not 0 <= contact < state.contact_count:
        raise ValueError("contact is outside the contact set")
    raw = list(state.raw_numerators)
    raw[contact] += 1
    return lifted_contact_reservoir_state(
        matrix,
        tuple(raw),
        state.amplitude,
    )


def apply_named_unit_action_to_predictive_state(
    incidence: Sequence[Sequence[int]],
    state: PredictiveContactReservoirState,
    contact: int,
) -> PredictiveContactReservoirState:
    """Exact descended update on ``(body_delta,remainder_vector)``."""
    matrix = _incidence(incidence)
    if not isinstance(state, PredictiveContactReservoirState):
        raise TypeError("state must be PredictiveContactReservoirState")
    if state.contact_count != len(matrix[0]):
        raise ValueError("state contact count does not match incidence")
    _require_int("contact", contact)
    if not 0 <= contact < state.contact_count:
        raise ValueError("contact is outside the contact set")

    remainders = list(state.contact_remainders)
    body_delta = state.body_delta
    if remainders[contact] == state.amplitude - 1:
        remainders[contact] = 0
        body_delta = tuple(
            value + matrix[body][contact]
            for body, value in enumerate(body_delta)
        )
    else:
        remainders[contact] += 1

    return PredictiveContactReservoirState(
        amplitude=state.amplitude,
        body_delta=body_delta,
        contact_remainders=tuple(remainders),
    )


def apply_named_word_to_lifted_state(
    incidence: Sequence[Sequence[int]],
    state: LiftedContactReservoirState,
    word: Iterable[int],
) -> LiftedContactReservoirState:
    current = state
    for contact in tuple(word):
        current = apply_named_unit_action_to_lifted_state(
            incidence,
            current,
            contact,
        )
    return current


def apply_named_word_to_predictive_state(
    incidence: Sequence[Sequence[int]],
    state: PredictiveContactReservoirState,
    word: Iterable[int],
) -> PredictiveContactReservoirState:
    current = state
    for contact in tuple(word):
        current = apply_named_unit_action_to_predictive_state(
            incidence,
            current,
            contact,
        )
    return current


def named_word_body_signature(
    incidence: Sequence[Sequence[int]],
    state: PredictiveContactReservoirState,
    word: Iterable[int],
) -> Vector:
    return apply_named_word_to_predictive_state(
        incidence,
        state,
        word,
    ).body_delta


def predictive_projection_commutes_with_named_word(
    incidence: Sequence[Sequence[int]],
    raw_numerators: Sequence[int],
    amplitude: int,
    word: Iterable[int],
) -> bool:
    """Exact descent check: full evolution then projection = projected evolution."""
    matrix = _incidence(incidence)
    full = lifted_contact_reservoir_state(
        matrix,
        raw_numerators,
        amplitude,
    )
    projected = PredictiveContactReservoirState(
        amplitude=full.amplitude,
        body_delta=full.body_delta,
        contact_remainders=full.contact_remainders,
    )
    full_after = apply_named_word_to_lifted_state(
        matrix,
        full,
        word,
    )
    projected_after = apply_named_word_to_predictive_state(
        matrix,
        projected,
        word,
    )
    expected = PredictiveContactReservoirState(
        amplitude=full_after.amplitude,
        body_delta=full_after.body_delta,
        contact_remainders=full_after.contact_remainders,
    )
    return projected_after == expected


def shortest_named_remainder_separator(
    left_remainders: Sequence[int],
    right_remainders: Sequence[int],
    amplitude: int,
) -> tuple[int, ...] | None:
    """Shortest repeated named-contact word separating two remainder vectors.

    The returned word acts on one contact only and has length at most ``A-1``.
    ``None`` means the remainder vectors are equal.
    """
    _require_positive_int("amplitude", amplitude)
    left = tuple(left_remainders)
    right = tuple(right_remainders)
    if len(left) != len(right):
        raise ValueError("remainder vectors must have equal length")
    for value in (*left, *right):
        _require_int("remainder", value)
        if not 0 <= value < amplitude:
            raise ValueError("remainders must lie in 0..amplitude-1")
    if left == right:
        return None

    best: tuple[int, int] | None = None
    for contact, (left_value, right_value) in enumerate(
        zip(left, right, strict=True)
    ):
        if left_value == right_value:
            continue
        left_distance = local_first_delivery_distance(
            left_value,
            amplitude,
        )
        right_distance = local_first_delivery_distance(
            right_value,
            amplitude,
        )
        length = min(left_distance, right_distance)
        if left_distance == right_distance:
            raise AssertionError("distinct remainders produced equal carry distance")
        candidate = (length, contact)
        if best is None or candidate < best:
            best = candidate
    if best is None:
        raise AssertionError("distinct remainder vectors lost every separator")
    length, contact = best
    if length > max(0, amplitude - 1):
        raise AssertionError("remainder separator exceeded the exact A-1 horizon")
    return (contact,) * length


def one_contact_horizon_remainder_class_count(
    amplitude: int,
    horizon: int,
) -> int:
    """Exact remainder classes visible by named unit actions through horizon ``h``."""
    _require_positive_int("amplitude", amplitude)
    _require_nonnegative_int("horizon", horizon)
    return min(amplitude, horizon + 1)


def fixed_body_horizon_remainder_class_count(
    contact_count: int,
    amplitude: int,
    horizon: int,
) -> int:
    """Exact product class count when every named contact is independently probeable."""
    _require_positive_int("contact_count", contact_count)
    classes = one_contact_horizon_remainder_class_count(
        amplitude,
        horizon,
    )
    return classes ** contact_count


def truncated_carry_signature(
    remainders: Sequence[int],
    amplitude: int,
    horizon: int,
) -> Vector:
    """Canonical finite-horizon remainder signature inside one body class."""
    _require_positive_int("amplitude", amplitude)
    _require_nonnegative_int("horizon", horizon)
    values = tuple(remainders)
    signature = []
    for remainder in values:
        _require_int("remainder", remainder)
        if not 0 <= remainder < amplitude:
            raise ValueError("remainders must lie in 0..amplitude-1")
        distance = local_first_delivery_distance(
            remainder,
            amplitude,
        )
        signature.append(
            distance if distance <= horizon else horizon + 1
        )
    return tuple(signature)


def all_truncated_remainder_signatures(
    contact_count: int,
    amplitude: int,
    horizon: int,
) -> tuple[Vector, ...]:
    """Enumerate exact finite-horizon signatures for regression/inspection."""
    _require_positive_int("contact_count", contact_count)
    _require_positive_int("amplitude", amplitude)
    _require_nonnegative_int("horizon", horizon)
    return tuple(
        sorted(
            {
                truncated_carry_signature(
                    remainders,
                    amplitude,
                    horizon,
                )
                for remainders in product(
                    range(amplitude),
                    repeat=contact_count,
                )
            }
        )
    )
