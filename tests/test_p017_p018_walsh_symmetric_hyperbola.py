from fractions import Fraction

from enterprise_math.p017_p018_walsh_symmetric_hyperbola import (
    fixed_total_conductor_parity,
    hyperbola_floor_classification,
    symmetric_hyperbola_point,
)


def test_physical_symmetric_detector_equals_hyperbola_expansion():
    for k in (17, 46, 82):
        checked = 0
        for radius in range(1, k):
            try:
                data = symmetric_hyperbola_point(k, radius)
            except ValueError:
                continue
            assert data["hyperbola_identity"] is True
            assert data["direct_symmetric_detector"] == data["expanded_symmetric_detector"]
            checked += 1
        assert checked > 0


def test_both_high_divisor_quadrant_has_zero_coefficient():
    # C_46=22; 23 and 29 are both above the reusable-floor cutoff.
    data = hyperbola_floor_classification(46, 23, 29)
    assert data["both_high_quadrant_compiled_away"] is True
    assert data["symmetric_hyperbola_coefficient"] == Fraction(0, 1)
    assert data["retained_by_compiler"] is False


def test_floor_reuse_is_controlled_by_product_hyperbola():
    # C_100=49.  The pair (3,5) can repeat at anchor a=1, while (7,11) cannot.
    low = hyperbola_floor_classification(100, 3, 5)
    high = hyperbola_floor_classification(100, 7, 11)
    assert low["floor_reusable_product_hyperbola"] is True
    assert high["floor_reusable_product_hyperbola"] is False
    assert high["boundary_only_by_product"] is True


def test_odd_total_support_vanishes_pointwise_below_product_cutoff():
    # C_1000=499; 3*5*7=105 fits and has odd support degree.
    data = fixed_total_conductor_parity(1000, (3, 5, 7))
    assert data["odd_degree_pointwise_zero"] is True
    assert all(row["coefficient"] == 0 for row in data["rows"])


def test_even_total_support_has_mobius_split_coefficients_and_zero_complete_bulk():
    # C_100=49; q=15 is an even-support reusable conductor.
    data = fixed_total_conductor_parity(100, (3, 5))
    assert data["odd_degree_pointwise_zero"] is False
    assert data["zero_complete_split_bulk"] is True
    coefficients = {row["lower_divisor"]: row["coefficient"] for row in data["rows"]}
    assert coefficients == {1: 1, 3: -1, 5: -1, 15: 1}
