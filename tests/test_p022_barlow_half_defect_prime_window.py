from enterprise_math.p022_barlow_half_defect_prime_window import (
    dangerous_prime_window,
    p_minus_two_odd_prime_roots,
    root_candidate_indices,
    root_candidate_offsets,
    root_incidence_is_companion_zero,
    root_quotient_parameters,
    target_companion_zero_is_automatically_off_support,
    target_prime_lies_in_dangerous_window,
    target_root_mod3_condition,
    target_window_matches_support_bound,
)
from enterprise_math.p022_barlow_franel_integer_companion import (
    forced_zero_offsets_from_integer_companion,
)
from enterprise_math.p022_barlow_low_order_defect_reduction import _is_prime


def test_dangerous_windows_are_exact_rearrangements() -> None:
    assert dangerous_prime_window(9, 5) == (21, 29)
    assert dangerous_prime_window(5, 23) == (13, 23)
    for prime in range(7, 5000):
        if prime % 24 not in (5, 23) or not _is_prime(prime):
            continue
        assert target_window_matches_support_bound(prime)


def test_near_midpoint_companion_zeros_are_automatically_off_support() -> None:
    # p=29 has a companion zero at d=2, but target support can only be
    # dangerous from d=9 onward.
    assert forced_zero_offsets_from_integer_companion(29) == (2,)
    assert not target_prime_lies_in_dangerous_window(29, 2)
    assert target_companion_zero_is_automatically_off_support(29, 2)

    # p=173 has a far-tail zero at d=82, so the window test alone cannot
    # exclude it; the prime-halving tree is needed for the final exclusion.
    assert 82 in forced_zero_offsets_from_integer_companion(173)
    assert target_prime_lies_in_dangerous_window(173, 82)
    assert not target_companion_zero_is_automatically_off_support(173, 82)


def test_direct_p_minus_two_root_offsets_and_mod3_condition() -> None:
    # p=53: p-2=3*17.  For q=17, quotient=3=2*1+1 and the two direct
    # candidate offsets are 17 and 18.
    assert p_minus_two_odd_prime_roots(53) == (3, 17)
    assert root_quotient_parameters(53, 17) == (3, 1)
    assert root_candidate_indices(53, 17) == (9, 8)
    assert root_candidate_offsets(53, 17) == (17, 18)
    assert target_root_mod3_condition(53, 17)
    assert root_incidence_is_companion_zero(53, 17) == (False, False)

    # q=3 is the special harmless root; its candidate A-indices are 2 and 1.
    assert root_candidate_indices(53, 3) == (2, 1)
    assert target_root_mod3_condition(53, 3)


def test_every_target_p_minus_two_root_obeys_the_mod3_constraint() -> None:
    for prime in range(7, 10000):
        if prime % 24 not in (5, 23) or not _is_prime(prime):
            continue
        for root in p_minus_two_odd_prime_roots(prime):
            assert target_root_mod3_condition(prime, root)
            if root != 3:
                quotient, t = root_quotient_parameters(prime, root)
                assert quotient % 3 == 0
                assert t % 3 == 1
