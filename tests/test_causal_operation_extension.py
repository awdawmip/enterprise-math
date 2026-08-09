import unittest

from enterprise_math.causal_operation_extension import (
    apply_operation_word,
    extension_defect,
    extension_is_zero_cost,
    operation_coupling_depth,
    shortest_mixed_operation_witness,
    static_common_is_joint_safe,
    zero_cost_theorem_check,
)


class CausalOperationExtensionTests(unittest.TestCase):
    def setUp(self):
        self.states = (0, 1, 2, 3)
        self.observation = {0: 0, 1: 0, 2: 0, 3: 1}
        self.g = {"g": {0: 0, 1: 0, 2: 1, 3: 0}}
        self.h = {"h": {0: 0, 1: 3, 2: 0, 3: 0}}

    def test_zero_cost_extension_iff_added_generators_respect_current_minimum_state(self):
        identity = {"id": {state: state for state in self.states}}
        self.assertTrue(
            extension_is_zero_cost(
                self.states,
                self.observation,
                self.g,
                identity,
            )
        )
        self.assertTrue(
            zero_cost_theorem_check(
                self.states,
                self.observation,
                self.g,
                identity,
            )
        )

        self.assertFalse(
            extension_is_zero_cost(
                self.states,
                self.observation,
                self.g,
                self.h,
            )
        )
        self.assertTrue(
            zero_cost_theorem_check(
                self.states,
                self.observation,
                self.g,
                self.h,
            )
        )

    def test_extension_defect_records_new_classes_and_lost_collisions(self):
        extra, lost = extension_defect(
            self.states,
            self.observation,
            self.g,
            self.h,
            maximum_order=4,
        )
        self.assertEqual(extra, 2)
        # P_g has fibers (3,1); P_(g,h) is discrete. J1 stays 4, J2 loses 3,
        # J3 loses 1, J4 stays zero.
        self.assertEqual(lost, (0, 3, 1, 0))

    def test_static_common_refinement_can_fail_only_under_mixed_words(self):
        self.assertFalse(
            static_common_is_joint_safe(
                self.states,
                self.observation,
                self.g,
                self.h,
            )
        )
        witness = shortest_mixed_operation_witness(
            self.states,
            self.observation,
            self.g,
            self.h,
        )
        self.assertIsNotNone(witness)
        left, right, word = witness
        self.assertEqual(len(word), 2)
        self.assertIn("g", word)
        self.assertIn("h", word)
        joint = {**self.g, **self.h}
        final_left = apply_operation_word(left, word, joint)
        final_right = apply_operation_word(right, word, joint)
        self.assertNotEqual(
            self.observation[final_left],
            self.observation[final_right],
        )
        self.assertEqual(operation_coupling_depth(
            self.states,
            self.observation,
            self.g,
            self.h,
        ), 2)

    def test_no_dynamic_coupling_when_static_common_is_already_joint_safe(self):
        states = (0, 1, 2, 3)
        observation = {state: state % 2 for state in states}
        plus_two = {"p2": {state: (state + 2) % 4 for state in states}}
        flip_within_parity = {"f": {0: 2, 2: 0, 1: 3, 3: 1}}
        self.assertTrue(
            static_common_is_joint_safe(
                states,
                observation,
                plus_two,
                flip_within_parity,
            )
        )
        self.assertIsNone(
            shortest_mixed_operation_witness(
                states,
                observation,
                plus_two,
                flip_within_parity,
            )
        )
        self.assertIsNone(
            operation_coupling_depth(
                states,
                observation,
                plus_two,
                flip_within_parity,
            )
        )


if __name__ == "__main__":
    unittest.main()
