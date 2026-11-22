from enterprise_math.p017_p018_carry_future_precision import (
    full_singleton_divisor_recovery,
    singleton_divisor_future_signature,
    size_future_signature,
    verify_size_future_residue_sufficiency,
)


def test_finite_size_future_factors_through_lcm_residue():
    data = verify_size_future_residue_sufficiency(
        fiber_size=17,
        first_quotient=101,
        refinements=(3, 5, 7, 9),
        residue_shift_multiplier=2,
    )
    assert data["same_size_future_signature"] is True
    assert data["first_signature"]["child_size_rows"] == data["shifted_signature"]["child_size_rows"]


def test_composite_total_refinements_need_only_their_total_product_residues():
    # Because R_5 o R_3 = R_15, a future language that asks the size after
    # staged (3,5) refinement needs only the same residue data as total d=15.
    signature = size_future_signature(23, 137, (3, 5, 15, 21))
    assert signature["finite_size_language_factors_through_residue"] is True
    assert signature["future_precision_modulus"] % 15 == 0
    assert signature["future_precision_modulus"] % 21 == 0


def test_singleton_child_visibility_is_exact_divisibility():
    data = singleton_divisor_future_signature(3 * 5 * 11, (3, 5, 7, 11, 15, 33, 55, 77))
    assert data["singleton_visibility_equals_divisibility"] is True
    visible = {row["refinement"] for row in data["rows"] if row["visible"]}
    assert visible == {3, 5, 11, 15, 33, 55}


def test_universal_singleton_divisor_language_recovers_full_quotient():
    for quotient in (3, 45, 165, 945):
        data = full_singleton_divisor_recovery(quotient)
        assert data["universal_divisor_future_is_information_complete"] is True
        assert data["recovered_first_quotient"] == quotient
