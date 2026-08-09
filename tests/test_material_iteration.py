import unittest

from enterprise_math.material_iteration import (
    HARDENING,
    SOFTENING,
    hardening_fixed,
    iterate_hardening,
    iterate_softening,
    softening_fixed,
    softening_fixed_by_basin,
)


class MaterialIterationTests(unittest.TestCase):
    def test_hardening_has_only_endpoint_fixed_points_for_power_gt_one(self):
        for amplitude in range(1, 30):
            for power in range(2, 6):
                fixed = [
                    sample
                    for sample in range(amplitude + 1)
                    if hardening_fixed(sample, amplitude, power)
                ]
                self.assertEqual(fixed, [0, amplitude])

    def test_every_interior_hardening_state_reaches_zero(self):
        for amplitude in range(2, 30):
            for power in range(2, 6):
                for sample in range(1, amplitude):
                    trace = iterate_hardening(sample, amplitude, power)
                    self.assertEqual(trace.operator, HARDENING)
                    self.assertEqual(trace.stabilized_at, 0)
                    self.assertLessEqual(trace.strict_steps, sample)
                    self.assertEqual(trace.states, tuple(sorted(trace.states, reverse=True)))

    def test_amplitude_endpoint_remains_fixed_under_hardening(self):
        trace = iterate_hardening(100, 100, 3)
        self.assertEqual(trace.states, (100,))
        self.assertEqual(trace.stabilized_at, 100)
        self.assertEqual(trace.strict_steps, 0)

    def test_softening_fixed_criterion_matches_integer_root_definition(self):
        for amplitude in range(1, 35):
            for power in range(2, 6):
                for sample in range(amplitude + 1):
                    self.assertEqual(
                        softening_fixed(sample, amplitude, power),
                        softening_fixed_by_basin(sample, amplitude, power),
                    )

    def test_softening_orbits_are_strictly_increasing_until_fixed_plateau(self):
        for amplitude in range(1, 30):
            for power in range(2, 5):
                for sample in range(amplitude + 1):
                    trace = iterate_softening(sample, amplitude, power)
                    self.assertEqual(trace.operator, SOFTENING)
                    self.assertTrue(softening_fixed(trace.stabilized_at, amplitude, power))
                    self.assertEqual(trace.states, tuple(sorted(trace.states)))
                    self.assertLessEqual(trace.strict_steps, amplitude - sample)

    def test_softening_can_stabilize_below_full_amplitude(self):
        trace = iterate_softening(500, 1000, 2)
        self.assertLess(trace.stabilized_at, 1000)
        self.assertTrue(softening_fixed(trace.stabilized_at, 1000, 2))
        self.assertGreater(trace.stabilized_at, 500)

    def test_invalid_power_is_rejected(self):
        with self.assertRaises(ValueError):
            iterate_hardening(1, 10, 1)
        with self.assertRaises(ValueError):
            iterate_softening(1, 10, 1)


if __name__ == "__main__":
    unittest.main()
