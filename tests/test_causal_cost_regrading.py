import unittest

from enterprise_math.causal_cost_regrading import (
    costs_dominate,
    regrading_monotonicity,
    uniform_regrading_exact,
    uniformly_scaled_costs,
)
from enterprise_math.causal_operation_language import minimum_future_partition, same_partition
from enterprise_math.causal_weighted_future import budget_partitions


class CausalCostRegradingTests(unittest.TestCase):
    def setUp(self):
        self.states = (0, 1, 2, 3)
        self.observation = {0: 0, 1: 0, 2: 0, 3: 1}
        self.generators = {
            "g": {0: 0, 1: 0, 2: 1, 3: 0},
            "h": {0: 0, 1: 3, 2: 0, 3: 0},
        }
        self.costs = {"g": 2, "h": 5}

    def test_generatorwise_cost_increase_can_only_delay_revelation(self):
        upper = {"g": 7, "h": 9}
        self.assertTrue(costs_dominate(self.costs, upper))
        self.assertTrue(
            regrading_monotonicity(
                self.states,
                self.observation,
                self.generators,
                self.costs,
                upper,
                maximum_budget=20,
            )
        )

    def test_uniform_scaling_is_exact_integer_change_of_cost_unit(self):
        for multiplier in (1, 2, 3, 5):
            self.assertEqual(
                uniformly_scaled_costs(self.costs, multiplier),
                {label: multiplier * value for label, value in self.costs.items()},
            )
            self.assertTrue(
                uniform_regrading_exact(
                    self.states,
                    self.observation,
                    self.generators,
                    self.costs,
                    multiplier,
                    maximum_budget=40,
                )
            )

    def test_cost_assignments_change_budget_layers_but_not_eventual_state(self):
        cheap = {"g": 1, "h": 1}
        expensive = {"g": 7, "h": 11}
        cheap_layers = budget_partitions(
            self.states,
            self.observation,
            self.generators,
            cheap,
            20,
        )
        expensive_layers = budget_partitions(
            self.states,
            self.observation,
            self.generators,
            expensive,
            20,
        )
        self.assertFalse(same_partition(cheap_layers[2], expensive_layers[2]))
        ultimate = minimum_future_partition(
            self.states,
            self.observation,
            self.generators,
        )
        self.assertTrue(same_partition(cheap_layers[-1], ultimate))
        self.assertTrue(same_partition(expensive_layers[-1], ultimate))

    def test_nonuniform_regrading_need_not_be_uniform_time_rescaling(self):
        upper = {"g": 4, "h": 5}
        self.assertTrue(costs_dominate(self.costs, upper))
        self.assertNotEqual(
            upper["g"] * self.costs["h"],
            upper["h"] * self.costs["g"],
        )
        self.assertTrue(
            regrading_monotonicity(
                self.states,
                self.observation,
                self.generators,
                self.costs,
                upper,
                maximum_budget=20,
            )
        )


if __name__ == "__main__":
    unittest.main()
