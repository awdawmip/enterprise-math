from enterprise_math.p022_barlow_observables import (
    layer_resolved_multiplicity_spectrum,
    layer_spectrum_forgets_to_global,
    rooted_shell_path_count_function,
    shell_cardinality,
    shell_multiplicity_spectrum,
    shell_total_geodesic_count,
    spectrum_recovers_cardinality,
    spectrum_recovers_total_geodesic_count,
)

FCC = (-1,)
HCP = (-1, 1)


def test_spectrum_recovers_cardinality_and_total_path_count() -> None:
    patterns = (FCC, HCP, (-1, -1, 1), (-1, 1, -1), (-1, -1, -1, 1, -1))
    for pattern in patterns:
        for radius in range(0, 5):
            spectrum = shell_multiplicity_spectrum(radius, pattern)
            assert spectrum_recovers_cardinality(spectrum) == shell_cardinality(
                radius, pattern
            )
            assert spectrum_recovers_total_geodesic_count(
                spectrum
            ) == shell_total_geodesic_count(radius, pattern)


def test_cardinality_does_not_determine_total_geodesic_count() -> None:
    first = (-1, -1, 1)
    second = (-1, 1, -1)
    radius = 3
    assert shell_cardinality(radius, first) == shell_cardinality(radius, second) == 96
    assert shell_total_geodesic_count(radius, first) == 402
    assert shell_total_geodesic_count(radius, second) == 384


def test_total_geodesic_count_does_not_determine_cardinality() -> None:
    radius = 2
    assert shell_total_geodesic_count(radius, FCC) == shell_total_geodesic_count(
        radius, HCP
    ) == 84
    assert shell_cardinality(radius, FCC) == 42
    assert shell_cardinality(radius, HCP) == 44


def test_cardinality_plus_total_count_does_not_determine_multiplicity_spectrum() -> None:
    first = (-1, -1, -1, 1, -1)
    second = (-1, -1, 1, -1, 1)
    radius = 3

    assert (
        shell_cardinality(radius, first),
        shell_total_geodesic_count(radius, first),
    ) == (
        shell_cardinality(radius, second),
        shell_total_geodesic_count(radius, second),
    ) == (96, 390)

    assert shell_multiplicity_spectrum(radius, first) == (
        (1, 18),
        (3, 54),
        (6, 6),
        (9, 18),
    )
    assert shell_multiplicity_spectrum(radius, second) == (
        (1, 14),
        (2, 8),
        (3, 42),
        (5, 4),
        (6, 8),
        (9, 20),
    )


def test_global_multiplicity_spectrum_does_not_determine_layer_resolved_spectrum() -> None:
    first = (-1, -1, -1, 1)
    second = (-1, 1, -1, 1)
    radius = 2

    assert shell_multiplicity_spectrum(radius, first) == shell_multiplicity_spectrum(
        radius, second
    ) == (
        (1, 18),
        (2, 18),
        (3, 2),
        (4, 6),
    )

    first_layers = layer_resolved_multiplicity_spectrum(radius, first)
    second_layers = layer_resolved_multiplicity_spectrum(radius, second)
    assert first_layers != second_layers
    assert layer_spectrum_forgets_to_global(first_layers) == layer_spectrum_forgets_to_global(
        second_layers
    )


def test_layer_resolved_spectrum_still_forgets_coordinate_labels() -> None:
    # A coordinate-labelled shell function contains enough information to
    # produce the layer-resolved spectrum, but sorting into histograms erases
    # endpoint identity.  Two reflected constant-drift stackings are the
    # simplest exact witness of that loss in the fixed axial chart.
    first = (-1,)
    second = (1,)
    radius = 2

    assert layer_resolved_multiplicity_spectrum(
        radius, first
    ) == layer_resolved_multiplicity_spectrum(radius, second)
    assert rooted_shell_path_count_function(
        radius, first
    ) != rooted_shell_path_count_function(radius, second)
