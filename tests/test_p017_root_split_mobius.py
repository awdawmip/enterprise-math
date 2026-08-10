import unittest

from enterprise_math.legendre import primes_up_to
from enterprise_math.p017_factor_root_spectrum import factor_root_relative_spectrum
from enterprise_math.p017_root_split_mobius import (
    root_split_mobius_counts,
    split_shell_count_by_mobius,
)
from enterprise_math.rough_interval_mobius import (
    rough_interval_direct_count,
    rough_interval_mobius_count,
)


class P017RootSplitMobiusTests(unittest.TestCase):
    def test_mobius_rough_interval_count_matches_direct_gcd_oracle(self) -> None:
        for prime in (2, 3, 5, 7, 11, 13):
            for lower in range(1, 30, 5):
                upper = lower + 11
                self.assertEqual(
                    rough_interval_mobius_count(lower, upper, prime),
                    rough_interval_direct_count(lower, upper, prime),
                )

    def test_mobius_branch_counts_reconstruct_actual_split_shells(self) -> None:
        for k in range(3, 80):
            split_primes = []
            for prime in primes_up_to(k):
                data = root_split_mobius_counts(k, prime)
                if data["realized_split"]:
                    split_primes.append(prime)
            expected = factor_root_relative_spectrum(k)["split_shell_primes"]
            self.assertEqual(tuple(split_primes), expected)

    def test_split_shell_count_is_exact_mobius_positivity_sum(self) -> None:
        for k in range(3, 80):
            self.assertEqual(
                split_shell_count_by_mobius(k),
                factor_root_relative_spectrum(k)["split_shell_count"],
            )

    def test_k6_p3_false_raw_split_has_zero_upper_mobius_count(self) -> None:
        data = root_split_mobius_counts(6, 3)
        self.assertTrue(data["raw_split"])
        self.assertGreater(data["lower_rough_count"], 0)
        self.assertEqual(data["upper_rough_count"], 0)
        self.assertFalse(data["realized_split"])


if __name__ == "__main__":
    unittest.main()
