import unittest

from enterprise_math.stage131_chain_jump_presentation import (
    chain_presentation_point,
)
from enterprise_math.stage131_chain_tc_spanner import (
    adjacent_chain_edges,
    brute_force_best_one_shortcut,
    chain_presentation_diameter,
    chain_shortcut_presentation_point,
    exact_chain_tc_spanner_pareto_frontier,
    is_k_tc_spanner_of_chain,
    one_shortcut_diameter_closed,
    one_shortcut_presentation,
    optimal_one_shortcut_diameter,
    optimal_one_shortcut_presentation,
    transitive_chain_edges,
    translation_invariant_frontier_pairs,
    unrestricted_frontier_pairs,
)


class Stage131ChainTcSpannerTests(unittest.TestCase):
    def test_adjacent_and_full_transitive_diameters(self):
        for n in range(1, 30):
            adjacent = adjacent_chain_edges(n)
            self.assertEqual(len(adjacent), n)
            self.assertEqual(chain_presentation_diameter(n, adjacent), n)

            full = transitive_chain_edges(n)
            self.assertEqual(len(full), n * (n + 1) // 2)
            self.assertEqual(chain_presentation_diameter(n, full), 1)
            self.assertTrue(is_k_tc_spanner_of_chain(n, full, 1))

    def test_adjacent_edges_are_forced_by_exact_chain_closure(self):
        with self.assertRaises(ValueError):
            chain_shortcut_presentation_point(
                4,
                {(0, 2), (1, 2), (2, 3), (3, 4)},
            )

    def test_one_shortcut_closed_diameter_matches_graph_for_every_small_edge(self):
        for n in range(2, 60):
            for source in range(n):
                for target in range(source + 2, n + 1):
                    point = one_shortcut_presentation(n, source, target)
                    self.assertEqual(
                        point.diameter,
                        one_shortcut_diameter_closed(n, source, target),
                    )
                    self.assertEqual(point.stored_rules, n + 1)

    def test_optimal_one_shortcut_closed_form_matches_bruteforce(self):
        for n in range(2, 80):
            predicted = optimal_one_shortcut_presentation(n)
            brute = brute_force_best_one_shortcut(n)
            self.assertEqual(
                predicted.diameter,
                optimal_one_shortcut_diameter(n),
            )
            self.assertEqual(predicted.diameter, brute.diameter)
            self.assertEqual(predicted.stored_rules, n + 1)

    def test_exact_small_unrestricted_frontier_pairs(self):
        expected = {
            3: frozenset({(3, 3), (4, 2), (6, 1)}),
            4: frozenset({(4, 4), (5, 3), (6, 2), (10, 1)}),
            5: frozenset({(5, 5), (6, 3), (8, 2), (15, 1)}),
            6: frozenset({(6, 6), (7, 4), (8, 3), (10, 2), (21, 1)}),
        }
        for n, pairs in expected.items():
            self.assertEqual(unrestricted_frontier_pairs(n), pairs)
            frontier = exact_chain_tc_spanner_pareto_frontier(n)
            self.assertEqual(
                frozenset((point.stored_rules, point.diameter) for point in frontier),
                pairs,
            )

    def test_source_dependent_shortcuts_strictly_improve_translation_invariant_frontier_at_n5(self):
        unrestricted = unrestricted_frontier_pairs(5)
        translation = translation_invariant_frontier_pairs(5)
        self.assertIn((6, 3), unrestricted)
        self.assertNotIn((6, 3), translation)
        self.assertIn((6, 4), translation)

        sharp = one_shortcut_presentation(5, 1, 4)
        self.assertEqual((sharp.stored_rules, sharp.diameter), (6, 3))

    def test_n6_unrestricted_frontier_also_strictly_dominates_jump_type_frontier(self):
        unrestricted = unrestricted_frontier_pairs(6)
        translation = translation_invariant_frontier_pairs(6)
        self.assertIn((7, 4), unrestricted)
        self.assertIn((7, 5), translation)
        self.assertIn((8, 3), unrestricted)
        self.assertIn((8, 4), translation)

    def test_one_source_specific_shortcut_beats_same_storage_translation_invariant_choice_on_1024_chain(self):
        n = 1024
        source_specific = optimal_one_shortcut_presentation(n)
        self.assertEqual(source_specific.stored_rules, 1025)
        self.assertEqual(source_specific.diameter, 683)
        self.assertEqual(
            optimal_one_shortcut_diameter(n),
            (2 * n + 1) // 3,
        )

        # The only translation-invariant presentation with exactly one extra
        # positional rule uses jump length n itself: {1,n}.  It helps only the
        # endpoint and leaves x_(n-1) at distance n-1.
        translation = chain_presentation_point(n, (1, n))
        self.assertEqual(translation.stored_rules, 1025)
        self.assertEqual(translation.full_closure_rounds, 1023)
        self.assertLess(source_specific.diameter, translation.full_closure_rounds)

    def test_optimal_one_shortcut_constructive_edge_is_valid(self):
        for n in (2, 3, 5, 10, 100, 1024):
            point = optimal_one_shortcut_presentation(n)
            if n == 1:
                continue
            shortcut = next(edge for edge in point.edges if edge[1] - edge[0] >= 2)
            source, target = shortcut
            d = point.diameter
            self.assertEqual(source, n - d - 1)
            self.assertEqual(target, 2 * n - 2 * d)

    def test_validation(self):
        with self.assertRaises(ValueError):
            one_shortcut_presentation(5, 2, 3)
        with self.assertRaises(ValueError):
            exact_chain_tc_spanner_pareto_frontier(7)


if __name__ == "__main__":
    unittest.main()
