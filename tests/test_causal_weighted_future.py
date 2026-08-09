import unittest

from enterprise_math.causal_operation_language import minimum_future_partition, same_partition
from enterprise_math.causal_weighted_future import (
    budget_partition_matches_distinguishing_costs,
    budget_partitions,
    distinguishing_cost,
    distinguishing_cost_strong_triangle,
    eventual_partition_matches_unweighted_future,
    transport_cost,
)


class CausalWeightedFutureTests(unittest.TestCase):
    def test_transport_uses_cheaper_multistep_path_not_first_expensive_target_discovery(self):
        states = (0, 1, 2)
        generators = {
            "direct": {0: 2, 1: 1, 2: 2},
            "step": {0: 1, 1: 2, 2: 2},
        }
        costs = {"direct": 10, "step": 3}
        self.assertEqual(transport_cost(states, generators, costs, 0, 2), 6)

    def test_distinguishing_cost_uses_cheaper_multistep_future(self):
        states = (0, 1, 2, 3, 4, 5)
        observation = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 1}
        generators = {
            # Expensive one-step distinction: 0->5 while 1->0.
            "direct": {0: 5, 1: 0, 2: 2, 3: 3, 4: 4, 5: 5},
            # Cheap two-step distinction: (0,1)->(2,3)->(4,5).
            "step": {0: 2, 1: 3, 2: 4, 3: 5, 4: 4, 5: 5},
        }
        costs = {"direct": 11, "step": 3}
        self.assertEqual(
            distinguishing_cost(states, observation, generators, costs, 0, 1),
            6,
        )

    def test_budget_partition_is_exact_distinguishing_cost_cut(self):
        states = (0, 1, 2, 3)
        observation = {0: 0, 1: 0, 2: 0, 3: 1}
        generators = {
            "g": {0: 0, 1: 0, 2: 1, 3: 0},
            "h": {0: 0, 1: 3, 2: 0, 3: 0},
        }
        costs = {"g": 2, "h": 5}
        partitions = budget_partitions(states, observation, generators, costs, 12)
        for budget, partition in enumerate(partitions):
            self.assertTrue(
                budget_partition_matches_distinguishing_costs(
                    states,
                    observation,
                    generators,
                    costs,
                    budget,
                )
            )
            # Nested future budgets can only refine state.
            if budget:
                previous = partitions[budget - 1]
                for left in states:
                    for right in states:
                        if partition[left] == partition[right]:
                            self.assertEqual(previous[left], previous[right])

    def test_positive_cost_regrading_changes_revelation_depth_not_eventual_quotient(self):
        states = (0, 1, 2, 3)
        observation = {0: 0, 1: 0, 2: 0, 3: 1}
        generators = {
            "g": {0: 0, 1: 0, 2: 1, 3: 0},
            "h": {0: 0, 1: 3, 2: 0, 3: 0},
        }
        unweighted = minimum_future_partition(states, observation, generators)
        for costs in (
            {"g": 1, "h": 1},
            {"g": 2, "h": 5},
            {"g": 9, "h": 1},
            {"g": 7, "h": 11},
        ):
            self.assertTrue(
                eventual_partition_matches_unweighted_future(
                    states, observation, generators, costs
                )
            )
            # Independently compare to a budget beyond every finite pair distance.
            distances = [
                distinguishing_cost(states, observation, generators, costs, a, b)
                for a in states
                for b in states
            ]
            finite = [value for value in distances if value is not None]
            final = budget_partitions(states, observation, generators, costs, max(finite, default=0))[-1]
            self.assertTrue(same_partition(final, unweighted))

    def test_distinguishing_cost_has_integer_strong_triangle_law(self):
        states = (0, 1, 2, 3, 4)
        observation = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1}
        generators = {
            "a": {0: 1, 1: 2, 2: 3, 3: 4, 4: 4},
            "b": {0: 0, 1: 3, 2: 2, 3: 3, 4: 0},
        }
        costs = {"a": 2, "b": 7}
        self.assertTrue(
            distinguishing_cost_strong_triangle(
                states, observation, generators, costs
            )
        )

    def test_transport_and_distinguishability_are_distinct_shadows_of_same_operations(self):
        states = (0, 1, 2, 3)
        generators = {
            "move": {0: 1, 1: 2, 2: 3, 3: 3},
            "probe": {0: 0, 1: 3, 2: 2, 3: 3},
        }
        costs = {"move": 2, "probe": 1}
        observation = {0: 0, 1: 0, 2: 0, 3: 1}

        # Moving 0 to 2 requires two move steps.
        self.assertEqual(transport_cost(states, generators, costs, 0, 2), 4)
        # Yet 0 and 1 can be distinguished after one cheap probe: 0->0, 1->3.
        self.assertEqual(
            distinguishing_cost(states, observation, generators, costs, 0, 1),
            1,
        )
        self.assertNotEqual(
            transport_cost(states, generators, costs, 0, 2),
            distinguishing_cost(states, observation, generators, costs, 0, 1),
        )

    def test_permanently_future_equivalent_pair_has_infinite_distinguishing_cost(self):
        states = (0, 1, 2)
        observation = {0: 0, 1: 0, 2: 1}
        generators = {
            "g": {0: 0, 1: 1, 2: 2},
        }
        costs = {"g": 4}
        self.assertIsNone(
            distinguishing_cost(states, observation, generators, costs, 0, 1)
        )


if __name__ == "__main__":
    unittest.main()
