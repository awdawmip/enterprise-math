from itertools import combinations
from math import comb, prod
import unittest

from enterprise_math.cutoff_pairing import transverse_prime_support
from enterprise_math.legendre import anchor_product
from enterprise_math.p017_canonical_token_incidence import (
    canonical_least_support_incidence_mobius,
    canonical_order_token_incidence,
    canonical_token_incidence_profile,
)
from enterprise_math.p017_mirror import (
    anchor_surviving_radius,
    mirror_center,
    mirror_pair,
)


class P017CanonicalTokenIncidenceTests(unittest.TestCase):
    def _direct_token_counts(self, k: int, order: int) -> tuple[int, int, int]:
        center = mirror_center(k)
        anchor = anchor_product(k)
        total = 0
        reusable = 0
        single_use = 0
        for radius in range(1, k):
            if not anchor_surviving_radius(k, radius):
                continue
            for state in mirror_pair(k, radius):
                support = tuple(transverse_prime_support(state, k, anchor))
                if len(support) <= order:
                    continue
                least = support[0]
                row_count = 0
                for subset in combinations(support[1:], order):
                    divisor = least * prod(subset)
                    row_count += 1
                    total += 1
                    if divisor <= k - 1:
                        reusable += 1
                    else:
                        single_use += 1
                self.assertEqual(row_count, comb(len(support) - 1, order))
        self.assertEqual(total, reusable + single_use)
        return total, reusable, single_use

    def test_least_support_mobius_formula_removes_smaller_prime_incidence(self):
        # k=22, D=5*7=35.  A raw D-incidence whose state is also divisible by 3
        # must not be counted as a canonical token with least prime 5.
        data = canonical_least_support_incidence_mobius(22, 35)
        self.assertEqual(data["token_primes"], (5, 7))
        self.assertEqual(data["smaller_transverse_primes"], (3,))
        self.assertEqual(
            data["canonical_incidence"],
            len(data["canonical_signed_points"]),
        )

    def test_specific_order_one_tokens(self):
        # k=22 has canonical order-one token products 39,57,15,21 on the
        # signed states with support sizes >=2.
        expected_nonzero = {15, 21, 39, 57}
        observed = set()
        for divisor in expected_nonzero:
            data = canonical_order_token_incidence(22, divisor, 1)
            self.assertEqual(data["canonical_incidence"], 1)
            observed.add(divisor)
        self.assertEqual(observed, expected_nonzero)

    def test_global_divisor_sum_equals_statewise_bonferroni_defect(self):
        for k, order in ((18, 1), (22, 1), (31, 1), (64, 1)):
            direct = self._direct_token_counts(k, order)
            profile = canonical_token_incidence_profile(k, order)
            self.assertEqual(profile["canonical_token_mass"], direct[0])
            self.assertEqual(profile["reusable_squarefree_token_mass"], direct[1])
            self.assertEqual(profile["single_use_squarefree_token_mass"], direct[2])

    def test_known_k22_cutoff_split(self):
        profile = canonical_token_incidence_profile(22, 1)
        self.assertEqual(profile["canonical_token_mass"], 4)
        self.assertEqual(profile["reusable_squarefree_token_mass"], 2)
        self.assertEqual(profile["single_use_squarefree_token_mass"], 2)

    def test_invalid_wrong_order_depth(self):
        with self.assertRaises(ValueError):
            canonical_order_token_incidence(22, 15, 3)


if __name__ == "__main__":
    unittest.main()
