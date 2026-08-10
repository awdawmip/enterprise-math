import unittest

from enterprise_math.precision_task_greedy import (
    five_state_greedy_counterexample,
    greedy_order_by_symbol_depth,
)
from enterprise_math.precision_task_scheduling import (
    optimal_order_by_symbol_depth,
    order_profile,
)


class PrecisionTaskGreedyTests(unittest.TestCase):
    def test_cheapest_next_greedy_can_be_strictly_suboptimal(self) -> None:
        states, tasks = five_state_greedy_counterexample()
        greedy = greedy_order_by_symbol_depth(states, tasks, base=2)
        optimal = optimal_order_by_symbol_depth(states, tasks, base=2)

        self.assertIn(greedy["order"][0], ("A", "B"))
        self.assertEqual(greedy["total_symbol_depth"], 3)
        self.assertEqual(optimal["minimum_symbol_depth"], 2)
        self.assertEqual(optimal["order"][0], "C")

    def test_both_locally_cheapest_first_choices_are_bad(self) -> None:
        states, tasks = five_state_greedy_counterexample()
        for first, second in (("A", "B"), ("B", "A")):
            profile = order_profile(states, tasks, (first, second, "C"), base=2)
            self.assertEqual(profile["repair_depths"], (1, 1, 1))
            self.assertEqual(profile["total_symbol_depth"], 3)

    def test_expensive_first_task_makes_two_tasks_redundant(self) -> None:
        states, tasks = five_state_greedy_counterexample()
        for tail in (("A", "B"), ("B", "A")):
            profile = order_profile(states, tasks, ("C", *tail), base=2)
            self.assertEqual(profile["repair_depths"], (2, 0, 0))
            self.assertEqual(profile["total_symbol_depth"], 2)
            self.assertEqual(profile["depth_slack"], 0)


if __name__ == "__main__":
    unittest.main()
