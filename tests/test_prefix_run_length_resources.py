import math
import unittest

from enterprise_math.prefix_run_length_resources import (
    fixed_phase_form_count,
    fixed_phase_information_lower_bound_bits,
    full_materialized_prefix_trace_bits,
    leading_polynomial_coefficient,
    prefix_polynomial_top_difference,
    prefix_run_resource_report,
    prefix_semantic_class_count,
    simple_rle_storage_upper_bound_bits,
    terminal_effect_count_exact_length,
    total_prefix_information_lower_bound_bits,
)


class PrefixRunLengthResourceTests(unittest.TestCase):
    def test_empty_word_report(self):
        report = prefix_run_resource_report(5, 0)
        self.assertEqual(report.literal_words, 1)
        self.assertEqual(report.prefix_semantic_classes, 1)
        self.assertEqual(report.terminal_effects, 1)
        self.assertEqual(report.total_information_lower_bound_bits, 0)
        self.assertEqual(report.materialized_trace_bits, 0)
        self.assertEqual(report.worst_case_simple_rle_bits, 0)

    def test_k5_h100_storage_compression(self):
        report = prefix_run_resource_report(5, 100)
        self.assertEqual(report.materialized_trace_bits, 500)
        self.assertEqual(report.maximum_phases, 5)
        # generator IDs need3 bits; run lengths need7 bits =>5*10.
        self.assertEqual(report.worst_case_simple_rle_bits, 50)
        self.assertGreaterEqual(report.materialized_to_rle_bit_ratio, 10)
        self.assertLessEqual(report.total_information_lower_bound_bits, 50)
        self.assertEqual(report.terminal_effects, 31)

    def test_simple_rle_is_logarithmic_in_h_for_fixed_k(self):
        k = 5
        small = prefix_run_resource_report(k, 100)
        large = prefix_run_resource_report(k, 1_000_000)
        self.assertEqual(small.maximum_phases, large.maximum_phases, 5)
        self.assertEqual(small.materialized_trace_bits, 500)
        self.assertEqual(large.materialized_trace_bits, 5_000_000)
        self.assertLess(large.worst_case_simple_rle_bits, 3 * small.worst_case_simple_rle_bits)

    def test_fixed_phase_information_bound(self):
        count = fixed_phase_form_count(5, 100, 5)
        self.assertEqual(count, math.factorial(5) * math.comb(99, 4))
        lower = fixed_phase_information_lower_bound_bits(5, 100, 5)
        self.assertEqual(lower, (count - 1).bit_length())
        self.assertLessEqual(lower, simple_rle_storage_upper_bound_bits(5, 100, 5))

    def test_post_saturation_class_count_is_degree_k_minus_one_polynomial(self):
        for k in range(1, 8):
            differences = prefix_polynomial_top_difference(
                k,
                start_horizon=k,
                sample_count=2 * k + 5,
            )
            self.assertTrue(differences)
            self.assertEqual(set(differences), {math.factorial(k)})
            self.assertEqual(leading_polynomial_coefficient(k), k)

    def test_growth_sits_between_terminal_and_literal(self):
        for k in range(1, 8):
            for horizon in range(1, 20):
                prefix = prefix_semantic_class_count(k, horizon)
                terminal = terminal_effect_count_exact_length(k, horizon)
                literal = k**horizon
                self.assertLessEqual(terminal, prefix)
                self.assertLessEqual(prefix, literal)

    def test_information_lower_bound_matches_total_class_count(self):
        for k in range(1, 6):
            for horizon in range(0, 20):
                count = prefix_semantic_class_count(k, horizon)
                self.assertEqual(
                    total_prefix_information_lower_bound_bits(k, horizon),
                    0 if count == 1 else (count - 1).bit_length(),
                )

    def test_materialized_trace_bits_formula(self):
        for k in range(1, 10):
            for horizon in range(0, 100):
                self.assertEqual(
                    full_materialized_prefix_trace_bits(k, horizon),
                    k * horizon,
                )

    def test_validation(self):
        with self.assertRaises(ValueError):
            simple_rle_storage_upper_bound_bits(3, 0, 1)
        with self.assertRaises(ValueError):
            prefix_polynomial_top_difference(4, 3, 10)


if __name__ == "__main__":
    unittest.main()
