import unittest

from enterprise_math.precision_exponent_calculus import (
    equal_exponent_scale,
    exponent_imbalance_defect,
    exponent_join_word,
    exponent_meet_word,
    exponent_sum_word,
    exponent_word_to_integer,
    p005_exponent_linearization_holds,
    rational_exponent_word,
    scale_axis_rank,
    scale_exponent_word,
    scale_hasse_distance,
    scale_hasse_distance_gcd_formula,
    scale_total_depth,
)


class PrecisionExponentCalculusTests(unittest.TestCase):
    def test_scale_word_round_trip_and_p005_linearization(self):
        self.assertEqual(scale_exponent_word(1), ())
        self.assertEqual(scale_exponent_word(180), ((2, 2), (3, 2), (5, 1)))
        self.assertEqual(exponent_word_to_integer(scale_exponent_word(180)), 180)
        for left in range(1, 50):
            for right in range(1, 50):
                self.assertTrue(p005_exponent_linearization_holds(left, right))

    def test_multiplication_gcd_lcm_are_sum_min_max(self):
        self.assertEqual(exponent_sum_word(12, 18), ((2, 3), (3, 3)))
        self.assertEqual(exponent_meet_word(12, 18), ((2, 1), (3, 1)))
        self.assertEqual(exponent_join_word(12, 18), ((2, 2), (3, 2)))

    def test_positive_rational_can_be_stored_as_integer_laurent_word(self):
        self.assertEqual(rational_exponent_word(2, 15), ((2, 1), (3, -1), (5, -1)))
        self.assertEqual(rational_exponent_word(12, 18), ((2, 1), (3, -1)))
        self.assertEqual(rational_exponent_word(7, 7), ())

    def test_rank_depth_and_hasse_distance_are_integer(self):
        self.assertEqual(scale_axis_rank(1), 0)
        self.assertEqual(scale_axis_rank(900), 3)
        self.assertEqual(scale_total_depth(900), 5)
        pairs = ((1, 60), (12, 18), (30, 180), (72, 125))
        for left, right in pairs:
            self.assertEqual(
                scale_hasse_distance(left, right),
                scale_hasse_distance_gcd_formula(left, right),
            )
        self.assertEqual(scale_hasse_distance(12, 18), 2)

    def test_equal_exponent_word_has_zero_arithmetic_imbalance_only(self):
        self.assertTrue(equal_exponent_scale(1))
        self.assertTrue(equal_exponent_scale(30))
        self.assertTrue(equal_exponent_scale(900))
        self.assertEqual(exponent_imbalance_defect(900), 0)
        self.assertFalse(equal_exponent_scale(180))
        self.assertEqual(exponent_imbalance_defect(180), 2)

    def test_invalid_words_fail_closed(self):
        with self.assertRaises(ValueError):
            scale_exponent_word(0)
        with self.assertRaises(ValueError):
            rational_exponent_word(0, 1)
        with self.assertRaises(ValueError):
            exponent_word_to_integer(((4, 1),))
        with self.assertRaises(ValueError):
            exponent_word_to_integer(((3, 1), (2, 1)))


if __name__ == "__main__":
    unittest.main()
