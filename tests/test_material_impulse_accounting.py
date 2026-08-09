import unittest

from enterprise_math.material_impulse_accounting import (
    constant_response_momentum_thresholds,
    retained_impulse_telescope,
)
from enterprise_math.material_impulse_world_1d import accumulate_material_impulses


class MaterialImpulseAccountingTests(unittest.TestCase):
    def test_retained_detail_equals_one_shot_projection_exhaustively_on_small_domain(self):
        for amplitude in range(1, 8):
            for scale in range(-4, 5):
                for left in range(amplitude + 1):
                    for middle in range(amplitude + 1):
                        for right in range(amplitude + 1):
                            report = retained_impulse_telescope(
                                (left, middle, right), amplitude, scale
                            )
                            self.assertEqual(
                                amplitude * report.sequential_impulse_quanta
                                + report.sequential_final_detail,
                                report.scaled_response_sum,
                            )
                            self.assertEqual(
                                report.sequential_impulse_quanta,
                                report.one_shot_impulse_quanta,
                            )
                            self.assertEqual(
                                report.sequential_final_detail,
                                report.one_shot_detail,
                            )

    def test_empty_response_sequence_has_zero_exact_ledger(self):
        report = retained_impulse_telescope((), amplitude=7, signed_impulse_scale=-3)
        self.assertEqual(report.response_sum, 0)
        self.assertEqual(report.sequential_impulse_quanta, 0)
        self.assertEqual(report.sequential_final_detail, 0)
        self.assertEqual(report.one_shot_impulse_quanta, 0)
        self.assertEqual(report.one_shot_detail, 0)

    def test_constant_response_thresholds_match_direct_retained_simulation(self):
        for amplitude in range(1, 12):
            for response in range(amplitude + 1):
                for scale in range(1, 6):
                    for inward in range(1, 6):
                        thresholds = constant_response_momentum_thresholds(
                            amplitude, response, scale, inward
                        )
                        if response == 0:
                            self.assertIsNone(
                                thresholds.retained_first_nonnegative_event
                            )
                            self.assertIsNone(thresholds.retained_first_outward_event)
                            continue

                        nonnegative = thresholds.retained_first_nonnegative_event
                        outward = thresholds.retained_first_outward_event
                        self.assertIsNotNone(nonnegative)
                        self.assertIsNotNone(outward)
                        for event_count, target in (
                            (nonnegative, inward),
                            (outward, inward + 1),
                        ):
                            report = accumulate_material_impulses(
                                (response,) * event_count,
                                amplitude,
                                scale,
                                retain_detail=True,
                            )
                            self.assertGreaterEqual(report.total_impulse_quanta, target)
                            if event_count > 0:
                                before = accumulate_material_impulses(
                                    (response,) * (event_count - 1),
                                    amplitude,
                                    scale,
                                    retain_detail=True,
                                )
                                self.assertLess(before.total_impulse_quanta, target)

    def test_subquantum_response_has_finite_retained_outward_threshold_but_no_dropped_one(self):
        report = constant_response_momentum_thresholds(
            amplitude=10,
            response_sample=3,
            outward_impulse_scale_magnitude=2,
            inward_normal_momentum_magnitude=1,
        )
        self.assertEqual(report.retained_first_nonnegative_event, 2)
        self.assertEqual(report.retained_first_outward_event, 4)
        self.assertEqual(report.dropped_impulse_per_event, 0)
        self.assertIsNone(report.dropped_first_nonnegative_event)
        self.assertIsNone(report.dropped_first_outward_event)

    def test_superquantum_dropped_policy_has_its_own_exact_momentum_threshold(self):
        report = constant_response_momentum_thresholds(
            amplitude=5,
            response_sample=4,
            outward_impulse_scale_magnitude=3,
            inward_normal_momentum_magnitude=5,
        )
        self.assertEqual(report.dropped_impulse_per_event, 2)
        self.assertEqual(report.dropped_first_nonnegative_event, 3)
        self.assertEqual(report.dropped_first_outward_event, 3)
        self.assertLessEqual(
            report.retained_first_nonnegative_event,
            report.dropped_first_nonnegative_event,
        )
        self.assertLessEqual(
            report.retained_first_outward_event,
            report.dropped_first_outward_event,
        )

    def test_invalid_telescope_and_threshold_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            retained_impulse_telescope((1,), 0, 1)
        with self.assertRaises(ValueError):
            retained_impulse_telescope((6,), 5, 1)
        with self.assertRaises(ValueError):
            retained_impulse_telescope((1,), 5, True)
        with self.assertRaises(ValueError):
            constant_response_momentum_thresholds(0, 0, 1, 1)
        with self.assertRaises(ValueError):
            constant_response_momentum_thresholds(5, 6, 1, 1)
        with self.assertRaises(ValueError):
            constant_response_momentum_thresholds(5, 1, 0, 1)
        with self.assertRaises(ValueError):
            constant_response_momentum_thresholds(5, 1, 1, 0)


if __name__ == "__main__":
    unittest.main()
