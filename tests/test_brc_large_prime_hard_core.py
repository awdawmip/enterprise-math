from __future__ import annotations

import unittest

from enterprise_math.brc_count_centered_carry import carry_bit, primes_up_to
from enterprise_math.brc_large_prime_hard_core import (
    large_prime_increment_certificate,
    odd_prime_carry_by_residue,
    odd_prime_carry_time_increment,
    rough_prime_radical_valuations,
)


class BRCLargePrimeHardCoreTests(unittest.TestCase):
    def test_half_residue_and_time_increment(self) -> None:
        for p in primes_up_to(97):
            if p == 2:
                continue
            for n in range(1, 257):
                self.assertEqual(odd_prime_carry_by_residue(n, p), carry_bit(n, p))
                self.assertEqual(
                    odd_prime_carry_time_increment(n, p),
                    carry_bit(n + 1, p) - carry_bit(n, p),
                )

    def test_exact_large_prime_increment_compiler(self) -> None:
        for cutoff in (3, 5, 7, 11, 17):
            for n in range(max(2, cutoff), 257):
                self.assertTrue(large_prime_increment_certificate(n, cutoff).verify())

    def test_degree_one_rough_radical_when_cutoff_squared_is_large(self) -> None:
        cutoff = 23
        for value in range(1, cutoff * cutoff):
            self.assertLessEqual(len(rough_prime_radical_valuations(value, cutoff)), 1)


if __name__ == "__main__":
    unittest.main()
