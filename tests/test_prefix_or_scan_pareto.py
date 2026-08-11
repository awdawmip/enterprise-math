import itertools
import unittest

from enterprise_math.prefix_or_scan_pareto import (
    hillis_steele_prefix_or,
    hillis_steele_word_or_gates,
    prefix_depth_lower_bound,
    prefix_scan_pareto_report,
    prefix_work_lower_bound_word_gates,
    sequential_prefix_or,
    sequential_word_or_gates,
)
from enterprise_math.prefix_observable_or_word_semantics import prefix_mask_trace


class PrefixORScanParetoTests(unittest.TestCase):
    def test_hillis_steele_matches_sequential_on_exhaustive_small_binary_masks(self):
        for bit_width in (1, 2, 3):
            alphabet = tuple(range(1 << bit_width))
            for length in range(1, 6):
                for values in itertools.product(alphabet, repeat=length):
                    self.assertEqual(
                        hillis_steele_prefix_or(values, bit_width),
                        sequential_prefix_or(values, bit_width),
                    )

    def test_scan_matches_prefix_word_semantics_on_one_hot_actions(self):
        k = 4
        for length in range(1, 7):
            for word in itertools.product(range(k), repeat=length):
                action_masks = tuple(1 << action for action in word)
                expected = prefix_mask_trace(word, k)
                self.assertEqual(sequential_prefix_or(action_masks, k), expected)
                self.assertEqual(hillis_steele_prefix_or(action_masks, k), expected)

    def test_exact_hillis_steele_gate_formula(self):
        expected = {
            1: 0,
            2: 1,
            3: 3,
            4: 5,
            5: 8,
            8: 17,
            20: 69,
        }
        for length, gates in expected.items():
            self.assertEqual(hillis_steele_word_or_gates(length), gates)

    def test_reference_h8_resource_tradeoff(self):
        report = prefix_scan_pareto_report(5, 8)
        self.assertEqual(report.work_lower_bound_word_gates, 7)
        self.assertEqual(report.depth_lower_bound, 3)

        seq = report.sequential_streaming
        self.assertEqual(seq.word_or_gates, 7)
        self.assertEqual(seq.bit_work, 35)
        self.assertEqual(seq.parallel_depth, 7)
        self.assertEqual(seq.extra_working_masks, 1)
        self.assertTrue(seq.full_prefix_semantics)

        par = report.hillis_steele_parallel
        self.assertEqual(par.word_or_gates, 17)
        self.assertEqual(par.bit_work, 85)
        self.assertEqual(par.parallel_depth, 3)
        self.assertEqual(par.extra_working_masks, 16)
        self.assertTrue(par.full_prefix_semantics)

        self.assertEqual(report.hillis_steele_extra_word_work, 10)
        self.assertEqual(report.hillis_steele_depth_saving, 4)

    def test_reference_h20_resource_tradeoff(self):
        report = prefix_scan_pareto_report(5, 20)
        self.assertEqual(report.sequential_streaming.word_or_gates, 19)
        self.assertEqual(report.sequential_streaming.parallel_depth, 19)
        self.assertEqual(report.hillis_steele_parallel.word_or_gates, 69)
        self.assertEqual(report.hillis_steele_parallel.parallel_depth, 5)
        self.assertEqual(report.hillis_steele_extra_word_work, 50)
        self.assertEqual(report.hillis_steele_depth_saving, 14)

    def test_sequential_hits_work_lower_bound_and_parallel_hits_depth_lower_bound(self):
        for length in range(1, 129):
            report = prefix_scan_pareto_report(3, length)
            self.assertEqual(
                report.sequential_streaming.word_or_gates,
                prefix_work_lower_bound_word_gates(length),
            )
            self.assertEqual(
                report.hillis_steele_parallel.parallel_depth,
                prefix_depth_lower_bound(length),
            )
            self.assertGreaterEqual(
                report.hillis_steele_parallel.word_or_gates,
                report.work_lower_bound_word_gates,
            )

    def test_terminal_only_balanced_tree_is_resource_attractive_but_semantically_invalid(self):
        report = prefix_scan_pareto_report(5, 20)
        terminal = report.terminal_only_balanced
        self.assertEqual(terminal.word_or_gates, 19)
        self.assertEqual(terminal.parallel_depth, 5)
        self.assertEqual(terminal.output_masks, 1)
        self.assertFalse(terminal.full_prefix_semantics)

        # Full prefix language requires all20 cumulative masks, not just final OR.
        self.assertEqual(report.sequential_streaming.output_masks, 20)
        self.assertEqual(report.hillis_steele_parallel.output_masks, 20)

    def test_sequential_gate_formula(self):
        for length in range(1, 100):
            self.assertEqual(sequential_word_or_gates(length), length - 1)

    def test_validation(self):
        with self.assertRaises(ValueError):
            prefix_scan_pareto_report(0, 4)
        with self.assertRaises(ValueError):
            hillis_steele_word_or_gates(0)
        with self.assertRaises(ValueError):
            sequential_prefix_or((8,), 3)


if __name__ == "__main__":
    unittest.main()
