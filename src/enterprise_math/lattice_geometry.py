"""Integer-only lattice-geometry tools for Enterprise Math research.

The reference model uses the A_p root lattice in its standard zero-sum
integer-coordinate representation. No floating-point values or true division
are used in this module.
"""

from __future__ import annotations

from math import comb, isqrt

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


def _charge_square_counts(coordinate_count: int, max_square_sum: int) -> dict[tuple[int, int], int]:
    """Finite coordinate-kernel convolution for charge and square-sum counts."""
    _require_positive("coordinate_count", coordinate_count)
    _require_natural("max_square_sum", max_square_sum)

    counts: dict[tuple[int, int], int] = {(0, 0): 1}
    for _ in range(coordinate_count):
        next_counts: dict[tuple[int, int], int] = {}
        for (charge, square_sum), multiplicity in counts.items():
            bound = isqrt(max_square_sum - square_sum)
            for coordinate in range(-bound, bound + 1):
                key = (charge + coordinate, square_sum + coordinate * coordinate)
                next_counts[key] = next_counts.get(key, 0) + multiplicity
        counts = next_counts
    return counts


def a_quadratic_shell_counts(p: int, max_q: int) -> tuple[int, ...]:
    """Return exact counts for q=0..max_q in A_p by repeated finite integer convolution.

    A_p is represented by p+1 integer coordinates whose total charge is zero.
    The dimension lift p -> p+1 is one more application of the same one-coordinate
    kernel; no real series or limiting process is used.
    """
    _require_positive("p", p)
    _require_natural("max_q", max_q)
    counts = _charge_square_counts(p + 1, 2 * max_q)
    return tuple(counts.get((0, 2 * q), 0) for q in range(max_q + 1))


def a_quadratic_shell_count(p: int, q: int) -> int:
    """Number of A_p displacements with integer quadratic separation exactly q."""
    _require_positive("p", p)
    _require_natural("q", q)
    return a_quadratic_shell_counts(p, q)[q]


def a_precision_distance_shell_count(p: int, distance: int) -> int:
    """Count A_p displacements whose collapsed radial distance is exactly distance."""
    _require_positive("p", p)
    _require_natural("distance", distance)
    lower_q = distance * distance
    upper_q = (distance + 1) * (distance + 1) - 1
    counts = a_quadratic_shell_counts(p, upper_q)
    return sum(counts[lower_q : upper_q + 1])


def a_precision_distance_ball_count(p: int, distance: int) -> int:
    """Count A_p displacements whose collapsed radial distance is at most distance."""
    _require_positive("p", p)
    _require_natural("distance", distance)
    upper_q = (distance + 1) * (distance + 1) - 1
    return sum(a_quadratic_shell_counts(p, upper_q))
