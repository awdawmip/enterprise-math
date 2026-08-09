import unittest

from enterprise_math.causal_prefix_complexity import finite_type_complexity
from enterprise_math.causal_state_capacity import (
    exact_encoding_has_enough_states,
    minimum_nonnegative_code_ceiling,
    minimum_register_ceiling_profile,
    nonnegative_register_capacity,
)


class CausalStateCapacityTests(unittest.TestCase):
    def test_exact_nonnegative_encoding_needs_c_distinct_codes(self):
        for classes in range(1, 10):
            ceiling = minimum_nonnegative_code_ceiling(classes)
            self.assertEqual(ceiling, classes - 1)
            self.assertEqual(nonnegative_register_capacity(ceiling), classes)
            self.assertTrue(exact_encoding_has_enough_states(classes, classes))
            if classes > 1:
                self.assertFalse(exact_encoding_has_enough_states(classes, classes - 1))

    def test_parity_stays_bounded_even_when_horizon_grows(self):
        alphabet = (0, 1)
        ceilings = []
        for horizon in range(1, 8):
            classes = finite_type_complexity(
                alphabet,
                horizon,
                lambda word: sum(word) % 2,
            )
            ceilings.append(minimum_nonnegative_code_ceiling(classes))
        self.assertEqual(tuple(ceilings), (1, 1, 1, 1, 1, 1, 1))

    def test_integer_sum_has_linear_capacity_growth(self):
        alphabet = (0, 1)
        class_counts = tuple(
            finite_type_complexity(alphabet, horizon, lambda word: sum(word))
            for horizon in range(1, 7)
        )
        self.assertEqual(class_counts, (2, 3, 4, 5, 6, 7))
        self.assertEqual(minimum_register_ceiling_profile(class_counts), (1, 2, 3, 4, 5, 6))

    def test_full_binary_history_has_exponential_capacity_even_in_one_integer(self):
        alphabet = (0, 1)
        for horizon in range(1, 7):
            classes = finite_type_complexity(alphabet, horizon, lambda word: word)
            self.assertEqual(classes, 2**horizon)
            # Any injective nonnegative single-register representation therefore
            # needs a code range reaching at least 2^N-1.
            self.assertEqual(minimum_nonnegative_code_ceiling(classes), 2**horizon - 1)


if __name__ == "__main__":
    unittest.main()
