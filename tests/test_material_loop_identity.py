import unittest

from enterprise_math.material_loop_identity import (
    standard_loop_identity,
    standard_single_peak_schedule,
)
from enterprise_math.material_response import MaterialCurveProfile, material_curve_profile


class MaterialLoopIdentityTests(unittest.TestCase):
    def test_reference_material_loop_area_equals_twice_repeated_depth_gap(self):
        profile = material_curve_profile(
            (0, 200, 400, 600, 800, 1000),
            amplitude=1000,
            loading_power=2,
            return_power=1,
            return_retention=500,
        )
        report = standard_loop_identity(profile, peak_depth=5)
        self.assertEqual(report.schedule, (0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0))
        self.assertEqual(
            report.signed_twice_area,
            2 * report.repeated_depth_signed_gap,
        )

    def test_symmetric_curve_has_zero_gap_and_zero_area(self):
        profile = material_curve_profile(
            (0, 1, 2, 3, 4, 5),
            amplitude=5,
            loading_power=1,
            return_power=1,
            return_retention=5,
        )
        report = standard_loop_identity(profile, peak_depth=5)
        self.assertEqual(report.repeated_depth_signed_gap, 0)
        self.assertEqual(report.signed_twice_area, 0)

    def test_identity_holds_on_small_arbitrary_branch_tables_with_shared_zero(self):
        # The theorem is combinatorial and does not require monotone or physical branches.
        profiles = (
            MaterialCurveProfile(
                amplitude=10,
                loading=(0, 2, 7, 4, 9),
                returning=(0, 8, 1, 6, 3),
                branch_gap=0,
                signed_area=0,
                peak_loading=9,
                peak_returning=8,
            ),
            MaterialCurveProfile(
                amplitude=9,
                loading=(0, 9, 0, 9),
                returning=(0, 0, 9, 0),
                branch_gap=0,
                signed_area=0,
                peak_loading=9,
                peak_returning=9,
            ),
        )
        for profile in profiles:
            for peak in range(1, len(profile.loading)):
                report = standard_loop_identity(profile, peak)
                self.assertEqual(
                    report.signed_twice_area,
                    report.reconstructed_twice_area,
                )

    def test_peak_zero_schedule_is_trivial(self):
        profile = material_curve_profile(
            (0, 1),
            amplitude=1,
            loading_power=1,
            return_power=1,
        )
        self.assertEqual(standard_single_peak_schedule(0), (0,))
        report = standard_loop_identity(profile, 0)
        self.assertEqual(report.signed_twice_area, 0)

    def test_mismatched_zero_branches_are_rejected(self):
        profile = MaterialCurveProfile(
            amplitude=5,
            loading=(0, 1, 2),
            returning=(1, 1, 2),
            branch_gap=0,
            signed_area=0,
            peak_loading=2,
            peak_returning=2,
        )
        with self.assertRaises(ValueError):
            standard_loop_identity(profile, 2)


if __name__ == "__main__":
    unittest.main()
