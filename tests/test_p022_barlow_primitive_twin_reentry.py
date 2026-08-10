from enterprise_math.p022_barlow_primitive_twin_reentry import (
    primitive_twin_reentry_valuation,
    twin_reentry_collision_requires_one_third_threshold,
    twin_reentry_failure_is_equal_depth_collision,
    twin_reentry_high_relation_support,
    twin_reentry_is_forced_below_one_third_threshold,
    twin_reentry_segment,
)


def test_twin_reentry_segment_is_the_lower_twin_prime() -> None:
    expected = {6: 11, 9: 17, 15: 29, 21: 41, 30: 59, 36: 71}
    for rank, segment in expected.items():
        assert twin_reentry_segment(rank) == segment
        assert twin_reentry_high_relation_support(rank) == (
            (rank, -1),
            (segment - 1, 1),
        )


def test_rank_six_primitive_rows_reenter_at_d11() -> None:
    for prime in (13, 73):
        assert primitive_twin_reentry_valuation(6, prime) == (1, 1, 0, 0)
        assert not twin_reentry_failure_is_equal_depth_collision(6, prime)
        assert twin_reentry_collision_requires_one_third_threshold(6, prime)

    assert twin_reentry_is_forced_below_one_third_threshold(6, 13)


def test_more_exact_twin_center_primitive_rows_reenter_with_unit_depth() -> None:
    examples = (
        (9, 937),
        (9, 1409),
        (15, 31),
        (15, 179),
        (21, 3019),
        (30, 1361),
    )
    for rank, prime in examples:
        assert primitive_twin_reentry_valuation(rank, prime) == (1, 1, 0, 0)
        assert not twin_reentry_failure_is_equal_depth_collision(rank, prime)
        assert twin_reentry_collision_requires_one_third_threshold(rank, prime)


def test_small_primitive_prime_is_forced_below_collision_threshold() -> None:
    # 31 is primitive at r=15, and 31 < 3*15-1=44.
    assert twin_reentry_is_forced_below_one_third_threshold(15, 31)


def test_large_primitive_prime_may_still_reenter_even_without_size_certificate() -> None:
    # The theorem does not claim the large-prime region is dangerous; only
    # that size alone no longer excludes the predecessor collision there.
    assert primitive_twin_reentry_valuation(9, 1409) == (1, 1, 0, 0)
