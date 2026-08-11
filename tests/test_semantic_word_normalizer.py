import itertools
import unittest

from enterprise_math.future_word_cache_pareto import (
    prefix_append_free_effect_fixture,
)
from enterprise_math.semantic_word_normalizer import (
    apply_effect_id,
    generated_transformation_monoid,
    normalize_word_parallel,
    normalize_word_sequential,
    normalized_word_effect_matches_literal,
    parallel_normalization_depth,
    word_representation_resource_report,
)


class SemanticWordNormalizerTests(unittest.TestCase):
    def test_identity_flip_generates_two_element_monoid(self):
        states = (0, 1)
        operations = {
            "id": {0: 0, 1: 1},
            "flip": {0: 1, 1: 0},
        }
        monoid = generated_transformation_monoid(states, operations)
        self.assertEqual(monoid.size, 2)

        for length in range(9):
            for word in itertools.product(tuple(operations), repeat=length):
                self.assertTrue(
                    normalized_word_effect_matches_literal(
                        monoid,
                        operations,
                        word,
                    )
                )
                sequential = normalize_word_sequential(monoid, word)
                parallel, depth = normalize_word_parallel(monoid, word)
                self.assertEqual(sequential, parallel)
                self.assertEqual(depth, parallel_normalization_depth(length))

    def test_normalized_effect_applies_exactly(self):
        states = (0, 1)
        operations = {
            "id": {0: 0, 1: 1},
            "flip": {0: 1, 1: 0},
        }
        monoid = generated_transformation_monoid(states, operations)
        odd = normalize_word_sequential(monoid, ("flip", "id", "flip", "flip"))
        self.assertEqual(apply_effect_id(monoid, 0, odd), 1)
        self.assertEqual(apply_effect_id(monoid, 1, odd), 0)

    def test_horizon_twenty_resource_triangle(self):
        states = (0, 1)
        operations = {
            "id": {0: 0, 1: 1},
            "flip": {0: 1, 1: 0},
        }
        report = word_representation_resource_report(states, operations, 20)
        self.assertEqual(report.monoid_size, 2)
        self.assertEqual(report.generator_state_table_cells, 4)
        self.assertEqual(report.literal_word_id_entries, 2 ** 21 - 2)
        self.assertEqual(report.semantic_effect_state_cells, 4)
        self.assertEqual(report.cayley_table_cells, 4)
        self.assertEqual(report.normal_form_total_cells, 8)
        self.assertEqual(report.generator_state_execution_rounds, 20)
        self.assertEqual(report.literal_cache_execution_rounds, 1)
        self.assertEqual(report.parallel_normal_form_rounds, 6)
        self.assertTrue(report.normal_form_auxiliary_smaller_than_literal_index)

    def test_short_horizon_literal_cache_can_be_smaller_than_cayley_table(self):
        states = (0, 1)
        operations = {
            "id": {0: 0, 1: 1},
            "flip": {0: 1, 1: 0},
        }
        report = word_representation_resource_report(states, operations, 1)
        self.assertEqual(report.literal_word_id_entries, 2)
        self.assertEqual(report.cayley_table_cells, 4)
        self.assertFalse(report.normal_form_auxiliary_smaller_than_literal_index)
        self.assertLess(report.literal_cache_total_cells, report.normal_form_total_cells)

    def test_duplicate_identity_generators_collapse_to_one_element(self):
        states = (0, 1)
        identity = {0: 0, 1: 1}
        operations = {"a": identity, "b": identity}
        monoid = generated_transformation_monoid(states, operations)
        self.assertEqual(monoid.size, 1)
        report = word_representation_resource_report(states, operations, 12)
        self.assertEqual(report.cayley_table_cells, 1)
        self.assertEqual(report.semantic_effect_state_cells, 2)
        self.assertEqual(report.normal_form_total_cells, 3)
        self.assertEqual(report.parallel_normal_form_rounds, 5)

    def test_free_prefix_fixture_can_make_monoid_table_more_expensive_for_short_horizon(self):
        states, operations = prefix_append_free_effect_fixture(2, 3)
        monoid = generated_transformation_monoid(states, operations)
        # Identity plus all14 distinct nonempty word effects through depth3 are
        # already present, before considering any longer overflow effect.
        self.assertGreaterEqual(monoid.size, 15)
        report = word_representation_resource_report(states, operations, 3)
        self.assertGreater(report.cayley_table_cells, report.literal_word_id_entries)
        self.assertFalse(report.normal_form_auxiliary_smaller_than_literal_index)

    def test_parallel_depth_law(self):
        expected = {0: 0, 1: 0, 2: 1, 3: 2, 4: 2, 5: 3, 8: 3, 9: 4, 20: 5}
        for length, depth in expected.items():
            self.assertEqual(parallel_normalization_depth(length), depth)

    def test_validation(self):
        with self.assertRaises(ValueError):
            generated_transformation_monoid((), {"a": {}})
        with self.assertRaises(ValueError):
            parallel_normalization_depth(-1)


if __name__ == "__main__":
    unittest.main()
