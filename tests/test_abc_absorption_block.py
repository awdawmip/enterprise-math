import math
import unittest

from enterprise_math.abc_absorption_block import (
    block_absorption_state,
    block_absorption_terms,
    block_derivative_content,
    block_raw_additive_content,
    minimum_absorption_redundancy_block_formula,
    normalized_block_derivative_coefficients,
    normalized_block_derivative_value,
    triple_block_additive_content,
)
from enterprise_math.abc_absorption_formula import minimum_absorption_redundancy_support_formula


class AbcAbsorptionBlockTests(unittest.TestCase):
    def test_block_derivative_content_is_image_generator(self) -> None:
        self.assertEqual(normalized_block_derivative_coefficients(242), ((2, 11), (11, 4)))
        self.assertEqual(block_derivative_content(242), 1)
        self.assertEqual(normalized_block_derivative_value(242, (-1, 3)), 1)

        self.assertEqual(normalized_block_derivative_coefficients(243), ((3, 5),))
        self.assertEqual(block_derivative_content(243), 5)
        self.assertEqual(normalized_block_derivative_value(243, (1,)), 5)

        self.assertEqual(block_derivative_content(1), 0)

    def test_raw_additive_block_contents_reconstruct_global_content(self) -> None:
        self.assertEqual(block_raw_additive_content(242), 11)
        self.assertEqual(block_raw_additive_content(243), 405)
        self.assertEqual(triple_block_additive_content(1, 242, 243), 1)

        self.assertEqual(block_raw_additive_content(8), 12)
        self.assertEqual(block_raw_additive_content(9), 6)
        self.assertEqual(triple_block_additive_content(1, 8, 9), 6)

    def test_block_formula_examples(self) -> None:
        self.assertEqual(block_absorption_terms(1, 242, 243), (5,))
        self.assertEqual(minimum_absorption_redundancy_block_formula(1, 242, 243), 5)

        self.assertEqual(block_absorption_terms(2, 7, 9), (3, 14, 4))
        self.assertEqual(minimum_absorption_redundancy_block_formula(2, 7, 9), 1)

        self.assertEqual(block_absorption_terms(5, 7, 12), (6, 14, 10))
        self.assertEqual(minimum_absorption_redundancy_block_formula(5, 7, 12), 2)

    def test_compact_state(self) -> None:
        state = block_absorption_state(1, 242, 243)
        self.assertEqual(state["radicals"], (1, 22, 3))
        self.assertEqual(state["multiplicity_residuals"], (1, 11, 81))
        self.assertEqual(state["block_derivative_contents"], (0, 1, 5))
        self.assertEqual(state["raw_additive_content"], 1)
        self.assertEqual(state["eta_min"], 5)

    def test_block_formula_matches_cross_prime_formula_exhaustively(self) -> None:
        checked = 0
        for c in range(3, 100):
            for a in range(1, c):
                b = c - a
                if math.gcd(a, b) != 1:
                    continue
                try:
                    block_value = minimum_absorption_redundancy_block_formula(a, b, c)
                except ValueError:
                    continue
                support_value = minimum_absorption_redundancy_support_formula(a, b, c)
                self.assertEqual(block_value, support_value)
                checked += 1
        self.assertGreater(checked, 1000)


if __name__ == "__main__":
    unittest.main()
