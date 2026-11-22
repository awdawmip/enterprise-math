from enterprise_math.p017_p018_walsh_mixed_farey import (
    mixed_farey_coordinates,
    mixed_farey_phase,
    pure_even_root_phases,
)


def test_mixed_root_is_determinant_one_farey_pair():
    data = mixed_farey_coordinates(5, 7)
    assert data["determinant_one"] is True
    assert 5 * data["inverse_a_mod_b"] - 7 * data["companion_t"] == 1
    assert data["signed_unity_root_u"] % 5 == 1
    assert data["signed_unity_root_u"] % 7 == 6


def test_mixed_root_phase_equals_sum_of_farey_neighbors():
    for a, b in ((3, 5), (5, 7), (7, 11), (15, 7)):
        for h in (1, 2, 5):
            data = mixed_farey_phase(46, a, b, h)
            assert data["phase_identity"] is True


def test_pure_even_roots_form_nonnegative_coefficient_cosine_pair():
    data = pure_even_root_phases(46, 15, 3)
    assert data["pure_even_coefficients_positive"] is True
    assert abs(data["pure_pair_phase_sum"].imag) < 1e-10
