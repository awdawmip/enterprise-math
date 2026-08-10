import unittest

from enterprise_math.legendre import primes_up_to
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
                small_prime_count = len(primes_up_to(prime - 1))
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

    def test_actual_p017_branch_can_require_full_method_switch(self) -> None:
        data = split_branch_proof_depths(13, 5)
        self.assertTrue(data["realized_split"])
        self.assertEqual(data["upper_interval"], (36, 39))
        self.assertEqual(data["upper_rough_count"], 1)
        self.assertEqual(data["lower_proof_depth"], 1)
        self.assertIsNone(data["upper_proof_depth"])
        self.assertIsNone(data["split_proof_depth"])
        self.assertEqual(rough_bonferroni_lower_bound(36, 39, 5, 1), 0)
        self.assertEqual(rough_interval_mobius_count(36, 39, 5), 1)

    def test_abstract_positive_interval_can_escape_all_odd_lower_truncations(self) -> None:
        # For p=5 and [2,6], the unique 5-rough state is 5.  The first-order
        # lower bound is zero and there is no deeper odd truncation because only
        # the small primes 2 and 3 are present; exact positivity returns only
        # after the even pair-intersection correction.
        self.assertEqual(rough_interval_mobius_count(2, 6, 5), 1)
        self.assertEqual(rough_bonferroni_lower_bound(2, 6, 5, 1), 0)
        self.assertIsNone(minimum_positive_bonferroni_depth(2, 6, 5))


if __name__ == "__main__":
    unittest.main()
