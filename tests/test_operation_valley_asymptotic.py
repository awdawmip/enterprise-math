import unittest

from enterprise_math.operation_valley_asymptotic import (
    balanced_probability_sandwich_holds,
    balanced_rounding_correction,
    balanced_total_safe_probability,
    ideal_candidate_block_counts,
    ideal_equal_block_probability,
    ideal_integer_block_count,
    operation_valley_sandwich_report,
    true_valley_lies_in_ideal_candidate_window,
)


class OperationValleyAsymptoticTests(unittest.TestCase):
    def test_exact_probability_sandwich_on_broad_finite_grid(self):
        checked = 0
        for state_count in range(3, 81):
            for block_count in range(2, state_count):
                self.assertTrue(
                    balanced_probability_sandwich_holds(
                        state_count, block_count
                    )
                )
                correction = balanced_rounding_correction(
                    state_count, block_count
                )
                self.assertGreaterEqual(correction, 1)
                self.assertLessEqual(correction, 4**block_count)
                checked += 1
        self.assertGreater(checked, 3000)

    def test_sandwich_is_exact_at_equal_integer_blocks(self):
        for state_count in range(4, 61):
            for block_count in range(2, state_count):
                if state_count % block_count:
                    continue
                self.assertEqual(
                    balanced_total_safe_probability(
                        state_count, block_count
                    ),
                    ideal_equal_block_probability(
                        state_count, block_count
                    ),
                )
                self.assertEqual(
                    balanced_rounding_correction(
                        state_count, block_count
                    ),
                    1,
                )

    def test_ideal_candidate_window_contains_true_global_valley(self):
        for state_count in range(3, 121):
            self.assertTrue(
                true_valley_lies_in_ideal_candidate_window(state_count)
            )
            report = operation_valley_sandwich_report(state_count)
            self.assertIn(
                report.true_block_count,
                report.candidate_block_counts,
            )
            self.assertIn(
                report.ideal_integer_block_count,
                report.candidate_block_counts,
            )

    def test_candidate_window_is_exactly_defined_by_surrogate_threshold(self):
        for state_count in range(3, 60):
            b0 = ideal_integer_block_count(state_count)
            threshold = (
                4**b0
                * ideal_equal_block_probability(state_count, b0)
            )
            expected = tuple(
                block_count
                for block_count in range(2, state_count)
                if ideal_equal_block_probability(
                    state_count, block_count
                )
                <= threshold
            )
            self.assertEqual(
                ideal_candidate_block_counts(state_count),
                expected,
            )

    def test_integer_surrogate_minimum_has_expected_reference_values(self):
        # These are exact integer minimizers of b^(b-n), not Lambert-W rounded
        # guesses.  They lock the finite surrogate used by the candidate window.
        expected = {
            3: 2,
            4: 2,
            5: 3,
            6: 3,
            8: 4,
            10: 5,
            12: 5,
            20: 8,
            30: 11,
        }
        for state_count, block_count in expected.items():
            self.assertEqual(
                ideal_integer_block_count(state_count),
                block_count,
            )

    def test_rounding_correction_can_be_strict_for_unequal_balanced_blocks(self):
        strict = []
        for state_count in range(3, 30):
            for block_count in range(2, state_count):
                if state_count % block_count == 0:
                    continue
                correction = balanced_rounding_correction(
                    state_count, block_count
                )
                if correction > 1:
                    strict.append((state_count, block_count))
        self.assertTrue(strict)

    def test_validation(self):
        with self.assertRaises(ValueError):
            ideal_equal_block_probability(2, 1)
        with self.assertRaises(ValueError):
            ideal_equal_block_probability(5, 5)
        with self.assertRaises(TypeError):
            ideal_equal_block_probability(True, 2)
        with self.assertRaises(ValueError):
            ideal_integer_block_count(2)


if __name__ == "__main__":
    unittest.main()
