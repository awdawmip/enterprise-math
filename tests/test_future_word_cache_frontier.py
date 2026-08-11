import unittest

from enterprise_math.future_word_cache_frontier import (
    frontier_cache_depths_closed_form,
    frontier_cache_depths_match_enumeration,
    frontier_is_sqrt_sparse,
    frontier_point_count_bound,
    frontier_round_counts,
)


class FutureWordCacheFrontierTests(unittest.TestCase):
    def test_horizon_eight_closed_form(self):
        self.assertEqual(frontier_cache_depths_closed_form(8), (1, 2, 3, 4, 8))
        self.assertEqual(frontier_round_counts(8), (8, 4, 3, 2, 1))

    def test_frontier_locations_are_independent_of_action_count(self):
        for horizon in range(1, 30):
            for action_count in (1, 2, 3, 5):
                self.assertTrue(
                    frontier_cache_depths_match_enumeration(action_count, horizon)
                )

    def test_sqrt_sparsity_through_large_prefix(self):
        for horizon in range(1, 1001):
            self.assertTrue(frontier_is_sqrt_sparse(horizon))
            self.assertLessEqual(
                len(frontier_cache_depths_closed_form(horizon)),
                frontier_point_count_bound(horizon),
            )

    def test_example_hundred_has_far_fewer_frontier_points_than_depth_choices(self):
        depths = frontier_cache_depths_closed_form(100)
        self.assertLessEqual(len(depths), 20)
        self.assertLess(len(depths), 100)
        self.assertEqual(depths[0], 1)
        self.assertEqual(depths[-1], 100)

    def test_validation(self):
        with self.assertRaises(ValueError):
            frontier_cache_depths_closed_form(0)
        with self.assertRaises(ValueError):
            frontier_point_count_bound(False)


if __name__ == "__main__":
    unittest.main()
