from itertools import product

from enterprise_math.p022_barlow_coordination import (
    barlow_shell_vertex_count_from_extreme_imbalances,
)
from enterprise_math.p022_barlow_coordination_history import (
    reconstruct_unordered_drift_history,
)
from enterprise_math.p022_barlow_local_observability import (
    recover_current_drift_pair_from_consecutive_energies,
    recover_current_drift_pair_from_consecutive_shells,
    recover_drift_history_by_sliding_shell_pairs,
    uniform_hidden_state_observation_depth,
)


def _shell_history(downward_word, upward_word):
    output = [1]
    down_sum = 0
    up_sum = 0
    for radius in range(1, len(upward_word) + 1):
        down_sum += downward_word[radius - 1]
        up_sum += upward_word[radius - 1]
        output.append(
            barlow_shell_vertex_count_from_extreme_imbalances(
                radius, up_sum, -down_sum
            )
        )
    return tuple(output)


def _direct_history(downward_word, upward_word):
    output = [(0, 0)]
    down_sum = 0
    up_sum = 0
    for index in range(len(upward_word)):
        down_sum += downward_word[index]
        up_sum += upward_word[index]
        output.append(tuple(sorted((abs(up_sum), abs(down_sum)))))
    return tuple(output)


def test_energy_step_decoder_matches_every_short_legal_transition() -> None:
    # Exhaust absolute current pairs reachable at each parity and every legal
    # predecessor choice.  The decoder sees only the two scalar energies.
    for current_radius in range(1, 25):
        current_values = range(current_radius % 2, current_radius + 1, 2)
        previous_values = set(range((current_radius - 1) % 2, current_radius, 2))
        for left in current_values:
            for right in current_values:
                expected = tuple(sorted((left, right)))
                left_predecessors = {
                    value
                    for value in (abs(left - 1), left + 1)
                    if value in previous_values
                }
                right_predecessors = {
                    value
                    for value in (abs(right - 1), right + 1)
                    if value in previous_values
                }
                for previous_left in left_predecessors:
                    for previous_right in right_predecessors:
                        previous_energy = previous_left**2 + previous_right**2
                        current_energy = left**2 + right**2
                        assert recover_current_drift_pair_from_consecutive_energies(
                            previous_energy, current_energy
                        ) == expected


def test_sliding_two_shell_decoder_matches_direct_microscopic_histories() -> None:
    for length in range(0, 7):
        words = tuple(product((-1, 1), repeat=length))
        for downward in words:
            for upward in words:
                shells = _shell_history(downward, upward)
                expected = _direct_history(downward, upward)
                assert recover_drift_history_by_sliding_shell_pairs(shells) == expected
                assert reconstruct_unordered_drift_history(shells) == expected
                for radius in range(1, len(shells)):
                    assert recover_current_drift_pair_from_consecutive_shells(
                        radius, shells[radius - 1], shells[radius]
                    ) == expected[radius]


def test_depth_one_fails_at_radius_seven_but_depth_two_separates() -> None:
    assert uniform_hidden_state_observation_depth() == 2

    # Same current energy Q_7=50 but distinct hidden current states.
    assert 1**2 + 7**2 == 5**2 + 5**2 == 50

    # Legal predecessors can be chosen with different previous energies, which
    # the two-shell decoder uses to disambiguate them.
    first = recover_current_drift_pair_from_consecutive_energies(
        0**2 + 6**2, 50
    )
    second = recover_current_drift_pair_from_consecutive_energies(
        4**2 + 4**2, 50
    )
    assert first == (1, 7)
    assert second == (5, 5)


def test_two_shell_formula_covers_sum_difference_and_zero_cases() -> None:
    # |L|=a+b
    assert recover_current_drift_pair_from_consecutive_energies(36, 50) == (1, 7)
    # |L|=|a-b|
    assert recover_current_drift_pair_from_consecutive_energies(16, 10) == (1, 3)
    # L^2=Q: one coordinate is zero.
    assert recover_current_drift_pair_from_consecutive_energies(5, 4) == (0, 2)
