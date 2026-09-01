import unittest

from enterprise_math.prime_collapse_field import (
    direct_power_interval_prime_count,
    factor_horizon,
)
from enterprise_math.prime_collapse_surplus import (
    mobius_survivor_count,
    post_horizon_prime_count,
    prime_degree_surplus,
    prime_degree_surplus_terms,
    prime_surplus_power_interval_prime_count,
    subsquare_survivor_count,
)


class PrimeCollapseSurplusTests(unittest.TestCase):
    def test_subsquare_survivors_are_one_plus_post_horizon_primes(self):
        for horizon in range(2, 16):
            for limit in range(1, (horizon + 1) ** 2):
                self.assertEqual(
                    mobius_survivor_count(limit, horizon),
                    subsquare_survivor_count(limit, horizon),
                )
                self.assertEqual(
                    subsquare_survivor_count(limit, horizon),
                    1 + post_horizon_prime_count(horizon, limit),
                )

    def test_every_basin_width_degree_is_in_subsquare_range(self):
        for power in range(2, 9):
            for k in range(2, 40):
                horizon = factor_horizon(k, power)
                for degree in range(1, power):
                    self.assertLess(k**degree, (horizon + 1) ** 2)

    def test_prime_surplus_decomposition_matches_direct_count(self):
        cases = [
            (2, 2), (3, 2), (4, 2),
            (2, 3), (3, 3), (4, 3), (5, 3),
            (2, 4), (3, 4), (4, 4), (5, 4),
            (2, 5),
        ]
        for k, power in cases:
            self.assertEqual(
                prime_surplus_power_interval_prime_count(k, power),
                direct_power_interval_prime_count(k, power),
            )

    def test_square_has_no_post_horizon_degree_surplus(self):
        for k in range(2, 100):
            self.assertEqual(prime_degree_surplus(k, 2), 0)

    def test_first_nontrivial_surplus_terms(self):
        self.assertEqual(
            prime_degree_surplus_terms(4, 3),
            ((1, 3, 0), (2, 3, 1)),
        )
        self.assertEqual(prime_degree_surplus(4, 3), 3)

        terms_p4 = prime_degree_surplus_terms(3, 4)
        self.assertEqual(terms_p4[:2], ((1, 4, 0), (2, 6, 0)))
        self.assertEqual(terms_p4[2], (3, 4, 3))
        self.assertEqual(prime_degree_surplus(3, 4), 12)


if __name__ == "__main__":
    unittest.main()
