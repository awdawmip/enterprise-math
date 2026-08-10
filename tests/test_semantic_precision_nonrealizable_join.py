import unittest

from enterprise_math.semantic_precision_nonrealizable_join import (
    modular_quotient_has_generic_product_branch_reflection,
    modulus_numeric_refines,
    prove_no_scalar_modulus_realizes_p2_numeric_and_branch_join,
    scalar_modulus_can_realize_p2_numeric_and_branch_join,
)


class SemanticPrecisionNonrealizableJoinTests(unittest.TestCase):
    def test_no_multiple_of_p_squared_is_branch_safe(self):
        for prime in (2, 3, 5, 7, 11):
            self.assertTrue(
                prove_no_scalar_modulus_realizes_p2_numeric_and_branch_join(prime)
            )
            target = prime * prime
            for multiplier in range(1, 20):
                modulus = target * multiplier
                self.assertTrue(modulus_numeric_refines(modulus, target))
                self.assertFalse(
                    modular_quotient_has_generic_product_branch_reflection(modulus)
                )
                self.assertFalse(
                    scalar_modulus_can_realize_p2_numeric_and_branch_join(
                        prime,
                        modulus,
                    )
                )

    def test_prime_field_has_branch_capability_but_not_p2_numeric_detail(self):
        for prime in (2, 3, 5, 7):
            self.assertTrue(
                modular_quotient_has_generic_product_branch_reflection(prime)
            )
            self.assertFalse(modulus_numeric_refines(prime, prime * prime))
            self.assertFalse(
                scalar_modulus_can_realize_p2_numeric_and_branch_join(
                    prime,
                    prime,
                )
            )

    def test_unrelated_prime_modulus_cannot_dominate_p2_numeric_requirement(self):
        self.assertFalse(modulus_numeric_refines(5, 4))
        self.assertTrue(modular_quotient_has_generic_product_branch_reflection(5))
        self.assertFalse(scalar_modulus_can_realize_p2_numeric_and_branch_join(2, 5))

    def test_validation(self):
        with self.assertRaises(ValueError):
            prove_no_scalar_modulus_realizes_p2_numeric_and_branch_join(4)
        with self.assertRaises(ValueError):
            modulus_numeric_refines(0, 2)
        with self.assertRaises(TypeError):
            modular_quotient_has_generic_product_branch_reflection(True)


if __name__ == "__main__":
    unittest.main()
