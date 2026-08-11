import itertools
import unittest

from enterprise_math.generator_geodesic_synthesis import (
    compact_generator_incidence_bits,
    explicit_boolean_monoid_state_count,
    geodesic_equals_minimum_cover,
    minimum_cost_or_geodesic,
    same_monoid_geodesic_gap_report,
    shortest_or_geodesic,
)
from enterprise_math.set_cover_formulaic_execution import minimum_cover_size_exact


def brute_weighted_cover(universe_size, sets, costs):
    full = frozenset(range(universe_size))
    best = None
    best_subset = None
    for size in range(len(sets) + 1):
        for selected in itertools.combinations(range(len(sets)), size):
            covered = frozenset().union(*(frozenset(sets[index]) for index in selected)) if selected else frozenset()
            if not full.issubset(covered):
                continue
            cost = sum(float(costs[index]) for index in selected)
            if best is None or cost < best:
                best = cost
                best_subset = selected
    return best, best_subset


class GeneratorGeodesicSynthesisTests(unittest.TestCase):
    def test_named_set_cover_is_target_geodesic(self):
        sets = ({0, 1}, {1, 2}, {2, 3}, {0, 3})
        result = shortest_or_geodesic(4, sets)
        self.assertEqual(result.distance, 2)
        self.assertEqual(result.distance, minimum_cover_size_exact(4, sets))
        self.assertTrue(geodesic_equals_minimum_cover(4, sets))

    def test_exhaustive_three_by_three_cover_instances(self):
        universe = (0, 1, 2)
        checked = 0
        for bits in itertools.product((0, 1), repeat=9):
            sets = []
            cursor = 0
            for _action in range(3):
                subset = set()
                for element in universe:
                    if bits[cursor]:
                        subset.add(element)
                    cursor += 1
                sets.append(frozenset(subset))
            sets = tuple(sets)
            expected = minimum_cover_size_exact(3, sets)
            result = shortest_or_geodesic(3, sets)
            self.assertEqual(result.distance, expected)
            self.assertEqual(result.reachable, expected is not None)
            self.assertTrue(geodesic_equals_minimum_cover(3, sets))
            self.assertLessEqual(result.visited_effect_states, 8)
            checked += 1
        self.assertEqual(checked, 512)

    def test_weighted_geodesic_equals_weighted_cover(self):
        sets = ({0, 1}, {2, 3}, {0, 1, 2, 3})
        for costs in (
            {0: 2, 1: 2, 2: 7},
            {0: 4, 1: 4, 2: 5},
            {0: 0, 1: 3, 2: 10},
        ):
            expected_cost, _subset = brute_weighted_cover(4, sets, costs)
            result = minimum_cost_or_geodesic(4, sets, costs)
            self.assertEqual(result.cost, expected_cost)

    def test_same_monoid_word_metric_depends_on_generator_presentation(self):
        for universe_size in range(2, 10):
            report = same_monoid_geodesic_gap_report(universe_size)
            self.assertEqual(report.semantic_monoid_states, 1 << universe_size)
            self.assertEqual(report.action_count, universe_size + 1)
            self.assertEqual(report.duplicate_catalogue_distance, universe_size)
            self.assertEqual(report.full_action_catalogue_distance, 1)
            self.assertEqual(report.distance_gap, universe_size - 1)

    def test_explicit_monoid_state_space_is_exponential_in_universe_dimension(self):
        # Dense generator incidence is only m*k bits in this proxy, while the
        # explicit OR monoid has 2^m effect states.
        for universe_size in range(2, 16):
            sets = tuple(frozenset({index}) for index in range(universe_size))
            compact = compact_generator_incidence_bits(universe_size, sets)
            expanded = explicit_boolean_monoid_state_count(universe_size)
            self.assertEqual(compact, universe_size * universe_size)
            self.assertEqual(expanded, 1 << universe_size)
        self.assertGreater(explicit_boolean_monoid_state_count(20), 10**6)

    def test_partial_target_geodesic(self):
        sets = ({0, 1}, {1, 2}, {3})
        # Target bits0 and2; need first two generators, bit3 irrelevant.
        result = shortest_or_geodesic(4, sets, target_mask=0b0101)
        self.assertEqual(result.distance, 2)

    def test_unreachable_target(self):
        result = shortest_or_geodesic(3, ({0}, {1}), target_mask=0b111)
        self.assertIsNone(result.distance)
        self.assertFalse(result.reachable)

    def test_validation(self):
        with self.assertRaises(ValueError):
            shortest_or_geodesic(0, ({0},))
        with self.assertRaises(ValueError):
            minimum_cost_or_geodesic(2, ({0},), {0: -1})


if __name__ == "__main__":
    unittest.main()
