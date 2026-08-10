import unittest
from enterprise_math.precision_padic_covering_isa import (
    covers, depth_one_exact_length, hamming_ball_volume,
    one_null_depth_gain, one_null_radius, volume_lower_bound_length
)

class PadicCoveringISATests(unittest.TestCase):
    def test_depth_one_scaling(self):
        self.assertEqual(depth_one_exact_length(2,1,3),7)
        self.assertEqual(depth_one_exact_length(2,2,3),28)
        self.assertEqual(depth_one_exact_length(3,2,2),12)

    def test_one_null_precision_loss(self):
        self.assertEqual(one_null_radius(2,1,3),2)
        self.assertEqual(one_null_radius(2,2,3),3)
        self.assertEqual(one_null_depth_gain(2,2,3),0)

    def test_z4_rank3_radius2_construction(self):
        cols=((1,0,0),(0,1,0),(0,0,1),(0,1,1),(0,1,2),(1,1,3))
        self.assertTrue(covers(cols,4,2))
        self.assertEqual(volume_lower_bound_length(2,2,3,2),4)

    def test_volume(self):
        self.assertEqual(hamming_ball_volume(2,2,4,2),67)

if __name__=="__main__":
    unittest.main()
