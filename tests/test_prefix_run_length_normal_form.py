import itertools
import unittest

from enterprise_math.prefix_observable_or_word_semantics import prefix_mask_trace
from enterprise_math.prefix_run_length_normal_form import (
    PrefixRun,
    canonical_word_from_prefix_runs,
    compose_prefix_run_forms,
    decode_prefix_runs_to_trace,
    normalize_prefix_word_to_runs,
    prefix_run_composition_matches_words,
    prefix_run_form_count_exact_length,
    prefix_run_form_count_with_phases,
    prefix_run_normal_form_matches_word,
    prefix_run_phase_count,
    prefix_run_word_length,
)


class PrefixRunLengthNormalFormTests(unittest.TestCase):
    def test_reference_word(self):
        word = (0, 0, 1, 0, 2, 2)
        form = normalize_prefix_word_to_runs(word, 3)
        self.assertEqual(
            form,
            (
                PrefixRun(0, 2),
                PrefixRun(1, 2),
                PrefixRun(2, 2),
            ),
        )
        self.assertEqual(prefix_run_word_length(form, 3), 6)
        self.assertEqual(prefix_run_phase_count(form, 3), 3)
        self.assertEqual(decode_prefix_runs_to_trace(form, 3), prefix_mask_trace(word, 3))
        self.assertEqual(canonical_word_from_prefix_runs(form, 3), (0, 0, 1, 1, 2, 2))
        self.assertTrue(prefix_run_normal_form_matches_word(word, 3))

    def test_exhaustive_small_words_round_trip(self):
        for k in range(1, 5):
            actions = tuple(range(k))
            for length in range(0, 7):
                for word in itertools.product(actions, repeat=length):
                    self.assertTrue(prefix_run_normal_form_matches_word(word, k))
                    form = normalize_prefix_word_to_runs(word, k)
                    self.assertLessEqual(len(form), k)
                    self.assertEqual(sum(phase.run_length for phase in form), length)
                    self.assertEqual(
                        decode_prefix_runs_to_trace(form, k),
                        prefix_mask_trace(word, k),
                    )

    def test_composition_matches_concatenation_exhaustively(self):
        actions = (0, 1, 2)
        for left_length in range(4):
            for right_length in range(4):
                for left in itertools.product(actions, repeat=left_length):
                    for right in itertools.product(actions, repeat=right_length):
                        self.assertTrue(
                            prefix_run_composition_matches_words(left, right, 3)
                        )

    def test_composition_merges_right_phases_already_seen_on_left(self):
        left = normalize_prefix_word_to_runs((0, 0, 2), 4)
        right = normalize_prefix_word_to_runs((0, 1, 1, 2, 3), 4)
        composed = compose_prefix_run_forms(left, right, 4)
        self.assertEqual(
            composed,
            (
                PrefixRun(0, 2),
                PrefixRun(2, 2),  # right's initial 0 phase merges here
                PrefixRun(1, 3),  # right's later 2 phase merges here
                PrefixRun(3, 1),
            ),
        )
        self.assertEqual(
            decode_prefix_runs_to_trace(composed, 4),
            prefix_mask_trace((0, 0, 2, 0, 1, 1, 2, 3), 4),
        )

    def test_k_one_reduces_to_duration_addition(self):
        for left_length in range(0, 8):
            for right_length in range(0, 8):
                left = normalize_prefix_word_to_runs((0,) * left_length, 1)
                right = normalize_prefix_word_to_runs((0,) * right_length, 1)
                combined = compose_prefix_run_forms(left, right, 1)
                total = left_length + right_length
                expected = () if total == 0 else (PrefixRun(0, total),)
                self.assertEqual(combined, expected)

    def test_count_formula_by_phase_count_matches_exhaustive_forms(self):
        for k in range(1, 5):
            actions = tuple(range(k))
            for length in range(0, 7):
                forms = {
                    normalize_prefix_word_to_runs(word, k)
                    for word in itertools.product(actions, repeat=length)
                }
                self.assertEqual(
                    len(forms),
                    prefix_run_form_count_exact_length(k, length),
                )
                if length > 0:
                    by_phase = {
                        phases: sum(1 for form in forms if len(form) == phases)
                        for phases in range(1, min(k, length) + 1)
                    }
                    for phases, count in by_phase.items():
                        self.assertEqual(
                            count,
                            prefix_run_form_count_with_phases(k, length, phases),
                        )

    def test_form_structure_is_bounded_by_generator_count_even_for_long_words(self):
        word = tuple(index % 5 for index in range(1000))
        form = normalize_prefix_word_to_runs(word, 5)
        self.assertEqual(len(form), 5)
        self.assertEqual(prefix_run_word_length(form, 5), 1000)

    def test_validation(self):
        with self.assertRaises(ValueError):
            normalize_prefix_word_to_runs((3,), 3)
        with self.assertRaises(ValueError):
            decode_prefix_runs_to_trace((PrefixRun(0, 1), PrefixRun(0, 2)), 2)
        with self.assertRaises(ValueError):
            decode_prefix_runs_to_trace((PrefixRun(0, 0),), 2)


if __name__ == "__main__":
    unittest.main()
