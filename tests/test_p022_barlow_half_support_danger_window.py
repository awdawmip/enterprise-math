from enterprise_math.p022_barlow_half_support_danger_window import (
    actual_support_offset_obeys_danger_window,
    large_companion_prime_is_automatically_safe,
    possible_target_cancellation_at_offset,
    target_danger_window,
    target_prime_is_in_danger_window,
    target_support_window_profile,
)


def test_exact_linear_windows() -> None:
    assert target_danger_window(10, 5) == (21, 32)
    assert target_danger_window(10, 23) == (21, 43)


def test_every_actual_nontrivial_support_offset_obeys_necessary_window() -> None:
    for prime in (23, 29, 47, 53, 71, 101, 149, 167, 173, 191, 197, 239):
        _, offsets, certified = target_support_window_profile(prime)
        assert offsets == certified
        for offset in offsets:
            assert actual_support_offset_obeys_danger_window(prime, offset)


def test_large_integer_companion_prime_divisors_are_structurally_safe() -> None:
    # p=29 divides K_2, but 29>3*2+2, so its midpoint zero is far too close to
    # the midpoint to meet the p=5 mod24 canonical support.
    assert large_companion_prime_is_automatically_safe(2, 29)

    # These exact K_d prime factors were found in the structural pressure path;
    # each lies far above the only possible target cancellation window.
    assert large_companion_prime_is_automatically_safe(8, 27143)
    assert large_companion_prime_is_automatically_safe(18, 389)
    assert large_companion_prime_is_automatically_safe(24, 149)


def test_window_membership_is_necessary_not_sufficient() -> None:
    # A prime may lie in the size window without dividing K_d.
    assert target_prime_is_in_danger_window(8, 23)
    assert not possible_target_cancellation_at_offset(8, 23)

    # Conversely p=29 divides K_2, but it is outside the target size window.
    assert not target_prime_is_in_danger_window(2, 29)
    assert not possible_target_cancellation_at_offset(2, 29)
