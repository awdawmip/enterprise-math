import unittest
from itertools import product

from enterprise_math.causal_close_packed_stacking import (
    actions_from_stacking,
    fcc_stacking,
    fixed_initial_stacking_count,
    global_shift_preserves_continuation,
    hcp_stacking,
    relative_steps,
    stacking_bijection_check,
    stacking_from_actions,
)


class CausalClosePackedStackingTests(unittest.TestCase):
    def test_repeated_f_is_fcc_abc_period_three(self):
        layers = fcc_stacking(12)
        self.assertEqual(layers, (0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 2))
        self.assertEqual(set(relative_steps(layers)), {1})

    def test_repeated_h_is_hcp_ab_period_two(self):
        layers = hcp_stacking(12)
        self.assertEqual(layers, (0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1))
        self.assertEqual(relative_steps(layers), (1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1))

    def test_action_words_biject_with_fixed_initial_close_packed_stackings(self):
        for layer_count in range(2, 9):
            seen = set()
            for actions in product(("F", "H"), repeat=layer_count - 2):
                actions = tuple(actions)
                self.assertTrue(stacking_bijection_check(0, 1, actions))
                layers = stacking_from_actions(0, 1, actions)
                self.assertEqual(actions_from_stacking(layers), actions)
                seen.add(layers)
            self.assertEqual(len(seen), fixed_initial_stacking_count(layer_count))

    def test_global_registry_phase_is_not_part_of_relative_continuation_state(self):
        layers = stacking_from_actions(0, 1, ("F", "H", "H", "F", "F"))
        for shift in (-5, -1, 0, 1, 2, 7):
            self.assertTrue(global_shift_preserves_continuation(layers, shift))

    def test_every_generated_sequence_respects_adjacent_registry_exclusion(self):
        for actions in product(("F", "H"), repeat=7):
            layers = stacking_from_actions(0, 1, tuple(actions))
            self.assertTrue(all(left != right for left, right in zip(layers, layers[1:])))

    def test_fcc_and_hcp_share_support_law_but_are_distinct_periodic_trajectories(self):
        fcc = fcc_stacking(10)
        hcp = hcp_stacking(10)
        self.assertNotEqual(fcc, hcp)
        self.assertEqual(actions_from_stacking(fcc), ("F",) * 8)
        self.assertEqual(actions_from_stacking(hcp), ("H",) * 8)


if __name__ == "__main__":
    unittest.main()
