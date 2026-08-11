import unittest

from enterprise_math.prefix_semantic_information_decomposition import (
    discovery_semantic_entropy_bits,
    duration_entropy_given_distinct_count_bits,
    expected_discovery_order_information_bits,
    expected_duration_information_bits,
    expected_stutter_provenance_bits,
    literal_word_entropy_bits,
    prefix_semantic_information_report,
    quotient_conditional_literal_entropy_bits,
    terminal_semantic_entropy_bits,
    timing_semantic_entropy_bits,
)


class PrefixSemanticInformationDecompositionTests(unittest.TestCase):
    def assertClose(self, left, right, tol=1e-9):
        self.assertLessEqual(abs(left - right), tol)

    def test_k2_h2_exact_reference(self):
        report = prefix_semantic_information_report(2, 2)
        self.assertClose(report.literal_entropy_bits, 2.0)
        self.assertClose(report.terminal_entropy_bits, 1.5)
        self.assertClose(report.discovery_entropy_bits, 2.0)
        self.assertClose(report.timing_entropy_bits, 2.0)
        self.assertClose(report.discovery_order_information_bits, 0.5)
        self.assertClose(report.duration_information_bits, 0.0)
        self.assertClose(report.stutter_provenance_bits, 0.0)
        self.assertClose(report.decomposition_sum_bits, 2.0)

    def test_duration_and_stutter_information_become_positive(self):
        report = prefix_semantic_information_report(2, 3)
        self.assertGreater(report.discovery_order_information_bits, 0.0)
        self.assertGreater(report.duration_information_bits, 0.0)
        self.assertGreater(report.stutter_provenance_bits, 0.0)
        self.assertLess(report.terminal_entropy_bits, report.discovery_entropy_bits)
        self.assertLess(report.discovery_entropy_bits, report.timing_entropy_bits)
        self.assertLess(report.timing_entropy_bits, report.literal_entropy_bits)

    def test_chain_rule_over_bounded_grid(self):
        for k in range(1, 7):
            for horizon in range(1, 10):
                report = prefix_semantic_information_report(k, horizon)
                self.assertLessEqual(report.terminal_entropy_bits, report.discovery_entropy_bits + 1e-10)
                self.assertLessEqual(report.discovery_entropy_bits, report.timing_entropy_bits + 1e-10)
                self.assertLessEqual(report.timing_entropy_bits, report.literal_entropy_bits + 1e-10)
                self.assertClose(report.decomposition_sum_bits, report.literal_entropy_bits)

    def test_order_information_formula_matches_entropy_gap(self):
        for k in range(1, 7):
            for horizon in range(1, 10):
                expected = expected_discovery_order_information_bits(k, horizon)
                actual = (
                    discovery_semantic_entropy_bits(k, horizon)
                    - terminal_semantic_entropy_bits(k, horizon)
                )
                self.assertClose(expected, actual)

    def test_duration_information_formula_matches_entropy_gap(self):
        for k in range(1, 6):
            for horizon in range(1, 9):
                expected = expected_duration_information_bits(k, horizon)
                actual = (
                    timing_semantic_entropy_bits(k, horizon)
                    - discovery_semantic_entropy_bits(k, horizon)
                )
                self.assertClose(expected, actual)

    def test_stutter_provenance_formula_matches_literal_timing_gap(self):
        for k in range(1, 6):
            for horizon in range(1, 9):
                expected = expected_stutter_provenance_bits(k, horizon)
                actual = (
                    literal_word_entropy_bits(k, horizon)
                    - timing_semantic_entropy_bits(k, horizon)
                )
                self.assertClose(expected, actual)

    def test_quotient_conditional_entropy_is_literal_minus_semantic(self):
        for level, entropy_fn in (
            ("terminal", terminal_semantic_entropy_bits),
            ("discovery", discovery_semantic_entropy_bits),
            ("timing", timing_semantic_entropy_bits),
        ):
            for k in range(1, 5):
                for horizon in range(1, 8):
                    expected = literal_word_entropy_bits(k, horizon) - entropy_fn(k, horizon)
                    self.assertClose(
                        quotient_conditional_literal_entropy_bits(k, horizon, level),
                        expected,
                    )

    def test_one_generator_has_zero_entropy_at_fixed_length(self):
        for horizon in range(1, 50):
            report = prefix_semantic_information_report(1, horizon)
            self.assertClose(report.literal_entropy_bits, 0.0)
            self.assertClose(report.terminal_entropy_bits, 0.0)
            self.assertClose(report.discovery_entropy_bits, 0.0)
            self.assertClose(report.timing_entropy_bits, 0.0)
            self.assertClose(report.decomposition_sum_bits, 0.0)

    def test_duration_entropy_given_s_is_zero_when_no_timing_choice_exists(self):
        for horizon in range(1, 10):
            self.assertClose(duration_entropy_given_distinct_count_bits(horizon, 1), 0.0)
            self.assertClose(
                duration_entropy_given_distinct_count_bits(horizon, horizon),
                0.0,
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            prefix_semantic_information_report(0, 3)
        with self.assertRaises(ValueError):
            quotient_conditional_literal_entropy_bits(2, 3, "bad")


if __name__ == "__main__":
    unittest.main()
