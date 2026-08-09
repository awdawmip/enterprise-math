import unittest
from itertools import product

from enterprise_math.collision_tick_window import static_contact_tick_window
from enterprise_math.collision_trajectory_threshold import (
    minimum_sampled_chebyshev_separation,
    sampled_contact_exists_at_factor,
    sampled_trajectory_contact_threshold,
)


def brute_minimum(start, step, horizon=20):
    return min(
        max(
            abs(coordinate + tick * velocity)
            for coordinate, velocity in zip(start, step, strict=True)
        )
        for tick in range(horizon + 1)
    )


class CollisionTrajectoryThresholdTests(unittest.TestCase):
    def test_binary_search_minimum_matches_bounded_brute_force_on_small_2d_domain(self):
        starts = list(product(range(-4, 5, 2), repeat=2))
        steps = list(product(range(-2, 3), repeat=2))
        for start in starts:
            for step in steps:
                exact = minimum_sampled_chebyshev_separation(start, step)
                brute = brute_minimum(start, step)
                self.assertEqual(exact, brute, (start, step, exact, brute))

    def test_threshold_matches_direct_tick_window_for_all_small_factors(self):
        starts = ((1, 0), (3, -1), (-4, 2), (2, 2))
        steps = ((-2, 0), (-1, 1), (1, -1), (0, 0))
        for start in starts:
            for step in steps:
                for radius_sum in range(3):
                    threshold = sampled_trajectory_contact_threshold(
                        start, step, radius_sum
                    )
                    for factor in range(1, 8):
                        direct = static_contact_tick_window(
                            start, step, radius_sum, factor
                        ) is not None
                        self.assertEqual(
                            sampled_contact_exists_at_factor(threshold, factor),
                            direct,
                            (start, step, radius_sum, factor, threshold),
                        )

    def test_point_swap_static_contact_extinguishes_at_terminal_factor(self):
        threshold = sampled_trajectory_contact_threshold(
            start=(1, 0),
            step=(-2, 0),
            radius_sum=0,
        )
        self.assertEqual(threshold.minimum_center_separation, 1)
        self.assertEqual(threshold.minimum_primitive_clearance, 1)
        self.assertEqual(threshold.finest_sampled_contact_factor, 2)
        self.assertEqual(threshold.first_resolving_factor, 1)
        self.assertTrue(sampled_contact_exists_at_factor(threshold, 2))
        self.assertFalse(sampled_contact_exists_at_factor(threshold, 1))

    def test_same_endpoint_path_has_primitive_sampled_contact(self):
        threshold = sampled_trajectory_contact_threshold(
            start=(2, 0),
            step=(-1, 0),
            radius_sum=0,
        )
        self.assertEqual(threshold.minimum_center_separation, 0)
        self.assertEqual(threshold.minimum_primitive_clearance, 0)
        self.assertIsNone(threshold.finest_sampled_contact_factor)
        self.assertIsNone(threshold.first_resolving_factor)
        self.assertTrue(sampled_contact_exists_at_factor(threshold, 1))

    def test_radius_can_turn_positive_center_minimum_into_persistent_support_contact(self):
        threshold = sampled_trajectory_contact_threshold(
            start=(3, 1),
            step=(-2, 0),
            radius_sum=1,
        )
        self.assertEqual(threshold.minimum_center_separation, 1)
        self.assertEqual(threshold.minimum_primitive_clearance, 0)
        self.assertTrue(sampled_contact_exists_at_factor(threshold, 1))

    def test_stationary_path_threshold_is_current_chebyshev_clearance(self):
        threshold = sampled_trajectory_contact_threshold(
            start=(5, -3),
            step=(0, 0),
            radius_sum=2,
        )
        self.assertEqual(threshold.minimum_center_separation, 5)
        self.assertEqual(threshold.minimum_primitive_clearance, 3)
        self.assertEqual(threshold.finest_sampled_contact_factor, 4)
        self.assertEqual(threshold.first_resolving_factor, 3)

    def test_invalid_inputs_are_rejected(self):
        with self.assertRaises(ValueError):
            minimum_sampled_chebyshev_separation((), ())
        with self.assertRaises(ValueError):
            minimum_sampled_chebyshev_separation((0,), (0, 1))
        with self.assertRaises(ValueError):
            sampled_trajectory_contact_threshold((0,), (0,), -1)
        threshold = sampled_trajectory_contact_threshold((1,), (0,), 0)
        with self.assertRaises(ValueError):
            sampled_contact_exists_at_factor(threshold, 0)


if __name__ == "__main__":
    unittest.main()
