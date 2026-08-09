"""Finite drift tradeoff between Barlow slice volume and geodesic witnesses.

For fixed shell radius n and target height q<n, the shell-slice vertex count is
independent of absolute prefix drift d, but two other observables move in
opposite directions:

- the filled radius-n ball slice loses d+1 vertices when d -> d+2;
- the total number of shortest paths ending on that shell layer strictly grows.

The extreme layer q=n is a sharp boundary: its total vertical path count is
always 3^n, independent of drift, although endpoint distribution still varies.
"""

from __future__ import annotations

from math import comb, gcd

from .p022_barlow_layer_geometry import layer_ball_vertex_count

Rational = tuple[int, int]


def _require_state(radius: int, height: int, absolute_drift: int) -> None:
    for name, value in (
        ("radius", radius),
        ("height", height),
        ("absolute_drift", absolute_drift),
    ):
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise ValueError(f"{name} must be a non-negative integer")
    if height > radius:
        raise ValueError("height cannot exceed shell radius")
    if absolute_drift > height or (height - absolute_drift) % 2:
        raise ValueError("absolute drift is incompatible with target height")


def layer_shell_geodesic_total(
    radius: int, height: int, absolute_drift: int
) -> int:
    """Exact total shortest-path multiplicity on one target shell layer."""
    _require_state(radius, height, absolute_drift)
    if radius == 0:
        return 1
    if height == radius:
        return 3 ** radius
    paired = (height - absolute_drift) // 2
    return comb(radius, height) * (
        3
        * (2 ** (radius - height + paired))
        * (1 + 2 ** absolute_drift)
        - 6
    )


def layer_shell_vertex_count(radius: int, height: int) -> int:
    """Stacking-independent non-extreme shell-layer cardinality."""
    if any(
        isinstance(value, bool) or not isinstance(value, int) or value < 0
        for value in (radius, height)
    ):
        raise ValueError("radius and height must be non-negative integers")
    if height >= radius:
        raise ValueError("universal boundary count is for non-extreme layers")
    return 3 * (2 * radius - height)


def layer_ball_slice_count(
    radius: int, height: int, absolute_drift: int
) -> int:
    """Filled radius-n slice cardinality at one unsigned target height."""
    _require_state(radius, height, absolute_drift)
    return layer_ball_vertex_count(radius, height, absolute_drift)


def next_drift_vertex_loss(
    radius: int, height: int, absolute_drift: int
) -> int:
    """Exact ball-slice loss under the legal step ``d -> d+2``."""
    _require_state(radius, height, absolute_drift)
    if absolute_drift + 2 > height:
        raise ValueError("no larger parity-compatible drift remains")
    current = layer_ball_slice_count(radius, height, absolute_drift)
    nxt = layer_ball_slice_count(radius, height, absolute_drift + 2)
    loss = current - nxt
    if loss != absolute_drift + 1:
        raise AssertionError("quadratic slice formula must lose d+1 vertices")
    return loss


def next_drift_geodesic_gain(
    radius: int, height: int, absolute_drift: int
) -> int:
    """Exact path-total gain under ``d -> d+2`` for a non-extreme layer."""
    _require_state(radius, height, absolute_drift)
    if height >= radius:
        raise ValueError("extreme layer has drift-independent total path count")
    if absolute_drift + 2 > height:
        raise ValueError("no larger parity-compatible drift remains")
    exponent_high = (height + absolute_drift) // 2
    exponent_low = (height - absolute_drift) // 2 - 1
    gain = 3 * comb(radius, height) * (2 ** (radius - height)) * (
        2 ** exponent_high - 2 ** exponent_low
    )
    direct = layer_shell_geodesic_total(
        radius, height, absolute_drift + 2
    ) - layer_shell_geodesic_total(radius, height, absolute_drift)
    if gain != direct or gain <= 0:
        raise AssertionError("closed geodesic gain must match direct difference")
    return gain


def average_shell_multiplicity(
    radius: int, height: int, absolute_drift: int
) -> Rational:
    """Reduced average number of shortest paths per shell-layer vertex."""
    _require_state(radius, height, absolute_drift)
    if height >= radius:
        # Extreme shell layer cardinality is drift-sensitive; defer to the exact
        # filled slice count rather than the universal boundary formula.
        vertices = layer_ball_slice_count(radius, height, absolute_drift)
    else:
        vertices = layer_shell_vertex_count(radius, height)
    paths = layer_shell_geodesic_total(radius, height, absolute_drift)
    divisor = gcd(paths, vertices)
    return paths // divisor, vertices // divisor
