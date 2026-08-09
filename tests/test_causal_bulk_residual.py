import unittest

from enterprise_math.causal_bulk_residual import (
    bounded_associativity_check,
    bounded_homomorphism_check,
    bounded_left_recovery_is_unique,
    bounded_reachable_values,
    bulk_extension_coarsens_residuals,
    collision_spectrum_nondecreasing_under_bulk_extension,
    compose_class_maps,
    left_translation_collision_spectrum,
    left_translation_fibers,
    residual_candidates,
    residual_resolution_map,
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
        left = residual_signature_under_bulk_law(alphabet, (2, 1), 3, observation, combine)
        right = residual_signature_under_bulk_law(alphabet, (0,), 3, observation, combine)
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

        futures = (0, 2, 5, 6, 9)
        self.assertTrue(
            same_bulk_fiber_is_future_safe_under_associative_extension(
                5, 1, 4, futures, max
            )
        )
        spectrum = left_translation_collision_spectrum(5, increments, max, 3)
        self.assertEqual(spectrum[1], 8)
        self.assertEqual(spectrum[2], 15)
        self.assertEqual(spectrum[3], 20)

    def test_max_bulk_accumulation_can_only_coarsen_residual_precision(self):
        increments = tuple(range(9))
        self.assertTrue(bulk_extension_coarsens_residuals(2, 5, increments, max))
        self.assertTrue(
            collision_spectrum_nondecreasing_under_bulk_extension(
                2, 5, increments, max, 4
            )
        )
        before = left_translation_collision_spectrum(2, increments, max, 2)
        after = left_translation_collision_spectrum(5, increments, max, 2)
        self.assertGreater(after[2], before[2])

    def test_residual_resolution_maps_compose_along_max_bulk_growth(self):
        increments = tuple(range(9))
        map_2_to_5 = residual_resolution_map(2, 5, increments, max)
        map_5_to_7 = residual_resolution_map(5, 7, increments, max)
        map_2_to_7 = residual_resolution_map(2, 7, increments, max)
        self.assertEqual(
            compose_class_maps(map_2_to_5, map_5_to_7),
            map_2_to_7,
        )

    def test_additive_bulk_keeps_residual_precision_exact_under_accumulation(self):
        increments = tuple(range(6))
        add = lambda left, right: left + right
        self.assertTrue(bulk_extension_coarsens_residuals(2, 4, increments, add))
        before = left_translation_collision_spectrum(2, increments, add, 3)
        after = left_translation_collision_spectrum(6, increments, add, 3)
        self.assertEqual(before, after)
        self.assertEqual(before[2], 0)
        resolution = residual_resolution_map(2, 6, increments, add)
        self.assertEqual(len(resolution), len(increments))

    def test_noncommutative_context_can_change_residual_partition_nonmonotonically(self):
        compose = lambda f, g: tuple(f[g[index]] for index in range(3))
        b = (0, 0, 1)
        u = (0, 2, 0)
        r = (0, 0, 0)
        r_prime = (0, 0, 1)
        increments = (r, r_prime)

        self.assertTrue(bounded_associativity_check((b, u, r, r_prime, compose(b, u)), compose))
        self.assertEqual(compose(b, r), compose(b, r_prime))
        new_bulk = compose(b, u)
        self.assertNotEqual(compose(new_bulk, r), compose(new_bulk, r_prime))
        self.assertFalse(bulk_extension_coarsens_residuals(b, u, increments, compose))
        with self.assertRaises(ValueError):
            residual_resolution_map(b, new_bulk, increments, compose)

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
        self.assertFalse(bounded_homomorphism_check(alphabet, 2, 2, binary_code, lambda a, b: a + b))

    def test_unique_recovery_is_about_reachable_increment_values_not_all_mathematical_values(self):
        combine = lambda bulk, increment: (bulk + increment) % 5
        reachable = (0, 1, 2)
        self.assertTrue(bounded_left_recovery_is_unique((0, 1, 2), reachable, combine))
        self.assertEqual(unique_residual(2, 4, reachable, combine), 2)


if __name__ == "__main__":
    unittest.main()
