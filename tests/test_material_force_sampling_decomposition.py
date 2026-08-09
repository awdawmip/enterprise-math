import unittest

from enterprise_math.material_force_sampling_decomposition import (
    force_sampling_defect_decomposition,
    inserted_saved_state_work_gain_numerator2,
)
from enterprise_math.material_force_work import FiniteForceLaw, uniform_force_law
from enterprise_math.material_response import explicit_material_curve_profile


class MaterialForceSamplingDecompositionTests(unittest.TestCase):
    def test_hardening_static_defect_splits_exactly_into_sampling_and_integrator_parts(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 1, 4, 9, 16), returning=(0, 1, 4, 9, 16), amplitude=16
            )
        )
        report = force_sampling_defect_decomposition(law, (0, 2, 4))
        self.assertEqual(
            report.total_static_defect_numerator2,
            report.state_sampling_defect_numerator2
            + report.integrator_pairing_defect_numerator2,
        )
        self.assertGreater(report.state_sampling_defect_numerator2, 0)
        self.assertGreater(report.integrator_pairing_defect_numerator2, 0)
        self.assertTrue(report.loading_nondecreasing)

    def test_full_saved_grid_removes_only_state_sampling_defect(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 1, 4, 9), returning=(0, 1, 4, 9), amplitude=9
            )
        )
        report = force_sampling_defect_decomposition(law, (0, 1, 2, 3))
        self.assertEqual(report.state_sampling_defect_numerator2, 0)
        expected_pairing = (1 - 0) + (4 - 1) + (9 - 4)
        self.assertEqual(report.integrator_pairing_defect_numerator2, expected_pairing)
        self.assertEqual(report.total_static_defect_numerator2, expected_pairing)

    def test_inserting_saved_state_has_exact_nonnegative_gain_for_hardening_force(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 2, 5, 9, 14), returning=(0, 2, 5, 9, 14), amplitude=14
            )
        )
        gain = inserted_saved_state_work_gain_numerator2(law, 0, 2, 4)
        self.assertEqual(gain, 2 * (5 - 0) * (4 - 2))
        self.assertGreater(gain, 0)

    def test_irregular_grid_insertion_gain_uses_remaining_physical_width(self):
        profile = explicit_material_curve_profile(
            loading=(1, 3, 8, 10), returning=(1, 3, 8, 10), amplitude=10
        )
        law = FiniteForceLaw(
            profile=profile,
            deformation_counts=(0, 2, 5, 11),
            force_scale_factor=1,
            force_unit="F",
            deformation_scale_factor=1,
            deformation_unit="x",
        )
        gain = inserted_saved_state_work_gain_numerator2(law, 0, 2, 3)
        self.assertEqual(gain, 2 * (8 - 1) * (11 - 5))

    def test_constant_force_has_zero_sampling_and_integrator_defects(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(4, 4, 4, 4), returning=(4, 4, 4, 4), amplitude=4
            )
        )
        report = force_sampling_defect_decomposition(law, (0, 3))
        self.assertEqual(report.state_sampling_defect_numerator2, 0)
        self.assertEqual(report.integrator_pairing_defect_numerator2, 0)
        self.assertEqual(report.total_static_defect_numerator2, 0)

    def test_nonmonotone_curve_keeps_exact_additivity_without_sign_claim(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 10, 1, 8), returning=(0, 10, 1, 8), amplitude=10
            )
        )
        report = force_sampling_defect_decomposition(law, (0, 3))
        self.assertFalse(report.loading_nondecreasing)
        self.assertEqual(
            report.total_static_defect_numerator2,
            report.state_sampling_defect_numerator2
            + report.integrator_pairing_defect_numerator2,
        )

    def test_invalid_schedules_and_insertions_are_rejected(self):
        law = uniform_force_law(
            explicit_material_curve_profile(
                loading=(0, 1, 2), returning=(0, 1, 2), amplitude=2
            )
        )
        with self.assertRaises(ValueError):
            force_sampling_defect_decomposition(law, (0, 2, 1))
        with self.assertRaises(ValueError):
            inserted_saved_state_work_gain_numerator2(law, 0, 2, 1)


if __name__ == "__main__":
    unittest.main()
