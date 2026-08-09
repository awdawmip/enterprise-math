import unittest

from enterprise_math.causal_completion_collapse import (
    collapse_is_idempotent_on_represented_range,
    completion_collapse,
    completion_root_index,
    exact_level_recovery,
    observable_is_order_embedding,
    plateau_level_classes,
)
from enterprise_math.lattice_geometry import a_ball_count
from enterprise_math.lego_partition_fiber import hidden_allocation_multiplicity


class CausalCompletionCollapseTests(unittest.TestCase):
    def test_perfect_square_growth_recovers_classical_integer_root_levels(self):
        capacities = tuple(level * level for level in range(8))
        self.assertTrue(observable_is_order_embedding(capacities))
        self.assertTrue(exact_level_recovery(capacities))
        self.assertEqual(completion_root_index(capacities, 20), 4)
        self.assertEqual(completion_collapse(capacities, 20), 16)
        self.assertTrue(collapse_is_idempotent_on_represented_range(capacities, 49))

    def test_a_p_ball_growth_is_a_causally_generated_p008_completion_sequence(self):
        for p in range(1, 5):
            capacities = tuple(a_ball_count(p, radius) for radius in range(7))
            self.assertTrue(observable_is_order_embedding(capacities))
            self.assertTrue(exact_level_recovery(capacities))
            self.assertTrue(collapse_is_idempotent_on_represented_range(capacities, capacities[-1]))

    def test_free_one_slot_configuration_count_cannot_recover_value_level(self):
        capacities = tuple(hidden_allocation_multiplicity(1, total) for total in range(8))
        self.assertEqual(capacities, (1,) * 8)
        self.assertFalse(observable_is_order_embedding(capacities))
        self.assertFalse(exact_level_recovery(capacities))
        self.assertEqual(plateau_level_classes(capacities), (tuple(range(8)),))
        # The largest represented level below capacity 1 is index 7, demonstrating
        # that configuration count has erased the distinct value levels.
        self.assertEqual(completion_root_index(capacities, 1), 7)

    def test_multi_slot_fiber_count_is_strict_in_total_and_can_embed_level(self):
        for slots in range(2, 6):
            capacities = tuple(
                hidden_allocation_multiplicity(slots, total)
                for total in range(8)
            )
            self.assertTrue(observable_is_order_embedding(capacities))
            self.assertTrue(exact_level_recovery(capacities))

    def test_plateau_is_a_real_observational_level_collapse(self):
        capacities = (1, 2, 2, 2, 5, 7, 7, 9)
        self.assertFalse(observable_is_order_embedding(capacities))
        self.assertEqual(
            plateau_level_classes(capacities),
            ((0,), (1, 2, 3), (4,), (5, 6), (7,)),
        )
        self.assertEqual(completion_root_index(capacities, 2), 3)
        self.assertEqual(completion_collapse(capacities, 6), 5)
        self.assertTrue(collapse_is_idempotent_on_represented_range(capacities, 9))


if __name__ == "__main__":
    unittest.main()
