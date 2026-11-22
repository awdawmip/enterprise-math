from enterprise_math.p017_p018_covering_height_dynamics import (
    bounded_prime_block_safety_certificate,
    next_prime_after,
    verify_composite_step_feasible_root_nesting,
)


def test_next_prime_after_small_inputs():
    assert next_prime_after(2) == 3
    assert next_prime_after(3) == 5
    assert next_prime_after(13) == 17
    assert next_prime_after(23) == 29


def test_composite_cutoff_steps_only_shrink_bounded_feasible_root_sets():
    for y in range(2, 20):
        if next_prime_after(y) == y + 1:
            continue
        data = verify_composite_step_feasible_root_nesting(y, 40)
        assert data["bounded_feasible_root_nesting"] is True
        assert set(data["roots_at_next"]) <= set(data["roots_at_y"])


def test_small_prime_blocks_are_boundedly_safe():
    for p in (2, 3, 5, 7, 11, 13, 17, 19):
        data = bounded_prime_block_safety_certificate(p, next_prime_after(p) - 1)
        assert data["bounded_prime_block_safe"] is True
        assert data["first_covering_root_through_block_end"] is None
