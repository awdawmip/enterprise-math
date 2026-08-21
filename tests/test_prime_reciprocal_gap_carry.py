import unittest

from enterprise_math.legendre import interior_hit_count, primes_up_to
from enterprise_math.prime_collapse_field import factor_horizon, interior_width
from enterprise_math.prime_horizon_gap import next_prime_after
from enterprise_math.prime_reciprocal_gap_carry import (
    reciprocal_boundary_prime,
    reciprocal_endpoint_state,
    reciprocal_integer_depth,
    reciprocal_jump_carry,
    reciprocal_prime_lag_budget,
    reciprocal_real_gap_threshold,
    reciprocal_three_layer_carry,
    reciprocal_threshold,
    reciprocal_threshold_ladder,
)


class PrimeReciprocalGapCarryTests(unittest.TestCase):
    def test_integer_depth_matches_literal_reciprocal_window(self):
        primes = primes_up_to(400)
        comparisons = 0
        for power in range(3, 7):
            for k in range(2, 24):
                horizon = factor_horizon(k, power)
                lower = k**power
                next_power = (k + 1) ** power
                for a, b in zip(primes, primes[1:]):
                    if a <= horizon:
                        continue
                    if a > lower:
                        break
                    depth = reciprocal_integer_depth(k, power, a, b)
                    m = lower // a
                    compiled = tuple(m - j for j in range(depth + 1)) if depth >= 0 else ()
                    literal = tuple(q for q in range(m, 0, -1) if b * q >= next_power)
                    self.assertEqual(compiled, literal)
                    comparisons += 1
        self.assertGreater(comparisons, 0)

    def test_jump_is_basin_hit_count_and_three_layer_carry_is_exact(self):
        comparisons = 0
        for power in range(3, 7):
            for k in range(2, 30):
                horizon = factor_horizon(k, power)
                for a in primes_up_to(min(k**power, 500)):
                    if a <= horizon or k**power // a < 1:
                        continue
                    m, _, jump, _ = reciprocal_endpoint_state(k, power, a)
                    self.assertGreater(m, 0)
                    self.assertEqual(jump, interior_hit_count(k, a, power))
                    jump2, carry2, threshold = reciprocal_jump_carry(k, power, a)
                    self.assertEqual(jump2, jump)
                    self.assertEqual(threshold, reciprocal_threshold(k, power, a, 0))
                    coarse, basin_bit, carry3, threshold3 = reciprocal_three_layer_carry(
                        k, power, a
                    )
                    self.assertEqual(coarse, interior_width(k, power) // a)
                    self.assertIn(basin_bit, (0, 1))
                    self.assertEqual(coarse + basin_bit, jump)
                    self.assertEqual(carry3, carry2)
                    self.assertEqual(threshold3, threshold)
                    comparisons += 1
        self.assertGreater(comparisons, 0)

    def test_unit_cost_ladder_is_dimension_independent(self):
        comparisons = 0
        for power in range(3, 8):
            for k in range(2, 25):
                horizon = factor_horizon(k, power)
                for a in primes_up_to(min(k**power, 400)):
                    if a <= horizon:
                        continue
                    m = k**power // a
                    if m < 3:
                        continue
                    ladder = reciprocal_threshold_ladder(k, power, a, min(7, m - 1))
                    for left, right in zip(ladder, ladder[1:]):
                        self.assertGreaterEqual(right, left + 1)
                        comparisons += 1
        self.assertGreater(comparisons, 0)

    def test_boundary_prime_compression_matches_literal_prime_slice(self):
        primes = primes_up_to(500)
        comparisons = 0
        for power in range(3, 6):
            for k in range(2, 20):
                horizon = factor_horizon(k, power)
                next_power = (k + 1) ** power
                for a, b in zip(primes, primes[1:]):
                    if a <= horizon:
                        continue
                    if a > k**power:
                        break
                    m = k**power // a
                    literal = tuple(q for q in primes_up_to(m) if b * q >= next_power)
                    boundary = reciprocal_boundary_prime(k, power, a, b)
                    self.assertEqual(boundary, literal[-1] if literal else None)
                    if m >= 2:
                        q, lag, slack, q_threshold = reciprocal_prime_lag_budget(
                            k, power, a, b
                        )
                        if boundary is not None:
                            self.assertEqual(q, boundary)
                            self.assertLessEqual(lag, slack)
                            self.assertLessEqual(q_threshold, b - a)
                    comparisons += 1
        self.assertGreater(comparisons, 0)

    def test_real_gap_threshold_is_exact_integerization_of_positive_width(self):
        comparisons = 0
        for power in range(3, 7):
            for k in range(2, 20):
                horizon = factor_horizon(k, power)
                for a in primes_up_to(min(k**power, 400)):
                    if a <= horizon:
                        continue
                    threshold = reciprocal_real_gap_threshold(k, power, a)
                    width = interior_width(k, power)
                    self.assertGreater(threshold * k**power, a * width)
                    if threshold > 0:
                        self.assertLessEqual((threshold - 1) * k**power, a * width)
                    comparisons += 1
        self.assertGreater(comparisons, 0)

    def test_cubic_reference_and_next_prime_gap_are_preserved(self):
        a, b, k = 1327, 1361, 119
        self.assertEqual(next_prime_after(a), b)
        self.assertEqual(reciprocal_real_gap_threshold(k, 3, a), 34)
        self.assertEqual(reciprocal_threshold(k, 3, a, 0), 35)
        self.assertEqual(reciprocal_integer_depth(k, 3, a, b), -1)


if __name__ == "__main__":
    unittest.main()
