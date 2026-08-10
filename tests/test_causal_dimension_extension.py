import unittest

from enterprise_math.causal_dimension_extension import (
    cumulative_signature,
    old_to_new_transition_inventory,
    revelation_spectrum_for_transition,
    total_revelation_spectrum,
)


class CausalDimensionExtensionTests(unittest.TestCase):
    def test_replacing_observation_can_merge_while_cumulative_signature_cannot(self):
        states = ("a", "b", "c", "d")
        old = {"a": 0, "b": 0, "c": 1, "d": 1}
        new = {"a": "x", "b": "y", "c": "x", "d": "y"}

        inventory = old_to_new_transition_inventory(states, old, new)
        self.assertEqual(inventory[0].split_count, 2)
        self.assertEqual(inventory[1].split_count, 2)

        cumulative = cumulative_signature(states, old, new)
        self.assertNotEqual(cumulative["a"], cumulative["c"])
        self.assertNotEqual(cumulative["b"], cumulative["d"])

    def test_lambda9_style_240_to_128_112_revelation(self):
        transition = old_to_new_transition_inventory(
            tuple(range(240)),
            {state: "E8" for state in range(240)},
            {
                state: "stable" if state < 128 else "mixed"
                for state in range(240)
            },
        )["E8"]
        spectrum = revelation_spectrum_for_transition(transition, 3)
        self.assertEqual(spectrum[0], 0)
        self.assertEqual(spectrum[1], 128 * 112)
        self.assertEqual(spectrum[2], 1_705_984)

    def test_homogeneous_extension_has_zero_revelation(self):
        states = tuple(range(10))
        inventory = old_to_new_transition_inventory(
            states,
            {state: state % 2 for state in states},
            {state: (state % 2) + 10 for state in states},
        )
        self.assertTrue(all(item.is_homogeneous for item in inventory.values()))
        self.assertEqual(total_revelation_spectrum(inventory, 4), (0, 0, 0, 0))


if __name__ == "__main__":
    unittest.main()
