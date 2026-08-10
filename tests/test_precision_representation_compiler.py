import unittest
from itertools import product

from enterprise_math.precision_representation_compiler import (
    compile_crt_translation_state,
    compile_prime_translation_state,
    composite_modulus,
    crt_compiled_class_count,
    crt_compiler_partition_is_exact,
    prime_compiled_class_count,
    prime_compiled_class_count_by_depth,
    prime_compiler_partition_is_exact,
    prime_incremental_repair_cost,
    prime_repair_excess,
    prime_subgroup_translation_signature,
    prime_translation_group_size,
    translation_depth,
)


class PrecisionRepresentationCompilerTests(unittest.TestCase):
    def test_prime_closed_form_interpolates_between_valuation_and_exact_residue(self):
        for prime in (2, 3, 5):
            for cap in range(1, 5):
                self.assertEqual(prime_compiled_class_count(prime, cap, cap), cap + 1)
                self.assertEqual(prime_compiled_class_count(prime, cap, 0), prime**cap)
                for subgroup_level in range(cap + 1):
                    depth = translation_depth(cap, subgroup_level)
                    self.assertEqual(
                        prime_translation_group_size(prime, cap, subgroup_level),
                        prime**depth,
                    )
                    self.assertEqual(
                        prime_compiled_class_count(prime, cap, subgroup_level),
                        cap - depth + prime**depth,
                    )
                    self.assertEqual(
                        prime_compiled_class_count_by_depth(prime, cap, depth),
                        cap - depth + prime**depth,
                    )

    def test_prime_compiler_partition_matches_full_future_signature(self):
        for prime, max_cap in ((2, 5), (3, 4), (5, 3)):
            for cap in range(1, max_cap + 1):
                for subgroup_level in range(cap + 1):
                    self.assertTrue(
                        prime_compiler_partition_is_exact(prime, cap, subgroup_level)
                    )
                    modulus = prime**cap
                    tokens = {
                        compile_prime_translation_state(
                            residue, prime, cap, subgroup_level
                        )
                        for residue in range(modulus)
                    }
                    signatures = {
                        prime_subgroup_translation_signature(
                            residue, prime, cap, subgroup_level
                        )
                        for residue in range(modulus)
                    }
                    self.assertEqual(
                        len(tokens),
                        prime_compiled_class_count(prime, cap, subgroup_level),
                    )
                    self.assertEqual(len(tokens), len(signatures))

    def test_repair_excess_and_incremental_cost_are_exact(self):
        for prime in (2, 3, 5, 7):
            for depth in range(0, 6):
                self.assertEqual(
                    prime_repair_excess(prime, depth), prime**depth - depth - 1
                )
                self.assertEqual(
                    prime_repair_excess(prime, depth + 1)
                    - prime_repair_excess(prime, depth),
                    prime_incremental_repair_cost(prime, depth),
                )
        self.assertEqual(prime_repair_excess(2, 1), 0)
        self.assertGreater(prime_repair_excess(2, 2), 0)

    def test_binary_first_translation_digit_is_free_at_partition_level(self):
        for cap in range(1, 7):
            baseline = {
                compile_prime_translation_state(residue, 2, cap, cap)
                for residue in range(2**cap)
            }
            first_digit = {
                compile_prime_translation_state(residue, 2, cap, cap - 1)
                for residue in range(2**cap)
            }
            self.assertEqual(len(baseline), len(first_digit))
            self.assertEqual(len(baseline), cap + 1)

    def test_crt_product_compiler_has_product_class_count(self):
        examples = (
            (((2, 2), (3, 1)), (1, 0)),
            (((2, 2), (3, 2)), (2, 1)),
            (((2, 1), (3, 1), (5, 1)), (0, 1, 1)),
        )
        for components, levels in examples:
            self.assertTrue(crt_compiler_partition_is_exact(components, levels))
            modulus = composite_modulus(components)
            tokens = {
                compile_crt_translation_state(residue, components, levels)
                for residue in range(modulus)
            }
            self.assertEqual(len(tokens), crt_compiled_class_count(components, levels))

    def test_small_crt_exhaustion(self):
        for components in (
            ((2, 1), (3, 1)),
            ((2, 2), (3, 1)),
            ((2, 1), (3, 2)),
        ):
            level_ranges = [range(cap + 1) for _, cap in components]
            for levels in product(*level_ranges):
                self.assertTrue(crt_compiler_partition_is_exact(components, levels))

    def test_invalid_inputs_fail_closed(self):
        with self.assertRaises(ValueError):
            prime_compiled_class_count(4, 3, 1)
        with self.assertRaises(ValueError):
            prime_compiled_class_count(2, 3, 4)
        with self.assertRaises(ValueError):
            compile_crt_translation_state(0, ((2, 2), (2, 1)), (1, 1))
        with self.assertRaises(ValueError):
            crt_compiled_class_count(((2, 2), (3, 1)), (1,))


if __name__ == "__main__":
    unittest.main()
