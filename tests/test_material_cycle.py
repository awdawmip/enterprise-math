import unittest

from enterprise_math.material_cycle import material_cycle_diagnostics
from enterprise_math.material_hysteresis import trace_deformation_schedule
from enterprise_math.material_response import material_curve_profile


class MaterialCycleTests(unittest.TestCase):
    def setUp(self):
        self.profile = material_curve_profile(
            (0, 200, 400, 600, 800, 1000),
            amplitude=1000,
            loading_power=2,
            return_power=1,
            return_retention=500,
        )

    def test_realized_cycle_pairs_only_indices_visited_on_both_branches(self):
        schedule = (0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0)
        states = trace_deformation_schedule(self.profile, schedule)
        report = material_cycle_diagnostics(states)
        self.assertEqual(report.peak_index, 5)
        self.assertEqual(
            tuple(gap.deformation_index for gap in report.revisited_gaps),
            (0, 1, 2, 3, 4),
        )
        self.assertNotIn(5, [gap.deformation_index for gap in report.revisited_gaps])

    def test_reference_realized_gap_sums_are_distinct_from_full_table_gap(self):
        schedule = (0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0)
        report = material_cycle_diagnostics(
            trace_deformation_schedule(self.profile, schedule)
        )
        self.assertEqual(
            tuple(gap.signed_gap for gap in report.revisited_gaps),
            (0, -60, -40, 60, 240),
        )
        self.assertEqual(report.paired_signed_gap_sum, 200)
        self.assertEqual(report.paired_absolute_gap_sum, 400)
        self.assertEqual(report.paired_loading_excess_sum, 300)
        self.assertEqual(report.paired_returning_excess_sum, 100)
        self.assertNotEqual(report.paired_loading_excess_sum, self.profile.branch_gap)
        self.assertEqual(self.profile.branch_gap, 800)

    def test_closed_zero_response_cycle_has_zero_residual_response(self):
        schedule = (0, 1, 2, 3, 4, 5, 4, 3, 2, 1, 0)
        report = material_cycle_diagnostics(
            trace_deformation_schedule(self.profile, schedule)
        )
        self.assertTrue(report.closed_deformation)
        self.assertEqual(report.start_index, 0)
        self.assertEqual(report.end_index, 0)
        self.assertEqual(report.residual_response, 0)
        self.assertEqual(report.branch_switch_count, 1)

    def test_monotone_loading_has_no_revisited_branch_gaps(self):
        report = material_cycle_diagnostics(
            trace_deformation_schedule(self.profile, (0, 1, 2, 3, 4, 5))
        )
        self.assertEqual(report.revisited_gaps, ())
        self.assertEqual(report.paired_absolute_gap_sum, 0)
        self.assertEqual(report.branch_switch_count, 0)

    def test_empty_history_is_rejected(self):
        with self.assertRaises(ValueError):
            material_cycle_diagnostics(())


if __name__ == "__main__":
    unittest.main()
