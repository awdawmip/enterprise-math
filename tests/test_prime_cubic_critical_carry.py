import unittest

from enterprise_math.legendre import interior_hit_count, primes_up_to
from enterprise_math.prime_collapse_field import factor_horizon
from enterprise_math.prime_cubic_critical_carry import (
    cubic_lower_boundary_prime,
    cubic_lower_full_nonforced_candidate,
    cubic_prime_lag_budget,
    cubic_real_gap_threshold,
    cubic_reciprocal_endpoint_state,
    cubic_reciprocal_integer_depth,
    cubic_reciprocal_jump_carry,
    cubic_reciprocal_three_layer_carry,
    cubic_reciprocal_threshold,
    cubic_reciprocal_threshold_ladder,
)
from enterprise_math.prime_horizon_gap import next_prime_after


class PrimeCubicCriticalCarryTests(unittest.TestCase):
    def test_integer_window_depth_matches_literal_interval(self):
        primes = primes_up_to(500)
        comparisons = 0
        for k in range(3, 35):
            horizon = factor_horizon(k, 3)
            lower = k**3
            next_cube = (k + 1) ** 3
            for a, b in zip(primes, primes[1:]):
                if a <= horizon:
                    continue
                if a > lower:
                    break
                depth = cubic_reciprocal_integer_depth(a, b, k)
                m = lower // a
                compiled = tuple(m - j for j in range(depth + 1)) if depth >= 0 else ()
                literal = tuple(
                    q
                    for q in range(1, m + 1)
                    if b * q >= next_cube
                )
                self.assertEqual(compiled, tuple(reversed(literal)))
                comparisons += 1
        self.assertGreater(comparisons, 0)

    def test_depth_threshold_is_exact_for_each_terminal_coordinate(self):
        for a in primes_up_to(300):
            if a < 5:
                continue
            for k in range(3, 30):
                if factor_horizon(k, 3) >= a or k**3 // a < 1:
                    continue
                m = k**3 // a
                for depth in range(min(6, m)):
                    q = m - depth
                    threshold = cubic_reciprocal_threshold(a, k, depth)
                    self.assertGreaterEqual((a + threshold) * q, (k + 1) ** 3)
                    if threshold > 0:
                        self.assertLess((a + threshold - 1) * q, (k + 1) ** 3)

    def test_jump_is_existing_cubic_hit_count_plus_second_carry(self):
        comparisons = 0
        for a in primes_up_to(500):
            if a < 5:
                continue
            for k in range(3, 40):
                if factor_horizon(k, 3) >= a or k**3 // a < 1:
                    continue
                m, _, jump, _ = cubic_reciprocal_endpoint_state(a, k)
                self.assertGreater(m, 0)
                self.assertEqual(jump, interior_hit_count(k, a, 3))
                jump2, reciprocal_carry, threshold = cubic_reciprocal_jump_carry(a, k)
                self.assertEqual(jump2, jump)
                self.assertEqual(threshold, cubic_reciprocal_threshold(a, k, 0))
                coarse, basin_bit, carry2, threshold2 = cubic_reciprocal_three_layer_carry(a, k)
                self.assertEqual(coarse + basin_bit, jump)
                self.assertIn(basin_bit, (0, 1))
                self.assertEqual(carry2, reciprocal_carry)
                self.assertEqual(threshold2, threshold)
                comparisons += 1
        self.assertGreater(comparisons, 0)

    def test_threshold_ladder_has_unit_cost_per_left_lag(self):
        comparisons = 0
        for a in primes_up_to(400):
            if a < 5:
                continue
            for k in range(3, 35):
                if factor_horizon(k, 3) >= a:
                    continue
                m = k**3 // a
                if m < 3:
                    continue
                ladder = cubic_reciprocal_threshold_ladder(a, k, min(8, m - 1))
                for left, right in zip(ladder, ladder[1:]):
                    self.assertGreaterEqual(right, left + 1)
                    comparisons += 1
        self.assertGreater(comparisons, 0)

    def test_boundary_prime_compression_matches_literal_prime_occupancy(self):
        primes = primes_up_to(500)
        comparisons = 0
        for k in range(3, 35):
            horizon = factor_horizon(k, 3)
            for a, b in zip(primes, primes[1:]):
                if a <= horizon:
                    continue
                if a > k**3:
                    break
                m = k**3 // a
                lo = -(-((k + 1) ** 3) // b)
                literal = tuple(q for q in primes_up_to(m) if q >= lo)
                boundary = cubic_lower_boundary_prime(a, b, k)
                self.assertEqual(boundary, literal[-1] if literal else None)
                full = cubic_lower_full_nonforced_candidate(a, b, k)
                expected_full = literal[-1] if literal and literal[-1] > k else None
                self.assertEqual(full, expected_full)
                comparisons += 1
        self.assertGreater(comparisons, 0)

    def test_1327_gap_separates_real_and_integer_activation(self):
        a, b, k = 1327, 1361, 119
        self.assertEqual(next_prime_after(a), b)
        self.assertEqual(cubic_real_gap_threshold(a, k), 34)
        self.assertEqual(b - a, 34)
        self.assertEqual(cubic_reciprocal_threshold(a, k, 0), 35)
        self.assertEqual(cubic_reciprocal_integer_depth(a, b, k), -1)
        self.assertIsNone(cubic_lower_boundary_prime(a, b, k))
        self.assertEqual(cubic_reciprocal_jump_carry(a, k), (33, 2, 35))

    def test_integer_activation_threshold_has_carry_teeth(self):
        a = 239
        expected = (27, 26, 24, 24, 23, 22, 21, 22)
        actual = tuple(cubic_reciprocal_threshold(a, k, 0) for k in range(30, 38))
        self.assertEqual(actual, expected)
        self.assertEqual(factor_horizon(37, 3), 234)
        self.assertLess(factor_horizon(37, 3), a)

    def test_prime_lag_cannot_exceed_right_gap_slack(self):
        comparisons = 0
        primes = primes_up_to(1000)
        for k in range(3, 60):
            horizon = factor_horizon(k, 3)
            for a, b in zip(primes, primes[1:]):
                if a <= horizon:
                    continue
                if a > k**3:
                    break
                m = k**3 // a
                if m < 2:
                    continue
                q, lag, slack, q_threshold = cubic_prime_lag_budget(a, b, k)
                captured = b * q >= (k + 1) ** 3
                if captured:
                    self.assertGreaterEqual(slack, 0)
                    self.assertLessEqual(lag, slack)
                    self.assertLessEqual(q_threshold, b - a)
                comparisons += 1
        self.assertGreater(comparisons, 0)


if __name__ == "__main__":
    unittest.main()
