import unittest

from enterprise_math.p017_high_product_split_geometry import (
    fixed_product_split_capacity,
    split_signed_residue,
    split_spacing_clique_capacity,
)


class P017HighProductSplitGeometryTests(unittest.TestCase):
    def test_k61_s105_sharp_three_split_example(self):
        data = fixed_product_split_capacity(61, 105)
        self.assertEqual(data["prime_factors"], (3, 5, 7))
        self.assertEqual(data["split_spacing_clique_capacity"], 3)
        self.assertEqual(
            data["anchor_split_points"],
            ((3, 37), (5, 23), (7, 47)),
        )
        self.assertEqual(data["same_product_terminal_capacity"], 3)

    def test_same_product_split_spacing_is_exact(self):
        data = fixed_product_split_capacity(61, 105)
        points = dict(data["anchor_split_points"])
        self.assertEqual((points[3] - points[5]) % (2 * 105 // (3 * 5)), 0)
        self.assertEqual((points[3] - points[7]) % (2 * 105 // (3 * 7)), 0)
        self.assertEqual((points[5] - points[7]) % (2 * 105 // (5 * 7)), 0)

    def test_large_combined_product_spacing_reduces_clique_capacity(self):
        # 3*5*7*67*3719.  The threshold graph allows at most three split
        # primes at k=8191, while exact alignment+anchor leaves only one.
        product_value = 26_163_165
        clique = split_spacing_clique_capacity(8_191, product_value)
        data = fixed_product_split_capacity(8_191, product_value)
        self.assertEqual(clique["prime_factors"], (3, 5, 7, 67, 3719))
        self.assertEqual(clique["split_spacing_clique_capacity"], 3)
        self.assertEqual(data["anchor_split_count"], 1)
        self.assertEqual(data["same_product_terminal_capacity"], 1)

    def test_known_duplicate_product_has_two_aligned_terminal_splits(self):
        # The k=9070 terminal bridge has two different residual-side splits
        # with the same combined product S=69069.
        data = fixed_product_split_capacity(9_070, 69_069)
        self.assertEqual(data["prime_factors"], (3, 7, 11, 13, 23))
        self.assertIn((11, 233), data["anchor_split_points"])
        self.assertIn((23, 779), data["anchor_split_points"])
        self.assertGreaterEqual(data["same_product_terminal_capacity"], 2)

    def test_split_residue_satisfies_both_side_divisibilities(self):
        data = split_signed_residue(9_070, 69_069, 11)
        x = data["centered_residue"]
        m = 9_070 * 9_071
        self.assertEqual((m - x) % (69_069 // 11), 0)
        self.assertEqual((m + x) % 11, 0)
        self.assertEqual(x % 2, 1)


if __name__ == "__main__":
    unittest.main()
