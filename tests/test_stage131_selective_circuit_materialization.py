import unittest
from fractions import Fraction

from enterprise_math.stage131_horn_hyperedge_presentation import balanced_binary_and_tree
from enterprise_math.stage131_selective_circuit_materialization import (
    available_circuit_count_under_fan_in,
    maximum_exact_base_depth_under_fan_in,
    maximum_round_saving_under_fan_in,
    minimum_width_circuit_count_at_depth,
    optimal_premise_literal_budget_plan,
    optimal_unit_rule_budget_plan,
    per_circuit_benefit,
    rooted_circuit_minimal_premises_form_antichain,
    rooted_circuit_types,
)
from enterprise_math.stage131_rooted_circuit_table_explosion import rooted_circuit_count


class Stage131SelectiveCircuitMaterializationTests(unittest.TestCase):
    def test_minimum_width_depth_d_count_is_two_to_d_minus_one(self):
        for host_height in range(1, 8):
            types = rooted_circuit_types(host_height)
            for depth in range(1, host_height + 1):
                expected = 1 << (depth - 1)
                self.assertEqual(minimum_width_circuit_count_at_depth(depth), expected)
                self.assertEqual(types[(depth + 1, depth)], expected)

    def test_fan_in_cap_bounds_exact_base_depth_and_saving(self):
        for height in range(1, 10):
            for width in range(1, (1 << min(height, 5)) + 2):
                depth = maximum_exact_base_depth_under_fan_in(height, width)
                expected_depth = 0 if width < 2 else min(height, width - 1)
                self.assertEqual(depth, expected_depth)
                self.assertEqual(
                    maximum_round_saving_under_fan_in(height, width),
                    max(0, expected_depth - 1),
                )

    def test_width_six_already_allows_depth_five_high_speedup_circuits(self):
        height = 5
        types = rooted_circuit_types(height)
        self.assertEqual(types[(6, 5)], 16)
        self.assertEqual(maximum_exact_base_depth_under_fan_in(height, 6), 5)
        self.assertEqual(maximum_round_saving_under_fan_in(height, 6), 4)
        self.assertGreaterEqual(available_circuit_count_under_fan_in(height, 6), 16)

    def test_uniform_unit_rule_budget_selects_deepest_narrowest_tie_class_first(self):
        plan = optimal_unit_rule_budget_plan(5, 10)
        self.assertEqual(plan.selected_circuits, 10)
        self.assertEqual(plan.total_rule_storage, 10)
        self.assertEqual(plan.total_premise_literal_storage, 60)
        self.assertEqual(plan.gross_weighted_round_saving, 40)
        self.assertEqual(plan.max_selected_fan_in, 6)
        self.assertEqual(len(plan.selected), 1)
        chosen = plan.selected[0]
        self.assertEqual((chosen.premise_width, chosen.base_depth), (6, 5))
        self.assertEqual(chosen.selected_count, 10)
        self.assertEqual(chosen.benefit_per_circuit, 4)

    def test_fan_in_cap_changes_best_unit_rule_depth(self):
        plan = optimal_unit_rule_budget_plan(5, 5, max_fan_in=5)
        self.assertEqual(plan.selected_circuits, 5)
        self.assertEqual(plan.max_selected_fan_in, 5)
        self.assertEqual(plan.gross_weighted_round_saving, 15)
        self.assertTrue(all(item.base_depth == 4 for item in plan.selected))

    def test_premise_literal_knapsack_prefers_depth_five_width_six_under_uniform_workload(self):
        plan = optimal_premise_literal_budget_plan(5, 60)
        self.assertEqual(plan.total_premise_literal_storage, 60)
        self.assertEqual(plan.selected_circuits, 10)
        self.assertEqual(plan.gross_weighted_round_saving, 40)
        self.assertEqual(plan.max_selected_fan_in, 6)
        self.assertEqual(
            tuple((item.premise_width, item.base_depth, item.selected_count) for item in plan.selected),
            ((6, 5, 10),),
        )

    def test_type_frequency_can_reverse_uniform_selection_priority(self):
        types = rooted_circuit_types(4)
        frequencies = {key: Fraction(0) for key in types}
        frequencies[(3, 2)] = 100
        frequencies[(5, 4)] = 1
        plan = optimal_unit_rule_budget_plan(4, 2, frequencies=frequencies)
        self.assertEqual(plan.selected_circuits, 2)
        self.assertEqual(len(plan.selected), 1)
        item = plan.selected[0]
        self.assertEqual((item.premise_width, item.base_depth), (3, 2))
        self.assertEqual(item.selected_count, 2)
        self.assertEqual(item.benefit_per_circuit, 100)

    def test_uniform_type_counts_sum_to_complete_rooted_circuit_table(self):
        for height in range(1, 9):
            self.assertEqual(sum(rooted_circuit_types(height).values()), rooted_circuit_count(height))

    def test_distinct_minimal_rooted_premises_form_antichain_on_explicit_small_trees(self):
        for height in range(1, 5):
            tree = balanced_binary_and_tree(height)
            self.assertTrue(rooted_circuit_minimal_premises_form_antichain(tree, tree.root))

    def test_per_circuit_benefit_is_frequency_times_saved_rounds(self):
        self.assertEqual(per_circuit_benefit((6, 5), Fraction(3, 2)), 6)
        self.assertEqual(per_circuit_benefit((2, 1), 100), 0)

    def test_available_count_under_fan_in_is_monotone(self):
        height = 6
        counts = [available_circuit_count_under_fan_in(height, width) for width in range(2, 20)]
        self.assertTrue(all(left <= right for left, right in zip(counts, counts[1:])))

    def test_validation(self):
        with self.assertRaises(ValueError):
            optimal_unit_rule_budget_plan(5, 0)
        with self.assertRaises(ValueError):
            optimal_premise_literal_budget_plan(5, 0)
        with self.assertRaises(ValueError):
            maximum_exact_base_depth_under_fan_in(5, 0)


if __name__ == "__main__":
    unittest.main()
