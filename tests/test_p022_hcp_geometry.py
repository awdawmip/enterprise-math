from collections import deque

from enterprise_math.p022_geodesic_multiplicity import a3_shell_total_geodesic_paths
from enterprise_math.p022_hcp_geometry import (
    hcp_geodesic_path_count,
    hcp_geodesic_path_count_coefficient,
    hcp_graph_distance,
    hcp_neighbors,
    hcp_shell,
    hcp_shell_count,
    hcp_shell_multiplicity_spectrum,
    hcp_shell_total_geodesic_paths,
    hcp_shell_total_geodesic_paths_closed,
    hcp_shell_total_geodesic_paths_recurrence,
)


def _bfs_distances_and_counts(max_radius: int):
    root = (0, 0, 0)
    distances = {root: 0}
    path_counts = {root: 1}
    queue = deque([root])
    while queue:
        current = queue.popleft()
        current_distance = distances[current]
        if current_distance == max_radius:
            continue
        for neighbor in hcp_neighbors(current):
            if neighbor not in distances:
                distances[neighbor] = current_distance + 1
                path_counts[neighbor] = path_counts[current]
                queue.append(neighbor)
            elif distances[neighbor] == current_distance + 1:
                path_counts[neighbor] += path_counts[current]
    return distances, path_counts


def test_hcp_contact_graph_is_degree_twelve_and_undirected() -> None:
    sample = (
        (0, 0, 0),
        (2, -1, 0),
        (-3, 2, 1),
        (1, 4, -2),
        (0, -2, -3),
    )
    for point in sample:
        neighbors = hcp_neighbors(point)
        assert len(neighbors) == 12
        assert len(set(neighbors)) == 12
        for neighbor in neighbors:
            assert point in hcp_neighbors(neighbor)


def test_closed_hcp_distance_matches_independent_bfs() -> None:
    distances, _ = _bfs_distances_and_counts(7)
    for point, distance in distances.items():
        assert hcp_graph_distance(point) == distance

    for radius in range(0, 7):
        shell = set(hcp_shell(radius))
        bfs_shell = {point for point, distance in distances.items() if distance == radius}
        assert shell == bfs_shell


def test_hcp_coordination_shell_sequence() -> None:
    expected = (1, 12, 44, 96, 170, 264, 380)
    assert tuple(hcp_shell_count(radius) for radius in range(len(expected))) == expected


def test_recursive_and_coefficient_geodesic_counts_match_independent_bfs() -> None:
    distances, path_counts = _bfs_distances_and_counts(6)
    for point, distance in distances.items():
        if distance <= 6:
            assert hcp_geodesic_path_count(point) == path_counts[point]
            assert hcp_geodesic_path_count_coefficient(point) == path_counts[point]


def test_hcp_shell_total_geodesic_counts() -> None:
    expected = (1, 12, 84, 384, 1524, 5592, 19812, 68808, 236628)
    assert tuple(
        hcp_shell_total_geodesic_paths(radius) for radius in range(len(expected))
    ) == expected
    assert tuple(
        hcp_shell_total_geodesic_paths_closed(radius) for radius in range(len(expected))
    ) == expected
    assert tuple(
        hcp_shell_total_geodesic_paths_recurrence(radius)
        for radius in range(len(expected))
    ) == expected


def test_closed_shell_formula_and_recurrence_agree_beyond_enumerated_range() -> None:
    for radius in range(0, 31):
        assert hcp_shell_total_geodesic_paths_closed(
            radius
        ) == hcp_shell_total_geodesic_paths_recurrence(radius)


def test_hcp_multiplicity_spectra_begin_to_differ_from_fcc_at_radius_two() -> None:
    assert hcp_shell_multiplicity_spectrum(1) == ((1, 12),)
    assert hcp_shell_multiplicity_spectrum(2) == (
        (1, 18),
        (2, 18),
        (3, 2),
        (4, 6),
    )
    assert hcp_shell_multiplicity_spectrum(3) == (
        (1, 18),
        (2, 6),
        (3, 36),
        (5, 6),
        (6, 18),
        (9, 12),
    )

    # FCC/A_3 and HCP have the same first coordination number and, more
    # surprisingly, the same radius-two total geodesic count. The full
    # multiplicity spectrum still separates them at radius two.
    assert a3_shell_total_geodesic_paths(2) == 84
    assert hcp_shell_total_geodesic_paths(2) == 84

    # At radius three even the shell-total multiplicity separates them.
    assert a3_shell_total_geodesic_paths(3) == 420
    assert hcp_shell_total_geodesic_paths(3) == 384


def test_radius_two_special_endpoints_expose_hcp_only_multiplicity_three() -> None:
    triple_endpoints = tuple(
        point for point in hcp_shell(2) if hcp_geodesic_path_count(point) == 3
    )
    assert set(triple_endpoints) == {(0, 0, 2), (0, 0, -2)}


def test_shell_spectrum_reconstructs_shell_size_and_total_path_count() -> None:
    for radius in range(0, 6):
        spectrum = hcp_shell_multiplicity_spectrum(radius)
        assert sum(endpoint_count for _, endpoint_count in spectrum) == hcp_shell_count(radius)
        assert sum(
            multiplicity * endpoint_count for multiplicity, endpoint_count in spectrum
        ) == hcp_shell_total_geodesic_paths(radius)
