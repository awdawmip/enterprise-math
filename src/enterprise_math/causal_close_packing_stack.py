"""Close-packed layer stacking as a relative causal continuation system.

Use three registry labels 0,1,2 (traditional A,B,C coordinates) only as a
reference chart.  Adjacent close-packed layers cannot repeat the same registry.
The intrinsic relative shift between consecutive layers is therefore one of two
orientations, +1 or -1 modulo 3.

Given the previous two layer registries `(a,b)` there are exactly two close-packed
choices for the next layer:

* `c` (cubic local environment): choose the third registry; the relative shift
  orientation is preserved;
* `h` (hexagonal local environment): return to the registry two layers back;
  the relative shift orientation flips.

Repeated `c` from AB gives ABCABC... (FCC/CCP stacking); repeated `h` gives
ABAB... (HCP stacking).  Arbitrary c/h words generate close-packed stacking
polytype candidates.  This module is combinatorial only; it does not claim a
physical energy-selection law between stackings.
"""

from __future__ import annotations

Registry = int
Orientation = int
Mode = str


def _require_registry(value: Registry) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value not in (0, 1, 2):
        raise ValueError("registry must be one of 0,1,2")


def relative_orientation(previous: Registry, current: Registry) -> Orientation:
    _require_registry(previous)
    _require_registry(current)
    if previous == current:
        raise ValueError("successive close-packed layers cannot use the same registry")
    step = (current - previous) % 3
    if step == 1:
        return 1
    if step == 2:
        return -1
    raise AssertionError("distinct mod-3 registries must differ by +/-1")


def next_registry(previous: Registry, current: Registry, mode: Mode) -> Registry:
    """Next close-packed layer under local cubic (`c`) or hexagonal (`h`) choice."""
    orientation = relative_orientation(previous, current)
    if mode == "c":
        # Continue the same cyclic/anticyclic displacement.
        return (current + orientation) % 3
    if mode == "h":
        # Reverse the displacement, returning to the layer-two-back registry.
        return previous
    raise ValueError("mode must be 'c' or 'h'")


def next_orientation(orientation: Orientation, mode: Mode) -> Orientation:
    if orientation not in (-1, 1):
        raise ValueError("orientation must be +/-1")
    if mode == "c":
        return orientation
    if mode == "h":
        return -orientation
    raise ValueError("mode must be 'c' or 'h'")


def stack_from_modes(
    initial: tuple[Registry, Registry],
    modes: tuple[Mode, ...],
) -> tuple[Registry, ...]:
    """Generate a close-packed registry sequence from local h/c continuation choices."""
    if not isinstance(initial, tuple) or len(initial) != 2:
        raise ValueError("initial must contain two registries")
    previous, current = initial
    relative_orientation(previous, current)
    result = [previous, current]
    for mode in modes:
        nxt = next_registry(previous, current, mode)
        result.append(nxt)
        previous, current = current, nxt
    return tuple(result)


def orientation_sequence(stack: tuple[Registry, ...]) -> tuple[Orientation, ...]:
    if not isinstance(stack, tuple) or len(stack) < 2:
        raise ValueError("stack must contain at least two layers")
    return tuple(
        relative_orientation(stack[index], stack[index + 1])
        for index in range(len(stack) - 1)
    )


def modes_from_stack(stack: tuple[Registry, ...]) -> tuple[Mode, ...]:
    """Recover the h/c local continuation word from a valid close-packed stack."""
    orientations = orientation_sequence(stack)
    return tuple(
        "c" if orientations[index + 1] == orientations[index] else "h"
        for index in range(len(orientations) - 1)
    )


def is_close_packed_registry_sequence(stack: tuple[Registry, ...]) -> bool:
    if not isinstance(stack, tuple) or not stack:
        return False
    try:
        for value in stack:
            _require_registry(value)
    except ValueError:
        return False
    return all(stack[index] != stack[index + 1] for index in range(len(stack) - 1))
