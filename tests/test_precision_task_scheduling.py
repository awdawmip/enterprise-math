import itertools
import unittest

from enterprise_math.precision_task_scheduling import (
    optimal_order_by_product_capacity,
    optimal_order_by_symbol_depth,
    order_profile,
)


class PrecisionTaskSchedulingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.states = (0, 1, 2, 3)
        self.tasks = {
            "A": {0: 0, 1: 0, 2: 0, 3: 1},
            "B": {0: 0, 1: 0, 2: 1, 3: 1},
            "C": {0: 0, 1: 1, 2: 0, 3: 1},
        }

    def test_same_final_precision_can_have_different_sequential_cost(self) -> None:
        efficient = order_profile(self.states, self.tasks, ("B", "C", "A"))
        wasteful = order_profile(self.states, self.tasks, ("C", "A", "B"))

        self.assertEqual(efficient["final_joint_class_count"], 4)
        self.assertEqual(wasteful["final_joint_class_count"], 4)

        self.assertEqual(efficient["repair_factors"], (2, 2, 1))
        self.assertEqual(efficient["product_capacity"], 4)
        self.assertEqual(efficient["total_symbol_depth"], 2)
        self.assertEqual(efficient["depth_slack"], 0)
        self.assertTrue(efficient["product_equality"])

        self.assertEqual(wasteful["repair_factors"], (2, 2, 2))
        self.assertEqual(wasteful["product_capacity"], 8)
        self.assertEqual(wasteful["total_symbol_depth"], 3)
        self.assertEqual(wasteful["depth_slack"], 1)
        self.assertFalse(wasteful["product_equality"])

    def test_dynamic_program_finds_global_depth_optimum(self) -> None:
        result = optimal_order_by_symbol_depth(self.states, self.tasks, base=2)
        exhaustive = [
            order_profile(self.states, self.tasks, order, base=2)
            for order in itertools.permutations(self.tasks)
        ]
        best = min(profile["total_symbol_depth"] for profile in exhaustive)
        self.assertEqual(result["minimum_symbol_depth"], best)
        self.assertEqual(result["total_symbol_depth"], 2)
        self.assertEqual(result["depth_slack"], 0)

    def test_dynamic_program_finds_global_product_optimum(self) -> None:
        result = optimal_order_by_product_capacity(self.states, self.tasks)
        exhaustive = [
            order_profile(self.states, self.tasks, order)
            for order in itertools.permutations(self.tasks)
        ]
        best = min(profile["product_capacity"] for profile in exhaustive)
        self.assertEqual(result["minimum_product_capacity"], best)
        self.assertEqual(result["product_capacity"], 4)
        self.assertEqual(result["product_slack"], 0)

    def test_final_depth_is_a_lower_bound_for_every_order(self) -> None:
        for order in itertools.permutations(self.tasks):
            profile = order_profile(self.states, self.tasks, order, base=2)
            self.assertGreaterEqual(
                profile["total_symbol_depth"],
                profile["final_depth_lower_bound"],
            )

    def test_product_equality_is_exact_uniform_branching_criterion(self) -> None:
        for order in itertools.permutations(self.tasks):
            profile = order_profile(self.states, self.tasks, order)
            self.assertEqual(
                profile["product_equality"],
                all(profile["uniform_branching"]),
            )


if __name__ == "__main__":
    unittest.main()
