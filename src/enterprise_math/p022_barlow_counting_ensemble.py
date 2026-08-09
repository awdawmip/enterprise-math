"""Exact counting averages over finite two-sided Barlow stacking windows.

At shell radius n there are 4^n microscopic two-sided interface windows: n
independent ±1 signs above the root and n below it.  This module computes exact
finite averages under the uniform counting measure, without introducing a
stochastic model as part of the geometry.

A key separation is that the arithmetic mean of whole-shell geodesic path
multiplicity grows with base 7/2, while counting-typical balanced windows have
individual exponential base 2+sqrt(2).  Rare high-drift histories therefore
lift the mean above the typical rate.
"""

from __future__ import annotations

from math import gcd

Rational = tuple[int, int]


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _reduce(numerator: int, denominator: int) -> Rational:
    if denominator <= 0:
        raise ValueError("denominator must be positive")
    divisor = gcd(abs(numerator), denominator)
    return numerator // divisor, denominator // divisor


def microscopic_two_sided_window_count(radius: int) -> int:
    _require_natural("radius", radius)
    return 4 ** radius


def uniform_shell_cardinality_mean(radius: int) -> Rational:
    """Exact average shell cardinality over all 4^n microscopic windows.

    For one length-n ±1 sum delta,

        sum delta^2 / 2^n = n.

    The two sides are independent, so E[Q_n]=2n.  Substitute into

        4*S_n = 42n^2 + 8 - Q_n.
    """
    _require_natural("radius", radius)
    if radius == 0:
        return (1, 1)
    return _reduce(42 * radius * radius + 8 - 2 * radius, 4)


def uniform_shell_cardinality_variance(radius: int) -> Rational:
    """Exact variance of shell cardinality under finite counting.

    A Rademacher sum has

        E[delta^4] = 3n^2 - 2n,

    hence Var(delta^2)=2n(n-1). Two independent sides give
    Var(Q_n)=4n(n-1), and S_n=(constant-Q_n)/4.
    """
    _require_natural("radius", radius)
    return _reduce(radius * (radius - 1), 4)


def total_shell_cardinality_over_all_windows(radius: int) -> int:
    """Sum of shell cardinality over all microscopic two-sided windows."""
    mean_num, mean_den = uniform_shell_cardinality_mean(radius)
    total = microscopic_two_sided_window_count(radius) * mean_num
    if total % mean_den:
        raise AssertionError("finite counting mean must recover an integer total")
    return total // mean_den


def total_geodesic_paths_over_all_windows(radius: int) -> int:
    """Sum of whole-shell shortest-path totals over all 4^n windows.

    For a target layer of height q<n, the signed BG01 form contains

        2^(-(q+delta)/2) + 2^(-(q-delta)/2).

    Summing over all length-q ±1 prefixes uses

        sum_word 2^(delta/2) = (sqrt(2)+1/sqrt(2))^q = (3/sqrt(2))^q.

    After including the unobserved suffixes and the two sides of the root, all
    radicals cancel. The exact total is

        12*14^n + 2*12^n - 18*8^n - 12*6^n + 18*4^n.

    Radius zero is the single root shell.
    """
    _require_natural("radius", radius)
    if radius == 0:
        return 1
    n = radius
    return (
        12 * (14 ** n)
        + 2 * (12 ** n)
        - 18 * (8 ** n)
        - 12 * (6 ** n)
        + 18 * (4 ** n)
    )


def uniform_geodesic_total_mean(radius: int) -> Rational:
    """Exact average whole-shell shortest-path total over microscopic windows."""
    _require_natural("radius", radius)
    total = total_geodesic_paths_over_all_windows(radius)
    return _reduce(total, microscopic_two_sided_window_count(radius))


def uniform_geodesic_mean_growth_fraction() -> Rational:
    """Exact dominant exponential base 7/2 for the arithmetic mean sequence."""
    return (7, 2)


def minimum_individual_geodesic_growth_equation() -> tuple[int, int, int]:
    """Integer equation encoding the balanced individual growth base.

    Return ``(shift,power,rhs)`` for

        (lambda-shift)^power = rhs.

    Here lambda=2+sqrt(2), so ``(lambda-2)^2=2``.
    """
    return (2, 2, 2)


def rademacher_second_moment(length: int) -> int:
    """Exact E[delta^2] numerator under the uniform one-sided word count."""
    _require_natural("length", length)
    return length


def rademacher_fourth_moment(length: int) -> int:
    """Exact E[delta^4] for a length-n ±1 word."""
    _require_natural("length", length)
    return 3 * length * length - 2 * length
