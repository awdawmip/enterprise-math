import unittest
from math import isqrt

from enterprise_math.p018_divisor_window import (
    divisor_quotient_window,
    divisor_window_separation,
    nonadjacent_small_product_root_pair_separation,
    odd_small_product_root_pair_separation,
    same_parity_divisor_windows,
)


class P018DivisorWindowTests(unittest.TestCase):
    def test_exact_window_endpoints(self):
        for k in range(3, 80):
            for d in range(2, k + 1):
                lo, hi = divisor_quotient_window(k, d)
                values = {n // d for n in range(k * k + 1, (k + 1) * (k + 1))}
                self.assertEqual(min(values), lo)
                self.assertEqual(max(values), hi)

    def test_sufficient_criterion_implies_strict_separation(self):
        for k in range(3, 160):
            for d in range(2, k):
                for e in range(d + 1, k + 1):
                    if 2 * d <= k * (e - d):
                        data = divisor_window_separation(k, d, e)
                        self.assertLess(data["right_window"][1], data["left_window"][0])
                        self.assertGreaterEqual(data["criterion_margin"], 0)
                        self.assertGreaterEqual(data["integer_gap"], 0)

    def test_all_same_parity_pairs_satisfy_criterion(self):
        for k in range(3, 250):
            data = same_parity_divisor_windows(k)
            for d, e in data["checked_pairs"]:
                self.assertEqual((e - d) % 2, 0)
                self.assertGreaterEqual(k * (e - d), 2 * d)

    def test_nonadjacent_small_product_root_pairs_are_disjoint(self):
        saw_d2 = False
        saw_general = False
        for k in range(7, 500):
            for d in range(2, k):
                for e in range(d + 2, k + 1):
                    if d * e >= k:
                        break
                    data = nonadjacent_small_product_root_pair_separation(k, d, e)
                    self.assertGreaterEqual(data["root_gap"], 2)
                    self.assertTrue(
                        set(data["left_candidates"]).isdisjoint(
                            data["right_candidates"]
                        )
                    )
                    if d == 2:
                        saw_d2 = True
                    else:
                        self.assertGreaterEqual(data["right_root"], 2 * d + 1)
                        saw_general = True
        self.assertTrue(saw_d2)
        self.assertTrue(saw_general)

    def test_sharp_small_product_base_families(self):
        data = nonadjacent_small_product_root_pair_separation(9, 2, 4)
        self.assertEqual((data["left_root"], data["right_root"]), (6, 4))
        self.assertEqual(data["root_gap"], 2)

        data = nonadjacent_small_product_root_pair_separation(16, 3, 5)
        self.assertEqual((data["left_root"], data["right_root"]), (9, 7))
        self.assertEqual(data["root_gap"], 2)

    def test_odd_corollary_routes_to_general_theorem(self):
        general = nonadjacent_small_product_root_pair_separation(52, 3, 7)
        odd = odd_small_product_root_pair_separation(52, 3, 7)
        self.assertEqual(general, odd)

    def test_adjacent_divisors_are_a_real_boundary(self):
        # de<k alone is insufficient when e=d+1.
        k = 13
        left_root = isqrt((k * k) // 3)
        right_root = isqrt((k * k) // 4)
        self.assertEqual((left_root, right_root), (7, 6))
        self.assertEqual(left_root - right_root, 1)
        with self.assertRaises(ValueError):
            nonadjacent_small_product_root_pair_separation(k, 3, 4)

    def test_adjacent_opposite_parity_can_overlap_windows(self):
        self.assertEqual(divisor_quotient_window(3, 2), (5, 7))
        self.assertEqual(divisor_quotient_window(3, 3), (4, 5))
        self.assertEqual(
            set(range(5, 8)).intersection(range(4, 6)),
            {5},
        )

    def test_validation(self):
        with self.assertRaises(ValueError):
            divisor_quotient_window(5, 1)
        with self.assertRaises(ValueError):
            divisor_window_separation(10, 6, 7)
        with self.assertRaises(ValueError):
            nonadjacent_small_product_root_pair_separation(13, 3, 4)
        with self.assertRaises(ValueError):
            nonadjacent_small_product_root_pair_separation(16, 3, 7)
        with self.assertRaises(ValueError):
            odd_small_product_root_pair_separation(16, 2, 5)


if __name__ == "__main__":
    unittest.main()
