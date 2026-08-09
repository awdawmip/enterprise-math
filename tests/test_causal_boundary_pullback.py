import unittest

from enterprise_math.causal_boundary_pullback import (
    basin_pullback_cuts_from_sums,
    basin_pullback_intervals_from_sums,
    budget_basin_intervals,
    pullback_partition_matches_direct_signatures,
    reachable_additive_sums,
    square_growth,
    unit_increment_continuation_type_count,
    unit_increment_formula_matches_pullback,
    unit_increment_full_revelation_budget,
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

    def test_square_growth_revelation_type_count_is_basin_width_limited_linear_budget(self):
        growth = square_growth(30)
        level = 4
        width = growth[level + 1] - growth[level]
        self.assertEqual(width, 9)
        for unit_cost in (1, 2, 5):
            self.assertEqual(
                unit_increment_full_revelation_budget(growth, level, unit_cost),
                unit_cost * (width - 1),
            )
            for budget in range(0, unit_cost * (width + 2)):
                self.assertEqual(
                    unit_increment_continuation_type_count(
                        growth, level, unit_cost, budget
                    ),
                    min(width, budget // unit_cost + 1),
                )
                self.assertTrue(
                    unit_increment_formula_matches_pullback(
                        growth, level, unit_cost, budget
                    )
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
        self.assertIn(5, basin_pullback_cuts_from_sums(growth, level, future_sums))
        intervals = basin_pullback_intervals_from_sums(growth, level, future_sums)
        self.assertEqual(intervals, ((4, 5), (5, 9)))

    def test_reachable_future_sums_are_actual_nonnegative_generator_combinations(self):
        sums = reachable_additive_sums((4, 7), (3, 5), budget=11)
        self.assertEqual(sums, (0, 4, 7, 8, 11, 12, 14, 15))

    def test_linear_growth_recovers_periodic_block_cut_pattern(self):
        growth = tuple(12 * level for level in range(20))
        level = 3
        sums = (0, 8, 16)
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

    def test_decreasing_next_width_blocks_the_closed_unit_formula_gate(self):
        growth = (0, 5, 8, 10)  # widths 5,3,2
        with self.assertRaises(ValueError):
            unit_increment_continuation_type_count(
                growth,
                level=0,
                unit_cost=1,
                budget=2,
            )


if __name__ == "__main__":
    unittest.main()
