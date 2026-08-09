import unittest

from enterprise_math.p018_channel_coalescence import (
    actual_collision_horizon_chain,
    actual_horizon_strict_descent,
    candidate_coalescence_horizon,
    candidate_horizon_strict_descent,
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
        # The known p=2,3 candidate collision is precisely the adjacent-label
        # exception.  Odd-label injectivity does not have this escape hatch.
        self.assertEqual(candidate_coalescence_horizon(14), 8)
        data = high_scale_candidate_channel_multiplicity(14, 9)
        self.assertEqual(data["divisor_hits"], (2, 3))
        self.assertEqual(data["multiplicity"], 2)
        self.assertEqual(data["odd_divisor_hits"], (3,))

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
        # The contraction is very fast even at a huge root scale.
        self.assertLess(len(actual_collision_horizon_chain(10**18)), 20)

    def test_validation(self):
        with self.assertRaises(ValueError):
            nonadjacent_candidate_overlap_cubic_contraction(13, 3, 4)
        with self.assertRaises(ValueError):
            high_scale_candidate_channel_multiplicity(14, 8)
        with self.assertRaises(ValueError):
            candidate_horizon_strict_descent(4)
        with self.assertRaises(ValueError):
            actual_horizon_strict_descent(3)


if __name__ == "__main__":
    unittest.main()
