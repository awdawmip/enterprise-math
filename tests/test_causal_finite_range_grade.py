import unittest

from enterprise_math.causal_finite_range_grade import (
    direct_window_grade,
    raw_memory_state_bound,
    sequential_window_grade,
)


class CausalFiniteRangeGradeTests(unittest.TestCase):
    def test_one_step_memory_reproduces_pair_grade_exactly(self):
        word = (0, 1, 1, 0, 1, 0)
        grade = lambda pair: 3 if pair[0] != pair[1] else -1
        self.assertEqual(
            sequential_window_grade(word, 2, grade),
            direct_window_grade(word, 2, grade),
        )

    def test_two_step_memory_reproduces_three_layer_interaction(self):
        word = (0, 1, 0, 1, 1, 0, 0)
        # Reward ABA-type windows differently from ABC/all-other patterns.
        grade = lambda triple: 5 if triple[0] == triple[2] else 2
        self.assertEqual(
            sequential_window_grade(word, 3, grade),
            direct_window_grade(word, 3, grade),
        )

    def test_five_layer_grade_still_uses_binary_one_symbol_growth(self):
        word = (0, 1, 2, 0, 1, 0, 2, 1, 0)
        grade = lambda block: sum((index + 1) * value for index, value in enumerate(block))
        self.assertEqual(
            sequential_window_grade(word, 5, grade),
            direct_window_grade(word, 5, grade),
        )

    def test_raw_suffix_state_count_is_only_an_upper_bound(self):
        self.assertEqual(raw_memory_state_bound(2, 1), 1)
        self.assertEqual(raw_memory_state_bound(2, 2), 3)
        self.assertEqual(raw_memory_state_bound(2, 3), 7)
        self.assertEqual(raw_memory_state_bound(3, 3), 13)

    def test_zero_local_grade_needs_no_effective_history_even_if_raw_window_is_large(self):
        word = (0, 1, 2, 0, 2, 1, 0)
        self.assertEqual(sequential_window_grade(word, 5, lambda block: 0), 0)
        self.assertEqual(direct_window_grade(word, 5, lambda block: 0), 0)


if __name__ == "__main__":
    unittest.main()
