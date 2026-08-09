"""Exact geodesic multiplicity observables for P022 discrete geometries.

This module deliberately stays on the geometry side of the Enterprise Math
ownership boundary.  The generic fact that non-negative witness counts form a
count-enriched correspondence algebra belongs to A4/A2.  P022 contributes the
closed integer specializations for concrete intrinsic geometries.

Two families are compared:

* the root lattice A_p = {x in Z^(p+1) : sum x_i = 0} with primitive moves
  e_i-e_j;
* simple cubic Z^d with standard-axis adjacency.

For both families the native graph metric is already a shortest-path metric,
so existence-only geodesic defect is identically zero.  What remains
geometry-discriminating is witness multiplicity: how many shortest paths and
how many geodesic intermediate states realize each distance layer.
"""

from __future__ import annotations

from math import comb, factorial


def _require_natural(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a non-negative integer")


def _require_positive(name: str, value: int) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")


def _require_integer_vector(name: str, vector: tuple[int, ...]) -> None:
    if not isinstance(vector, tuple) or not vector:
        raise ValueError(f"{name} must be a non-empty tuple")
    if any(isinstance(value, bool) or not isinstance(value, int) for value in vector):
        raise ValueError(f"{name} entries must be integers")


def _require_a_displacement(vector: tuple[int, ...]) -> None:
    _require_integer_vector("vector", vector)
    if len(vector) < 2:
        raise ValueError("A_p displacement needs at least two coordinates")
    if sum(vector) != 0:
        raise ValueError("A_p displacement must have zero coordinate sum")


def a_graph_radius(vector: tuple[int, ...]) -> int:
    """Native A_p graph distance from zero to ``vector``."""
    _require_a_displacement(vector)
    return sum(value for value in vector if value > 0)


def sc_graph_radius(vector: tuple[int, ...]) -> int:
    """Native simple-cubic L1 graph distance from zero to ``vector``."""
    _require_integer_vector("vector", vector)
    return sum(abs(value) for value in vector)


def a_geodesic_path_count(vector: tuple[int, ...]) -> int:
    """Number of shortest primitive-root paths from zero to an A_p endpoint.

    If r is the graph radius, every shortest path performs exactly r transfers
    from negative coordinates to positive coordinates.  Destination labels and
    source labels can be ordered independently, which gives

        (r!)^2 / (prod_{v_i>0} v_i! * prod_{v_j<0} (-v_j)!).
    """
    _require_a_displacement(vector)
    radius = a_graph_radius(vector)
    positive_denominator = 1
    negative_denominator = 1
    for value in vector:
        if value > 0:
            positive_denominator *= factorial(value)
        elif value < 0:
            negative_denominator *= factorial(-value)
    numerator = factorial(radius) ** 2
    denominator = positive_denominator * negative_denominator
    if numerator % denominator != 0:
        raise AssertionError("A_p geodesic multiplicity must be integral")
    return numerator // denominator


def sc_geodesic_path_count(vector: tuple[int, ...]) -> int:
    """Number of shortest standard-axis paths to a simple-cubic endpoint."""
    _require_integer_vector("vector", vector)
    radius = sc_graph_radius(vector)
    denominator = 1
    for value in vector:
        denominator *= factorial(abs(value))
    numerator = factorial(radius)
    if numerator % denominator != 0:
        raise AssertionError("simple-cubic geodesic multiplicity must be integral")
    return numerator // denominator


def _bounded_sum_coefficients(bounds: tuple[int, ...]) -> tuple[int, ...]:
    """Coefficients of prod_i (1+t+...+t^bounds_i) by finite integer DP."""
    if not bounds:
        return (1,)
    if any(isinstance(value, bool) or not isinstance(value, int) or value < 0 for value in bounds):
        raise ValueError("bounds must be non-negative integers")
    total = sum(bounds)
    coefficients = [0] * (total + 1)
    coefficients[0] = 1
    current_total = 0
    for bound in bounds:
        next_coefficients = [0] * (total + 1)
        for subtotal in range(current_total + 1):
            multiplicity = coefficients[subtotal]
            if multiplicity == 0:
                continue
            for increment in range(bound + 1):
                next_coefficients[subtotal + increment] += multiplicity
        coefficients = next_coefficients
        current_total += bound
    return tuple(coefficients)


def a_geodesic_interval_profile(vector: tuple[int, ...]) -> tuple[int, ...]:
    """Layer sizes of the geodesic interval I_a(0,vector) in A_p.

    Entry ``a`` counts represented endpoints y satisfying

        d(0,y)=a and d(y,vector)=d(0,vector)-a.

    Positive-coordinate progress and negative-coordinate deficit repair are
    independent bounded compositions of the same layer index, so the profile
    is the pointwise product of their coefficient sequences.
    """
    _require_a_displacement(vector)
    positive = tuple(value for value in vector if value > 0)
    negative = tuple(-value for value in vector if value < 0)
    radius = sum(positive)
    positive_coefficients = _bounded_sum_coefficients(positive)
    negative_coefficients = _bounded_sum_coefficients(negative)
    if len(positive_coefficients) != radius + 1 or len(negative_coefficients) != radius + 1:
        raise AssertionError("positive and negative A_p masses must agree")
    return tuple(
        positive_coefficients[layer] * negative_coefficients[layer]
        for layer in range(radius + 1)
    )


def sc_geodesic_interval_profile(vector: tuple[int, ...]) -> tuple[int, ...]:
    """Layer sizes of the L1 geodesic interval for a simple-cubic endpoint."""
    _require_integer_vector("vector", vector)
    return _bounded_sum_coefficients(tuple(abs(value) for value in vector))


def stirling_second(n: int, k: int) -> int:
    """Stirling number S(n,k), computed by its exact integer recurrence."""
    _require_natural("n", n)
    _require_natural("k", k)
    if k > n:
        return 0
    row = [0] * (k + 1)
    row[0] = 1
    for size in range(1, n + 1):
        next_row = [0] * (k + 1)
        upper = min(size, k)
        for blocks in range(1, upper + 1):
            next_row[blocks] = blocks * row[blocks] + row[blocks - 1]
        row = next_row
    return row[k]


def a_shell_total_geodesic_paths(p: int, radius: int) -> int:
    """Total shortest-path multiplicity over the radius-r shell of A_p.

    Let n=p+1.  If an endpoint uses ``a`` positive coordinates and ``b``
    negative coordinates, choose those disjoint coordinate sets and then count
    onto destination/source label sequences independently.  Thus, for r>0,

      sum_{a,b>=1,a+b<=n}
        C(n,a) C(n-a,b)
        a! S(r,a) b! S(r,b).
    """
    _require_positive("p", p)
    _require_natural("radius", radius)
    if radius == 0:
        return 1
    coordinate_count = p + 1
    total = 0
    for positive_count in range(1, min(coordinate_count - 1, radius) + 1):
        positive_onto = factorial(positive_count) * stirling_second(radius, positive_count)
        if positive_onto == 0:
            continue
        remaining_coordinates = coordinate_count - positive_count
        for negative_count in range(1, min(remaining_coordinates, radius) + 1):
            negative_onto = factorial(negative_count) * stirling_second(radius, negative_count)
            if negative_onto == 0:
                continue
            total += (
                comb(coordinate_count, positive_count)
                * comb(remaining_coordinates, negative_count)
                * positive_onto
                * negative_onto
            )
    return total


def sc_shell_total_geodesic_paths(dimension: int, radius: int) -> int:
    """Total shortest-path multiplicity over the L1 radius-r shell of Z^d."""
    _require_positive("dimension", dimension)
    _require_natural("radius", radius)
    if radius == 0:
        return 1
    return sum(
        comb(dimension, active_coordinates)
        * (2 ** active_coordinates)
        * factorial(active_coordinates)
        * stirling_second(radius, active_coordinates)
        for active_coordinates in range(1, min(dimension, radius) + 1)
    )


def a3_shell_total_geodesic_paths(radius: int) -> int:
    """Closed form for the A_3/FCC-type primitive graph shell, r>=1."""
    _require_natural("radius", radius)
    if radius == 0:
        return 1
    return 6 * (4 ** radius) + 8 * (3 ** radius) - 24 * (2 ** radius) + 12


def sc3_shell_total_geodesic_paths(radius: int) -> int:
    """Closed form for the standard 3D simple-cubic L1 graph shell, r>=1."""
    _require_natural("radius", radius)
    if radius == 0:
        return 1
    return 8 * (3 ** radius) - 12 * (2 ** radius) + 6
