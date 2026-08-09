from itertools import product

from enterprise_math.p022_barlow_growth import (
    barlow_layer_shell_total_geodesic_paths,
    barlow_shell_total_geodesic_paths_closed,
    growth_constant_integer_equation,
    period_absolute_drift_data,
    period_drift,
)
from enterprise_math.p022_barlow_stacking import (
    barlow_geodesic_path_count,
    barlow_shell,
    barlow_shell_total_geodesic_paths,
)
from enterprise_math.p022_geodesic_multiplicity import a3_shell_total_geodesic_paths
from enterprise_math.p022_hcp_geometry import hcp_shell_total_geodesic_paths_closed

FCC = (-1,)
HCP = (-1, 1)


def test_layer_formula_matches_direct_endpoint_sum_for_all_short_periods() -> None:
    # Every ± pattern of period <=4, every shell through radius five, every
    # target layer in that shell.  This is a geometry-level cross-check of the
    # exposed-face formula, not just a whole-shell identity.
    for period in range(1, 5):
        for pattern in product((-1, 1), repeat=period):
            pattern = tuple(pattern)
            for radius in range(0, 6):
                shell = barlow_shell(radius, pattern)
                for layer in range(-radius, radius + 1):
                    direct = sum(
                        barlow_geodesic_path_count(point, pattern)
                        for point in shell
                        if point[2] == layer
                    )
                    assert barlow_layer_shell_total_geodesic_paths(
                        radius, layer, pattern
                    ) == direct


def test_whole_shell_closed_formula_matches_direct_enumeration() -> None:
    for period in range(1, 5):
        for pattern in product((-1, 1), repeat=period):
            pattern = tuple(pattern)
            for radius in range(0, 7):
                assert barlow_shell_total_geodesic_paths_closed(
                    radius, pattern
                ) == barlow_shell_total_geodesic_paths(radius, pattern)


def test_fcc_and_hcp_specializations_recover_existing_formulas() -> None:
    for radius in range(0, 8):
        assert barlow_shell_total_geodesic_paths_closed(
            radius, FCC
        ) == a3_shell_total_geodesic_paths(radius)
        assert barlow_shell_total_geodesic_paths_closed(
            radius, HCP
        ) == hcp_shell_total_geodesic_paths_closed(radius)


def test_period_drift_and_integer_growth_equations() -> None:
    assert period_drift(FCC) == -1
    assert period_absolute_drift_data(FCC) == (1, 1)
    assert growth_constant_integer_equation(FCC) == (2, 4)
    # (lambda-2)^2=4 -> lambda=4.

    assert period_drift(HCP) == 0
    assert period_absolute_drift_data(HCP) == (0, 2)
    assert growth_constant_integer_equation(HCP) == (4, 4)
    # (lambda-2)^4=4 -> lambda=2+sqrt(2).

    assert period_absolute_drift_data((-1, -1, 1)) == (1, 3)
    assert growth_constant_integer_equation((-1, -1, 1)) == (6, 16)
    # lambda=2+2^(2/3).

    assert period_absolute_drift_data((-1, -1, -1, 1)) == (2, 4)
    assert growth_constant_integer_equation((-1, -1, -1, 1)) == (8, 64)
    # lambda=2+2^(3/4).


def test_same_period_length_and_absolute_drift_need_not_have_same_finite_shells() -> None:
    # This preserves the exact boundary of the asymptotic theorem: finite
    # shells still read the prefix-imbalance trajectory within the period.
    alternating = (-1, 1, -1, 1)
    clustered = (-1, -1, 1, 1)
    assert period_absolute_drift_data(alternating) == period_absolute_drift_data(
        clustered
    ) == (0, 4)

    finite_difference_seen = any(
        barlow_shell_total_geodesic_paths_closed(radius, alternating)
        != barlow_shell_total_geodesic_paths_closed(radius, clustered)
        for radius in range(1, 8)
    )
    assert finite_difference_seen

    # But the exact algebraic growth equation is the same because only the
    # long-run drift density enters the exponential rate.
    assert growth_constant_integer_equation(
        alternating
    ) == growth_constant_integer_equation(clustered) == (8, 16)
