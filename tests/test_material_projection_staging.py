import unittest

from enterprise_math.material_projection_staging import (
    response_impulse_staging_report,
)


class MaterialProjectionStagingTests(unittest.TestCase):
    def test_exact_remainder_formula_matches_direct_and_staged_projection(self):
        for amplitude in range(1, 10):
            for response in range(amplitude + 1):
                for force_max in range(0, 12):
                    for multiplier in range(0, 14):
                        for divisor in range(1, 9):
                            report = response_impulse_staging_report(
                                response,
                                amplitude,
                                force_max,
                                multiplier,
                                divisor,
                            )
                            self.assertEqual(report.defect_count, report.defect_formula_count)
                            self.assertGreaterEqual(report.defect_count, 0)

    def test_zero_whole_force_can_still_produce_nonzero_direct_impulse(self):
        report = response_impulse_staging_report(
            response_sample=1,
            response_amplitude=2,
            full_scale_force_count=1,
            impulse_multiplier=8,
            impulse_divisor=1,
        )
        self.assertEqual(report.force_count, 0)
        self.assertEqual(report.force_remainder, 1)
        self.assertEqual(report.staged_impulse_count, 0)
        self.assertEqual(report.direct_impulse_count, 4)
        self.assertEqual(report.defect_count, 4)
        self.assertFalse(report.intermediate_force_projection_safe)

    def test_staging_defect_can_exceed_one_count(self):
        report = response_impulse_staging_report(7, 9, 14, 29, 1)
        self.assertEqual(report.defect_count, 25)
        self.assertGreater(report.defect_count, 1)

    def test_exact_intermediate_force_has_zero_defect(self):
        for amplitude in range(1, 12):
            report = response_impulse_staging_report(
                response_sample=amplitude,
                response_amplitude=amplitude,
                full_scale_force_count=7,
                impulse_multiplier=13,
                impulse_divisor=5,
            )
            self.assertEqual(report.force_remainder, 0)
            self.assertEqual(report.defect_count, 0)
            self.assertTrue(report.intermediate_force_projection_safe)

    def test_zero_multiplier_makes_intermediate_projection_future_safe_for_this_task(self):
        report = response_impulse_staging_report(1, 3, 2, 0, 7)
        self.assertEqual(report.direct_impulse_count, 0)
        self.assertEqual(report.staged_impulse_count, 0)
        self.assertTrue(report.intermediate_force_projection_safe)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            response_impulse_staging_report(2, 1, 1, 1, 1)
        with self.assertRaises(ValueError):
            response_impulse_staging_report(0, 0, 1, 1, 1)
        with self.assertRaises(ValueError):
            response_impulse_staging_report(0, 1, 1, 1, 0)


if __name__ == "__main__":
    unittest.main()
