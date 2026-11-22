from enterprise_math.p017_p018_square_lift_height import (
    prove_height_gap_for_residue,
    square_phase_lift_height_gap,
)


def test_distinguished_root_is_least_positive_once_primorial_exceeds_k_squared():
    for k, cutoff in ((5, 5), (7, 7), (10, 11), (13, 13)):
        data = square_phase_lift_height_gap(k, cutoff)
        assert data["primorial_exceeds_k_squared"] is True
        assert data["least_positive_lift"] == k
        assert data["height_gap_verified"] is True
        assert all(
            x >= data["nontrivial_lift_lower_bound"]
            for x in data["nontrivial_positive_lifts"]
        )


def test_nontrivial_sign_lifts_jump_beyond_square_root_of_primorial_scale():
    data = square_phase_lift_height_gap(7, 11)
    bound = data["nontrivial_lift_lower_bound"]
    for x in data["nontrivial_positive_lifts"]:
        result = prove_height_gap_for_residue(x, 7, 11)
        assert result["distinguished"] is False
        assert x >= bound


def test_distinguished_root_passes_height_gap_directly():
    data = prove_height_gap_for_residue(7, 7, 7)
    assert data["distinguished"] is True
    assert data["height_gap_verified"] is True
