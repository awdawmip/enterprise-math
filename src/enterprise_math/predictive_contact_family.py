"""Symmetric integer action-family predictive quotient for E001 Boolean contact.

For contact predicate ``gap < d`` and a finite nonempty family of positive action
magnitudes ``a_j``, suppose the world engine permits both ``+a_j`` separation
and lower-clipped ``-a_j`` closing.  Let ``g = gcd(a_j)``.  The entire action
family factors through the single signed coordinate

    K(gap) = ceil((d-gap)/g).

Every +a_j shifts K down by ``a_j/g``.  Every clipped -a_j shifts K up by the
same integer and caps at ``ceil(d/g)``, the K-value of gap zero.  The coordinate
is also behaviorally minimal for Boolean CONTACT/SEPARATE under arbitrary finite
words because the symmetric normalized action family generates all integer
translations (Bezout), after moving sufficiently far into the separated region
to avoid the lower-gap clipping cap during a distinguishing word.

This is a collision/contact specialization of E002/P023 gcd-safe predictive
state.  It is not a complete collision or rebound state.
"""

from __future__ import annotations

from functools import reduce
from math import gcd
from typing import Iterable


def _require_int(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise TypeError(f"{name} must be an integer")


def _require_positive(name: str, value: int) -> None:
    _require_int(name, value)
    if value <= 0:
        raise ValueError(f"{name} must be positive")


def _require_nonnegative(name: str, value: int) -> None:
    _require_int(name, value)
    if value < 0:
        raise ValueError(f"{name} must be nonnegative")


def normalize_magnitudes(magnitudes: Iterable[int]) -> tuple[int, ...]:
    values = tuple(magnitudes)
    if not values:
        raise ValueError("at least one action magnitude is required")
    for value in values:
        _require_positive("action magnitude", value)
    return values


def action_family_gcd(magnitudes: Iterable[int]) -> int:
    """Positive gcd of one nonempty action-magnitude family."""
    values = normalize_magnitudes(magnitudes)
    return reduce(gcd, values)


def family_contact_coordinate(
    gap: int,
    precision: int,
    magnitudes: Iterable[int],
) -> int:
    """Signed gcd-step coordinate ``ceil((d-gap)/g)``."""
    _require_nonnegative("gap", gap)
    _require_positive("precision", precision)
    step = action_family_gcd(magnitudes)
    # ceil((d-gap)/step) == -floor((gap-d)/step), exact on signed integers.
    return -((gap - precision) // step)


def family_contact_from_coordinate(coordinate: int) -> bool:
    """Boolean contact observation factors as ``K>=1``."""
    _require_int("coordinate", coordinate)
    return coordinate >= 1


def coordinate_cap(precision: int, magnitudes: Iterable[int]) -> int:
    """Largest K-value, attained by the ground-clipped gap zero state."""
    _require_positive("precision", precision)
    step = action_family_gcd(magnitudes)
    return (precision + step - 1) // step


def separate_coordinate(
    coordinate: int,
    magnitude: int,
    magnitudes: Iterable[int],
) -> int:
    """Exact K-update under ``gap -> gap + magnitude``."""
    _require_int("coordinate", coordinate)
    _require_positive("magnitude", magnitude)
    values = normalize_magnitudes(magnitudes)
    if magnitude not in values:
        raise ValueError("magnitude must belong to the declared action family")
    step = action_family_gcd(values)
    return coordinate - magnitude // step


def close_coordinate(
    coordinate: int,
    precision: int,
    magnitude: int,
    magnitudes: Iterable[int],
) -> int:
    """Exact K-update under ``gap -> max(0, gap - magnitude)``."""
    _require_int("coordinate", coordinate)
    _require_positive("precision", precision)
    _require_positive("magnitude", magnitude)
    values = normalize_magnitudes(magnitudes)
    if magnitude not in values:
        raise ValueError("magnitude must belong to the declared action family")
    step = action_family_gcd(values)
    return min(coordinate + magnitude // step, coordinate_cap(precision, values))


def apply_gap_action(gap: int, signed_action: int) -> int:
    """Physical gap action: positive separates, negative closes with lower clip."""
    _require_nonnegative("gap", gap)
    _require_int("signed_action", signed_action)
    return max(0, gap + signed_action)


def apply_coordinate_action(
    coordinate: int,
    precision: int,
    signed_action: int,
    magnitudes: Iterable[int],
) -> int:
    """Apply one declared signed action directly to K."""
    _require_int("signed_action", signed_action)
    if signed_action == 0:
        raise ValueError("signed_action must be nonzero")
    values = normalize_magnitudes(magnitudes)
    magnitude = abs(signed_action)
    if magnitude not in values:
        raise ValueError("action magnitude must belong to declared family")
    if signed_action > 0:
        return separate_coordinate(coordinate, magnitude, values)
    return close_coordinate(coordinate, precision, magnitude, values)


def family_future_signature(
    gap: int,
    precision: int,
    word: Iterable[int],
) -> tuple[bool, ...]:
    """Boolean contact signature including current sample and every word prefix."""
    _require_nonnegative("gap", gap)
    _require_positive("precision", precision)
    current = gap
    signature = [current < precision]
    for action in word:
        _require_int("signed action", action)
        if action == 0:
            raise ValueError("actions must be nonzero")
        current = apply_gap_action(current, action)
        signature.append(current < precision)
    return tuple(signature)


def coordinate_future_signature(
    coordinate: int,
    precision: int,
    magnitudes: Iterable[int],
    word: Iterable[int],
) -> tuple[bool, ...]:
    """Same Boolean future generated entirely in quotient coordinate K."""
    values = normalize_magnitudes(magnitudes)
    current = coordinate
    signature = [family_contact_from_coordinate(current)]
    for action in word:
        current = apply_coordinate_action(current, precision, action, values)
        signature.append(family_contact_from_coordinate(current))
    return tuple(signature)


def family_fiber_bounds(
    coordinate: int,
    precision: int,
    magnitudes: Iterable[int],
) -> tuple[int, int]:
    """Inclusive nonnegative gap interval represented by one K-value.

    Before clipping to ``gap>=0``, K=k means

        d-k*g <= gap <= d-(k-1)*g-1.

    The returned fiber is intersected with nonnegative gaps.  Very large K above
    the cap has no physical fiber and is rejected.
    """
    _require_int("coordinate", coordinate)
    _require_positive("precision", precision)
    values = normalize_magnitudes(magnitudes)
    step = action_family_gcd(values)
    cap = coordinate_cap(precision, values)
    if coordinate > cap:
        raise ValueError("coordinate lies above the physical gap-zero cap")
    lower = max(0, precision - coordinate * step)
    upper = precision - (coordinate - 1) * step - 1
    if upper < lower:
        raise ValueError("coordinate has no nonnegative physical gap fiber")
    return lower, upper


def family_fiber_size(
    coordinate: int,
    precision: int,
    magnitudes: Iterable[int],
) -> int:
    lower, upper = family_fiber_bounds(coordinate, precision, magnitudes)
    return upper - lower + 1
