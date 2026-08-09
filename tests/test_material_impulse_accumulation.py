import unittest

from enterprise_math.material_impulse_accumulation import (
    INWARD,
    OUTWARD,
    STALL,
    impulse_accumulation_thresholds,
    lifted_momentum_numerator,
    minimum_ticks_for_cumulative_impulse,
    oriented_momentum_phase,
    retained_impulse_history_certificate,
)


class MaterialImpulseAccumulationTests(unittest.TestCase):
    def test_lifted_history_is_exact_for_arbitrary_response_words(self):
        for amplitude in range(1, 8):
            words = (
                (),
                (0,),
                (amplitude,),
                tuple(range(amplitude + 1)),
                tuple(reversed(range(amplitude + 1))),
            )
            for word in words:
                for maximum in range(0, 6):
                    for sign in (-1, 1):
                        for momentum in range(-3, 4):
                            for detail in range(-(amplitude - 1), amplitude):
                                report = retained_impulse_history_certificate(
                                    momentum,
                                    detail,
                                    word,
                                    amplitude,
                                    maximum,
                                    sign,
                                )
                                self.assertEqual(
                                    report.final_lifted_numerator,
                                    report.initial_lifted_numerator
                                    + sign * maximum * sum(word),
                                )

    def test_oriented_phase_has_exact_two_sided_stall_band(self):
        for amplitude in range(1, 12):
            for value in range(-3 * amplitude, 3 * amplitude + 1):
                phase = oriented_momentum_phase(value, amplitude)
                if value >= amplitude:
                    self.assertEqual(phase, INWARD)
                elif value <= -amplitude:
                    self.assertEqual(phase, OUTWARD)
                else:
                    self.assertEqual(phase, STALL)

    def test_stop_and_true_reversal_thresholds_are_sharp(self):
        for amplitude in range(1, 20):
            for initial in range(1, 5 * amplitude + 1):
                t = impulse_accumulation_thresholds(initial, amplitude)
                self.assertEqual(
                    oriented_momentum_phase(initial - t.minimum_impulse_numerator_to_stop, amplitude),
                    STALL if t.minimum_impulse_numerator_to_stop > 0 or initial < amplitude else INWARD,
                )
                if t.minimum_impulse_numerator_to_stop > 0:
                    self.assertEqual(
                        oriented_momentum_phase(
                            initial - (t.minimum_impulse_numerator_to_stop - 1),
                            amplitude,
                        ),
                        INWARD,
                    )
                self.assertEqual(
                    oriented_momentum_phase(
                        initial - t.minimum_impulse_numerator_to_reverse,
                        amplitude,
                    ),
                    OUTWARD,
                )
                self.assertNotEqual(
                    oriented_momentum_phase(
                        initial - (t.minimum_impulse_numerator_to_reverse - 1),
                        amplitude,
                    ),
                    OUTWARD,
                )

    def test_reference_momentum_requires_extra_amplitude_cell_after_stopping_to_reverse(self):
        # Whole inward p=5 with zero detail on A=4 gives lifted inward Pi=20.
        thresholds = impulse_accumulation_thresholds(20, 4)
        self.assertEqual(thresholds.minimum_impulse_numerator_to_stop, 17)
        self.assertEqual(thresholds.stall_impulse_numerator_range, (17, 23))
        self.assertEqual(thresholds.minimum_impulse_numerator_to_reverse, 24)
        self.assertEqual(oriented_momentum_phase(20 - 16, 4), INWARD)
        self.assertEqual(oriented_momentum_phase(20 - 17, 4), STALL)
        self.assertEqual(oriented_momentum_phase(20 - 23, 4), STALL)
        self.assertEqual(oriented_momentum_phase(20 - 24, 4), OUTWARD)

    def test_constant_subquantum_response_has_distinct_stop_and_reverse_tick_thresholds(self):
        # A=4, response=1, J=1 -> one impulse numerator per tick.
        # p=1, eta=0 => Pi0=4: stop after 1 tick, true outward whole momentum after 8 ticks.
        thresholds = impulse_accumulation_thresholds(4, 4)
        self.assertEqual(
            minimum_ticks_for_cumulative_impulse(
                thresholds.minimum_impulse_numerator_to_stop, 1
            ),
            1,
        )
        self.assertEqual(
            minimum_ticks_for_cumulative_impulse(
                thresholds.minimum_impulse_numerator_to_reverse, 1
            ),
            8,
        )
        after_one = retained_impulse_history_certificate(1, 0, (1,), 4, 1, -1)
        self.assertEqual(after_one.final_momentum_quanta, 0)
        after_eight = retained_impulse_history_certificate(1, 0, (1,) * 8, 4, 1, -1)
        self.assertEqual(after_eight.final_momentum_quanta, -1)

    def test_zero_per_tick_impulse_cannot_reach_positive_threshold(self):
        self.assertIsNone(minimum_ticks_for_cumulative_impulse(1, 0))
        self.assertEqual(minimum_ticks_for_cumulative_impulse(0, 0), 0)

    def test_lifted_coordinate_rejects_detail_outside_cell(self):
        with self.assertRaises(ValueError):
            lifted_momentum_numerator(1, 4, 4)
        with self.assertRaises(ValueError):
            lifted_momentum_numerator(1, -4, 4)


if __name__ == "__main__":
    unittest.main()
