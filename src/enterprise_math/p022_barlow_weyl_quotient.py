"""B2/C2 reflection-chamber interpretation of Barlow coordination history.

A labelled two-sided signed drift state is ``(x,y) in Z^2``.  The finite signed
permutation group acts by independent sign flips and coordinate exchange.  Its
canonical orbit representative is ``sort(abs(x),abs(y))``, exactly the
coordination-history state used by P022.

The chamber walls have distinct repair semantics:

- coordinate wall ``a=0``: a sign reflection fixes the coarse state and one
  orientation bit is born when the labelled path leaves zero;
- diagonal wall ``a=b``: coordinate exchange fixes the coarse state and one
  side-label bit is born when the labelled path splits.

Thus microscopic word-pair fibers are path-lift multiplicities of the orbit
quotient, with one binary branch for each symmetry-breaking wall exit.
"""

from __future__ import annotations

from itertools import product

from .p022_barlow_two_sided_repair import (
    diagonal_split_count,
    total_zero_departure_events,
    two_sided_microscopic_fiber_size,
)

LabelledState = tuple[int, int]
ChamberState = tuple[int, int]
LabelledPath = tuple[LabelledState, ...]
ChamberPath = tuple[ChamberState, ...]


def canonical_b2_orbit_representative(state: LabelledState) -> ChamberState:
    """Canonical representative ``0<=a<=b`` of the signed-permutation orbit."""
    if (
        not isinstance(state, tuple)
        or len(state) != 2
        or any(isinstance(value, bool) or not isinstance(value, int) for value in state)
    ):
        raise ValueError("state must be an integer pair")
    return tuple(sorted((abs(state[0]), abs(state[1]))))


def b2_orbit(state: LabelledState) -> tuple[LabelledState, ...]:
    """Complete signed-permutation orbit of one integer pair."""
    x, y = state
    values = {
        (sx * left, sy * right)
        for left, right in ((x, y), (y, x))
        for sx, sy in product((-1, 1), repeat=2)
    }
    return tuple(sorted(values))


def b2_orbit_size_from_chamber(state: ChamberState) -> int:
    """Orbit size from chamber-wall stabilizers.

    - origin: 1;
    - coordinate wall ``(0,b)``, b>0: 4;
    - diagonal wall ``(a,a)``, a>0: 4;
    - interior ``0<a<b``: 8.
    """
    a, b = state
    if a < 0 or b < a:
        raise ValueError("state must satisfy 0<=a<=b")
    if a == b == 0:
        return 1
    if a == 0 or a == b:
        return 4
    return 8


def labelled_prefix_path(
    left_word: tuple[int, ...], right_word: tuple[int, ...]
) -> LabelledPath:
    """Signed prefix-drift path from two equal-length +/-1 words."""
    if len(left_word) != len(right_word):
        raise ValueError("word lengths must agree")
    if any(sign not in (-1, 1) for sign in left_word + right_word):
        raise ValueError("words must contain only -1/+1 signs")
    left = 0
    right = 0
    path = []
    for left_step, right_step in zip(left_word, right_word, strict=True):
        left += left_step
        right += right_step
        path.append((left, right))
    return tuple(path)


def chamber_path_from_labelled(path: LabelledPath) -> ChamberPath:
    """Apply the B2 orbit quotient at every time label."""
    return tuple(canonical_b2_orbit_representative(state) for state in path)


def path_wall_event_counts(path: ChamberPath) -> tuple[int, int]:
    """Return ``(coordinate-wall exits, diagonal-wall splits)``.

    These are exactly the existing P022 counts ``E`` and ``B``.  The initial
    pre-state is the chamber origin ``(0,0)``.
    """
    if not isinstance(path, tuple):
        raise ValueError("path must be a tuple")
    previous = (0, 0)
    coordinate_events = 0
    diagonal_events = 0
    for current in path:
        if (
            not isinstance(current, tuple)
            or len(current) != 2
            or current[0] < 0
            or current[1] < current[0]
        ):
            raise ValueError("path states must lie in 0<=a<=b")
        # One sign label per zero coordinate of the previous coarse state.
        coordinate_events += int(previous[0] == 0) + int(previous[1] == 0)
        # One exchange label only if a diagonal fixed state actually splits.
        diagonal_events += int(
            previous[0] == previous[1] and current[0] != current[1]
        )
        previous = current
    return coordinate_events, diagonal_events


def quotient_path_lift_count(path: ChamberPath) -> int:
    """Exact number of labelled microscopic path lifts of one chamber path."""
    coordinate_events, diagonal_events = path_wall_event_counts(path)
    return 2 ** (coordinate_events + diagonal_events)


def compare_with_existing_repair_theorem(path: ChamberPath) -> tuple[int, int]:
    """Cross-check the Weyl-wall count with the existing event-repair theorem."""
    coordinate_events, diagonal_events = path_wall_event_counts(path)
    existing_e = total_zero_departure_events(path)
    existing_b = diagonal_split_count(path)
    if (coordinate_events, diagonal_events) != (existing_e, existing_b):
        raise AssertionError("Weyl-wall events must equal existing E/B repair events")
    lift_count = 2 ** (coordinate_events + diagonal_events)
    existing_fiber = two_sided_microscopic_fiber_size(path)
    if lift_count != existing_fiber:
        raise AssertionError("orbit-path lift count must equal microscopic fiber size")
    return lift_count, existing_fiber
