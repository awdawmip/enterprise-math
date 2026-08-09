import unittest

from enterprise_math.causal_bulk_residual import (
    bounded_associativity_check,
    bounded_homomorphism_check,
    bounded_left_recovery_is_unique,
    bounded_reachable_values,
    left_translation_collision_spectrum,
    left_translation_fibers,
    residual_candidates,
    residual_signature_under_bulk_law,
    same_bulk_fiber_is_future_safe_under_associative_extension,
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

    def test_non_cancellative_max_bulk_law_has_large_but_future_safe_residual_fiber(self):
        increments = (0, 1, 2, 3, 4, 5, 6, 7)
        fibers = left_translation_fibers(5, increments, max)
        self.assertEqual(fibers[5], (0, 1, 2, 3, 4, 5))
        self.assertEqual(residual_candidates(5, 5, increments, max), (0, 1, 2, 3, 4, 5))
        with self.assertRaises(ValueError):
            unique_residual(5, 5, increments, max)
        self.assertFalse(bounded_left_recovery_is_unique((5,), increments, max))
        self.assertTrue(bounded_associativity_check(increments, max))

        # Once bulk=5 has collapsed all increments <=5 to the same current max,
        # any later max-extension sees them identically.
        futures = (0, 2, 5, 6, 9)
        self.assertTrue(
            same_bulk_fiber_is_future_safe_under_associative_extension(
                5, 1, 4, futures, max
            )
        )
        spectrum = left_translation_collision_spectrum(5, increments, max, 3)
        # Six increments are swallowed into the same current total 5.
        self.assertEqual(spectrum[1], 8)
        self.assertEqual(spectrum[2], 15)
        self.assertEqual(spectrum[3], 20)

    def test_boolean_or_nonunique_residual_is_also_a_causal_collapse(self):
        combine = lambda left, right: bool(left or right)
        increments = (False, True)
        self.assertEqual(residual_candidates(True, True, increments, combine), increments)
        with self.assertRaises(ValueError):
            unique_residual(True, True, increments, combine)
        self.assertTrue(bounded_associativity_check(increments, combine))
        spectrum = left_translation_collision_spectrum(True, increments, combine, 2)
        self.assertEqual(spectrum, (1, 2, 1))

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
