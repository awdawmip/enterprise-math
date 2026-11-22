from math import gcd

from enterprise_math.legendre import direct_square_interval_prime_count
from enterprise_math.p017_p018_carry_anchored_jacobsthal import (
    anchored_unit_step_rough_count,
    square_boundary_anchored_wheel_state,
    unit_step_anchor,
)


def test_step_two_channel_is_exactly_one_consecutive_reduced_residue_interval():
    for wheel in (1, 3, 5, 15, 21, 105, 1155):
        for first_quotient in (-21, -9, -1, 1, 7, 23):
            for fiber_size in range(0, 16):
                data = anchored_unit_step_rough_count(fiber_size, first_quotient, wheel)
                assert data["unit_step_equivalence"] is True
                anchor = unit_step_anchor(first_quotient, wheel)
                assert data["rough_count"] == sum(
                    gcd(anchor - offset, wheel) == 1 for offset in range(fiber_size)
                )


def test_square_anchor_reduced_residue_count_is_exact_prime_gap():
    for k in range(3, 41):
        data = square_boundary_anchored_wheel_state(k)
        assert data["rough_count"] == direct_square_interval_prime_count(k)
        assert data["candidate_count"] == (k if k % 2 == 0 else k - 1)


def test_bounded_square_anchors_have_a_survivor_without_claiming_an_infinite_proof():
    for k in (5, 10, 31, 64, 127, 256):
        data = square_boundary_anchored_wheel_state(k)
        assert data["first_survivor_offset"] is not None
        assert data["first_survivor_offset"] < data["candidate_count"]
