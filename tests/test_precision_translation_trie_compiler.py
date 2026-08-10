import unittest
from itertools import combinations

from enterprise_math.precision_translation_trie_compiler import (
    compile_translation_trie_state,
    subgroup_translation_language,
    subgroup_trie_class_count,
    translation_centers,
    translation_future_signature,
    translation_trie_class_count,
    translation_trie_partition_is_exact,
    trie_deficit_node_count,
)


class PrecisionTranslationTrieCompilerTests(unittest.TestCase):
    def test_single_translation_recovers_valuation_partition_size(self):
        for prime in (2, 3, 5):
            for cap in range(1, 5):
                self.assertEqual(
                    translation_trie_class_count((0,), prime, cap), cap + 1
                )
                self.assertTrue(
                    translation_trie_partition_is_exact((0,), prime, cap)
                )

    def test_full_translation_language_recovers_exact_residue(self):
        for prime, cap in ((2, 3), (3, 2), (5, 1)):
            modulus = prime**cap
            language = tuple(range(modulus))
            self.assertEqual(translation_trie_class_count(language, prime, cap), modulus)
            self.assertEqual(trie_deficit_node_count(language, prime, cap), 0)
            self.assertTrue(translation_trie_partition_is_exact(language, prime, cap))

    def test_subgroup_languages_recover_closed_form(self):
        for prime in (2, 3, 5):
            for cap in range(1, 5):
                for subgroup_level in range(cap + 1):
                    language = subgroup_translation_language(prime, cap, subgroup_level)
                    self.assertEqual(
                        subgroup_trie_class_count(prime, cap, subgroup_level),
                        subgroup_level + prime ** (cap - subgroup_level),
                    )
                    self.assertTrue(
                        translation_trie_partition_is_exact(language, prime, cap)
                    )

    def test_arbitrary_small_translation_subsets_match_future_signatures(self):
        # Exhaust every nonempty subset for 2^3 and 3^2 state spaces.
        for prime, cap in ((2, 3), (3, 2)):
            modulus = prime**cap
            residues = tuple(range(modulus))
            for size in range(1, modulus + 1):
                for language in combinations(residues, size):
                    self.assertTrue(
                        translation_trie_partition_is_exact(language, prime, cap)
                    )
                    tokens = {
                        compile_translation_trie_state(
                            residue, language, prime, cap
                        )
                        for residue in residues
                    }
                    signatures = {
                        translation_future_signature(
                            residue, language, prime, cap
                        )
                        for residue in residues
                    }
                    self.assertEqual(len(tokens), len(signatures))
                    self.assertEqual(
                        len(tokens),
                        translation_trie_class_count(language, prime, cap),
                    )

    def test_center_count_plus_deficit_nodes_is_exact(self):
        examples = (
            ((0, 4), 2, 3),
            ((0, 1, 4), 2, 3),
            ((0, 3, 6), 3, 2),
            ((1, 2, 7), 2, 3),
        )
        for language, prime, cap in examples:
            centers = translation_centers(language, prime, cap)
            self.assertEqual(
                translation_trie_class_count(language, prime, cap),
                len(centers) + trie_deficit_node_count(language, prime, cap),
            )

    def test_distinct_tokens_are_signature_distinguishable(self):
        language = (0, 1, 4)
        prime = 2
        cap = 3
        by_token = {}
        for residue in range(prime**cap):
            token = compile_translation_trie_state(residue, language, prime, cap)
            signature = translation_future_signature(residue, language, prime, cap)
            by_token.setdefault(token, set()).add(signature)
        self.assertTrue(all(len(signatures) == 1 for signatures in by_token.values()))
        representative_signatures = [next(iter(signatures)) for signatures in by_token.values()]
        self.assertEqual(
            len(representative_signatures), len(set(representative_signatures))
        )

    def test_invalid_inputs_fail_closed(self):
        with self.assertRaises(ValueError):
            translation_trie_class_count((), 2, 3)
        with self.assertRaises(ValueError):
            translation_trie_class_count((0,), 4, 3)
        with self.assertRaises(ValueError):
            subgroup_translation_language(2, 3, 4)


if __name__ == "__main__":
    unittest.main()
