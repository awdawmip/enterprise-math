import unittest
from fractions import Fraction

from enterprise_math.abc_fourth_power_cyclotomic_boundary import (
    fourth_power_cyclotomic_boundary_state,
    fourth_power_top_forcing_boundary,
)


class FourthPowerCyclotomicBoundaryTests(unittest.TestCase):
    def test_difference_can_activate_with_squarefree_top_phi4(self) -> None:
        state = fourth_power_cyclotomic_boundary_state(23, 41)
        self.assertEqual((state.radius, state.center), (9, 32))
        self.assertEqual(state.centered_quadratic, 1105)
        self.assertEqual(state.phi4, 2210)
        self.assertTrue(state.phi4_squarefree)
        self.assertEqual(state.difference_top_residual, 1)
        self.assertEqual(state.difference_lower_carrier_residual, 3)
        self.assertEqual(state.rho_difference, Fraction(3, 2))
        boundary = fourth_power_top_forcing_boundary(23, 41)
        self.assertTrue(boundary["difference_active"])
        self.assertTrue(boundary["difference_top_squarefree"])
        self.assertTrue(boundary["difference_counterexample_to_top_forcing"])

    def test_difference_formula_can_be_subunit_in_same_shell(self) -> None:
        state = fourth_power_cyclotomic_boundary_state(3, 5)
        self.assertEqual((state.radius, state.center), (1, 4))
        self.assertLess(state.rho_difference, 1)
        self.assertTrue(state.phi4_squarefree)

    def test_sum_activation_forces_repeated_phi8_support(self) -> None:
        state = fourth_power_cyclotomic_boundary_state(839, 1277)
        self.assertEqual(state.rho_sum, Fraction(9521, 8464))
        self.assertFalse(state.phi8_odd_part_squarefree)
        self.assertEqual(state.sum_top_residual, 9521)
        boundary = fourth_power_top_forcing_boundary(839, 1277)
        self.assertTrue(boundary["sum_active"])
        self.assertTrue(boundary["sum_top_repetition_forced"])
        self.assertFalse(boundary["difference_counterexample_to_top_forcing"])

    def test_squarefree_phi8_odd_part_is_automatically_subunit(self) -> None:
        state = fourth_power_cyclotomic_boundary_state(3, 5)
        self.assertTrue(state.phi8_odd_part_squarefree)
        self.assertEqual(state.sum_top_residual, 1)
        self.assertLess(state.rho_sum, 1)

    def test_repeated_sum_prime_has_order_eight_support(self) -> None:
        state = fourth_power_cyclotomic_boundary_state(839, 1277)
        # p^4+q^4 = 2 * 17401 * 9521^2.
        self.assertEqual(state.sum_top_half, 17401 * 9521**2)
        self.assertEqual(9521 % 8, 1)


if __name__ == "__main__":
    unittest.main()
