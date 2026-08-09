import unittest

from enterprise_math.causal_boundary_pullback import (
    basin_pullback_cuts_from_sums,
    basin_pullback_intervals_from_sums,
    budget_basin_intervals,
    pullback_partition_matches_direct_signatures,
    reachable_additive_sums,
    square_growth,
)


class CausalBoundaryPullbackTests(unittest.TestCase):
    def test_square_growth_plus_one_carves_current_basin_from_future_boundary_backward(self):
        growth = square_growth(20)
        level = 4  # current basin [16,25), width 9
        generators = (1,)
        costs = (1,)

        self.assertEqual(budget_basin_intervals(growth, level, generators, costs, 0), ((16, 25),))
        self.assertEqual(
            budget_basin_intervals(growth, level, generators, costs, 1),
            ((16, 24), (24, 25)),
        )
        self.assertEqual(
            budget_basin_intervals(growth, level, generators, costs, 3),
            ((16, 22), (22, 23), (23, 24), (24, 25)),
        )
        self.assertEqual(
            basin_pullback_cuts_from_sums(growth, level, (0, 1, 2, 3)),
            (22, 23, 24),
        )

    def test_pullback_intervals_match_direct_future_signatures_for_nonlinear_growth(self):
        growth = square_growth(30)
        for level in range(1, 9):
            for budget in range(0, 8):
                self.assertTrue(
                    pullback_partition_matches_direct_signatures(
                        growth,
                        level,
                        generators=(1, 3),
                        costs=(2, 5),
                        budget=budget,
                    )
                )

    def test_large_future_can_pull_back_more_than_the_next_boundary(self):
        growth = square_growth(30)
        level = 2  # [4,9)
        future_sums = (0, 20)
        # 25-20=5 lies inside [4,9), so a boundary two levels ahead can matter.
        self.assertIn(5, basin_pullback_cuts_from_sums(growth, level, future_sums))
        intervals = basin_pullback_intervals_from_sums(growth, level, future_sums)
        self.assertEqual(intervals, ((4, 5), (5, 9)))

    def test_reachable_future_sums_are_actual_nonnegative_generator_combinations(self):
        sums = reachable_additive_sums((4, 7), (3, 5), budget=11)
        self.assertEqual(sums, (0, 4, 7, 8, 11, 12))

    def test_linear_growth_recovers_periodic_block_cut_pattern(self):
        growth = tuple(12 * level for level in range(20))
        level = 3
        sums = (0, 8, 16)
        # Boundary pullbacks of multiples of 12 create local cuts at remainder 4 and 8.
        self.assertEqual(
            tuple(cut - growth[level] for cut in basin_pullback_cuts_from_sums(growth, level, sums)),
            (4, 8),
        )

    def test_budget_api_requires_enough_future_headroom(self):
        growth = square_growth(5)
        with self.assertRaises(ValueError):
            budget_basin_intervals(
                growth,
                level=3,
                generators=(10,),
                costs=(1,),
                budget=1,
            )


if __name__ == "__main__":
    unittest.main()
