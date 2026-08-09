import math
import unittest

from enterprise_math.abc_absorption_formula import (
    additive_relation_content,
    cross_block_absorption_terms,
    minimum_absorption_redundancy_support_formula,
    one_plus_squarefree_to_prime_power_absorption,
    raw_additive_relation_vector,
    squarefree_perfect_absorption,
    support_formula_matches_determinantal_formula,
    two_prime_power_blocks_absorption,
)


class AbcAbsorptionFormulaTests(unittest.TestCase):
    def test_raw_relation_rows_and_cross_terms(self) -> None:
        self.assertEqual(raw_additive_relation_vector(1, 8, 9), (12, -6))
        self.assertEqual(additive_relation_content(1, 8, 9), 6)
        self.assertEqual(cross_block_absorption_terms(1, 8, 9), (1,))
        self.assertEqual(minimum_absorption_redundancy_support_formula(1, 8, 9), 1)

        self.assertEqual(raw_additive_relation_vector(1, 3, 4), (1, -4))
        self.assertEqual(additive_relation_content(1, 3, 4), 1)
        self.assertEqual(cross_block_absorption_terms(1, 3, 4), (2,))
        self.assertEqual(minimum_absorption_redundancy_support_formula(1, 3, 4), 2)

    def test_closed_formula_matches_determinantal_formula_exhaustively(self) -> None:
        checked = 0
        for c in range(3, 100):
            for a in range(1, c):
                b = c - a
                if math.gcd(a, b) != 1:
                    continue
                self.assertTrue(support_formula_matches_determinantal_formula(a, b, c))
                checked += 1
        self.assertGreater(checked, 1000)

    def test_squarefree_family_has_perfect_absorption(self) -> None:
        for triple in ((1, 5, 6), (2, 3, 5), (5, 6, 11), (14, 15, 29)):
            self.assertTrue(squarefree_perfect_absorption(*triple))
            self.assertEqual(minimum_absorption_redundancy_support_formula(*triple), 1)

    def test_one_plus_squarefree_prime_power_family(self) -> None:
        self.assertEqual(one_plus_squarefree_to_prime_power_absorption(3, 2, 2), 2)
        self.assertEqual(one_plus_squarefree_to_prime_power_absorption(7, 2, 3), 3)
        self.assertEqual(one_plus_squarefree_to_prime_power_absorption(15, 2, 4), 4)
        self.assertEqual(one_plus_squarefree_to_prime_power_absorption(31, 2, 5), 5)

    def test_two_prime_power_blocks_and_perfect_absorption(self) -> None:
        data = two_prime_power_blocks_absorption(2, 3, 3, 2)
        self.assertEqual(data["row_content"], 6)
        self.assertEqual(data["eta_min"], 1)
        self.assertTrue(data["perfect_absorption"])

        fermat = two_prime_power_blocks_absorption(2, 4, 17, 1)
        self.assertEqual(fermat["eta_min"], 4)
        self.assertFalse(fermat["perfect_absorption"])

    def test_high_quality_examples(self) -> None:
        self.assertEqual(
            minimum_absorption_redundancy_support_formula(1, 4374, 4375), 1
        )
        self.assertEqual(
            minimum_absorption_redundancy_support_formula(
                2, 3**10 * 109, 23**5
            ),
            1,
        )

    def test_invalid_family_inputs(self) -> None:
        with self.assertRaises(ValueError):
            one_plus_squarefree_to_prime_power_absorption(9, 2, 3)
        with self.assertRaises(ValueError):
            two_prime_power_blocks_absorption(2, 2, 3, 2)


if __name__ == "__main__":
    unittest.main()
