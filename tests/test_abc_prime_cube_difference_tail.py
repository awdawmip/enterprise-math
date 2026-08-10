import unittest

from enterprise_math.abc_prime_cube_difference_tail import (
    balanced_cube_difference_split,
    ceil_sqrt,
    cube_difference_tail_power_profile,
    large_residual_integer_union_bound,
)
from enterprise_math.abc_support import multiplicity_residual


class PrimeCubeDifferenceTailTests(unittest.TestCase):
    def test_ceil_sqrt(self) -> None:
        self.assertEqual(ceil_sqrt(0), 0)
        self.assertEqual(ceil_sqrt(1), 1)
        self.assertEqual(ceil_sqrt(15), 4)
        self.assertEqual(ceil_sqrt(16), 4)
        self.assertEqual(ceil_sqrt(17), 5)

    def test_square_divisor_union_bound_dominates_exact_residual_count(self) -> None:
        for height in (50, 100, 250):
            for threshold in (2, 3, 5, 10, 20):
                exact = sum(
                    1
                    for n in range(1, height + 1)
                    if multiplicity_residual(n) >= threshold
                )
                bound = large_residual_integer_union_bound(height, threshold)
                self.assertLessEqual(exact, bound)

    def test_balanced_split_uses_sqrt_TP_horizon(self) -> None:
        state = balanced_cube_difference_split(81, 4)
        self.assertEqual(state.split_horizon, 18)
        self.assertEqual(state.radius_residual_threshold, 18)
        self.assertEqual(state.quadratic_residual_threshold, 10)
        self.assertGreaterEqual(state.radius_value_union_bound, 0)
        self.assertGreaterEqual(state.quadratic_value_union_bound, 0)

    def test_formal_tail_powers(self) -> None:
        self.assertEqual(
            cube_difference_tail_power_profile(),
            {
                "center_height_power": (7, 4),
                "threshold_power": (-1, 4),
            },
        )


if __name__ == "__main__":
    unittest.main()
