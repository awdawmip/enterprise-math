import unittest

from enterprise_math.material_kinematic_coupling_2d import (
    componentwise_return_vector,
    direction_budget_report_2d,
    direction_lock_residue_counts_2d,
    primitive_ray_locked_return_vector,
)


class MaterialKinematicCoupling2DTests(unittest.TestCase):
    def test_exact_tradeoff_identity_on_small_integer_domain(self):
        for x in range(-6, 7):
            for y in range(-6, 7):
                if x == 0 and y == 0:
                    continue
                for amplitude in range(1, 10):
                    for response in range(amplitude + 1):
                        report = direction_budget_report_2d(
                            (x, y), response, amplitude
                        )
                        self.assertEqual(
                            report.componentwise_linf_budget,
                            report.exact_linf_return_budget,
                        )
                        self.assertEqual(
                            report.ray_locked_budget_defect,
                            report.expected_defect_from_remainder,
                        )
                        self.assertEqual(
                            report.componentwise_preserves_primitive_ray,
                            report.remainder_lock_condition,
                        )
                        self.assertEqual(
                            report.componentwise_preserves_primitive_ray,
                            report.componentwise_vector
                            == report.primitive_ray_locked_vector,
                        )

    def test_axis_and_square_diagonal_are_always_ray_locked(self):
        vectors = ((7, 0), (-7, 0), (0, 9), (0, -9), (6, 6), (6, -6), (-6, 6))
        for vector in vectors:
            for amplitude in range(1, 13):
                for response in range(amplitude + 1):
                    report = direction_budget_report_2d(vector, response, amplitude)
                    self.assertEqual(report.primitive_linf, 1)
                    self.assertTrue(report.componentwise_preserves_primitive_ray)
                    self.assertEqual(report.ray_locked_budget_defect, 0)

    def test_general_primitive_slope_exposes_direction_budget_conflict(self):
        report = direction_budget_report_2d((2, 3), 2, 4)
        self.assertEqual(report.ray_scale, 1)
        self.assertEqual(report.primitive_direction, (2, 3))
        self.assertEqual(report.primitive_linf, 3)
        self.assertEqual(report.ray_remainder, 2)
        self.assertFalse(report.remainder_lock_condition)
        self.assertEqual(report.componentwise_vector, (1, 1))
        self.assertEqual(report.primitive_ray_locked_vector, (0, 0))
        self.assertEqual(report.exact_linf_return_budget, 1)
        self.assertEqual(report.ray_locked_budget_defect, 1)

    def test_joint_material_refinement_preserves_both_policies_and_lock_status(self):
        for vector in ((2, 3), (4, -6), (-5, 2), (9, 0), (7, 7)):
            for amplitude in range(1, 9):
                for response in range(amplitude + 1):
                    base = direction_budget_report_2d(vector, response, amplitude)
                    for refinement in (2, 3, 5):
                        refined = direction_budget_report_2d(
                            vector,
                            refinement * response,
                            refinement * amplitude,
                        )
                        self.assertEqual(
                            refined.componentwise_vector,
                            base.componentwise_vector,
                        )
                        self.assertEqual(
                            refined.primitive_ray_locked_vector,
                            base.primitive_ray_locked_vector,
                        )
                        self.assertEqual(
                            refined.componentwise_preserves_primitive_ray,
                            base.componentwise_preserves_primitive_ray,
                        )
                        self.assertEqual(
                            refined.ray_locked_budget_defect,
                            base.ray_locked_budget_defect,
                        )

    def test_closed_form_response_residue_counts_match_bruteforce(self):
        for x in range(-5, 6):
            for y in range(-5, 6):
                if x == 0 and y == 0:
                    continue
                for amplitude in range(1, 13):
                    counts = direction_lock_residue_counts_2d((x, y), amplitude)
                    brute_locked = sum(
                        direction_budget_report_2d(
                            (x, y), response, amplitude
                        ).componentwise_preserves_primitive_ray
                        for response in range(amplitude)
                    )
                    self.assertEqual(counts.locked_response_residues, brute_locked)
                    self.assertEqual(
                        counts.divergent_response_residues,
                        amplitude - brute_locked,
                    )

    def test_full_response_returns_original_vector_under_both_policies(self):
        for vector in ((2, 3), (-4, 6), (0, -8), (5, 5)):
            for amplitude in range(1, 10):
                self.assertEqual(
                    componentwise_return_vector(vector, amplitude, amplitude),
                    vector,
                )
                self.assertEqual(
                    primitive_ray_locked_return_vector(vector, amplitude, amplitude),
                    vector,
                )

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            direction_budget_report_2d((0, 0), 1, 2)
        with self.assertRaises(ValueError):
            direction_budget_report_2d((1, 2), -1, 2)
        with self.assertRaises(ValueError):
            direction_budget_report_2d((1, 2), 3, 2)
        with self.assertRaises(ValueError):
            direction_lock_residue_counts_2d((1, 2), 0)


if __name__ == "__main__":
    unittest.main()
