import unittest

from enterprise_math.p017_split_pattern import (
    simultaneous_split_count,
    split_pattern,
    split_pattern_count,
)


class P017SplitPatternTests(unittest.TestCase):
    def test_k8_has_simultaneous_p2_p3_split(self) -> None:
        self.assertEqual(split_pattern(8, (2, 3)), (True, True))

    def test_pattern_counts_partition_the_bounded_range(self) -> None:
        primes = (2, 3)
        max_k = 300
        total = sum(
            split_pattern_count(primes, pattern, max_k)
            for pattern in ((False, False), (False, True), (True, False), (True, True))
        )
        self.assertEqual(total, max_k - max(primes) + 1)

    def test_every_small_fixed_prime_family_has_bounded_simultaneous_witnesses(self) -> None:
        self.assertGreater(simultaneous_split_count((2, 3), 100), 0)
        self.assertGreater(simultaneous_split_count((2, 3, 5), 1000), 0)


if __name__ == "__main__":
    unittest.main()
