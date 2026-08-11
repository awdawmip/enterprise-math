import unittest

from enterprise_math.or_circuit_execution_lower_bound import (
    fused_one_shot_mask,
    intermediate_materialization_depth_tax,
    one_shot_execution_depth_lower_bound,
    one_shot_execution_work_lower_bound,
    or_execution_lower_bound_report,
    reusable_normal_form_depth_lower_bound,
    reusable_normal_form_work_lower_bound,
    staged_depth_is_one_shot_optimal,
)


class ORCircuitExecutionLowerBoundTests(unittest.TestCase):
    def test_k5_h20_reference(self):
        report = or_execution_lower_bound_report(5, 20)
        self.assertEqual(report.reusable_normal_form_work, 95)
        self.assertEqual(report.reusable_normal_form_depth, 5)
        self.assertEqual(report.staged_one_shot_work, 100)
        self.assertEqual(report.staged_one_shot_depth, 6)
        self.assertEqual(report.fused_one_shot_work, 100)
        self.assertEqual(report.fused_one_shot_depth, 5)
        self.assertEqual(report.materialization_depth_tax, 1)
        self.assertTrue(report.fused_hits_work_lower_bound)
        self.assertTrue(report.fused_hits_depth_lower_bound)

    def test_depth_tax_is_zero_exactly_at_power_of_two_horizons(self):
        for horizon in range(1, 129):
            is_power_two = horizon & (horizon - 1) == 0
            self.assertEqual(
                staged_depth_is_one_shot_optimal(horizon),
                is_power_two,
            )
            self.assertEqual(
                intermediate_materialization_depth_tax(horizon),
                0 if is_power_two else 1,
            )

    def test_exact_lower_bound_formulas(self):
        for k in range(1, 10):
            for horizon in range(1, 65):
                self.assertEqual(
                    reusable_normal_form_work_lower_bound(k, horizon),
                    k * (horizon - 1),
                )
                self.assertEqual(
                    one_shot_execution_work_lower_bound(k, horizon),
                    k * horizon,
                )
                self.assertLessEqual(
                    one_shot_execution_depth_lower_bound(horizon),
                    reusable_normal_form_depth_lower_bound(horizon) + 1,
                )

    def test_fused_mask_semantics(self):
        state = 0b00101
        actions = (0b10000, 0b00010, 0b01000, 0b00010)
        expected = state
        for mask in actions:
            expected |= mask
        self.assertEqual(fused_one_shot_mask(state, actions, 5), expected)

    def test_validation(self):
        with self.assertRaises(ValueError):
            reusable_normal_form_work_lower_bound(0, 3)
        with self.assertRaises(ValueError):
            one_shot_execution_depth_lower_bound(0)
        with self.assertRaises(ValueError):
            fused_one_shot_mask(0, (), 3)


if __name__ == "__main__":
    unittest.main()
