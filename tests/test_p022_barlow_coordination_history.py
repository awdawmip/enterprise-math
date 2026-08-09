from itertools import product

from enterprise_math.p022_barlow_aperiodic import (
    imbalance_trajectory_from_interface_windows,
    shell_total_from_imbalance_trajectory,
)
from enterprise_math.p022_barlow_coordination import (
    barlow_shell_vertex_count_from_extreme_imbalances,
)
from enterprise_math.p022_barlow_coordination_history import (
    candidate_absolute_drift_pairs,
    geodesic_total_from_coordination_history,
    reconstruct_unordered_drift_history,
    successor_energy_map,
    unordered_drift_pair_successors,
)


def _shell_history(downward_word, upward_word):
    length = len(upward_word)
    output = [1]
    down_sum = 0
    up_sum = 0
    for radius in range(1, length + 1):
        down_sum += downward_word[radius - 1]
        up_sum += upward_word[radius - 1]
        output.append(
            barlow_shell_vertex_count_from_extreme_imbalances(
                radius,
                up_sum,
                -down_sum,
            )
        )
    return tuple(output)


def _direct_unordered_drift_history(downward_word, upward_word):
    output = [(0, 0)]
    down_sum = 0
    up_sum = 0
    for index in range(len(upward_word)):
        down_sum += downward_word[index]
        up_sum += upward_word[index]
        output.append(tuple(sorted((abs(up_sum), abs(down_sum)))))
    return tuple(output)


def test_successor_orbits_have_unique_squared_energies() -> None:
    for radius in range(0, 20):
        values = range(radius % 2, radius + 1, 2)
        for left in values:
            for right in values:
                pair = tuple(sorted((left, right)))
                successors = unordered_drift_pair_successors(pair)
                energy_map = successor_energy_map(pair)
                assert len(energy_map) == len(successors)
                assert len({energy for energy, _ in energy_map}) == len(successors)


def test_coordination_history_reconstructs_unordered_drift_for_all_short_windows() -> None:
    for length in range(0, 7):
        words = tuple(product((-1, 1), repeat=length))
        for downward in words:
            for upward in words:
                shells = _shell_history(downward, upward)
                assert reconstruct_unordered_drift_history(
                    shells
                ) == _direct_unordered_drift_history(downward, upward)


def test_coordination_history_reconstructs_geodesic_total() -> None:
    for length in range(0, 6):
        words = tuple(product((-1, 1), repeat=length))
        for downward in words:
            for upward in words:
                shells = _shell_history(downward, upward)
                trajectory = imbalance_trajectory_from_interface_windows(
                    tuple(downward), tuple(upward)
                )
                direct = shell_total_from_imbalance_trajectory(
                    length, trajectory
                )
                assert geodesic_total_from_coordination_history(shells) == direct


def test_single_radius_energy_can_have_multiple_static_drift_pairs() -> None:
    # 50=1^2+7^2=5^2+5^2, so S_7 alone cannot recover the unordered pair.
    assert candidate_absolute_drift_pairs(7, 50) == ((1, 7), (5, 5))


def test_full_history_resolves_the_radius_seven_static_ambiguity() -> None:
    # Two windows ending in the two different Q=50 representations necessarily
    # have different earlier coordination histories.
    first_down = (1, 1, 1, 1, 1, 1, 1)       # |delta_-7|=7
    first_up = (1, 1, 1, 1, -1, -1, -1)       # |delta_7|=1
    second_down = (1, 1, 1, 1, 1, 1, -1)      # |delta_-7|=5
    second_up = (1, 1, 1, 1, 1, 1, -1)        # |delta_7|=5

    first_shells = _shell_history(first_down, first_up)
    second_shells = _shell_history(second_down, second_up)
    assert first_shells[-1] == second_shells[-1]
    assert first_shells != second_shells
    assert reconstruct_unordered_drift_history(first_shells)[-1] == (1, 7)
    assert reconstruct_unordered_drift_history(second_shells)[-1] == (5, 5)


def test_path_total_history_does_not_recover_coordination_history() -> None:
    # FCC-like constant drift and HCP-like alternating drift share T_0,T_1,T_2
    # but have different S_2.
    fcc_shells = (1, 12, 42)
    hcp_shells = (1, 12, 44)
    fcc_paths = tuple(
        geodesic_total_from_coordination_history(fcc_shells[: radius + 1])
        for radius in range(3)
    )
    hcp_paths = tuple(
        geodesic_total_from_coordination_history(hcp_shells[: radius + 1])
        for radius in range(3)
    )
    assert fcc_paths == hcp_paths == (1, 12, 84)
    assert fcc_shells != hcp_shells
