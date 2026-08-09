from collections import Counter
from itertools import product
from math import isclose, sqrt

from enterprise_math.p022_barlow_coordination import (
    barlow_shell_vertex_count_from_extreme_imbalances,
)
from enterprise_math.p022_barlow_counting_ensemble import (
    microscopic_two_sided_window_count,
    rademacher_fourth_moment,
    rademacher_second_moment,
    total_geodesic_paths_over_all_windows,
    total_shell_cardinality_over_all_windows,
    uniform_geodesic_mean_growth_fraction,
    uniform_geodesic_total_mean,
    uniform_shell_cardinality_mean,
    uniform_shell_cardinality_variance,
)
from enterprise_math.p022_barlow_growth import layer_shell_total_from_imbalance if False else barlow_layer_shell_total_geodesic_paths
from enterprise_math.p022_barlow_aperiodic import (
    imbalance_trajectory_from_interface_windows,
    shell_total_from_imbalance_trajectory,
)


def _signed_sum(word) -> int:
    return sum(word)


def _shell_cardinality_from_words(radius: int, downward_word, upward_word) -> int:
    positive = _signed_sum(upward_word)
    negative = -_signed_sum(downward_word)
    return barlow_shell_vertex_count_from_extreme_imbalances(
        radius, positive, negative
    )


def _geodesic_total_from_words(radius: int, downward_word, upward_word) -> int:
    trajectory = imbalance_trajectory_from_interface_windows(
        tuple(downward_word), tuple(upward_word)
    )
    return shell_total_from_imbalance_trajectory(radius, trajectory)


def test_rademacher_even_moments_match_direct_word_counting() -> None:
    for length in range(0, 10):
        words = tuple(product((-1, 1), repeat=length))
        denominator = 2 ** length
        second = sum(_signed_sum(word) ** 2 for word in words)
        fourth = sum(_signed_sum(word) ** 4 for word in words)
        assert second == denominator * rademacher_second_moment(length)
        assert fourth == denominator * rademacher_fourth_moment(length)


def test_shell_mean_variance_and_total_match_all_short_two_sided_windows() -> None:
    for radius in range(0, 6):
        words = tuple(product((-1, 1), repeat=radius))
        values = [
            _shell_cardinality_from_words(radius, downward, upward)
            for downward in words
            for upward in words
        ]
        count = len(values)
        assert count == microscopic_two_sided_window_count(radius)
        assert sum(values) == total_shell_cardinality_over_all_windows(radius)

        mean_num, mean_den = uniform_shell_cardinality_mean(radius)
        assert sum(values) * mean_den == mean_num * count

        variance_num, variance_den = uniform_shell_cardinality_variance(radius)
        # Use the exact identity Var = E[S^2]-E[S]^2 without floats.
        square_sum = sum(value * value for value in values)
        assert (
            (square_sum * mean_den * mean_den - count * mean_num * mean_num)
            * variance_den
            == variance_num * count * mean_den * mean_den
        )


def test_geodesic_mean_closed_form_matches_all_short_two_sided_windows() -> None:
    for radius in range(0, 6):
        words = tuple(product((-1, 1), repeat=radius))
        direct_total = sum(
            _geodesic_total_from_words(radius, downward, upward)
            for downward in words
            for upward in words
        )
        assert direct_total == total_geodesic_paths_over_all_windows(radius)
        mean_num, mean_den = uniform_geodesic_total_mean(radius)
        assert direct_total * mean_den == mean_num * (4 ** radius)


def test_mean_geodesic_growth_base_is_seven_halves() -> None:
    assert uniform_geodesic_mean_growth_fraction() == (7, 2)
    # Finite roots approach 7/2 from the exact average formula.
    roots = []
    for radius in range(12, 25):
        mean_num, mean_den = uniform_geodesic_total_mean(radius)
        roots.append((mean_num / mean_den) ** (1 / radius))
    assert abs(roots[-1] - 3.5) < abs(roots[0] - 3.5)
    assert roots[-1] > 2 + sqrt(2)


def test_mean_shell_is_near_maximal_on_n_squared_scale() -> None:
    # Exact mean deficit from the maximal 21n^2/2+O(1) shell scale is only
    # linear in n because E[Q_n]=2n.
    for radius in range(2, 20):
        mean_num, mean_den = uniform_shell_cardinality_mean(radius)
        assert mean_den in (1, 2)
        mean = mean_num / mean_den
        normalized = mean / (radius * radius)
        assert normalized < 10.5 + 2 / (radius * radius)
        assert normalized > 10.5 - 1 / radius
