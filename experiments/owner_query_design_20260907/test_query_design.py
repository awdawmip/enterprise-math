"""Exact query-design regression using positive BRC counterexample consumers."""

import copy
from fractions import Fraction
from itertools import combinations
import json
import unittest

from query_design import (ALL_TRIPLES, OPTIMAL_PAIR_COVER, Branch, SignedAxisChart,
                          classify_query_set, minimum_query_plan, observe,
                          raw_marginal_table, verify_counterexample)


def population(records):
    return tuple(Branch(record["label"], tuple(record["coordinate"]), Fraction(record["weight"]))
                 for record in records)


class QueryDesignTests(unittest.TestCase):
    def test_complete_range_and_minimum_plans(self):
        for s in range(12):
            result = minimum_query_plan(s)
            expected = 1 if s == 0 else 2 if s == 1 else 6 if s <= 3 else 20 if s <= 7 else None
            with self.subTest(s=s):
                self.assertEqual(result["global_minimum_table_count"], expected)
                self.assertEqual(result["status"], "GUARANTEED" if s < 8 else "COUNTEREXAMPLE")
                self.assertEqual(result["query_count"], expected if s < 8 else 20)
                self.assertEqual(result["sparsity_premise"], "USER_DECLARED_NOT_VERIFIED_FROM_OBSERVATIONS")
                self.assertEqual(json.loads(json.dumps(result)), result)

    def test_zero_target_and_empty_query_collection(self):
        empty = classify_query_set(0, [])
        self.assertEqual(empty["status"], "COUNTEREXAMPLE")
        self.assertEqual(empty["verification"]["target_support"], 0)
        self.assertEqual(empty["verification"]["competitor_support"], 1)
        for query in ALL_TRIPLES:
            self.assertEqual(classify_query_set(0, [query])["status"], "GUARANTEED")

    def test_bad_proposed_six_groups_and_corrected_cover(self):
        # These were proposed as a hint, and are deliberately not trusted.
        bad_one_based = [(1, 2, 3), (1, 2, 4), (3, 5, 6), (4, 5, 6), (1, 4, 5), (2, 3, 6)]
        bad = [tuple(a - 1 for a in q) for q in bad_one_based]
        result = classify_query_set(2, bad)
        self.assertEqual(result["missing_required_subsets"], [[0, 5], [1, 4], [2, 3]])
        self.assertEqual(result["status"], "COUNTEREXAMPLE")
        self.assertEqual(result["verification"]["target_support"], 2)
        self.assertTrue(all(row["fiber_histograms_equal"] for row in result["verification"]["comparisons"]))
        incidence = [sum(axis in query for query in OPTIMAL_PAIR_COVER) for axis in range(6)]
        self.assertEqual(incidence, [3] * 6)
        pair_counts = {pair: sum(set(pair).issubset(q) for q in OPTIMAL_PAIR_COVER)
                       for pair in combinations(range(6), 2)}
        self.assertTrue(all(count >= 1 for count in pair_counts.values()))
        self.assertEqual({pair for pair, count in pair_counts.items() if count == 2}, {(0, 1), (2, 3), (4, 5)})
        self.assertEqual(classify_query_set(3, OPTIMAL_PAIR_COVER)["status"], "GUARANTEED")

    def test_every_maximal_missing_subset_has_raw_brc_witness(self):
        # 6 singleton + 15 pair + 20 triple omissions: all 41 exact maximal failures.
        cases = 0
        for order, s in ((1, 1), (2, 3), (3, 7)):
            for missing in combinations(range(6), order):
                queries = tuple(q for q in ALL_TRIPLES if not set(missing).issubset(q))
                result = classify_query_set(s, queries)
                with self.subTest(missing=missing, s=s):
                    self.assertEqual(result["status"], "COUNTEREXAMPLE")
                    checked = verify_counterexample(s, queries, result["counterexample"])
                    self.assertTrue(checked["valid"])
                    self.assertEqual(checked["target_support"], 2**(order - 1))
                    self.assertEqual(checked["competitor_support"], 2**(order - 1))
                    self.assertTrue(all(row["fiber_histograms_equal"] for row in checked["comparisons"]))
                    # One full query containing the omitted subset distinguishes it.
                    distinguishing = next(q for q in ALL_TRIPLES if set(missing).issubset(q))
                    left = population(result["counterexample"]["target"])
                    right = population(result["counterexample"]["competitor"])
                    self.assertNotEqual(observe(left, [distinguishing]), observe(right, [distinguishing]))
                cases += 1
        self.assertEqual(cases, 41)

    def test_all_twenty_tables_fail_at_eight_but_four_axis_readout_separates(self):
        result = minimum_query_plan(8)
        left = population(result["counterexample"]["target"])
        right = population(result["counterexample"]["competitor"])
        self.assertEqual(observe(left, ALL_TRIPLES), observe(right, ALL_TRIPLES))
        self.assertNotEqual(raw_marginal_table(left, (0, 1, 2, 3)),
                            raw_marginal_table(right, (0, 1, 2, 3)))
        self.assertEqual(result["verification"]["target_support"], 8)

    def test_general_anchor_signed_frame_and_counterexample_binding(self):
        chart = SignedAxisChart(anchor=(17, -5, 0, 42, -19, 8),
                                permutation=(5, 2, 4, 1, 3, 0), signs=(-1, 1, -1, -1, 1, 1))
        coordinate = (2, -7, 0, 3, -1, 8)
        self.assertEqual(chart.to_chart(chart.to_world(coordinate)), coordinate)
        for s, queries in ((0, []), (1, [(0, 1, 2)]), (3, [(0, 1, 2), (3, 4, 5)]),
                           (7, ALL_TRIPLES[:-1]), (8, ALL_TRIPLES)):
            result = classify_query_set(s, queries, chart=chart)
            self.assertEqual(result["status"], "COUNTEREXAMPLE")
            self.assertTrue(verify_counterexample(s, queries, result["counterexample"], chart=chart)["valid"])
            self.assertFalse(verify_counterexample(s, queries, result["counterexample"])["valid"])

    def test_joint_can3_depth_is_lossless_and_can3_alone_is_not(self):
        left = (Branch("left", (0, 0, 0, 0, 0, 0)),)
        right = (Branch("right", (1, 1, 1, 1, 1, 1)),)
        left_raw, right_raw = observe(left, ALL_TRIPLES), observe(right, ALL_TRIPLES)
        self.assertNotEqual(left_raw, right_raw)
        left_joint = observe(left, ALL_TRIPLES, encoding="can3_depth")
        right_joint = observe(right, ALL_TRIPLES, encoding="can3_depth")
        self.assertNotEqual(left_joint, right_joint)
        for query in ALL_TRIPLES:
            left_visible = {visible: mass for (visible, depth), mass in left_joint[query].items()}
            right_visible = {visible: mass for (visible, depth), mass in right_joint[query].items()}
            self.assertEqual(left_visible, right_visible)
            repaired = {tuple(v + depth for v in visible): mass
                        for (visible, depth), mass in right_joint[query].items()}
            self.assertEqual(repaired, right_raw[query])
        with self.assertRaises(ValueError):
            observe(left, ALL_TRIPLES, encoding="can3_only")

    def test_arbitrary_positive_rational_mass_observation_reuses_existing_consumer(self):
        branches = (Branch("a", (-2, 0, 4, 1, -9, 3), Fraction(2, 7)),
                    Branch("b", (-2, 0, 4, 1, -9, 3), Fraction(5, 7)))
        query = (0, 1, 2)
        self.assertEqual(observe(branches, [query])[query], {(-2, 0, 4): Fraction(1)})
        # Two labels at one Cell are one spatial support, not two support points.
        self.assertEqual(len(raw_marginal_table(branches, tuple(range(6)))), 1)

    def test_sparse_promise_is_not_evidence_from_the_observed_tables(self):
        queries = [(0, 1, 2), (3, 4, 5)]
        declared_one = classify_query_set(1, queries)
        self.assertEqual(declared_one["status"], "GUARANTEED")
        actual_two = classify_query_set(2, queries)
        self.assertEqual(actual_two["status"], "COUNTEREXAMPLE")
        self.assertEqual(actual_two["verification"]["target_support"], 2)
        self.assertEqual(declared_one["sparsity_premise"], "USER_DECLARED_NOT_VERIFIED_FROM_OBSERVATIONS")

    def test_invalid_inputs_and_duplicate_queries(self):
        for s in (-1, True, 1.0):
            with self.assertRaises(ValueError):
                minimum_query_plan(s)
        for queries in ([(0, 1)], [(0, 1, 1)], [(0, 1, 6)], [(False, 1, 2)],
                        [(0, 1, 2), (2, 1, 0)]):
            with self.assertRaises(ValueError):
                classify_query_set(1, queries)
        with self.assertRaises(ValueError):
            SignedAxisChart(permutation=(0, 1, 2, 3, 4, 4))
        with self.assertRaises(ValueError):
            SignedAxisChart(signs=(1, 1, 1, 1, 1, 0))
        with self.assertRaises(ValueError):
            SignedAxisChart(anchor=(0, 0, 0, 0, 0, 0.5))

    def test_tampered_witnesses_and_spatial_equality(self):
        queries = [(0, 1, 2)]
        baseline = classify_query_set(1, queries)["counterexample"]
        changed = copy.deepcopy(baseline)
        changed["competitor"][0]["weight"] = "2/1"
        self.assertFalse(verify_counterexample(1, queries, changed)["valid"])
        changed = copy.deepcopy(baseline)
        changed["competitor"][0]["coordinate"] = changed["target"][0]["coordinate"][:]
        self.assertFalse(verify_counterexample(1, queries, changed)["valid"])
        changed = copy.deepcopy(baseline)
        changed["varying_axes"] = [0]
        self.assertFalse(verify_counterexample(1, queries, changed)["valid"])
        self.assertFalse(verify_counterexample(2, queries, baseline)["valid"])
        self.assertFalse(verify_counterexample(1, ALL_TRIPLES, baseline)["valid"])


if __name__ == "__main__":
    unittest.main()
