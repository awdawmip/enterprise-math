import unittest
from math import isqrt

from enterprise_math.legendre import is_prime, primes_up_to
from enterprise_math.prime_collapse_field import factor_horizon, interior_width
from enterprise_math.prime_horizon_gap import (
    COFACTOR_GAP,
    HORIZON_GAP,
    cubic_pure_cap_nonforced_interval,
    exclusive_cofactor_certificate,
    exclusive_cofactor_regime,
    first_exclusive_cofactor_prime,
    horizon_drift_components,
    horizon_gap_threshold,
    horizon_successor_exceeds_threshold,
    is_pure_cofactor_cap_candidate,
    next_prime_after,
    pure_cofactor_cap_certificate,
    pure_cofactor_cap_nonforced_candidates,
    pure_cofactor_cap_nonforced_interval,
)


class PrimeHorizonGapTests(unittest.TestCase):
    @staticmethod
    def _direct_e1_exists(k: int, power: int, q: int) -> bool:
        lower = k**power
        upper = (k + 1) ** power - 1
        horizon = factor_horizon(k, power)
        for r in range(horizon + 1, upper // q + 1):
            if is_prime(r) and lower < q * r <= upper:
                return True
        return False

    @staticmethod
    def _direct_singleton_support_exists(k: int, power: int, q: int) -> bool:
        lower = k**power
        upper = (k + 1) ** power - 1
        horizon = factor_horizon(k, power)
        candidates = primes_up_to(horizon)
        first_multiple = (lower // q + 1) * q
        for n in range(first_multiple, upper + 1, q):
            support = tuple(r for r in candidates if n % r == 0)
            if support == (q,):
                return True
        return False

    def test_global_e1_criterion_matches_direct_search(self):
        comparisons = 0
        for power in range(2, 5):
            for k in range(2, 16):
                horizon = factor_horizon(k, power)
                for q in primes_up_to(horizon):
                    derived = exclusive_cofactor_certificate(k, power, q)
                    self.assertEqual(
                        derived is not None,
                        self._direct_e1_exists(k, power, q),
                    )
                    if derived is not None:
                        r = derived // q
                        self.assertTrue(is_prime(r))
                        self.assertGreater(r, horizon)
                        self.assertGreater(derived, k**power)
                        self.assertLessEqual(derived, (k + 1) ** power - 1)
                    comparisons += 1
        self.assertEqual(comparisons, 554)

    def test_cubic_k23_exposes_horizon_gap_scope_boundary(self):
        k = 23
        q = 109
        power = 3
        lower = k**power
        upper = (k + 1) ** power - 1
        horizon = factor_horizon(k, power)

        self.assertEqual((lower, upper, horizon), (12167, 13823, 117))
        self.assertEqual(exclusive_cofactor_regime(k, power, q), HORIZON_GAP)

        # The next prime after A/q is still a candidate divisor, so q*113 is
        # not singleton support even though it lies in the cubic basin.
        self.assertEqual(lower // q, 111)
        self.assertEqual(next_prime_after(lower // q), 113)
        self.assertLessEqual(113, horizon)
        self.assertTrue(lower < q * 113 <= upper)

        # The first eligible exclusive cofactor is 127, but it overshoots U.
        self.assertEqual(first_exclusive_cofactor_prime(k, power, q), 127)
        self.assertGreater(q * 127, upper)
        self.assertIsNone(exclusive_cofactor_certificate(k, power, q))
        self.assertTrue(is_pure_cofactor_cap_candidate(k, power, q))
        self.assertIsNone(pure_cofactor_cap_certificate(k, power, q))
        self.assertEqual(pure_cofactor_cap_nonforced_interval(k, power), (109, 110))

    def test_both_exclusive_cofactor_regimes_occur(self):
        self.assertEqual(exclusive_cofactor_regime(23, 3, 2), COFACTOR_GAP)
        self.assertEqual(exclusive_cofactor_regime(23, 3, 109), HORIZON_GAP)

    def test_selected_cubic_nonforced_pure_cap_examples(self):
        expected = {
            23: ((109, 110), (109,)),
            64: ((508, 512), (509,)),
            120: ((1302, 1314), (1303, 1307)),
            138: ((1621, 1621), (1621,)),
            1005: ((31859, 31860), (31859,)),
        }
        for k, (interval, candidates) in expected.items():
            self.assertEqual(pure_cofactor_cap_nonforced_interval(k, 3), interval)
            self.assertEqual(cubic_pure_cap_nonforced_interval(k), interval)
            self.assertEqual(pure_cofactor_cap_nonforced_candidates(k, 3), candidates)

    def test_cubic_cap_four_cutoffs_collapse_to_two(self):
        for k in range(3, 1000):
            generic = pure_cofactor_cap_nonforced_interval(k, 3)
            collapsed = cubic_pure_cap_nonforced_interval(k)
            self.assertEqual(generic, collapsed)

            lower = k**3
            upper = (k + 1) ** 3 - 1
            horizon = factor_horizon(k, 3)
            self.assertLess(horizon, k * k)

            # Any integer q in the horizon-gap / lower-root band already has
            # the two higher-power exclusions required by the pure cap.
            lower_q, upper_q = collapsed
            for q in (lower_q, upper_q):
                if q <= upper_q and q * horizon > lower:
                    self.assertGreaterEqual(q, k + 1)
                    self.assertGreater(q**3, upper)
                    self.assertGreater(q * q * (horizon + 1), upper)

    def test_prime_slice_compiler_matches_predicate_definition(self):
        comparisons = 0
        for power in range(2, 6):
            for k in range(2, 120):
                lower_q, upper_q = pure_cofactor_cap_nonforced_interval(k, power)
                compiled = (
                    tuple(q for q in primes_up_to(upper_q) if q >= lower_q)
                    if lower_q <= upper_q
                    else ()
                )
                literal = []
                horizon = factor_horizon(k, power)
                for q in primes_up_to(min(horizon, isqrt(k**power))):
                    if (
                        is_pure_cofactor_cap_candidate(k, power, q)
                        and pure_cofactor_cap_certificate(k, power, q) is None
                    ):
                        literal.append(q)
                self.assertEqual(compiled, tuple(literal))
                self.assertEqual(
                    pure_cofactor_cap_nonforced_candidates(k, power),
                    tuple(literal),
                )
                comparisons += 1
        self.assertEqual(comparisons, 472)

    def test_horizon_gap_decomposes_into_drift_and_square_remainder(self):
        for power in range(2, 10):
            for k in range(2, 80):
                drift, remainder, root_lower = horizon_drift_components(k, power)
                horizon = factor_horizon(k, power)
                upper = (k + 1) ** power - 1
                numerator, denominator = horizon_gap_threshold(k, power)

                self.assertEqual(denominator, root_lower)
                self.assertEqual(horizon, root_lower + drift)
                self.assertEqual(upper, horizon * horizon + remainder)
                self.assertGreaterEqual(remainder, 0)
                self.assertLessEqual(remainder, 2 * horizon)
                self.assertEqual(
                    numerator,
                    drift * root_lower + drift * drift + remainder,
                )

                if power % 2 == 0:
                    half_power = power // 2
                    self.assertEqual(drift, interior_width(k, half_power))
                    self.assertEqual(remainder, 2 * horizon)

    def test_square_pure_horizon_cap_is_empty(self):
        for k in range(2, 100):
            horizon = factor_horizon(k, 2)
            self.assertEqual(horizon, k)
            lower_q, upper_q = pure_cofactor_cap_nonforced_interval(k, 2)
            self.assertGreater(lower_q, upper_q)
            for q in primes_up_to(horizon):
                self.assertFalse(is_pure_cofactor_cap_candidate(k, 2, q))

    def test_quartic_gap_threshold_and_legendre_localization(self):
        for k in range(2, 100):
            numerator, denominator = horizon_gap_threshold(k, 4)
            self.assertEqual(denominator, k * k)
            self.assertEqual(
                numerator,
                2 * k**3 + 6 * k**2 + 4 * k,
            )

            upper = (k + 1) ** 4 - 1
            self.assertEqual(
                upper - k * k * (k + 2) ** 2,
                2 * k * (k + 2),
            )

            # If the horizon successor crossed the cap threshold, then it
            # would lie strictly above (k+2)^2.  Since the quartic horizon is
            # (k+1)^2-1, that would give a prime-free consecutive-square gap.
            if horizon_successor_exceeds_threshold(k, 4):
                successor = next_prime_after(factor_horizon(k, 4))
                self.assertGreater(successor, (k + 2) ** 2)

    def test_pure_cap_criterion_matches_direct_singleton_search_small_grid(self):
        comparisons = 0
        for power in (3, 4):
            for k in range(3, 45):
                lower = k**power
                horizon = factor_horizon(k, power)
                for q in primes_up_to(min(horizon, isqrt(lower))):
                    if not is_pure_cofactor_cap_candidate(k, power, q):
                        continue
                    self.assertEqual(
                        pure_cofactor_cap_certificate(k, power, q) is not None,
                        self._direct_singleton_support_exists(k, power, q),
                    )
                    comparisons += 1
        self.assertEqual(comparisons, 325)


if __name__ == "__main__":
    unittest.main()
