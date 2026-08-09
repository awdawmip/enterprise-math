"""Exact coordination-shell precision for arbitrary Barlow stackings.

Unlike geodesic path multiplicity, the number of vertices in a whole native
graph shell collapses almost all intermediate stacking information.  At radius
n it depends only on the squared imbalances of the two extreme layer prefixes:

    4*S_n = 42*n^2 + 8 - delta_n^2 - delta_-n^2.

The corresponding ball count depends only on the cumulative quadratic drift
energy.  These are geometry-specific task-relative precision coordinates.
"""

from __future__ import annotations

from math import gcd


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_imbalance(vertical_length: int, imbalance: int) -> None:
    _require_natural("vertical_length", vertical_length)
    if isinstance(imbalance, bool) or not isinstance(imbalance, int):
        raise ValueError("imbalance must be an integer")
    if abs(imbalance) > vertical_length or (vertical_length - imbalance) % 2:
        raise ValueError("imbalance is incompatible with vertical length")


def barlow_vertical_support_size(vertical_length: int, imbalance: int) -> int:
    """Number of endpoints reachable by the mandatory monotone vertical word.

    Put ``d=|delta|`` and ``c=(vertical_length-d)/2``.  The vertical witness
    support is the Minkowski sum of a triangular hex-ball ``H_c`` and an
    oriented discrete triangle ``Delta_d``.  Its lattice-point count is

        K(c,d) = 3c^2 + 3(d+1)c + C(d+2,2).
    """
    _require_imbalance(vertical_length, imbalance)
    drift = abs(imbalance)
    paired = (vertical_length - drift) // 2
    return (
        3 * paired * paired
        + 3 * (drift + 1) * paired
        + (drift + 1) * (drift + 2) // 2
    )


def barlow_layer_shell_vertex_count(
    radius: int, target_layer: int, imbalance: int
) -> int:
    """Exact number of radius-shell vertices on one target layer.

    For an extreme layer ``|k|=radius``, every endpoint in the mandatory
    vertical support lies on the shell, so the answer is ``K(c,d)``.

    For a non-extreme layer, adding ``t=radius-|k|>0`` triangular steps expands
    the support from ``H_c+Delta_d`` to ``H_(c+t)+Delta_d``.  Taking the
    difference of consecutive support sizes gives

        3*(2*radius-|k|),

    independent of the stacking imbalance.
    """
    _require_natural("radius", radius)
    if isinstance(target_layer, bool) or not isinstance(target_layer, int):
        raise ValueError("target_layer must be an integer")
    vertical = abs(target_layer)
    if vertical > radius:
        return 0
    _require_imbalance(vertical, imbalance)
    if radius == 0:
        return 1
    if vertical == radius:
        return barlow_vertical_support_size(vertical, imbalance)
    return 3 * (2 * radius - vertical)


def extreme_layer_vertex_count(radius: int, imbalance: int) -> int:
    """Closed extreme-layer count in terms of ``n`` and ``|delta_n|``.

        K_ext(n,d) = (3n^2 + 6n + 4 - d^2)/4.
    """
    _require_imbalance(radius, imbalance)
    numerator = 3 * radius * radius + 6 * radius + 4 - imbalance * imbalance
    if numerator % 4:
        raise AssertionError("Barlow parity must make extreme-layer count integral")
    return numerator // 4


def barlow_shell_vertex_count_from_extreme_imbalances(
    radius: int, positive_imbalance: int, negative_imbalance: int
) -> int:
    """Exact whole-shell cardinality from only the two extreme imbalances.

        4*S_n = 42n^2 + 8 - delta_n^2 - delta_-n^2.
    """
    _require_natural("radius", radius)
    _require_imbalance(radius, positive_imbalance)
    _require_imbalance(radius, negative_imbalance)
    if radius == 0:
        return 1
    numerator = (
        42 * radius * radius
        + 8
        - positive_imbalance * positive_imbalance
        - negative_imbalance * negative_imbalance
    )
    if numerator % 4:
        raise AssertionError("Barlow shell formula must be integral")
    return numerator // 4


def shell_drift_energy_from_vertex_count(radius: int, shell_vertex_count: int) -> int:
    """Invert the shell formula to recover ``delta_n^2+delta_-n^2``."""
    _require_natural("radius", radius)
    _require_natural("shell_vertex_count", shell_vertex_count)
    if radius == 0:
        if shell_vertex_count != 1:
            raise ValueError("radius-zero shell contains exactly one vertex")
        return 0
    energy = 42 * radius * radius + 8 - 4 * shell_vertex_count
    if energy < 0:
        raise ValueError("shell count is incompatible with Barlow geometry")
    return energy


def barlow_ball_vertex_count_from_cumulative_energy(
    radius: int, cumulative_drift_energy: int
) -> int:
    """Exact crystal-ball cardinality from cumulative quadratic drift energy.

    Let

        E_n = sum_{r=1}^n (delta_r^2 + delta_-r^2).

    Then

        4*B_n = 4 + 7n(n+1)(2n+1) + 8n - E_n.
    """
    _require_natural("radius", radius)
    _require_natural("cumulative_drift_energy", cumulative_drift_energy)
    numerator = (
        4
        + 7 * radius * (radius + 1) * (2 * radius + 1)
        + 8 * radius
        - cumulative_drift_energy
    )
    if numerator < 0 or numerator % 4:
        raise ValueError("cumulative energy is incompatible with Barlow ball parity")
    return numerator // 4


def cumulative_drift_energy_from_ball_vertex_count(
    radius: int, ball_vertex_count: int
) -> int:
    """Invert the crystal-ball formula."""
    _require_natural("radius", radius)
    _require_natural("ball_vertex_count", ball_vertex_count)
    energy = (
        4
        + 7 * radius * (radius + 1) * (2 * radius + 1)
        + 8 * radius
        - 4 * ball_vertex_count
    )
    if energy < 0:
        raise ValueError("ball count is incompatible with Barlow geometry")
    return energy


def periodic_shell_quadratic_coefficient(
    period_length: int, absolute_period_drift: int
) -> tuple[int, int]:
    """Reduced exact fraction for the n^2 shell-growth coefficient.

    A periodic stacking has the same absolute drift density ``mu=|D|/L`` in
    both directions, so

        S_n / n^2 -> 21/2 - mu^2/2
                     = (21 L^2 - D^2)/(2 L^2).
    """
    if isinstance(period_length, bool) or not isinstance(period_length, int) or period_length <= 0:
        raise ValueError("period_length must be positive")
    _require_natural("absolute_period_drift", absolute_period_drift)
    if absolute_period_drift > period_length or (period_length - absolute_period_drift) % 2:
        raise ValueError("period drift is incompatible with a ±1 word")
    numerator = 21 * period_length * period_length - absolute_period_drift * absolute_period_drift
    denominator = 2 * period_length * period_length
    divisor = gcd(numerator, denominator)
    return numerator // divisor, denominator // divisor


def periodic_ball_cubic_coefficient(
    period_length: int, absolute_period_drift: int
) -> tuple[int, int]:
    """Reduced exact fraction for the n^3 crystal-ball growth coefficient."""
    shell_num, shell_den = periodic_shell_quadratic_coefficient(
        period_length, absolute_period_drift
    )
    denominator = 3 * shell_den
    divisor = gcd(shell_num, denominator)
    return shell_num // divisor, denominator // divisor
