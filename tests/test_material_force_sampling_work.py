import unittest

from enterprise_math.material_force_sampling_work import (
    current_hold_work_over_explicit_saved_schedule,
    saved_force_sampling_work_report,
)
from enterprise_math.material_force_work import FiniteForceLaw, uniform_force_law
from enterprise_math.material_response import explicit_material_curve_profile


class MaterialForceSamplingWorkTests(unittest.TestCase):
    def test_monotone_hardening_orders_current_chord_endpoint_work(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 1, 4), returning=(0, 1, 4), amplitude=4
            )
        )
        report = saved_force_sampling_work_report(law, 0, 2)
        self.assertEqual(report.current_hold_work_numerator2, 0)
        self.assertEqual(report.chord_work_numerator2, 6)
        self.assertEqual(report.endpoint_hold_work_numerator2, 16)
        self.assertEqual(report.current_sampling_defect_numerator2, 6)
        self.assertEqual(report.endpoint_sampling_defect_numerator2, 10)
        self.assertEqual(
            (report.exact_average_force_numerator, report.exact_average_force_denominator),
            (3, 2),
        )
        self.assertTrue(report.loading_nondecreasing_on_interval)

    def test_constant_force_has_no_sampling_defect(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(3, 3, 3, 3), returning=(3, 3, 3, 3), amplitude=3
            )
        )
        for start in range(0, 3):
            for end in range(start + 1, 4):
                report = saved_force_sampling_work_report(law, start, end)
                self.assertEqual(report.current_sampling_defect_numerator2, 0)
                self.assertEqual(report.endpoint_sampling_defect_numerator2, 0)
                self.assertEqual(
                    (report.exact_average_force_numerator, report.exact_average_force_denominator),
                    (3, 1),
                )

    def test_irregular_deformation_grid_is_used_exactly(self):
        profile = explicit_material_curve_profile(
            loading=(0, 2, 5, 9), returning=(0, 2, 5, 9), amplitude=9
        )
        law = FiniteForceLaw(
            profile=profile,
            deformation_counts=(0, 2, 5, 11),
            force_scale_factor=1,
            force_unit="F",
            deformation_scale_factor=1,
            deformation_unit="x",
        )
        report = saved_force_sampling_work_report(law, 1, 3)
        expected_chord2 = (2 + 5) * 3 + (5 + 9) * 6
        self.assertEqual(report.chord_work_numerator2, expected_chord2)
        self.assertEqual(report.current_hold_work_numerator2, 2 * 2 * 9)
        self.assertEqual(report.endpoint_hold_work_numerator2, 2 * 9 * 9)

    def test_more_saved_force_samples_increase_left_hold_work_for_hardening_curve(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 1, 4, 9, 16), returning=(0, 1, 4, 9, 16), amplitude=16
            )
        )
        coarse = current_hold_work_over_explicit_saved_schedule(law, (0, 4))
        medium = current_hold_work_over_explicit_saved_schedule(law, (0, 2, 4))
        fine = current_hold_work_over_explicit_saved_schedule(law, (0, 1, 2, 3, 4))
        chord = saved_force_sampling_work_report(law, 0, 4).chord_work_numerator2
        self.assertLess(coarse, medium)
        self.assertLess(medium, fine)
        self.assertLess(fine, chord)

    def test_nonmonotone_force_can_reverse_the_simple_ordering(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 10, 1), returning=(0, 10, 1), amplitude=10
            )
        )
        report = saved_force_sampling_work_report(law, 1, 2)
        self.assertFalse(report.loading_nondecreasing_on_interval)
        self.assertGreater(report.current_hold_work_numerator2, report.chord_work_numerator2)
        self.assertLess(report.endpoint_hold_work_numerator2, report.chord_work_numerator2)

    def test_invalid_depth_and_schedule_inputs_are_rejected(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 1, 2), returning=(0, 1, 2), amplitude=2
            )
        )
        with self.assertRaises(ValueError):
            saved_force_sampling_work_report(law, 1, 1)
        with self.assertRaises(ValueError):
            current_hold_work_over_explicit_saved_schedule(law, (0, 2, 1))
        with self.assertRaises(ValueError):
            current_hold_work_over_explicit_saved_schedule(law, (0,))


if __name__ == "__main__":
    unittest.main()
