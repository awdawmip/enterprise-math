"""Explicit integer distance gauge for arbitrary Barlow target layers.

For target layer k, let q=|k| and let delta be the signed effective prefix
imbalance of the mandatory vertical interfaces. Put

    d = |delta|,
    c = (q-d)/2.

The vertical endpoint support is ``H_c + Delta_d^epsilon`` where ``H_c`` is the
triangular hex-ball and ``epsilon=sign(delta)``.  More generally

    H_s + Delta_d^+
      = {(x,y): -s <= x,y,x+y <= s+d},

with the negative orientation obtained by reflection.  The minimum expanded
hex radius required by a coordinate (x,y) therefore has a six-affine maximum
formula, yielding the exact native graph distance without BFS.
"""

from __future__ import annotations

from .p022_barlow_stacking import StackingPattern, stacking_prefix_imbalance


def _require_integer(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")


def _require_layer_imbalance(target_layer: int, imbalance: int) -> None:
    _require_integer("target_layer", target_layer)
    _require_integer("imbalance", imbalance)
    vertical = abs(target_layer)
    if abs(imbalance) > vertical or (vertical - imbalance) % 2:
        raise ValueError("imbalance is incompatible with target-layer length")


def drift_orientation(imbalance: int) -> int:
    """Use +1 for zero/positive drift and -1 for negative drift."""
    _require_integer("imbalance", imbalance)
    return -1 if imbalance < 0 else 1


def drifted_hex_required_radius(x: int, y: int, imbalance: int) -> int:
    """Smallest s>=0 with ``(x,y) in H_s+Delta_|delta|^sign``.

    With ``epsilon=sign(delta)`` and ``d=|delta|``, the plus-oriented set is

        -s <= epsilon*x, epsilon*y, epsilon*(x+y) <= s+d.

    Solving these six inequalities for the least non-negative integer s gives
    the returned affine maximum.
    """
    _require_integer("x", x)
    _require_integer("y", y)
    _require_integer("imbalance", imbalance)
    epsilon = drift_orientation(imbalance)
    drift = abs(imbalance)
    ex = epsilon * x
    ey = epsilon * y
    es = epsilon * (x + y)
    return max(
        0,
        -ex,
        -ey,
        -es,
        ex - drift,
        ey - drift,
        es - drift,
    )


def barlow_endpoint_distance_from_imbalance(
    x: int, y: int, target_layer: int, imbalance: int
) -> int:
    """Exact native graph distance from the root to ``(x,y,target_layer)``."""
    _require_integer("x", x)
    _require_integer("y", y)
    _require_layer_imbalance(target_layer, imbalance)
    vertical = abs(target_layer)
    drift = abs(imbalance)
    paired = (vertical - drift) // 2
    required = drifted_hex_required_radius(x, y, imbalance)
    extra_horizontal = max(0, required - paired)
    return vertical + extra_horizontal


def barlow_endpoint_distance(
    x: int, y: int, target_layer: int, pattern: StackingPattern
) -> int:
    """Exact distance using only the selected layer's prefix imbalance."""
    imbalance = stacking_prefix_imbalance(pattern, target_layer)
    return barlow_endpoint_distance_from_imbalance(
        x, y, target_layer, imbalance
    )


def barlow_layer_ball_contains_from_imbalance(
    radius: int,
    x: int,
    y: int,
    target_layer: int,
    imbalance: int,
) -> bool:
    """Coordinate-sensitive membership in the rooted radius ball."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    return (
        barlow_endpoint_distance_from_imbalance(x, y, target_layer, imbalance)
        <= radius
    )


def barlow_layer_shell_contains_from_imbalance(
    radius: int,
    x: int,
    y: int,
    target_layer: int,
    imbalance: int,
) -> bool:
    """Coordinate-sensitive membership in the exact rooted shell."""
    if isinstance(radius, bool) or not isinstance(radius, int) or radius < 0:
        raise ValueError("radius must be a non-negative integer")
    return (
        barlow_endpoint_distance_from_imbalance(x, y, target_layer, imbalance)
        == radius
    )
