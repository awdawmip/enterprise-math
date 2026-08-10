import unittest
from fractions import Fraction

from enterprise_math.abc_effective_small_derivative import (
    effective_bound_implies_capacity_abc,
    effective_small_derivative_state,
    rational_effective_small_derivative_bound_holds,
)
from enterprise_math.abc_small_derivative_block import (
    rational_small_derivative_bound_holds,
)


class AbcEffectiveSmallDerivativeTests(unittest.TestCase):
    def test_1_plus_242_refined_bound_is_exact(self) -> None:
        state = effective_small_derivative_state(1, 242, 243)
        self.assertEqual(state.mu, 27)
        self.assertEqual(state.eta_min, 5)
        self.assertEqual(state.effective_mu, Fraction(27, 5))
        self.assertEqual(state.pair_capacity_ab, 15)
        self.assertEqual(state.multiplicity_residual_c, 81)
        self.assertEqual(state.refined_mu_lower_bound, 27)
        self.assertEqual(state.refined_capacity_slack, 0)

    def test_effective_bound_can_hold_when_pasten_norm_bound_at_same_exponent_fails(self) -> None:
        triple = (1, 242, 243)
        self.assertFalse(rational_small_derivative_bound_holds(*triple, 1, 3))
        self.assertTrue(rational_effective_small_derivative_bound_holds(*triple, 1, 3))
        self.assertTrue(effective_bound_implies_capacity_abc(*triple, 1, 3))

    def test_1_plus_512_has_nonzero_refined_capacity_slack(self) -> None:
        state = effective_small_derivative_state(1, 512, 513)
        self.assertEqual(state.mu, 13)
        self.assertEqual(state.eta_min, 3)
        self.assertEqual(state.effective_mu, Fraction(13, 3))
        self.assertEqual(state.refined_mu_lower_bound, 3)
        self.assertEqual(state.refined_capacity_slack, 90)
        self.assertFalse(rational_small_derivative_bound_holds(1, 512, 513, 1, 4))
        self.assertTrue(rational_effective_small_derivative_bound_holds(1, 512, 513, 1, 4))

    def test_mersenne_family_member_shows_exact_eta_gain(self) -> None:
        state = effective_small_derivative_state(1, 31, 32)
        self.assertEqual(state.mu, 80)
        self.assertEqual(state.eta_min, 5)
        self.assertEqual(state.effective_mu, Fraction(16, 1))
        self.assertEqual(state.refined_mu_lower_bound, 80)
        self.assertEqual(state.refined_capacity_slack, 0)
        self.assertFalse(rational_effective_small_derivative_bound_holds(1, 31, 32, 4, 5))
        self.assertTrue(rational_effective_small_derivative_bound_holds(1, 31, 32, 5, 6))

    def test_generic_nonunit_example(self) -> None:
        state = effective_small_derivative_state(5, 7, 12)
        self.assertEqual(state.mu, 1)
        self.assertEqual(state.eta_min, 2)
        self.assertEqual(state.refined_mu_lower_bound, 1)
        self.assertEqual(state.refined_capacity_slack, 8)


if __name__ == "__main__":
    unittest.main()
