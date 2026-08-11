import itertools
import unittest

from enterprise_math.formulaic_idempotent_word_normal_form import (
    apply_mask_effect,
    commuting_idempotent_mask_fixture,
    formulaic_normal_form_resource_report,
    mask_normal_form_matches_literal,
    multiply_mask_normal_forms,
    parallel_formulaic_normalization,
    reachable_effect_count_including_identity,
    reachable_nonidentity_effect_count,
    word_mask_normal_form,
)
from enterprise_math.future_word_cache_pareto import (
    literal_word_count,
    unique_effect_count,
)
from enterprise_math.semantic_word_normalizer import generated_transformation_monoid
from enterprise_math.semantic_word_normalizer_resources import semantic_normalizer_resource_report


class FormulaicIdempotentWordNormalFormTests(unittest.TestCase):
    def test_exact_monoid_size_is_two_to_k(self):
        for k in range(1, 6):
            states, operations = commuting_idempotent_mask_fixture(k)
            monoid = generated_transformation_monoid(states, operations)
            self.assertEqual(len(states), 1 << k)
            self.assertEqual(monoid.size, 1 << k)

    def test_formulaic_normal_form_matches_all_small_literal_words(self):
        k = 3
        for length in range(6):
            for word in itertools.product(range(k), repeat=length):
                self.assertTrue(mask_normal_form_matches_literal(word, k))
                parallel, depth = parallel_formulaic_normalization(word, k)
                self.assertEqual(parallel, word_mask_normal_form(word, k))
                if length <= 1:
                    self.assertEqual(depth, 0)

    def test_idempotent_commutative_product(self):
        k = 5
        self.assertEqual(multiply_mask_normal_forms(0b00101, 0b11000, k), 0b11101)
        self.assertEqual(multiply_mask_normal_forms(0b00101, 0b00101, k), 0b00101)
        self.assertEqual(
            multiply_mask_normal_forms(0b00101, 0b11000, k),
            multiply_mask_normal_forms(0b11000, 0b00101, k),
        )

    def test_effect_application_is_one_or(self):
        self.assertEqual(apply_mask_effect(0b00101, 0b11000, 5), 0b11101)
        self.assertEqual(apply_mask_effect(0b11111, 0b00100, 5), 0b11111)

    def test_reachable_effect_count_by_horizon(self):
        k = 5
        self.assertEqual(reachable_effect_count_including_identity(k, 0), 1)
        self.assertEqual(reachable_effect_count_including_identity(k, 1), 6)
        self.assertEqual(reachable_effect_count_including_identity(k, 2), 16)
        self.assertEqual(reachable_effect_count_including_identity(k, 5), 32)
        self.assertEqual(reachable_effect_count_including_identity(k, 20), 32)
        self.assertEqual(reachable_nonidentity_effect_count(k, 20), 31)

    def test_unique_literal_effect_count_matches_subset_formula_small_case(self):
        k = 3
        states, operations = commuting_idempotent_mask_fixture(k)
        for horizon in (1, 2, 3):
            self.assertEqual(
                unique_effect_count(states, operations, horizon),
                reachable_nonidentity_effect_count(k, horizon),
            )

    def test_k5_h20_resource_separation(self):
        report = formulaic_normal_form_resource_report(5, 20)
        self.assertEqual(report.state_count, 32)
        self.assertEqual(report.monoid_size, 32)
        self.assertEqual(report.generic_cayley_cells, 1024)
        self.assertEqual(report.generic_effect_action_cells, 1024)
        self.assertEqual(report.formulaic_normal_form_bits, 5)
        self.assertEqual(report.formulaic_generator_metadata_entries, 5)
        self.assertEqual(report.formulaic_parallel_normalization_depth, 5)
        self.assertEqual(report.formulaic_total_depth, 6)
        self.assertEqual(report.literal_word_entries, literal_word_count(5, 20))
        self.assertGreater(report.literal_word_entries, 10**10)

    def test_generic_monoid_report_and_formulaic_report_agree_on_table_sizes(self):
        states, operations = commuting_idempotent_mask_fixture(4)
        generic = semantic_normalizer_resource_report(states, operations, 8)
        formulaic = formulaic_normal_form_resource_report(4, 8)
        self.assertEqual(generic.monoid_size, formulaic.monoid_size)
        self.assertEqual(generic.cayley_parallel.auxiliary_storage_cells, formulaic.generic_cayley_cells)
        self.assertEqual(generic.shared_effect_action_cells, formulaic.generic_effect_action_cells)
        self.assertEqual(generic.cayley_parallel.total_depth, formulaic.formulaic_total_depth)

    def test_formulaic_representation_avoids_both_generic_tables(self):
        report = formulaic_normal_form_resource_report(6, 12)
        self.assertEqual(report.monoid_size, 64)
        self.assertEqual(report.generic_cayley_cells, 4096)
        self.assertEqual(report.generic_effect_action_cells, 4096)
        self.assertEqual(report.formulaic_normal_form_bits, 6)
        self.assertEqual(report.formulaic_generator_metadata_entries, 6)

    def test_validation(self):
        with self.assertRaises(ValueError):
            commuting_idempotent_mask_fixture(0)
        with self.assertRaises(ValueError):
            word_mask_normal_form((3,), 3)
        with self.assertRaises(ValueError):
            apply_mask_effect(8, 0, 3)


if __name__ == "__main__":
    unittest.main()
