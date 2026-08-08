"""Integer-only lattice-geometry tools for Enterprise Math research.

The reference model uses the A_p root lattice in its standard zero-sum
integer-coordinate representation. No floating-point values or true division
are used in this module.
"""

from __future__ import annotations

from math import comb

from .core import integer_nth_root


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_a_point(name: str, point: tuple[int, ...]) -> None:
    if not isinstance(point, tuple) or len(point) < 2:
        raise ValueError(f"{name} must be a tuple with at least two coordinates")
    if any(isinstance(x, bool) or not isinstance(x, int) for x in point):
        raise ValueError(f"{name} coordinates must be integers")
    if sum(point) != 0:
        raise ValueError(f"{name} must lie in an A_p zero-sum lattice")


def _require_same_a_lattice(x: tuple[int, ...], y: tuple[int, ...]) -> None:
    _require_a_point("x", x)
    _require_a_point("y", y)
    if len(x) != len(y):
        raise ValueError("x and y must have the same dimension")


def a_graph_distance(x: tuple[int, ...], y: tuple[int, ...]) -> int:
    """Word distance for primitive A_p roots e_i-e_j."""
    _require_same_a_lattice(x, y)
    delta = tuple(a - b for a, b in zip(x, y))
    return sum(value for value in delta if value > 0)


def a_quadratic_separation(x: tuple[int, ...], y: tuple[int, ...]) -> int:
    """Return q=(1/2) sum_i (x_i-y_i)^2, which is integral on A_p."""
    _require_same_a_lattice(x, y)
    square_sum = sum((a - b) ** 2 for a, b in zip(x, y))
    if square_sum % 2 != 0:
        raise AssertionError("zero-sum integer differences must have even square sum")
    return square_sum // 2


def a_collapsed_radial_distance(x: tuple[int, ...], y: tuple[int, ...]) -> int:
    """Integer-root collapse of the A_p quadratic separation."""
    return integer_nth_root(a_quadratic_separation(x, y), 2)


def a_triangle_carry(
    x: tuple[int, ...], y: tuple[int, ...], z: tuple[int, ...]
) -> int:
    """Positive triangle defect of collapsed radial distance.

    P019 proves that this value is always 0 or 1.
    """
    direct = a_collapsed_radial_distance(x, z)
    via = a_collapsed_radial_distance(x, y) + a_collapsed_radial_distance(y, z)
    return max(0, direct - via)


def a_coordinator_shell_count(p: int, radius: int) -> int:
    """Number of A_p points at primitive-root graph distance exactly radius."""
    _require_positive("p", p)
    _require_natural("radius", radius)
    if radius == 0:
        return 1
    return sum(
        comb(p, j) ** 2 * comb(radius - j + p - 1, p - 1)
        for j in range(0, min(p, radius) + 1)
    )


def a_ball_count(p: int, radius: int) -> int:
    """Number of A_p points at primitive-root graph distance at most radius."""
    _require_positive("p", p)
    _require_natural("radius", radius)
    return sum(
        comb(p, j) ** 2 * comb(radius - j + p, p)
        for j in range(0, min(p, radius) + 1)
    )


def a_ball_root(n: int, p: int) -> int:
    """Greatest graph radius whose A_p ball contains at most n states.

    n=0 is treated as the empty state and returns radius 0 by convention.
    """
    _require_natural("n", n)
    _require_positive("p", p)
    if n == 0:
        return 0
    lo = 0
    hi = 1
    while a_ball_count(p, hi) <= n:
        hi *= 2
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if a_ball_count(p, mid) <= n:
            lo = mid
        else:
            hi = mid
    return lo


def a_ball_collapse(n: int, p: int) -> int:
    """Collapse n to the greatest complete A_p graph-ball cardinality not exceeding n."""
    _require_natural("n", n)
    _require_positive("p", p)
    if n == 0:
        return 0
    return a_ball_count(p, a_ball_root(n, p))


def a_first_precision_shell_count(p: int) -> int:
    """Count nonzero A_p displacements with R_2(q)=1, equivalently 1<=q<=3."""
    _require_positive("p", p)
    n = p + 1
    q1 = p * (p + 1)
    q2 = 6 * comb(n, 4)
    q3 = 6 * comb(n, 3) + 20 * comb(n, 6)
    return q1 + q2 + q3
