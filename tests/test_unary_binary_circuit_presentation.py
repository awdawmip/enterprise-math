import unittest
from fractions import Fraction

from enterprise_math.unary_binary_circuit_presentation import (
    binary_execution_blocks,
    binary_execution_exponents,
    binary_power_execution_matches_literal,
    binary_power_exponents,
    binary_power_rule_count,
    binary_precompute_multiplications,
    compare_binary_to_contiguous_same_storage,
    execute_unary_power_from_binary_table,
    first_horizon_binary_strictly_dominates_same_storage_contiguous,
    literal_unary_power,
    worst_case_binary_execution_blocks,
)


class UnaryBinaryCircuitPresentationTests(unittest.TestCase):
    def test_binary_exponents_and_rule_count(self):
        self.assertEqual(binary_power_exponents(1), (1,))
        self.assertEqual(binary_power_exponents(13), (1, 2, 4, 8))
        self.assertEqual(binary_power_exponents(1024), tuple(1 << bit for bit in range(11)))
        self.assertEqual(binary_power_rule_count(13), 4)
        self.assertEqual(binary_power_rule_count(1024), 11)
        self.assertEqual(binary_precompute_multiplications(1024), 10)

    def test_binary_execution_exponents_are_exact_binary_expansion(self):
        self.assertEqual(binary_execution_exponents(0), ())
        self.assertEqual(binary_execution_exponents(13), (1, 4, 8))
        self.assertEqual(sum(binary_execution_exponents(13)), 13)
        self.assertEqual(binary_execution_blocks(13), 3)

    def test_exact_worst_case_popcount_formula(self):
        for horizon in range(1, 1000):
            brute = max(value.bit_count() for value in range(1, horizon + 1))
            self.assertEqual(worst_case_binary_execution_blocks(horizon), brute)

    def test_nontrivial_integer_matrix_power_matches_literal_for_all_exponents(self):
        generator = ((1, 1), (1, 0))
        horizon = 80
        for exponent in range(horizon + 1):
            self.assertTrue(
                binary_power_execution_matches_literal(
                    generator,
                    exponent,
                    horizon,
                )
            )
            self.assertEqual(
                execute_unary_power_from_binary_table(generator, exponent, horizon),
                literal_unary_power(generator, exponent),
            )

    def test_fraction_matrix_power_matches_literal(self):
        generator = (
            (Fraction(1, 2), Fraction(1, 3)),
            (Fraction(2, 5), Fraction(3, 4)),
        )
        for exponent in range(0, 25):
            self.assertTrue(
                binary_power_execution_matches_literal(generator, exponent, 24)
            )

    def test_first_strict_same_storage_domination_is_horizon_thirteen(self):
        self.assertEqual(
            first_horizon_binary_strictly_dominates_same_storage_contiguous(),
            13,
        )
        comparison = compare_binary_to_contiguous_same_storage(13)
        self.assertEqual(comparison.binary_stored_rules, 4)
        self.assertEqual(comparison.binary_worst_execution_blocks, 3)
        self.assertEqual(comparison.contiguous_macro_depth_at_same_rule_count, 4)
        self.assertEqual(comparison.contiguous_worst_execution_blocks, 4)
        self.assertTrue(comparison.binary_strictly_faster_at_same_rule_count)

    def test_horizon_1024_same_storage_gap_is_large(self):
        comparison = compare_binary_to_contiguous_same_storage(1024)
        self.assertEqual(comparison.binary_stored_rules, 11)
        self.assertEqual(comparison.binary_worst_execution_blocks, 10)
        self.assertEqual(comparison.contiguous_macro_depth_at_same_rule_count, 11)
        self.assertEqual(comparison.contiguous_worst_execution_blocks, 94)
        self.assertEqual(comparison.execution_blocks_saved, 84)

    def test_full_literal_unary_table_has_depth_one_but_linear_storage(self):
        comparison = compare_binary_to_contiguous_same_storage(255)
        self.assertEqual(comparison.binary_stored_rules, 8)
        self.assertEqual(comparison.binary_worst_execution_blocks, 8)
        # Binary circuit does not claim to beat a full table's one lookup; it
        # beats the contiguous literal table at the same small storage.
        self.assertGreater(comparison.contiguous_worst_execution_blocks, 8)

    def test_validation(self):
        with self.assertRaises(ValueError):
            binary_power_exponents(0)
        with self.assertRaises(ValueError):
            binary_execution_exponents(-1)
        with self.assertRaises(ValueError):
            execute_unary_power_from_binary_table(((1,),), 5, 4)


if __name__ == "__main__":
    unittest.main()
