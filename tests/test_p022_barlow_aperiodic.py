from itertools import product

from enterprise_math.p022_barlow_aperiodic import (
    imbalance_trajectory_from_interface_windows,
    layer_shell_total_from_imbalance,
    shell_total_from_imbalance_trajectory,
)
from enterprise_math.p022_barlow_growth import (
    barlow_layer_shell_total_geodesic_paths,
    barlow_shell_total_geodesic_paths_closed,
)
from enterprise_math.p022_barlow_stacking import stacking_prefix_imbalance


def test_periodic_specialization_factors_through_finite_imbalance_trajectory() -> None:
    for period in range(1, 5):
        for pattern in product((-1, 1), repeat=period):
            pattern = tuple(pattern)
            for radius in range(0, 8):
                trajectory = tuple(
                    stacking_prefix_imbalance(pattern, layer)
                    for layer in range(-radius, radius + 1)
                )
                assert shell_total_from_imbalance_trajectory(
                    radius, trajectory
                ) == barlow_shell_total_geodesic_paths_closed(radius, pattern)

                for layer, imbalance in zip(
                    range(-radius, radius + 1), trajectory, strict=True
                ):
                    assert layer_shell_total_from_imbalance(
                        radius, layer, imbalance
                    ) == barlow_layer_shell_total_geodesic_paths(
                        radius, layer, pattern
                    )


def test_two_sided_interface_windows_build_expected_trajectory() -> None:
    downward_upward = (-1, 1, 1, -1)
    upward = (1, 1, -1, 1)
    trajectory = imbalance_trajectory_from_interface_windows(
        downward_upward, upward
    )
    # Downward effective signs are the negatives of the listed upward
    # interface signs. Upward effective signs are listed directly.
    assert trajectory == (0, -1, 0, 1, 0, 1, 2, 1, 2)


def test_shell_total_reads_absolute_imbalance_not_sign() -> None:
    radius = 5
    first = (-1, -2, -1, 0, -1, 0, 1, 2, 1, 0, 1)
    second = tuple(-value for value in first)
    assert shell_total_from_imbalance_trajectory(
        radius, first
    ) == shell_total_from_imbalance_trajectory(radius, second)


def test_same_final_imbalance_does_not_determine_finite_shell() -> None:
    radius = 4
    # Both upward windows end with imbalance zero, but their intermediate
    # absolute trajectories differ. Mirror the same construction downward so
    # the whole-shell difference is driven only by intermediate precision.
    alternating = (-1, 1, -1, 1)
    clustered = (-1, -1, 1, 1)

    alt_traj = imbalance_trajectory_from_interface_windows(
        alternating, alternating
    )
    cluster_traj = imbalance_trajectory_from_interface_windows(
        clustered, clustered
    )

    assert alt_traj[0] == cluster_traj[0] == 0
    assert alt_traj[-1] == cluster_traj[-1] == 0
    assert alt_traj != cluster_traj
    assert shell_total_from_imbalance_trajectory(
        radius, alt_traj
    ) != shell_total_from_imbalance_trajectory(radius, cluster_traj)
