import itertools
import unittest

from enterprise_math.set_cover_formulaic_execution import (
    action_masks,
    design_execution_separation_report,
    distinct_word_effect_masks,
    formulaic_word_matrix_matches_literal,
    minimum_cover_size_exact,
    parallel_union_normalization_depth,
    parallel_word_union_mask,
    word_union_mask,
)
from enterprise_math.integer_action_capability_basis import (
    INTEGER_MODULE,
    STATE_KERNEL,
    action_subset_preserves,
)
from enterprise_math.integer_action_capability_set_cover import (
    selected_sets_cover_universe,
    set_cover_action_matrices,
    set_cover_observation_rows,
    verify_set_cover_capability_equivalence,
)


class SetCoverFormulaicExecutionTests(unittest.TestCase):
    def test_named_instance_formulaic_word_effect(self):
        sets = ({0, 1}, {1, 2}, {2})
        word = (0, 2, 0, 1, 2)
        self.assertEqual(action_masks(3, sets), (0b011, 0b110, 0b100))
        self.assertEqual(word_union_mask(3, sets, word), 0b111)
        self.assertTrue(formulaic_word_matrix_matches_literal(3, sets, word))
        parallel, depth = parallel_word_union_mask(3, sets, word)
        self.assertEqual(parallel, 0b111)
        self.assertEqual(depth, 3)

    def test_execution_normalization_depth_is_logarithmic(self):
        expected = {0: 0, 1: 0, 2: 1, 3: 2, 4: 2, 5: 3, 8: 3, 9: 4, 32: 5}
        for length, depth in expected.items():
            self.assertEqual(parallel_union_normalization_depth(length), depth)

    def test_effect_count_is_number_of_distinct_candidate_unions(self):
        sets = ({0}, {1}, {2})
        self.assertEqual(len(distinct_word_effect_masks(3, sets)), 8)

        nested = ({0}, {0, 1}, {0, 1, 2})
        self.assertEqual(
            distinct_word_effect_masks(3, nested),
            frozenset({0b000, 0b001, 0b011, 0b111}),
        )

    def test_report_combines_easy_execution_with_minimum_cover_design(self):
        sets = ({0, 1}, {1, 2}, {2, 3}, {0, 3})
        report = design_execution_separation_report(4, sets, horizon=64)
        self.assertTrue(report.full_family_preserves_precision)
        self.assertEqual(report.minimum_preserving_action_count, 2)
        self.assertEqual(report.word_normal_form_bits, 4)
        self.assertEqual(report.word_normalization_depth_at_horizon, 6)
        self.assertEqual(report.word_normalization_bit_work_at_horizon, 4 * 63)

    def test_exhaustive_three_by_three_same_family_execution_and_selection(self):
        universe = (0, 1, 2)
        action_indices = (0, 1, 2)
        checked_families = 0
        checked_words = 0
        checked_subsets = 0

        for bits in itertools.product((0, 1), repeat=9):
            sets = []
            cursor = 0
            for _action in action_indices:
                subset = set()
                for element in universe:
                    if bits[cursor]:
                        subset.add(element)
                    cursor += 1
                sets.append(frozenset(subset))
            sets = tuple(sets)

            full = tuple(action_indices)
            if not selected_sets_cover_universe(3, sets, full):
                continue
            checked_families += 1
            actions = set_cover_action_matrices(3, sets)
            observations = set_cover_observation_rows(3)

            # Same compiled family: every word through length4 executes by OR.
            for length in range(5):
                for word in itertools.product(action_indices, repeat=length):
                    self.assertTrue(formulaic_word_matrix_matches_literal(3, sets, word))
                    mask, depth = parallel_word_union_mask(3, sets, word)
                    self.assertEqual(mask, word_union_mask(3, sets, word))
                    self.assertEqual(depth, parallel_union_normalization_depth(length))
                    checked_words += 1

            # The generator-subset design problem on the same matrices remains
            # exactly Set Cover at both project precision levels.
            for subset_size in range(4):
                for selected in itertools.combinations(action_indices, subset_size):
                    cover = selected_sets_cover_universe(3, sets, selected)
                    kernel = action_subset_preserves(
                        actions,
                        observations,
                        selected,
                        mode=STATE_KERNEL,
                    )
                    module = action_subset_preserves(
                        actions,
                        observations,
                        selected,
                        mode=INTEGER_MODULE,
                    )
                    self.assertEqual(cover, kernel)
                    self.assertEqual(cover, module)
                    self.assertTrue(
                        verify_set_cover_capability_equivalence(3, sets, selected)
                    )
                    checked_subsets += 1

            expected_min = next(
                size
                for size in range(1, 4)
                if any(
                    selected_sets_cover_universe(3, sets, selected)
                    for selected in itertools.combinations(action_indices, size)
                )
            )
            self.assertEqual(minimum_cover_size_exact(3, sets), expected_min)

        self.assertGreater(checked_families, 0)
        self.assertGreater(checked_words, 0)
        self.assertEqual(checked_subsets, checked_families * 8)

    def test_duplicate_actions_do_not_change_execution_effect_set_but_can_change_design_catalogue(self):
        sets = ({0, 1}, {0, 1}, {2})
        effects = distinct_word_effect_masks(3, sets)
        self.assertEqual(effects, frozenset({0b000, 0b011, 0b100, 0b111}))
        self.assertEqual(minimum_cover_size_exact(3, sets), 2)

    def test_validation(self):
        with self.assertRaises(ValueError):
            word_union_mask(0, ({0},), (0,))
        with self.assertRaises(ValueError):
            word_union_mask(2, ({0},), (1,))


if __name__ == "__main__":
    unittest.main()
