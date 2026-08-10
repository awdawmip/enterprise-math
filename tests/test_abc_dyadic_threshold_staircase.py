import unittest
from fractions import Fraction

from enterprise_math.abc_dyadic_threshold_staircase import (
    activation_matrix_from_crossings,
    compatible_staircase_state_count,
    dyadic_threshold_staircase,
    threshold_crossing_depths,
)


class DyadicThresholdStaircaseTests(unittest.TestCase):
    def test_exact_staircase_fixture(self) -> None:
        state = dyadic_threshold_staircase(
            3,
            41,
            2,
            3,
            (
                Fraction(1, 22),
                Fraction(1, 2),
                Fraction(1, 1),
                Fraction(11, 1),
            ),
        )
        self.assertEqual(state.exponents, (2, 4, 8, 16))
        self.assertEqual(state.crossing_depths, (0, 1, 2, None))
        self.assertEqual(
            state.activation_matrix,
            (
                (True, True, True, True),
                (False, True, True, True),
                (False, False, True, True),
                (False, False, False, False),
            ),
        )
        self.assertTrue(state.monotone_crossings_verified)
        self.assertTrue(state.reconstruction_verified)

    def test_distinct_thresholds_may_share_one_crossing_depth(self) -> None:
        state = dyadic_threshold_staircase(
            3,
            41,
            2,
            3,
            (
                Fraction(1, 2),
                Fraction(1, 1),
                Fraction(10, 1),
                Fraction(11, 1),
            ),
        )
        self.assertEqual(state.crossing_depths, (1, 2, 2, None))
        self.assertEqual(state.activation_matrix[1], state.activation_matrix[2])

    def test_state_count_is_combinations_with_repetition(self) -> None:
        self.assertEqual(compatible_staircase_state_count(3, 4), 70)
        state = dyadic_threshold_staircase(
            3,
            41,
            2,
            3,
            (
                Fraction(1, 22),
                Fraction(1, 2),
                Fraction(1, 1),
                Fraction(11, 1),
            ),
        )
        self.assertEqual(state.compatible_matrix_state_count, 70)
        self.assertEqual(state.unconstrained_boolean_matrix_state_count, 2**16)
        self.assertLess(
            state.compatible_matrix_state_count,
            state.unconstrained_boolean_matrix_state_count,
        )

    def test_matrix_reconstruction_accepts_weak_staircase(self) -> None:
        matrix = activation_matrix_from_crossings(3, (1, 2, 2, None))
        self.assertEqual(
            matrix,
            (
                (False, True, True, True),
                (False, False, True, True),
                (False, False, True, True),
                (False, False, False, False),
            ),
        )

    def test_crossing_depths_are_monotone_in_threshold(self) -> None:
        pressures = (
            Fraction(1, 22),
            Fraction(13, 22),
            Fraction(221, 22),
            Fraction(221, 22),
        )
        crossings = threshold_crossing_depths(
            pressures,
            (Fraction(1, 22), Fraction(1, 2), Fraction(1), Fraction(11)),
        )
        self.assertEqual(crossings, (0, 1, 2, None))

    def test_rejects_nonincreasing_threshold_grid(self) -> None:
        with self.assertRaises(ValueError):
            dyadic_threshold_staircase(
                3,
                41,
                2,
                3,
                (Fraction(1), Fraction(1)),
            )

    def test_rejects_nonmonotone_crossing_encoding(self) -> None:
        with self.assertRaises(ValueError):
            activation_matrix_from_crossings(3, (2, 1))


if __name__ == "__main__":
    unittest.main()
