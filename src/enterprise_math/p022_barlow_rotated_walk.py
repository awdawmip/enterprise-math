"""Rotate two Barlow signed drifts into a standard Z^2 cardinal walk.

If S,T are the two signed prefix drifts, define U=(S+T)/2 and V=(S-T)/2.
Each microscopic pair of signs changes exactly one of U,V by one, so (U,V) is
a standard nearest-neighbor walk on Z^2.  Barlow repair events become B2 wall
visits/departures in these coordinates.
"""

from __future__ import annotations

from .p022_barlow_excursion_repair import StackingWord

RotatedState = tuple[int, int]
RotatedPath = tuple[RotatedState, ...]


def rotated_walk(left_word: StackingWord, right_word: StackingWord) -> RotatedPath:
    if len(left_word) != len(right_word):
        raise ValueError("two-sided words must have equal length")
    s = 0
    t = 0
    output: list[RotatedState] = []
    for left, right in zip(left_word, right_word, strict=True):
        if left not in (-1, 1) or right not in (-1, 1):
            raise ValueError("stacking signs must be ±1")
        s += left
        t += right
        if (s + t) % 2 or (s - t) % 2:
            raise AssertionError("rotated coordinates must remain integral")
        output.append(((s + t) // 2, (s - t) // 2))
    return tuple(output)


def is_cardinal_walk(path: RotatedPath) -> bool:
    previous = (0, 0)
    for current in path:
        du = current[0] - previous[0]
        dv = current[1] - previous[1]
        if (abs(du), abs(dv)) not in ((1, 0), (0, 1)):
            return False
        previous = current
    return True


def diagonal_wall_membership_count_before_steps(path: RotatedPath) -> int:
    """Multiplicity-weighted visits to U=V and U=-V before each next step."""
    total = 0
    previous = (0, 0)
    for _current in path:
        u, v = previous
        total += int(u == v) + int(u == -v)
        previous = _current
    return total


def coordinate_wall_departure_count(path: RotatedPath) -> int:
    """Departures from the coordinate-axis union, excluding the origin overlap.

    At an axis point away from the origin, a cardinal next step either stays on
    the same axis or leaves it.  Count exactly the latter transitions.
    """
    total = 0
    previous = (0, 0)
    for current in path:
        u, v = previous
        on_exactly_one_axis = (u == 0) ^ (v == 0)
        if on_exactly_one_axis and current[0] != 0 and current[1] != 0:
            total += 1
        previous = current
    return total


def b2_wall_repair_count(path: RotatedPath) -> int:
    return diagonal_wall_membership_count_before_steps(path) + coordinate_wall_departure_count(path)
