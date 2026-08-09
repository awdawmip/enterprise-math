import unittest

from enterprise_math.material_rebound_threshold import rebound_staircase
from enterprise_math.material_response import MaterialCurveProfile, material_curve_profile


class MaterialReboundThresholdTests(unittest.TestCase):
    def test_linear_return_branch_has_exact_unit_staircase(self):
        profile = material_curve_profile(
            (0, 200, 400, 600, 800, 1000),
            amplitude=1000,
            loading_power=1,
            return_power=1,
            return_retention=1000,
        )
        staircase = rebound_staircase(profile, incoming_budget=4, controlling_gap=2)
        self.assertEqual(
            tuple(th.minimum_response_sample for th in staircase.thresholds),
            (250, 500, 750, 1000),
        )
        self.assertEqual(
            tuple(th.first_deformation_depth for th in staircase.thresholds),
            (2, 3, 4, 5),
        )
        self.assertEqual(
            tuple(th.first_collapse_factor for th in staircase.thresholds),
            (4, 5, 6, 7),
        )
        self.assertEqual(staircase.maximum_representable_returned_budget, 4)

    def test_retained_return_branch_can_make_high_rebound_levels_unreachable(self):
        profile = material_curve_profile(
            (0, 200, 400, 600, 800, 1000),
            amplitude=1000,
            loading_power=1,
            return_power=1,
            return_retention=500,
        )
        staircase = rebound_staircase(profile, incoming_budget=4, controlling_gap=2)
        self.assertEqual(staircase.maximum_representable_returned_budget, 2)
        self.assertIsNotNone(staircase.thresholds[0].first_deformation_depth)
        self.assertIsNotNone(staircase.thresholds[1].first_deformation_depth)
        self.assertIsNone(staircase.thresholds[2].first_deformation_depth)
        self.assertIsNone(staircase.thresholds[3].first_deformation_depth)

    def test_threshold_formula_matches_direct_floor_budget_on_small_monotone_profiles(self):
        for amplitude in range(2, 15):
            returning = tuple(range(amplitude + 1))
            profile = MaterialCurveProfile(
                amplitude=amplitude,
                loading=returning,
                returning=returning,
                branch_gap=0,
                signed_area=0,
                peak_loading=amplitude,
                peak_returning=amplitude,
            )
            for budget in range(1, 8):
                staircase = rebound_staircase(profile, budget, controlling_gap=1)
                for threshold in staircase.thresholds:
                    level = threshold.returned_budget_level
                    expected_depth = next(
                        (
                            depth
                            for depth, sample in enumerate(returning)
                            if depth >= 1 and (budget * sample) // amplitude >= level
                        ),
                        None,
                    )
                    self.assertEqual(threshold.first_deformation_depth, expected_depth)

    def test_zero_budget_has_empty_staircase(self):
        profile = material_curve_profile(
            (0, 1, 2),
            amplitude=2,
            loading_power=1,
            return_power=1,
        )
        staircase = rebound_staircase(profile, 0, controlling_gap=1)
        self.assertEqual(staircase.thresholds, ())
        self.assertEqual(staircase.maximum_representable_returned_budget, 0)

    def test_nonmonotone_return_branch_is_rejected(self):
        profile = MaterialCurveProfile(
            amplitude=5,
            loading=(0, 1, 2, 3),
            returning=(0, 3, 1, 5),
            branch_gap=0,
            signed_area=0,
            peak_loading=3,
            peak_returning=5,
        )
        with self.assertRaises(ValueError):
            rebound_staircase(profile, 3, controlling_gap=1)


if __name__ == "__main__":
    unittest.main()
