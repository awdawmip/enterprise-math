import unittest

from enterprise_math.material_impulse_sampling import (
    compare_impulse_depth_schedules,
    endpoint_layer_depth,
)


class MaterialImpulseSamplingTests(unittest.TestCase):
    def test_proposal_depth_is_exact_max_of_saved_endpoint_depths(self):
        for d in range(1, 10):
            for start_gap in range(1, 12):
                for end_gap in range(1, 12):
                    report = compare_impulse_depth_schedules(start_gap, end_gap, d)
                    self.assertEqual(
                        report.proposal_depth,
                        max(report.start_depth, report.free_end_depth),
                    )
                    self.assertGreaterEqual(report.proposal_depth, report.start_depth)

    def test_outside_to_outside_high_speed_skip_remains_resolved_in_both_schedules(self):
        report = compare_impulse_depth_schedules(
            start_gap=5,
            free_end_gap=7,
            collapse_factor=4,
        )
        self.assertEqual(report.start_depth, 0)
        self.assertEqual(report.free_end_depth, 0)
        self.assertEqual(report.proposal_depth, 0)
        self.assertTrue(report.both_endpoints_resolved)
        self.assertFalse(report.proposal_is_deeper)

    def test_entering_visible_layer_is_one_tick_earlier_under_proposal_sampling(self):
        report = compare_impulse_depth_schedules(
            start_gap=5,
            free_end_gap=2,
            collapse_factor=4,
        )
        self.assertEqual(report.start_depth, 0)
        self.assertEqual(report.free_end_depth, 2)
        self.assertEqual(report.proposal_depth, 2)
        self.assertTrue(report.proposal_is_deeper)

    def test_continued_approach_inside_layer_reads_deeper_proposal_state(self):
        report = compare_impulse_depth_schedules(
            start_gap=3,
            free_end_gap=1,
            collapse_factor=5,
        )
        self.assertEqual(report.start_depth, 2)
        self.assertEqual(report.free_end_depth, 4)
        self.assertEqual(report.proposal_depth, 4)
        self.assertTrue(report.proposal_is_deeper)

    def test_retreat_never_makes_proposal_schedule_deeper_than_start(self):
        for d in range(2, 8):
            for start_gap in range(1, d):
                for end_gap in range(start_gap, d + 4):
                    report = compare_impulse_depth_schedules(start_gap, end_gap, d)
                    self.assertEqual(report.proposal_depth, report.start_depth)
                    self.assertFalse(report.proposal_is_deeper)

    def test_endpoint_depth_has_exact_visible_layer_threshold(self):
        for d in range(1, 10):
            self.assertEqual(endpoint_layer_depth(d, d), 0)
            if d > 1:
                self.assertEqual(endpoint_layer_depth(d - 1, d), 1)
            self.assertEqual(endpoint_layer_depth(d + 5, d), 0)

    def test_primitive_contact_is_outside_positive_gap_schedule_comparator(self):
        with self.assertRaises(ValueError):
            endpoint_layer_depth(0, 4)
        with self.assertRaises(ValueError):
            compare_impulse_depth_schedules(3, 0, 4)
        with self.assertRaises(ValueError):
            compare_impulse_depth_schedules(3, 2, 0)


if __name__ == "__main__":
    unittest.main()
