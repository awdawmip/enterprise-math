from enterprise_math.p017_p018_carry_global_half_skew import global_mobius_carry_half_skew


def test_full_mobius_carry_field_has_universal_negative_one_half_skew():
    for P in (3, 5, 15, 35, 105, 1155):
        data = global_mobius_carry_half_skew(P)
        assert data["second_minus_first_half"] == -1
        assert data["universal_global_half_skew"] == -1
