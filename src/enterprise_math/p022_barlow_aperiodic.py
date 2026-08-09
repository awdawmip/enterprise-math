"""Finite shell formulas for arbitrary (not necessarily periodic) Barlow words.

The geometry-specific shell-total formula needs only the signed prefix
imbalance at each queried target layer.  Periodicity is not part of the finite
formula; it is required only by the stronger constant-recurrence theorem.
"""

from __future__ import annotations

from math import comb


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_sign_word(name: str, word: tuple[int, ...]) -> None:
    if not isinstance(word, tuple):
        raise ValueError(f"{name} must be a tuple")
    if any(sign not in (-1, 1) for sign in word):
        raise ValueError(f"{name} entries must be -1 or +1")


def layer_shell_total_from_imbalance(
    radius: int, target_layer: int, imbalance: int
) -> int:
    """Exact geodesic total on one target layer from its prefix imbalance.

    This is BG01 stripped of every periodic assumption.
    """
    _require_natural("radius", radius)
    if isinstance(target_layer, bool) or not isinstance(target_layer, int):
        raise ValueError("target_layer must be an integer")
    if isinstance(imbalance, bool) or not isinstance(imbalance, int):
        raise ValueError("imbalance must be an integer")
    vertical = abs(target_layer)
    if vertical > radius:
        return 0
    if abs(imbalance) > vertical or (vertical - imbalance) % 2:
        raise ValueError("imbalance is incompatible with target-layer length")
    if radius == 0:
        if target_layer != 0 or imbalance != 0:
            raise ValueError("radius zero contains only the root layer/state")
        return 1
    if vertical == radius:
        return 3 ** vertical

    drift_count = abs(imbalance)
    paired = (vertical - drift_count) // 2
    in_layer = radius - vertical
    boundary_mass = 3 * (2 ** (paired + in_layer)) * (1 + 2 ** drift_count) - 6
    return comb(radius, in_layer) * boundary_mass


def imbalance_trajectory_from_interface_windows(
    downward_upward_interface_signs: tuple[int, ...],
    upward_interface_signs: tuple[int, ...],
) -> tuple[int, ...]:
    """Return signed imbalances from negative through positive target layers.

    ``upward_interface_signs[j]`` is the sign of interface ``j -> j+1`` for
    j>=0. ``downward_upward_interface_signs[j]`` is the *upward* sign of the
    interface ``-j-1 -> -j``.  Traversing downward reverses horizontal offsets,
    so the effective downward prefix imbalance is the negative cumulative sum.

    If each window has length R, the output is ordered by target layers
    ``-R,...,-1,0,1,...,R``.
    """
    _require_sign_word("downward_upward_interface_signs", downward_upward_interface_signs)
    _require_sign_word("upward_interface_signs", upward_interface_signs)
    if len(downward_upward_interface_signs) != len(upward_interface_signs):
        raise ValueError("two-sided windows must have equal radius")
    radius = len(upward_interface_signs)

    downward = []
    cumulative = 0
    for sign in downward_upward_interface_signs:
        cumulative -= sign
        downward.append(cumulative)

    upward = []
    cumulative = 0
    for sign in upward_interface_signs:
        cumulative += sign
        upward.append(cumulative)

    return tuple(reversed(downward)) + (0,) + tuple(upward)


def shell_total_from_imbalance_trajectory(
    radius: int, imbalances: tuple[int, ...]
) -> int:
    """Exact whole-shell geodesic total from the finite imbalance trajectory."""
    _require_natural("radius", radius)
    if not isinstance(imbalances, tuple) or len(imbalances) != 2 * radius + 1:
        raise ValueError("trajectory must contain one imbalance for each layer -R..R")
    total = 0
    for offset, imbalance in enumerate(imbalances):
        layer = offset - radius
        total += layer_shell_total_from_imbalance(radius, layer, imbalance)
    return total
