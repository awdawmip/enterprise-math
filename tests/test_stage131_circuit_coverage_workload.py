import unittest
from fractions import Fraction

from enterprise_math.stage131_circuit_coverage_workload import (
    circuit_coverage_indices,
    coverage_benefit,
    coverage_objective_is_monotone_submodular_exhaustive,
    exact_coverage_materialization_small,
    greedy_coverage_materialization,
    marginal_coverage_gain,
    minimal_premise_workload,
    normalize_root_seed_workload,
    positive_minimal_premise_workload_is_modular,
    rooted_circuit_candidates,
)
from enterprise_math.stage131_horn_hyperedge_presentation import balanced_binary_and_tree


class Stage131CircuitCoverageWorkloadTests(unittest.TestCase):
    def test_positive_minimal_premise_workload_is_modular_and_depth_one_is_zero_value(self):
        for height in range(1, 4):
            tree = balanced_binary_and_tree(height)
            self.assertTrue(positive_minimal_premise_workload_is_modular(tree))
            queries = normalize_root_seed_workload(tree, minimal_premise_workload(tree))
            by_seed = {query.seeds: index for index, query in enumerate(queries)}
            for circuit in rooted_circuit_candidates(tree):
                query = queries[by_seed[circuit]]
                covered = circuit_coverage_indices(circuit, queries)
                if query.one_round_saving == 0:
                    self.assertEqual(covered, frozenset())
                else:
                    self.assertEqual(covered, frozenset({by_seed[circuit]}))

    def test_height_two_overlap_makes_candidate_values_strictly_nonadditive(self):
        tree = balanced_binary_and_tree(2)
        p = frozenset({"H1_0", "L2", "L3"})
        q = frozenset({"L0", "L1", "L2", "L3"})
        seed = p | q
        queries = normalize_root_seed_workload(tree, {seed: 1})
        self.assertEqual(queries[0].base_root_depth, 2)
        self.assertEqual(coverage_benefit((p,), queries), 1)
        self.assertEqual(coverage_benefit((q,), queries), 1)
        self.assertEqual(coverage_benefit((p, q), queries), 1)
        self.assertLess(coverage_benefit((p, q), queries), coverage_benefit((p,), queries) + coverage_benefit((q,), queries))

    def test_weighted_coverage_is_monotone_submodular_on_full_height_two_candidate_family(self):
        tree = balanced_binary_and_tree(2)
        workload = {
            frozenset({"H1_0", "H1_1"}): 3,
            frozenset({"H1_0", "L2", "L3"}): 5,
            frozenset({"L0", "L1", "H1_1"}): 4,
            frozenset({"L0", "L1", "L2", "L3"}): 2,
            frozenset({"H1_0", "L0", "L1", "L2", "L3"}): 7,
            frozenset({"H1_0", "H1_1", "L0", "L1"}): 1,
        }
        self.assertTrue(coverage_objective_is_monotone_submodular_exhaustive(tree, workload))

    def test_diminishing_returns_is_strict_on_overlap_example(self):
        tree = balanced_binary_and_tree(2)
        p = frozenset({"H1_0", "L2", "L3"})
        q = frozenset({"L0", "L1", "L2", "L3"})
        queries = normalize_root_seed_workload(tree, {p: 1, q: 1, p | q: 10})
        self.assertGreater(marginal_coverage_gain((), q, queries), marginal_coverage_gain((p,), q, queries))

    def test_greedy_and_exact_agree_on_simple_height_two_workload(self):
        tree = balanced_binary_and_tree(2)
        workload = {
            frozenset({"H1_0", "L2", "L3"}): 10,
            frozenset({"L0", "L1", "H1_1"}): 8,
            frozenset({"L0", "L1", "L2", "L3"}): 6,
            frozenset({"H1_0", "L0", "L1", "L2", "L3"}): 3,
        }
        greedy = greedy_coverage_materialization(tree, workload, 2)
        exact = exact_coverage_materialization_small(tree, workload, 2)
        self.assertEqual(greedy.gross_weighted_round_saving, exact.gross_weighted_round_saving)

    def test_greedy_value_is_monotone_in_budget(self):
        tree = balanced_binary_and_tree(3)
        workload = {circuit: Fraction(index + 1) for index, circuit in enumerate(rooted_circuit_candidates(tree))}
        benefits = [greedy_coverage_materialization(tree, workload, budget).gross_weighted_round_saving for budget in range(1, 8)]
        self.assertTrue(all(left <= right for left, right in zip(benefits, benefits[1:])))

    def test_validation(self):
        tree = balanced_binary_and_tree(2)
        with self.assertRaises(ValueError):
            normalize_root_seed_workload(tree, {})
        with self.assertRaises(ValueError):
            greedy_coverage_materialization(tree, {frozenset({"H1_0", "H1_1"}): 1}, 0)
        tree4 = balanced_binary_and_tree(4)
        with self.assertRaises(ValueError):
            exact_coverage_materialization_small(tree4, minimal_premise_workload(tree4), 2)


if __name__ == "__main__":
    unittest.main()
