#!/usr/bin/env python3
"""Exact checker for the arbitrary-direction Enterprise parabola candidate.

Standard-library only.  All coordinate algebra is exact over Fraction.
The checker verifies:
  * frame inversion and canonical local triple reconstruction;
  * C3 covariance and direction-scale covariance;
  * carrier lattice index det = Delta_S and six-element C6 direction orbit;
  * exact discrete parabola generation in every primitive direction tested;
  * the universal carrier-fold seam defect at the vertex.

This is a research checker, not a canonical-foundation declaration.
"""

from __future__ import annotations

from fractions import Fraction
from hashlib import sha256
from itertools import product
from math import gcd
from typing import Sequence, Tuple

Vec3 = Tuple[int, int, int]
Frac3 = Tuple[Fraction, Fraction, Fraction]


def rho(v: Sequence[int]) -> tuple[int, int, int]:
    a, b, c = v
    return c, a, b


def rho2(v: Sequence[int]) -> tuple[int, int, int]:
    return rho(rho(v))


def reverse_decode(v: Sequence[int]) -> tuple[int, int, int]:
    maximum = max(v)
    return tuple(maximum - x for x in v)  # type: ignore[return-value]


def delta(v: Sequence[int]) -> int:
    a, b, c = v
    return a * a + b * b + c * c - a * b - b * c - c * a


def canonical_triples(bound: int) -> list[Vec3]:
    return [
        v
        for v in product(range(bound + 1), repeat=3)
        if min(v) == 0
    ]


def canonicalize(v: Sequence[Fraction | int]) -> Frac3:
    values = tuple(Fraction(x) for x in v)
    minimum = min(values)
    return tuple(x - minimum for x in values)  # type: ignore[return-value]


def carrier_equal(x: Sequence[Fraction | int], y: Sequence[Fraction | int]) -> bool:
    difference = [Fraction(a) - Fraction(b) for a, b in zip(x, y)]
    return difference[0] == difference[1] == difference[2]


def local_coordinates(
    direction: Sequence[int], displacement: Sequence[Fraction | int]
) -> tuple[Fraction, Fraction, Fraction, Frac3]:
    a, b, c = direction
    A, B, C = (Fraction(x) for x in displacement)
    determinant = delta(direction)
    if determinant <= 0:
        raise ValueError("direction must be nonzero and canonical")

    alpha = (
        (a - b) * A + (b - c) * B + (c - a) * C
    ) / determinant
    beta = (
        (c - b) * A + (a - c) * B + (b - a) * C
    ) / determinant
    minimum = min(alpha, beta, Fraction(0))
    local = (alpha - minimum, beta - minimum, -minimum)
    return alpha, beta, minimum, local


def carrier_vec2(v: Sequence[int]) -> tuple[int, int]:
    a, b, c = v
    return a - c, b - c


def det2(u: Sequence[int], v: Sequence[int]) -> int:
    return u[0] * v[1] - u[1] * v[0]


def gcd3(v: Sequence[int]) -> int:
    result = 0
    for value in v:
        result = gcd(result, value)
    return result


def run(bound: int = 12) -> dict[str, object]:
    points = canonical_triples(bound)
    directions = [v for v in points if v != (0, 0, 0)]
    primitive_directions = [v for v in directions if gcd3(v) == 1]

    pair_count = 0
    for direction in directions:
        rotated = rho(direction)
        rotated2 = rho2(direction)
        for point in points:
            alpha, beta, minimum, local = local_coordinates(direction, point)
            reconstructed = tuple(
                local[0] * direction[i]
                + local[1] * rotated[i]
                + local[2] * rotated2[i]
                for i in range(3)
            )
            assert carrier_equal(reconstructed, point)
            assert min(local) == 0 and all(value >= 0 for value in local)

            rotated_result = local_coordinates(rho(direction), rho(point))
            assert (alpha, beta, minimum, local) == rotated_result

            scaled_direction = tuple(3 * value for value in direction)
            scaled = local_coordinates(scaled_direction, point)
            assert scaled[0] == alpha / 3
            assert scaled[1] == beta / 3
            assert scaled[2] == minimum / 3
            assert scaled[3] == tuple(value / 3 for value in local)
            pair_count += 1

    index_count = 0
    orbit_count = 0
    for direction in directions:
        assert det2(carrier_vec2(direction), carrier_vec2(rho(direction))) == delta(direction)
        index_count += 1

        orbit: set[Vec3] = set()
        value = direction
        for turn in range(3):
            if turn:
                value = rho(value)
            orbit.add(value)
            orbit.add(reverse_decode(value))
        assert len(orbit) == 6
        orbit_count += 1

    curve_rows: list[str] = []
    curve_count = 0
    for direction in primitive_directions:
        rotated = rho(direction)
        rotated2 = rho2(direction)
        for transverse_step in range(1, 6):
            for axial_quadratic_step in range(1, 6):
                aperture = Fraction(
                    transverse_step * transverse_step,
                    axial_quadratic_step,
                )
                for parameter in range(-10, 11):
                    U = Fraction(axial_quadratic_step * parameter * parameter)
                    if parameter >= 0:
                        T1 = Fraction(transverse_step * parameter)
                        T2 = Fraction(0)
                    else:
                        T1 = Fraction(0)
                        T2 = Fraction(-transverse_step * parameter)

                    raw = tuple(
                        U * direction[i] + T1 * rotated[i] + T2 * rotated2[i]
                        for i in range(3)
                    )
                    point = canonicalize(raw)
                    local = local_coordinates(direction, point)[3]
                    assert local == (U, T1, T2)
                    assert local[1] * local[1] + local[2] * local[2] == aperture * local[0]
                    curve_rows.append(
                        f"{direction}|{transverse_step}|{axial_quadratic_step}|"
                        f"{parameter}|{point}|{local}"
                    )
                    curve_count += 1

    seam_rows: list[str] = []
    seam_count = 0
    for direction in primitive_directions:
        rotated = rho(direction)
        rotated2 = rho2(direction)
        for transverse_step in range(1, 6):
            for axial_quadratic_step in range(1, 6):
                minus = tuple(
                    axial_quadratic_step * direction[i]
                    + transverse_step * rotated2[i]
                    for i in range(3)
                )
                plus = tuple(
                    axial_quadratic_step * direction[i]
                    + transverse_step * rotated[i]
                    for i in range(3)
                )
                folded_second_difference = tuple(
                    minus[i] + plus[i] for i in range(3)
                )
                expected = tuple(
                    (2 * axial_quadratic_step - transverse_step) * direction[i]
                    for i in range(3)
                )
                assert carrier_equal(folded_second_difference, expected)
                seam_rows.append(
                    f"{direction}|{transverse_step}|{axial_quadratic_step}|"
                    f"{canonicalize(minus)}|{canonicalize(plus)}|"
                    f"{canonicalize(folded_second_difference)}"
                )
                seam_count += 1

    return {
        "bound": bound,
        "directions": len(directions),
        "primitive_directions": len(primitive_directions),
        "direction_point_pairs": pair_count,
        "lattice_index_checks": index_count,
        "C6_orbit_checks": orbit_count,
        "discrete_curve_states": curve_count,
        "discrete_curve_sha256": sha256("\n".join(curve_rows).encode()).hexdigest(),
        "seam_checks": seam_count,
        "seam_sha256": sha256("\n".join(seam_rows).encode()).hexdigest(),
    }


if __name__ == "__main__":
    import json

    print(json.dumps(run(), indent=2, sort_keys=True))
