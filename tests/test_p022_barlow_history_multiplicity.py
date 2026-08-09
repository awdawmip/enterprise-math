from itertools import product

from enterprise_math.p022_barlow_coordination import (
    barlow_shell_vertex_count_from_extreme_imbalances,
)
from enterprise_math.p022_barlow_history_multiplicity import (
    global_multiplicity_spectrum_from_coordination_history,
    layer_geodesic_multiplicity_spectrum,
    spectrum_shell_cardinality,
    spectrum_total_geodesic_paths,
)
from enterprise_math.p022_barlow_stacking import (
    barlow_shell_multiplicity_spectrum,
    barlow_shell_total_geodesic_paths,
    stacking_prefix_imbalance,
)

FCC = (-1,)
HCP = (-1, 1)


def _shell_history(pattern, radius: int) -> tuple[int, ...]:
    output = [1]
    for current in range(1, radius + 1):
        positive = stacking_prefix_imbalance(pattern, current)
        negative = stacking_prefix_imbalance(pattern, -current)
        output.append(
            barlow_shell_vertex_count_from_extreme_imbalances(
                current, positive, negative
            )
        )
    return tuple(output)


def test_layer_spectrum_depends_only_on_height_and_absolute_drift() -> None:
    # Literal prefix order is irrelevant; the canonical representative in the
    # implementation is checked against all short actual prefix words by using
    # them as one-period stackings and comparing the target positive layer.
    for height in range(0, 6):
        for word in product((-1, 1), repeat=height):
            pattern = tuple(word) if word else (1,)
            drift = abs(sum(word))
            for radius in range(height, 6):
                expected = {}
                # Filter the actual shell spectrum down to the selected layer.
                # We compute it by direct endpoint queries through the public
                # whole-shell function using a one-prefix-period pattern.
                from enterprise_math.p022_barlow_stacking import (
                    barlow_distance_and_geodesic_count,
                )

                for first in range(-radius, radius + 1):
                    for second in range(-radius, radius + 1):
                        distance, multiplicity = barlow_distance_and_geodesic_count(
                            (first, second, height), pattern
                        )
                        if distance == radius:
                            expected[multiplicity] = expected.get(multiplicity, 0) + 1
                assert layer_geodesic_multiplicity_spectrum(
                    radius, height, drift
                ) == tuple(sorted(expected.items()))


def test_coordination_history_reconstructs_global_spectrum_for_short_periods() -> None:
    for period in range(1, 5):
        for pattern in product((-1, 1), repeat=period):
            pattern = tuple(pattern)
            for radius in range(0, 5):
                history = _shell_history(pattern, radius)
                reconstructed = global_multiplicity_spectrum_from_coordination_history(
                    history
                )
                direct = barlow_shell_multiplicity_spectrum(radius, pattern)
                assert reconstructed == direct
                assert spectrum_shell_cardinality(reconstructed) == history[-1]
                assert spectrum_total_geodesic_paths(
                    reconstructed
                ) == barlow_shell_total_geodesic_paths(radius, pattern)


def test_path_total_history_does_not_determine_global_spectrum() -> None:
    # FCC and HCP agree on T_0,T_1,T_2=(1,12,84) but already have distinct
    # radius-two multiplicity spectra.
    fcc_history = _shell_history(FCC, 2)
    hcp_history = _shell_history(HCP, 2)
    fcc_spectrum = global_multiplicity_spectrum_from_coordination_history(
        fcc_history
    )
    hcp_spectrum = global_multiplicity_spectrum_from_coordination_history(
        hcp_history
    )
    assert spectrum_total_geodesic_paths(fcc_spectrum) == 84
    assert spectrum_total_geodesic_paths(hcp_spectrum) == 84
    assert fcc_spectrum == ((1, 12), (2, 24), (4, 6))
    assert hcp_spectrum == ((1, 18), (2, 18), (3, 2), (4, 6))
    assert fcc_spectrum != hcp_spectrum
