from itertools import product

from enterprise_math.p022_barlow_coordination import (
    barlow_ball_vertex_count_from_cumulative_energy,
    barlow_layer_shell_first_moment,
    barlow_layer_shell_vertex_count,
    barlow_shell_vertex_count_from_extreme_imbalances,
    barlow_vertical_support_first_moment,
    barlow_vertical_support_size,
    cumulative_drift_energy_from_ball_vertex_count,
    extreme_layer_vertex_count,
    periodic_ball_cubic_coefficient,
    periodic_shell_quadratic_coefficient,
    recover_imbalance_from_shell_layer_moment,
    recover_imbalance_from_vertical_support_moment,
    shell_drift_energy_from_vertex_count,
)
from enterprise_math.p022_barlow_growth import barlow_shell_total_geodesic_paths_closed
from enterprise_math.p022_barlow_stacking import (
    barlow_shell,
    stacking_prefix_imbalance,
    vertical_witness_polynomial,
)
from enterprise_math.p022_hcp_geometry import hcp_shell_count

FCC = (-1,)
HCP = (-1, 1)


def _support_points(polynomial):
    return tuple(point for point, coefficient in polynomial.items() if coefficient > 0)


def _support_size(polynomial) -> int:
    return len(_support_points(polynomial))


def _shell_count(pattern, radius: int) -> int:
    positive = stacking_prefix_imbalance(pattern, radius)
    negative = stacking_prefix_imbalance(pattern, -radius)
    return barlow_shell_vertex_count_from_extreme_imbalances(
        radius, positive, negative
    )


def _ball_count(pattern, radius: int) -> int:
    return sum(_shell_count(pattern, current) for current in range(radius + 1))


def test_vertical_support_closed_form_and_moment_match_exact_polynomial_support() -> None:
    for period in range(1, 6):
        for pattern in product((-1, 1), repeat=period):
            pattern = tuple(pattern)
            for layer in range(-8, 9):
                imbalance = stacking_prefix_imbalance(pattern, layer)
                polynomial = vertical_witness_polynomial(pattern, layer)
                points = _support_points(polynomial)
                direct_size = len(points)
                direct_q_moment = sum(q for q, _ in points)
                direct_r_moment = sum(r for _, r in points)

                assert barlow_vertical_support_size(abs(layer), imbalance) == direct_size
                assert barlow_vertical_support_first_moment(
                    abs(layer), imbalance
                ) == direct_q_moment == direct_r_moment
                assert recover_imbalance_from_vertical_support_moment(
                    abs(layer), direct_size, direct_q_moment
                ) == imbalance


def test_layer_shell_formula_and_moment_match_direct_shell_enumeration() -> None:
    for period in range(1, 5):
        for pattern in product((-1, 1), repeat=period):
            pattern = tuple(pattern)
            for radius in range(0, 7):
                shell = barlow_shell(radius, pattern)
                for layer in range(-radius, radius + 1):
                    points = tuple(point for point in shell if point[2] == layer)
                    direct_size = len(points)
                    direct_q_moment = sum(point[0] for point in points)
                    direct_r_moment = sum(point[1] for point in points)
                    imbalance = stacking_prefix_imbalance(pattern, layer)

                    assert barlow_layer_shell_vertex_count(
                        radius, layer, imbalance
                    ) == direct_size
                    assert barlow_layer_shell_first_moment(
                        radius, layer, imbalance
                    ) == direct_q_moment == direct_r_moment
                    assert recover_imbalance_from_shell_layer_moment(
                        radius, layer, direct_size, direct_q_moment
                    ) == imbalance


def test_nonextreme_layer_cardinality_is_stacking_independent_but_moment_is_not() -> None:
    radius = 6
    patterns = (
        (-1,),
        (-1, 1),
        (-1, -1, 1),
        (-1, -1, 1, 1),
        (-1, 1, 1, -1, 1),
    )
    for layer in range(-radius + 1, radius):
        expected_size = 3 * (2 * radius - abs(layer))
        sizes = set()
        moments = set()
        for pattern in patterns:
            imbalance = stacking_prefix_imbalance(pattern, layer)
            size = barlow_layer_shell_vertex_count(radius, layer, imbalance)
            moment = barlow_layer_shell_first_moment(radius, layer, imbalance)
            sizes.add(size)
            moments.add(moment)
            assert size == expected_size
            assert moment == imbalance * (2 * radius - abs(layer))
        assert sizes == {expected_size}
        if layer != 0:
            assert len(moments) >= 1


def test_extreme_layer_count_is_exact_quadratic_drift_observable() -> None:
    for radius in range(0, 9):
        for imbalance in range(-radius, radius + 1, 2):
            assert extreme_layer_vertex_count(
                radius, imbalance
            ) == barlow_vertical_support_size(radius, imbalance)


