import unittest
from fractions import Fraction

from enterprise_math.abc_projective_adaptive_precision import (
    adaptive_projective_precision_state,
    dyadic_projective_precision_level_from_fraction,
    level_is_sum_of_threshold_bits,
)


class ProjectiveAdaptivePrecisionTests(unittest.TestCase):
    def test_exact_levels(self) -> None:
        cases = (
            (Fraction(1, 3), 0),
            (Fraction(1, 1), 1),
            (Fraction(3, 2), 1),
            (Fraction(2, 1), 2),
            (Fraction(7, 1), 3),
            (Fraction(8, 1), 4),
        )
        for value, expected in cases:
            self.assertEqual(
                dyadic_projective_precision_level_from_fraction(value), expected
            )
            self.assertTrue(level_is_sum_of_threshold_bits(value))

    def test_small_abc_states(self) -> None:
        subunit = adaptive_projective_precision_state(2, 3, 5)
        self.assertEqual(subunit.level, 0)
        self.assertEqual(subunit.crossed_thresholds, ())
        self.assertEqual(subunit.next_threshold, 1)

        boundary = adaptive_projective_precision_state(1, 2, 3)
        self.assertEqual(boundary.level, 1)
        self.assertEqual(boundary.crossed_thresholds, (1,))
        self.assertEqual(boundary.next_threshold, 2)

        high = adaptive_projective_precision_state(3, 125, 128)
        self.assertEqual(high.level, 3)
        self.assertEqual(high.crossed_thresholds, (1, 2, 4))
        self.assertEqual(high.next_threshold, 8)


if __name__ == "__main__":
    unittest.main()
