import unittest

from enterprise_math.presentation_budget_planner import (
    max_macro_depth_for_rule_budget,
    minimal_execution_blocks_for_rule_budget,
    minimal_execution_blocks_for_scalar_budget,
    minimal_macro_depth_for_execution_budget,
    minimal_rule_count_for_execution_budget,
    pareto_macro_depth_for_rule_budget,
    plan_for_execution_budget,
    plan_for_rule_budget,
    plan_for_scalar_budget,
    state_compression_execution_gain,
)
from enterprise_math.presentation_storage_depth_pareto import (
    literal_macro_rule_count,
    macro_execution_blocks,
)


class PresentationBudgetPlannerTests(unittest.TestCase):
    def test_execution_budget_inverse_formula(self):
        expected = {
            12: (1, 2, 12),
            6: (2, 6, 6),
            5: (3, 14, 4),
            4: (3, 14, 4),
            3: (4, 30, 3),
            2: (6, 126, 2),
            1: (12, 8190, 1),
        }
        for rounds, (depth, rules, achieved) in expected.items():
            plan = plan_for_execution_budget(2, 12, rounds)
            self.assertEqual(plan.macro_depth, depth)
            self.assertEqual(plan.stored_rules, rules)
            self.assertEqual(plan.achieved_execution_blocks, achieved)
            self.assertLessEqual(plan.achieved_execution_blocks, rounds)
            if depth > 1:
                self.assertGreater(macro_execution_blocks(12, depth - 1), rounds)

    def test_more_allowed_rounds_than_horizon_still_uses_generator_presentation(self):
        self.assertEqual(minimal_macro_depth_for_execution_budget(7, 100), 1)
        self.assertEqual(minimal_rule_count_for_execution_budget(3, 7, 100), 3)

    def test_rule_budget_planner_skips_dominated_depth_five(self):
        # d=5 (62 rules) is affordable under125, but d=4 (30 rules) has the same
        # three-block runtime and therefore Pareto-dominates it.
        self.assertEqual(max_macro_depth_for_rule_budget(2, 12, 125), 5)
        self.assertEqual(minimal_execution_blocks_for_rule_budget(2, 12, 125), 3)
        self.assertEqual(pareto_macro_depth_for_rule_budget(2, 12, 125), 4)
        plan = plan_for_rule_budget(2, 12, 125)
        self.assertEqual(plan.macro_depth, 4)
        self.assertEqual(plan.stored_rules, 30)
        self.assertEqual(plan.achieved_execution_blocks, 3)
        self.assertEqual(plan.unused_rule_budget, 95)

    def test_rule_budget_thresholds_hit_frontier_points(self):
        cases = (
            (2, 1, 2, 12),
            (6, 2, 6, 6),
            (14, 3, 14, 4),
            (30, 4, 30, 3),
            (62, 4, 30, 3),
            (125, 4, 30, 3),
            (126, 6, 126, 2),
            (8190, 12, 8190, 1),
            (10000, 12, 8190, 1),
        )
        for budget, depth, stored, rounds in cases:
            plan = plan_for_rule_budget(2, 12, budget)
            self.assertEqual(
                (plan.macro_depth, plan.stored_rules, plan.achieved_execution_blocks),
                (depth, stored, rounds),
            )

    def test_inverse_planners_match_bruteforce_for_small_parameter_grid(self):
        checked = 0
        for action_count in range(1, 5):
            for horizon in range(1, 13):
                # Execution-budget problem: minimize rule storage subject to
                # execution blocks <= R.
                for rounds in range(1, horizon + 3):
                    candidates = [
                        depth
                        for depth in range(1, horizon + 1)
                        if macro_execution_blocks(horizon, depth) <= rounds
                    ]
                    brute_depth = min(
                        candidates,
                        key=lambda depth: literal_macro_rule_count(action_count, depth),
                    )
                    self.assertEqual(
                        minimal_macro_depth_for_execution_budget(horizon, rounds),
                        brute_depth,
                    )
                    checked += 1

                maximum_rules = literal_macro_rule_count(action_count, horizon)
                # Sample every exact frontier threshold and several in-between
                # budgets rather than every enormous integer budget.
                budgets = {action_count, maximum_rules}
                for depth in range(1, horizon + 1):
                    value = literal_macro_rule_count(action_count, depth)
                    budgets.add(value)
                    if value > action_count:
                        budgets.add(value - 1)
                for budget in sorted(budgets):
                    if budget < action_count:
                        continue
                    affordable = [
                        depth
                        for depth in range(1, horizon + 1)
                        if literal_macro_rule_count(action_count, depth) <= budget
                    ]
                    best_rounds = min(
                        macro_execution_blocks(horizon, depth)
                        for depth in affordable
                    )
                    brute_depth = min(
                        depth
                        for depth in affordable
                        if macro_execution_blocks(horizon, depth) == best_rounds
                    )
                    plan = plan_for_rule_budget(action_count, horizon, budget)
                    self.assertEqual(plan.macro_depth, brute_depth)
                    self.assertEqual(plan.achieved_execution_blocks, best_rounds)
                    checked += 1
        self.assertGreater(checked, 1000)

    def test_state_compression_can_buy_an_extra_execution_round_under_same_scalar_budget(self):
        large, small = state_compression_execution_gain(
            action_count=2,
            horizon=12,
            scalar_budget=1000,
            larger_state_dimension=4,
            smaller_state_dimension=2,
        )
        self.assertEqual(large.macro_depth, 4)
        self.assertEqual(large.achieved_execution_blocks, 3)
        self.assertEqual(large.stored_transition_scalars, 30 * 16)
        self.assertEqual(small.macro_depth, 6)
        self.assertEqual(small.achieved_execution_blocks, 2)
        self.assertEqual(small.stored_transition_scalars, 126 * 4)
        self.assertLess(small.achieved_execution_blocks, large.achieved_execution_blocks)

    def test_scalar_budget_minimum_execution_matches_rule_budget_after_matrix_cost(self):
        # 4-dimensional matrices cost16 scalars/rule; 1000 scalars means a
        # rule budget of62, whose Pareto plan is depth4 / three execution blocks.
        self.assertEqual(
            minimal_execution_blocks_for_scalar_budget(2, 12, 4, 1000),
            3,
        )
        self.assertEqual(plan_for_scalar_budget(2, 12, 4, 1000).macro_depth, 4)

    def test_validation(self):
        with self.assertRaises(ValueError):
            plan_for_rule_budget(2, 12, 1)
        with self.assertRaises(ValueError):
            plan_for_scalar_budget(2, 12, 4, 16)
        with self.assertRaises(ValueError):
            state_compression_execution_gain(2, 12, 1000, 2, 4)


if __name__ == "__main__":
    unittest.main()
