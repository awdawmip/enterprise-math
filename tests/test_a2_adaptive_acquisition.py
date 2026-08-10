import unittest

from enterprise_math.a2_adaptive_acquisition import (
    class_count,
    eight_state_stage_gap_witness,
    four_bit_order_separation_witness,
    four_state_process_precision_witness,
    four_state_storage_gap_witness,
    language_safe_partition,
    optimal_adaptive_acquisition,
    optimal_fixed_order_interactive,
    optimal_stage_synchronous,
    power_capacity_tight_tree_exists,
    product_acquisition_system,
    queries_descend_to_target,
    query_signature_partition,
)


class A2AdaptiveAcquisitionTests(unittest.TestCase):
    def test_true_adaptive_order_separation_uses_four_binary_queries(self) -> None:
        states, target, queries = four_bit_order_separation_witness()
        adaptive = optimal_adaptive_acquisition(states, target, queries)
        ordered = optimal_fixed_order_interactive(states, target, queries)
        stage = optimal_stage_synchronous(states, target, queries)
        self.assertEqual(adaptive["target_storage_depth"], 1)
        self.assertEqual(adaptive["minimum_symbol_depth"], 3)
        self.assertEqual(adaptive["first_query"], "x0")
        self.assertEqual(ordered["minimum_symbol_depth"], 4)
        self.assertEqual(stage["minimum_symbol_depth"], 4)
        self.assertEqual(adaptive["language_safe_class_count"], 16)
        self.assertEqual(adaptive["transcript_class_count"], 8)
        self.assertEqual(adaptive["transcript_depth"], 3)
        self.assertEqual(adaptive["tree_packing_slack"], 0)
        self.assertEqual(adaptive["transcript_multiplicity_slack"], 2)

    def test_three_binary_queries_cannot_have_adaptive_vs_ordered_depth_gap(self) -> None:
        states = tuple(range(8))
        queries = {
            f"x{index}": {state: (state >> index) & 1 for state in states}
            for index in range(3)
        }
        for truth_mask in range(1 << len(states)):
            target = {state: (truth_mask >> state) & 1 for state in states}
            adaptive = optimal_adaptive_acquisition(states, target, queries)
            ordered = optimal_fixed_order_interactive(states, target, queries)
            self.assertEqual(
                adaptive["minimum_symbol_depth"],
                ordered["minimum_symbol_depth"],
            )

    def test_storage_gap_can_be_pure_tree_packing_defect(self) -> None:
        states, target, queries = four_state_storage_gap_witness()
        adaptive = optimal_adaptive_acquisition(states, target, queries)
        self.assertTrue(queries_descend_to_target(states, target, queries))
        self.assertEqual(adaptive["target_storage_depth"], 2)
        self.assertEqual(adaptive["transcript_depth"], 2)
        self.assertEqual(adaptive["minimum_symbol_depth"], 3)
        self.assertEqual(adaptive["tree_packing_slack"], 1)
        self.assertEqual(adaptive["transcript_multiplicity_slack"], 0)
        self.assertFalse(power_capacity_tight_tree_exists(states, target, queries))

    def test_balanced_target_descending_tree_hits_storage_lower_bound(self) -> None:
        states, target, queries = eight_state_stage_gap_witness()
        adaptive = optimal_adaptive_acquisition(states, target, queries)
        self.assertTrue(queries_descend_to_target(states, target, queries))
        self.assertTrue(power_capacity_tight_tree_exists(states, target, queries))
        self.assertEqual(adaptive["target_storage_depth"], 3)
        self.assertEqual(adaptive["minimum_symbol_depth"], 3)

    def test_fixed_interactive_and_stage_synchronous_are_distinct_models(self) -> None:
        states, target, queries = eight_state_stage_gap_witness()
        adaptive = optimal_adaptive_acquisition(states, target, queries)
        ordered = optimal_fixed_order_interactive(states, target, queries)
        stage = optimal_stage_synchronous(states, target, queries)
        self.assertEqual(adaptive["minimum_symbol_depth"], 3)
        self.assertEqual(ordered["minimum_symbol_depth"], 3)
        self.assertEqual(stage["minimum_symbol_depth"], 5)

    def test_process_precision_can_be_finer_than_answer_precision(self) -> None:
        states, target, queries = four_state_process_precision_witness()
        adaptive = optimal_adaptive_acquisition(states, target, queries)
        self.assertFalse(queries_descend_to_target(states, target, queries))
        self.assertEqual(class_count(states, target), 2)
        self.assertEqual(class_count(states, language_safe_partition(states, target, queries)), 4)
        self.assertEqual(adaptive["transcript_class_count"], 4)
        self.assertEqual(adaptive["proof_multiplicities"], (2, 2))
        self.assertEqual(adaptive["proof_repair_spectrum"], (4, 2))

    def test_partition_redundant_bundled_query_can_lower_acquisition_cost(self) -> None:
        states, target, queries = four_state_process_precision_witness()
        before_signature = query_signature_partition(states, queries)
        before = optimal_adaptive_acquisition(states, target, queries)
        enriched = {**queries, "TARGET": target}
        after_signature = query_signature_partition(states, enriched)
        after = optimal_adaptive_acquisition(states, target, enriched)
        self.assertEqual(
            class_count(states, before_signature),
            class_count(states, after_signature),
        )
        self.assertEqual(before["minimum_symbol_depth"], 2)
        self.assertEqual(after["minimum_symbol_depth"], 1)
        self.assertEqual(before["language_safe_class_count"], after["language_safe_class_count"])
        self.assertEqual(before["transcript_class_count"], 4)
        self.assertEqual(after["transcript_class_count"], 2)

    def test_adaptive_direct_sum_is_additive_on_component_local_queries(self) -> None:
        left = four_bit_order_separation_witness()
        right = four_state_storage_gap_witness()
        product = product_acquisition_system(*left, *right)
        left_cost = optimal_adaptive_acquisition(*left)["minimum_symbol_depth"]
        right_cost = optimal_adaptive_acquisition(*right)["minimum_symbol_depth"]
        product_cost = optimal_adaptive_acquisition(*product)["minimum_symbol_depth"]
        self.assertEqual((left_cost, right_cost, product_cost), (3, 3, 6))

    def test_general_cost_hierarchy_has_strict_witnesses(self) -> None:
        states, target, queries = four_state_storage_gap_witness()
        adaptive = optimal_adaptive_acquisition(states, target, queries)
        self.assertLess(adaptive["target_storage_depth"], adaptive["minimum_symbol_depth"])

        states, target, queries = four_bit_order_separation_witness()
        adaptive = optimal_adaptive_acquisition(states, target, queries)
        ordered = optimal_fixed_order_interactive(states, target, queries)
        self.assertLess(adaptive["minimum_symbol_depth"], ordered["minimum_symbol_depth"])

        states, target, queries = eight_state_stage_gap_witness()
        ordered = optimal_fixed_order_interactive(states, target, queries)
        stage = optimal_stage_synchronous(states, target, queries)
        self.assertLess(ordered["minimum_symbol_depth"], stage["minimum_symbol_depth"])


if __name__ == "__main__":
    unittest.main()
