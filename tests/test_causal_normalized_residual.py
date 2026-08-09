import unittest

from enterprise_math.causal_finite_range_grade import direct_window_grade
from enterprise_math.causal_normalized_residual import (
    normalized_residual_signature,
    reconstruct_future_value,
    structural_class_count,
    structural_classes,
    words,
)


class CausalNormalizedResidualTests(unittest.TestCase):
    def test_binary_sum_has_one_structural_future_type_after_bulk_is_removed(self):
        alphabet = (0, 1)
        prefixes = tuple(prefix for length in range(5) for prefix in words(alphabet, length))
        observation = lambda word: sum(word)
        self.assertEqual(
            structural_class_count(alphabet, prefixes, 4, observation),
            1,
        )
        self.assertEqual(
            normalized_residual_signature(alphabet, (1, 1, 0), 3, observation),
            normalized_residual_signature(alphabet, (0,), 3, observation),
        )

    def test_bulk_plus_normalized_increment_reconstructs_exact_future_value(self):
        prefix = (1, 1, 0)
        suffix = (1, 0, 1, 1)
        current = sum(prefix)
        increment = sum(prefix + suffix) - current
        self.assertEqual(reconstruct_future_value(current, increment), sum(prefix + suffix))

    def test_pair_window_grade_needs_only_last_symbol_structurally(self):
        alphabet = (0, 1)
        local_grade = lambda pair: 5 if pair[0] == pair[1] else -2
        observation = lambda word: direct_window_grade(word, 2, local_grade)
        prefixes = tuple(prefix for length in range(1, 5) for prefix in words(alphabet, length))
        classes = structural_classes(alphabet, prefixes, 3, observation)
        self.assertLessEqual(len(set(classes.values())), 2)
        # Prefixes ending in the same symbol have identical future grade increments,
        # regardless of already accumulated bulk grade.
        for left in prefixes:
            for right in prefixes:
                if left[-1] == right[-1]:
                    self.assertEqual(classes[left], classes[right])

    def test_three_window_grade_has_at_most_last_two_symbol_structural_types(self):
        alphabet = (0, 1)
        local_grade = lambda triple: 3 if triple[0] == triple[2] else 1
        observation = lambda word: direct_window_grade(word, 3, local_grade)
        prefixes = tuple(prefix for length in range(2, 6) for prefix in words(alphabet, length))
        classes = structural_classes(alphabet, prefixes, 3, observation)
        self.assertLessEqual(len(set(classes.values())), 4)
        for left in prefixes:
            for right in prefixes:
                if left[-2:] == right[-2:]:
                    self.assertEqual(classes[left], classes[right])

    def test_full_history_integer_encoding_does_not_collapse_after_normalization(self):
        # O(w) interprets a binary word as an integer.  Subtracting the current
        # integer does not make its future response history-free because appending
        # a suffix scales the old prefix by 2^|suffix|.
        alphabet = (0, 1)

        def binary_code(word):
            value = 0
            for bit in word:
                value = 2 * value + bit
            return value

        prefixes = words(alphabet, 4)
        classes = structural_classes(alphabet, prefixes, 3, binary_code)
        self.assertEqual(len(set(classes.values())), 16)


if __name__ == "__main__":
    unittest.main()
