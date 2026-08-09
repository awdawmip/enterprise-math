import unittest

from enterprise_math.material_impulse_passivity import (
    ACTIVE_AMPLIFICATION,
    DECELERATED_TOWARD,
    DISSIPATIVE_REBOUND,
    ELASTIC_REFLECTION,
    STALL,
    fixed_impulse_passive_on_tail,
    impulse_passivity_report,
    minimum_momentum_for_fixed_impulse_passivity,
)


class MaterialImpulsePassivityTests(unittest.TestCase):
    def test_exact_squared_momentum_defect_identity(self):
        for momentum in range(1, 30):
            for impulse in range(0, 2 * momentum + 8):
                report = impulse_passivity_report(momentum, impulse)
                self.assertEqual(
                    report.squared_defect,
                    impulse * (impulse - 2 * momentum),
                )
                self.assertEqual(
                    report.passive_nonamplifying,
                    impulse <= 2 * momentum,
                )

    def test_five_integer_impulse_regimes(self):
        p = 5
        self.assertEqual(impulse_passivity_report(p, 2).regime, DECELERATED_TOWARD)
        self.assertEqual(impulse_passivity_report(p, 5).regime, STALL)
        self.assertEqual(impulse_passivity_report(p, 7).regime, DISSIPATIVE_REBOUND)
        self.assertEqual(impulse_passivity_report(p, 10).regime, ELASTIC_REFLECTION)
        self.assertEqual(impulse_passivity_report(p, 11).regime, ACTIVE_AMPLIFICATION)

    def test_fixed_impulse_tail_passivity_has_exact_minimum_momentum(self):
        for impulse in range(0, 30):
            minimum = minimum_momentum_for_fixed_impulse_passivity(impulse)
            self.assertTrue(fixed_impulse_passive_on_tail(impulse, minimum))
            if minimum > 1:
                self.assertFalse(
                    fixed_impulse_passive_on_tail(impulse, minimum - 1)
                )

    def test_only_small_fixed_impulses_are_passive_for_all_positive_momentum_quanta(self):
        self.assertTrue(fixed_impulse_passive_on_tail(0, 1))
        self.assertTrue(fixed_impulse_passive_on_tail(1, 1))
        self.assertTrue(fixed_impulse_passive_on_tail(2, 1))
        self.assertFalse(fixed_impulse_passive_on_tail(3, 1))

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            impulse_passivity_report(0, 1)
        with self.assertRaises(ValueError):
            impulse_passivity_report(1, -1)
        with self.assertRaises(ValueError):
            minimum_momentum_for_fixed_impulse_passivity(-1)
        with self.assertRaises(ValueError):
            fixed_impulse_passive_on_tail(1, 0)


if __name__ == "__main__":
    unittest.main()
