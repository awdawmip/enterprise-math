from functools import lru_cache
import unittest

from enterprise_math.core import integer_nth_root
from enterprise_math.p023_p024_adaptive_threshold_precision import (
    adaptive_prime_word_best_first_threshold,
    adaptive_prime_word_cost_after_current,
    adaptive_unit_query_depth_after_current,
    adaptive_unit_query_depth_dp_after_current,
    destructive_first_nonidentity_merge_pair,
    destructive_single_trajectory_exact_depth,
    destructive_single_trajectory_identifiable,
    minimal_static_future_thresholds_after_current,
    static_threshold_signature,
    static_thresholds_separate_domain,
    threshold_bit,
)


def literal_destructive_can_identify(
    max_state: int, root_exp: int, max_depth: int
) -> bool:
    """Independent small-domain adaptive oracle on one mutating trajectory."""

    @lru_cache(maxsize=None)
    def solve(states: tuple[int, ...], depth: int) -> bool:
        if len(states) <= 1:
            return True
        if len(set(states)) < len(states):
            return False
        if depth == 0:
            return False

        # Denominators above max_state send every surviving candidate to zero,
        # so 1..max_state+1 is already exhaustive for this bounded oracle.
        for action in range(1, max_state + 2):
            groups: dict[int, list[int]] = {}
            for state in states:
                next_state = state // action
                observed = integer_nth_root(next_state, root_exp)
                groups.setdefault(observed, []).append(next_state)
            if all(solve(tuple(group), depth - 1) for group in groups.values()):
                return True
        return False

    # The free current root observation has already isolated state zero.
    return solve(tuple(range(1, max_state + 1)), max_depth)


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

    def test_reset_oracle_adaptive_unit_depth_matches_information_bound(self):
        for max_state in range(0, 100):
            closed = adaptive_unit_query_depth_after_current(max_state)
            exact_dp = adaptive_unit_query_depth_dp_after_current(max_state)
            self.assertEqual(closed, exact_dp)
            expected = 0 if max_state <= 1 else (max_state - 1).bit_length()
            self.assertEqual(closed, expected)

    def test_static_vs_reset_oracle_adaptive_gap_is_large(self):
        max_state = 64
        static_future_queries = len(
            minimal_static_future_thresholds_after_current(max_state)
        )
        reset_queries = adaptive_unit_query_depth_after_current(max_state)
        self.assertEqual(static_future_queries, 63)
        self.assertEqual(reset_queries, 6)

    def test_prime_word_weighted_reset_oracle_cost_reference_values(self):
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

    def test_prime_word_reset_cost_dominates_unit_query_depth(self):
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

    def test_destructive_first_nonidentity_action_forces_exact_merge(self):
        for max_state in range(3, 20):
            for action in range(2, max_state + 3):
                pair = destructive_first_nonidentity_merge_pair(max_state, action)
                self.assertIsNotNone(pair)
                left, right = pair
                self.assertNotEqual(left, right)
                self.assertEqual(left // action, right // action)

    def test_destructive_single_trajectory_has_sharp_impossibility_boundary(self):
        for root_exp in range(1, 8):
            for max_state in range(0, min(8, 2**root_exp)):
                closed = destructive_single_trajectory_exact_depth(
                    max_state, root_exp
                )
                expected = 0 if max_state <= 1 else 1 if max_state == 2 else None
                self.assertEqual(closed, expected)
                self.assertEqual(
                    destructive_single_trajectory_identifiable(max_state, root_exp),
                    expected is not None,
                )

                for depth in range(0, 5):
                    literal = literal_destructive_can_identify(
                        max_state, root_exp, depth
                    )
                    predicted = expected is not None and depth >= expected
                    self.assertEqual(literal, predicted)

    def test_reset_oracle_and_destructive_execution_are_not_same_resource(self):
        max_state = 64
        root_exp = 7
        self.assertLess(max_state, 2**root_exp)
        self.assertEqual(adaptive_unit_query_depth_after_current(max_state), 6)
        self.assertIsNone(
            destructive_single_trajectory_exact_depth(max_state, root_exp)
        )

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
        with self.assertRaises(ValueError):
            destructive_single_trajectory_exact_depth(4, 2)
        with self.assertRaises(ValueError):
            destructive_first_nonidentity_merge_pair(4, 0)


if __name__ == "__main__":
    unittest.main()
