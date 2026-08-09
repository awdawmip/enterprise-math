import unittest

from enterprise_math.material_precision_compatibility import (
    MATERIAL_UNDERRESOLVED,
    REPRESENTED_CONTACT,
    RESOLVED,
    spatial_material_compatibility,
)
from enterprise_math.material_response import material_curve_profile


class MaterialPrecisionCompatibilityTests(unittest.TestCase):
    def setUp(self):
        # Four samples represent deformation depths 0..3.
        self.profile = material_curve_profile(
            (0, 100, 200, 300),
            amplitude=300,
            loading_power=1,
            return_power=1,
        )

    def test_exact_three_region_factor_partition(self):
        gap = 2
        reports = [
            spatial_material_compatibility(gap, factor, self.profile)
            for factor in range(1, 9)
        ]
        self.assertEqual(
            [report.status for report in reports],
            [
                RESOLVED,
                RESOLVED,
                REPRESENTED_CONTACT,
                REPRESENTED_CONTACT,
                REPRESENTED_CONTACT,
                MATERIAL_UNDERRESOLVED,
                MATERIAL_UNDERRESOLVED,
                MATERIAL_UNDERRESOLVED,
            ],
        )
        self.assertEqual(
            [report.generated_depth for report in reports],
            [None, None, 1, 2, 3, 4, 5, 6],
        )
        self.assertTrue(all(report.finest_contact_factor == 3 for report in reports))
        self.assertTrue(
            all(report.coarsest_represented_contact_factor == 5 for report in reports)
        )

    def test_general_formula_matches_direct_depth_classification(self):
        for max_depth in range(1, 7):
            samples = tuple(range(max_depth + 1))
            profile = material_curve_profile(
                samples,
                amplitude=max_depth,
                loading_power=1,
                return_power=1,
            )
            for gap in range(1, 8):
                for factor in range(1, 14):
                    report = spatial_material_compatibility(gap, factor, profile)
                    if factor <= gap:
                        expected_status = RESOLVED
                        expected_depth = None
                    else:
                        expected_depth = factor - gap
                        expected_status = (
                            REPRESENTED_CONTACT
                            if expected_depth <= max_depth
                            else MATERIAL_UNDERRESOLVED
                        )
                    self.assertEqual(report.status, expected_status)
                    self.assertEqual(report.generated_depth, expected_depth)
                    self.assertEqual(report.finest_contact_factor, gap + 1)
                    self.assertEqual(
                        report.coarsest_represented_contact_factor,
                        gap + max_depth,
                    )

    def test_no_saturation_at_material_ceiling(self):
        # gap=1,d=6 generates depth 5, but this profile only represents 0..3.
        report = spatial_material_compatibility(1, 6, self.profile)
        self.assertEqual(report.status, MATERIAL_UNDERRESOLVED)
        self.assertEqual(report.generated_depth, 5)
        self.assertNotEqual(report.generated_depth, report.max_material_depth)

    def test_invalid_positive_gap_or_factor_is_rejected(self):
        with self.assertRaises(ValueError):
            spatial_material_compatibility(0, 1, self.profile)
        with self.assertRaises(ValueError):
            spatial_material_compatibility(1, 0, self.profile)


if __name__ == "__main__":
    unittest.main()
