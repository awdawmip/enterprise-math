from itertools import product

from enterprise_math.p022_barlow_distance_gauge import (
    barlow_endpoint_distance,
    barlow_endpoint_distance_from_imbalance,
    barlow_layer_shell_contains_from_imbalance,
    drifted_hex_required_radius,
)
from enterprise_math.p022_barlow_stacking import (
    barlow_shell,
    stacking_prefix_imbalance,
)


def test_gauge_shell_matches_direct_barlow_shell_for_all_short_patterns() -> None:
    for period in range(1, 5):
        for pattern in product((-1, 1), repeat=period):
            pattern = tuple(pattern)
            for radius in range(0, 6):
                direct = set(barlow_shell(radius, pattern))
                reconstructed = set()
                bound = 2 * radius
                for layer in range(-radius, radius + 1):
                    imbalance = stacking_prefix_imbalance(pattern, layer)
                    for x in range(-bound, bound + 1):
                        for y in range(-bound, bound + 1):
                            if barlow_layer_shell_contains_from_imbalance(
                                radius, x, y, layer, imbalance
                            ):
                                reconstructed.add((x, y, layer))
                assert reconstructed == direct


def test_distance_function_depends_only_on_selected_layer_signed_imbalance() -> None:
    first = (-1, -1, 1)
    second = (-1, 1, -1)
    layer = 3
    assert stacking_prefix_imbalance(first, layer) == stacking_prefix_imbalance(
        second, layer
    ) == -1

    for x in range(-8, 9):
        for y in range(-8, 9):
            assert barlow_endpoint_distance(
                x, y, layer, first
            ) == barlow_endpoint_distance(x, y, layer, second)


def test_opposite_signed_drift_is_exact_horizontal_reflection() -> None:
    for layer in range(0, 9):
        for imbalance in range(-layer, layer + 1, 2):
            for x in range(-8, 9):
                for y in range(-8, 9):
                    assert barlow_endpoint_distance_from_imbalance(
                        x, y, layer, imbalance
                    ) == barlow_endpoint_distance_from_imbalance(
                        -x, -y, layer, -imbalance
                    )


def test_zero_drift_reduces_to_triangular_hex_radius() -> None:
    for x in range(-8, 9):
        for y in range(-8, 9):
            assert drifted_hex_required_radius(x, y, 0) == max(
                abs(x), abs(y), abs(x + y)
            )


def test_vertical_support_is_exact_zero_extra_horizontal_region() -> None:
    for layer in range(0, 9):
        for imbalance in range(-layer, layer + 1, 2):
            paired = (layer - abs(imbalance)) // 2
            for x in range(-10, 11):
                for y in range(-10, 11):
                    distance = barlow_endpoint_distance_from_imbalance(
                        x, y, layer, imbalance
                    )
                    assert (distance == layer) == (
                        drifted_hex_required_radius(x, y, imbalance) <= paired
                    )
