import collections
import itertools
import math
import unittest

from enterprise_math.prefix_observation_semantic_ladder import (
    discovery_order_normal_form,
    discovery_order_to_terminal_mask,
)
from enterprise_math.prefix_run_length_normal_form import (
    PrefixRun,
    normalize_prefix_word_to_runs,
)
from enterprise_math.prefix_semantic_fiber_decomposition import (
    discovery_order_literal_fiber_size,
    literal_word_count_from_discovery_fibers,
    literal_word_count_from_terminal_fibers,
    positive_compositions,
    stirling_second_kind,
    terminal_fiber_equals_order_factor,
    terminal_set_literal_fiber_size,
    timing_fiber_maximum,
    timing_fiber_minimum,
    timing_fiber_size_from_durations,
    timing_fibers_sum_to_discovery_fiber,
    timing_form_literal_fiber_size,
)


class PrefixSemanticFiberDecompositionTests(unittest.TestCase):
    def test_stirling_reference_values(self):
        self.assertEqual(stirling_second_kind(0, 0), 1)
        self.assertEqual(stirling_second_kind(3, 2), 3)
        self.assertEqual(stirling_second_kind(5, 2), 15)
        self.assertEqual(stirling_second_kind(5, 3), 25)
        self.assertEqual(stirling_second_kind(6, 3), 90)

    def test_terminal_and_discovery_fibers_match_literal_grouping(self):
        for k in range(1, 5):
            actions = tuple(range(k))
            for horizon in range(1, 7):
                terminal_groups = collections.Counter()
                discovery_groups = collections.Counter()
                for word in itertools.product(actions, repeat=horizon):
                    discovery = discovery_order_normal_form(word, k)
                    terminal = discovery_order_to_terminal_mask(discovery, k)
                    terminal_groups[terminal] += 1
                    discovery_groups[discovery] += 1

                for terminal, count in terminal_groups.items():
                    s = terminal.bit_count()
                    self.assertEqual(
                        count,
                        terminal_set_literal_fiber_size(horizon, s),
                    )
                for discovery, count in discovery_groups.items():
                    s = len(discovery)
                    self.assertEqual(
                        count,
                        discovery_order_literal_fiber_size(horizon, s),
                    )

    def test_timing_fibers_match_literal_grouping_exactly(self):
        for k in range(1, 5):
            actions = tuple(range(k))
            for horizon in range(1, 7):
                timing_groups = collections.Counter(
                    normalize_prefix_word_to_runs(word, k)
                    for word in itertools.product(actions, repeat=horizon)
                )
                for form, count in timing_groups.items():
                    self.assertEqual(
                        count,
                        timing_form_literal_fiber_size(form, k),
                    )

    def test_fixed_duration_fiber_formula(self):
        form = (
            PrefixRun(2, 3),
            PrefixRun(0, 2),
            PrefixRun(3, 4),
        )
        # phase1 stutters1^2, phase2 stutters2^1, phase3 stutters3^3
        self.assertEqual(timing_form_literal_fiber_size(form, 4), 1 * 2 * 27)

    def test_timing_fibers_sum_to_discovery_stirling_number(self):
        for horizon in range(1, 12):
            for s in range(1, horizon + 1):
                self.assertTrue(timing_fibers_sum_to_discovery_fiber(horizon, s))
                self.assertTrue(terminal_fiber_equals_order_factor(horizon, s))

    def test_timing_fiber_minimum_and_maximum_are_sharp(self):
        for horizon in range(1, 12):
            for s in range(1, horizon + 1):
                values = tuple(
                    timing_fiber_size_from_durations(comp)
                    for comp in positive_compositions(horizon, s)
                )
                self.assertEqual(min(values), timing_fiber_minimum(horizon, s))
                self.assertEqual(max(values), timing_fiber_maximum(horizon, s))
                self.assertEqual(min(values), 1)
                self.assertEqual(max(values), s ** (horizon - s))

    def test_full_literal_count_reconstructed_from_each_quotient(self):
        for k in range(1, 8):
            for horizon in range(1, 12):
                expected = k**horizon
                self.assertEqual(
                    literal_word_count_from_terminal_fibers(k, horizon),
                    expected,
                )
                self.assertEqual(
                    literal_word_count_from_discovery_fibers(k, horizon),
                    expected,
                )

    def test_terminal_fiber_is_factorial_times_discovery_fiber(self):
        for horizon in range(1, 15):
            for s in range(1, horizon + 1):
                self.assertEqual(
                    terminal_set_literal_fiber_size(horizon, s),
                    math.factorial(s) * discovery_order_literal_fiber_size(horizon, s),
                )

    def test_positive_composition_count(self):
        for horizon in range(1, 12):
            for s in range(1, horizon + 1):
                self.assertEqual(
                    len(positive_compositions(horizon, s)),
                    math.comb(horizon - 1, s - 1),
                )

    def test_validation(self):
        with self.assertRaises(ValueError):
            terminal_set_literal_fiber_size(0, 1)
        with self.assertRaises(ValueError):
            timing_fiber_maximum(3, 4)
        with self.assertRaises(ValueError):
            timing_form_literal_fiber_size((PrefixRun(0, 1), PrefixRun(0, 1)), 2)


if __name__ == "__main__":
    unittest.main()
