import unittest
from enterprise_math.precision_covering_code_isa import (
    binary_covering_radius, depth_one_exact_length, hamming_ball_volume,
    normalized_binary_search, one_redundant_radius, short_word_excess,
    volume_lower_bound_length,
)

class CoveringCodeISATests(unittest.TestCase):
    def test_volume_and_endpoints(self):
        self.assertEqual(hamming_ball_volume(2,5,2),16)
        self.assertEqual(volume_lower_bound_length(2,5,2),8)
        self.assertEqual(depth_one_exact_length(2,5),31)
        self.assertEqual(one_redundant_radius(2,7),4)

    def test_r5_radius2_construction(self):
        gens=(1,2,4,8,16,3,5,6,31)
        self.assertEqual(binary_covering_radius(gens,5),2)
        self.assertEqual(short_word_excess(2,5,9,2),14)

    def test_r7_radius3_construction(self):
        gens=(1,2,4,8,16,32,64,96,57,97,71)
        self.assertEqual(binary_covering_radius(gens,7),3)

    def test_normalized_small_lower_bound(self):
        checked, found = normalized_binary_search(5,2,8)
        self.assertEqual(checked,2600)
        self.assertIsNone(found)

if __name__=="__main__":
    unittest.main()
