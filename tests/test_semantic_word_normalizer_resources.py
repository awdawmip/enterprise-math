import unittest

from enterprise_math.future_word_cache_pareto import prefix_append_free_effect_fixture
from enterprise_math.semantic_word_normalizer import generated_transformation_monoid
from enterprise_math.semantic_word_normalizer_resources import (
    first_horizon_cayley_smaller_than_literal_index,
    right_generator_transition_table,
    semantic_normalizer_resource_report,
)


class SemanticWordNormalizerResourceTests(unittest.TestCase):
    def test_identity_flip_resource_points(self):
        states = (0, 1)
        operations = {
            "id": {0: 0, 1: 1},
            "flip": {0: 1, 1: 0},
        }
        report = semantic_normalizer_resource_report(states, operations, 20)
        self.assertEqual(report.monoid_size, 2)
        self.assertEqual(report.shared_effect_action_cells, 4)

        self.assertEqual(report.sequential_automaton.auxiliary_storage_cells, 4)
        self.assertEqual(report.sequential_automaton.normalization_depth, 19)
        self.assertEqual(report.sequential_automaton.total_depth, 20)

        self.assertEqual(report.cayley_parallel.auxiliary_storage_cells, 4)
        self.assertEqual(report.cayley_parallel.normalization_depth, 5)
        self.assertEqual(report.cayley_parallel.total_depth, 6)

        self.assertEqual(report.literal_index.auxiliary_storage_cells, 2 ** 21 - 2)
        self.assertEqual(report.literal_index.total_depth, 1)
        self.assertEqual(report.first_cayley_break_even_horizon, 2)

    def test_right_generator_table_matches_cayley_generator_columns(self):
        states = (0, 1)
        operations = {
            "id": {0: 0, 1: 1},
            "flip": {0: 1, 1: 0},
        }
        monoid = generated_transformation_monoid(states, operations)
        table = right_generator_transition_table(monoid)
        self.assertEqual(len(table), monoid.size)
        self.assertTrue(all(len(row) == len(monoid.action_names) for row in table))
        for effect_id, row in enumerate(table):
            for action_index, action in enumerate(monoid.action_names):
                self.assertEqual(
                    row[action_index],
                    monoid.multiplication_table[effect_id][monoid.generator_ids[action]],
                )

    def test_duplicate_identity_generators_make_cayley_better_from_horizon_one(self):
        states = (0, 1)
        identity = {0: 0, 1: 1}
        operations = {"a": identity, "b": identity}
        report = semantic_normalizer_resource_report(states, operations, 12)
        self.assertEqual(report.monoid_size, 1)
        self.assertEqual(report.sequential_automaton.auxiliary_storage_cells, 2)
        self.assertEqual(report.cayley_parallel.auxiliary_storage_cells, 1)
        self.assertEqual(report.first_cayley_break_even_horizon, 1)

    def test_free_prefix_large_monoid_delays_cayley_break_even(self):
        states, operations = prefix_append_free_effect_fixture(2, 3)
        monoid = generated_transformation_monoid(states, operations)
        self.assertEqual(monoid.size, 16)
        self.assertEqual(first_horizon_cayley_smaller_than_literal_index(2, 16), 8)

        short = semantic_normalizer_resource_report(states, operations, 3)
        self.assertGreater(
            short.cayley_parallel.auxiliary_storage_cells,
            short.literal_index.auxiliary_storage_cells,
        )

        long = semantic_normalizer_resource_report(states, operations, 8)
        self.assertLess(
            long.cayley_parallel.auxiliary_storage_cells,
            long.literal_index.auxiliary_storage_cells,
        )

    def test_mk_vs_m2_tradeoff_opens_when_m_exceeds_generator_count(self):
        states, operations = prefix_append_free_effect_fixture(2, 3)
        report = semantic_normalizer_resource_report(states, operations, 8)
        self.assertEqual(report.monoid_size, 16)
        self.assertEqual(report.sequential_automaton.auxiliary_storage_cells, 32)
        self.assertEqual(report.cayley_parallel.auxiliary_storage_cells, 256)
        self.assertEqual(report.sequential_automaton.total_depth, 8)
        self.assertEqual(report.cayley_parallel.total_depth, 4)

    def test_break_even_formula_validation(self):
        self.assertEqual(first_horizon_cayley_smaller_than_literal_index(2, 2), 2)
        self.assertEqual(first_horizon_cayley_smaller_than_literal_index(1, 2), 5)
        with self.assertRaises(ValueError):
            first_horizon_cayley_smaller_than_literal_index(0, 2)


if __name__ == "__main__":
    unittest.main()
