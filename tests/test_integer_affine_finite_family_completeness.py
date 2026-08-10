import unittest

from enterprise_math.integer_affine_finite_family_completeness import (
    finite_family_complete_for_all_targets,
    finite_family_complete_for_rational_image_targets,
    finite_family_lcm,
    finite_modular_family_completeness_report,
)


class IntegerAffineFiniteFamilyCompletenessTests(unittest.TestCase):
    def test_full_row_rank_family_complete_exactly_when_lcm_contains_exponent(self):
        matrix = (
            (2, 0),
            (0, 6),
        )
        cases = (
            ((2, 3), 6, True),
            ((4, 3), 12, True),
            ((2,), 2, False),
            ((3,), 3, False),
            ((4, 6), 12, True),
        )
        for family, expected_lcm, expected in cases:
            self.assertEqual(finite_family_lcm(family), expected_lcm)
            self.assertEqual(
                finite_family_complete_for_all_targets(matrix, family),
                expected,
            )
            self.assertEqual(
                finite_family_complete_for_rational_image_targets(matrix, family),
                expected,
            )

    def test_rank_deficient_family_can_be_complete_on_rational_image_but_not_all_targets(self):
        matrix = (
            (2,),
            (0,),
        )
        for family in ((2,), (2, 3), (4, 6)):
            report = finite_modular_family_completeness_report(matrix, family)
            self.assertTrue(report.rational_image_complete)
            self.assertFalse(report.all_target_complete)
            self.assertEqual(report.free_cokernel_rank, 1)
            self.assertEqual(report.torsion_exponent, 2)

    def test_rank_deficient_torsion_incomplete_family_fails_both_levels(self):
        matrix = (
            (6,),
            (0,),
        )
        report = finite_modular_family_completeness_report(matrix, (2,))
        self.assertFalse(report.rational_image_complete)
        self.assertFalse(report.all_target_complete)
        self.assertEqual(report.lcm_ceiling, 2)
        self.assertEqual(report.torsion_exponent, 6)

    def test_same_lcm_means_same_completeness(self):
        matrix = ((12,),)
        families = (
            (12,),
            (3, 4),
            (2, 3, 4),
            (4, 6),
        )
        reports = [finite_modular_family_completeness_report(matrix, family) for family in families]
        self.assertTrue(all(report.lcm_ceiling == 12 for report in reports))
        self.assertTrue(all(report.all_target_complete for report in reports))

    def test_surjective_map_is_complete_even_at_modulus_one(self):
        matrix = (
            (1, 0),
            (0, 1),
        )
        report = finite_modular_family_completeness_report(matrix, (1,))
        self.assertTrue(report.rational_image_complete)
        self.assertTrue(report.all_target_complete)
        self.assertEqual(report.torsion_exponent, 1)

    def test_validation(self):
        with self.assertRaises(ValueError):
            finite_family_lcm(())
        with self.assertRaises(ValueError):
            finite_family_lcm((0,))
        with self.assertRaises(TypeError):
            finite_family_lcm((True,))


if __name__ == "__main__":
    unittest.main()
