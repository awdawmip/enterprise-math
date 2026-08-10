import unittest
from fractions import Fraction

from enterprise_math.abc_exponent_pressure_inheritance import (
    exponent_pressure_inheritance_state,
    inheritance_cocycle_holds,
)


class ExponentPressureInheritanceTests(unittest.TestCase):
    def test_fourth_power_counterexample_is_resonant_square_lift(self) -> None:
        state = exponent_pressure_inheritance_state(23, 41, 2, 4, "difference")
        self.assertEqual(state.exponent_ratio, 2)
        self.assertEqual(state.overlap_factor, 2)
        self.assertEqual(state.quotient_residual, 1)
        self.assertEqual(state.inheritance_multiplier, 1)
        self.assertEqual(state.transport_class, "resonant")
        self.assertEqual(state.lower_ratio, Fraction(3, 2))
        self.assertEqual(state.upper_ratio, Fraction(3, 2))
        self.assertEqual(state.new_indices, (4,))

    def test_ninth_power_difference_counterexample_is_resonant_cube_lift(self) -> None:
        state = exponent_pressure_inheritance_state(23, 71, 3, 9, "difference")
        self.assertEqual(state.exponent_ratio, 3)
        self.assertEqual(state.overlap_factor, 3)
        self.assertEqual(state.quotient_residual, 1)
        self.assertEqual(state.inheritance_multiplier, 1)
        self.assertEqual(state.lower_ratio, Fraction(1372, 47))
        self.assertEqual(state.upper_ratio, Fraction(1372, 47))
        self.assertEqual(state.new_indices, (9,))

    def test_ninth_power_sum_can_attenuate_active_cube_pressure(self) -> None:
        state = exponent_pressure_inheritance_state(5, 59, 3, 9, "sum")
        self.assertEqual(state.inheritance_multiplier, Fraction(1, 3))
        self.assertEqual(state.transport_class, "attenuated")
        self.assertEqual(state.lower_ratio, Fraction(13, 6))
        self.assertEqual(state.upper_ratio, Fraction(13, 18))
        self.assertGreaterEqual(state.lower_ratio, 1)
        self.assertLess(state.upper_ratio, 1)

    def test_ninth_power_sum_can_be_resonant(self) -> None:
        state = exponent_pressure_inheritance_state(11, 13, 3, 9, "sum")
        self.assertEqual(state.overlap_factor, 3)
        self.assertEqual(state.quotient_residual, 1)
        self.assertEqual(state.inheritance_multiplier, 1)
        self.assertEqual(state.transport_class, "resonant")
        self.assertEqual(state.lower_ratio, Fraction(7, 6))
        self.assertEqual(state.upper_ratio, Fraction(7, 6))

    def test_ninth_power_sum_can_amplify_subunit_cube_pressure(self) -> None:
        state = exponent_pressure_inheritance_state(7, 29, 3, 9, "sum")
        self.assertEqual(state.overlap_factor, 3)
        self.assertEqual(state.quotient_residual, 19)
        self.assertEqual(state.inheritance_multiplier, 19)
        self.assertEqual(state.transport_class, "amplified")
        self.assertEqual(state.lower_ratio, Fraction(1, 6))
        self.assertEqual(state.upper_ratio, Fraction(19, 6))
        self.assertLess(state.lower_ratio, 1)
        self.assertGreater(state.upper_ratio, 1)

    def test_ninth_power_difference_can_attenuate(self) -> None:
        state = exponent_pressure_inheritance_state(3, 5, 3, 9, "difference")
        self.assertEqual(state.overlap_factor, 1)
        self.assertEqual(state.quotient_residual, 1)
        self.assertEqual(state.inheritance_multiplier, Fraction(1, 3))
        self.assertEqual(state.transport_class, "attenuated")

    def test_inheritance_multiplier_is_a_divisibility_cocycle(self) -> None:
        self.assertTrue(inheritance_cocycle_holds(3, 5, 2, 4, 8, "difference"))
        direct = exponent_pressure_inheritance_state(3, 5, 2, 8, "difference")
        self.assertEqual(direct.inheritance_multiplier, 1)

    def test_even_ratio_same_sign_sum_is_rejected(self) -> None:
        with self.assertRaises(ValueError):
            exponent_pressure_inheritance_state(3, 5, 2, 4, "sum")


if __name__ == "__main__":
    unittest.main()
