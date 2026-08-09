from functools import lru_cache
from itertools import product

from enterprise_math.p022_geodesic_multiplicity import (
    a3_shell_total_geodesic_paths,
    a_geodesic_interval_profile,
    a_geodesic_path_count,
    a_graph_radius,
    a_shell_total_geodesic_paths,
    sc3_shell_total_geodesic_paths,
    sc_geodesic_interval_profile,
    sc_geodesic_path_count,
    sc_shell_total_geodesic_paths,
)


def _a_shell(p: int, radius: int) -> tuple[tuple[int, ...], ...]:
    coordinate_count = p + 1
    if radius == 0:
        return ((0,) * coordinate_count,)
    points = []
    for prefix in product(range(-radius, radius + 1), repeat=coordinate_count - 1):
        last = -sum(prefix)
        if -radius <= last <= radius:
            point = prefix + (last,)
            if a_graph_radius(point) == radius:
                points.append(point)
    return tuple(points)


def _sc_shell(dimension: int, radius: int) -> tuple[tuple[int, ...], ...]:
    if radius == 0:
        return ((0,) * dimension,)
    return tuple(
        point
        for point in product(range(-radius, radius + 1), repeat=dimension)
        if sum(abs(value) for value in point) == radius
    )


@lru_cache(maxsize=None)
def _a_recursive_path_count(vector: tuple[int, ...]) -> int:
    if all(value == 0 for value in vector):
        return 1
    positive = [index for index, value in enumerate(vector) if value > 0]
    negative = [index for index, value in enumerate(vector) if value < 0]
    total = 0
    for destination in positive:
        for source in negative:
            next_vector = list(vector)
            next_vector[destination] -= 1
            next_vector[source] += 1
            total += _a_recursive_path_count(tuple(next_vector))
    return total


@lru_cache(maxsize=None)
def _sc_recursive_path_count(vector: tuple[int, ...]) -> int:
    if all(value == 0 for value in vector):
        return 1
    total = 0
    for coordinate, value in enumerate(vector):
        if value == 0:
            continue
        next_vector = list(vector)
        next_vector[coordinate] += -1 if value > 0 else 1
        total += _sc_recursive_path_count(tuple(next_vector))
    return total


def _a_interval_profile_by_enumeration(vector: tuple[int, ...]) -> tuple[int, ...]:
    radius = a_graph_radius(vector)
    ranges = []
    for value in vector:
        if value > 0:
            ranges.append(range(0, value + 1))
        elif value < 0:
            ranges.append(range(value, 1))
        else:
            ranges.append(range(0, 1))
    counts = [0] * (radius + 1)
    for middle in product(*ranges):
        if sum(middle) != 0:
            continue
        left = a_graph_radius(middle)
        remainder = tuple(value - mid for value, mid in zip(vector, middle, strict=True))
        if left + a_graph_radius(remainder) == radius:
            counts[left] += 1
    return tuple(counts)


def _sc_interval_profile_by_enumeration(vector: tuple[int, ...]) -> tuple[int, ...]:
    radius = sum(abs(value) for value in vector)
    ranges = []
    for value in vector:
        if value >= 0:
            ranges.append(range(0, value + 1))
        else:
            ranges.append(range(value, 1))
    counts = [0] * (radius + 1)
    for middle in product(*ranges):
        left = sum(abs(value) for value in middle)
        right = sum(abs(value - mid) for value, mid in zip(vector, middle, strict=True))
        if left + right == radius:
            counts[left] += 1
    return tuple(counts)


def test_a_endpoint_formula_matches_independent_recursive_counts() -> None:
    for p in (1, 2, 3):
        for radius in range(0, 5):
            for endpoint in _a_shell(p, radius):
                assert a_geodesic_path_count(endpoint) == _a_recursive_path_count(endpoint)


def test_sc_endpoint_formula_matches_independent_recursive_counts() -> None:
    for dimension in (1, 2, 3):
        for radius in range(0, 5):
            for endpoint in _sc_shell(dimension, radius):
                assert sc_geodesic_path_count(endpoint) == _sc_recursive_path_count(endpoint)


def test_interval_profiles_match_direct_geodesic_interval_enumeration() -> None:
    for endpoint in _a_shell(3, 4):
        assert a_geodesic_interval_profile(endpoint) == _a_interval_profile_by_enumeration(endpoint)
    for endpoint in _sc_shell(3, 4):
        assert sc_geodesic_interval_profile(endpoint) == _sc_interval_profile_by_enumeration(endpoint)


def test_shell_total_formulas_match_endpoint_sums() -> None:
    for p in (1, 2, 3):
        for radius in range(0, 5):
            direct = sum(a_geodesic_path_count(endpoint) for endpoint in _a_shell(p, radius))
            assert a_shell_total_geodesic_paths(p, radius) == direct
    for dimension in (1, 2, 3):
        for radius in range(0, 5):
            direct = sum(sc_geodesic_path_count(endpoint) for endpoint in _sc_shell(dimension, radius))
            assert sc_shell_total_geodesic_paths(dimension, radius) == direct


def test_three_dimensional_closed_forms() -> None:
    expected_a3 = (1, 12, 84, 420, 1812)
    expected_sc3 = (1, 6, 30, 126, 462)
    for radius, expected in enumerate(expected_a3):
        assert a_shell_total_geodesic_paths(3, radius) == expected
        assert a3_shell_total_geodesic_paths(radius) == expected
    for radius, expected in enumerate(expected_sc3):
        assert sc_shell_total_geodesic_paths(3, radius) == expected
        assert sc3_shell_total_geodesic_paths(radius) == expected


def test_same_shell_can_have_different_geodesic_multiplicity() -> None:
    # A_3/FCC-type radius two already separates endpoints by path multiplicity.
    assert a_geodesic_path_count((2, -2, 0, 0)) == 1
    assert a_geodesic_path_count((1, 1, -2, 0)) == 2
    assert a_geodesic_path_count((1, 1, -1, -1)) == 4

    # The corresponding interval-layer multiplicities also differ.
    assert a_geodesic_interval_profile((2, -2, 0, 0)) == (1, 1, 1)
    assert a_geodesic_interval_profile((1, 1, -2, 0)) == (1, 2, 1)
    assert a_geodesic_interval_profile((1, 1, -1, -1)) == (1, 4, 1)


def test_a3_and_sc3_multiplicity_separate_even_when_native_geodesic_defect_is_zero() -> None:
    # Both geometries use their own unweighted shortest-path metric, so the
    # existence-only geodesic defect is automatically zero.  Count structure
    # nevertheless differs immediately and increasingly with radius.
    for radius in range(1, 5):
        assert a3_shell_total_geodesic_paths(radius) > sc3_shell_total_geodesic_paths(radius)