def test_whole_shell_formula_matches_all_short_periodic_barlow_shells() -> None:
    for period in range(1, 6):
        for pattern in product((-1, 1), repeat=period):
            pattern = tuple(pattern)
            for radius in range(0, 8):
                positive = stacking_prefix_imbalance(pattern, radius)
                negative = stacking_prefix_imbalance(pattern, -radius)
                direct = len(barlow_shell(radius, pattern))
                closed = barlow_shell_vertex_count_from_extreme_imbalances(
                    radius, positive, negative
                )
                assert closed == direct
                assert shell_drift_energy_from_vertex_count(radius, direct) == (
                    positive * positive + negative * negative
                )


def test_fcc_and_hcp_coordination_sequences_are_special_cases() -> None:
    expected_fcc = (1, 12, 42, 92, 162, 252, 362, 492)
    for radius, expected in enumerate(expected_fcc):
        assert _shell_count(FCC, radius) == expected

    for radius in range(0, 8):
        assert _shell_count(HCP, radius) == hcp_shell_count(radius)


def test_ball_count_uses_only_cumulative_quadratic_drift_energy() -> None:
    for period in range(1, 5):
        for pattern in product((-1, 1), repeat=period):
            pattern = tuple(pattern)
            cumulative_energy = 0
            direct_ball = 1
            for radius in range(1, 9):
                positive = stacking_prefix_imbalance(pattern, radius)
                negative = stacking_prefix_imbalance(pattern, -radius)
                cumulative_energy += positive * positive + negative * negative
                shell = len(barlow_shell(radius, pattern))
                direct_ball += shell
                assert barlow_ball_vertex_count_from_cumulative_energy(
                    radius, cumulative_energy
                ) == direct_ball
                assert cumulative_drift_energy_from_ball_vertex_count(
                    radius, direct_ball
                ) == cumulative_energy


def test_same_shell_energy_can_hide_top_bottom_allocation() -> None:
    radius = 5
    # These two absolute drift pairs have the same quadratic energy 26, so the
    # whole shell cardinality cannot distinguish how drift is split by side.
    first = barlow_shell_vertex_count_from_extreme_imbalances(radius, 5, 1)
    second = barlow_shell_vertex_count_from_extreme_imbalances(radius, 1, 5)
    assert first == second
    assert shell_drift_energy_from_vertex_count(radius, first) == 26


def test_same_shell_cardinality_can_hide_geodesic_multiplicity() -> None:
    first = (-1, -1, 1)
    second = (-1, 1, -1)
    radius = 3

    assert _shell_count(first, radius) == _shell_count(second, radius) == 96
    assert barlow_shell_total_geodesic_paths_closed(
        radius, first
    ) == 402
    assert barlow_shell_total_geodesic_paths_closed(
        radius, second
    ) == 384

    # The extreme quadratic energy agrees while the intermediate absolute
    # imbalance trajectories differ.
    first_energy = (
        stacking_prefix_imbalance(first, radius) ** 2
        + stacking_prefix_imbalance(first, -radius) ** 2
    )
    second_energy = (
        stacking_prefix_imbalance(second, radius) ** 2
        + stacking_prefix_imbalance(second, -radius) ** 2
    )
    assert first_energy == second_energy == 2


def test_same_ball_cardinality_can_hide_current_shell_and_path_structure() -> None:
    first = (-1, -1, 1)
    second = (-1, 1, -1)
    radius = 4

    assert _ball_count(first, radius) == _ball_count(second, radius) == 321
    assert _shell_count(first, radius) == 169
    assert _shell_count(second, radius) == 168
    assert barlow_shell_total_geodesic_paths_closed(
        radius, first
    ) == 1596
    assert barlow_shell_total_geodesic_paths_closed(
        radius, second
    ) == 1524


def test_periodic_asymptotic_coefficients_are_exact_rational_data() -> None:
    # FCC: mu=1, shell coefficient 10 and ball coefficient 10/3.
    assert periodic_shell_quadratic_coefficient(1, 1) == (10, 1)
    assert periodic_ball_cubic_coefficient(1, 1) == (10, 3)

    # HCP / any zero-drift periodic stacking: shell coefficient 21/2 and ball 7/2.
    assert periodic_shell_quadratic_coefficient(2, 0) == (21, 2)
    assert periodic_ball_cubic_coefficient(2, 0) == (7, 2)

    # Period 3 with |D|=1: 21/2 - (1/3)^2/2 = 94/9.
    assert periodic_shell_quadratic_coefficient(3, 1) == (94, 9)
    assert periodic_ball_cubic_coefficient(3, 1) == (94, 27)
