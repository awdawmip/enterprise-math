from enterprise_math.p017_p018_walsh_euclidean_descent import (
    euclidean_boundary_column,
    euclidean_child_scale,
)


def test_repeatable_parent_conductor_descends_strictly_to_child_single_use():
    data = euclidean_child_scale(46, 15)
    assert data["positive_odd_radius_count_H"] == 23
    assert data["complete_q_blocks_A"] == 1
    assert data["boundary_prefix_h"] == 8
    assert data["child_scale_k_prime"] == 16
    assert data["strict_scale_contraction"] is True
    assert data["child_conductor_single_use"] is True


def test_small_remainder_can_collapse_to_tiny_child_scale():
    data = euclidean_child_scale(46, 21)
    assert data["boundary_prefix_h"] == 2
    assert data["child_scale_k_prime"] == 4
    assert data["child_conductor_single_use"] is True


def test_parent_boundary_column_equals_child_column_exactly():
    for k, primes in ((46, (3, 5)), (46, (3, 7)), (82, (3, 5))):
        data = euclidean_boundary_column(k, primes)
        assert data["euclidean_boundary_descent_identity"] is True
        assert data["parent_raw_signed_column"] == data["child_raw_signed_column"]
        assert all(row["signed_sum"] == 0 for row in data["complete_block_rows"])


def test_already_single_use_parent_needs_no_strict_descent():
    data = euclidean_child_scale(46, 35)
    assert data["complete_q_blocks_A"] == 0
    assert data["child_scale_k_prime"] == 46
    assert data["strict_scale_contraction"] is False
    assert data["child_conductor_single_use"] is True
