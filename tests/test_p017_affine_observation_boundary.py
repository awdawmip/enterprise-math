import unittest

from enterprise_math.p017_affine_observation_boundary import (
    affine_parity_lifts,
    affine_root_observation_partition,
    unbounded_affine_root_fiber_family,
)


class P017AffineObservationBoundaryTests(unittest.TestCase):
    def test_explicit_3_5_family_is_one_mod_30_progression(self):
        for scale in range(1, 20):
            data = unbounded_affine_root_fiber_family(scale)
            self.assertEqual(data["k"], 30 * scale + 16)
            self.assertEqual(data["lift_count"], scale)
            self.assertEqual(
                data["lifts"], tuple(23 + 30 * t for t in range(scale))
            )
            self.assertLessEqual(data["observation_count"], 8)
            self.assertGreaterEqual(data["max_fiber"], (scale + 7) // 8)

    def test_local_root_observation_has_at_most_eight_states(self):
        for k in range(20, 240):
            for a, b in ((3, 5), (3, 7), (5, 7), (3, 11)):
                if a * b >= k:
                    continue
                try:
                    data = affine_root_observation_partition(k, a, b)
                except ValueError:
                    continue
                self.assertLessEqual(data["lower_root_count"], 2)
                self.assertLessEqual(data["upper_root_count"], 2)
                self.assertLessEqual(data["cubic_root_count"], 2)
                self.assertLessEqual(data["observation_count"], 8)

    def test_large_family_has_large_single_observation_fiber(self):
        data = unbounded_affine_root_fiber_family(64)
        self.assertEqual(data["lift_count"], 64)
        self.assertGreaterEqual(data["max_fiber"], 8)

        # The actual finite fiber is usually far larger than the universal
        # 1/8 pigeonhole guarantee; this checkpoint makes the growth visible
        # without elevating the observed value into a theorem.
        larger = unbounded_affine_root_fiber_family(166)
        self.assertEqual(larger["lift_count"], 166)
        self.assertGreaterEqual(larger["max_fiber"], 21)

    def test_parity_lifts_are_exact_divisibility_lifts(self):
        k = 496
        lifts = affine_parity_lifts(k, 3, 5)
        center = k * (k + 1)
        for radius in lifts:
            self.assertEqual(radius % 2, 1)
            self.assertEqual((center - radius) % 3, 0)
            self.assertEqual((center + radius) % 5, 0)


if __name__ == "__main__":
    unittest.main()
