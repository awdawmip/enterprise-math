import unittest

from enterprise_math.p017_hard_core import residual_hard_core_tail_gap
from enterprise_math.p017_mirror import anchor_surviving_radius, mirror_pair
from enterprise_math.p017_cofactor_window import square_basin_smooth_tail


class P017HardCoreTests(unittest.TestCase):
    def test_known_hard_core_witnesses(self):
        data = residual_hard_core_tail_gap(22, 5)
        self.assertEqual((data["lower_core"], data["upper_core"]), (3, 7))
        self.assertEqual((data["lower_tail"], data["upper_tail"]), (167, 73))
        self.assertEqual(data["tail_gap"], 94)
        self.assertGreaterEqual(data["tail_gap"], data["parity_lower_bound"])

        data = residual_hard_core_tail_gap(28, 23)
        self.assertEqual((data["lower_core"], data["upper_core"]), (3, 5))
        self.assertEqual((data["lower_tail"], data["upper_tail"]), (263, 167))
        self.assertEqual(data["tail_gap"], 96)

    def test_dense_residual_hard_core_scan(self):
        saw = False
        for k in range(5, 220):
            for r in range(1, k):
                if not anchor_surviving_radius(k, r):
                    continue
                lower, upper = mirror_pair(k, r)
                lower_data = square_basin_smooth_tail(k, lower)
                upper_data = square_basin_smooth_tail(k, upper)
                if bool(lower_data["is_prime"]) or bool(upper_data["is_prime"]):
                    continue
                a = int(lower_data["smooth_core"])
                b = int(upper_data["smooth_core"])
                if a * b >= k:
                    continue
                data = residual_hard_core_tail_gap(k, r)
                self.assertLess(data["core_product"], k)
                self.assertGreater(data["lower_tail"], k)
                self.assertGreater(data["upper_tail"], k)
                self.assertGreater(data["tail_gap"], k + 5)
                self.assertGreaterEqual(data["tail_gap"], data["parity_lower_bound"])
                self.assertEqual(data["tail_gap"] % 2, 0)
                saw = True
        self.assertTrue(saw)

    def test_rejects_nonhard_cases(self):
        with self.assertRaises(ValueError):
            residual_hard_core_tail_gap(31, 7)  # full-core product 135 >= 31
        with self.assertRaises(ValueError):
            residual_hard_core_tail_gap(10, 2)  # not anchor-surviving


if __name__ == "__main__":
    unittest.main()
