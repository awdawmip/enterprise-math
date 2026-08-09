"""Close-packed layer stacking as a two-state causal continuation system.

Layer registries live in Z/3Z and adjacent close-packed layers cannot use the
same registry.  The relative step delta_n=s_(n+1)-s_n is therefore +1 or -1 mod
3.  Given two consecutive layers, the next layer has exactly two close-packed
choices:

F: continue to the third registry, preserving delta;
H: return to the registry used two layers earlier, flipping delta.

Thus F acts as identity on the two continuation types and H as sign flip.  With
fixed first two registries, every F/H word bijects with one admissible close-
packed stacking sequence.  Repeated F gives ABCABC... (FCC stacking), repeated H
gives ABAB... (HCP stacking).

This support law does not assert that FCC and HCP have identical higher-order
local relation contexts; those are separate observables.  In particular common-
neighbor analysis distinguishes their nearest-neighbor bond environments.
"""

from __future__ import annotations


def _require_registry(value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value not in (0, 1, 2):
        raise ValueError("registry must be 0,1,2")


def relative_step(left: int, right: int) -> int:
    _require_registry(left)
    _require_registry(right)
    residue = (right - left) % 3
    if residue == 1:
        return 1
    if residue == 2:
        return -1
    raise ValueError("adjacent close-packed layers cannot use the same registry")


def next_delta(delta: int, action: str) -> int:
    if delta not in (-1, 1):
        raise ValueError("delta must be +1 or -1")
    if action == "F":
        return delta
    if action == "H":
        return -delta
    raise ValueError("action must be F or H")


def next_registry(previous: int, current: int, action: str) -> int:
    delta = relative_step(previous, current)
    nxt_delta = next_delta(delta, action)
    return (current + nxt_delta) % 3


def stacking_from_actions(
    first: int,
    second: int,
    actions: tuple[str, ...],
) -> tuple[int, ...]:
    _require_registry(first)
    _require_registry(second)
    relative_step(first, second)
    layers = [first, second]
    for action in actions:
        layers.append(next_registry(layers[-2], layers[-1], action))
    return tuple(layers)


def actions_from_stacking(layers: tuple[int, ...]) -> tuple[str, ...]:
    if not isinstance(layers, tuple) or len(layers) < 2:
        raise ValueError("stacking must contain at least two layers")
    for registry in layers:
        _require_registry(registry)
    deltas = tuple(relative_step(left, right) for left, right in zip(layers, layers[1:]))
    actions = []
    for previous, current in zip(deltas, deltas[1:]):
        actions.append("F" if current == previous else "H")
    return tuple(actions)


def stacking_bijection_check(
    first: int,
    second: int,
    actions: tuple[str, ...],
) -> bool:
    layers = stacking_from_actions(first, second, actions)
    return actions_from_stacking(layers) == actions


def fcc_stacking(layer_count: int) -> tuple[int, ...]:
    if isinstance(layer_count, bool) or not isinstance(layer_count, int) or layer_count < 2:
        raise ValueError("layer_count must be at least two")
    return stacking_from_actions(0, 1, ("F",) * (layer_count - 2))


def hcp_stacking(layer_count: int) -> tuple[int, ...]:
    if isinstance(layer_count, bool) or not isinstance(layer_count, int) or layer_count < 2:
        raise ValueError("layer_count must be at least two")
    return stacking_from_actions(0, 1, ("H",) * (layer_count - 2))


def global_registry_shift(layers: tuple[int, ...], shift: int) -> tuple[int, ...]:
    if isinstance(shift, bool) or not isinstance(shift, int):
        raise ValueError("shift must be an integer")
    return tuple((registry + shift) % 3 for registry in layers)


def relative_steps(layers: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(relative_step(left, right) for left, right in zip(layers, layers[1:]))


def global_shift_preserves_continuation(layers: tuple[int, ...], shift: int) -> bool:
    shifted = global_registry_shift(layers, shift)
    return relative_steps(shifted) == relative_steps(layers)


def fixed_initial_stacking_count(layer_count: int) -> int:
    """Number of admissible stackings with fixed first two distinct registries."""
    if isinstance(layer_count, bool) or not isinstance(layer_count, int) or layer_count < 2:
        raise ValueError("layer_count must be at least two")
    return 2 ** (layer_count - 2)
