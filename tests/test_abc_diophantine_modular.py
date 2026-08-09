import math
import unittest

from enterprise_math.abc_absorption_two_variable import minimum_linf_diophantine_solution
from enterprise_math.abc_diophantine_modular import (
    minimum_linf_two_variable_modular,
    reduced_minimum_linf_two_variable_modular,
)


class AbcDiophantineModularTests(unittest.TestCase):
    def test_hand_examples(self) -> None:
        one = minimum_linf_two_variable_modular(5, 2, 1)
        self.assertEqual((one.u, one.v, one.radius), (1, -2, 2))
        self.assertEqual(one.candidate_differences, (3, -4))

        two = minimum_linf_two_variable_modular(5, 2, 2)
        self.assertEqual((two.u, two.v, two.radius), (0, 1, 1))
        self.assertEqual(two.difference, -1)

        balanced = minimum_linf_two_variable_modular(5, 3, 32)
        self.assertEqual((balanced.u, balanced.v, balanced.radius), (4, 4, 4))
        self.assertEqual(balanced.difference, 0)

    def test_reduced_solver(self) -> None:
        reduced = reduced_minimum_linf_two_variable_modular(10, 4, 2)
        self.assertEqual((reduced.A, reduced.B, reduced.N), (5, 2, 1))
        self.assertEqual((reduced.u, reduced.v, reduced.radius), (1, -2, 2))

    def test_closed_solver_matches_binary_interval_solver_exhaustively(self) -> None:
        checked = 0
        for A in range(1, 25):
            for B in range(1, 25):
                for N in range(0, 80):
                    d = math.gcd(A, B)
                    if N % d:
                        continue
                    closed = reduced_minimum_linf_two_variable_modular(A, B, N)
                    if N == 0:
                        self.assertEqual(closed.radius, 0)
                        continue
                    reference = minimum_linf_diophantine_solution(A, B, N)
                    self.assertEqual(closed.radius, reference.radius)
                    self.assertEqual(A * closed.u + B * closed.v, N)
                    checked += 1
        self.assertGreater(checked, 10000)

    def test_only_two_nearest_difference_representatives_are_needed(self) -> None:
        for A, B, N in ((73, 7, 2304), (11, 4, 405), (19, 1, 256), (23, 2, 1)):
            result = minimum_linf_two_variable_modular(A, B, N)
            self.assertLessEqual(len(result.candidate_differences), 2)
            self.assertIn(result.difference, result.candidate_differences)

    def test_unsolvable_reduction_rejected(self) -> None:
        with self.assertRaises(ValueError):
            reduced_minimum_linf_two_variable_modular(6, 10, 7)


if __name__ == "__main__":
    unittest.main()
