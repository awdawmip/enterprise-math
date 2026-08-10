import unittest

from enterprise_math.abc_prime_cube_cyclotomic_support import (
    cube_difference_quadratic_multiplicity_support,
    cube_sum_activation_requires_repeated_one_mod_six,
    prime_cube_cyclotomic_support,
)


class PrimeCubeCyclotomicSupportTests(unittest.TestCase):
    def test_activated_cube_sum_repeated_prime_is_one_mod_six(self) -> None:
        support = prime_cube_cyclotomic_support(5, 59)
        self.assertEqual(support.phi6_factor, 3211)
        self.assertEqual(support.phi6_factorization, ((13, 2), (19, 1)))
        self.assertEqual(support.phi6_repeated_primes, (13,))
        self.assertTrue(cube_sum_activation_requires_repeated_one_mod_six(5, 59))

    def test_activated_cube_difference_repeated_quadratic_prime_is_one_mod_six(self) -> None:
        support = prime_cube_cyclotomic_support(5, 101)
        self.assertEqual(support.phi3_factorization, ((3, 1), (7, 2), (73, 1)))
        self.assertEqual(support.phi3_repeated_primes, (7,))
        self.assertEqual(cube_difference_quadratic_multiplicity_support(5, 101), (7,))

    def test_three_never_repeats(self) -> None:
        for q, p in ((5, 7), (7, 13), (13, 19), (13, 109)):
            support = prime_cube_cyclotomic_support(q, p)
            for factorization in (support.phi6_factorization, support.phi3_factorization):
                three_exponent = next((e for r, e in factorization if r == 3), 0)
                self.assertLessEqual(three_exponent, 1)

    def test_phi3_phi6_supports_are_disjoint(self) -> None:
        support = prime_cube_cyclotomic_support(13, 109)
        self.assertEqual(support.phi6_factorization, ((7, 3), (31, 1)))
        self.assertEqual(support.phi3_factorization, ((3, 1), (67, 2)))
        self.assertTrue(
            set(r for r, _e in support.phi6_factorization).isdisjoint(
                r for r, _e in support.phi3_factorization
            )
        )

    def test_safe_small_pair_is_squarefree_on_both_quadratic_factors(self) -> None:
        support = prime_cube_cyclotomic_support(3, 7)
        self.assertEqual(support.phi6_factorization, ((37, 1),))
        self.assertEqual(support.phi3_factorization, ((79, 1),))
        self.assertEqual(support.phi6_repeated_primes, ())
        self.assertEqual(support.phi3_repeated_primes, ())


if __name__ == "__main__":
    unittest.main()
