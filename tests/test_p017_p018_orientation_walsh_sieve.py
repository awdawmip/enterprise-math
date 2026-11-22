from enterprise_math.p017_p018_orientation_walsh_sieve import (
    orientation_signed_root_fiber,
    orientation_walsh_point,
    orientation_walsh_profile,
)


def test_point_endpoints_are_exact_opposite_side_weighted_prime_detectors():
    for k in (8, 17, 46):
        for radius in range(1, k):
            try:
                data = orientation_walsh_point(k, radius)
            except ValueError:
                continue
            coefficients = data["walsh_coefficients"]
            assert sum(coefficients) == data["upper_prime_weight_W_plus_one"]
            assert sum(((-1) ** j) * value for j, value in enumerate(coefficients)) == (
                data["lower_prime_weight_W_minus_one"]
            )
            assert (
                data["upper_prime_weight_W_plus_one"]
                + data["lower_prime_weight_W_minus_one"]
                > 0
            ) == data["at_least_one_prime_side"]


def test_global_even_signed_levels_reconstruct_weighted_prime_side_observable():
    expected = {
        46: {
            "surviving": 22,
            "levels": (22, -5, 1, 5, -1),
            "weighted": 44,
        },
        82: {
            "surviving": 40,
            "levels": (40, -3, 5, 14, -2, 1),
            "weighted": 86,
        },
    }
    for k, row in expected.items():
        data = orientation_walsh_profile(k)
        assert data["surviving_radius_count"] == row["surviving"]
        assert data["signed_levels"] == row["levels"]
        assert data["weighted_prime_side_observable"] == row["weighted"]
        assert data["weighted_prime_side_observable"] == 2 * sum(
            data["signed_levels"][degree]
            for degree in range(0, len(data["signed_levels"]), 2)
        )
        assert data["prime_mirror_side_exists"] is True


def test_nonempty_signed_root_columns_have_zero_floor_bulk_after_anchor_mobius():
    for selected in ((3,), (3, 5), (3, 5, 7), (5, 7, 11)):
        data = orientation_signed_root_fiber(46, selected)
        assert data["floor_bulk_exactly_zero"] is True
        assert data["mobius_root_exact_sum"] == data["direct_signed_fiber"]
        assert data["mobius_boundary_only_sum"] == data["direct_signed_fiber"]


def test_anchor_free_and_anchored_scales_both_use_boundary_only_columns():
    # k=16 has no effective odd anchor; k=46 has the effective odd anchor 23.
    anchor_free = orientation_signed_root_fiber(16, (3, 5))
    anchored = orientation_signed_root_fiber(46, (3, 5))
    assert anchor_free["effective_odd_anchors"] == ()
    assert anchored["effective_odd_anchors"] == (23,)
    assert anchor_free["floor_bulk_exactly_zero"] is True
    assert anchored["floor_bulk_exactly_zero"] is True
