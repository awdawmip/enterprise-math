from fractions import Fraction
from itertools import product

from enterprise_math.abc_merged_rank_path_generator import (
    area_from_merged_rank_path,
    merged_rank_path,
    quadratic_energy_from_merged_rank_path,
)
from enterprise_math.abc_quadratic_history_closure import (
    direct_quadratic_energy,
    evaluate_quadratic_energy_jet,
    quadratic_energy_jet,
)
from enterprise_math.abc_two_step_history import activation_area
from enterprise_math.abc_signed_exponent_transport import dyadic_difference_pressure_tower


def test_common_rank_path_generates_area_and_energy() -> None:
    thresholds = (Fraction(1, 4), Fraction(1, 1))
    current = (Fraction(1, 2), Fraction(3, 2))
    candidates = (Fraction(3, 4), Fraction(2, 1))
    futures = (Fraction(2, 1), Fraction(3, 1))
    path = merged_rank_path(thresholds, current, candidates, futures)
    jet = quadratic_energy_jet(thresholds, current, candidates, futures)
    for x in product((0, 1), repeat=2):
        for y in product((0, 1), repeat=2):
            assert quadratic_energy_from_merged_rank_path(path, x, y) == evaluate_quadratic_energy_jet(jet, x, y)
            assert quadratic_energy_from_merged_rank_path(path, x, y) == direct_quadratic_energy(
                thresholds, current, candidates, futures, x, y
            )


def test_path_is_monotone_and_compresses_incidence_bits() -> None:
    path = merged_rank_path(
        (Fraction(1, 4), Fraction(1, 1)),
        (Fraction(1, 2), Fraction(3, 2)),
        (Fraction(3, 4), Fraction(2, 1)),
        (Fraction(2, 1), Fraction(3, 1)),
    )
    assert path.full_rank_path == tuple(sorted(path.full_rank_path))
    assert path.compatible_path_count < path.unconstrained_incidence_count


def test_area_from_common_path_matches_direct_final_grid() -> None:
    thresholds = (Fraction(1, 2), Fraction(2, 1))
    current = (Fraction(3, 4), Fraction(3, 2))
    candidates = (Fraction(1, 1), Fraction(3, 1))
    futures = (Fraction(5, 2), Fraction(4, 1))
    path = merged_rank_path(thresholds, current, candidates, futures)
    x = (1, 0)
    y = (1, 1)
    final_thresholds = tuple(sorted((*thresholds, candidates[0])))
    final_values = (*current, *futures)
    assert area_from_merged_rank_path(path, x, y) == activation_area(final_thresholds, final_values)


def test_exact_arithmetic_path_generates_stage108_cubic_fixture() -> None:
    pressures = dyadic_difference_pressure_tower(3, 41, 2, 1).pressures
    path = merged_rank_path(
        (),
        pressures[:1],
        (Fraction(1, 10), Fraction(1, 2)),
        pressures[1:],
    )
    assert path.full_rank_path == (0, 2)
    assert quadratic_energy_from_merged_rank_path(path, (1, 1), (1,)) == 4
    assert quadratic_energy_from_merged_rank_path(path, (1, 0), (1,)) == 1
