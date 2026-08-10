import unittest
from fractions import Fraction

from enterprise_math.abc_prime_square_pell_shells import (
    both_prime_square_shells_failure_count_bound,
    predecessor_prime_square_shell,
    prime_square_shell_failure_pell_reduction,
    successor_prime_square_shell,
)


class AbcPrimeSquarePellShellTests(unittest.TestCase):
    def test_predecessor_17_square_recovers_1_plus_288(self) -> None:
        data = predecessor_prime_square_shell(17)
        self.assertEqual(data.neighboring_value, 288)
        self.assertEqual(data.neighboring_residual, 48)
        self.assertEqual(data.neighboring_capacity, 19)
        self.assertEqual(data.sigma_projective, Fraction(24, 1))

    def test_successor_239_square_recovers_hard_example(self) -> None:
        data = successor_prime_square_shell(239)
        self.assertEqual(data.neighboring_value, 57122)
        self.assertEqual(data.neighboring_residual, 2197)
        self.assertEqual(data.sigma_projective, Fraction(2197, 2))

    def test_both_pell_signs_occur(self) -> None:
        plus = prime_square_shell_failure_pell_reduction(17, 1, 1, 2)
        self.assertIsNotNone(plus)
        if plus is None:
            raise AssertionError("predecessor failure disappeared")
        self.assertEqual(plus.pell_identity, 1)

        minus = prime_square_shell_failure_pell_reduction(239, -1, 3, 5)
        self.assertIsNotNone(minus)
        if minus is None:
            raise AssertionError("successor failure disappeared")
        self.assertEqual(minus.pell_identity, -1)
        self.assertEqual(minus.pell_coefficient, 2)

    def test_combined_pell_bound_saves_above_half_exponent(self) -> None:
        X = 10**14
        bound = both_prime_square_shells_failure_count_bound(X, 3, 5)
        self.assertLess(bound, int(X**0.5))


if __name__ == "__main__":
    unittest.main()
