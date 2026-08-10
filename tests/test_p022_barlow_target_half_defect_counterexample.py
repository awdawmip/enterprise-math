from enterprise_math.p022_barlow_target_half_defect_counterexample import (
    TARGET_COUNTEREXAMPLE_EARLIER_INDEX,
    TARGET_COUNTEREXAMPLE_MIDPOINT,
    TARGET_COUNTEREXAMPLE_PRIME,
    target_counterexample_defect_valuation,
    target_counterexample_earlier_franel_identity,
    target_counterexample_midpoint_lift,
    target_counterexample_profile,
    target_counterexample_relation,
    target_counterexample_support_correction,
    target_counterexample_support_zero_hits,
)


def test_target_counterexample_is_inside_declared_residue_family() -> None:
    assert TARGET_COUNTEREXAMPLE_PRIME % 24 == 5
    assert TARGET_COUNTEREXAMPLE_MIDPOINT == (TARGET_COUNTEREXAMPLE_PRIME - 1) // 2
    boundary = 2 * TARGET_COUNTEREXAMPLE_MIDPOINT - 1
    assert boundary == TARGET_COUNTEREXAMPLE_PRIME - 2
    assert boundary % 3 == 0


def test_earlier_franel_term_is_exactly_twice_the_prime() -> None:
    value, prime, quotient = target_counterexample_earlier_franel_identity()
    assert prime == TARGET_COUNTEREXAMPLE_PRIME
    assert value == 739_162
    assert quotient == 2


def test_canonical_A_relation_uses_F8_with_exponent_two() -> None:
    relation = dict(target_counterexample_relation())
    assert relation[TARGET_COUNTEREXAMPLE_EARLIER_INDEX] == 2
    assert relation[184_789] == 1


def test_only_F8_is_a_support_zero_modulo_p() -> None:
    assert target_counterexample_support_zero_hits() == (8,)


def test_midpoint_zero_is_simple_but_defect_direction_reverses() -> None:
    assert target_counterexample_midpoint_lift() == 153_310
    assert target_counterexample_support_correction() == 2
    assert target_counterexample_defect_valuation() == -1
    assert target_counterexample_profile() == (369_581, 184_790, 2, 1, -1)
