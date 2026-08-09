import unittest

from enterprise_math.material_oscillator_phase_budget import (
    balanced_linear_phase_trace,
    first_transverse_quantum,
    pythagorean_phase_budget,
    sharp_last_live_parameter,
    strict_rise_count,
)


class MaterialOscillatorPhaseBudgetTests(unittest.TestCase):
    def test_first_transverse_mode_threshold_is_exact_and_sharp(self):
        for amplitude in range(2, 60):
            last = sharp_last_live_parameter(amplitude)
            self.assertEqual(last, 2 * amplitude - 1)
            self.assertEqual(first_transverse_quantum(amplitude, last), 1)
            self.assertEqual(first_transverse_quantum(amplitude, 2 * amplitude), 0)
            for m in range(2, 2 * amplitude):
                self.assertGreater(first_transverse_quantum(amplitude, m), 0)
            for m in range(2 * amplitude, 2 * amplitude + 5):
                self.assertEqual(first_transverse_quantum(amplitude, m), 0)

    def test_every_projected_peak_has_at_most_amplitude_strict_rises(self):
        for amplitude in range(0, 35):
            for parameter in range(2, max(3, 2 * amplitude + 5)):
                report = pythagorean_phase_budget(amplitude, parameter)
                self.assertLessEqual(report.strict_rises, amplitude)
                self.assertEqual(report.live_transverse_mode, report.first_transverse_quantum > 0)

    def test_m_equal_amplitude_constructs_exact_linear_phase_count(self):
        for amplitude in range(2, 80):
            trace = balanced_linear_phase_trace(amplitude)
            rises = strict_rise_count(trace)
            expected = (amplitude + 1) // 2
            self.assertEqual(rises, expected)
            self.assertEqual(
                trace.states[: expected + 1],
                tuple((amplitude - n, n) for n in range(expected + 1)),
            )
            self.assertNotEqual(trace.steps[expected].status, "RISE")

    def test_linear_constructive_lower_bound_and_integer_upper_bound_share_one_scale(self):
        for amplitude in range(2, 100):
            trace = balanced_linear_phase_trace(amplitude)
            lower = (amplitude + 1) // 2
            upper = amplitude
            self.assertEqual(strict_rise_count(trace), lower)
            self.assertLessEqual(lower, upper)
            self.assertLessEqual(2 * lower - amplitude, 1)

    def test_small_reference_traces_are_exact_staircases(self):
        self.assertEqual(
            balanced_linear_phase_trace(5).states[:4],
            ((5, 0), (4, 1), (3, 2), (2, 3)),
        )
        self.assertEqual(
            balanced_linear_phase_trace(10).states[:6],
            ((10, 0), (9, 1), (8, 2), (7, 3), (6, 4), (5, 5)),
        )

    def test_invalid_family_parameters_are_rejected(self):
        with self.assertRaises(ValueError):
            first_transverse_quantum(5, 1)
        with self.assertRaises(ValueError):
            sharp_last_live_parameter(1)
        with self.assertRaises(ValueError):
            balanced_linear_phase_trace(1)


if __name__ == "__main__":
    unittest.main()
