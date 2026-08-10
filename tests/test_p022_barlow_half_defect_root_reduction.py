from enterprise_math.p022_barlow_half_defect_root_reduction import (
    direct_root_companion_incidents,
    direct_root_incidence_gcd,
    minus_root_prime_from_offset,
    plus_root_prime_from_offset,
    target_direct_root_candidates,
)


def test_offset_divisor_reconstructs_known_target_roots() -> None:
    assert plus_root_prime_from_offset(17, 17) == 53
    assert minus_root_prime_from_offset(18, 17) == 53
    assert ("plus", 17, 53) in target_direct_root_candidates(17)
    assert ("minus", 17, 53) in target_direct_root_candidates(18)

    assert plus_root_prime_from_offset(44, 11) == 101
    assert minus_root_prime_from_offset(45, 11) == 101
    assert ("plus", 11, 101) in target_direct_root_candidates(44)
    assert ("minus", 11, 101) in target_direct_root_candidates(45)


def test_q_three_is_removed_as_harmless_root() -> None:
    # p=23 has p-2=3*7.  q=3 generates only A-indices 2 and 1 and is
    # intentionally absent from the dangerous candidate list.
    assert all(q != 3 for _, q, _ in target_direct_root_candidates(7))
    assert ("plus", 7, 23) in target_direct_root_candidates(7)
    assert ("minus", 7, 23) in target_direct_root_candidates(8)


def test_no_direct_root_incident_in_bounded_offset_range() -> None:
    # Finite pressure test only; the theorem is the offset-divisor reduction,
    # not a claim that this bounded check proves infinite avoidance.
    for offset in range(1, 1000):
        assert direct_root_companion_incidents(offset) == ()
        assert direct_root_incidence_gcd(offset) == 1


def test_p157_negative_boundary_is_outside_target_candidate_arithmetic() -> None:
    # The known cancellation uses d=62,q=31,p=157.  Here d/q=2, not 1 mod3,
    # and p=13 mod24, so it is excluded exactly by the target arithmetic.
    assert 62 % 31 == 0
    assert 62 // 31 == 2
    assert 2 % 3 != 1
    assert 157 % 24 == 13
    assert ("plus", 31, 157) not in target_direct_root_candidates(62)
