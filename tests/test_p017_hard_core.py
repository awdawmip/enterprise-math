import unittest

from enterprise_math.p017_hard_core import (
    anchor_parity_full_core_capacity,
    residual_hard_core_tail_gap,
    residual_multi_lift_tail_gap,
)
from enterprise_math.p017_mirror import anchor_surviving_radius, mirror_pair
from enterprise_math.p017_cofactor_window import square_basin_smooth_tail


class P017HardCoreTests(unittest.TestCase):
    def test_anchor_parity_doubles_effective_full_core_modulus(self):
        # k=28,r=23 has S_-=3, S_+=5, S=15.
        # Raw L053 lifts mod 15 are [8,23]; anchor-forced odd parity keeps only 23.
        data = anchor_parity_full_core_capacity(28, 23)
        self.assertEqual(data["modulus"], 15)
        self.assertEqual(data["raw_full_core_lifts"], [8, 23])
        self.assertEqual(data["parity_full_core_lifts"], [23])
        self.assertEqual(data["anchor_full_core_lifts"], [23])
        self.assertEqual(data["parity_modulus"], 30)
        self.assertEqual(data["parity_capacity"], 1)

    def test_2s_ge_k_forces_at_most_one_parity_lift(self):
        saw = False
        for k in range(5, 180):
            for r in range(1, k):
                if not anchor_surviving_radius(k, r):
                    continue
                lower, upper = mirror_pair(k, r)
                lower_data = square_basin_smooth_tail(k, lower)
                upper_data = square_basin_smooth_tail(k, upper)
                if bool(lower_data["is_prime"]) or bool(upper_data["is_prime"]):
                    continue
                data = anchor_parity_full_core_capacity(k, r)
                if 2 * int(data["modulus"]) >= k:
                    self.assertLessEqual(data["parity_capacity"], 1)
                    saw = True
        self.assertTrue(saw)

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
        saw_multi = False
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

                if 2 * a * b < k:
                    multi = residual_multi_lift_tail_gap(k, r)
                    self.assertGreater(multi["tail_gap"], 3 * k + 9)
                    self.assertGreaterEqual(
                        multi["tail_gap"], multi["multi_lift_parity_lower_bound"]
                    )
                    saw_multi = True
        self.assertTrue(saw)
        self.assertTrue(saw_multi)

    def test_multi_lift_witness(self):
        data = residual_multi_lift_tail_gap(52, 23)
        self.assertEqual((data["lower_core"], data["upper_core"]), (3, 7))
        self.assertEqual(data["core_product"], 21)
        self.assertLess(2 * data["core_product"], 52)
        self.assertEqual((data["lower_tail"], data["upper_tail"]), (911, 397))
        self.assertEqual(data["tail_gap"], 514)
        self.assertGreater(data["tail_gap"], 3 * 52 + 9)

    def test_rejects_nonhard_cases(self):
        with self.assertRaises(ValueError):
            residual_hard_core_tail_gap(31, 7)  # full-core product 135 >= 31
        with self.assertRaises(ValueError):
            residual_hard_core_tail_gap(10, 2)  # not anchor-surviving
        with self.assertRaises(ValueError):
            residual_multi_lift_tail_gap(28, 23)  # 2*15 >= 28


if __name__ == "__main__":
    unittest.main()
