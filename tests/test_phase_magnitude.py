import unittest

from enterprise_math.black_hole import clock_state, horizon_zero_interval
from enterprise_math.phase_magnitude import (
    charged_phase_magnitude,
    is_zero_phase_boundary,
    schwarzschild_phase_magnitude,
)


class PhaseMagnitudeTests(unittest.TestCase):
    def test_schwarzschild_zero_magnitude_basin_splits_into_three_phases(self):
        horizon = 10
        precision = 4
        lower, upper = horizon_zero_interval(precision, horizon)
        observations = {
            radius: schwarzschild_phase_magnitude(precision, radius, horizon)
            for radius in range(lower, upper + 1)
        }
        self.assertTrue(any(value == (-1, 0) for value in observations.values()))
        self.assertEqual(observations[horizon], (0, 0))
        self.assertTrue(any(value == (1, 0) for value in observations.values()))

    def test_exact_schwarzschild_horizon_is_unique_zero_phase_at_every_precision(self):
        for horizon in range(1, 50):
            for precision in range(1, 30):
                for radius in range(1, 2 * horizon + 20):
                    observation = schwarzschild_phase_magnitude(
                        precision, radius, horizon
                    )
                    self.assertEqual(
                        is_zero_phase_boundary(observation),
                        radius == horizon,
                    )

    def test_clock_zero_does_not_imply_horizon_at_coarse_precision(self):
        sigma = 2
        horizon = 10
        self.assertEqual(clock_state(sigma, 9, horizon), 0)
        self.assertEqual(clock_state(sigma, 10, horizon), 0)
        self.assertEqual(clock_state(sigma, 11, horizon), 0)
        self.assertEqual(schwarzschild_phase_magnitude(sigma * sigma, 9, horizon)[0], -1)
        self.assertEqual(schwarzschild_phase_magnitude(sigma * sigma, 10, horizon)[0], 0)
        self.assertEqual(schwarzschild_phase_magnitude(sigma * sigma, 11, horizon)[0], 1)

    def test_same_nonzero_clock_state_can_occur_on_opposite_sides(self):
        sigma = 2
        horizon = 3
        self.assertEqual(clock_state(sigma, 2, horizon), 1)
        self.assertEqual(clock_state(sigma, 4, horizon), 1)
        self.assertEqual(schwarzschild_phase_magnitude(4, 2, horizon)[0], -1)
        self.assertEqual(schwarzschild_phase_magnitude(4, 4, horizon)[0], 1)

    def test_charged_zero_magnitude_does_not_determine_phase(self):
        a, b, precision = 5, 5, 10
        observed = {
            radius: charged_phase_magnitude(precision, radius, a, b)
            for radius in range(1, 8)
        }
        zero_magnitude_phases = {
            phase
            for phase, magnitude in observed.values()
            if magnitude == 0
        }
        self.assertTrue(zero_magnitude_phases.issubset({-1, 0, 1}))
        self.assertNotIn(0, zero_magnitude_phases)

    def test_charged_exact_zero_vertex_requires_zero_phase(self):
        a, b = 10, 16  # roots 2 and 8
        for precision in range(1, 30):
            self.assertTrue(is_zero_phase_boundary(charged_phase_magnitude(precision, 2, a, b)))
            self.assertTrue(is_zero_phase_boundary(charged_phase_magnitude(precision, 8, a, b)))
            for radius in range(1, 15):
                if radius not in (2, 8):
                    self.assertFalse(
                        is_zero_phase_boundary(
                            charged_phase_magnitude(precision, radius, a, b)
                        )
                    )


if __name__ == "__main__":
    unittest.main()
