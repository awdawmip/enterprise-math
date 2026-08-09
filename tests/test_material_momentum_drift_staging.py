import unittest

from enterprise_math.material_momentum_drift_staging import (
    lifted_momentum_drift_staging_report,
)


class MaterialMomentumDriftStagingTests(unittest.TestCase):
    def test_exact_defect_formula_matches_direct_projection_on_small_domain(self):
        for divisor in range(1, 9):
            for whole in range(0, 9):
                for detail in range(divisor):
                    for multiplier in range(0, 12):
                        for drift_divisor in range(1, 8):
                            report = lifted_momentum_drift_staging_report(
                                whole,
                                detail,
                                divisor,
                                multiplier,
                                drift_divisor,
                            )
                            self.assertEqual(
                                report.displacement_defect_count,
                                report.defect_formula_count,
                            )
                            self.assertGreaterEqual(report.displacement_defect_count, 0)

    def test_zero_whole_momentum_can_move_under_lifted_drift(self):
        report = lifted_momentum_drift_staging_report(
            whole_momentum_count=0,
            momentum_detail_numerator=3,
            momentum_detail_divisor=4,
            drift_multiplier=4,
            drift_divisor=1,
        )
        self.assertEqual(report.staged_displacement_count, 0)
        self.assertEqual(report.direct_lifted_displacement_count, 3)
        self.assertEqual(report.displacement_defect_count, 3)
        self.assertFalse(report.whole_momentum_quotient_safe_for_position)

    def test_zero_momentum_detail_makes_lifted_and_staged_drift_equal(self):
        for whole in range(0, 10):
            for multiplier in range(0, 10):
                for drift_divisor in range(1, 8):
                    report = lifted_momentum_drift_staging_report(
                        whole, 0, 5, multiplier, drift_divisor
                    )
                    self.assertEqual(report.displacement_defect_count, 0)
                    self.assertTrue(report.whole_momentum_quotient_safe_for_position)

    def test_retained_detail_can_cross_multiple_position_cells(self):
        report = lifted_momentum_drift_staging_report(1, 9, 10, 25, 1)
        self.assertEqual(report.staged_displacement_count, 25)
        self.assertEqual(report.direct_lifted_displacement_count, 47)
        self.assertEqual(report.displacement_defect_count, 22)

    def test_zero_drift_multiplier_makes_momentum_detail_future_invisible(self):
        report = lifted_momentum_drift_staging_report(3, 4, 5, 0, 7)
        self.assertEqual(report.staged_displacement_count, 0)
        self.assertEqual(report.direct_lifted_displacement_count, 0)
        self.assertTrue(report.whole_momentum_quotient_safe_for_position)

    def test_invalid_detail_and_divisors_are_rejected(self):
        with self.assertRaises(ValueError):
            lifted_momentum_drift_staging_report(0, 4, 4, 1, 1)
        with self.assertRaises(ValueError):
            lifted_momentum_drift_staging_report(0, 0, 0, 1, 1)
        with self.assertRaises(ValueError):
            lifted_momentum_drift_staging_report(0, 0, 1, 1, 0)


if __name__ == "__main__":
    unittest.main()
