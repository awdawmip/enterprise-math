from collections import deque

from enterprise_math.p022_barlow_stacking import (
    barlow_distance_and_geodesic_count,
    barlow_geodesic_path_count,
    barlow_graph_distance,
    barlow_neighbors,
    barlow_shell,
    barlow_shell_multiplicity_spectrum,
    barlow_shell_total_geodesic_paths,
    stacking_prefix_counts,
    stacking_prefix_imbalance,
    vertical_witness_polynomial,
    vertical_witness_polynomial_from_counts,
)
from enterprise_math.p022_geodesic_multiplicity import a3_shell_total_geodesic_paths
from enterprise_math.p022_hcp_geometry import (
    hcp_geodesic_path_count,
    hcp_graph_distance,
    hcp_shell_multiplicity_spectrum,
    hcp_shell_total_geodesic_paths,
)

FCC = (-1,)
HCP = (-1, 1)


def _bfs(pattern, max_radius):
    root = (0, 0, 0)
    distance = {root: 0}
    count = {root: 1}
    queue = deque([root])
    while queue:
        current = queue.popleft()
        current_distance = distance[current]
        if current_distance == max_radius:
            continue
        for neighbor in barlow_neighbors(current, pattern):
            if neighbor not in distance:
                distance[neighbor] = current_distance + 1
                count[neighbor] = count[current]
                queue.append(neighbor)
            elif distance[neighbor] == current_distance + 1:
                count[neighbor] += count[current]
    return distance, count


def test_barlow_formula_matches_independent_bfs_for_fcc_and_hcp() -> None:
    for pattern in (FCC, HCP):
        distances, counts = _bfs(pattern, 5)
        for point, distance in distances.items():
            assert barlow_graph_distance(point, pattern) == distance
            assert barlow_geodesic_path_count(point, pattern) == counts[point]


def test_alternating_barlow_pattern_reconstructs_hcp_exactly() -> None:
    for radius in range(0, 5):
        assert barlow_shell_multiplicity_spectrum(
            radius, HCP
        ) == hcp_shell_multiplicity_spectrum(radius)
        assert barlow_shell_total_geodesic_paths(
            radius, HCP
        ) == hcp_shell_total_geodesic_paths(radius)
        for point in barlow_shell(radius, HCP):
            assert barlow_graph_distance(point, HCP) == hcp_graph_distance(point)
            assert barlow_geodesic_path_count(point, HCP) == hcp_geodesic_path_count(point)


def test_constant_barlow_pattern_reconstructs_fcc_a3_shell_invariants() -> None:
    expected_spectra = {
        0: ((1, 1),),
        1: ((1, 12),),
        2: ((1, 12), (2, 24), (4, 6)),
        3: ((1, 12), (3, 48), (6, 8), (9, 24)),
        4: ((1, 12), (4, 48), (6, 24), (12, 24), (16, 24), (24, 24), (36, 6)),
    }
    for radius, spectrum in expected_spectra.items():
        assert barlow_shell_multiplicity_spectrum(radius, FCC) == spectrum
        assert barlow_shell_total_geodesic_paths(
            radius, FCC
        ) == a3_shell_total_geodesic_paths(radius)


def test_vertical_polynomial_depends_only_on_cumulative_effective_sign_counts() -> None:
    patterns = (
        (-1, -1, 1, 1),
        (-1, 1, -1, 1),
        (1, -1, -1, 1),
    )
    target_layer = 4
    polynomials = []
    for pattern in patterns:
        minus_count, plus_count = stacking_prefix_counts(pattern, target_layer)
        assert (minus_count, plus_count) == (2, 2)
        assert stacking_prefix_imbalance(pattern, target_layer) == 0
        polynomial = vertical_witness_polynomial(pattern, target_layer)
        assert polynomial == vertical_witness_polynomial_from_counts(2, 2)
        polynomials.append(polynomial)
    assert polynomials[0] == polynomials[1] == polynomials[2]


def test_same_prefix_counts_give_same_root_to_target_layer_metric_and_counts() -> None:
    first = (-1, -1, 1, 1)
    second = (-1, 1, -1, 1)
    for q in range(-4, 5):
        for r in range(-4, 5):
            point = (q, r, 4)
            assert barlow_distance_and_geodesic_count(
                point, first
            ) == barlow_distance_and_geodesic_count(point, second)


def test_prefix_order_can_still_be_visible_at_intermediate_layers() -> None:
    first = (-1, -1, 1, 1)
    second = (-1, 1, -1, 1)
    # At layer four both prefixes contain two signs of each kind and therefore
    # have identical root-to-layer metric/count semantics.  At layer two their
    # cumulative counts differ, so the narrower compression does not preserve
    # all intermediate-layer queries.
    assert stacking_prefix_counts(first, 4) == stacking_prefix_counts(second, 4) == (2, 2)
    assert stacking_prefix_counts(first, 2) == (2, 0)
    assert stacking_prefix_counts(second, 2) == (1, 1)

    witnessed_difference = False
    for q in range(-3, 4):
        for r in range(-3, 4):
            point = (q, r, 2)
            if barlow_distance_and_geodesic_count(
                point, first
            ) != barlow_distance_and_geodesic_count(point, second):
                witnessed_difference = True
                break
        if witnessed_difference:
            break
    assert witnessed_difference
