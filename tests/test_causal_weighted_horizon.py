import unittest

from enterprise_math.causal_operation_language import same_partition
from enterprise_math.causal_weighted_future import budget_partitions
from enterprise_math.causal_weighted_horizon import (
    horizon_partition_is_ultimate,
    weighted_composition_horizon,
    weighted_window_certificate_is_sound,
    weighted_window_stability_certificate,
)


class CausalWeightedHorizonTests(unittest.TestCase):
    def test_one_budget_plateau_is_not_stability_when_generator_cost_exceeds_one(self):
        states = (0, 1, 2)
        observation = {0: 0, 1: 0, 2: 1}
        generators = {
            "g": {0: 0, 1: 2, 2: 2},
        }
        costs = {"g": 5}
        partitions = budget_partitions(states, observation, generators, costs, 5)
        for budget in range(1, 5):
            self.assertTrue(same_partition(partitions[budget], partitions[budget - 1]))
        self.assertFalse(same_partition(partitions[5], partitions[4]))
        self.assertFalse(
            weighted_window_stability_certificate(
                states, observation, generators, costs, budget=4
            )
        )

    def test_maximum_finite_distinguishing_cost_is_exact_weighted_horizon(self):
        states = (0, 1, 2, 3)
        observation = {0: 0, 1: 0, 2: 0, 3: 1}
        generators = {
            "g": {0: 0, 1: 0, 2: 1, 3: 0},
            "h": {0: 0, 1: 3, 2: 0, 3: 0},
        }
        costs = {"g": 2, "h": 5}
        self.assertEqual(
            weighted_composition_horizon(
                states, observation, generators, costs
            ),
            7,
        )
        self.assertTrue(
            horizon_partition_is_ultimate(
                states, observation, generators, costs
            )
        )

    def test_cmax_wide_constant_window_certifies_permanent_stability(self):
        states = (0, 1, 2, 3)
        observation = {0: 0, 1: 0, 2: 0, 3: 1}
        generators = {
            "g": {0: 0, 1: 0, 2: 1, 3: 0},
            "h": {0: 0, 1: 3, 2: 0, 3: 0},
        }
        costs = {"g": 2, "h": 5}
        # Ultimate state is reached at budget 7. A full Cmax=5 window has become
        # constant by budget 12, so P12=P7 is a sound stabilization certificate.
        self.assertTrue(
            weighted_window_stability_certificate(
                states, observation, generators, costs, budget=12
            )
        )
        self.assertTrue(
            weighted_window_certificate_is_sound(
                states, observation, generators, costs, budget=12
            )
        )

    def test_horizon_zero_when_current_observation_already_contains_all_future_distinction(self):
        states = (0, 1, 2)
        observation = {0: 0, 1: 1, 2: 2}
        generators = {"g": {0: 1, 1: 2, 2: 0}}
        costs = {"g": 9}
        self.assertEqual(
            weighted_composition_horizon(
                states, observation, generators, costs
            ),
            0,
        )
        self.assertTrue(
            horizon_partition_is_ultimate(
                states, observation, generators, costs
            )
        )


if __name__ == "__main__":
    unittest.main()
