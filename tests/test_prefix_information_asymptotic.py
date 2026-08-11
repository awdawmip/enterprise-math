import math
import unittest

from enterprise_math.prefix_information_asymptotic import (
    discovery_entropy_gap_to_limit_bits,
    discovery_entropy_limit_bits,
    duration_entropy_limit_bits,
    missing_any_generator_union_bound,
    positive_geometric_entropy_bits,
    prefix_information_asymptotic_report,
    stutter_provenance_asymptotic_residual_bits,
    timing_entropy_gap_to_limit_bits,
    timing_entropy_limit_bits,
)


class PrefixInformationAsymptoticTests(unittest.TestCase):
    def assertClose(self, left, right, tol=1e-9):
        self.assertLessEqual(abs(left - right), tol)

    def test_geometric_entropy_reference(self):
        self.assertClose(positive_geometric_entropy_bits(1.0), 0.0)
        self.assertClose(positive_geometric_entropy_bits(0.5), 2.0)

    def test_k_one_limit_is_zero(self):
        self.assertClose(discovery_entropy_limit_bits(1), 0.0)
        self.assertClose(duration_entropy_limit_bits(1), 0.0)
        self.assertClose(timing_entropy_limit_bits(1), 0.0)
        for horizon in (1, 10, 100):
            report = prefix_information_asymptotic_report(1, horizon)
            self.assertClose(report.timing_entropy_bits, 0.0)
            self.assertClose(report.literal_entropy_bits, 0.0)

    def test_k_two_exact_limit_is_three_bits(self):
        self.assertClose(discovery_entropy_limit_bits(2), 1.0)
        self.assertClose(duration_entropy_limit_bits(2), 2.0)
        self.assertClose(timing_entropy_limit_bits(2), 3.0)

        report = prefix_information_asymptotic_report(2, 20)
        self.assertLess(report.terminal_entropy_bits, 0.001)
        self.assertLess(abs(report.discovery_entropy_bits - 1.0), 0.001)
        self.assertLess(abs(report.timing_entropy_bits - 3.0), 0.001)
        self.assertLess(abs(report.stutter_provenance_bits - 17.0), 0.001)

    def test_k_three_limit_components(self):
        discovery = discovery_entropy_limit_bits(3)
        duration = duration_entropy_limit_bits(3)
        timing = timing_entropy_limit_bits(3)
        self.assertClose(discovery, math.log2(math.factorial(3)))
        self.assertClose(timing, discovery + duration)
        self.assertGreater(duration, 0.0)

        report = prefix_information_asymptotic_report(3, 30)
        self.assertLess(abs(report.discovery_entropy_bits - discovery), 0.01)
        self.assertLess(abs(report.timing_entropy_bits - timing), 0.02)
        self.assertLess(report.terminal_entropy_bits, 0.01)

    def test_missing_generator_bound_decays_exponentially(self):
        for k in (2, 3, 5, 10):
            previous = 1.0
            for horizon in (k, 2 * k, 5 * k, 10 * k, 20 * k):
                bound = missing_any_generator_union_bound(k, horizon)
                self.assertLessEqual(bound, previous + 1e-15)
                previous = bound
            self.assertLess(previous, 1e-6)

    def test_finite_entropy_gaps_tend_toward_zero(self):
        # Use k=2 where exact finite computation is cheap even at long horizons.
        for horizon in (10, 20, 40):
            self.assertLess(
                abs(timing_entropy_gap_to_limit_bits(2, horizon)),
                0.1 if horizon == 10 else 0.001,
            )
            self.assertLess(
                abs(discovery_entropy_gap_to_limit_bits(2, horizon)),
                0.1 if horizon == 10 else 0.001,
            )
            self.assertLess(
                abs(stutter_provenance_asymptotic_residual_bits(2, horizon)),
                0.1 if horizon == 10 else 0.001,
            )

    def test_timing_class_count_can_grow_while_entropy_stays_bounded(self):
        # k=2 has exact timing class count 2H for H>=2, while timing entropy ->3.
        from enterprise_math.prefix_observation_semantic_ladder import (
            timing_semantic_count_exact_length,
        )

        small_count = timing_semantic_count_exact_length(2, 10)
        large_count = timing_semantic_count_exact_length(2, 40)
        self.assertEqual(small_count, 20)
        self.assertEqual(large_count, 80)
        small_entropy = prefix_information_asymptotic_report(2, 10).timing_entropy_bits
        large_entropy = prefix_information_asymptotic_report(2, 40).timing_entropy_bits
        self.assertLess(abs(large_entropy - 3.0), abs(small_entropy - 3.0))

    def test_validation(self):
        with self.assertRaises(ValueError):
            positive_geometric_entropy_bits(0.0)
        with self.assertRaises(ValueError):
            timing_entropy_limit_bits(0)


if __name__ == "__main__":
    unittest.main()
