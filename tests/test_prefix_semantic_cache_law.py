import math
import unittest

from enterprise_math.prefix_semantic_cache_law import (
    discovery_cache_entries_through_horizon,
    literal_cache_entries_through_horizon,
    prefix_semantic_cache_report,
    saturated_discovery_cache_size,
    saturated_terminal_cache_size,
    terminal_cache_entries_through_horizon,
    timing_cache_entries_by_exact_length_sum,
    timing_cache_entries_through_horizon,
    timing_cache_hockey_stick_identity,
    timing_cache_top_difference,
)


class PrefixSemanticCacheLawTests(unittest.TestCase):
    def test_hockey_stick_closed_form_matches_direct_sum(self):
        for k in range(1, 9):
            for horizon in range(0, 30):
                self.assertTrue(timing_cache_hockey_stick_identity(k, horizon))
                self.assertEqual(
                    timing_cache_entries_through_horizon(k, horizon),
                    timing_cache_entries_by_exact_length_sum(k, horizon),
                )

    def test_k5_h5_reference(self):
        report = prefix_semantic_cache_report(5, 5)
        self.assertEqual(report.literal_entries, 3906)
        self.assertEqual(report.timing_entries, 1546)
        self.assertEqual(report.discovery_entries, 326)
        self.assertEqual(report.terminal_entries, 32)

    def test_k5_h20_reference(self):
        report = prefix_semantic_cache_report(5, 20)
        self.assertEqual(report.literal_entries, 119_209_289_550_781)
        self.assertEqual(report.timing_entries, 2_514_181)
        self.assertEqual(report.discovery_entries, 326)
        self.assertEqual(report.terminal_entries, 32)
        self.assertGreater(report.literal_to_timing_ratio, 10**7)
        self.assertGreater(report.timing_to_discovery_ratio, 7000)

    def test_terminal_and_discovery_caches_saturate(self):
        for k in range(1, 10):
            terminal = saturated_terminal_cache_size(k)
            discovery = saturated_discovery_cache_size(k)
            for horizon in (k, k + 1, 2 * k, 10 * k):
                self.assertEqual(
                    terminal_cache_entries_through_horizon(k, horizon),
                    terminal,
                )
                self.assertEqual(
                    discovery_cache_entries_through_horizon(k, horizon),
                    discovery,
                )

    def test_timing_cache_is_degree_k_polynomial_after_saturation(self):
        for k in range(1, 8):
            differences = timing_cache_top_difference(
                k,
                start_horizon=k,
                sample_count=2 * k + 7,
            )
            self.assertTrue(differences)
            # Leading coefficient1 => k-th finite difference is k!.
            self.assertEqual(set(differences), {math.factorial(k)})

    def test_growth_ordering(self):
        for k in range(1, 8):
            for horizon in range(0, 25):
                literal = literal_cache_entries_through_horizon(k, horizon)
                timing = timing_cache_entries_through_horizon(k, horizon)
                discovery = discovery_cache_entries_through_horizon(k, horizon)
                terminal = terminal_cache_entries_through_horizon(k, horizon)
                self.assertLessEqual(terminal, discovery)
                self.assertLessEqual(discovery, timing)
                self.assertLessEqual(timing, literal)

    def test_k_one_specialization(self):
        # One generator: every exact length has one timing class, so timing cache
        # has H+1 entries including empty identity; discovery/terminal saturate at2.
        for horizon in range(0, 30):
            self.assertEqual(timing_cache_entries_through_horizon(1, horizon), horizon + 1)
            self.assertEqual(literal_cache_entries_through_horizon(1, horizon), horizon + 1)
            self.assertEqual(
                discovery_cache_entries_through_horizon(1, horizon),
                1 if horizon == 0 else 2,
            )
            self.assertEqual(
                terminal_cache_entries_through_horizon(1, horizon),
                1 if horizon == 0 else 2,
            )

    def test_validation(self):
        with self.assertRaises(ValueError):
            prefix_semantic_cache_report(0, 5)
        with self.assertRaises(ValueError):
            timing_cache_top_difference(4, 3, 10)


if __name__ == "__main__":
    unittest.main()
