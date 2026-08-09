import unittest
from math import isqrt

from enterprise_math.p018_channel_coalescence import (
    actual_coalescence_horizon,
    actual_collision_horizon_chain,
    actual_divisor_root,
    actual_divisor_root_collision,
    actual_horizon_strict_descent,
    candidate_coalescence_horizon,
    candidate_horizon_strict_descent,
    divisor_root_channel,
    high_scale_actual_divisor_root_injectivity,
    high_scale_candidate_channel_multiplicity,
    nonadjacent_candidate_overlap_cubic_contraction,
)


class P018ChannelCoalescenceTests(unittest.TestCase):
    def test_nonadjacent_overlaps_obey_cubic_candidate_horizon(self):
        saw = False
        saw_near = False
        for k in range(5, 300):
            horizon = candidate_coalescence_horizon(k)
            for d in range(2, k):
                for e in range(d + 2, k + 1):
                    try:
                        data = nonadjacent_candidate_overlap_cubic_contraction(
                            k, d, e
                        )
                    except ValueError:
                        continue
                    self.assertLess(data["right_base_cubic"], 2 * k * k)
                    self.assertLessEqual(max(data["common_roots"]), horizon)
                    saw = True
                    if max(data["common_roots"]) + 2 >= horizon:
                        saw_near = True
        self.assertTrue(saw)
        self.assertTrue(saw_near)

    def test_explicit_near_horizon_candidate_witnesses(self):
        witnesses = (
            (97, 13, 15, 26),
            (487, 39, 41, 77),
            (1980, 99, 101, 198),
        )
        for k, d, e, target in witnesses:
            data = nonadjacent_candidate_overlap_cubic_contraction(k, d, e)
            self.assertIn(target, data["common_roots"])
            self.assertLessEqual(target, data["candidate_coalescence_horizon"])
            self.assertLess(data["right_base_cubic"], 2 * k * k)

    def test_high_scale_candidate_multiplicity_is_adjacent_only(self):
        saw_double = False
        saw_odd_single = False
        for k in range(6, 150):
            horizon = candidate_coalescence_horizon(k)
            for target in range(horizon + 1, k + 1):
                data = high_scale_candidate_channel_multiplicity(k, target)
                self.assertLessEqual(data["multiplicity"], 2)
                self.assertLessEqual(data["odd_multiplicity"], 1)
                if data["multiplicity"] == 2:
                    left, right = data["divisor_hits"]
                    self.assertEqual(right, left + 1)
                    saw_double = True
                if data["odd_multiplicity"] == 1:
                    saw_odd_single = True
        self.assertTrue(saw_double)
        self.assertTrue(saw_odd_single)

    def test_k14_adjacent_collision_remains_above_cubic_candidate_horizon(self):
        self.assertEqual(candidate_coalescence_horizon(14), 8)
        data = high_scale_candidate_channel_multiplicity(14, 9)
        self.assertEqual(data["divisor_hits"], (2, 3))
        self.assertEqual(data["multiplicity"], 2)
        self.assertEqual(data["odd_divisor_hits"], (3,))

    def test_actual_collision_has_exact_cubic_bound(self):
        self.assertEqual(actual_coalescence_horizon(97), 26)
        data = actual_divisor_root_collision(97, 9464, 13, 14)
        self.assertTrue(data["coalesces"])
        self.assertEqual(data["common_root"], 26)
        self.assertEqual(data["common_root"], data["actual_coalescence_horizon"])
        self.assertLess(data["common_root"] ** 3, 2 * 98**2)

    def test_actual_collision_bound_exhaustive_small_range(self):
        saw = False
        for k in range(2, 36):
            horizon = actual_coalescence_horizon(k)
            for n in range(k * k, (k + 1) * (k + 1)):
                owner: dict[int, int] = {}
                for divisor in range(2, min(n + 1, 2 * k + 12)):
                    root = actual_divisor_root(k, n, divisor)
                    if root in owner:
                        data = actual_divisor_root_collision(
                            k, n, owner[root], divisor
                        )
                        self.assertTrue(data["coalesces"])
                        self.assertLessEqual(root, horizon)
                        self.assertLess(root**3, 2 * (k + 1) ** 2)
                        saw = True
                    else:
                        owner[root] = divisor
        self.assertTrue(saw)

    def test_adjacent_collision_family_makes_cubic_constant_asymptotically_sharp(self):
        for m in range(2, 90):
            d = m
            e = m + 1
            target = 2 * m
            n = 4 * m * m * (m + 1)
            k = isqrt(n)
            self.assertEqual(n // e, target * target)
            self.assertEqual(n // d, (target + 1) ** 2 - 1)
            data = actual_divisor_root_collision(k, n, d, e)
            self.assertTrue(data["coalesces"])
            self.assertEqual(data["common_root"], target)
            self.assertEqual(m * (2 * n), (m + 1) * target**3)
            self.assertLessEqual(target, actual_coalescence_horizon(k))

    def test_high_scale_actual_roots_are_injective_in_total_divisor(self):
        saw_high = False
        for k in range(8, 55):
            samples = (
                k * k,
                k * k + k,
                (k + 1) * (k + 1) - 1,
            )
            divisors = tuple(range(2, 2 * k + 5))
            for n in samples:
                data = high_scale_actual_divisor_root_injectivity(k, n, divisors)
                high_roots = [
                    root
                    for root in data["roots_by_divisor"].values()
                    if root > data["actual_coalescence_horizon"]
                ]
                self.assertEqual(len(high_roots), len(set(high_roots)))
                saw_high |= bool(high_roots)
        self.assertTrue(saw_high)

    def test_candidate_and_actual_horizons_strictly_descend(self):
        for k in range(5, 2000):
            candidate = candidate_horizon_strict_descent(k)
            self.assertLess(candidate["horizon"], k)
        for k in range(4, 2000):
            actual = actual_horizon_strict_descent(k)
            self.assertLess(actual["horizon"], k)

    def test_actual_collision_horizon_chain_is_well_founded(self):
        for k in (4, 5, 14, 97, 631, 10_000, 10**9):
            chain = actual_collision_horizon_chain(k)
            self.assertEqual(chain[0], k)
            self.assertLess(chain[-1], 4)
            for left, right in zip(chain, chain[1:]):
                self.assertLess(right, left)
        self.assertLess(len(actual_collision_horizon_chain(10**18)), 20)

    def test_complete_basin_includes_lower_square_boundary(self):
        self.assertEqual(actual_divisor_root(5, 25, 3), isqrt(25 // 3))
        with self.assertRaises(ValueError):
            actual_divisor_root(5, 24, 3)

    def test_candidate_channel_is_boundary_based_not_exact_cofactor_window(self):
        data = divisor_root_channel(3, 3)
        self.assertEqual(data["base_root"], 1)
        self.assertEqual(data["candidates"], (1, 2))

    def test_validation(self):
        with self.assertRaises(ValueError):
            nonadjacent_candidate_overlap_cubic_contraction(13, 3, 4)
        with self.assertRaises(ValueError):
            high_scale_candidate_channel_multiplicity(14, 8)
        with self.assertRaises(ValueError):
            candidate_horizon_strict_descent(4)
        with self.assertRaises(ValueError):
            actual_horizon_strict_descent(3)
        with self.assertRaises(ValueError):
            divisor_root_channel(5, 1)
        with self.assertRaises(ValueError):
            actual_divisor_root_collision(10, 100, 3, 3)


if __name__ == "__main__":
    unittest.main()
