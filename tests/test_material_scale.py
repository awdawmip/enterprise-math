import unittest

from enterprise_math.material_scale import (
    hardening_scale_report,
    softening_scale_report,
)


class MaterialScaleTests(unittest.TestCase):
    def test_softening_is_exactly_homogeneous_under_integer_refinement(self):
        for amplitude in range(1, 18):
            for sample in range(amplitude + 1):
                for power in range(1, 5):
                    for refinement in range(1, 7):
                        report = softening_scale_report(
                            sample, amplitude, power, refinement
                        )
                        self.assertEqual(report.defect, 0)
                        self.assertEqual(
                            report.scaled_value,
                            refinement * report.base_value,
                        )

    def test_hardening_defect_is_exact_bounded_remainder_carry(self):
        saw_positive_defect = False
        for amplitude in range(1, 18):
            for sample in range(amplitude + 1):
                for power in range(1, 5):
                    for refinement in range(1, 7):
                        report = hardening_scale_report(
                            sample, amplitude, power, refinement
                        )
                        self.assertEqual(
                            report.defect,
                            report.expected_defect_from_remainder,
                        )
                        self.assertGreaterEqual(report.defect, 0)
                        self.assertLess(report.defect, refinement)
                        self.assertEqual(
                            report.scaled_value,
                            report.transported_base + report.defect,
                        )
                        saw_positive_defect |= report.defect > 0
        self.assertTrue(saw_positive_defect)

    def test_exact_divisibility_removes_hardening_scale_defect(self):
        report = hardening_scale_report(50, 100, power=2, refinement=7)
        self.assertEqual(report.base_remainder, 0)
        self.assertEqual(report.defect, 0)
        self.assertEqual(report.scaled_value, 7 * report.base_value)

    def test_nonzero_remainder_can_create_refinement_shell(self):
        report = hardening_scale_report(33, 100, power=2, refinement=7)
        self.assertGreater(report.base_remainder, 0)
        self.assertGreater(report.defect, 0)
        self.assertLess(report.defect, 7)


if __name__ == "__main__":
    unittest.main()
