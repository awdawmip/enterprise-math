import itertools
import unittest

from enterprise_math.pair_dispersion import (
    merge_pair_dispersion_identity,
    pair_dispersion,
    pair_dispersion_identity,
    zero_sum_quadratic_separation,
)


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
