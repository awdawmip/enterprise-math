import unittest
from math import isqrt

from enterprise_math.p018_divisor_window import (
    divisor_channel_overlap_dichotomy,
    divisor_quotient_window,
    divisor_root_channel,
    divisor_window_separation,
    fourth_root,
    high_scale_divisor_channel_multiplicity,
    nonadjacent_small_product_root_pair_separation,
    odd_small_product_root_pair_separation,
    product_threshold_overlap_quartic_contraction,
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

    def test_overlap_dichotomy_exhaustive_small_range(self):
        saw_adjacent = False
        saw_product = False
        for k in range(4, 70):
            for d in range(2, k):
                for e in range(d + 1, k + 1):
                    data = divisor_channel_overlap_dichotomy(k, d, e)
                    if not data["overlap"]:
                        continue
                    self.assertTrue(
                        data["adjacent_exception"] or data["product_threshold"]
                    )
                    saw_adjacent |= bool(data["adjacent_exception"])
                    saw_product |= bool(data["product_threshold"])
        self.assertTrue(saw_adjacent)
        self.assertTrue(saw_product)

    def test_k14_sharp_collision_is_adjacent_high_scale_exception(self):
        self.assertEqual(fourth_root(14**3), 7)
        data = divisor_channel_overlap_dichotomy(14, 2, 3)
        self.assertTrue(data["overlap"])
        self.assertEqual(data["common_roots"], (9,))
        self.assertTrue(data["adjacent_exception"])
        self.assertFalse(data["product_threshold"])

        high = high_scale_divisor_channel_multiplicity(14, 9)
        self.assertEqual(high["coalescence_horizon"], 8)
        self.assertEqual(high["divisor_hits"], (2, 3))
        self.assertEqual(high["multiplicity"], 2)
        self.assertTrue(high["adjacent_double"])

    def test_product_overlap_contracts_below_quartic_horizon(self):
        data = product_threshold_overlap_quartic_contraction(20, 5, 7)
        self.assertEqual(data["common_roots"], (8,))
        self.assertTrue(data["product_threshold"])
        self.assertEqual(data["larger_base_root"], 7)
        self.assertEqual(data["quartic_base_ceiling"], fourth_root(20**3))
        self.assertLessEqual(
            max(data["common_roots"]),
            data["coalescence_horizon"],
        )

    def test_all_product_threshold_overlaps_obey_quartic_horizon(self):
        saw = False
        for k in range(4, 85):
            ceiling = fourth_root(k**3) + 1
            for d in range(2, k):
                for e in range(d + 1, k + 1):
                    data = divisor_channel_overlap_dichotomy(k, d, e)
                    if not data["overlap"] or not data["product_threshold"]:
                        continue
                    contracted = product_threshold_overlap_quartic_contraction(k, d, e)
                    self.assertLessEqual(max(contracted["common_roots"]), ceiling)
                    self.assertLessEqual(contracted["larger_base_root"] ** 4, k**3)
                    saw = True
        self.assertTrue(saw)

    def test_above_quartic_horizon_multiplicity_is_at_most_two(self):
        saw_double = False
        saw_single = False
        for k in range(6, 65):
            horizon = fourth_root(k**3) + 1
            for target in range(horizon + 1, k + 1):
                data = high_scale_divisor_channel_multiplicity(k, target)
                self.assertLessEqual(data["multiplicity"], 2)
                if data["multiplicity"] == 2:
                    left, right = data["divisor_hits"]
                    self.assertEqual(right, left + 1)
                    saw_double = True
                elif data["multiplicity"] == 1:
                    saw_single = True
        self.assertTrue(saw_double)
        self.assertTrue(saw_single)

    def test_high_scale_odd_divisor_channels_are_unique(self):
        for k in range(10, 65):
            horizon = fourth_root(k**3) + 1
            for target in range(horizon + 1, k + 1):
                data = high_scale_divisor_channel_multiplicity(k, target)
                odd_hits = [d for d in data["divisor_hits"] if d % 2]
                self.assertLessEqual(len(odd_hits), 1)

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
            divisor_root_channel(5, 1)
        with self.assertRaises(ValueError):
            divisor_window_separation(10, 6, 7)
        with self.assertRaises(ValueError):
            nonadjacent_small_product_root_pair_separation(13, 3, 4)
        with self.assertRaises(ValueError):
            nonadjacent_small_product_root_pair_separation(16, 3, 7)
        with self.assertRaises(ValueError):
            odd_small_product_root_pair_separation(16, 2, 5)
        with self.assertRaises(ValueError):
            product_threshold_overlap_quartic_contraction(14, 2, 3)
        with self.assertRaises(ValueError):
            high_scale_divisor_channel_multiplicity(14, 8)


if __name__ == "__main__":
    unittest.main()
