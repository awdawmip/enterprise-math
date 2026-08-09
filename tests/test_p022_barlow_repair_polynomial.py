from collections import Counter
from itertools import product
from math import comb

from enterprise_math.p022_barlow_repair_polynomial import (
    collision_coefficients_from_repair_polynomial,
    coordination_history_image_size,
    coordination_history_image_size_closed,
    evaluate_repair_polynomial,
    maximum_fiber_microscopic_mass_fraction,
    maximum_repair_coefficient_closed,
    microscopic_domain_from_repair_polynomial,
    minimum_repair_coefficient_closed,
    repair_polynomial_coefficients,
    total_repair_load_from_polynomial,
)
from enterprise_math.p022_barlow_two_sided_repair import (
    two_sided_microscopic_fiber_size,
    two_sided_repair_bit_count,
    unordered_absolute_pair_history,
)


def _words(length: int):
    return tuple(tuple(word) for word in product((-1, 1), repeat=length))


def _direct_history_fibers(length: int):
    fibers = {}
    words = _words(length)
    for left in words:
        for right in words:
            history = unordered_absolute_pair_history(left, right)
            fibers.setdefault(history, 0)
            fibers[history] += 1
    return fibers


def test_repair_polynomial_matches_direct_history_bit_distribution() -> None:
    for length in range(0, 7):
        direct = Counter()
        for history, fiber_size in _direct_history_fibers(length).items():
            repair = two_sided_repair_bit_count(history)
            assert fiber_size == 2 ** repair
            assert fiber_size == two_sided_microscopic_fiber_size(history)
            direct[repair] += 1

        coefficients = repair_polynomial_coefficients(length)
        reconstructed = Counter(
            {repair: count for repair, count in enumerate(coefficients) if count}
        )
        assert reconstructed == direct


def test_known_initial_repair_polynomials() -> None:
    assert repair_polynomial_coefficients(0) == (1,)
    assert repair_polynomial_coefficients(1) == (0, 0, 1)
    assert repair_polynomial_coefficients(2) == (0, 0, 2, 1)
    assert repair_polynomial_coefficients(3) == (0, 0, 2, 1, 3)
    assert repair_polynomial_coefficients(4) == (0, 0, 4, 6, 8, 2)


def test_closed_coordination_history_image_count_matches_weighted_chamber_recursion() -> None:
    expected = (1, 1, 3, 6, 20, 50, 175, 490, 1764, 5292, 19404)
    assert tuple(coordination_history_image_size(length) for length in range(11)) == expected
    for length in range(0, 25):
        assert coordination_history_image_size(length) == coordination_history_image_size_closed(
            length
        )


def test_repair_polynomial_at_two_reconstructs_all_microscopic_windows() -> None:
    for length in range(0, 20):
        coefficients = repair_polynomial_coefficients(length)
        assert evaluate_repair_polynomial(coefficients, 2) == 4 ** length
        assert microscopic_domain_from_repair_polynomial(length) == 4 ** length


def test_derivative_at_two_matches_total_event_repair_load() -> None:
    for length in range(0, 15):
        assert total_repair_load_from_polynomial(length) >= 0


def test_collision_coefficients_from_repair_profile_match_direct_fiber_counts() -> None:
    for length in range(0, 7):
        fibers = _direct_history_fibers(length)
        coefficients = collision_coefficients_from_repair_polynomial(
            repair_polynomial_coefficients(length)
        )
        for order, coefficient in enumerate(coefficients, start=1):
            direct = sum(
                comb(fiber_size, order)
                for fiber_size in fibers.values()
                if fiber_size >= order
            )
            assert coefficient == direct


def test_lowest_and_highest_nonzero_coefficients_match_closed_forms() -> None:
    for length in range(0, 30):
        coefficients = repair_polynomial_coefficients(length)
        if length == 0:
            assert coefficients == (1,)
            assert minimum_repair_coefficient_closed(length) == 1
            assert maximum_repair_coefficient_closed(length) == 1
            continue

        assert coefficients[2] == minimum_repair_coefficient_closed(length)
        assert len(coefficients) - 1 == length + 1
        assert coefficients[length + 1] == maximum_repair_coefficient_closed(length)


def test_maximum_fiber_microscopic_mass_fraction_has_closed_parity_forms() -> None:
    assert maximum_fiber_microscopic_mass_fraction(0) == (1, 1)
    for half in range(1, 15):
        even = 2 * half
        assert maximum_fiber_microscopic_mass_fraction(even) == (1, 2 ** half)

        odd = 2 * half + 1
        assert maximum_fiber_microscopic_mass_fraction(odd) == (
            3,
            2 ** (half + 1),
        )
