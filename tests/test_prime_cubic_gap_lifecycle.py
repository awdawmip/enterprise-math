import unittest

from enterprise_math.legendre import primes_up_to
from enterprise_math.prime_collapse_field import factor_horizon
from enterprise_math.prime_cubic_gap_lifecycle import (
    HORIZON_INSIDE,
    PRE_HORIZON,
    RETIRED,
    cubic_first_horizon_at_least,
    cubic_gap_full_nonforced_witness,
    cubic_gap_max_captured_prime,
    cubic_gap_phase,
    cubic_horizon_crossing_interval,
    cubic_last_pre_horizon_k,
    cubic_pre_gap_activation_interval,
    cubic_pre_gap_activation_margin,
    cubic_pre_gap_critical_length,
    cubic_reciprocal_candidate_interval,
)


class PrimeCubicGapLifecycleTests(unittest.TestCase):
    def test_horizon_inverse_and_phase_are_exact(self):
        for t in range(2, 300):
            k = cubic_first_horizon_at_least(t)
            self.assertGreaterEqual(factor_horizon(k, 3), t)
            if k > 0:
                self.assertLess(factor_horizon(k - 1, 3), t)

        for a, b in [(113, 127), (1327, 1361)]:
            first, last = cubic_horizon_crossing_interval(a, b)
            for k in range(max(1, first - 3), last + 4):
                horizon = factor_horizon(k, 3)
                phase = cubic_gap_phase(k, a, b)
                expected = (
                    PRE_HORIZON
                    if horizon < a
                    else HORIZON_INSIDE
                    if horizon < b
                    else RETIRED
                )
                self.assertEqual(phase, expected)

    def test_1327_1361_is_exact_critical_prototype(self):
        a, b = 1327, 1361
        self.assertEqual(cubic_last_pre_horizon_k(a), 119)
        self.assertEqual(cubic_pre_gap_critical_length(a), 34)
        self.assertEqual(b - a, 34)
        self.assertEqual(cubic_pre_gap_activation_interval(a, b), (119, 119))
        self.assertGreater(cubic_pre_gap_activation_margin(119, a, b), 0)
        self.assertLessEqual(cubic_pre_gap_activation_margin(118, a, b), 0)
        self.assertEqual(cubic_horizon_crossing_interval(a, b), (120, 121))

        # The real reciprocal interval is positive at k=119, but contains no
        # integer at all, so this pre-horizon phase has no captured prime q.
        self.assertEqual(cubic_reciprocal_candidate_interval(119, a, b), (1270, 1269))
        self.assertIsNone(cubic_gap_max_captured_prime(119, a, b))
        self.assertIsNone(cubic_gap_full_nonforced_witness(119, a, b))

        # The same fixed gap is then swept by the factor horizon.
        self.assertEqual(factor_horizon(119, 3), 1314)
        self.assertEqual(factor_horizon(120, 3), 1330)
        self.assertEqual(factor_horizon(121, 3), 1347)
        self.assertEqual(factor_horizon(122, 3), 1364)

    def test_113_127_has_no_pre_activation_but_has_horizon_phase(self):
        a, b = 113, 127
        self.assertEqual(cubic_last_pre_horizon_k(a), 22)
        self.assertEqual(cubic_pre_gap_critical_length(a), 17)
        self.assertEqual(b - a, 14)
        self.assertIsNone(cubic_pre_gap_activation_interval(a, b))
        self.assertEqual(cubic_horizon_crossing_interval(a, b), (23, 24))

    def test_reciprocal_integer_compiler_matches_literal_q_conditions(self):
        # Exhaustively compare the exact reciprocal slice with the literal
        # inequalities for small cubic PRE_HORIZON configurations.
        primes = primes_up_to(400)
        comparisons = 0
        for k in range(3, 35):
            lower = k**3
            upper = (k + 1) ** 3 - 1
            horizon = factor_horizon(k, 3)
            for a, b in zip(primes, primes[1:]):
                if a <= horizon:
                    continue
                if a > lower:
                    break
                lo, hi = cubic_reciprocal_candidate_interval(k, a, b)
                compiled = tuple(q for q in primes_up_to(horizon) if lo <= q <= hi)
                literal = tuple(
                    q
                    for q in primes_up_to(horizon)
                    if q * horizon <= lower
                    and a * q < lower
                    and lower < b * q
                    and b * q > upper
                )
                self.assertEqual(compiled, literal)
                comparisons += 1
        self.assertGreater(comparisons, 0)

    def test_only_1327_gap_reaches_pre_activation_threshold_below_5000(self):
        primes = primes_up_to(5000)
        hits = []
        for a, b in zip(primes, primes[1:]):
            try:
                critical = cubic_pre_gap_critical_length(a)
            except ValueError:
                continue
            if b - a >= critical:
                hits.append((a, b, b - a, critical))
        self.assertEqual(hits, [(1327, 1361, 34, 34)])


if __name__ == "__main__":
    unittest.main()
