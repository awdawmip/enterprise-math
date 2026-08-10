import unittest
from fractions import Fraction

from enterprise_math.stage131_chain_tc_spanner import (
    adjacent_chain_edges,
    optimal_one_shortcut_presentation,
)
from enterprise_math.stage131_chain_workload_shortcuts import (
    adjacent_workload_total_cost,
    best_shortcut_set_under_rule_budget,
    one_shortcut_total_cost_closed,
    one_shortcut_weighted_gain,
    optimal_one_shortcut_for_workload,
    optimal_uniform_one_shortcuts,
    single_query_workload,
    uniform_adjacent_expected_depth,
    uniform_all_pairs_workload,
    uniform_one_shortcut_gain_closed,
    workload_budget_curve,
    workload_expected_depth,
    workload_shortcut_point,
)
from enterprise_math.stage131_uniform_workload_shortcut import (
    balanced_positive_three_parts,
    optimal_uniform_one_shortcut_gain,
    optimal_uniform_one_shortcuts_closed,
    uniform_adjacent_total_depth,
    uniform_query_pair_count,
)


class Stage131ChainWorkloadShortcutTests(unittest.TestCase):
    def test_one_shortcut_rectangle_gain_matches_literal_shortest_paths_for_all_small_shortcuts(self):
        for n in range(2, 10):
            weights = {
                (source, target): Fraction((source + 1) * (target + 2), 3)
                for source in range(n)
                for target in range(source + 1, n + 1)
            }
            baseline = adjacent_workload_total_cost(n, weights)
            adjacent = adjacent_chain_edges(n)
            for source in range(n):
                for target in range(source + 2, n + 1):
                    gain = one_shortcut_weighted_gain(n, weights, source, target)
                    point = workload_shortcut_point(
                        n,
                        frozenset((*adjacent, (source, target))),
                        weights,
                    )
                    self.assertEqual(
                        point.total_weighted_depth,
                        baseline - gain,
                    )
                    self.assertEqual(
                        point.total_weighted_depth,
                        one_shortcut_total_cost_closed(n, weights, source, target),
                    )

    def test_single_query_workload_caches_the_exact_query_edge(self):
        n = 20
        weights = single_query_workload(n, 3, 17)
        point = optimal_one_shortcut_for_workload(n, weights)
        self.assertIn((3, 17), point.edges)
        self.assertEqual(point.expected_depth, 1)
        self.assertGreater(point.worst_case_diameter, 1)

    def test_endpoint_query_prefers_direct_endpoint_shortcut_over_worst_case_balanced_shortcut(self):
        n = 30
        workload = single_query_workload(n, 0, n)
        workload_opt = optimal_one_shortcut_for_workload(n, workload)
        worst_opt = optimal_one_shortcut_presentation(n)
        self.assertIn((0, n), workload_opt.edges)
        self.assertEqual(workload_opt.expected_depth, 1)
        self.assertNotIn((0, n), worst_opt.edges)
        self.assertLess(worst_opt.diameter, workload_opt.worst_case_diameter)

    def test_uniform_gain_is_xyz_and_closed_balanced_constructor_matches_bruteforce_optimizer(self):
        for n in range(2, 80):
            brute = optimal_one_shortcut_for_workload(n, uniform_all_pairs_workload(n))
            brute_shortcuts = tuple(
                edge
                for edge in brute.edges
                if edge[1] - edge[0] >= 2
            )
            closed = optimal_uniform_one_shortcuts_closed(n)
            self.assertIn(brute_shortcuts[0], closed)
            self.assertEqual(set(optimal_uniform_one_shortcuts(n)), set(closed))

            best_gain = optimal_uniform_one_shortcut_gain(n)
            for source, target in closed:
                self.assertEqual(
                    uniform_one_shortcut_gain_closed(n, source, target),
                    best_gain,
                )

    def test_balanced_three_parts_differ_by_at_most_one(self):
        for total in range(3, 200):
            triples = balanced_positive_three_parts(total)
            self.assertTrue(triples)
            for triple in triples:
                self.assertEqual(sum(triple), total)
                self.assertLessEqual(max(triple) - min(triple), 1)
            products = {x * y * z for x, y, z in triples}
            self.assertEqual(len(products), 1)

    def test_uniform_adjacent_closed_cost_and_expected_depth(self):
        for n in range(1, 100):
            workload = uniform_all_pairs_workload(n)
            adjacent = adjacent_chain_edges(n)
            self.assertEqual(
                adjacent_workload_total_cost(n, workload),
                uniform_adjacent_total_depth(n),
            )
            self.assertEqual(
                workload_expected_depth(n, adjacent, workload),
                uniform_adjacent_expected_depth(n),
            )
            self.assertEqual(uniform_query_pair_count(n), n * (n + 1) // 2)

    def test_uniform_1024_closed_one_shortcut_expected_depth_is_about_266(self):
        n = 1024
        shortcuts = optimal_uniform_one_shortcuts_closed(n)
        self.assertTrue(shortcuts)
        source, target = shortcuts[0]
        gain = optimal_uniform_one_shortcut_gain(n)
        total = uniform_adjacent_total_depth(n) - gain
        expected = Fraction(total, uniform_query_pair_count(n))
        self.assertEqual(expected, Fraction(34899219, 131200))
        self.assertGreater(expected, 266)
        self.assertLess(expected, 267)
        self.assertEqual(uniform_adjacent_expected_depth(n), 342)
        self.assertEqual(
            uniform_one_shortcut_gain_closed(n, source, target),
            gain,
        )

    def test_exact_small_workload_budget_curve_is_monotone_in_lexicographic_execution_objective(self):
        n = 5
        workload = {
            (0, 5): 20,
            (1, 4): 10,
            (0, 3): 3,
            (2, 5): 2,
        }
        curve = workload_budget_curve(n, workload)
        self.assertTrue(curve)
        self.assertEqual(curve[0].stored_rules, n)
        self.assertEqual(curve[-1].expected_depth, 1)
        self.assertTrue(
            all(
                left.stored_rules < right.stored_rules
                for left, right in zip(curve, curve[1:])
            )
        )
        self.assertTrue(
            all(
                (right.expected_depth, right.worst_case_diameter)
                < (left.expected_depth, left.worst_case_diameter)
                for left, right in zip(curve, curve[1:])
            )
        )
        # Expected workload depth can saturate at1 while later storage still
        # buys a smaller global worst-case continuation diameter.
        self.assertEqual(curve[-2].expected_depth, 1)
        self.assertGreater(curve[-2].worst_case_diameter, curve[-1].worst_case_diameter)

    def test_budget_optimizer_matches_one_shortcut_optimizer_at_n_plus_one_rules(self):
        n = 6
        workload = {
            (0, 6): 10,
            (1, 5): 7,
            (0, 4): 2,
            (3, 6): 1,
        }
        direct = optimal_one_shortcut_for_workload(n, workload)
        budgeted = best_shortcut_set_under_rule_budget(n, workload, n + 1)
        self.assertEqual(direct.total_weighted_depth, budgeted.total_weighted_depth)
        self.assertEqual(direct.expected_depth, budgeted.expected_depth)

    def test_validation(self):
        with self.assertRaises(ValueError):
            single_query_workload(5, 2, 2)
        with self.assertRaises(ValueError):
            optimal_one_shortcut_for_workload(5, {})
        with self.assertRaises(ValueError):
            best_shortcut_set_under_rule_budget(5, {(0, 5): 1}, 4)


if __name__ == "__main__":
    unittest.main()
