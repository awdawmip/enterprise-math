import unittest

from enterprise_math.homomorphic_semantic_reflection import (
    evaluate_integer_polynomial,
    homomorphic_semantic_reflection_report,
    modular_zero_false_positive,
    modular_zero_reflects_exactly_on_interval,
    polynomial_evaluation_commutes_with_modulus,
    product_branch_reflection_for_all_residues,
)


def is_prime(value):
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


class HomomorphicSemanticReflectionTests(unittest.TestCase):
    def test_polynomial_evaluation_commutes_with_every_small_modulus(self):
        polynomials = (
            (0,),
            (1,),
            (3, -2, 5),
            (7, 0, -3, 2),
        )
        for coefficients in polynomials:
            for value in range(-8, 9):
                for modulus in range(1, 16):
                    self.assertTrue(
                        polynomial_evaluation_commutes_with_modulus(
                            coefficients,
                            value,
                            modulus,
                        )
                    )

    def test_every_finite_modulus_has_exact_zero_reflection_false_positive(self):
        for modulus in range(1, 30):
            value = modular_zero_false_positive(modulus)
            self.assertNotEqual(value, 0)
            self.assertEqual(value % modulus, 0)
            report = homomorphic_semantic_reflection_report(modulus)
            self.assertTrue(report.polynomial_syntax_preserved)
            self.assertTrue(report.exact_zero_forward_sound)
            self.assertFalse(report.exact_zero_reflected_on_unbounded_integers)

    def test_height_bound_restores_zero_reflection(self):
        for bound in range(0, 10):
            for modulus in range(1, 15):
                self.assertEqual(
                    modular_zero_reflects_exactly_on_interval(modulus, bound),
                    modulus > bound,
                )
                if modulus > bound:
                    for value in range(-bound, bound + 1):
                        self.assertEqual(value % modulus == 0, value == 0)

    def test_product_branch_reflection_exactly_matches_prime_moduli(self):
        for modulus in range(2, 50):
            self.assertEqual(
                product_branch_reflection_for_all_residues(modulus),
                is_prime(modulus),
                modulus,
            )
            self.assertEqual(
                homomorphic_semantic_reflection_report(modulus).product_branch_reflection,
                is_prime(modulus),
            )
        self.assertFalse(product_branch_reflection_for_all_residues(1))

    def test_polynomial_evaluator_reference(self):
        # 3 - 2x + 5x^2 at x=4.
        self.assertEqual(evaluate_integer_polynomial((3, -2, 5), 4), 75)

    def test_validation(self):
        with self.assertRaises(ValueError):
            evaluate_integer_polynomial((), 1)
        with self.assertRaises(TypeError):
            evaluate_integer_polynomial((1, True), 1)
        with self.assertRaises(ValueError):
            modular_zero_reflects_exactly_on_interval(2, -1)
        with self.assertRaises(ValueError):
            product_branch_reflection_for_all_residues(0)


if __name__ == "__main__":
    unittest.main()
