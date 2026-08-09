import unittest

from enterprise_math.causal_operation_grade_filtration import grade_histogram_on_small_system
from enterprise_math.causal_precision_tree_operations import (
    one_level_safe_count_formula,
    precision_tree_levels,
    terminal_identity_tower_count,
    zero_grade_map_count_from_tower,
)
from enterprise_math.causal_semantic_grade import distinguishing_depth_matrix
from enterprise_math.causal_weighted_future import budget_partitions


class CausalPrecisionTreeOperationsTests(unittest.TestCase):
    def test_four_state_precision_tree_count_matches_exhaustive_grade_zero_histogram(self):
        states = (0, 1, 2, 3)
        observation = {0: 0, 1: 0, 2: 0, 3: 1}
        generators = {
            "g": {0: 0, 1: 0, 2: 1, 3: 0},
            "h": {0: 0, 1: 3, 2: 0, 3: 0},
        }
        costs = {"g": 2, "h": 5}
        partitions = budget_partitions(
            states, observation, generators, costs, 7
        )
        levels = precision_tree_levels(states, partitions)
        self.assertEqual(
            tuple(tuple(sorted(map(len, level))) for level in levels),
            ((1, 3), (1, 1, 2), (1, 1, 1, 1)),
        )

        recursive_count = zero_grade_map_count_from_tower(states, partitions)
        depth = distinguishing_depth_matrix(
            states, observation, generators, costs
        )
        exhaustive = grade_histogram_on_small_system(states, depth)[0]
        self.assertEqual(recursive_count, 64)
        self.assertEqual(recursive_count, exhaustive)

    def test_one_level_tower_reduces_to_safe_partition_formula(self):
        states = (0, 1, 2, 3, 4)
        partition = {0: 0, 1: 0, 2: 0, 3: 1, 4: 1}
        self.assertEqual(
            zero_grade_map_count_from_tower(states, (partition,)),
            one_level_safe_count_formula(states, partition),
        )
        self.assertEqual(
            one_level_safe_count_formula(states, partition),
            (3 ** 3 + 2 ** 3) * (3 ** 2 + 2 ** 2),
        )

    def test_discrete_only_tower_allows_every_raw_endomap(self):
        states = (0, 1, 2, 3)
        discrete = {state: state for state in states}
        self.assertEqual(
            zero_grade_map_count_from_tower(states, (discrete,)),
            terminal_identity_tower_count(states),
        )
        self.assertEqual(terminal_identity_tower_count(states), 4 ** 4)

    def test_repeated_budget_layers_do_not_change_tree_count(self):
        states = (0, 1, 2)
        coarse = {0: 0, 1: 0, 2: 1}
        fine = {0: 0, 1: 1, 2: 2}
        repeated = (coarse, coarse, coarse, fine, fine)
        compressed = (coarse, fine)
        self.assertEqual(
            zero_grade_map_count_from_tower(states, repeated),
            zero_grade_map_count_from_tower(states, compressed),
        )


if __name__ == "__main__":
    unittest.main()
