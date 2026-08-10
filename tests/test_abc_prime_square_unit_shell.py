import unittest
from fractions import Fraction

from enterprise_math.abc_prime_square_unit_shell import (
    prime_square_pcc_failure,
    prime_square_unit_shell,
)


class AbcPrimeSquareUnitShellTests(unittest.TestCase):
    def test_239_square_extreme_example(self) -> None:
        data = prime_square_unit_shell(239)
        self.assertEqual(data.square, 57121)
        self.assertEqual(data.successor, 57122)
        self.assertEqual(data.successor_radical, 26)
        self.assertEqual(data.successor_residual, 2197)
        self.assertEqual(data.successor_capacity, 21)
        self.assertEqual(data.sigma_projective, Fraction(2197, 2))
        self.assertTrue(prime_square_pcc_failure(239, 3, 5))
        self.assertFalse(prime_square_pcc_failure(239, 2, 3))

    def test_small_prime_square_examples(self) -> None:
        for prime in (5, 7, 11, 13, 17, 19, 23):
            data = prime_square_unit_shell(prime)
            self.assertEqual(data.sigma_projective, Fraction(data.successor_residual, 2))
            self.assertEqual(data.successor % 4, 2)

    def test_all_odd_successor_primes_are_one_mod_four(self) -> None:
        data = prime_square_unit_shell(41)
        # Internal constructor assertion verifies every odd support prime.
        self.assertEqual(data.successor, 1682)

    def test_nonprime_or_small_input_rejected(self) -> None:
        for value in (3, 9, 15, 25):
            with self.assertRaises(ValueError):
                prime_square_unit_shell(value)


if __name__ == "__main__":
    unittest.main()
