import unittest

from enterprise_math.engineering_collision import Body2D
from enterprise_math.material_contact_history import (
    contact_deformation_schedule,
    trace_contact_material_history,
)
from enterprise_math.material_hysteresis import LOADING, RETURNING
from enterprise_math.material_response import material_curve_profile


class MaterialContactHistoryTests(unittest.TestCase):
    def setUp(self):
        self.profile = material_curve_profile(
            (0, 200, 400, 600, 800, 1000),
            amplitude=1000,
            loading_power=2,
            return_power=1,
            return_retention=500,
        )

    @staticmethod
    def pair_state(right_x):
        return (
            Body2D(0, 0, 0, 2),
            Body2D(1, right_x, 0, 2),
        )

    def test_symmetric_approach_and_departure_generates_depth_schedule(self):
        positions = (10, 4, 3, 2, 1, 0, 1, 2, 3, 4, 10)
        history = tuple(self.pair_state(x) for x in positions)
        pair, schedule = contact_deformation_schedule(history)
        self.assertEqual(pair, (0, 1))
        self.assertEqual(schedule, (0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0))

    def test_geometry_history_selects_loading_then_returning_material_branches(self):
        positions = (10, 4, 3, 2, 1, 0, 1, 2, 3, 4, 10)
        report = trace_contact_material_history(
            tuple(self.pair_state(x) for x in positions),
            self.profile,
        )
        self.assertEqual(report.deformation_schedule, (0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0))
        self.assertEqual(report.peak_deformation, 5)
        self.assertEqual(report.contact_state_count, 9)
        self.assertEqual(report.separate_state_count, 2)

        loading_depth_three = report.material_states[3]
        returning_depth_three = report.material_states[7]
        self.assertEqual(loading_depth_three.deformation_index, 3)
        self.assertEqual(returning_depth_three.deformation_index, 3)
        self.assertEqual(loading_depth_three.branch, LOADING)
        self.assertEqual(returning_depth_three.branch, RETURNING)
        self.assertNotEqual(
            loading_depth_three.response_sample,
            returning_depth_three.response_sample,
        )

    def test_separate_only_history_remains_zero_deformation(self):
        history = (self.pair_state(10), self.pair_state(9), self.pair_state(8))
        report = trace_contact_material_history(history, self.profile)
        self.assertEqual(report.deformation_schedule, (0, 0, 0))
        self.assertEqual(report.peak_deformation, 0)
        self.assertEqual(report.contact_state_count, 0)
        self.assertTrue(all(state.response_sample == 0 for state in report.material_states))

    def test_curve_domain_overflow_is_rejected_instead_of_clamped(self):
        short_profile = material_curve_profile(
            (0, 100, 200),
            amplitude=200,
            loading_power=1,
            return_power=1,
        )
        history = (self.pair_state(10), self.pair_state(0))
        with self.assertRaises(ValueError):
            trace_contact_material_history(history, short_profile)

    def test_pair_identity_cannot_change_mid_history(self):
        history = (
            self.pair_state(10),
            (Body2D(0, 0, 0, 2), Body2D(2, 4, 0, 2)),
        )
        with self.assertRaises(ValueError):
            contact_deformation_schedule(history)


if __name__ == "__main__":
    unittest.main()
