"""Exact drifted-hex geometry of Barlow ball and shell slices.

For shell/ball radius n and target layer k, put q=|k|, d=|delta_k| and

    short = n - (q+d)/2,
    long  = n - (q-d)/2.

For a non-extreme layer q<n, the radius-n ball slice is a lattice hexagon with
alternating side lengths ``short,long``. Its shell slice is exactly the lattice
boundary. Hence boundary cardinality depends only on ``short+long=2n-q``, while
filled-slice cardinality retains the anisotropy ``long-short=d``.
"""

from __future__ import annotations

from math import isqrt

from .p022_barlow_coordination import barlow_vertical_support_size


def _require_state(radius: int, target_layer: int, imbalance: int) -> tuple[int, int]:
    for name, value in (
        ("radius", radius),
        ("target_layer", target_layer),
        ("imbalance", imbalance),
    ):
        if isinstance(value, bool) or not isinstance(value, int):
            raise ValueError(f"{name} must be an integer")
    if radius < 0:
        raise ValueError("radius must be non-negative")
    vertical = abs(target_layer)
    if vertical > radius:
        raise ValueError("target layer lies outside the radius ball")
    drift = abs(imbalance)
    if drift > vertical or (vertical - drift) % 2:
        raise ValueError("imbalance is incompatible with target-layer length")
    return vertical, drift


def layer_hex_side_lengths(
    radius: int, target_layer: int, imbalance: int
) -> tuple[int, int]:
    """Return ``(short,long)`` alternating side lengths of the outer slice.

    At an extreme layer the short side may be zero, degenerating the hexagon to
    an oriented triangle when the prefix has full drift.
    """
    vertical, drift = _require_state(radius, target_layer, imbalance)
    short_numerator = 2 * radius - vertical - drift
    long_numerator = 2 * radius - vertical + drift
    if short_numerator % 2 or long_numerator % 2:
        raise AssertionError("Barlow parity must make layer side lengths integral")
    return short_numerator // 2, long_numerator // 2


def layer_effective_perimeter_parameter(
    radius: int, target_layer: int, imbalance: int
) -> int:
    """Return ``short+long=2*radius-|k|``."""
    short, long = layer_hex_side_lengths(radius, target_layer, imbalance)
    return short + long


def layer_ball_vertex_count(
    radius: int, target_layer: int, imbalance: int
) -> int:
    """Exact vertex count in the radius ball restricted to one target layer.

    Put ``P=2n-|k|`` and ``d=|delta_k|``. The drifted hex is
    ``H_short + Delta_d`` and has

        4*A = 3P^2 + 6P + 4 - d^2.
    """
    _, drift = _require_state(radius, target_layer, imbalance)
    perimeter = 2 * radius - abs(target_layer)
    numerator = 3 * perimeter * perimeter + 6 * perimeter + 4 - drift * drift
    if numerator % 4:
        raise AssertionError("Barlow slice count must be integral")
    return numerator // 4


def layer_shell_vertex_count(
    radius: int, target_layer: int, imbalance: int
) -> int:
    """Exact shell-slice cardinality from the ball-slice difference.

    For ``|k|<n`` this is the boundary length ``3(2n-|k|)``. For an extreme
    layer there is no radius-(n-1) slice on that layer, so the shell slice is
    the entire drifted support.
    """
    vertical, _ = _require_state(radius, target_layer, imbalance)
    current = layer_ball_vertex_count(radius, target_layer, imbalance)
    if vertical == radius:
        return current
    previous = layer_ball_vertex_count(radius - 1, target_layer, imbalance)
    return current - previous


def recover_absolute_imbalance_from_ball_slice_count(
    radius: int, target_layer: int, slice_vertex_count: int
) -> int:
    """Recover ``|delta_k|`` from the filled ball-slice cardinality."""
    if (
        isinstance(slice_vertex_count, bool)
        or not isinstance(slice_vertex_count, int)
        or slice_vertex_count <= 0
    ):
        raise ValueError("slice_vertex_count must be positive")
    vertical = abs(target_layer)
    if radius < 0 or vertical > radius:
        raise ValueError("target layer lies outside the radius ball")
    perimeter = 2 * radius - vertical
    square = 3 * perimeter * perimeter + 6 * perimeter + 4 - 4 * slice_vertex_count
    if square < 0:
        raise ValueError("slice count is incompatible with Barlow geometry")
    drift = isqrt(square)
    if drift * drift != square:
        raise ValueError("slice count does not encode an integral drift square")
    if drift > vertical or (vertical - drift) % 2:
        raise ValueError("recovered drift is incompatible with target layer")
    return drift


def layer_boundary_side_multiset(
    radius: int, target_layer: int, imbalance: int
) -> tuple[int, ...]:
    """Return the six cyclic side lengths without orientation labels."""
    short, long = layer_hex_side_lengths(radius, target_layer, imbalance)
    return (short, long, short, long, short, long)


def anisotropy_from_side_lengths(short: int, long: int) -> int:
    """Recover absolute drift from the alternating side-length gap."""
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in (short, long)
    ):
        raise ValueError("side lengths must be non-negative integers")
    if long < short:
        short, long = long, short
    return long - short
