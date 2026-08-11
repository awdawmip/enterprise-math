import itertools
import unittest

from enterprise_math.prefix_observable_or_word_semantics import (
    compose_prefix_mask_traces,
    full_support_prefix_trace_count,
    prefix_mask_trace,
    prefix_observable_word_count_report,
    prefix_state_trace,
    prefix_trace_composition_matches_words,
    prefix_trace_count_exact_length,
    terminal_effect_count_exact_length,
    terminal_effect_matches_prefix_trace,
)


class PrefixObservableORWordSemanticsTests(unittest.TestCase):
    def test_ab_ba_same_terminal_effect_but_different_prefix_trace(self):
        ab = prefix_mask_trace((0, 1), 2)
        ba = prefix_mask_trace((1, 0), 2)
        self.assertEqual(ab, (0b01, 0b11))
        self.assertEqual(ba, (0b10, 0b11))
        self.assertNotEqual(ab, ba)
        self.assertTrue(terminal_effect_matches_prefix_trace((0, 1), 2))
        self.assertTrue(terminal_effect_matches_prefix_trace((1, 0), 2))

    def test_prefix_trace_is_exact_for_all_initial_states(self):
        word = (0, 2, 1, 2)
        trace = prefix_mask_trace(word, 3)
        for initial in range(8):
            self.assertEqual(
                prefix_state_trace(initial, word, 3),
                tuple(initial | mask for mask in trace),
            )
        # Starting from0 recovers the normal form itself, proving extensional
        # minimality for full prefix-state observation.
        self.assertEqual(prefix_state_trace(0, word, 3), trace)

    def test_prefix_trace_composition_matches_concatenation_exhaustively_small(self):
        actions = (0, 1, 2)
        for left_length in range(4):
            for right_length in range(4):
                for left in itertools.product(actions, repeat=left_length):
                    for right in itertools.product(actions, repeat=right_length):
                        self.assertTrue(
                            prefix_trace_composition_matches_words(left, right, 3)
                        )
                        composed = compose_prefix_mask_traces(
                            prefix_mask_trace(left, 3),
                            prefix_mask_trace(right, 3),
                            3,
                        )
                        self.assertEqual(
                            composed,
                            prefix_mask_trace((*left, *right), 3),
                        )

    def test_count_formula_matches_exhaustive_word_enumeration(self):
        for k in range(1, 5):
            actions = tuple(range(k))
            for length in range(0, 6):
                words = tuple(itertools.product(actions, repeat=length))
                prefix_traces = {prefix_mask_trace(word, k) for word in words}
                terminal_effects = {
                    trace[-1] if trace else 0
                    for trace in prefix_traces
                }
                self.assertEqual(
                    len(prefix_traces),
                    prefix_trace_count_exact_length(k, length),
                )
                self.assertEqual(
                    len(terminal_effects),
                    terminal_effect_count_exact_length(k, length),
                )

    def test_k5_h5_reference_counts(self):
        report = prefix_observable_word_count_report(5, 5)
        self.assertEqual(report.literal_word_count, 5**5)
        self.assertEqual(report.terminal_effect_count, 31)
        self.assertEqual(report.prefix_trace_count, 1045)
        self.assertEqual(report.full_support_prefix_trace_count, 120)
        self.assertEqual(full_support_prefix_trace_count(5, 5), 120)

    def test_full_support_prefix_order_count_with_stuttering(self):
        # k=3,H=5: all three generators must first appear; choose their order
        # (3!) and two later discovery positions among positions2..5 (C(4,2)).
        self.assertEqual(full_support_prefix_trace_count(3, 5), 6 * 6)

    def test_one_generator_terminal_monoid_finite_but_prefix_word_semantics_unbounded(self):
        traces = [prefix_mask_trace((0,) * length, 1) for length in range(1, 21)]
        self.assertEqual(len(set(traces)), 20)
        self.assertTrue(all(trace[-1] == 1 for trace in traces))
        self.assertEqual(
            {terminal_effect_count_exact_length(1, length) for length in range(1, 21)},
            {1},
        )

    def test_prefix_trace_count_sits_between_terminal_effects_and_literal_words(self):
        for k in range(1, 6):
            for length in range(1, 8):
                report = prefix_observable_word_count_report(k, length)
                self.assertLessEqual(report.terminal_effect_count, report.prefix_trace_count)
                self.assertLessEqual(report.prefix_trace_count, report.literal_word_count)

    def test_validation(self):
        with self.assertRaises(ValueError):
            prefix_mask_trace((2,), 2)
        with self.assertRaises(ValueError):
            prefix_trace_count_exact_length(0, 3)


if __name__ == "__main__":
    unittest.main()
