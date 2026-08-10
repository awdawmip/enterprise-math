from enterprise_math.p022_barlow_primitive_successor_capture import (
    is_twin_prime_deferral_center,
    primitive_capture_location,
    primitive_event_capture_valuation,
    primitive_event_is_captured_within_one_step,
    primitive_successor_capture_valuation,
    successor_relation_previous_exponent,
)
from enterprise_math.p022_barlow_target_negative_unit_crossing import (
    TARGET_NEGATIVE_UNIT_PRIME,
    certify_target_negative_unit_prime,
)


def test_capture_location_is_r_or_successor_except_twin_prime_center() -> None:
    assert primitive_capture_location(8) == 8       # 15 composite
    assert primitive_capture_location(16) == 17     # 31 prime, 33 composite
    assert primitive_capture_location(49) == 50     # 97 prime, 99 composite
    assert primitive_capture_location(6) is None    # 11,13 twin primes
    assert is_twin_prime_deferral_center(6)


def test_successor_relation_contains_previous_generator_once() -> None:
    for rank in (3, 4, 7, 9, 16, 19, 49):
        if primitive_capture_location(rank) == rank + 1:
            assert successor_relation_previous_exponent(rank) == 1


def test_p157_primitive_event_is_captured_at_d17_with_negative_unit() -> None:
    assert primitive_successor_capture_valuation(16, 157) == -1
    assert primitive_event_capture_valuation(16, 157) == (17, -1)
    assert primitive_event_is_captured_within_one_step(16, 157)


def test_p369581_is_captured_immediately_before_later_sign_reversal() -> None:
    assert primitive_event_capture_valuation(8, 369_581) == (8, 1)
    assert primitive_event_is_captured_within_one_step(8, 369_581)


def test_p518220701_is_captured_immediately_at_d50() -> None:
    assert primitive_event_capture_valuation(50, 518_220_701) == (50, 1)


def test_large_negative_unit_prime_was_already_captured_at_d50() -> None:
    assert certify_target_negative_unit_prime()
    assert primitive_event_capture_valuation(49, TARGET_NEGATIVE_UNIT_PRIME) == (50, -1)
    assert primitive_event_is_captured_within_one_step(49, TARGET_NEGATIVE_UNIT_PRIME)
