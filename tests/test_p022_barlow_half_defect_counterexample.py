from enterprise_math.p022_barlow_half_defect_counterexample import (
    EXPECTED_DEFECT_VALUATION,
    FIRST_SUPPORT_COLLISION_PRIME,
    first_counterexample_basic_arithmetic,
    first_counterexample_defect_valuation,
    first_counterexample_flux_correction,
    first_counterexample_low_support_zero_hits,
    first_counterexample_midpoint_is_simple,
    first_counterexample_relation_exponent,
)


def test_first_target_family_support_collision_is_exact() -> None:
    assert FIRST_SUPPORT_COLLISION_PRIME == 369_581
    assert first_counterexample_basic_arithmetic()
    assert first_counterexample_relation_exponent() == 2
    assert first_counterexample_low_support_zero_hits() == (8,)


def test_first_counterexample_has_simple_midpoint_but_negative_marker() -> None:
    assert first_counterexample_midpoint_is_simple()
    assert first_counterexample_flux_correction() == -2
    assert first_counterexample_defect_valuation() == EXPECTED_DEFECT_VALUATION == -1
