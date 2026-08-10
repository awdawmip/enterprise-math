import unittest

from enterprise_math.p017_fixed_prime_split_exceptions import (
    fixed_prime_failure_count,
    fixed_prime_failure_defect,
)


class P017FixedPrimeSplitExceptionTests(unittest.TestCase):
    def test_every_bounded_failure_has_a_bounded_pell_defect(self) -> None:
        for prime in (2, 3, 5, 7, 11):
            for k in range(max(3, prime), 500):
                data = fixed_prime_failure_defect(k, prime)
                if not data["failure"]:
                    continue
                self.assertTrue(
                    data["lower_defect"] is not None
                    or data["upper_defect"] is not None
                )

    def test_failure_counts_are_sparse_on_bounded_ranges(self) -> None:
        counts_1000 = {
            prime: fixed_prime_failure_count(prime, 1000)
            for prime in (2, 3, 5, 7, 11)
        }
        counts_5000 = {
            prime: fixed_prime_failure_count(prime, 5000)
            for prime in (2, 3, 5, 7, 11)
        }
        for prime in counts_1000:
            self.assertGreaterEqual(counts_5000[prime], counts_1000[prime])
            self.assertLess(counts_5000[prime], 500)


if __name__ == "__main__":
    unittest.main()
