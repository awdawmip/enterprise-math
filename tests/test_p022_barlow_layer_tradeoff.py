from itertools import product

from enterprise_math.p022_barlow_layer_tradeoff import (
    average_shell_multiplicity,
    layer_ball_slice_count,
    layer_shell_geodesic_total,
    layer_shell_vertex_count,
    next_drift_geodesic_gain,
    next_drift_vertex_loss,
)
from enterprise_math.p022_barlow_stacking import (
    barlow_geodesic_path_count,
    barlow_shell,
    stacking_prefix_imbalance,
)


def test_layer_geodesic_total_matches_direct_endpoint_sum() -> None:
    for period in range(1, 5):
        for pattern in product((-1, 1), repeat=period):
            pattern = tuple(pattern)
            for radius in range(0, 6):
                shell = barlow_shell(radius, pattern)
                for layer in range(-radius, radius + 1):
                    height = abs(layer)
                    drift = abs(stacking_prefix_imbalance(pattern, layer))
                    direct = sum(
                        barlow_geodesic_path_count(point, pattern)
                        for point in shell
                        if point[2] == layer
                    )
                    assert layer_shell_geodesic_total(
                        radius, height, drift
                    ) == direct


def test_drift_step_loses_exactly_d_plus_one_ball_vertices() -> None:
    for radius in range(1, 20):
        for height in range(0, radius + 1):
            drifts = tuple(range(height % 2, height + 1, 2))
            for drift in drifts[:-1]:
                assert next_drift_vertex_loss(
                    radius, height, drift
                ) == drift + 1


def test_nonextreme_drift_step_strictly_increases_geodesic_total() -> None:
    for radius in range(2, 15):
        for height in range(0, radius):
            drifts = tuple(range(height % 2, height + 1, 2))
            values = [
                layer_shell_geodesic_total(radius, height, drift)
                for drift in drifts
            ]
            assert all(
                values[index] < values[index + 1]
                for index in range(len(values) - 1)
            )
            for drift in drifts[:-1]:
                assert next_drift_geodesic_gain(radius, height, drift) == (
                    layer_shell_geodesic_total(radius, height, drift + 2)
                    - layer_shell_geodesic_total(radius, height, drift)
                )


def test_nonextreme_shell_vertex_count_is_fixed_while_ball_slice_shrinks() -> None:
    for radius in range(2, 15):
        for height in range(0, radius):
            shell_vertices = layer_shell_vertex_count(radius, height)
            assert shell_vertices == 3 * (2 * radius - height)
            drifts = tuple(range(height % 2, height + 1, 2))
            ball_values = [
                layer_ball_slice_count(radius, height, drift)
                for drift in drifts
            ]
            assert all(
                ball_values[index] > ball_values[index + 1]
                for index in range(len(ball_values) - 1)
            )


def test_extreme_layer_total_path_count_is_drift_independent() -> None:
    for radius in range(1, 20):
        values = {
            layer_shell_geodesic_total(radius, radius, drift)
            for drift in range(radius % 2, radius + 1, 2)
        }
        assert values == {3 ** radius}


def test_average_shell_multiplicity_strictly_increases_with_drift_nonextreme() -> None:
    for radius in range(2, 12):
        for height in range(0, radius):
            fractions = [
                average_shell_multiplicity(radius, height, drift)
                for drift in range(height % 2, height + 1, 2)
            ]
            for (left_num, left_den), (right_num, right_den) in zip(
                fractions, fractions[1:]
            ):
                assert left_num * right_den < right_num * left_den
