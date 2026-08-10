import unittest

from enterprise_math.abc_prime_cube_cyclotomic_congruence import (
    prime_cube_cyclotomic_congruence_signature,
    ratio_space_compression_factor,
)


class PrimeCubeCyclotomicCongruenceTests(unittest.TestCase):
    def test_sum_repeated_prime_square_gives_two_order_six_roots(self) -> None:
        sig = prime_cube_cyclotomic_congruence_signature(5, 59, "sum")
        self.assertEqual(sig.repeated_modulus, 13**2)
        self.assertEqual(sig.root_choice_count, 2)
        self.assertEqual(len(sig.constraints), 1)
        item = sig.constraints[0]
        self.assertEqual((item.prime, item.exponent, item.order), (13, 2, 6))
        self.assertEqual(pow(item.observed_ratio, 6, item.modulus), 1)
        self.assertNotEqual(pow(item.observed_ratio, 2, item.modulus), 1)
        self.assertNotEqual(pow(item.observed_ratio, 3, item.modulus), 1)
        self.assertEqual(
            item.observed_ratio * item.inverse_ratio % item.modulus,
            1,
        )

    def test_difference_repeated_prime_square_gives_two_order_three_roots(self) -> None:
        sig = prime_cube_cyclotomic_congruence_signature(5, 101, "difference")
        self.assertEqual(sig.repeated_modulus, 7**2)
        self.assertEqual(sig.root_choice_count, 2)
        item = sig.constraints[0]
        self.assertEqual((item.prime, item.exponent, item.order), (7, 2, 3))
        self.assertEqual(pow(item.observed_ratio, 3, item.modulus), 1)
        self.assertNotEqual(item.observed_ratio, 1)

    def test_higher_prime_power_modulus_is_retained_exactly(self) -> None:
        sig = prime_cube_cyclotomic_congruence_signature(13, 109, "sum")
        self.assertEqual(sig.repeated_modulus, 7**3)
        self.assertEqual(sig.root_choice_count, 2)
        self.assertEqual(sig.constraints[0].exponent, 3)

    def test_sum_and_difference_signatures_are_independent(self) -> None:
        sum_sig = prime_cube_cyclotomic_congruence_signature(13, 109, "sum")
        diff_sig = prime_cube_cyclotomic_congruence_signature(13, 109, "difference")
        self.assertEqual(sum_sig.repeated_modulus, 7**3)
        self.assertEqual(diff_sig.repeated_modulus, 67**2)
        self.assertEqual(ratio_space_compression_factor(sum_sig), (7**3, 2))
        self.assertEqual(ratio_space_compression_factor(diff_sig), (67**2, 2))

    def test_squarefree_quadratic_factor_has_trivial_congruence_signature(self) -> None:
        sig = prime_cube_cyclotomic_congruence_signature(3, 7, "sum")
        self.assertEqual(sig.constraints, ())
        self.assertEqual(sig.repeated_modulus, 1)
        self.assertEqual(sig.root_choice_count, 1)


if __name__ == "__main__":
    unittest.main()
