import unittest

from enterprise_math.core import integer_nth_root
from enterprise_math.p023_p024_adaptive_threshold_precision import (
    adaptive_prime_word_best_first_threshold,
    adaptive_prime_word_cost_after_current,
    adaptive_unit_query_depth_after_current,
    adaptive_unit_query_depth_dp_after_current,
    minimal_static_future_thresholds_after_current,
    static_threshold_signature,
    static_thresholds_separate_domain,
    threshold_bit,
)


class P023P024AdaptiveThresholdPrecisionTests(unittest.TestCase):
    def test_binary_root_observation_is_exact_threshold_query(self):
        for root_exp in range(1, 8):
            for max_state in range(0, 2**root_exp):
                for state in range(max_state + 1):
                    for threshold in range(1, max_state + 2):
                        observed = integer_nth_root(state // threshold, root_exp)
                        self.assertEqual(observed, threshold_bit(state, threshold))

    def test_static_future_thresholds_are_exactly_all_adjacent_cuts(self):
        for max_state in range(0, 40):
            future = minimal_static_future_thresholds_after_current(max_state)
            full = (1,) + future if max_state >= 1 else ()
            self.assertTrue(static_thresholds_separate_domain(max_state, full))
            for omitted in future:
                reduced = tuple(t for t in full if t != omitted)
                self.assertFalse(static_thresholds_separate_domain(max_state, reduced))

    def test_adaptive_unit_depth_matches_information_bound(self):
        for max_state in range(0, 100):
            closed = adaptive_unit_query_depth_after_current(max_state)
            exact_dp = adaptive_unit_query_depth_dp_after_current(max_state)
            self.assertEqual(closed, exact_dp)
            expected = 0 if max_state <= 1 else (max_state - 1).bit_length()
            self.assertEqual(closed, expected)

    def test_static_vs_adaptive_gap_is_large(self):
        max_state = 64
        static_future_queries = len(
            minimal_static_future_thresholds_after_current(max_state)
        )
        adaptive_queries = adaptive_unit_query_depth_after_current(max_state)
        self.assertEqual(static_future_queries, 63)
        self.assertEqual(adaptive_queries, 6)

    def test_prime_word_weighted_adaptive_cost_reference_values(self):
        expected = {
            1: 0,
            2: 1,
            3: 2,
            4: 3,
            5: 4,
            8: 5,
            16: 7,
            32: 10,
            64: 11,
            100: 13,
        }
        for max_state, value in expected.items():
            self.assertEqual(adaptive_prime_word_cost_after_current(max_state), value)

    def test_prime_word_adaptive_cost_dominates_unit_query_depth(self):
        for max_state in range(1, 80):
            self.assertGreaterEqual(
                adaptive_prime_word_cost_after_current(max_state),
                adaptive_unit_query_depth_after_current(max_state),
            )
            if max_state > 1:
                first = adaptive_prime_word_best_first_threshold(max_state)
                self.assertIsNotNone(first)
                self.assertGreaterEqual(first, 2)
                self.assertLessEqual(first, max_state)

    def test_signatures_are_monotone_threshold_vectors(self):
        thresholds = (1, 3, 5, 8)
        signatures = [static_threshold_signature(q, thresholds) for q in range(10)]
        for left, right in zip(signatures, signatures[1:]):
            self.assertTrue(all(a <= b for a, b in zip(left, right)))

    def test_validation(self):
        with self.assertRaises(ValueError):
            threshold_bit(-1, 1)
        with self.assertRaises(ValueError):
            threshold_bit(1, 0)
        with self.assertRaises(ValueError):
            adaptive_unit_query_depth_after_current(-1)
        with self.assertRaises(ValueError):
            adaptive_prime_word_cost_after_current(-1)


if __name__ == "__main__":
    unittest.main()
