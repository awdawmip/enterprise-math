from enterprise_math.p017_p018_square_covering_height import (
    bertrand_survivor_below_sqrt_y,
    bounded_common_root_minimum_sign_lift,
    bounded_square_covering_height,
    is_fixed_y_square_covering_root,
)


def test_bertrand_floor_exhibits_survivor_below_sqrt_cutoff():
    for y in range(3, 31):
        for x in range(1, y + 1):
            if x * x >= y:
                break
            data = bertrand_survivor_below_sqrt_y(x, y)
            assert data["rules_out_cover"] is True
            assert not is_fixed_y_square_covering_root(x, y)


def test_no_diagonal_or_subdiagonal_covering_root_for_small_verified_scales():
    for y in range(2, 31):
        data = bounded_square_covering_height(y, y)
        assert data["no_covering_root_in_search"] is True
        assert data["first_covering_root_in_search"] is None


def test_legacy_y73_covering_phase_has_an_enormous_minimum_sign_lift():
    data = bounded_common_root_minimum_sign_lift()
    assert data["y"] == 73
    assert data["orbit_size"] == 2**17
    assert data["minimum_positive_sign_lift"] == 54983378811556946852865
    assert data["minimum_over_y_ratio"] > 10**20
    assert data["minimum_over_floor_sqrt_wheel_ratio"] > 10**8
    assert data["full_cover_verified"] is True
    assert data["not_a_global_h_y_minimality_claim"] is True
