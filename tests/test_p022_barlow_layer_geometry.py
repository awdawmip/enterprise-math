from itertools import product

from enterprise_math.p022_barlow_layer_geometry import (
    anisotropy_from_side_lengths,
    layer_ball_vertex_count,
    layer_boundary_side_multiset,
    layer_effective_perimeter_parameter,
    layer_hex_side_lengths,
    layer_shell_vertex_count,
)
from enterprise_math.p022_barlow_stacking import (
    barlow_shell,
    stacking_prefix_imbalance,
)


def test_layer_ball_and_shell_counts_match_direct_barlow_enumeration() -> None:
    for period in range(1, 5):
        for pattern in product((-1, 1), repeat=period):
            pattern = tuple(pattern)
            accumulated = set()
            for radius in range(0, 6):
                shell = set(barlow_shell(radius, pattern))
                accumulated.update(shell)
                for layer in range(-radius, radius + 1):
                    imbalance = stacking_prefix_imbalance(pattern, layer)
                    direct_shell = sum(1 for point in shell if point[2] == layer)
                    direct_ball = sum(
                        1 for point in accumulated if point[2] == layer
                    )
                    assert layer_shell_vertex_count(
                        radius, layer, imbalance
                    ) == direct_shell
                    assert layer_ball_vertex_count(
                        radius, layer, imbalance
                    ) == direct_ball


def test_alternating_side_lengths_encode_absolute_drift() -> None:
    for radius in range(0, 12):
        for layer in range(-radius, radius + 1):
            vertical = abs(layer)
            for imbalance in range(-vertical, vertical + 1, 2):
                short, long = layer_hex_side_lengths(
                    radius, layer, imbalance
                )
                assert short <= long
                assert long - short == abs(imbalance)
                assert anisotropy_from_side_lengths(short, long) == abs(
                    imbalance
                )
                assert short + long == layer_effective_perimeter_parameter(
                    radius, layer, imbalance
                ) == 2 * radius - vertical
                assert layer_boundary_side_multiset(
                    radius, layer, imbalance
                ) == (short, long, short, long, short, long)


def test_nonextreme_shell_slice_is_boundary_length_independent_of_anisotropy() -> None:
    for radius in range(1, 20):
        for layer in range(-radius + 1, radius):
            vertical = abs(layer)
            expected = 3 * (2 * radius - vertical)
            values = {
                layer_shell_vertex_count(radius, layer, imbalance)
                for imbalance in range(-vertical, vertical + 1, 2)
            }
            assert values == {expected}


def test_ball_slice_cardinality_distinguishes_absolute_drift() -> None:
    for radius in range(1, 12):
        for layer in range(-radius, radius + 1):
            vertical = abs(layer)
            counts = {}
            for imbalance in range(-vertical, vertical + 1, 2):
                count = layer_ball_vertex_count(radius, layer, imbalance)
                counts.setdefault(abs(imbalance), count)
                assert counts[abs(imbalance)] == count
            # The formula is strictly decreasing in d^2 over represented d>=0.
            ordered = sorted(counts.items())
            assert all(
                ordered[index][1] > ordered[index + 1][1]
                for index in range(len(ordered) - 1)
            )
