import itertools
import unittest
from fractions import Fraction

from enterprise_math.presentation_storage_depth_pareto import (
    closed_literal_macro_rule_count,
    execute_word_from_macro_table,
    full_terminal_readout_rule_count,
    literal_macro_pareto_frontier,
    literal_macro_rule_count,
    macro_execution_blocks,
    macro_execution_matches_literal,
    presentation_depth_table,
    presentation_pareto_point,
    precompute_literal_macro_table,
    terminal_readout_scalar_count,
    transition_macro_scalar_count,
    word_transition_matrix,
)


class PresentationStorageDepthParetoTests(unittest.TestCase):
    def test_closed_rule_count_matches_literal_sum(self):
        for action_count in range(1, 6):
            for depth in range(1, 8):
                self.assertEqual(
                    literal_macro_rule_count(action_count, depth),
                    closed_literal_macro_rule_count(action_count, depth),
                )

    def test_binary_horizon_twelve_frontier(self):
        frontier = literal_macro_pareto_frontier(2, 12)
        self.assertEqual(
            tuple(point.macro_depth for point in frontier),
            (1, 2, 3, 4, 6, 12),
        )
        self.assertEqual(
            tuple(point.stored_macro_rules for point in frontier),
            (2, 6, 14, 30, 126, 8190),
        )
        self.assertEqual(
            tuple(point.worst_case_execution_blocks for point in frontier),
            (12, 6, 4, 3, 2, 1),
        )

    def test_unary_endpoint_is_linear_storage_not_exponential(self):
        table = presentation_depth_table(1, 6)
        self.assertEqual(table[0], (1, 1, 6))
        self.assertEqual(table[-1], (6, 6, 1))
        self.assertEqual(full_terminal_readout_rule_count(1, 6), 6)

    def test_macro_execution_matches_literal_for_noncommuting_generators(self):
        matrices = {
            "A": ((1, 1), (0, 1)),
            "B": ((1, 0), (1, 1)),
        }
        words = tuple(
            word
            for length in range(0, 7)
            for word in itertools.product(tuple(matrices), repeat=length)
        )
        for word in words:
            literal = word_transition_matrix(matrices, word)
            for depth in range(1, max(1, len(word)) + 1):
                self.assertTrue(
                    macro_execution_matches_literal(matrices, word, depth)
                )
                self.assertEqual(
                    execute_word_from_macro_table(matrices, word, depth),
                    literal,
                )

    def test_macro_table_contains_exact_derived_transitions_not_new_law(self):
        matrices = {
            "A": ((1, 1), (0, 1)),
            "B": ((1, 0), (1, 1)),
        }
        table = precompute_literal_macro_table(matrices, 3)
        self.assertEqual(len(table), 2 + 4 + 8)
        for word, stored in table.items():
            self.assertEqual(stored, word_transition_matrix(matrices, word))

    def test_fraction_predictive_matrices_are_supported(self):
        matrices = {
            "A": (
                (Fraction(1, 2), Fraction(1, 3)),
                (Fraction(0), Fraction(1)),
            ),
            "B": (
                (Fraction(1), Fraction(0)),
                (Fraction(2, 5), Fraction(1, 2)),
            ),
        }
        word = ("A", "B", "A", "A", "B")
        self.assertTrue(macro_execution_matches_literal(matrices, word, 2))
        self.assertTrue(macro_execution_matches_literal(matrices, word, 5))

    def test_state_dimension_changes_scalar_storage_not_rule_count(self):
        point = presentation_pareto_point(
            2,
            8,
            2,
            state_dimension=4,
        )
        self.assertEqual(point.stored_macro_rules, 6)
        self.assertEqual(point.stored_transition_scalars, 96)
        self.assertEqual(point.worst_case_execution_blocks, 4)

        self.assertEqual(transition_macro_scalar_count(2, 2, 4), 96)
        self.assertEqual(transition_macro_scalar_count(2, 2, 2), 24)

    def test_terminal_readout_table_and_transition_table_have_different_per_rule_state_costs(self):
        # Through horizon4 with two actions there are 30 nonempty literal words.
        self.assertEqual(full_terminal_readout_rule_count(2, 4), 30)
        # A reusable 5-state transition macro stores 25 scalars per word.
        self.assertEqual(transition_macro_scalar_count(2, 4, 5), 30 * 25)
        # A terminal readout with 2 output rows stores only 10 scalars per word,
        # but cannot by itself continue arbitrary suffix execution.
        self.assertEqual(terminal_readout_scalar_count(2, 4, 5, 2), 30 * 10)

    def test_macro_execution_block_formula(self):
        self.assertEqual(macro_execution_blocks(0, 3), 0)
        self.assertEqual(macro_execution_blocks(1, 3), 1)
        self.assertEqual(macro_execution_blocks(7, 3), 3)
        self.assertEqual(macro_execution_blocks(12, 4), 3)

    def test_validation(self):
        with self.assertRaises(ValueError):
            literal_macro_rule_count(0, 2)
        with self.assertRaises(ValueError):
            presentation_pareto_point(2, 3, 4)
        with self.assertRaises(ValueError):
            macro_execution_blocks(-1, 2)


if __name__ == "__main__":
    unittest.main()
