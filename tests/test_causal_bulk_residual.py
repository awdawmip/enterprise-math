import unittest

from enterprise_math.causal_bulk_residual import (
    bounded_homomorphism_check,
    bounded_left_recovery_is_unique,
    bounded_reachable_values,
    residual_signature_under_bulk_law,
    unique_residual,
)


class CausalBulkResidualTests(unittest.TestCase):
    def test_integer_sum_residual_is_future_sum_without_using_subtraction_as_primitive(self):
        alphabet = (0, 1, 2)
        observation = lambda word: sum(word)
        combine = lambda bulk, increment: bulk + increment
        self.assertTrue(bounded_homomorphism_check(alphabet, 3, 3, observation, combine))
        reachable = bounded_reachable_values(alphabet, 3, observation)
        self.assertTrue(bounded_left_recovery_is_unique(reachable, reachable, combine))
        left = residual_signature_under_bulk_law(
            alphabet, (2, 1), 3, observation, combine
        )
        right = residual_signature_under_bulk_law(
            alphabet, (0,), 3, observation, combine
        )
        self.assertEqual(left, right)

    def test_word_length_is_another_bulk_law_with_one_structural_type(self):
        alphabet = ("A", "B")
        observation = len
        combine = lambda bulk, increment: bulk + increment
        self.assertTrue(bounded_homomorphism_check(alphabet, 3, 4, observation, combine))
        self.assertEqual(
            residual_signature_under_bulk_law(alphabet, ("A", "B"), 4, observation, combine),
            residual_signature_under_bulk_law(alphabet, (), 4, observation, combine),
        )

    def test_non_cancellative_max_bulk_law_has_nonunique_residual(self):
        # With max-composition, bulk=5,total=5 is compatible with many future
        # increments <=5.  The bulk value alone has erased which increment happened.
        with self.assertRaises(ValueError):
            unique_residual(5, 5, (0, 1, 2, 3, 4, 5), max)
        self.assertFalse(
            bounded_left_recovery_is_unique((5,), (0, 1, 2, 3, 4, 5), max)
        )

    def test_boolean_or_also_fails_unique_residual_after_true_bulk(self):
        combine = lambda left, right: bool(left or right)
        with self.assertRaises(ValueError):
            unique_residual(True, True, (False, True), combine)

    def test_bulk_law_must_match_actual_word_composition(self):
        alphabet = (0, 1)
        binary_code = lambda word: sum(bit << index for index, bit in enumerate(reversed(word)))
        # Plain integer addition is not the causal concatenation law for a binary
        # positional code, so the homomorphism gate correctly rejects it.
        self.assertFalse(bounded_homomorphism_check(alphabet, 2, 2, binary_code, lambda a, b: a + b))

    def test_unique_recovery_is_about_reachable_increment_values_not_all_mathematical_values(self):
        # Even if a global operation has collisions elsewhere, only increments that
        # the declared future can actually produce matter to the exact residual gate.
        combine = lambda bulk, increment: (bulk + increment) % 5
        reachable = (0, 1, 2)
        self.assertTrue(bounded_left_recovery_is_unique((0, 1, 2), reachable, combine))
        self.assertEqual(unique_residual(2, 4, reachable, combine), 2)


if __name__ == "__main__":
    unittest.main()
