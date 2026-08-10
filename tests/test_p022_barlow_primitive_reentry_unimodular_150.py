from enterprise_math.p022_barlow_primitive_reentry_unimodular_150 import (
    NEW_PRIMITIVE_PRIME_41,
    NEW_PRIMITIVE_PRIME_63,
    TWIN_REENTRY_21,
    TWIN_REENTRY_30,
    new_primitive_rows_are_certified_150,
    primitive_twin_reentry_certificate,
    projected_new_primitive_supports_150,
    twin_prime_blackout_profile,
    two_row_actual_prime_core_determinant_150,
    two_row_unimodular_residual_determinant_150,
    verify_primitive_reentry_unimodular_150,
)


def test_twin_prime_deferral_has_linear_blackout_then_canonical_reentry() -> None:
    blackout_6, target_6 = twin_prime_blackout_profile(6)
    assert blackout_6 == (8,)
    assert target_6 == 11
    assert primitive_twin_reentry_certificate(6, 13) == (11, 1)
    assert primitive_twin_reentry_certificate(6, 73) == (11, 1)

    assert primitive_twin_reentry_certificate(*TWIN_REENTRY_21[:2]) == TWIN_REENTRY_21[2:]
    assert primitive_twin_reentry_certificate(*TWIN_REENTRY_30[:2]) == TWIN_REENTRY_30[2:]


def test_two_new_rows_are_genuine_primitive_unit_singletons() -> None:
    assert NEW_PRIMITIVE_PRIME_41 == 1_466_657
    assert NEW_PRIMITIVE_PRIME_63 == 1_017_335_309_243_777_987
    assert new_primitive_rows_are_certified_150()
    assert projected_new_primitive_supports_150() == (((41, 1),), ((63, 1),))


def test_two_real_prime_rows_make_the_residual_and_core_unimodular() -> None:
    assert two_row_unimodular_residual_determinant_150() == -1
    assert two_row_actual_prime_core_determinant_150() == -1
    assert verify_primitive_reentry_unimodular_150()
