import unittest

from enterprise_math.material_oscillator import PythagoreanRotation
from enterprise_math.material_peak_wave import (
    FALL,
    PLATEAU,
    RISE,
    peak_step,
    projected_peak_trace,
)


class MaterialPeakWaveTests(unittest.TestCase):
    def test_rise_margin_exactly_matches_next_y_on_small_states(self):
        rotations = (
            PythagoreanRotation(3, 4, 5),
            PythagoreanRotation(5, 12, 13),
            PythagoreanRotation(8, 15, 17),
        )
        for rotation in rotations:
            for x in range(-10, 11):
                for y in range(0, 11):
                    report = peak_step(x, y, rotation)
                    before_y = report.before[1]
                    after_y = report.after[1]
                    if report.status == RISE:
                        self.assertGreater(after_y, before_y)
                    elif report.status == PLATEAU:
                        self.assertEqual(after_y, before_y)
                    elif report.status == FALL:
                        self.assertLess(after_y, before_y)
                    else:
                        self.fail("unknown peak status")

    def test_negative_x_nonnegative_y_forces_next_y_fall(self):
        rotation = PythagoreanRotation(399, 40, 401)
        for x in range(-10, 0):
            for y in range(0, 11):
                self.assertEqual(peak_step(x, y, rotation).status, FALL)

    def test_peak_trace_always_finds_finite_nonrise_on_small_amplitudes(self):
        rotations = (
            PythagoreanRotation(3, 4, 5),
            PythagoreanRotation(5, 12, 13),
            PythagoreanRotation(399, 40, 401),
        )
        for rotation in rotations:
            for amplitude in range(1, 80):
                trace = projected_peak_trace(amplitude, rotation)
                self.assertIn(trace.termination_status, (PLATEAU, FALL))
                self.assertLessEqual(trace.first_nonrise_step, amplitude + 2)
                peak_y = trace.peak_state[1]
                self.assertEqual(peak_y, max(state[1] for state in trace.states))

    def test_zero_amplitude_is_trivial_peak(self):
        trace = projected_peak_trace(0, PythagoreanRotation(3, 4, 5))
        self.assertEqual(trace.peak_state, (0, 0))
        self.assertEqual(trace.first_nonrise_step, 0)
        self.assertEqual(trace.termination_status, PLATEAU)

    def test_reference_rotation_needs_no_external_angle_target(self):
        trace = projected_peak_trace(1000, PythagoreanRotation(399, 40, 401))
        self.assertGreater(trace.peak_state[1], 900)
        self.assertIn(trace.termination_status, (PLATEAU, FALL))
        # Structural guarantee only; no pi/2 or external sine phase is used.
        self.assertLessEqual(trace.first_nonrise_step, 1002)


if __name__ == "__main__":
    unittest.main()
