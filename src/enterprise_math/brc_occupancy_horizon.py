"""Finite-horizon six-axis occupancy observer for Heartbeat World.

This is a T0/T6 domain operator, not a new BRC family. Six Boolean bits record
whether the six positive native-axis neighbor channels are occupied. A scan
heartbeat visits one axis per tick in cyclic order. The reference use-once
update marks the current channel occupied, then rotates the frame.

The tool compiles exact finite-horizon observation keys. It does not model a
many-body lattice gas, negative-axis occupancy, payload semantics, or physical
exclusion. Time/phase remains separately typed in Heartbeat World.
"""
from __future__ import annotations
from dataclasses import dataclass

AXES = 6


def _bit(value: int) -> int:
    if type(value) is not int or value not in (0, 1):
        raise ValueError("occupancy bits must be integer 0/1")
    return value


def occupancy(bits) -> tuple[int, ...]:
    result = tuple(_bit(v) for v in bits)
    if len(result) != AXES:
        raise ValueError("Heartbeat World occupancy state requires six positive-axis bits")
    return result


def count(bits) -> int:
    return sum(occupancy(bits))


def rotate(bits, steps=1) -> tuple[int, ...]:
    bits = occupancy(bits)
    if type(steps) is not int:
        raise TypeError("steps must be integer")
    k = steps % AXES
    return bits[k:] + bits[:k]


def use_once_tick(bits) -> tuple[int, ...]:
    """Mark active +E1 occupied, then advance one heartbeat phase."""
    bits = occupancy(bits)
    return rotate((1,) + bits[1:], 1)


def static_tick(bits) -> tuple[int, ...]:
    """Pure phase advance with no material occupancy change."""
    return rotate(bits, 1)


def count_future_key(bits, horizon: int, *, mutating=True) -> tuple[int, ...]:
    bits = occupancy(bits)
    if type(horizon) is not int or horizon < 0:
        raise ValueError("horizon must be nonnegative integer")
    step = use_once_tick if mutating else static_tick
    values = [count(bits)]
    for _ in range(horizon):
        bits = step(bits)
        values.append(count(bits))
    return tuple(values)


def active_bit_future_key(bits, horizon: int) -> tuple[int, ...]:
    bits = occupancy(bits)
    if type(horizon) is not int or horizon < 0:
        raise ValueError("horizon must be nonnegative integer")
    return tuple(bits[i % AXES] for i in range(horizon + 1))


def mutating_count_class_count(horizon: int) -> int:
    """Exact classes for use-once updates observed only by total occupancy count.

    For 0<=h<=5: 2^h*(7-h). From h>=5 all 64 masks are distinguished.
    """
    if type(horizon) is not int or horizon < 0:
        raise ValueError("horizon must be nonnegative integer")
    if horizon >= AXES - 1:
        return 2**AXES
    return (2**horizon) * (AXES - horizon + 1)


def static_active_bit_class_count(horizon: int) -> int:
    if type(horizon) is not int or horizon < 0:
        raise ValueError("horizon must be nonnegative integer")
    return 2**min(horizon + 1, AXES)


def cyclic_pattern(bits) -> tuple[int, ...]:
    """Canonical C6 rotation-orbit representative for a phase-free observer."""
    bits = occupancy(bits)
    return min(rotate(bits, k) for k in range(AXES))


@dataclass(frozen=True)
class OccupancyState:
    bits: tuple[int, ...]

    def __post_init__(self):
        object.__setattr__(self, "bits", occupancy(self.bits))

    @property
    def occupied_count(self) -> int:
        return count(self.bits)

    def tick(self, *, mutating=True) -> "OccupancyState":
        return OccupancyState(use_once_tick(self.bits) if mutating else static_tick(self.bits))

    def future_key(self, horizon: int, *, mutating=True) -> tuple[int, ...]:
        return count_future_key(self.bits, horizon, mutating=mutating)
