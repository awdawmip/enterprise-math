from enterprise_math.p022_barlow_twin_general_high_size import (
    common_transfer_prime_is_large_enough,
    minimum_affine_prime_after_seven_rank,
    seven_rank_affine_size_gate,
)


def test_actual_affine_candidate_clears_the_fixed_delta_threshold() -> None:
    # r=90,h=6,c=24 gives q=647 and delta=72.
    prime, minimum = seven_rank_affine_size_gate(90, 6, 24)
    assert prime == 647
    assert minimum == 7 * 72 + 39 == 543
    assert prime >= minimum


def test_first_noncoprime_transfer_example_is_far_too_small() -> None:
    # The exact common factor 701 at (h,c)=(51,-120) has delta=288.
    assert minimum_affine_prime_after_seven_rank(51, -120) == 2055
    assert not common_transfer_prime_is_large_enough(51, -120, 701)
