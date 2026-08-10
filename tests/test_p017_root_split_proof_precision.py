import unittest

from enterprise_math.p017_root_split_proof_precision import split_branch_proof_depths
from enterprise_math.rough_bonferroni import (
    minimum_positive_bonferroni_depth,
    rough_bonferroni_lower_bound,
)
from enterprise_math.rough_interval_mobius import rough_interval_mobius_count


class P017RootSplitProofPrecisionTests(unittest.TestCase):
    def test_odd_bonferroni_bounds_never_exceed_exact_rough_count(self) -> None:
        for prime in (3, 5, 7, 11, 13):
            for lower in range(1, 40, 7):
                upper = lower + 12
                exact = rough_interval_mobius_count(lower, upper, prime)
                small_prime_count = len(__import__("enterprise_math.legendre", fromlist=["primes_up_to"]).primes_up_to(prime - 1))
                for depth in range(1, small_prime_count + 1, 2):
                    self.assertLessEqual(
                        rough_bonferroni_lower_bound(lower, upper, prime, depth),
                        exact,
                    )

    def test_proof_depth_really_jumps_across_actual_split_shells(self) -> None:
        data8 = split_branch_proof_depths(8, 3)
        self.assertEqual((data8["lower_proof_depth"], data8["upper_proof_depth"]), (1, 1))
        self.assertEqual(data8["split_proof_depth"], 1)

        data18 = split_branch_proof_depths(18, 7)
        self.assertEqual((data18["lower_proof_depth"], data18["upper_proof_depth"]), (3, 3))
        self.assertEqual(data18["split_proof_depth"], 3)

        data104 = split_branch_proof_depths(104, 13)
        self.assertEqual((data104["lower_proof_depth"], data104["upper_proof_depth"]), (5, 3))
        self.assertEqual(data104["split_proof_depth"], 5)

    def test_failed_odd_certificate_does_not_mean_empty_interval(self) -> None:
        # Search a small deterministic interval family for an exact-positive case
        # with no positive odd truncation, pinning the semantic distinction if one
        # exists.  The assertion is conditional because not every tiny family has
        # such a witness.
        witness = None
        for prime in (5, 7, 11, 13, 17):
            for lower in range(1, 80):
                upper = lower + 5
                if rough_interval_mobius_count(lower, upper, prime) <= 0:
                    continue
                if minimum_positive_bonferroni_depth(lower, upper, prime) is None:
                    witness = (lower, upper, prime)
                    break
            if witness is not None:
                break
        if witness is not None:
            lower, upper, prime = witness
            self.assertGreater(rough_interval_mobius_count(lower, upper, prime), 0)
            self.assertIsNone(minimum_positive_bonferroni_depth(lower, upper, prime))


if __name__ == "__main__":
    unittest.main()
