from __future__ import annotations

import unittest

from enterprise_math.brc_count_centered_carry import mobius
from enterprise_math.brc_prime_cutoff_factorization import (
    cutoff_divisor_lift_convolution,
    cutoff_log_connection_valuations,
    cutoff_mobius_convolution,
    expected_cutoff_lambda_valuations,
    prime_cutoff_certificate,
    prime_cutoff_parts,
    rough_linear_on_block,
    rough_mobius,
    rough_mobius_degree,
)


class BRCPrimeCutoffFactorizationTests(unittest.TestCase):
    def test_unique_prime_cutoff_parts(self) -> None:
        self.assertEqual(prime_cutoff_parts(2**3 * 3 * 5**2 * 11, 5), (2**3 * 3 * 5**2, 11))
        self.assertEqual(prime_cutoff_parts(77, 5), (1, 77))

    def test_exact_recoalescence_and_log_connections(self) -> None:
        for cutoff in (2, 3, 5, 7, 11):
            for n in range(1, 193):
                self.assertEqual(cutoff_mobius_convolution(n, cutoff), mobius(n))
                self.assertEqual(cutoff_divisor_lift_convolution(n, cutoff), 1)
                self.assertEqual(
                    cutoff_log_connection_valuations(n, cutoff),
                    expected_cutoff_lambda_valuations(n, cutoff),
                )
                self.assertEqual(
                    cutoff_log_connection_valuations(n, cutoff, rough=True),
                    expected_cutoff_lambda_valuations(n, cutoff, rough=True),
                )
                self.assertTrue(prime_cutoff_certificate(n, cutoff).verify())

    def test_rough_depth_one_when_cutoff_squared_covers_block(self) -> None:
        block_max = 512
        cutoff = 23
        self.assertTrue(rough_linear_on_block(block_max, cutoff))
        for n in range(1, block_max + 1):
            if rough_mobius(n, cutoff):
                self.assertLessEqual(rough_mobius_degree(n, cutoff), 1)

        self.assertFalse(rough_linear_on_block(512, 11))
        self.assertEqual(rough_mobius_degree(13 * 17, 11), 2)


if __name__ == "__main__":
    unittest.main()
