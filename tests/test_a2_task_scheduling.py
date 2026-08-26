import unittest
from itertools import permutations

from enterprise_math.a2_task_scheduling import (
    five_state_greedy_counterexample,
    generator_number,
    greedy_order_by_symbol_depth,
    minimal_task_bases,
    normalize_schedule_codes,
    optimal_order_by_symbol_depth,
    order_profile,
    task_dependency_closure,
)


class A2TaskSchedulingTests(unittest.TestCase):
    def test_greedy_cheapest_next_can_be_globally_suboptimal(self):
        states, tasks = five_state_greedy_counterexample()
        greedy = greedy_order_by_symbol_depth(states, tasks, 2)
        optimal = optimal_order_by_symbol_depth(states, tasks, 2)
        self.assertEqual(greedy["total_symbol_depth"], 3)
        self.assertEqual(optimal["minimum_symbol_depth"], 2)
        self.assertEqual(optimal["positive_cost_generators"], ("C",))

    def test_same_final_precision_can_have_different_order_cost(self):
        states = (0, 1, 2, 3)
        tasks = {
            "A": {0: 0, 1: 0, 2: 0, 3: 1},
            "B": {0: 0, 1: 0, 2: 1, 3: 1},
            "C": {0: 0, 1: 1, 2: 0, 3: 1},
        }
        efficient = order_profile(states, tasks, ("B", "C", "A"), 2)
        wasteful = order_profile(states, tasks, ("C", "A", "B"), 2)
        self.assertEqual(efficient["final_joint_class_count"], 4)
        self.assertEqual(wasteful["final_joint_class_count"], 4)
        self.assertEqual(efficient["repair_factors"], (2, 2, 1))
        self.assertEqual(wasteful["repair_factors"], (2, 2, 2))
        self.assertEqual(efficient["total_symbol_depth"], 2)
        self.assertEqual(wasteful["total_symbol_depth"], 3)

    def test_slack_decomposes_into_radix_and_incidence_parts(self):
        states, tasks = five_state_greedy_counterexample()
        profile = order_profile(states, tasks, ("A", "C", "B"), 2)
        self.assertEqual(
            profile["total_depth_slack"],
            profile["radix_packing_slack"] + profile["incidence_capacity_slack"],
        )
        self.assertGreaterEqual(profile["radix_packing_slack"], 0)
        self.assertGreaterEqual(profile["incidence_capacity_slack"], 0)

    def test_dependency_closure_is_not_a_dimension_theory(self):
        states = (0, 1, 2, 3)
        tasks = {
            "A": {0: 0, 1: 0, 2: 1, 3: 1},
            "B": {0: 0, 1: 1, 2: 0, 3: 1},
            "C": {0: (0, 0), 1: (0, 1), 2: (1, 0), 3: (1, 1)},
        }
        self.assertEqual(task_dependency_closure(states, tasks, ("C",)), frozenset(tasks))
        self.assertEqual(task_dependency_closure(states, tasks, ("A", "B")), frozenset(tasks))
        bases = set(minimal_task_bases(states, tasks))
        self.assertIn(frozenset({"C"}), bases)
        self.assertIn(frozenset({"A", "B"}), bases)
        self.assertEqual(generator_number(states, tasks), 1)

    def test_two_stage_normalization_preserves_joint_semantics(self):
        states, tasks = five_state_greedy_counterexample()
        for order in permutations(tasks):
            data = normalize_schedule_codes(states, tasks, order, 2)
            self.assertEqual(
                len(set(data["packed_codes"].values())),
                data["final_joint_class_count"],
            )
            self.assertEqual(
                len(set(data["normalized_codes"].values())),
                data["final_joint_class_count"],
            )
            self.assertLessEqual(
                len(data["realized_packed_codes"]),
                data["product_capacity"],
            )

    def test_optimal_schedule_reaches_final_lower_bound_on_counterexample(self):
        states, tasks = five_state_greedy_counterexample()
        optimal = optimal_order_by_symbol_depth(states, tasks, 2)
        self.assertEqual(optimal["minimum_symbol_depth"], optimal["final_state_depth"])
        self.assertEqual(optimal["total_depth_slack"], 0)


if __name__ == "__main__":
    unittest.main()
