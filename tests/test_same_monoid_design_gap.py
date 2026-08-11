import unittest

from enterprise_math.same_monoid_design_gap import (
    duplicate_singleton_catalogue,
    full_action_catalogue,
    same_monoid_design_gap_report,
)
from enterprise_math.set_cover_formulaic_execution import (
    distinct_word_effect_masks,
    formulaic_word_matrix_matches_literal,
)


class SameMonoidDesignGapTests(unittest.TestCase):
    def test_gap_scales_from_one_to_m(self):
        for universe_size in range(2, 9):
            report = same_monoid_design_gap_report(universe_size)
            self.assertEqual(report.action_count, universe_size + 1)
            self.assertEqual(report.semantic_effect_count, 1 << universe_size)
            self.assertEqual(report.duplicate_catalogue_minimum, universe_size)
            self.assertEqual(report.full_action_catalogue_minimum, 1)
            self.assertEqual(report.minimum_basis_gap, universe_size - 1)

    def test_catalogues_have_identical_generated_effect_sets(self):
        for universe_size in range(2, 7):
            left = duplicate_singleton_catalogue(universe_size)
            right = full_action_catalogue(universe_size)
            self.assertEqual(
                distinct_word_effect_masks(universe_size, left),
                distinct_word_effect_masks(universe_size, right),
            )

    def test_same_formulaic_executor_law_on_both_catalogues(self):
        universe_size = 4
        catalogues = (
            duplicate_singleton_catalogue(universe_size),
            full_action_catalogue(universe_size),
        )
        words = (
            (),
            (0,),
            (0, 1),
            (4,),
            (3, 2, 1, 0),
            (4, 4, 0, 2),
        )
        for catalogue in catalogues:
            for word in words:
                self.assertTrue(
                    formulaic_word_matrix_matches_literal(
                        universe_size,
                        catalogue,
                        word,
                    )
                )

    def test_validation(self):
        with self.assertRaises(ValueError):
            duplicate_singleton_catalogue(1)
        with self.assertRaises(ValueError):
            full_action_catalogue(False)


if __name__ == "__main__":
    unittest.main()
