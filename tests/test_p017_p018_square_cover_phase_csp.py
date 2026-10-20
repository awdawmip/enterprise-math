from enterprise_math.p017_p018_square_cover_phase_csp import (
    exhaustive_phase_feasibility_small_y,
    verify_square_cover_phase,
    y73_square_cover_phase_certificate,
    Y73_PHASE_CERTIFICATE,
)


def test_small_negative_square_phase_spaces_are_infeasible_through_13():
    for y in range(2, 14):
        data = exhaustive_phase_feasibility_small_y(y)
        assert data["feasible"] is False
        assert data["witness"] is None


def test_y73_explicit_phase_is_a_complete_negative_square_cover():
    data = verify_square_cover_phase(73, Y73_PHASE_CERTIFICATE)
    assert data["covers_full_horizon"] is True
    assert data["first_uncovered_offset"] is None
    assert len(data["covering_witnesses"]) == 146


def test_y73_phase_minimum_sign_lift_remains_far_above_the_diagonal():
    data = y73_square_cover_phase_certificate()
    assert data["phase_feasibility_verified"] is True
    assert data["root_class_count"] == 2**17
    assert data["minimum_positive_sign_lift"] == 627431388493620297650
    assert data["covering_height_upper_bound"] > 73
    assert data["minimum_over_diagonal_ratio"] > 10**18
    assert data["not_first_feasible_y_claim"] is True
    assert data["not_global_h73_minimality_claim"] is True
