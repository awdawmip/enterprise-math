import unittest
from math import gcd

from enterprise_math.legendre import (
    anchor_face_sum,
    anchor_product,
    anchor_transfer,
    anchor_transfer_discrepancy,
    binary_carry_delta,
    binary_carry_event,
    binary_carry_square_interval_prime_count,
    carry_square_interval_prime_count,
    centered_square_carry,
    direct_square_interval_prime_count,
    euclidean_basin_descent,
    interior_hit_count,
    mobius_square_interval_prime_count,
    square_carry,
    square_hit_count_from_carry,
    verify_bounded_common_root_witness,
)


class LegendrePressureTests(unittest.TestCase):
    def test_euclidean_basin_descent(self):
        for power in range(2, 6):
            for k in range(0, 30):
                for d in range(1, 25):
                    coarse, local = euclidean_basin_descent(k, d, power)
                    self.assertEqual(
                        interior_hit_count(k, d, power),
                        coarse + local,
                    )

    def test_square_carry_is_ternary_and_centered(self):
        seen = set()
        for k in range(1, 100):
            for d in range(1, 100):
                carry = square_carry(k, d)
                self.assertIn(carry, (0, 1, 2))
                self.assertEqual(carry, centered_square_carry(k, d))
                self.assertEqual(
                    interior_hit_count(k, d, 2),
                    square_hit_count_from_carry(k, d),
                )
                seen.add(carry)
        self.assertEqual(seen, {0, 1, 2})

    def test_mobius_and_carry_prime_counts(self):
        for k in range(1, 21):
            direct = direct_square_interval_prime_count(k)
            self.assertEqual(mobius_square_interval_prime_count(k), direct)
            self.assertEqual(carry_square_interval_prime_count(k), direct)
            self.assertEqual(binary_carry_square_interval_prime_count(k), direct)

    def test_binary_pairing_sign_rule_and_explicit_event(self):
        for k in range(2, 150):
            for odd_d in range(1, 150, 2):
                delta = binary_carry_delta(k, odd_d)
                expected_nonzero = 1 if (k // odd_d) % 2 == 0 else -1
                self.assertIn(delta, (0, expected_nonzero))
                self.assertEqual(
                    delta,
                    expected_nonzero * binary_carry_event(k, odd_d),
                )

    def test_anchor_face_cancels(self):
        for k in range(2, 100):
            self.assertEqual(anchor_face_sum(k), 0)

    def test_anchor_transfer_is_centered_discrepancy(self):
        for k in range(2, 60):
            anchor = anchor_product(k)
            for b in range(1, 70):
                if gcd(b, anchor) == 1:
                    self.assertEqual(
                        anchor_transfer(k, b),
                        anchor_transfer_discrepancy(k, b),
                    )

    def test_large_transverse_transfer_localizes(self):
        for k in range(2, 60):
            anchor = anchor_product(k)
            upper = (k + 1) ** 2 - 1
            for b in range(k + 1, upper + 20):
                if gcd(b, anchor) != 1:
                    continue
                transfer = anchor_transfer_discrepancy(k, b)
                self.assertGreaterEqual(transfer, 0)
                if b > 2 * k:
                    self.assertIn(transfer, (0, 1))
                if b > upper:
                    self.assertEqual(transfer, 0)

    def test_overstrong_anchor_transfer_bound_has_counterexample(self):
        # k=456 has anchor primes {2,3,19}.  The tempting bound
        # |Lambda_b(k)| <= omega(A_k)=3 fails already at b=5.
        self.assertEqual(anchor_transfer(456, 5), -4)

    def test_unbounded_common_root_covering_witness(self):
        self.assertTrue(verify_bounded_common_root_witness())


if __name__ == "__main__":
    unittest.main()
