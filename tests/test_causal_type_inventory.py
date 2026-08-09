import unittest

from enterprise_math.causal_type_inventory import (
    additive_type_observation,
    combine_inventories,
    inventory_size,
    same_identity_free_state,
    type_inventory,
)


class CausalTypeInventoryTests(unittest.TestCase):
    def test_identity_renaming_inside_types_changes_nothing(self):
        left = {"a": "tau0", "b": "tau0", "c": "tau1"}
        right = {"x": "tau0", "y": "tau1", "z": "tau0"}
        self.assertTrue(same_identity_free_state(left, right))
        self.assertEqual(type_inventory(left), {"tau0": 2, "tau1": 1})

    def test_different_type_multiplicity_is_future_relevant_in_general(self):
        left = {"a": "tau0", "b": "tau0"}
        right = {"x": "tau0", "y": "tau1"}
        self.assertFalse(same_identity_free_state(left, right))

    def test_disjoint_union_becomes_count_addition_shadow(self):
        combined = combine_inventories(
            {"tau0": 2, "tau1": 1},
            {"tau0": 3, "tau2": 4},
        )
        self.assertEqual(combined, {"tau0": 5, "tau1": 1, "tau2": 4})
        self.assertEqual(inventory_size(combined), 10)

    def test_additive_observation_factors_through_inventory(self):
        inventory = {"tau0": 2, "tau1": 3}
        responses = {"tau0": 7, "tau1": -2}
        self.assertEqual(additive_type_observation(inventory, responses), 8)

    def test_same_inventory_forces_same_every_additive_type_observation(self):
        left = {"a": "tau0", "b": "tau0", "c": "tau1"}
        right = {"x": "tau1", "y": "tau0", "z": "tau0"}
        inventory_left = type_inventory(left)
        inventory_right = type_inventory(right)
        self.assertEqual(inventory_left, inventory_right)
        for responses in (
            {"tau0": 1, "tau1": 0},
            {"tau0": 5, "tau1": 11},
            {"tau0": -3, "tau1": 4},
        ):
            self.assertEqual(
                additive_type_observation(inventory_left, responses),
                additive_type_observation(inventory_right, responses),
            )


if __name__ == "__main__":
    unittest.main()
