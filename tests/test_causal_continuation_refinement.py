import unittest

from enterprise_math.causal_continuation_refinement import (
    class_count,
    future_equivalent,
    initial_observation_partition,
    stable_continuation_types,
)


class CausalContinuationRefinementTests(unittest.TestCase):
    def test_equal_now_but_different_one_step_future_are_split(self):
        observations = {"a": 0, "b": 0, "x": 1, "y": 2}
        actions = {
            "step": {
                "a": "x",
                "b": "y",
                "x": "x",
                "y": "y",
            }
        }
        initial = initial_observation_partition(observations)
        self.assertEqual(initial["a"], initial["b"])
        stable, _ = stable_continuation_types(observations, actions)
        self.assertNotEqual(stable["a"], stable["b"])
        self.assertFalse(future_equivalent("a", "b", observations, actions))

    def test_truly_same_continuation_is_collapsed(self):
        observations = {"a": 0, "b": 0, "x": 1}
        actions = {
            "step": {
                "a": "x",
                "b": "x",
                "x": "x",
            }
        }
        stable, _ = stable_continuation_types(observations, actions)
        self.assertEqual(stable["a"], stable["b"])
        self.assertTrue(future_equivalent("a", "b", observations, actions))
        self.assertEqual(class_count(stable), 2)

    def test_difference_can_appear_only_after_two_steps(self):
        observations = {
            "a": 0,
            "b": 0,
            "a1": 0,
            "b1": 0,
            "x": 1,
            "y": 2,
        }
        actions = {
            "step": {
                "a": "a1",
                "b": "b1",
                "a1": "x",
                "b1": "y",
                "x": "x",
                "y": "y",
            }
        }
        stable, rounds = stable_continuation_types(observations, actions)
        self.assertNotEqual(stable["a"], stable["b"])
        self.assertGreaterEqual(rounds, 2)

    def test_multiple_actions_are_part_of_the_future_signature(self):
        observations = {"a": 0, "b": 0, "x": 1, "y": 2, "z": 3}
        actions = {
            "left": {"a": "x", "b": "x", "x": "x", "y": "y", "z": "z"},
            "right": {"a": "y", "b": "z", "x": "x", "y": "y", "z": "z"},
        }
        stable, _ = stable_continuation_types(observations, actions)
        self.assertNotEqual(stable["a"], stable["b"])

    def test_no_actions_reduces_to_current_observation_classes(self):
        observations = {"a": 0, "b": 0, "c": 1}
        stable, _ = stable_continuation_types(observations, {})
        initial = initial_observation_partition(observations)
        for left in observations:
            for right in observations:
                self.assertEqual(
                    stable[left] == stable[right],
                    initial[left] == initial[right],
                )


if __name__ == "__main__":
    unittest.main()
