from enterprise_math.p022_barlow_half_defect_counterexample import (
    EXPECTED_DEFECT_VALUATION,
    EXPLICIT_SUPPORT_COLLISION_PRIME,
    explicit_counterexample_basic_arithmetic,
    explicit_counterexample_defect_valuation,
    explicit_counterexample_flux_correction,
    explicit_counterexample_low_support_zero_hits,
    explicit_counterexample_midpoint_is_simple,
    explicit_counterexample_relation_exponent,
)


def test_explicit_target_family_support_collision_is_exact() -> None:
    assert EXPLICIT_SUPPORT_COLLISION_PRIME == 369_581
    assert explicit_counterexample_basic_arithmetic()
    assert explicit_counterexample_relation_exponent() == 2
    assert explicit_counterexample_low_support_zero_hits() == (8,)


def test_explicit_counterexample_has_simple_midpoint_but_negative_marker() -> None:
    assert explicit_counterexample_midpoint_is_simple()
    assert explicit_counterexample_flux_correction() == -2
    assert explicit_counterexample_defect_valuation() == EXPECTED_DEFECT_VALUATION == -1
