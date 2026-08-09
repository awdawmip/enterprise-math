import unittest

from enterprise_math.material_oscillator import PythagoreanRotation
from enterprise_math.material_scale import (
    hardening_scale_report,
    rotation_scale_report,
    softening_scale_report,
)


class MaterialScaleTests(unittest.TestCase):
    def test_softening_refinement_has_exact_bounded_root_carry(self):
        saw_positive_defect = False
        for amplitude in range(1, 18):
            for sample in range(amplitude + 1):
                for power in range(1, 5):
                    for refinement in range(1, 7):
                        report = softening_scale_report(
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
                        self.assertEqual(
                            report.base_argument,
                            report.base_value**power + report.base_root_remainder,
                        )
                        saw_positive_defect |= report.defect > 0
        self.assertTrue(saw_positive_defect)

    def test_softening_exact_homogeneity_is_zero_carry_special_case(self):
        exact = softening_scale_report(50, 100, power=2, refinement=7)
        self.assertEqual(exact.base_root_remainder, 0)
        self.assertEqual(exact.defect, 0)
        self.assertEqual(exact.scaled_value, 7 * exact.base_value)

        shell = softening_scale_report(1, 3, power=2, refinement=2)
        self.assertEqual(shell.base_value, 1)
        self.assertEqual(shell.base_root_remainder, 2)
        self.assertEqual(shell.defect, 1)
        self.assertEqual(shell.scaled_value, 3)

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

    def test_rotation_refinement_defect_is_exactly_determined_by_base_details(self):
        rotation = PythagoreanRotation(3, 4, 5)
        saw_nonzero = False
        saw_negative = False
        saw_positive = False
        for x in range(-6, 7):
            for y in range(-6, 7):
                for refinement in range(1, 8):
                    report = rotation_scale_report((x, y), rotation, refinement)
                    self.assertEqual(
                        report.defects,
                        report.expected_defects_from_details,
                    )
                    self.assertEqual(
                        report.refined_after,
                        (
                            report.transported_base_after[0] + report.defects[0],
                            report.transported_base_after[1] + report.defects[1],
                        ),
                    )
                    self.assertTrue(
                        all(abs(defect) < refinement for defect in report.defects)
                    )
                    saw_nonzero |= report.defects != (0, 0)
                    saw_negative |= any(defect < 0 for defect in report.defects)
                    saw_positive |= any(defect > 0 for defect in report.defects)
        self.assertTrue(saw_nonzero)
        self.assertTrue(saw_negative)
        self.assertTrue(saw_positive)

    def test_exact_rotation_divisibility_removes_refinement_defect(self):
        rotation = PythagoreanRotation(3, 4, 5)
        report = rotation_scale_report((1, 2), rotation, refinement=7)
        self.assertEqual(report.base_details, (0, 0))
        self.assertEqual(report.defects, (0, 0))
        self.assertEqual(report.refined_after, report.transported_base_after)

    def test_exact_divisibility_removes_hardening_scale_defect(self):
        report = hardening_scale_report(50, 100, power=2, refinement=7)
        self.assertEqual(report.base_remainder, 0)
        self.assertEqual(report.defect, 0)
        self.assertEqual(report.scaled_value, 7 * report.base_value)

    def test_nonzero_remainder_can_create_hardening_refinement_shell(self):
        report = hardening_scale_report(33, 100, power=2, refinement=7)
        self.assertGreater(report.base_remainder, 0)
        self.assertGreater(report.defect, 0)
        self.assertLess(report.defect, 7)


if __name__ == "__main__":
    unittest.main()
