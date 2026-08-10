import unittest
from fractions import Fraction

from enterprise_math.abc_odd_prime_exponent_cyclotomic import (
    activation_pressure_bounds,
    odd_prime_exponent_cyclotomic_state,
)


class OddPrimeExponentCyclotomicTests(unittest.TestCase):
    def test_cube_sum_is_the_ell_three_specialization(self) -> None:
        state = odd_prime_exponent_cyclotomic_state(11, 13, 3, "sum")
        self.assertEqual(state.projective_ratio, Fraction(7, 6))
        self.assertEqual(state.cyclotomic_factor, 3 * 7**2)
        self.assertEqual(state.cyclotomic_residual, 7)
        self.assertEqual(state.repeated_modulus, 7**2)
        self.assertEqual(state.crt_root_choice_count, 2)
        self.assertEqual(state.constraints[0].root_order, 6)
        bounds = activation_pressure_bounds(state)
        self.assertTrue(bounds["cyclotomic_repetition_forced"])

    def test_cube_difference_is_the_ell_three_specialization(self) -> None:
        state = odd_prime_exponent_cyclotomic_state(23, 71, 3, "difference")
        self.assertEqual(state.projective_ratio, Fraction(1372, 47))
        self.assertEqual(state.cyclotomic_factor, 3 * 7**4)
        self.assertEqual(state.cyclotomic_residual, 7**3)
        self.assertEqual(state.repeated_modulus, 7**4)
        self.assertEqual(state.crt_root_choice_count, 2)
        self.assertEqual(state.constraints[0].root_order, 3)
        bounds = activation_pressure_bounds(state, Fraction(20, 1))
        self.assertTrue(bounds["active"])

    def test_fifth_power_sum_has_four_local_ratio_classes(self) -> None:
        state = odd_prime_exponent_cyclotomic_state(37, 59, 5, "sum")
        self.assertEqual(state.projective_ratio, Fraction(31, 30))
        self.assertEqual(state.cyclotomic_factor, 31**2 * 8501)
        self.assertEqual(state.cyclotomic_residual, 31)
        self.assertEqual(state.repeated_modulus, 31**2)
        self.assertEqual(state.crt_root_choice_count, 4)
        item = state.constraints[0]
        self.assertEqual((item.prime, item.exponent, item.root_order), (31, 2, 10))
        self.assertEqual(item.local_root_count, 4)
        self.assertEqual(31 % 10, 1)
        bounds = activation_pressure_bounds(state)
        self.assertLessEqual(
            bounds["actual_class_density"],
            bounds["pressure_class_density_upper_bound"],
        )

    def test_fifth_power_difference_has_four_local_ratio_classes(self) -> None:
        state = odd_prime_exponent_cyclotomic_state(19, 29, 5, "difference")
        self.assertEqual(state.projective_ratio, Fraction(121, 48))
        self.assertEqual(state.cyclotomic_factor, 5 * 11**3 * 271)
        self.assertEqual(state.cyclotomic_residual, 11**2)
        self.assertEqual(state.repeated_modulus, 11**3)
        self.assertEqual(state.crt_root_choice_count, 4)
        self.assertEqual(state.constraints[0].root_order, 5)
        self.assertEqual(11 % 10, 1)

    def test_seventh_power_examples_follow_one_mod_fourteen_support(self) -> None:
        diff_state = odd_prime_exponent_cyclotomic_state(3, 31, 7, "difference")
        self.assertEqual(diff_state.projective_ratio, Fraction(29, 17))
        self.assertEqual(diff_state.constraints[0].prime, 29)
        self.assertEqual(diff_state.constraints[0].local_root_count, 6)
        self.assertEqual(diff_state.crt_root_choice_count, 6)
        self.assertEqual(29 % 14, 1)

        sum_state = odd_prime_exponent_cyclotomic_state(13, 53, 7, "sum")
        self.assertEqual(sum_state.projective_ratio, Fraction(841, 462))
        self.assertEqual(sum_state.constraints[0].prime, 29)
        self.assertEqual(sum_state.constraints[0].exponent, 3)
        self.assertEqual(sum_state.crt_root_choice_count, 6)
        self.assertEqual(sum_state.constraints[0].root_order, 14)

    def test_squarefree_cyclotomic_factor_cannot_activate(self) -> None:
        state = odd_prime_exponent_cyclotomic_state(3, 5, 5, "sum")
        self.assertEqual(state.cyclotomic_residual, 1)
        self.assertLess(state.projective_ratio, 1)
        self.assertEqual(state.repeated_prime_count, 0)
        self.assertFalse(activation_pressure_bounds(state)["active"])


if __name__ == "__main__":
    unittest.main()
