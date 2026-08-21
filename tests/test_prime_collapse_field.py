import unittest

from enterprise_math.legendre import interior_hit_count, square_carry
from enterprise_math.prime_collapse_field import (
    direct_power_interval_prime_count,
    even_power_horizon_closed_form,
    factor_horizon,
    forced_visibility_degree,
    interior_width,
    interior_width_carry,
    mobius_power_interval_prime_count,
    polynomial_carry,
    polynomial_hit_baseline,
)


class PrimeCollapseFieldTests(unittest.TestCase):
    def test_even_factor_horizon_closed_form(self):
        for power in range(2, 10, 2):
            for k in range(0, 80):
                self.assertEqual(
                    factor_horizon(k, power),
                    even_power_horizon_closed_form(k, power),
                )

    def test_square_is_the_unique_exact_coordinate_alignment_on_grid(self):
        for k in range(1, 100):
            self.assertEqual(factor_horizon(k, 2), k)
            for power in range(3, 9):
                self.assertGreater(factor_horizon(k, power), k)

    def test_width_carry_is_one_bit_and_exact(self):
        for power in range(2, 9):
            for k in range(0, 50):
                for d in range(1, 60):
                    carry = interior_width_carry(k, d, power)
                    self.assertIn(carry, (0, 1))
                    self.assertEqual(
                        interior_hit_count(k, d, power),
                        interior_width(k, power) // d + carry,
                    )

    def test_polynomial_carry_is_exact_residue_local_and_bounded(self):
        for power in range(2, 9):
            for k in range(0, 50):
                for d in range(1, 60):
                    carry = polynomial_carry(k, d, power)
                    self.assertEqual(
                        interior_hit_count(k, d, power),
                        polynomial_hit_baseline(k, d, power) + carry,
                    )
                    self.assertEqual(carry, polynomial_carry(k % d, d, power))
                    self.assertGreaterEqual(carry, 0)
                    self.assertLessEqual(carry, 2**power - 2)

    def test_power_two_recovers_existing_square_carry(self):
        for k in range(0, 100):
            for d in range(1, 100):
                self.assertEqual(polynomial_carry(k, d, 2), square_carry(k, d))

    def test_forced_visibility_degree(self):
        for power in range(2, 9):
            degree = forced_visibility_degree(power)
            for k in range(1, 80):
                horizon = factor_horizon(k, power)
                for j in range(1, degree + 1):
                    self.assertLessEqual(k**j, horizon)

    def test_mobius_prime_count_matches_direct_on_small_basins(self):
        cases = [
            (1, 2), (2, 2), (3, 2), (4, 2),
            (1, 3), (2, 3), (3, 3),
            (1, 4), (2, 4),
            (1, 5), (2, 5),
        ]
        for k, power in cases:
            self.assertEqual(
                mobius_power_interval_prime_count(k, power),
                direct_power_interval_prime_count(k, power),
            )


if __name__ == "__main__":
    unittest.main()
