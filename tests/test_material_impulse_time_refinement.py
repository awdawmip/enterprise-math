import unittest

from enterprise_math.material_impulse_time_refinement import (
    balanced_impulse_capacity_schedule,
    constant_response_time_refinement_report,
    variable_response_pairing_report,
)


class MaterialImpulseTimeRefinementTests(unittest.TestCase):
    def test_balanced_capacity_schedule_preserves_total_for_all_small_inputs(self):
        for full in range(0, 30):
            for steps in range(1, 12):
                schedule = balanced_impulse_capacity_schedule(full, steps)
                self.assertEqual(len(schedule), steps)
                self.assertEqual(sum(schedule), full)
                self.assertLessEqual(max(schedule) - min(schedule), 1)

    def test_retained_detail_makes_constant_response_refinement_exact(self):
        for amplitude in range(1, 10):
            for response in range(amplitude + 1):
                for full in range(0, 16):
                    for steps in range(1, 8):
                        schedule = balanced_impulse_capacity_schedule(full, steps)
                        report = constant_response_time_refinement_report(
                            full, schedule, response, amplitude
                        )
                        self.assertTrue(report.retained_endpoint_exact)
                        self.assertEqual(
                            report.refined_whole_impulse_retained,
                            report.coarse_whole_impulse,
                        )
                        self.assertEqual(
                            report.refined_detail_retained,
                            report.coarse_detail,
                        )

    def test_detail_dropping_can_destroy_subquantum_force_under_time_refinement(self):
        report = constant_response_time_refinement_report(
            full_capacity=4,
            subcapacities=(1, 1, 1, 1),
            response_sample=1,
            amplitude=4,
        )
        self.assertEqual(report.coarse_whole_impulse, 1)
        self.assertEqual(report.refined_whole_impulse_retained, 1)
        self.assertEqual(report.refined_whole_impulse_dropped, 0)
        self.assertTrue(report.retained_endpoint_exact)
        self.assertFalse(report.dropped_endpoint_exact)

    def test_detail_dropping_is_exact_when_every_substep_is_individually_divisible(self):
        report = constant_response_time_refinement_report(
            full_capacity=8,
            subcapacities=(4, 4),
            response_sample=2,
            amplitude=4,
        )
        self.assertEqual(report.coarse_whole_impulse, 4)
        self.assertEqual(report.refined_whole_impulse_dropped, 4)
        self.assertTrue(report.dropped_endpoint_exact)

    def test_variable_response_pairing_can_make_substep_order_dynamically_visible(self):
        report = variable_response_pairing_report(
            capacities=(2, 1),
            responses=(1, 2),
            amplitude=2,
        )
        self.assertEqual(report.paired_raw_impulse_numerator, 4)
        self.assertEqual(report.reversed_response_raw_impulse_numerator, 5)
        self.assertEqual(report.order_defect_numerator, -1)

    def test_equal_capacities_or_equal_responses_remove_pairing_order_defect(self):
        equal_j = variable_response_pairing_report((2, 2, 2), (0, 1, 2), 2)
        equal_r = variable_response_pairing_report((1, 2, 3), (1, 1, 1), 2)
        self.assertEqual(equal_j.order_defect_numerator, 0)
        self.assertEqual(equal_r.order_defect_numerator, 0)

    def test_invalid_subcapacity_sum_is_rejected(self):
        with self.assertRaises(ValueError):
            constant_response_time_refinement_report(4, (1, 1), 1, 4)


if __name__ == "__main__":
    unittest.main()
