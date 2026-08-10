import unittest

from enterprise_math.nonlinear_profinite_ghost import (
    CONSTANTS,
    chosen_square_factor_for_prime,
    factor_root_mod_prime_power,
    intersective_polynomial,
    legendre_symbol,
    polynomial_has_integer_root,
    polynomial_root_modulus,
    profinite_ghost_report,
    two_adic_root_17,
)


PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)


class NonlinearProfiniteGhostTests(unittest.TestCase):
    def test_polynomial_has_no_integer_root(self):
        self.assertEqual(CONSTANTS, (13, 17, 221))
        self.assertFalse(polynomial_has_integer_root())
        for value in range(-30, 31):
            self.assertNotEqual(intersective_polynomial(value), 0)

    def test_odd_prime_character_choice_always_supplies_one_square_factor(self):
        for prime in PRIMES:
            constant = chosen_square_factor_for_prime(prime)
            self.assertIn(constant, CONSTANTS)
            if prime == 2:
                self.assertEqual(constant, 17)
                continue
            self.assertIn(legendre_symbol(constant, prime), (0, 1))
            if prime not in (13, 17):
                symbols = (
                    legendre_symbol(13, prime),
                    legendre_symbol(17, prime),
                    legendre_symbol(221, prime),
                )
                self.assertIn(1, symbols)

    def test_two_adic_root_of_seventeen_through_deep_levels(self):
        final = two_adic_root_17(14)
        self.assertEqual((final * final - 17) % (2 ** 14), 0)
        for exponent in range(1, 15):
            reduced = final % (2 ** exponent)
            self.assertEqual((reduced * reduced - 17) % (2 ** exponent), 0)
            self.assertEqual(intersective_polynomial(reduced) % (2 ** exponent), 0)

    def test_prime_power_factor_roots(self):
        for prime in PRIMES:
            max_exponent = 8 if prime == 2 else 4
            for exponent in range(1, max_exponent + 1):
                root, constant = factor_root_mod_prime_power(prime, exponent)
                modulus = prime ** exponent
                self.assertIn(constant, CONSTANTS)
                self.assertEqual((root * root - constant) % modulus, 0)
                self.assertEqual(intersective_polynomial(root) % modulus, 0)

    def test_crt_constructs_polynomial_root_for_every_modulus_in_large_prefix(self):
        for modulus in range(1, 501):
            root = polynomial_root_modulus(modulus)
            self.assertTrue(0 <= root < modulus or modulus == 1)
            self.assertEqual(
                intersective_polynomial(root) % modulus,
                0,
                modulus,
            )

    def test_mixed_prime_power_moduli(self):
        for modulus in (
            2 ** 9 * 3 ** 4,
            5 ** 3 * 7 ** 2,
            13 ** 3 * 17 ** 2,
            2 ** 6 * 5 ** 2 * 11 * 19,
            3 ** 3 * 13 ** 2 * 29,
        ):
            root = polynomial_root_modulus(modulus)
            self.assertEqual(intersective_polynomial(root) % modulus, 0)

    def test_report_locks_local_everywhere_global_nowhere_boundary(self):
        report = profinite_ghost_report(300)
        self.assertFalse(report.has_integer_root)
        self.assertTrue(report.all_checked_moduli_have_roots)
        self.assertEqual(report.checked_modulus_max, 300)

    def test_validation(self):
        with self.assertRaises(ValueError):
            chosen_square_factor_for_prime(1)
        with self.assertRaises(ValueError):
            legendre_symbol(13, 2)
        with self.assertRaises(ValueError):
            two_adic_root_17(0)
        with self.assertRaises(ValueError):
            polynomial_root_modulus(0)
        with self.assertRaises(TypeError):
            intersective_polynomial(True)


if __name__ == "__main__":
    unittest.main()
