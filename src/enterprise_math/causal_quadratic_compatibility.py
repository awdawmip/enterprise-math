"""Quadratic integer-potential compatibility of unit-amplitude causal events.

For an integer slot state define the formal quadratic relation value

    Q(x)=1/2 * sum_i x_i^2

on sectors where it is integral.  A unit-amplitude event delta_i in {-1,0,+1}
changes Q by

    Q(x+delta)-Q(x)=sum_i x_i*delta_i + support(delta)/2.

Therefore the increment is integral for every integer x iff the event support is
even.  Since sum x_i^2 == sum x_i mod 2, Q itself is integral exactly on even-
total sectors.

Consequences for modular conservation grammars:
* exact total-conserving transfers have support two and preserve the integer Q
  channel from the zero-total sector;
* parity/D events have support two and preserve even-total Q integrality;
* the higher irreducible mod-m creation/annihilation event has support m, so it
  is Q-compatible iff m is even.

Thus identical low-order A-type primitive geometry may differ in whether the
quadratic P019 observation remains an exact integer channel under higher events.
"""

from __future__ import annotations

from .causal_irreducible_modular_events import (
    irreducible_modular_events,
    support_size,
)

Vector = tuple[int, ...]


def doubled_quadratic_value(state: Vector) -> int:
    return sum(value * value for value in state)


def quadratic_value_if_integer(state: Vector) -> int | None:
    doubled = doubled_quadratic_value(state)
    return doubled // 2 if doubled % 2 == 0 else None


def quadratic_integrality_matches_total_parity(state: Vector) -> bool:
    return (doubled_quadratic_value(state) % 2) == (sum(state) % 2)


def quadratic_increment_doubled(state: Vector, event: Vector) -> int:
    if len(state) != len(event):
        raise ValueError("state and event must have equal length")
    return 2 * sum(x * delta for x, delta in zip(state, event)) + support_size(event)


def quadratic_increment_is_integer_for_all_states(event: Vector) -> bool:
    return support_size(event) % 2 == 0


def quadratic_increment_if_integer(state: Vector, event: Vector) -> int | None:
    doubled = quadratic_increment_doubled(state, event)
    return doubled // 2 if doubled % 2 == 0 else None


def modular_irreducibles_all_quadratic_compatible(slot_count: int, modulus: int) -> bool:
    return all(
        quadratic_increment_is_integer_for_all_states(event)
        for event in irreducible_modular_events(slot_count, modulus)
    )


def higher_modular_channel_is_quadratic_compatible(modulus: int) -> bool:
    if isinstance(modulus, bool) or not isinstance(modulus, int) or modulus < 3:
        raise ValueError("higher modular channel theorem is stated for modulus >=3")
    return modulus % 2 == 0
