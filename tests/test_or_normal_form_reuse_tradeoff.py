import unittest

from enterprise_math.or_normal_form_reuse_tradeoff import (
    independent_fused_work,
    materialization_work_saving,
    materialized_reuse_work,
    or_normal_form_reuse_report,
)


class ORNormalFormReuseTradeoffTests(unittest.TestCase):
    def test_q_one_has_same_work_and_possible_depth_tax(self):
        report = or_normal_form_reuse_report(5, 20, 1)
        self.assertEqual(report.materialized_work, 100)
        self.assertEqual(report.fused_work, 100)
        self.assertEqual(report.work_saving, 0)
        self.assertFalse(report.materialization_saves_work)
        self.assertEqual(report.materialization_depth_tax, 1)

    def test_reuse_saves_exact_formula(self):
        for k in (1, 3, 8):
            for horizon in (1, 2, 5, 20):
                for reuse in (1, 2, 10):
                    materialized = materialized_reuse_work(k, horizon, reuse)
                    fused = independent_fused_work(k, horizon, reuse)
                    saving = materialization_work_saving(k, horizon, reuse)
                    self.assertEqual(fused - materialized, saving)
                    self.assertEqual(saving, k * (reuse - 1) * (horizon - 1))

    def test_large_reuse_makes_materialization_valuable(self):
        report = or_normal_form_reuse_report(16, 64, 100)
        self.assertEqual(report.work_saving, 16 * 99 * 63)
        self.assertTrue(report.materialization_saves_work)
        self.assertIn(report.materialization_depth_tax, (0, 1))

    def test_power_of_two_horizon_has_no_parallel_depth_tax(self):
        for horizon in (1, 2, 4, 8, 16, 64):
            report = or_normal_form_reuse_report(5, horizon, 10)
            self.assertEqual(report.materialization_depth_tax, 0)
            self.assertTrue(report.materialization_saves_work or horizon == 1)

    def test_validation(self):
        with self.assertRaises(ValueError):
            materialized_reuse_work(2, 3, 0)
        with self.assertRaises(ValueError):
            independent_fused_work(False, 3, 1)


if __name__ == "__main__":
    unittest.main()
