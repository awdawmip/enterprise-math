import unittest

from enterprise_math.material_collapse_world_1d import REBOUND, TRANSMIT, ZERO_RETURN
from enterprise_math.material_response import material_curve_profile
from enterprise_math.material_scale_response import (
    refinement_rebound_profile,
    returning_branch_is_monotone,
)
from enterprise_math.scale_tunneling_1d import Wall1D


class MaterialScaleResponseTests(unittest.TestCase):
    def setUp(self):
        self.wall = Wall1D(0, 0)

    def test_monotone_return_branch_gives_weakening_rebound_then_transmission(self):
        profile = material_curve_profile(
            (0, 200, 400, 600, 800, 1000),
            amplitude=1000,
            loading_power=1,
            return_power=1,
            return_retention=1000,
        )
        report = refinement_rebound_profile(
            self.wall,
            -2,
            2,
            0,
            6,
            profile,
        )
        self.assertTrue(report.returning_branch_monotone)
        self.assertTrue(report.rebound_weakens_under_refinement)
        self.assertEqual(report.factors, (6, 5, 4, 3, 2, 1))
        self.assertEqual(
            [outcome.kind for outcome in report.outcomes],
            [REBOUND, REBOUND, REBOUND, ZERO_RETURN, TRANSMIT, TRANSMIT],
        )
        self.assertEqual(report.rebound_budgets, (3, 2, 1, 0, None, None))
        self.assertEqual(report.outcomes[3].rebound.returned_budget, 0)
        self.assertNotEqual(report.outcomes[3].kind, REBOUND)

    def test_return_branch_from_standard_material_profile_is_monotone(self):
        profile = material_curve_profile(
            (0, 200, 400, 600, 800, 1000),
            amplitude=1000,
            loading_power=2,
            return_power=2,
            return_retention=700,
        )
        self.assertTrue(returning_branch_is_monotone(profile))
        report = refinement_rebound_profile(
            self.wall, -2, 2, 0, 6, profile
        )
        self.assertTrue(report.rebound_weakens_under_refinement)

    def test_plateaus_are_allowed_under_weak_monotonicity(self):
        profile = material_curve_profile(
            (0, 1, 2, 3, 4, 5),
            amplitude=5,
            loading_power=1,
            return_power=1,
            return_retention=2,
        )
        self.assertTrue(returning_branch_is_monotone(profile))
        report = refinement_rebound_profile(
            self.wall, -2, 2, 0, 6, profile
        )
        rebound_values = [value for value in report.rebound_budgets if value is not None]
        self.assertEqual(rebound_values, sorted(rebound_values, reverse=True))

    def test_nonmonotone_custom_curve_is_detected_but_not_silently_reordered(self):
        # Construct directly to stress the theorem precondition.
        from enterprise_math.material_response import MaterialCurveProfile

        profile = MaterialCurveProfile(
            amplitude=10,
            loading=(0, 1, 2, 3, 4, 5),
            returning=(0, 8, 2, 9, 3, 10),
            branch_gap=0,
            signed_area=0,
            peak_loading=5,
            peak_returning=10,
        )
        self.assertFalse(returning_branch_is_monotone(profile))
        report = refinement_rebound_profile(
            self.wall, -2, 2, 0, 6, profile
        )
        self.assertFalse(report.returning_branch_monotone)
        # The engine reports the actual sequence; it does not sort/fix it.
        self.assertEqual(len(report.outcomes), 6)

    def test_invalid_coarsest_factor_is_rejected(self):
        profile = material_curve_profile(
            (0, 1, 2),
            amplitude=2,
            loading_power=1,
            return_power=1,
        )
        with self.assertRaises(ValueError):
            refinement_rebound_profile(self.wall, -2, 2, 0, 0, profile)


if __name__ == "__main__":
    unittest.main()
