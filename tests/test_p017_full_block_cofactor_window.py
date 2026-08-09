import unittest

from enterprise_math.p017_full_block_cofactor_window import (
    canonical_full_block_cofactors,
    full_block_cofactor_window,
)


class P017FullBlockCofactorWindowTests(unittest.TestCase):
    def test_k22_full_block_windows_recover_exact_token_incidence(self):
        block75 = canonical_full_block_cofactors(22, 75)
        self.assertEqual(block75["q_min"], 7)
        self.assertEqual(block75["q_max"], 7)
        self.assertEqual(block75["canonical_cofactors"], (7,))
        self.assertEqual(block75["canonical_signed_points"], (-19,))
        self.assertEqual(block75["canonical_incidence"], 1)

        block21 = canonical_full_block_cofactors(22, 21)
        self.assertEqual(block21["q_min"], 24)
        self.assertEqual(block21["q_max"], 25)
        self.assertEqual(block21["canonical_cofactors"], (25,))
        self.assertEqual(block21["canonical_signed_points"], (-19,))
        self.assertEqual(block21["canonical_incidence"], 1)

    def test_exact_valuation_filter_can_empty_a_raw_squarefree_window(self):
        data = canonical_full_block_cofactors(22, 45)
        self.assertEqual(data["canonical_cofactors"], ())
        self.assertEqual(data["canonical_incidence"], 0)

    def test_k524287_order_five_reusable_candidate_windows_leave_exactly_five(self):
        # These are exactly the nine six-prime radicals below the parent cutoff.
        candidates = (
            255_255,
            285_285,
            345_345,
            373_065,
            435_435,
            440_895,
            451_605,
            465_465,
            504_735,
        )
        expected = {
            255_255: (),
            285_285: (963_517,),
            345_345: (),
            373_065: (736_807,),
            435_435: (631_271,),
            440_895: (623_453,),
            451_605: (),
            465_465: (590_543,),
            504_735: (),
        }
        total = 0
        raw_sizes = {}
        for block in candidates:
            data = canonical_full_block_cofactors(524_287, block)
            self.assertLessEqual(data["raw_window_size"], 4)
            self.assertEqual(data["canonical_cofactors"], expected[block])
            raw_sizes[block] = data["raw_window_size"]
            total += data["canonical_incidence"]
        self.assertEqual(total, 5)
        self.assertEqual(raw_sizes[255_255], 4)
        self.assertEqual(raw_sizes[285_285], 4)

    def test_window_endpoints_are_integer_only(self):
        data = full_block_cofactor_window(64, 105)
        self.assertEqual(data["q_min"], (64 * 64) // 105 + 1)
        self.assertEqual(data["q_max"], (64 * 66) // 105)

    def test_invalid_anchor_prime_block(self):
        with self.assertRaises(ValueError):
            canonical_full_block_cofactors(22, 33)


if __name__ == "__main__":
    unittest.main()
