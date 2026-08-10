import unittest
from itertools import combinations

from enterprise_math.precision_crt_translation_compiler import (
    compile_correlated_crt_translation_state,
    correlated_crt_class_count,
    correlated_crt_future_signature,
    correlated_crt_partition_is_exact,
    crt_modulus,
    projected_translation_language,
)


class PrecisionCRTTranslationCompilerTests(unittest.TestCase):
    def test_correlated_action_set_factorizes_through_marginal_compilers(self):
        examples = (
            (((2, 1), (3, 1)), (0, 1)),
            (((2, 2), (3, 1)), (0, 1, 5)),
            (((2, 1), (3, 2)), (0, 3, 7)),
            (((2, 2), (5, 1)), (0, 4, 9)),
        )
        for components, language in examples:
            self.assertTrue(correlated_crt_partition_is_exact(language, components))
            modulus = crt_modulus(components)
            tokens = {
                compile_correlated_crt_translation_state(
                    residue, language, components
                )
                for residue in range(modulus)
            }
            signatures = {
                correlated_crt_future_signature(residue, language, components)
                for residue in range(modulus)
            }
            self.assertEqual(len(tokens), len(signatures))
            self.assertEqual(len(tokens), correlated_crt_class_count(language, components))

    def test_all_nonempty_languages_on_modulus_six(self):
        components = ((2, 1), (3, 1))
        residues = tuple(range(6))
        for size in range(1, 7):
            for language in combinations(residues, size):
                self.assertTrue(correlated_crt_partition_is_exact(language, components))

    def test_small_correlated_languages_on_twelve_do_not_break_factorization(self):
        components = ((2, 2), (3, 1))
        residues = tuple(range(12))
        for size in (1, 2, 3):
            for language in combinations(residues, size):
                self.assertTrue(correlated_crt_partition_is_exact(language, components))

    def test_projection_discards_only_cross_axis_action_correlation(self):
        components = ((2, 2), (3, 1))
        language = (0, 5)
        self.assertEqual(projected_translation_language(language, components, 0), (0, 1))
        self.assertEqual(projected_translation_language(language, components, 1), (0, 2))
        self.assertTrue(correlated_crt_partition_is_exact(language, components))

    def test_same_marginal_languages_give_same_compiler_complexity(self):
        components = ((2, 1), (3, 1))
        # Under CRT both languages project to {0,1} on each axis even though their
        # joint pairings are different.
        left = (0, 1)
        right = (0, 5)
        for index in range(2):
            self.assertEqual(
                projected_translation_language(left, components, index),
                projected_translation_language(right, components, index),
            )
        self.assertEqual(
            correlated_crt_class_count(left, components),
            correlated_crt_class_count(right, components),
        )

    def test_invalid_inputs_fail_closed(self):
        with self.assertRaises(ValueError):
            correlated_crt_class_count((), ((2, 1), (3, 1)))
        with self.assertRaises(ValueError):
            correlated_crt_class_count((0,), ((2, 1), (2, 2)))
        with self.assertRaises(ValueError):
            projected_translation_language((0,), ((2, 1),), 1)


if __name__ == "__main__":
    unittest.main()
