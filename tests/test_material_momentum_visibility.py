import unittest

from enterprise_math.material_momentum_visibility import (
    EXACT_STOP,
    HIDDEN_INWARD,
    HIDDEN_OUTWARD,
    VISIBLE_INWARD,
    VISIBLE_OUTWARD,
    momentum_visibility_report,
    momentum_visibility_thresholds,
)


class MaterialMomentumVisibilityTests(unittest.TestCase):
    def test_exact_thresholds_split_lifted_and_whole_direction(self):
        thresholds = momentum_visibility_thresholds(10, 4)
        self.assertEqual(thresholds.first_whole_zero_impulse, 7)
        self.assertEqual(thresholds.exact_lifted_stop_impulse, 10)
        self.assertEqual(thresholds.first_lifted_outward_impulse, 11)
        self.assertEqual(thresholds.first_whole_outward_impulse, 14)
        self.assertEqual(thresholds.hidden_outward_impulse_count, 3)

    def test_reference_visibility_sequence_contains_hidden_outward_band(self):
        phases = [momentum_visibility_report(10, impulse, 4).visibility_phase for impulse in range(0, 16)]
        self.assertEqual(phases[:7], [VISIBLE_INWARD] * 7)
        self.assertEqual(phases[7:10], [HIDDEN_INWARD] * 3)
        self.assertEqual(phases[10], EXACT_STOP)
        self.assertEqual(phases[11:14], [HIDDEN_OUTWARD] * 3)
        self.assertEqual(phases[14:], [VISIBLE_OUTWARD] * 2)

    def test_hidden_outward_is_already_true_lifted_reversal(self):
        report = momentum_visibility_report(10, 11, 4)
        self.assertEqual(report.lifted_momentum, -1)
        self.assertEqual(report.whole_inward_momentum_count, 0)
        self.assertTrue(report.lifted_outward)
        self.assertFalse(report.whole_outward_visible)
        self.assertEqual(report.visibility_phase, HIDDEN_OUTWARD)

    def test_divisor_one_has_no_hidden_nonzero_band(self):
        thresholds = momentum_visibility_thresholds(5, 1)
        self.assertEqual(thresholds.hidden_outward_impulse_count, 0)
        self.assertEqual(momentum_visibility_report(5, 4, 1).visibility_phase, VISIBLE_INWARD)
        self.assertEqual(momentum_visibility_report(5, 5, 1).visibility_phase, EXACT_STOP)
        self.assertEqual(momentum_visibility_report(5, 6, 1).visibility_phase, VISIBLE_OUTWARD)

    def test_general_partition_matches_direct_whole_quotient(self):
        for pi0 in range(1, 30):
            for divisor in range(1, 9):
                for impulse in range(0, pi0 + 2 * divisor + 3):
                    report = momentum_visibility_report(pi0, impulse, divisor)
                    pi = pi0 - impulse
                    expected_whole = pi // divisor if pi >= 0 else -((-pi) // divisor)
                    self.assertEqual(report.whole_inward_momentum_count, expected_whole)
                    self.assertEqual(report.lifted_outward, pi < 0)
                    self.assertEqual(report.whole_outward_visible, expected_whole < 0)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            momentum_visibility_report(0, 0, 1)
        with self.assertRaises(ValueError):
            momentum_visibility_report(1, -1, 1)
        with self.assertRaises(ValueError):
            momentum_visibility_thresholds(1, 0)


if __name__ == "__main__":
    unittest.main()
