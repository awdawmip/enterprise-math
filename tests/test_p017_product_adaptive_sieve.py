import unittest

from enterprise_math.p017_product_adaptive_sieve import (
    ordinary_bonferroni_divisor_sum,
    product_adaptive_divisor_majorant,
    squarefree_token_candidates_below_cutoff,
    support_moment_divisor_sum,
)


class P017ProductAdaptiveSieveTests(unittest.TestCase):
    def test_support_moment_divisor_sum_matches_small_reference_values(self):
        self.assertEqual(support_moment_divisor_sum(22, 1)["support_moment"], 17)
        self.assertEqual(support_moment_divisor_sum(22, 2)["support_moment"], 5)
        self.assertEqual(support_moment_divisor_sum(31, 1)["support_moment"], 30)

    def test_ordinary_bonferroni_is_pure_cg12_divisor_sum(self):
        self.assertEqual(ordinary_bonferroni_divisor_sum(18, 1)["ordinary_bonferroni"], 7)
        self.assertEqual(ordinary_bonferroni_divisor_sum(22, 1)["ordinary_bonferroni"], 17)
        self.assertEqual(ordinary_bonferroni_divisor_sum(22, 3)["ordinary_bonferroni"], 13)
        self.assertEqual(ordinary_bonferroni_divisor_sum(31, 3)["ordinary_bonferroni"], 20)

    def test_full_product_adaptive_majorant_uses_cg13_cg14(self):
        k18 = product_adaptive_divisor_majorant(18, 1)
        self.assertEqual(k18["ordinary_bonferroni"], 7)
        self.assertEqual(k18["ordinary_token_defect"], 1)
        self.assertEqual(k18["reusable_full_block_token_mass"], 0)
        self.assertEqual(k18["product_adaptive_majorant"], 6)
        self.assertEqual(k18["high_full_block_correction"], 1)

        k22 = product_adaptive_divisor_majorant(22, 1)
        self.assertEqual(k22["ordinary_bonferroni"], 17)
        self.assertEqual(k22["ordinary_token_defect"], 4)
        self.assertEqual(k22["reusable_squarefree_token_mass"], 2)
        self.assertEqual(k22["reusable_full_block_token_mass"], 1)
        self.assertEqual(k22["product_adaptive_majorant"], 14)
        self.assertEqual(k22["high_full_block_correction"], 3)

        k31 = product_adaptive_divisor_majorant(31, 1)
        self.assertEqual(k31["ordinary_bonferroni"], 30)
        self.assertEqual(k31["ordinary_token_defect"], 10)
        self.assertEqual(k31["reusable_full_block_token_mass"], 2)
        self.assertEqual(k31["product_adaptive_majorant"], 22)

    def test_low_product_candidate_generator_prunes_by_joint_product(self):
        # Four-prime products <=1999 are a very small subset of all choices.
        rows = squarefree_token_candidates_below_cutoff(2000, 3)
        self.assertTrue(rows)
        self.assertEqual(rows[0], (1155, (3, 5, 7, 11)))
        self.assertTrue(all(product <= 1999 for product, _primes in rows))
        self.assertTrue(all(len(primes) == 4 for _product, primes in rows))

    def test_invalid_even_order(self):
        with self.assertRaises(ValueError):
            product_adaptive_divisor_majorant(22, 2)


if __name__ == "__main__":
    unittest.main()
