import unittest

from enterprise_math.precision_scheduling_slack import (
    incidence_only_slack_witness,
    optimal_interface_overhead,
    radix_only_slack_witness,
    schedule_slack_decomposition,
)


class PrecisionSchedulingSlackTests(unittest.TestCase):
    def test_incidence_slack_can_exist_without_radix_slack(self) -> None:
        states, tasks = incidence_only_slack_witness()
        data = schedule_slack_decomposition(states, tasks, ("E", "F"), base=2)
        self.assertEqual(data["repair_factors"], (3, 3))
        self.assertEqual(data["product_capacity"], 9)
        self.assertEqual(data["final_joint_class_count"], 5)
        self.assertEqual(data["total_symbol_depth"], 4)
        self.assertEqual(data["product_depth"], 4)
        self.assertEqual(data["final_depth_lower_bound"], 3)
        self.assertEqual(data["radix_packing_slack"], 0)
        self.assertEqual(data["incidence_capacity_slack"], 1)
        self.assertEqual(data["total_slack"], 1)

    def test_radix_slack_can_exist_without_incidence_slack(self) -> None:
        states, tasks = radix_only_slack_witness()
        data = schedule_slack_decomposition(states, tasks, ("E", "F"), base=2)
        self.assertEqual(data["repair_factors"], (3, 5))
        self.assertEqual(data["product_capacity"], 15)
        self.assertEqual(data["final_joint_class_count"], 15)
        self.assertEqual(data["product_depth"], 4)
        self.assertEqual(data["total_symbol_depth"], 5)
        self.assertEqual(data["radix_packing_slack"], 1)
        self.assertEqual(data["incidence_capacity_slack"], 0)
        self.assertEqual(data["total_slack"], 1)

    def test_optimal_schedule_can_have_unavoidable_interface_overhead(self) -> None:
        states, tasks = incidence_only_slack_witness()
        data = optimal_interface_overhead(states, tasks, base=2)
        self.assertEqual(data["minimum_symbol_depth"], 4)
        self.assertEqual(data["final_depth_lower_bound"], 3)
        self.assertEqual(data["interface_overhead"], 1)

    def test_direct_bundled_task_removes_interface_overhead(self) -> None:
        states, tasks = incidence_only_slack_witness()
        joint = {
            state: (tasks["E"][state], tasks["F"][state])
            for state in states
        }
        bundled = optimal_interface_overhead(states, {"EF": joint}, base=2)
        self.assertEqual(bundled["final_joint_class_count"], 5)
        self.assertEqual(bundled["minimum_symbol_depth"], 3)
        self.assertEqual(bundled["interface_overhead"], 0)

    def test_two_slack_components_always_sum_exactly(self) -> None:
        for factory in (incidence_only_slack_witness, radix_only_slack_witness):
            states, tasks = factory()
            for order in (tuple(tasks), tuple(reversed(tuple(tasks)))):
                data = schedule_slack_decomposition(states, tasks, order, base=2)
                self.assertEqual(
                    data["total_slack"],
                    data["radix_packing_slack"] + data["incidence_capacity_slack"],
                )


if __name__ == "__main__":
    unittest.main()
