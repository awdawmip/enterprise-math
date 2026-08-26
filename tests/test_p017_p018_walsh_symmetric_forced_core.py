from enterprise_math.p017_p018_walsh_symmetric_forced_core import (
    forced_partition_count,
    forced_symmetric_root_pattern,
)


def test_two_reusable_blocks_force_even_nonzero_and_odd_zero_coefficients():
    even = forced_symmetric_root_pattern(46, (3,), (5,))
    assert even["coefficient_forced"] is True
    assert even["total_selected_degree"] == 2
    assert even["forced_coefficient_magnitude"] == 1
    assert even["even_degree_forced_nonzero"] is True

    odd = forced_symmetric_root_pattern(46, (3, 5), (7,))
    # lower radical 15 and upper radical 7 are both <= C_46=22.
    assert odd["coefficient_forced"] is True
    assert odd["total_selected_degree"] == 3
    assert odd["forced_symmetric_coefficient"] == 0
    assert odd["odd_degree_forced_zero"] is True


def test_any_pattern_above_C_squared_has_no_irreducible_nonzero_coefficient():
    # C_46=22 and 3*5*7*11=1155 > 22^2=484.
    data = forced_partition_count(46, (3, 5, 7, 11))
    assert data["selected_conductor"] == 1155
    assert data["forced_symmetric_conductor_horizon"] == 484
    assert data["forced_nonzero_root_patterns"] == 0
    assert data["free_tail_root_patterns"] > 0


def test_even_union_below_C_squared_can_have_irreducible_root_patterns():
    data = forced_partition_count(46, (3, 5, 7))
    # Degree three is odd, so forced low-low patterns cancel even though the product is small.
    assert data["selected_degree"] == 3
    assert data["forced_nonzero_root_patterns"] == 0
    assert data["forced_zero_root_patterns"] > 0

    pair = forced_partition_count(46, (3, 5))
    assert pair["selected_degree"] == 2
    assert pair["forced_nonzero_root_patterns"] == 4
    assert pair["free_tail_root_patterns"] == 0
