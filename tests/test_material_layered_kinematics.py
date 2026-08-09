import unittest

from enterprise_math.material_layered_kinematics import (
    compare_two_layer_orders,
    staged_layer_order,
)


class MaterialLayeredKinematicsTests(unittest.TestCase):
    def test_staged_projection_is_direct_or_exactly_one_below(self):
        for budget in range(0, 20):
            for a1 in range(1, 8):
                for r1 in range(a1 + 1):
                    for a2 in range(1, 8):
                        for r2 in range(a2 + 1):
                            report = staged_layer_order(budget, r1, a1, r2, a2)
                            self.assertIn(report.direct_minus_staged, (0, 1))
                            self.assertEqual(
                                report.direct_minus_staged,
                                report.carry_bit,
                            )

    def test_layer_exchange_changes_staged_budget_by_at_most_one(self):
        saw_positive = False
        saw_negative = False
        saw_equal = False
        for budget in range(0, 20):
            for a1 in range(1, 8):
                for r1 in range(a1 + 1):
                    for a2 in range(1, 8):
                        for r2 in range(a2 + 1):
                            report = compare_two_layer_orders(
                                budget, r1, a1, r2, a2
                            )
                            self.assertLessEqual(report.absolute_order_difference, 1)
                            self.assertEqual(
                                report.direct_budget,
                                budget * r1 * r2 // (a1 * a2),
                            )
                            if report.signed_order_difference > 0:
                                saw_positive = True
                            elif report.signed_order_difference < 0:
                                saw_negative = True
                            else:
                                saw_equal = True
        self.assertTrue(saw_positive)
        self.assertTrue(saw_negative)
        self.assertTrue(saw_equal)

    def test_full_response_layer_is_projection_identity(self):
        for budget in range(0, 30):
            for amplitude in range(1, 10):
                report = staged_layer_order(
                    budget,
                    amplitude,
                    amplitude,
                    3,
                    7,
                )
                self.assertEqual(report.staged_budget, budget * 3 // 7)
                self.assertEqual(report.direct_minus_staged, 0)

    def test_zero_response_layer_annihilates_both_orders(self):
        report = compare_two_layer_orders(17, 0, 5, 4, 7)
        self.assertEqual(report.direct_budget, 0)
        self.assertEqual(report.order_12.staged_budget, 0)
        self.assertEqual(report.order_21.staged_budget, 0)
        self.assertEqual(report.absolute_order_difference, 0)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            staged_layer_order(-1, 1, 2, 1, 2)
        with self.assertRaises(ValueError):
            staged_layer_order(1, 3, 2, 1, 2)
        with self.assertRaises(ValueError):
            staged_layer_order(1, 1, 0, 1, 2)
        with self.assertRaises(ValueError):
            compare_two_layer_orders(1, 1, 2, 3, 2)


if __name__ == "__main__":
    unittest.main()
