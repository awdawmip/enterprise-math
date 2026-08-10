import pytest

from enterprise_math.p022_barlow_forced_midpoint_fallback import (
    forced_midpoint_fallback_capture_location,
    forced_midpoint_signed_high_support,
    forced_midpoint_small_support_bound,
)


def test_signed_localization_for_5_mod24_and_composite_midpoints() -> None:
    expected = {
        29: (5, ((13, 1),)),
        53: (9, ((25, 1),)),
        149: (25, ((73, 1),)),
        2351: (392, ((1174, 1),)),
        3701: (617, ((1849, 1),)),
    }
    for prime, row in expected.items():
        assert forced_midpoint_small_support_bound(prime) == row[0]
        assert forced_midpoint_signed_high_support(prime) == row


def test_prime_midpoint_has_only_one_positive_and_one_negative_extra_pair() -> None:
    expected = {
        23: (4, ((5, 1), (6, -1), (10, 1))),
        47: (8, ((11, 1), (12, -1), (22, 1))),
        383: (64, ((95, 1), (96, -1), (190, 1))),
    }
    for prime, row in expected.items():
        assert forced_midpoint_signed_high_support(prime) == row


def test_actual_primitive_twin_rows_are_captured_by_midpoint_fallback() -> None:
    # Both have composite midpoint, so no high positive cancellation channel
    # survives above B=(q+1)/6.
    assert forced_midpoint_fallback_capture_location(726, 2351) == 1175
    assert forced_midpoint_fallback_capture_location(1014, 3701) == 1850


def test_prime_midpoint_target_also_falls_back_when_high_positive_index_is_preprimitive() -> None:
    # q=11279 has prime midpoint 5639 and primitive twin rank 3744.  The sole
    # extra positive support index is 2819<3744, hence a q-unit by primitiveness.
    assert forced_midpoint_fallback_capture_location(3744, 11279) == 5639


def test_fallback_rejects_the_remaining_superlarge_window() -> None:
    # q=1373 has primitive twin rank 96 but q>=6r-1, so this theorem is not
    # allowed to pretend the midpoint localization has closed the case.
    with pytest.raises(ValueError, match="r>\(q\+1\)/6"):
        forced_midpoint_fallback_capture_location(96, 1373)
