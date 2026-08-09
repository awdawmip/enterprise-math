import unittest

from enterprise_math.material_hysteresis import LOADING, RETURNING
from enterprise_math.material_physical_projection import ForceImpulseCountScale
from enterprise_math.material_response import explicit_material_curve_profile
from enterprise_math.material_strength_depth import (
    material_physical_strength_depth_report,
    minimum_collapse_factor_for_physical_strength,
)


def unit_scale(tick=1):
    return ForceImpulseCountScale(
        force_scale_factor=1,
        time_scale_factor=1,
        momentum_scale_factor=1,
        tick_duration_count=tick,
        force_unit="F",
        time_unit="T",
        momentum_unit="P",
    )


class MaterialPhysicalStrengthDepthTests(unittest.TestCase):
    def setUp(self):
        self.profile = explicit_material_curve_profile(
            loading=(0, 10, 20, 40, 80, 100),
            returning=(0, 5, 15, 30, 60, 90),
            amplitude=100,
        )

    def test_static_loading_strength_layer_appears_only_after_response_curve_crosses_exact_threshold(self):
        report = material_physical_strength_depth_report(
            self.profile,
            LOADING,
            full_scale_force_count=1,
            scale=unit_scale(),
            closing_score=1,
            self_coupling=2,
        )
        self.assertEqual(report.strength_per_response_sample, 2)
        self.assertEqual(report.required_strength_product, 100)
        self.assertEqual(report.required_response_sample, 50)
        self.assertEqual(report.first_sufficient_positive_depth, 4)
        self.assertEqual(report.sufficient_positive_depths, (4, 5))
        self.assertTrue(report.any_represented_depth_physically_strong_enough)
        self.assertEqual(
            minimum_collapse_factor_for_physical_strength(3, report),
            7,
        )

    def test_stronger_force_scale_moves_physical_activation_outward_without_changing_curve(self):
        weak = material_physical_strength_depth_report(
            self.profile, LOADING, 1, unit_scale(), 1, 2
        )
        strong = material_physical_strength_depth_report(
            self.profile, LOADING, 5, unit_scale(), 1, 2
        )
        self.assertEqual(weak.first_sufficient_positive_depth, 4)
        self.assertEqual(strong.required_response_sample, 10)
        self.assertEqual(strong.first_sufficient_positive_depth, 1)

    def test_loading_and_returning_can_have_different_physical_strength_depths(self):
        loading = material_physical_strength_depth_report(
            self.profile, LOADING, 2, unit_scale(), 1, 2
        )
        returning = material_physical_strength_depth_report(
            self.profile, RETURNING, 2, unit_scale(), 1, 2
        )
        self.assertEqual(loading.required_response_sample, 25)
        self.assertEqual(returning.required_response_sample, 25)
        self.assertEqual(loading.first_sufficient_positive_depth, 3)
        self.assertEqual(returning.first_sufficient_positive_depth, 3)
        # Increase the demand so the weaker return branch activates later.
        loading2 = material_physical_strength_depth_report(
            self.profile, LOADING, 2, unit_scale(), 3, 4
        )
        returning2 = material_physical_strength_depth_report(
            self.profile, RETURNING, 2, unit_scale(), 3, 4
        )
        self.assertEqual(loading2.required_response_sample, 38)
        self.assertEqual(returning2.required_response_sample, 38)
        self.assertEqual(loading2.first_sufficient_positive_depth, 3)
        self.assertEqual(returning2.first_sufficient_positive_depth, 4)

    def test_zero_tick_or_physically_too_weak_material_has_no_strength_layer(self):
        zero_tick = material_physical_strength_depth_report(
            self.profile, LOADING, 10, unit_scale(tick=0), 1, 2
        )
        self.assertIsNone(zero_tick.required_response_sample)
        self.assertIsNone(zero_tick.first_sufficient_positive_depth)
        self.assertIsNone(
            minimum_collapse_factor_for_physical_strength(2, zero_tick)
        )

        too_weak = material_physical_strength_depth_report(
            self.profile, LOADING, 1, unit_scale(), 3, 1
        )
        self.assertIsNone(too_weak.required_response_sample)
        self.assertIsNone(too_weak.first_sufficient_positive_depth)

    def test_physical_unit_scales_change_threshold_by_cross_products_not_hidden_float_conversion(self):
        scale = ForceImpulseCountScale(
            force_scale_factor=2,
            time_scale_factor=5,
            momentum_scale_factor=3,
            tick_duration_count=4,
            force_unit="F",
            time_unit="T",
            momentum_unit="P",
        )
        report = material_physical_strength_depth_report(
            self.profile,
            LOADING,
            full_scale_force_count=7,
            scale=scale,
            closing_score=2,
            self_coupling=3,
        )
        # G=7*4*3*3=252; H=2*100*2*5=2000; ceil(H/G)=8.
        self.assertEqual(report.strength_per_response_sample, 252)
        self.assertEqual(report.required_strength_product, 2000)
        self.assertEqual(report.required_response_sample, 8)
        self.assertEqual(report.first_sufficient_positive_depth, 1)

    def test_nonmonotone_branch_is_rejected_for_single_threshold_theorem(self):
        nonmonotone = explicit_material_curve_profile(
            loading=(0, 50, 30, 80),
            returning=(0, 20, 40, 60),
            amplitude=100,
        )
        with self.assertRaises(ValueError):
            material_physical_strength_depth_report(
                nonmonotone, LOADING, 1, unit_scale(), 1, 2
            )

    def test_invalid_gap_or_branch_is_rejected(self):
        report = material_physical_strength_depth_report(
            self.profile, LOADING, 1, unit_scale(), 1, 2
        )
        with self.assertRaises(ValueError):
            minimum_collapse_factor_for_physical_strength(0, report)
        with self.assertRaises(ValueError):
            material_physical_strength_depth_report(
                self.profile, "UNKNOWN", 1, unit_scale(), 1, 2
            )


if __name__ == "__main__":
    unittest.main()
