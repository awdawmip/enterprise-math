import itertools
import unittest

from enterprise_math.prefix_observation_semantic_ladder import (
    compose_discovery_orders,
    discovery_composition_matches_words,
    discovery_left_regular_band_identities_hold,
    discovery_monoid_size,
    discovery_order_from_event_masks,
    discovery_order_normal_form,
    discovery_order_to_terminal_mask,
    discovery_semantic_count_exact_length,
    discovery_to_terminal_is_homomorphism,
    normalize_word_to_all_three_levels,
    prefix_event_masks_from_discovery_order,
    terminal_semantic_count_exact_length,
    timing_semantic_count_exact_length,
    timing_to_discovery_is_homomorphism,
)
from enterprise_math.prefix_run_length_normal_form import (
    normalize_prefix_word_to_runs,
)


class PrefixObservationSemanticLadderTests(unittest.TestCase):
    def test_strict_terminal_vs_discovery_witness(self):
        ab = normalize_word_to_all_three_levels((0, 1), 2)
        ba = normalize_word_to_all_three_levels((1, 0), 2)
        self.assertNotEqual(ab[1], ba[1])
        self.assertEqual(ab[2], ba[2])

    def test_strict_discovery_vs_timing_witness(self):
        aab = normalize_word_to_all_three_levels((0, 0, 1), 2)
        abb = normalize_word_to_all_three_levels((0, 1, 1), 2)
        self.assertNotEqual(aab[0], abb[0])
        self.assertEqual(aab[1], abb[1])
        self.assertEqual(aab[2], abb[2])

    def test_discovery_composition_matches_words_exhaustively(self):
        actions = (0, 1, 2)
        for left_length in range(4):
            for right_length in range(4):
                for left in itertools.product(actions, repeat=left_length):
                    for right in itertools.product(actions, repeat=right_length):
                        self.assertTrue(discovery_composition_matches_words(left, right, 3))

    def test_timing_to_discovery_homomorphism_exhaustively(self):
        actions = (0, 1, 2)
        forms = {
            normalize_prefix_word_to_runs(word, 3)
            for length in range(4)
            for word in itertools.product(actions, repeat=length)
        }
        for left in forms:
            for right in forms:
                self.assertTrue(timing_to_discovery_is_homomorphism(left, right, 3))

    def test_discovery_to_terminal_homomorphism_exhaustively(self):
        actions = (0, 1, 2)
        orders = {
            discovery_order_normal_form(word, 3)
            for length in range(4)
            for word in itertools.product(actions, repeat=length)
        }
        for left in orders:
            for right in orders:
                self.assertTrue(discovery_to_terminal_is_homomorphism(left, right, 3))

    def test_event_mask_encoding_is_exact_for_discovery_order(self):
        for k in range(1, 6):
            for size in range(k + 1):
                for order in itertools.permutations(range(k), size):
                    events = prefix_event_masks_from_discovery_order(order, k)
                    self.assertEqual(discovery_order_from_event_masks(events, k), order)
                    self.assertEqual(
                        discovery_order_to_terminal_mask(order, k),
                        events[-1] if events else 0,
                    )

    def test_left_regular_band_identities(self):
        for k in range(1, 5):
            orders = {
                discovery_order_normal_form(word, k)
                for length in range(k + 1)
                for word in itertools.product(range(k), repeat=length)
            }
            for left in orders:
                for right in orders:
                    self.assertTrue(
                        discovery_left_regular_band_identities_hold(left, right, k)
                    )

    def test_exact_count_ladder_matches_exhaustive_words(self):
        for k in range(1, 5):
            actions = tuple(range(k))
            for length in range(0, 6):
                words = tuple(itertools.product(actions, repeat=length))
                timing = set()
                discovery = set()
                terminal = set()
                for word in words:
                    t, d, m = normalize_word_to_all_three_levels(word, k)
                    timing.add(t)
                    discovery.add(d)
                    terminal.add(m)
                self.assertEqual(len(timing), timing_semantic_count_exact_length(k, length))
                self.assertEqual(len(discovery), discovery_semantic_count_exact_length(k, length))
                self.assertEqual(len(terminal), terminal_semantic_count_exact_length(k, length))
                self.assertLessEqual(len(terminal), len(discovery))
                self.assertLessEqual(len(discovery), len(timing))

    def test_k5_h5_reference_ladder(self):
        self.assertEqual(terminal_semantic_count_exact_length(5, 5), 31)
        self.assertEqual(discovery_semantic_count_exact_length(5, 5), 325)
        self.assertEqual(timing_semantic_count_exact_length(5, 5), 1045)

    def test_discovery_semantics_saturates_but_timing_keeps_growing(self):
        k = 4
        saturated = discovery_monoid_size(k) - 1
        for horizon in (4, 5, 10, 100):
            self.assertEqual(discovery_semantic_count_exact_length(k, horizon), saturated)
        self.assertGreater(
            timing_semantic_count_exact_length(k, 100),
            timing_semantic_count_exact_length(k, 10),
        )

    def test_discovery_monoid_sizes(self):
        self.assertEqual(discovery_monoid_size(1), 2)
        self.assertEqual(discovery_monoid_size(2), 5)
        self.assertEqual(discovery_monoid_size(3), 16)
        self.assertEqual(discovery_monoid_size(4), 65)
        self.assertEqual(discovery_monoid_size(5), 326)

    def test_validation(self):
        with self.assertRaises(ValueError):
            compose_discovery_orders((0, 0), (), 2)
        with self.assertRaises(ValueError):
            discovery_order_from_event_masks((0b11,), 2)


if __name__ == "__main__":
    unittest.main()
