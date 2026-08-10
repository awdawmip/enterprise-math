import unittest
from fractions import Fraction

from enterprise_math.abc_signed_exponent_transport import (
    dyadic_difference_pressure_tower,
    signed_doubling_transport_state,
)


class SignedExponentTransportTests(unittest.TestCase):
    def test_fourth_power_counterexample_is_dyadic_difference_resonance(self) -> None:
        state = signed_doubling_transport_state(23, 41, 2)
        self.assertEqual(state.lower_difference_ratio, Fraction(3, 2))
        self.assertEqual(state.sum_residual, 1)
        self.assertEqual(state.difference_to_difference_multiplier, 1)
        self.assertEqual(state.difference_transport_class, "resonant")
        self.assertEqual(state.upper_difference_ratio, Fraction(3, 2))

        self.assertEqual(state.lower_sum_ratio, Fraction(1, 128))
        self.assertEqual(state.difference_residual, 192)
        self.assertEqual(state.sum_to_difference_multiplier, 192)
        self.assertEqual(state.sum_transport_class, "amplified")

    def test_doubling_can_strictly_amplify_difference_pressure(self) -> None:
        state = signed_doubling_transport_state(7, 17, 2)
        self.assertEqual(state.lower_difference_ratio, Fraction(1, 6))
        self.assertEqual(state.sum_residual, 13)
        self.assertEqual(state.difference_to_difference_multiplier, 13)
        self.assertEqual(state.upper_difference_ratio, Fraction(13, 6))
        self.assertEqual(state.difference_transport_class, "amplified")

    def test_doubling_never_attenuates_either_sign(self) -> None:
        fixtures = [(3, 5, 2), (7, 17, 2), (11, 13, 3), (5, 59, 3)]
        for q, p, exponent in fixtures:
            state = signed_doubling_transport_state(q, p, exponent)
            self.assertGreaterEqual(state.upper_difference_ratio, state.lower_difference_ratio)
            self.assertGreaterEqual(state.upper_difference_ratio, state.lower_sum_ratio)
            self.assertGreaterEqual(state.difference_to_difference_multiplier, 1)
            self.assertGreaterEqual(state.sum_to_difference_multiplier, 1)

    def test_resonant_dyadic_tower_can_remain_constant(self) -> None:
        tower = dyadic_difference_pressure_tower(3, 5, 2, 2)
        self.assertEqual(tower.exponents, (2, 4, 8))
        self.assertEqual(tower.pressures, (Fraction(1, 2),) * 3)
        self.assertEqual(tower.step_multipliers, (1, 1))
        self.assertTrue(tower.nondecreasing_verified)

    def test_once_difference_is_active_it_stays_active_under_doubling(self) -> None:
        tower = dyadic_difference_pressure_tower(23, 41, 2, 1)
        self.assertGreaterEqual(tower.pressures[0], 1)
        self.assertGreaterEqual(tower.pressures[1], 1)


if __name__ == "__main__":
    unittest.main()
