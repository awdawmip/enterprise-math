import unittest
from fractions import Fraction

from enterprise_math.abc_projective_capacity_condition import (
    projective_bound_implies_capacity_abc,
    projective_capacity_condition_state,
    rational_projective_capacity_bound_holds,
    support_log_derivative_load,
)


class AbcProjectiveCapacityConditionTests(unittest.TestCase):
    def test_exact_support_loads(self) -> None:
        self.assertEqual(support_log_derivative_load(1), 0)
        self.assertEqual(support_log_derivative_load(242), Fraction(15, 22))
        self.assertEqual(support_log_derivative_load(243), Fraction(5, 3))
        self.assertEqual(support_log_derivative_load(3**10 * 109), Fraction(1093, 327))

    def test_classic_projective_state_is_explicit_weighted_radical_defect(self) -> None:
        a = 2
        b = 3**10 * 109
        c = 23**5
        state = projective_capacity_condition_state(a, b, c)
        self.assertEqual(state.radical_product, 15042)
        self.assertEqual(state.sigma_projective, Fraction(6561, 11))
        self.assertEqual(state.effective_mu, 601)
        self.assertEqual(state.ordinary_mu, 601)
        self.assertEqual(max(state.cyclic_weighted_defects), Fraction(6561, 11))

    def test_resource_chain_can_be_strict(self) -> None:
        data = projective_capacity_condition_state(2, 7, 9)
        self.assertEqual(data.sigma_projective, Fraction(1, 3))
        self.assertEqual(data.effective_mu, 1)
        self.assertEqual(data.ordinary_mu, 1)
        self.assertLess(data.sigma_projective, data.effective_mu)

    def test_projective_bound_gives_exact_weighted_radical_consequence(self) -> None:
        triple = (1, 242, 243)
        self.assertTrue(rational_projective_capacity_bound_holds(*triple, 1, 3))
        self.assertTrue(projective_bound_implies_capacity_abc(*triple, 1, 3))

    def test_classic_strict_projective_vs_effective_condition_at_exact_rational_exponent(self) -> None:
        triple = (2, 3**10 * 109, 23**5)
        # 31/76 lies strictly between log_c(sigma_proj) and log_c(mu_eff).
        self.assertTrue(rational_projective_capacity_bound_holds(*triple, 31, 76))
        state = projective_capacity_condition_state(*triple)
        self.assertFalse(
            state.effective_mu.numerator**76
            < state.effective_mu.denominator**76 * triple[2]**31
        )


if __name__ == "__main__":
    unittest.main()
