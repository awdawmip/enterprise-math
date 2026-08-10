import unittest

from enterprise_math.legendre import is_prime, primes_up_to
from enterprise_math.prime_collapse_field import (
    direct_power_interval_prime_count,
    factor_horizon,
)
from enterprise_math.prime_collapse_surplus import (
    mobius_survivor_count,
    post_horizon_prime_count,
    prime_degree_surplus,
    prime_surplus_power_interval_prime_count,
    square_gap_exclusive_certificate,
    square_gap_target,
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

    @staticmethod
    def _direct_singleton_support_certificate(q: int, offset: int) -> int | None:
        k = q + offset
        horizon = factor_horizon(k, 2)
        candidates = primes_up_to(horizon)
        for n in range(k * k + 1, (k + 1) * (k + 1)):
            support = tuple(r for r in candidates if n % r == 0)
            if support == (q,):
                return n
        return None

    def test_square_gap_certificate_is_exact_on_bounded_grid(self):
        for offset in range(0, 8):
            for q in primes_up_to(300):
                if q == 2 or q <= offset * offset + 2 * offset:
                    continue
                derived = square_gap_exclusive_certificate(q, offset)
                direct = self._direct_singleton_support_certificate(q, offset)
                self.assertEqual(derived is not None, direct is not None)
                self.assertEqual(
                    derived is not None,
                    is_prime(square_gap_target(q, offset)),
                )
                if derived is not None:
                    self.assertEqual(derived, q * square_gap_target(q, offset))

    def test_twin_prime_diagonal_specialization(self):
        for q in primes_up_to(500):
            if q == 2:
                continue
            certificate = square_gap_exclusive_certificate(q, 0)
            self.assertEqual(certificate is not None, is_prime(q + 2))
            if certificate is not None:
                self.assertEqual(certificate, q * (q + 2))


if __name__ == "__main__":
    unittest.main()
