import unittest

from enterprise_math.causal_recursive_join import kernel_is_associative
from enterprise_math.causal_weighted_context_refinement import (
    compile_weighted_contextual_kernel,
    induced_weighted_type_kernel,
    stable_weighted_contextual_types,
)


class CausalWeightedContextRefinementTests(unittest.TestCase):
    def test_grade_channel_can_force_finer_types_than_value_observation(self):
        states = (0, 1, 2, 3)
        observations = {state: state % 2 for state in states}
        # Base-4 residue join with exact local carry grade.
        raw_kernel = {
            (left, right, (left + right) % 4, (left + right) // 4): 1
            for left in states
            for right in states
        }
        self.assertTrue(kernel_is_associative(states, raw_kernel))
        classes, induced, _ = compile_weighted_contextual_kernel(
            states, observations, raw_kernel
        )
        # Parity alone would identify 0~2 and 1~3, but future carry grades can
        # distinguish those residues, so all four raw states remain necessary.
        self.assertEqual(len(set(classes.values())), 4)
        self.assertTrue(kernel_is_associative(tuple(sorted(set(classes.values()))), induced))

    def test_without_grade_observation_parity_can_remain_two_types(self):
        states = (0, 1, 2, 3)
        observations = {state: state % 2 for state in states}
        raw_kernel = {
            (left, right, (left + right) % 4, 0): 1
            for left in states
            for right in states
        }
        classes, induced, _ = compile_weighted_contextual_kernel(
            states, observations, raw_kernel
        )
        self.assertEqual(len(set(classes.values())), 2)
        self.assertTrue(kernel_is_associative(tuple(sorted(set(classes.values()))), induced))

    def test_duplicate_raw_identities_with_same_future_join_profile_collapse(self):
        states = ("a0", "a1")
        observations = {"a0": 0, "a1": 0}
        # Every pair produces the same raw output a0 with no grade shift.
        raw_kernel = {
            (left, right, "a0", 0): 1
            for left in states
            for right in states
        }
        classes, induced, _ = compile_weighted_contextual_kernel(
            states, observations, raw_kernel
        )
        self.assertEqual(len(set(classes.values())), 1)
        self.assertEqual(induced, {(0, 0, 0, 0): 1})

    def test_unsafe_manual_partition_is_rejected_by_induced_kernel(self):
        states = (0, 1)
        # Same current observation, but pair grade distinguishes left raw state.
        raw_kernel = {
            (0, 0, 0, 0): 1,
            (0, 1, 1, 0): 1,
            (1, 0, 1, 1): 1,
            (1, 1, 0, 1): 1,
        }
        manual = {0: 0, 1: 0}
        with self.assertRaises(ValueError):
            induced_weighted_type_kernel(states, raw_kernel, manual)

        observations = {0: 0, 1: 0}
        stable, _ = stable_weighted_contextual_types(states, observations, raw_kernel)
        self.assertEqual(len(set(stable.values())), 2)


if __name__ == "__main__":
    unittest.main()
