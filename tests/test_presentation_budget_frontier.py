import unittest
from fractions import Fraction

from enterprise_math.presentation_budget_frontier import (
    compare_state_dimensions_at_same_latency,
    frontier_points_from_horizon_formula,
    horizon_pareto_macro_depths,
    minimal_scalar_storage_for_execution_budget,
    pareto_depths_match_scanned_frontier,
    pareto_frontier_size_sqrt_bound,
    same_latency_storage_ratio,
)
from enterprise_math.presentation_storage_depth_pareto import (
    literal_macro_pareto_frontier,
)


class PresentationBudgetFrontierTests(unittest.TestCase):
    def test_horizon_twelve_depths_are_action_count_independent(self):
        expected = (1, 2, 3, 4, 6, 12)
        self.assertEqual(horizon_pareto_macro_depths(12), expected)
        for action_count in range(1, 8):
            self.assertTrue(pareto_depths_match_scanned_frontier(action_count, 12))
            self.assertEqual(
                tuple(point.macro_depth for point in literal_macro_pareto_frontier(action_count, 12)),
                expected,
            )

    def test_horizon_only_formula_matches_scanned_frontier_for_many_horizons_and_k(self):
        checked = 0
        for horizon in range(1, 80):
            depths = horizon_pareto_macro_depths(horizon)
            self.assertLessEqual(len(depths), pareto_frontier_size_sqrt_bound(horizon))
            for action_count in (1, 2, 3, 5):
                self.assertTrue(
                    pareto_depths_match_scanned_frontier(action_count, horizon)
                )
                checked += 1
        self.assertEqual(checked, 79 * 4)

    def test_frontier_formula_reconstructs_points(self):
        direct = literal_macro_pareto_frontier(3, 20, state_dimension=4)
        formula = frontier_points_from_horizon_formula(3, 20, state_dimension=4)
        self.assertEqual(direct, formula)

    def test_minimum_scalar_storage_for_latency_target(self):
        # k=2,h=12,R=2 -> d=6 -> 126 matrices.  A 4D matrix has16 scalars.
        self.assertEqual(
            minimal_scalar_storage_for_execution_budget(2, 12, 2, 4),
            126 * 16,
        )
        # Same latency in a 2D state costs one quarter as many scalars.
        self.assertEqual(
            minimal_scalar_storage_for_execution_budget(2, 12, 2, 2),
            126 * 4,
        )

    def test_same_latency_state_compression_has_exact_square_storage_ratio(self):
        self.assertEqual(same_latency_storage_ratio(4, 2), Fraction(1, 4))
        self.assertEqual(same_latency_storage_ratio(11, 2), Fraction(4, 121))

        comparison = compare_state_dimensions_at_same_latency(
            action_count=2,
            horizon=12,
            max_execution_blocks=2,
            larger_state_dimension=4,
            smaller_state_dimension=2,
        )
        self.assertEqual(comparison.macro_depth, 6)
        self.assertEqual(comparison.stored_rules, 126)
        self.assertEqual(comparison.larger_scalar_storage, 2016)
        self.assertEqual(comparison.smaller_scalar_storage, 504)
        self.assertEqual(comparison.exact_storage_ratio, Fraction(1, 4))
        self.assertEqual(comparison.scalar_storage_saved, 1512)

    def test_weighted_fan_dimension_change_would_reduce_same_latency_dense_storage_by_4_over_121(self):
        comparison = compare_state_dimensions_at_same_latency(
            action_count=2,
            horizon=12,
            max_execution_blocks=3,
            larger_state_dimension=11,
            smaller_state_dimension=2,
        )
        # R=3 -> d=4 ->30 rules.
        self.assertEqual(comparison.macro_depth, 4)
        self.assertEqual(comparison.stored_rules, 30)
        self.assertEqual(comparison.exact_storage_ratio, Fraction(4, 121))
        self.assertEqual(comparison.larger_scalar_storage, 30 * 121)
        self.assertEqual(comparison.smaller_scalar_storage, 30 * 4)

    def test_validation(self):
        with self.assertRaises(ValueError):
            horizon_pareto_macro_depths(0)
        with self.assertRaises(ValueError):
            same_latency_storage_ratio(2, 2)
        with self.assertRaises(ValueError):
            compare_state_dimensions_at_same_latency(2, 12, 2, 2, 4)


if __name__ == "__main__":
    unittest.main()
