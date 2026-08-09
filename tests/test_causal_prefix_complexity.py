import unittest

from enterprise_math.causal_prefix_complexity import (
    continuation_complexity_profile,
    finite_type_complexity,
)


class CausalPrefixComplexityTests(unittest.TestCase):
    def test_parity_has_uniform_two_type_continuation_complexity(self):
        alphabet = (0, 1)
        for horizon in range(1, 8):
            observation = lambda word: sum(word) % 2
            profile = continuation_complexity_profile(alphabet, horizon, observation)
            self.assertLessEqual(max(profile), 2)
            self.assertEqual(finite_type_complexity(alphabet, horizon, observation), 2)

    def test_full_word_identity_has_exponentially_growing_type_count(self):
        alphabet = (0, 1)
        for horizon in range(1, 6):
            observation = lambda word: word
            profile = continuation_complexity_profile(alphabet, horizon, observation)
            self.assertEqual(profile[-1], 2**horizon)
            self.assertEqual(finite_type_complexity(alphabet, horizon, observation), 2**horizon)

    def test_integer_sum_has_unbounded_label_count_but_simple_accumulator_schema(self):
        alphabet = (0, 1)
        for horizon in range(1, 7):
            observation = lambda word: sum(word)
            profile = continuation_complexity_profile(alphabet, horizon, observation)
            # At depth d, prefixes are classified by their current number of ones.
            self.assertEqual(profile, tuple(depth + 1 for depth in range(horizon + 1)))
            self.assertEqual(finite_type_complexity(alphabet, horizon, observation), horizon + 1)

    def test_constant_observation_collapses_every_prefix_depth_to_one_type(self):
        alphabet = ("A", "B", "C")
        for horizon in range(0, 5):
            profile = continuation_complexity_profile(
                alphabet,
                horizon,
                lambda word: 0,
            )
            self.assertEqual(profile, tuple(1 for _ in range(horizon + 1)))


if __name__ == "__main__":
    unittest.main()
