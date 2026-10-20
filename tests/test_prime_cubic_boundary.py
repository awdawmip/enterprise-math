import unittest

from enterprise_math.prime_cubic_boundary import (
    cubic_boundary_gap_state,
    cubic_boundary_margin_identity,
    cubic_boundary_primes,
    cubic_pure_cap_max_nonforced_candidate,
    previous_prime_at_most,
)
from enterprise_math.prime_horizon_gap import (
    cubic_pure_cap_nonforced_interval,
    pure_cofactor_cap_nonforced_candidates,
)


class PrimeCubicBoundaryTests(unittest.TestCase):
    def test_previous_prime_at_most(self):
        self.assertEqual(previous_prime_at_most(2), 2)
        self.assertEqual(previous_prime_at_most(3), 3)
        self.assertEqual(previous_prime_at_most(4), 3)
        self.assertEqual(previous_prime_at_most(110), 109)

    def test_selected_cubic_boundary_pairs(self):
        expected = {
            23: (109, 127),
            64: (509, 541),
            120: (1307, 1361),
            138: (1621, 1657),
            1005: (31859, 31957),
        }
        for k, pair in expected.items():
            self.assertEqual(cubic_boundary_primes(k), pair)

    def test_canonical_max_obstruction_matches_prime_slice(self):
        comparisons = 0
        for k in range(3, 2000):
            candidates = pure_cofactor_cap_nonforced_candidates(k, 3)
            expected = candidates[-1] if candidates else None
            self.assertEqual(
                cubic_pure_cap_max_nonforced_candidate(k),
                expected,
            )
            comparisons += 1
        self.assertEqual(comparisons, 1997)

    def test_existence_needs_only_top_prime_in_slice(self):
        for k in range(3, 2000):
            lower_q, upper_q = cubic_pure_cap_nonforced_interval(k)
            top_prime = previous_prime_at_most(upper_q)
            expected = top_prime if top_prime >= lower_q else None
            self.assertEqual(
                cubic_pure_cap_max_nonforced_candidate(k),
                expected,
            )

    def test_gap_margin_identity(self):
        for k in range(3, 2000):
            left_lag, right_gap, horizon_margin, overshoot_margin = (
                cubic_boundary_gap_state(k)
            )
            identity_horizon, identity_overshoot = cubic_boundary_margin_identity(k)
            self.assertGreaterEqual(left_lag, 0)
            self.assertGreater(right_gap, 0)
            self.assertEqual(horizon_margin, identity_horizon)
            self.assertEqual(overshoot_margin, identity_overshoot)
            self.assertEqual(
                cubic_pure_cap_max_nonforced_candidate(k) is not None,
                horizon_margin > 0 and overshoot_margin > 0,
            )


if __name__ == "__main__":
    unittest.main()
