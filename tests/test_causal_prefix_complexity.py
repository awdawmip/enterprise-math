import unittest

from enterprise_math.causal_prefix_complexity import (
    continuation_complexity_profile,
    continuation_fiber_sizes,
    finite_type_complexity,
    future_collapse_spectrum,
    future_distinction_loss,
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

    def test_copy_constraint_requires_exponential_midpoint_continuation_capacity(self):
        alphabet = (0, 1)
        for half in range(1, 6):
            horizon = 2 * half

            def copy_observation(word, half=half):
                return word[:half] == word[half:]

            profile = continuation_complexity_profile(alphabet, horizon, copy_observation)
            # At the midpoint each different first half accepts a different unique
            # suffix, so all 2^half prefixes have distinct future signatures.
            self.assertEqual(profile[half], 2**half)
            self.assertGreaterEqual(finite_type_complexity(alphabet, horizon, copy_observation), 2**half)

    def test_parity_future_collapse_forgets_many_histories_exactly(self):
        alphabet = (0, 1)
        horizon = 6
        depth = 5
        observation = lambda word: sum(word) % 2
        sizes = continuation_fiber_sizes(alphabet, horizon, depth, observation)
        self.assertEqual(sizes, (16, 16))
        self.assertEqual(future_distinction_loss(alphabet, horizon, depth, observation), 30)
        spectrum = future_collapse_spectrum(alphabet, horizon, depth, observation, 3)
        self.assertEqual(spectrum[1], 32)
        self.assertEqual(spectrum[2], 2 * (16 * 15 // 2))
        self.assertEqual(spectrum[3], 2 * (16 * 15 * 14 // 6))

    def test_full_identity_future_collapse_has_no_higher_collisions(self):
        alphabet = (0, 1)
        horizon = 5
        depth = 5
        observation = lambda word: word
        self.assertEqual(continuation_fiber_sizes(alphabet, horizon, depth, observation), (1,) * 32)
        self.assertEqual(future_distinction_loss(alphabet, horizon, depth, observation), 0)
        spectrum = future_collapse_spectrum(alphabet, horizon, depth, observation, 3)
        self.assertEqual(spectrum[1], 32)
        self.assertEqual(spectrum[2], 0)
        self.assertEqual(spectrum[3], 0)

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
