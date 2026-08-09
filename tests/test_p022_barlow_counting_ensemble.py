from itertools import product

from enterprise_math.p022_barlow_coordination import (
    barlow_shell_vertex_count_from_extreme_imbalances,
)
from enterprise_math.p022_barlow_counting_ensemble import (
    microscopic_two_sided_window_count,
    minimum_individual_geodesic_growth_equation,
    rademacher_fourth_moment,
    rademacher_second_moment,
    total_geodesic_paths_over_all_windows,
    total_shell_cardinality_over_all_windows,
    uniform_geodesic_mean_growth_fraction,
    uniform_geodesic_total_mean,
    uniform_shell_cardinality_mean,
    uniform_shell_cardinality_variance,
)
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


def test_mean_geodesic_growth_base_exceeds_balanced_individual_base_exactly() -> None:
    assert uniform_geodesic_mean_growth_fraction() == (7, 2)
    assert minimum_individual_geodesic_growth_equation() == (2, 2, 2)
    # 7/2 > 2+sqrt(2) iff 3/2 > sqrt(2), equivalently 9 > 8.
    assert 3 * 3 > 2 * 2 * 2


def test_mean_shell_is_near_maximal_on_n_squared_scale_without_floats() -> None:
    # Exact mean is (42n^2-2n+8)/4.  Compare after cross multiplication.
    for radius in range(2, 20):
        mean_num, mean_den = uniform_shell_cardinality_mean(radius)
        # mean/n^2 < 21/2 + 2/n^2
        assert 2 * mean_num < (21 * radius * radius + 4) * mean_den
        # mean/n^2 > 21/2 - 1/n
        assert 2 * radius * mean_num > (
            21 * radius * radius * radius - 2 * radius * radius
        ) * mean_den
