import itertools
import unittest

from enterprise_math.pair_dispersion import (
    merge_pair_dispersion_identity,
    pair_dispersion,
    pair_dispersion_identity,
    reassociate_imbalances,
    reassociation_quadratic_identity,
    zero_sum_quadratic_separation,
)
from enterprise_math.contraction_trace import square_split_imbalance


class PairDispersionTests(unittest.TestCase):
    def test_pair_dispersion_algebraic_identity(self):
        for length in range(1, 7):
            for values in itertools.product(range(-2, 3), repeat=length):
                direct, algebraic = pair_dispersion_identity(values)
                self.assertEqual(direct, algebraic)

    def test_fraction_free_merge_identity(self):
        for left_size in range(1, 4):
            for right_size in range(1, 4):
                left_states = itertools.product(range(-2, 3), repeat=left_size)
                for left in left_states:
                    for right in itertools.product(range(-2, 3), repeat=right_size):
                        left_side, right_side = merge_pair_dispersion_identity(
                            left, right
                        )
                        self.assertEqual(left_side, right_side)

    def test_local_reassociation_transports_imbalances_exactly(self):
        for left_size in range(1, 4):
            for middle_size in range(1, 4):
                for right_size in range(1, 4):
                    for left_total in range(-4, 5):
                        for middle_total in range(-4, 5):
                            for right_total in range(-4, 5):
                                old_inner = square_split_imbalance(
                                    left_size,
                                    middle_size,
                                    left_total,
                                    middle_total,
                                )
                                old_parent = square_split_imbalance(
                                    left_size + middle_size,
                                    right_size,
                                    left_total + middle_total,
                                    right_total,
                                )
                                new_inner, new_parent = reassociate_imbalances(
                                    left_size,
                                    middle_size,
                                    right_size,
                                    old_inner,
                                    old_parent,
                                )
                                expected_inner = square_split_imbalance(
                                    middle_size,
                                    right_size,
                                    middle_total,
                                    right_total,
                                )
                                expected_parent = square_split_imbalance(
                                    left_size,
                                    middle_size + right_size,
                                    left_total,
                                    middle_total + right_total,
                                )
                                self.assertEqual(
                                    (new_inner, new_parent),
                                    (expected_inner, expected_parent),
                                )
                                identity_left, identity_right = (
                                    reassociation_quadratic_identity(
                                        left_size,
                                        middle_size,
                                        right_size,
                                        old_inner,
                                        old_parent,
                                    )
                                )
                                self.assertEqual(identity_left, identity_right)

    def test_unit_slot_rotation_matches_closed_example(self):
        # ((x,y),z) -> (x,(y,z))
        for x in range(-4, 5):
            for y in range(-4, 5):
                for z in range(-4, 5):
                    u = x - y
                    v = x + y - 2 * z
                    up, vp = reassociate_imbalances(1, 1, 1, u, v)
                    self.assertEqual(2 * up, v - u)
                    self.assertEqual(2 * vp, v + 3 * u)
                    self.assertEqual(3 * u * u + v * v, 3 * up * up + vp * vp)

    def test_zero_sum_pair_dispersion_recovers_quadratic_separation(self):
        for coordinate_count in range(2, 7):
            for prefix in itertools.product(range(-2, 3), repeat=coordinate_count - 1):
                values = prefix + (-sum(prefix),)
                expected = sum(value * value for value in values) // 2
                self.assertEqual(
                    zero_sum_quadratic_separation(values),
                    expected,
                )
                self.assertEqual(
                    pair_dispersion(values),
                    2 * coordinate_count * expected,
                )


if __name__ == "__main__":
    unittest.main()
